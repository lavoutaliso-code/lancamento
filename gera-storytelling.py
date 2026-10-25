#!/usr/bin/env python3
"""A página das três histórias — pra ela escolher ANTES de refazer as copies."""
import os, sys
DIR = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, DIR)
from storytelling_fda import HISTORIAS, ATOS   # noqa: E402

ATO = {a[0]: a for a in ATOS}


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def bloco(h):
    atos = ''
    for chave, titulo, oque, porque in h['atos']:
        _, nome, dias, posts, cm = ATO[chave]
        atos += (
            f'<div class="at">'
            f'<div class="at-b"><span class="at-d">{dias} dia{"s" if dias > 1 else ""}</span>'
            f'<span class="at-p">{posts} posts</span></div>'
            f'<div class="at-c"><div class="at-l1"><h4>{esc(titulo)}</h4>'
            f'<span class="at-og">{esc(nome)}</span></div>'
            f'<div class="at-tx"><p class="at-o">{esc(oque)}</p>'
            f'<p class="at-q"><b>por quê:</b> {esc(porque)}</p></div></div></div>')
    jg = ''.join(f'<li><q>{esc(t)}</q><small>{esc(u)}</small></li>' for t, u in h['jargoes'])
    return (
        f'<section class="hi{" apv" if h["id"] == "A" else ""}" id="h{h["id"]}" '
        f'style="--acc:{h["acc"]};--cab:{h["cor"]}">'
        f'<header class="hi-cab"><span class="hi-id">OPÇÃO {h["id"]}'
        + ('  ·  ✅ APROVADA' if h['id'] == 'A' else '') + '</span>'
        f'<h2>{esc(h["nome"])}</h2><p class="hi-sub">{esc(h["sub"])}</p>'
        f'<p class="hi-log">{esc(h["log"])}</p></header>'
        f'<div class="hi-ft">'
        f'<div><span>quem é o protagonista</span><b>{esc(h["quem"])}</b></div>'
        f'<div><span>em que tempo</span><b>{esc(h["tempo"])}</b></div>'
        f'<div><span>o que segura a audiência</span><b>{esc(h["gancho"])}</b></div></div>'
        f'<h3 class="hi-h3">como os 19 dias se contam</h3>'
        f'<div class="ats">{atos}</div>'
        f'<div class="hi-fim">'
        f'<div class="bx"><h3>os jargões desta história</h3><ul class="jg">{jg}</ul></div>'
        f'<div class="bx"><h3>onde entra o enigma que você desenhou</h3>'
        f'<p>{esc(h["enigma"])}</p></div>'
        f'<div class="bx bx2"><h3>o que ela pede de você</h3><p>{esc(h["pede"])}</p></div>'
        f'<div class="bx bx3"><h3>o risco</h3><p>{esc(h["risco"])}</p></div>'
        f'</div></section>')


