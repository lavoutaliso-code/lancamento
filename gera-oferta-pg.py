#!/usr/bin/env python3
"""A página da OPERAÇÃO FIM DE ANO: a oferta montada, os jargões e os 3 vídeos
do enigma. É a folha de rosto da estrutura — o que vendemos, com que palavras."""
import os, sys
DIR=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,DIR)
from oferta_fda import OFERTA, JARGOES_DELA, JARGOES_NOVOS, ENIGMA

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

pil = ''.join(
 f'<article class="pil"><div class="pil-c"><span class="pil-n">{p["n"]}</span>'
 f'<h3>{p["nome"]}</h3></div><p class="pil-o">{p["oque"]}</p>'
 f'<ul>{"".join(f"<li>{x}</li>" for x in p["entrega"])}</ul></article>'
 for p in OFERTA['pilares'])

jd = ''.join(f'<li><q>{esc(t)}</q><small>{dt} · {cm} comentários</small></li>'
             for t, dt, cm in JARGOES_DELA)
jn = ''.join(f'<li><q>{esc(t)}</q><small>{uso}</small></li>' for t, uso in JARGOES_NOVOS)

eni = ''.join(
 f'<article class="eni"><div class="eni-c"><span class="eni-d">{e["d"]}</span>'
 f'<span class="eni-p">{e["peca"]}</span></div>'
 f'<p class="eni-cena">{e["cena"]}</p>'
 f'<p class="eni-tx"><b>na tela:</b> {e["texto"]}</p>'
 f'<div class="eni-leg">{e["legenda"]}</div>'
 f'<span class="eni-kw">palavra: {e["kw"]}</span></article>' for e in ENIGMA)

CSS = """
:root{--bg:#0E0E11;--sup:#17171C;--txt:#F5F2F7;--txt2:#A29AA8;--linha:#2A2A32;
 --rosa:#FF2D87;--marca:#FFE27A;--f:-apple-system,'SF Pro Text','Helvetica Neue',Arial,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--txt);font-family:var(--f);line-height:1.55;
 -webkit-font-smoothing:antialiased}
.w{max-width:1180px;margin:0 auto;padding:40px 22px 80px}
.selo{display:inline-block;font-size:11px;font-weight:800;letter-spacing:2px;
 color:var(--rosa);border:1.5px solid var(--rosa);border-radius:7px;padding:4px 11px}
h1{font-size:clamp(34px,6vw,58px);font-weight:800;letter-spacing:-.035em;line-height:1.02;
 margin:14px 0 10px}
.pr{font-size:18px;color:var(--txt);max-width:40ch}
.dor{font-size:15px;color:var(--txt2);max-width:62ch;margin-top:14px}
.ag{margin-top:18px;border-left:3px solid var(--rosa);padding:10px 0 10px 16px;
 font-size:15px;max-width:60ch}
h2{font-size:12px;font-weight:800;letter-spacing:2.2px;color:var(--txt2);
 text-transform:uppercase;margin:52px 0 16px}
.gr{display:grid;grid-template-columns:repeat(auto-fit,minmax(272px,1fr));gap:14px}
.pil{background:var(--sup);border:1px solid var(--linha);border-radius:16px;padding:18px 20px}
.pil-c{display:flex;align-items:center;gap:11px;margin-bottom:9px}
.pil-n{display:grid;place-items:center;width:28px;height:28px;border-radius:50%;flex:none;
 background:var(--rosa);color:#fff;font-size:14px;font-weight:800}
.pil h3{font-size:15px;font-weight:800;letter-spacing:-.01em}
.pil-o{font-size:13.5px;color:var(--txt2);margin-bottom:11px}
.pil ul{list-style:none;display:grid;gap:6px}
.pil li{font-size:12.5px;color:var(--txt);padding-left:16px;position:relative}
.pil li::before{content:"";position:absolute;left:0;top:8px;width:6px;height:6px;
 border-radius:2px;background:var(--marca)}
.isca{background:linear-gradient(135deg,#1C1620,#17171C);border:1px solid var(--rosa);
 border-radius:16px;padding:20px 22px;margin-top:14px}
.isca h3{font-size:17px;font-weight:800}
.isca p{font-size:14px;color:var(--txt2);margin-top:6px;max-width:68ch}
.isca .trava{font-size:13px;color:var(--marca);margin-top:11px;font-weight:600}
.jg{list-style:none;display:grid;gap:9px;
 grid-template-columns:repeat(auto-fit,minmax(330px,1fr))}
.jg li{background:var(--sup);border:1px solid var(--linha);border-radius:13px;padding:13px 16px}
.jg q{display:block;font-size:15.5px;font-style:italic;quotes:'“' '”'}
.jg small{display:block;font-size:11.5px;color:var(--txt2);margin-top:5px}
.jg.novos q{color:var(--marca)}
.eni{background:var(--sup);border:1px solid var(--linha);border-radius:16px;padding:18px 20px;
 display:flex;flex-direction:column}
.eni-c{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.eni-d{font-size:11px;font-weight:800;color:#fff;background:var(--rosa);border-radius:6px;
 padding:2px 9px}
.eni-p{font-size:11.5px;color:var(--txt2)}
.eni-cena{font-size:13.5px;color:var(--txt2)}
.eni-tx{font-size:12.5px;color:var(--txt);margin-top:9px}
.eni-leg{font-size:13.5px;background:#0E0E11;border:1px dashed var(--linha);border-radius:11px;
 padding:11px 13px;margin:11px 0 12px;white-space:pre-line}

/* ⚠️ margin-top:auto encosta o selo no rodapé — sem isso os três cartões,
   que o grid deixa da mesma altura, mostram a palavra em alturas diferentes */
.eni-kw{align-self:flex-start;font-size:10.5px;font-weight:800;background:var(--marca);
 color:#2A1F00;border-radius:5px;padding:3px 9px;margin-top:auto}
.nt{font-size:12.5px;color:var(--txt2);margin-top:30px;max-width:92ch;
 border-top:1px solid var(--linha);padding-top:16px}
.nt b{color:var(--txt)}
.lk{display:inline-block;margin-top:22px;margin-right:9px;font-size:14px;font-weight:700;
 color:#0E0E11;background:var(--marca);border-radius:11px;padding:11px 18px;text-decoration:none}
.lk.l2{background:transparent;color:var(--txt);border:1.5px solid var(--linha)}
"""

