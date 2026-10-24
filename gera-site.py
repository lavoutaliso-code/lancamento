#!/usr/bin/env python3
"""O SITE DO LANÇAMENTO — a estrutura completa, com agendamento ligado.

  · os 51 posts dela de 05/10 a 23/10, em ordem, dentro das 5 categorias
  · cada um é uma ramificação ① referência → ②②② três ideias → ③ o meu post
  · clicar no + abre o CARD DE AGENDAMENTO: arquivo → feed/dump/reels →
    dia e hora → legenda → agenda de verdade na @izabelalaila

⚠️ O AGENDAMENTO NÃO É MAQUETE. Ele repete o caminho que já estava provado
   no Postador do painel performance (23/10):
     1. sobe o arquivo cru  → POST {API}/painel-midia?perfil=lai&id=&nome=&tipo=
     2. lê o pacote inteiro → GET  {API}/painel-gestao?perfil=lai
     3. acrescenta o item em conteudo.postador e DEVOLVE TUDO
        → POST {API}/painel-gestao  com `base` = a rev lida
     4. a ronda do backend acorda de minuto em minuto e publica

⚠️ POR QUE DEVOLVER O PACOTE INTEIRO: `POST /painel-gestao` grava
   pessoal+conteudo+mapas de uma vez. Mandar só o postador APAGARIA pauta,
   mapa e demanda dela. E `base` é a trava contra sobrescrita: se a rev andou
   entre a leitura e a escrita, o servidor recusa e a tela relê.

⚠️ A HORA É DE BRASÍLIA — o mesmo erro de 3h que já custou 18 cartões
   corrigidos no caixa. O seletor nativo devolve hora local; o item vai com
   o carimbo de Brasília montado à mão.
"""
import base64
import io
import json
import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DIR)
from ideias51 import IDEIAS51   # noqa: E402

POSTS = json.load(open(os.path.join(DIR, 'posts-lancamento.json')))
CAPAS = os.path.join(DIR, 'capas-mariaeduardasv')
try:
    from PIL import Image
except ImportError:
    Image = None

API = 'https://lavou-backend-production.up.railway.app'
PERFIL = 'lai'          # @izabelalaila — medido em /postador/fila
CONTA = '@izabelalaila'

CATS = [
    ('teaser',   1, 'O enigma',           'Diz que vem coisa e não diz o quê. Só pede uma palavra.'),
    ('dor',      2, 'A dor com nome',     'Para de falar de você. Nomeia o problema de quem assiste.'),
    ('amostra',  3, 'A entrega de graça', 'Dá pronto o menor pedaço útil. Quem pega, levanta a mão.'),
    ('evento',   4, 'O ao vivo',          'Tira a audiência do feed e põe num lugar onde ela senta.'),
    ('venda',    5, 'O carrinho aberto',  'Oferta nomeada, prazo curto, cupom por comentário.'),
]
PEDE = {'Oferta', 'Isca', 'Enigma', 'Relógio', 'Evento'}


def b64(code, lado=400):
    f = os.path.join(CAPAS, code + '.jpg')
    if not os.path.exists(f):
        return ''
    if Image:
        im = Image.open(f).convert('RGB')
        im.thumbnail((lado, lado))
        buf = io.BytesIO()
        im.save(buf, 'JPEG', quality=74, optimize=True)
        d = buf.getvalue()
    else:
        d = open(f, 'rb').read()
    return 'data:image/jpeg;base64,' + base64.b64encode(d).decode()


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


for i, p in enumerate(POSTS):
    p['n'] = i
    p['ideias'] = IDEIAS51[i]
    p['capaB64'] = b64(p['code'])
    p['link'] = 'https://www.instagram.com/p/' + p['code'] + '/'
    p['fmt'] = 'reel' if p['tipo'] == 'reel' else 'feed'
    p['pede'] = p['papel'] in PEDE
    p['sid'] = f'p{i:02d}'


