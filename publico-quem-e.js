/* Quem É O PÚBLICO DELA, de verdade — não por achismo.
 *
 * Lê os 345 perfis que comentaram nos posts da @izabelalaila
 * (comentarios-izabela.json) e busca, de cada um, o perfil público:
 * seguidores, seguindo, nº de posts, bio e categoria.
 *
 *   node ~/Desktop/mapa-ia-mockups/publico-quem-e.js [quantos]
 *
 * ⚠️ O QUE ISTO MEDE E O QUE NÃO MEDE:
 *    - MEDE: seguidores, bio, categoria, se é conta profissional. Público.
 *    - NÃO MEDE: faturamento, nº de funcionárias. Isso NÃO existe na API.
 *      O que dá pra fazer é ler o SINAL que a própria pessoa escreveu na bio
 *      («equipe», «agende com nossas profissionais», «vagas») e dizer que é
 *      sinal, não censo. A classificação sai num arquivo pra conferir à mão.
 *
 * ⚠️ POR QUE PELA PÁGINA E NÃO PELA API: `/api/v1/users/web_profile_info/`
 *    devolveu **429 em 345 de 345** leituras em 24/10/2026, e continuou em 429
 *    mesmo com recuo de 90s — o corte é por ritmo e dura horas. A página do
 *    perfil (`instagram.com/<user>/`) devolve o mesmo que interessa na
 *    `<meta name="description">`: seguidores, seguindo, posts e a bio.
 *
 * ⚠️ Comentarista NÃO é seguidor. É o subconjunto que se mexe — que é
 *    justamente quem compra num lançamento por comentário. Dito na tela.
 */
const { chromium } = require('/Users/lavoutaliso/ferramentas-visual/node_modules/playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const PERFIL_CHROME = path.join(os.homedir(),
  'Library/Application Support/Google/Chrome/Profile 1/Cookies');
const QUANTOS = Number(process.argv[2] || 140);   // amostra; 345 de uma vez dá 429
const SAIDA = path.join(__dirname, 'publico-izabela.json');

function cookies() {
  const py = `
import browser_cookie3, json, warnings; warnings.filterwarnings('ignore')
out=[]
for dom in ['instagram.com','facebook.com']:
    try:
        for c in browser_cookie3.chrome(cookie_file=${JSON.stringify(PERFIL_CHROME)}, domain_name=dom):
            d = c.domain if c.domain.startswith('.') else '.'+c.domain.lstrip('.')
            out.append({'name':c.name,'value':c.value,'domain':d,'path':c.path or '/',
                        'httpOnly':False,'secure':True,'sameSite':'None',
                        'expires':int(c.expires) if c.expires else -1})
    except Exception: pass
print(json.dumps(out))`;
  return JSON.parse(execFileSync('python3', ['-c', py], { maxBuffer: 8e6 }).toString());
}

(async () => {
  const bruto = JSON.parse(fs.readFileSync(path.join(__dirname, 'comentarios-izabela.json')));
  const quem = new Map();   // usuário → quantos posts dela ele comentou
  for (const k of Object.keys(bruto)) {
    const vistos = new Set();
    for (const c of bruto[k].lista) {
      if (vistos.has(c.u)) continue;        // o mesmo comentário repetido no payload
      vistos.add(c.u);
      quem.set(c.u, (quem.get(c.u) || 0) + 1);
    }
  }
  const lista = [...quem.entries()].sort((a, b) => b[1] - a[1]).slice(0, QUANTOS);
  console.log(`── ${lista.length} perfis para ler ──`);

  const b = await chromium.launch({ headless: true });
  const ctx = await b.newContext({ viewport: { width: 1280, height: 1000 }, locale: 'pt-BR',
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      + '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' });
  await ctx.addCookies(cookies());
  const p = await ctx.newPage();
  await p.goto('https://www.instagram.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await p.waitForTimeout(4000);

  const out = [];
  let erros = 0, seguidas = 0;
  const grava = () => fs.writeFileSync(SAIDA, JSON.stringify({
    colhidoEm: new Date().toISOString(), lidos: out.length, falhas: erros,
    deOndeVeio: 'quem comentou nos 7 posts da @izabelalaila',
    oQueNaoMede: 'faturamento e nº de funcionárias — não existem na API; '
      + 'o sinal de «tem equipe» sai da bio escrita pela própria pessoa',
    perfis: out }, null, 1));
  for (let i = 0; i < lista.length; i++) {
    const [u, vezes] = lista[i];
    let d = null;
    try {
      await p.goto('https://www.instagram.com/' + encodeURIComponent(u) + '/',
        { waitUntil: 'domcontentloaded', timeout: 45000 });
      await p.waitForTimeout(2600);
      d = await p.evaluate(() => {
        const m = document.querySelector('meta[name="description"]');
        if (!m || !m.content) return null;
        const c = m.content;
        /* «6,892 seguidores, 6,161 seguindo, 187 posts — NOME (@user) no Instagram: "BIO"» */
        const num = (re) => {
          const x = c.match(re); if (!x) return null;
          const t = x[1].replace(/[.,]/g, '').trim().toUpperCase();
          if (/^\d+$/.test(t)) return Number(t);
          const n = parseFloat(x[1].replace(',', '.'));
          if (/MI|M$/.test(t)) return Math.round(n * 1e6);
          if (/MIL|K$/.test(t)) return Math.round(n * 1e3);
          return null;
        };
        const nome = (c.match(/—\s*(.+?)\s*\(@/) || [])[1] || '';
        const bio = (c.match(/no Instagram:\s*"([\s\S]*)"\s*$/) || [])[1] || '';
        const corpo = (document.querySelector('header') || document.body).innerText || '';
        return {
          seguidores: num(/([\d.,]+\s*(?:mi|mil|M|K)?)\s*seguidores/i),
          segue: num(/([\d.,]+\s*(?:mi|mil|M|K)?)\s*seguindo/i),
          posts: num(/([\d.,]+\s*(?:mi|mil|M|K)?)\s*posts/i),
          nome, bio,
          /* a bio da meta vem truncada; o header traz o resto quando existe */
          bioCompleta: corpo.replace(/\s+/g, ' ').slice(0, 400),
          privado: /conta.{0,12}privada|This account is private/i.test(corpo),
        };
      });
      if (d && d.seguidores == null) d = null;
    } catch (_) { /* segue */ }
    if (!d) {
      erros++;
      seguidas++;
      /* ⚠️ 345 leituras seguidas deram 429 em TODAS. O Instagram corta por
         ritmo, não por total — o recuo é obrigatório, não educação. */
      if (seguidas >= 3) {
        const espera = Math.min(90, 12 * seguidas);
        console.log(`  … ${seguidas} falhas seguidas, recuando ${espera}s`);
        await p.waitForTimeout(espera * 1000);
        seguidas = 0;
      }
    } else {
      seguidas = 0;
      out.push({ u, comentouEm: vezes, nome: d.nome, seguidores: d.seguidores,
        segue: d.segue, posts: d.posts, bio: d.bio.replace(/\s+/g, ' ').trim(),
        contexto: d.bioCompleta, privado: d.privado });
    }
    if ((i + 1) % 10 === 0) {
      grava();   /* ⚠️ grava parcial: 7 minutos de coleta não podem morrer num 429 */
      console.log(`  ${i + 1}/${lista.length}  lidos:${out.length} falhas:${erros}`);
    }
    await p.waitForTimeout(1500 + Math.floor(Math.random() * 900));
  }

  grava();
  console.log(`✅ ${SAIDA} — ${out.length} perfis lidos, ${erros} falharam`);
  await b.close();
})();