HTML = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>OPERAÇÃO FIM DE ANO · a oferta</title>
<meta name="theme-color" content="#0E0E11"><style>{CSS}</style></head><body>
<div class="w">
 <span class="selo">MENTORIA · 01.11 → 31.12</span>
 <h1>OPERAÇÃO<br>FIM DE ANO</h1>
 <p class="pr">{OFERTA['promessa']}</p>
 <p class="dor">{OFERTA['dor']}</p>
 <p class="ag"><b>Por que agora:</b> {OFERTA['porque_agora']}</p>

 <h2>as quatro frentes</h2>
 <div class="gr">{pil}</div>

 <h2>a isca — o que ela ganha de graça</h2>
 <div class="isca"><h3>{OFERTA['isca']['nome']}</h3>
  <p>{OFERTA['isca']['oque']}</p>
  <p class="trava">{OFERTA['isca']['trava']}</p></div>

 <h2>o enigma — os três vídeos</h2>
 <div class="gr">{eni}</div>

 <h2>os jargões que você JÁ usa</h2>
 <ul class="jg">{jd}</ul>

 <h2>os jargões novos, na mesma família</h2>
 <ul class="jg novos">{jn}</ul>

 <p class="nt">⚠️ <b>O tom não foi inventado.</b> Os seus salvos não deram pra ler — a
  sessão do Chrome não está logada no Instagram. Então o tom saiu de onde dava pra medir:
  as <b>165 legendas com texto</b> dos 296 posts seus colhidos em 24/10/2026. Cada jargão
  da primeira lista tem a data e a contagem do post de onde veio.
  <br><br>⚠️ <b>Toda palavra-chave</b> (OPERAÇÃO, CONTA, JANEIRO, AO VIVO…) precisa nascer
  ligada a um funil que mede antes de ir pro ar.</p>

 <a class="lk" href="storytelling.html">escolher a história ↗</a>
 <a class="lk l2" href="index.html">ver os 51 posts com as 153 copies →</a>
</div></body></html>"""

saida=os.path.join(DIR,'oferta.html')
open(saida,'w').write(HTML)
print(f'✅ {saida}  ({len(HTML.encode())//1024} KB · {len(OFERTA["pilares"])} pilares · '
      f'{len(JARGOES_DELA)+len(JARGOES_NOVOS)} jargões)')