def bloco(p, idx_na_cat):
    sid = p['sid']
    fios = ''.join(f'<i class="fio-decl" data-de="rf-{sid}" data-para="op-{sid}-{j}"></i>'
                   for j in (1, 2, 3))
    fios += ''.join(f'<i class="fio-decl" data-de="op-{sid}-{j}" data-para="sl-{sid}"></i>'
                    for j in (1, 2, 3))
    cards = ''.join(
        f'<div class="op" data-no="op-{sid}-{j}" data-mo="{sid}" data-op="{j}">'
        f'<div class="op-l1"><span class="op-n">{j}</span>'
        f'<span class="op-an">{esc(ide)}</span></div>'
        f'<button class="op-use" data-mo="{sid}" data-op="{j}">usar esta</button></div>'
        for j, ide in enumerate(p['ideias'], 1))
    kw = (f'<span class="rf-kw">pede «{esc(p["pedido"])}»</span>'
          if p.get('pedido') else '<span class="rf-kw rf-kw0">não pede nada</span>')
    return (
        f'<div class="mo" data-mo-id="{sid}">{fios}'
        f'<div class="mo-cab"><span class="mo-n">{idx_na_cat}</span>'
        f'<span class="mo-dt">{p["quando"][8:10]}/{p["quando"][5:7]}</span>'
        f'<span class="mo-pa pa-{"s" if p["pede"] else "n"}">{p["papel"]}</span></div>'
        f'<div class="mo-g" data-fmt="{p["fmt"]}">'
        f'<a class="rf" data-no="rf-{sid}" href="{p["link"]}" target="_blank" rel="noopener">'
        f'<img src="{p["capaB64"]}" alt="" loading="lazy">'
        f'<span class="rf-pl"><svg viewBox="0 0 24 24" width="24" height="24">'
        f'<path d="M8 5v14l11-7z" fill="currentColor"/></svg></span>'
        f'<span class="rf-tag">{p["fmt"]}</span></a>'
        f'<div class="opz">{cards}</div>'
        f'<button class="sl-box" data-no="sl-{sid}" data-add="{sid}">'
        f'<span class="sl-mais">+</span><span class="sl-sub">agendar o meu post</span></button>'
        f'<div class="pe pe-ref">{kw}'
        f'<span class="rf-cm">💬 {p["cm"]} · {p["quando"][8:10]}/{p["quando"][5:7]}</span>'
        f'<p class="rf-leg">{esc(p["legenda"][:86])}…</p></div>'
        f'<div class="pe"></div><div class="pe pe-slot" id="est-{sid}"></div>'
        f'</div></div>')


FAIXAS = ''
_vistos = 0
for chave, n, nome, oque in CATS:
    ps = [p for p in POSTS if p['cat'] == chave]
    # ⚠️ categoria vazia é ERRO, não «pula». Foi assim que 20 posts sumiram
    #    da tela sem ninguém ver: o filtro não achava a chave e seguia reto.
    assert ps, f'categoria "{chave}" não casou com nenhum post — chaves no JSON: ' \
               + str(sorted({p["cat"] for p in POSTS}))
    _vistos += len(ps)
    pede = sum(1 for p in ps if p['pede'])
    FAIXAS += (
        f'<section class="fx" id="fx-{chave}">'
        f'<div class="fx-cab"><span class="fx-n">{n}</span>'
        f'<div class="fx-tt"><h3>{nome}</h3><p>{oque}</p></div>'
        f'<span class="fx-j"><b>{len(ps)} posts</b><br>{pede} pedem · {len(ps) - pede} não</span>'
        f'</div><div class="qd"><div class="qd-canvas"><svg class="fios"></svg>'
        + ''.join(bloco(p, i) for i, p in enumerate(ps, 1))
        + '</div></div></section>')