CSS = """
:root{--bg:#0D0D10;--sup:#16161B;--txt:#F6F3F8;--txt2:#9C94A3;--linha:#282831;
 --f:-apple-system,BlinkMacSystemFont,system-ui,'SF Pro Text','Helvetica Neue',Arial,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--txt);font-family:var(--f);line-height:1.55;
 -webkit-font-smoothing:antialiased}
.w{max-width:1120px;margin:0 auto;padding:40px 22px 90px}
.selo{display:inline-block;font-size:11px;font-weight:800;letter-spacing:2px;color:#FF2D87;
 border:1.5px solid #FF2D87;border-radius:7px;padding:4px 11px}
h1{font-size:clamp(30px,5vw,46px);font-weight:800;letter-spacing:-.034em;line-height:1.05;
 margin:13px 0 12px}
.int{font-size:15px;color:var(--txt2);max-width:72ch}
.int b{color:var(--txt)}
.reg{display:flex;gap:9px;flex-wrap:wrap;margin-top:18px}
.reg i{font-style:normal;font-size:11.5px;font-weight:700;color:var(--txt2);
 background:var(--sup);border:1px solid var(--linha);border-radius:8px;padding:5px 11px}
.reg i b{color:var(--txt)}

.hi{margin-top:46px;border:1px solid var(--linha);border-radius:22px;overflow:hidden;
 background:var(--sup)}
.hi.apv{border:2px solid var(--acc);box-shadow:0 0 0 5px rgba(255,45,135,.09)}
.hi:not(.apv){opacity:.62}
.hi:not(.apv):hover{opacity:1}
.hi-cab{background:var(--cab);padding:26px 28px 24px;border-bottom:3px solid var(--acc)}
.hi-id{font-size:10.5px;font-weight:800;letter-spacing:2px;color:var(--acc)}
.hi-cab h2{font-size:clamp(25px,4vw,36px);font-weight:800;letter-spacing:-.03em;
 line-height:1.04;margin-top:7px}
.hi-sub{font-size:13.5px;color:var(--txt2);margin-top:5px}
.hi-log{font-size:16.5px;margin-top:15px;max-width:60ch;border-left:3px solid var(--acc);
 padding-left:14px}
.hi-ft{display:grid;grid-template-columns:repeat(auto-fit,minmax(248px,1fr));
 border-bottom:1px solid var(--linha)}
.hi-ft>div{padding:15px 20px;border-right:1px solid var(--linha)}
.hi-ft>div:last-child{border-right:0}
.hi-ft span{display:block;font-size:10px;font-weight:800;letter-spacing:1.4px;
 text-transform:uppercase;color:var(--txt2)}
.hi-ft b{display:block;font-size:13.5px;font-weight:600;margin-top:5px}
.hi-h3{font-size:11px;font-weight:800;letter-spacing:2px;color:var(--txt2);
 text-transform:uppercase;padding:22px 28px 0}

.ats{padding:12px 28px 4px}
.at{display:grid;grid-template-columns:92px 1fr;gap:18px;padding:15px 0;
 border-bottom:1px dashed var(--linha);align-items:start}
.at:last-child{border-bottom:0}
.at-b{display:flex;flex-direction:column;gap:5px;align-items:flex-start;padding-top:2px}
.at-d{font-size:11px;font-weight:800;color:#0D0D10;background:var(--acc);border-radius:6px;
 padding:3px 9px}
.at-p{font-size:10.5px;color:var(--txt2);font-weight:700}
.at-l1{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.at-c h4{font-size:15px;font-weight:800;letter-spacing:-.01em}
.at-og{font-size:10.5px;font-weight:700;color:var(--txt2);border:1px solid var(--linha);
 border-radius:5px;padding:1px 7px}
/* ⚠️ num só texto de 76ch sobrava metade da linha vazia à direita.
   «o que acontece» e «por quê» andam lado a lado e preenchem a faixa. */
.at-tx{display:grid;grid-template-columns:1.2fr 1fr;gap:26px;margin-top:8px;align-items:start}
@media(max-width:860px){.at-tx{grid-template-columns:1fr;gap:7px}}
.at-o{font-size:13.5px;color:var(--txt)}
.at-q{font-size:12.5px;color:var(--txt2);border-left:2px solid var(--linha);padding-left:13px}
.at-q b{color:var(--acc)}

/* ⚠️ 4 caixas em auto-fit viram 3+1 e sobra meia linha vazia embaixo.
   2×2 fecha o bloco. */
.hi-fim{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;
 background:var(--linha);border-top:1px solid var(--linha);margin-top:14px}
@media(max-width:700px){.hi-fim{grid-template-columns:1fr}}
.bx{background:var(--sup);padding:19px 22px}
.bx h3{font-size:10.5px;font-weight:800;letter-spacing:1.6px;text-transform:uppercase;
 color:var(--txt2);margin-bottom:10px}
.bx p{font-size:13.5px;color:var(--txt)}
.bx2 p,.bx3 p{color:var(--txt2)}
.bx3 h3{color:#FF6B6B}
.jg{list-style:none;display:grid;gap:9px}
.jg q{display:block;font-size:14px;font-style:italic;color:var(--txt);quotes:'“' '”'}
.jg small{display:block;font-size:11.5px;color:var(--txt2);margin-top:3px}

.nt{font-size:12.5px;color:var(--txt2);margin-top:40px;border-top:1px solid var(--linha);
 padding-top:16px;max-width:92ch}
.nt b{color:var(--txt)}
.lk{display:inline-block;margin-top:22px;margin-right:9px;font-size:13.5px;font-weight:700;
 color:#0D0D10;background:#FFE27A;border-radius:11px;padding:11px 18px;text-decoration:none}
.lk.l2{background:transparent;color:var(--txt);border:1.5px solid var(--linha)}
@media(max-width:620px){.at{grid-template-columns:1fr;gap:9px}
 .at-b{flex-direction:row;align-items:center}}
"""

HTML = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>OPERAÇÃO FIM DE ANO · 3 histórias</title>
<meta name="theme-color" content="#0D0D10"><style>{CSS}</style></head><body>
<div class="w">
 <span class="selo">ESCOLHER ANTES DAS COPIES</span>
 <h1>Que história a gente vai contar?</h1>
 <p class="int" style="color:var(--txt);font-weight:600;margin-bottom:9px">
  ✅ Escolhida: <b>A OPERAÇÃO</b> — as 153 copies já foram reescritas dentro dela.</p>
 <p class="int">Três opções. Não são três versões da mesma — em cada uma muda
  <b>quem é o protagonista</b> (o time · você · a cliente), muda <b>o tempo</b>
  (presente · passado · futuro) e muda <b>o que prende a audiência</b> por 19 dias.
  O enigma que você desenhou — elevador, máscara, telão — cabe nas três,
  mas significa uma coisa diferente em cada.</p>
 <div class="reg">
  <i>a régua é medida: <b>19 dias</b></i><i><b>51 posts</b></i>
  <i>5 atos do lançamento da <b>@mariaeduardasv</b></i>
  <i>jargões: <b>10 seus</b> + 8 novos</i>
 </div>
 {''.join(bloco(h) for h in HISTORIAS)}
 <p class="nt">⚠️ <b>Depois que você escolher</b>, as 153 copies são reescritas dentro
  da história aprovada — hoje elas estão certas na oferta e soltas na narrativa, que é
  exatamente o que você apontou. A estrutura de 19 dias e 5 atos não muda; muda o que
  cada post conta.
  <br><br>⚠️ <b>As palavras-chave</b> de cada história (OPERAÇÃO, as quatro dos inimigos,
  as das bifurcações) só vão pro ar depois de nascerem ligadas a um funil que mede.</p>
 <a class="lk" href="oferta.html">a oferta montada ↗</a>
 <a class="lk l2" href="index.html">os 51 posts ↗</a>
</div></body></html>"""

saida = os.path.join(DIR, 'storytelling.html')
open(saida, 'w').write(HTML)
assert len(HISTORIAS) == 3 and all(len(h['atos']) == 5 for h in HISTORIAS)
print(f'✅ {saida}  ({len(HTML.encode()) // 1024} KB · {len(HISTORIAS)} histórias × 5 atos)')