# ════════════════════════════════════════════════════════════════════════
CSS = """
:root{--bg:#F4F4F6;--sup:#FFF;--txt:#1A0A12;--txt2:#7B6B74;--linha:#E4DFE4;
 --rosa:#FF2D87;--marca:#FFE27A;--ok:#1F7A4C;--fio:#C2BBC4;--azul:#0A84FF;
 --W:190px;--gapX:92px;
 --f:-apple-system,'SF Pro Text','Helvetica Neue','Inter',Arial,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--txt);font-family:var(--f);line-height:1.5;
 -webkit-font-smoothing:antialiased}
.topo{position:sticky;top:0;z-index:80;background:rgba(244,244,246,.95);
 backdrop-filter:saturate(180%) blur(16px);border-bottom:1px solid var(--linha);padding:13px 22px}
.topo h1{font-size:18px;font-weight:800;letter-spacing:-.02em}
.topo p{font-size:12.5px;color:var(--txt2);margin-top:3px;max-width:108ch}
.est{display:flex;gap:7px;flex-wrap:wrap;margin-top:9px;align-items:center}
.est span{font-size:11px;font-weight:700;padding:4px 10px;border-radius:8px;
 border:1.5px solid var(--linha);background:var(--sup);color:var(--txt2)}
.est .lig{background:#E8F7EE;border-color:#A8DCBE;color:#15663D}
.est .des{background:#FFF0F4;border-color:#FFC4D8;color:#A3104A}
.wrap{padding:20px 22px 46px}
.nt{font-size:12.5px;color:var(--txt2);margin-top:16px;max-width:92ch}

.fx{margin-bottom:30px}
.fx-cab{display:flex;align-items:center;gap:13px;margin-bottom:11px}
.fx-n{display:grid;place-items:center;width:36px;height:36px;border-radius:50%;flex:none;
 background:var(--rosa);color:#fff;font-size:17px;font-weight:800}
.fx-tt h3{font-size:18px;font-weight:800;letter-spacing:-.02em}
.fx-tt p{font-size:12.5px;color:var(--txt2)}
.fx-j{margin-left:auto;font-size:11px;color:var(--txt2);text-align:right;line-height:1.45}
.fx-j b{font-size:12.5px;color:var(--txt)}

.qd{border:1.6px solid var(--linha);border-radius:16px;position:relative;overflow:auto;
 background:radial-gradient(circle,#DCD8DD 1px,transparent 1px) 0 0/24px 24px,var(--sup)}
.qd-canvas{position:relative;padding:24px 26px;width:max-content;min-width:100%}
svg.fios{position:absolute;left:0;top:0;pointer-events:none;overflow:visible}
.fio-decl{display:none}
.fio{fill:none;stroke:var(--fio);stroke-width:1.8;stroke-linecap:round}
.pino{fill:var(--fio)}

.mo{display:inline-block;vertical-align:top;margin-right:64px}
.mo:last-child{margin-right:0}
.mo-cab{display:flex;align-items:center;gap:8px;margin-bottom:11px}
.mo-n{font-size:11px;font-weight:800;color:#fff;background:var(--rosa);border-radius:6px;
 padding:2px 8px}
.mo-dt{font-size:11.5px;font-weight:700;color:var(--txt2)}
.mo-pa{font-size:10px;font-weight:800;padding:2px 7px;border-radius:5px;text-transform:uppercase;
 letter-spacing:.4px}
.pa-s{background:var(--marca);color:#5B4708}
.pa-n{background:#EDEAE4;color:#6B6258}

.mo-g{display:grid;grid-template-columns:var(--W) auto var(--W);
 column-gap:var(--gapX);row-gap:10px;align-items:center}
.rf,.opz,.sl-box{grid-row:1}
.pe{grid-row:2;align-self:start}
.rf{position:relative;display:block;width:var(--W);border-radius:18px;overflow:hidden;
 background:#E9E5E9;box-shadow:0 4px 14px -8px rgba(0,0,0,.35)}
.mo-g[data-fmt=reel] .rf,.mo-g[data-fmt=reel] .sl-box{aspect-ratio:9/16}
.mo-g[data-fmt=feed] .rf,.mo-g[data-fmt=feed] .sl-box{aspect-ratio:4/5}
.rf img{width:100%;height:100%;object-fit:cover;display:block}
.rf-pl{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:44px;height:44px;
 border-radius:50%;background:rgba(0,0,0,.46);color:#fff;display:grid;place-items:center}
.rf-tag{position:absolute;right:8px;top:8px;font-size:9px;font-weight:800;color:#fff;
 background:rgba(0,0,0,.62);border-radius:5px;padding:2px 7px;text-transform:uppercase}
.pe-ref{width:var(--W)}
.rf-kw{display:inline-block;font-size:10px;font-weight:800;background:var(--marca);
 border-radius:5px;padding:2px 7px}
.rf-kw0{background:#EDEAE4;color:#6B6258}
.rf-cm{display:block;font-size:10.5px;color:var(--txt2);margin-top:4px}
.rf-leg{font-size:11px;color:var(--txt2);margin-top:4px}

.opz{display:flex;flex-direction:column;gap:13px;width:234px}
.op{background:var(--sup);border:1.6px solid var(--linha);border-radius:12px;padding:10px 11px}
.op.on{border-color:var(--ok);box-shadow:0 0 0 2px rgba(31,122,76,.15)}
.op-l1{display:flex;align-items:flex-start;gap:7px}
.op-n{font-size:10px;font-weight:800;color:#fff;background:var(--txt);border-radius:5px;
 padding:1px 6px;flex:none;margin-top:1px}
.op-an{font-size:12px;font-weight:600;line-height:1.35}
.op-use{font:inherit;font-size:10.5px;font-weight:700;padding:4px 10px;margin-top:8px;
 cursor:pointer;border:1.5px solid var(--linha);border-radius:7px;background:transparent;
 color:var(--txt2)}
.op.on .op-use{background:var(--ok);color:#fff;border-color:var(--ok)}

.sl-box{width:var(--W);border:2.6px dashed #B4ADB7;border-radius:18px;background:#FBFAFB;
 cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;
 gap:9px;padding:12px;font:inherit}
.sl-box:hover{border-color:var(--rosa);background:#FFF5FA}
.sl-mais{width:40px;height:40px;border-radius:50%;background:var(--marca);
 border:2px solid var(--txt);display:grid;place-items:center;font-size:23px;line-height:1}
.sl-box:hover .sl-mais{background:var(--rosa);color:#fff;border-color:var(--rosa)}
.sl-sub{font-size:10.5px;color:var(--txt2);text-align:center;line-height:1.35}
.pe-slot{width:var(--W);font-size:10.5px}
.mo-g.agendado .sl-box{border-style:solid;border-color:var(--ok);background:#F2FBF6}
.mo-g.agendado .sl-mais{background:var(--ok);color:#fff;border-color:var(--ok)}
.ag-ok{display:block;color:var(--ok);font-weight:700}
.ag-er{display:block;color:#A3104A;font-weight:700}

/* ══ O CARD DE AGENDAMENTO — padrão Apple ═══════════════════════════════ */
.vu{position:fixed;inset:0;z-index:200;background:rgba(0,0,0,.34);
 backdrop-filter:blur(3px);display:grid;place-items:center;padding:20px}
.vu[hidden]{display:none}
.cd{width:min(460px,100%);max-height:92vh;overflow:auto;background:rgba(255,255,255,.96);
 backdrop-filter:saturate(180%) blur(20px);border-radius:20px;
 box-shadow:0 28px 70px -18px rgba(0,0,0,.4);padding:0;overscroll-behavior:contain}
.cd-cab{padding:18px 22px 12px;text-align:center;border-bottom:.5px solid rgba(0,0,0,.1)}
.cd-cab h3{font-size:17px;font-weight:700;letter-spacing:-.01em}
.cd-cab p{font-size:12.5px;color:var(--txt2);margin-top:2px}
.cd-cp{padding:4px 22px 18px}
.gr{border-bottom:.5px solid rgba(0,0,0,.08);padding:13px 0}
.gr:last-of-type{border-bottom:none}
.gr-t{font-size:11px;font-weight:700;color:var(--txt2);text-transform:uppercase;
 letter-spacing:.6px;margin-bottom:8px}
.seg{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;background:rgba(118,118,128,.12);
 border-radius:9px;padding:2px}
.seg button{font:inherit;font-size:13px;font-weight:600;padding:7px 4px;cursor:pointer;
 border:none;border-radius:7px;background:transparent;color:var(--txt)}
.seg button.on{background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.12)}
.seg small{display:block;font-size:9.5px;font-weight:500;color:var(--txt2);margin-top:1px}
.lin{display:flex;gap:9px}
.lin input{flex:1;font:inherit;font-size:15px;padding:10px 11px;border:none;border-radius:10px;
 background:rgba(118,118,128,.12);color:var(--txt)}
.cd textarea{width:100%;font:inherit;font-size:14px;padding:11px;border:none;border-radius:10px;
 background:rgba(118,118,128,.12);min-height:92px;resize:vertical;line-height:1.45}
.arq{display:flex;align-items:center;gap:11px;padding:11px;border-radius:12px;
 background:rgba(118,118,128,.09);cursor:pointer}
.arq-ic{width:42px;height:42px;border-radius:10px;background:var(--marca);display:grid;
 place-items:center;font-size:20px;flex:none;overflow:hidden}
.arq-ic img{width:100%;height:100%;object-fit:cover}
.arq-tx{font-size:13.5px;font-weight:600;min-width:0}
.arq-tx small{display:block;font-size:11.5px;font-weight:400;color:var(--txt2);
 white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.barra{height:4px;border-radius:2px;background:rgba(118,118,128,.18);margin-top:7px;
 overflow:hidden}
.barra i{display:block;height:100%;background:var(--azul);width:0;transition:width .2s}
.cd-pe{display:grid;gap:8px;padding:0 22px 20px}
.bt{font:inherit;font-size:16px;font-weight:600;padding:13px;cursor:pointer;border:none;
 border-radius:13px}
.bt-ok{background:var(--azul);color:#fff}
.bt-ok:disabled{opacity:.42;cursor:not-allowed}
.bt-no{background:rgba(118,118,128,.12);color:var(--azul)}
.cd-av{font-size:11.5px;color:var(--txt2);text-align:center;padding:0 22px 8px;line-height:1.45}
.cd-er{font-size:12.5px;color:#A3104A;font-weight:600;text-align:center;padding:0 22px 8px}

@media(max-width:1500px){:root{--gapX:76px;--W:178px}.opz{width:220px}.mo{margin-right:54px}}
@media(max-width:1250px){:root{--gapX:58px;--W:162px}.opz{width:206px}.mo{margin-right:44px}}
"""

JS = r"""
/* ══ fios medidos: a ponta nasce da borda real ══════════════════════════ */
function pts(el,lado,wrap){var r=el.getBoundingClientRect(),w=wrap.getBoundingClientRect();
  var x=r.left-w.left,y=r.top-w.top;
  return lado==='dir'?[x+r.width,y+r.height/2]:[x,y+r.height/2];}
function curva(a,b){var dx=Math.max(20,Math.abs(b[0]-a[0])*0.5);
  return 'M'+a[0]+' '+a[1]+' C'+(a[0]+dx)+' '+a[1]+' '+(b[0]-dx)+' '+b[1]+' '+b[0]+' '+b[1];}
function desenha(qd){var wrap=qd.querySelector('.qd-canvas'),svg=qd.querySelector('svg.fios');
  if(!wrap||!svg)return; var W=wrap.scrollWidth,H=wrap.scrollHeight;
  svg.setAttribute('width',W);svg.setAttribute('height',H);
  svg.setAttribute('viewBox','0 0 '+W+' '+H);
  var out='';
  qd.querySelectorAll('[data-de]').forEach(function(f){
    var A=qd.querySelector('[data-no="'+f.dataset.de+'"]'),B=qd.querySelector('[data-no="'+f.dataset.para+'"]');
    if(!A||!B)return;
    var a=pts(A,'dir',wrap),b=pts(B,'esq',wrap);
    out+='<path class="fio" d="'+curva(a,b)+'"/><circle class="pino" cx="'+a[0]+'" cy="'+a[1]+
      '" r="2.8"/><circle class="pino" cx="'+b[0]+'" cy="'+b[1]+'" r="2.8"/>';});
  svg.innerHTML=out;}
function todosOsFios(){document.querySelectorAll('.qd').forEach(desenha);}
addEventListener('resize',todosOsFios); addEventListener('load',todosOsFios);

(function(){
 var API='__API__', PERFIL='__PERFIL__';

 /* ── escolher a ideia ──────────────────────────────────────────────── */
 var ESC='lan-escolha';
 function lerE(){try{return JSON.parse(localStorage.getItem(ESC))||{}}catch(e){return {}}}
 function pintaE(){var d=lerE();document.querySelectorAll('.op').forEach(function(o){
   o.classList.toggle('on',d[o.dataset.mo]===o.dataset.op);});}
 document.addEventListener('click',function(ev){var u=ev.target.closest('.op-use');if(!u)return;
   var d=lerE();d[u.dataset.mo]=u.dataset.op;
   try{localStorage.setItem(ESC,JSON.stringify(d))}catch(e){}
   pintaE();});

 /* ══ O CARD DE AGENDAMENTO ════════════════════════════════════════════ */
 var vu=document.getElementById('vu'), ALVO=null, ARQ=null, TIPO='feed';
 var el={arq:document.getElementById('cd-arq'),ic:document.getElementById('cd-ic'),
   nome:document.getElementById('cd-nome'),sub:document.getElementById('cd-sub'),
   barra:document.getElementById('cd-barra'),dia:document.getElementById('cd-dia'),
   hora:document.getElementById('cd-hora'),leg:document.getElementById('cd-leg'),
   ok:document.getElementById('cd-ok'),er:document.getElementById('cd-er'),
   file:document.getElementById('cd-file'),tit:document.getElementById('cd-tit')};

 function abreCard(sid){
   ALVO=sid; ARQ=null; TIPO='feed'; el.er.textContent='';
   el.ic.innerHTML='📎'; el.nome.textContent='Escolher arquivo';
   el.sub.textContent='foto ou vídeo do seu celular';
   el.barra.style.width='0'; el.leg.value=''; el.file.value='';
   document.querySelectorAll('#cd-seg button').forEach(function(b){
     b.classList.toggle('on',b.dataset.t==='feed');});
   var mo=document.querySelector('[data-mo-id="'+sid+'"]');
   el.tit.textContent='Post '+(mo?mo.querySelector('.mo-dt').textContent:'')+' · '+
     (mo?mo.querySelector('.mo-pa').textContent:'');
   /* sugere amanhã às 9h, hora de Brasília */
   var d=new Date(Date.now()+864e5);
   el.dia.value=d.toISOString().slice(0,10); el.hora.value='09:00';
   vu.hidden=false; checa();
 }
 function fecha(){vu.hidden=true;}
 function checa(){el.ok.disabled=!(ARQ&&el.dia.value&&el.hora.value);}

 document.addEventListener('click',function(ev){
   var b=ev.target.closest('.sl-box'); if(b){abreCard(b.dataset.add);return;}
   if(ev.target.id==='cd-nao'||ev.target===vu){fecha();return;}
   var t=ev.target.closest('#cd-seg button');
   if(t){TIPO=t.dataset.t;
     document.querySelectorAll('#cd-seg button').forEach(function(x){
       x.classList.toggle('on',x===t);}); return;}
   if(ev.target.closest('#cd-arq')) el.file.click();
 });
 ['input','change'].forEach(function(e){
   el.dia.addEventListener(e,checa); el.hora.addEventListener(e,checa);});
 el.file.addEventListener('change',function(){
   var f=el.file.files&&el.file.files[0]; if(!f)return;
   ARQ=f; el.nome.textContent=f.name;
   el.sub.textContent=(f.type||'arquivo')+' · '+(f.size/1048576).toFixed(1)+' MB';
   if(/^image\//.test(f.type)){var u=URL.createObjectURL(f);
     el.ic.innerHTML='<img src="'+u+'" alt="">';}
   else el.ic.innerHTML='🎬';
   if(/^video\//.test(f.type)&&TIPO==='feed'){
     TIPO='reels';document.querySelectorAll('#cd-seg button').forEach(function(x){
       x.classList.toggle('on',x.dataset.t==='reels');});}
   checa();});

 /* ⚠️ BRASÍLIA. O seletor devolve a hora local do aparelho; o postador
    compara com o relógio de Brasília. Montar o carimbo à mão é o que evita
    repetir o erro de 3 horas que já custou 18 cartões no caixa. */
 function isoBrasilia(dia,hora){ return dia+'T'+hora+':00-03:00'; }

 function sobeArquivo(mid,arq,aoAndar){
   return new Promise(function(ok){
     var q='?perfil='+encodeURIComponent(PERFIL)+'&id='+encodeURIComponent(mid)+
           '&nome='+encodeURIComponent(arq.name||mid)+'&tipo='+encodeURIComponent(arq.type||'');
     var x=new XMLHttpRequest();
     x.open('POST',API+'/painel-midia'+q,true);
     x.setRequestHeader('Content-Type','application/octet-stream');
     x.timeout=20*60*1000;
     if(x.upload)x.upload.onprogress=function(e){
       if(e.lengthComputable)aoAndar(Math.round(e.loaded/e.total*100));};
     x.onload=function(){try{ok(JSON.parse(x.responseText))}catch(e){ok({ok:false,motivo:'resposta'})}};
     x.onerror=function(){ok({ok:false,motivo:'sem_rede'})};
     x.ontimeout=function(){ok({ok:false,motivo:'demorou'})};
     x.send(arq);});
 }

 /* ⚠️ lê o pacote INTEIRO, acrescenta, devolve tudo. Mandar só o postador
    apagaria pauta, mapa e demanda dela. `base` é a trava contra sobrescrita. */
 async function enfileira(item){
   for(var tent=0;tent<3;tent++){
     var r=await fetch(API+'/painel-gestao?perfil='+PERFIL).then(function(x){return x.json()});
     if(!r||!r.ok) return {ok:false,motivo:'nao_li_o_pacote'};
     var d=r.dados||{}, conteudo=d.conteudo||{};
     var lista=Array.isArray(conteudo.postador)?conteudo.postador.slice():[];
     lista=lista.filter(function(x){return x && x.id!==item.id});
     lista.push(item);
     conteudo.postador=lista;
     var g=await fetch(API+'/painel-gestao',{method:'POST',
       headers:{'Content-Type':'application/json'},
       body:JSON.stringify({perfil:PERFIL,base:r.rev||0,
         pessoal:d.pessoal||null,conteudo:conteudo,mapas:d.mapas||null})})
       .then(function(x){return x.json()});
     if(g&&g.ok) return {ok:true,rev:g.rev};
     if(g&&g.motivo==='desatualizado') continue;   /* alguém gravou no meio: relê */
     return {ok:false,motivo:(g&&g.motivo)||'recusado'};
   }
   return {ok:false,motivo:'desatualizado_3x'};
 }

 var AG='lan-agendado';
 function lerA(){try{return JSON.parse(localStorage.getItem(AG))||{}}catch(e){return {}}}
 function pintaA(){var d=lerA();
   document.querySelectorAll('.mo').forEach(function(mo){
     var sid=mo.dataset.moId, v=d[sid], g=mo.querySelector('.mo-g'),
         est=document.getElementById('est-'+sid), box=mo.querySelector('.sl-box');
     g.classList.toggle('agendado',!!v);
     if(v){box.querySelector('.sl-mais').textContent='✓';
       box.querySelector('.sl-sub').textContent=v.tipo+' · '+v.quandoTxt;
       est.innerHTML='<span class="ag-ok">agendado ✓</span>';}
     else{box.querySelector('.sl-mais').textContent='+';
       box.querySelector('.sl-sub').textContent='agendar o meu post'; est.innerHTML='';}});}

 el.ok.addEventListener('click',async function(){
   if(!ARQ||!ALVO)return;
   el.ok.disabled=true; el.er.textContent=''; el.ok.textContent='Subindo o arquivo…';
   var mid='m'+Date.now()+Math.random().toString(36).slice(2,6);
   var up=await sobeArquivo(mid,ARQ,function(p){el.barra.style.width=p+'%';});
   if(!up||!up.ok){el.er.textContent='O arquivo não subiu ('+((up&&up.motivo)||'erro')+').';
     el.ok.textContent='Agendar';el.ok.disabled=false;return;}
   el.ok.textContent='Agendando…';
   var quando=isoBrasilia(el.dia.value,el.hora.value);
   var item={id:'lan'+Date.now()+Math.random().toString(36).slice(2,5),
     tipo:TIPO==='feed'?'feed':(TIPO==='dump'?'dump':'reels'),
     perfil:PERFIL, quando:quando, criado:Date.now(),
     legenda:el.leg.value||'',
     partes:[{mid:mid,nome:ARQ.name||'',tipo:ARQ.type||'',mup:1}],
     origem:'site-lancamento', passo:ALVO};
   var g=await enfileira(item);
   if(!g.ok){el.er.textContent='Não consegui agendar ('+g.motivo+'). Tente de novo.';
     el.ok.textContent='Agendar';el.ok.disabled=false;return;}
   var d=lerA();
   d[ALVO]={tipo:item.tipo,quando:quando,
     quandoTxt:el.dia.value.slice(8)+'/'+el.dia.value.slice(5,7)+' '+el.hora.value,
     id:item.id,mid:mid};
   try{localStorage.setItem(AG,JSON.stringify(d))}catch(e){}
   el.ok.textContent='Agendar'; el.ok.disabled=false;
   fecha(); pintaA(); requestAnimationFrame(todosOsFios);
 });

 /* ── o estado do motor, dito na cara ──────────────────────────────── */
 fetch(API+'/postador/fila').then(function(r){return r.json()}).then(function(d){
   var e=document.getElementById('sinal');
   if(!d||!d.ok){e.innerHTML='<span class="des">servidor não respondeu</span>';return;}
   var n=((d.fila||{})[PERFIL]||[]).length;
   e.innerHTML='<span class="'+(d.relogio?'lig':'des')+'">'+
     (d.relogio?'relógio ligado — publica sozinho':'relógio DESLIGADO')+'</span>'+
     '<span>conta: '+(((d.conta||{})[PERFIL]||{}).nome||PERFIL)+'</span>'+
     '<span>'+n+' na fila</span>';
 }).catch(function(){
   document.getElementById('sinal').innerHTML='<span class="des">sem conexão com o servidor</span>';});

 pintaE(); pintaA();
 requestAnimationFrame(todosOsFios); setTimeout(todosOsFios,340);
})();
""".replace('__API__', API).replace('__PERFIL__', PERFIL)

CARD = f"""
<div class="vu" id="vu" hidden>
 <div class="cd" role="dialog" aria-modal="true">
  <div class="cd-cab"><h3>Agendar post</h3><p id="cd-tit">no {CONTA}</p></div>
  <div class="cd-cp">
   <div class="gr"><div class="gr-t">O arquivo</div>
    <div class="arq" id="cd-arq"><span class="arq-ic" id="cd-ic">📎</span>
     <span class="arq-tx"><span id="cd-nome">Escolher arquivo</span>
      <small id="cd-sub">foto ou vídeo do seu celular</small></span></div>
    <div class="barra"><i id="cd-barra"></i></div>
    <input type="file" id="cd-file" accept="image/*,video/*" hidden></div>
   <div class="gr"><div class="gr-t">Formato</div>
    <div class="seg" id="cd-seg">
     <button data-t="feed" class="on">Feed<small>foto única</small></button>
     <button data-t="dump">Dump<small>carrossel</small></button>
     <button data-t="reels">Reels<small>vídeo</small></button></div></div>
   <div class="gr"><div class="gr-t">Quando (horário de Brasília)</div>
    <div class="lin"><input type="date" id="cd-dia"><input type="time" id="cd-hora"></div></div>
   <div class="gr"><div class="gr-t">Legenda</div>
    <textarea id="cd-leg" placeholder="a legenda que vai com o post…"></textarea></div>
  </div>
  <p class="cd-er" id="cd-er"></p>
  <p class="cd-av">Ao agendar, o post entra na fila do seu Instagram e o servidor
   publica sozinho na hora marcada.</p>
  <div class="cd-pe"><button class="bt bt-ok" id="cd-ok" disabled>Agendar</button>
   <button class="bt bt-no" id="cd-nao">Cancelar</button></div>
 </div></div>"""

n_pede = sum(1 for p in POSTS if p['pede'])
HTML = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lançamento · a estrutura</title>
<meta name="theme-color" content="#F4F4F6">
<style>{CSS}</style></head><body>
<div class="topo">
 <h1>Lançamento — a estrutura completa</h1>
 <p>Os <b>{len(POSTS)} posts</b> da @mariaeduardasv de 05/10 a 23/10, na ordem,
  dentro das 5 categorias ({n_pede} pedem alguma coisa, {len(POSTS) - n_pede} não pedem nada).
  Cada um é uma ramificação <b>① referência → ②②② três ideias → ③ o meu post</b>.
  Clicar no <b>+</b> agenda o post de verdade no {CONTA}.</p>
 <div class="est" id="sinal"><span>consultando o servidor…</span></div>
</div>
<div class="wrap">
{FAIXAS}
 <p class="nt">⚠️ <b>A dor é hipótese</b> («a cliente vem uma vez e some»). As
  {len(POSTS) * 3} ideias são adaptações pro seu nicho — e toda palavra-chave que for
  pro ar precisa nascer ligada a um funil que mede.</p>
</div>
{CARD}
<script>{JS}</script></body></html>"""

assert _vistos == len(POSTS), f'{len(POSTS) - _vistos} posts ficaram de fora das categorias'
saida = os.path.join(DIR, 'index.html')
open(saida, 'w').write(HTML)
print(f'✅ {saida}  ({len(HTML.encode()) / 1e6:.2f} MB · {len(POSTS)} posts · {len(POSTS) * 3} ideias)')
