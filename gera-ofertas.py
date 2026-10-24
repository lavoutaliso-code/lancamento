#!/usr/bin/env python3
"""As 3 ofertas, estruturadas pra ela ESCOLHER — não pra ela ler.

A diferença de um relatório: as três calculadoras funcionam de verdade nesta
página. Ela mexe nos números do salão dela e vê o que cada isca cospe. É assim
que dá pra julgar se a isca entrega um número que faz comprar — ou um número
que só entristece.

⚠️ TUDO QUE É NÚMERO DELA VEIO MEDIDO na @izabelalaila em 24/10/2026:
   296 posts colhidos e 398 comentários lidos. As evidências citadas em cada
   oferta têm data e contagem; nenhuma é impressão.

⚠️ AS CONTAS DAS CALCULADORAS SÃO ARITMÉTICA PURA — preço, custo, tempo e
   quantidade. Nenhuma promete faturamento: elas mostram o teto que a conta
   dela permite hoje. Projeção de venda não entra, porque não dá pra medir.
"""
import os

DIR = os.path.dirname(os.path.abspath(__file__))

EVID = [
    ('12.969', 'comentários no chamado pra <b>fazer parte</b> do time', '24/05/2026',
     'o maior post da história do perfil — e dezenas ficaram sem resposta: '
     '«suas 20 futuras técnicas estão aqui aguardando»'),
    ('2.516', 'em «lá na frente a conta fecha, o trabalho devolve»', '26/02/2024',
     'a promessa de que o esforço vira dinheiro é o que mais emociona esse público'),
    ('1.808', 'na estratégia da Virgínia — palavra pedida: «<b>agenda lotada</b>»', '24/03/2024',
     'agenda lotada é o desejo que elas mesmas nomeiam'),
    ('1.182', 'no <b>modelo de comanda pronto</b>', '24/05/2024',
     'material pronto pra usar hoje converte mais que conselho'),
    ('671', 'em «32 clientes de progressiva num dia, com equipe bem montada»', '04/12/2025',
     'equipe + pico de dezembro, provado na sua própria operação'),
    ('420', 'em «você fica no <b>operacional</b> ou no <b>estratégico</b>?»', '07/04/2024',
     'elas se reconhecem presas no operacional'),
]

PERG = [
    'Como você organiza a questão financeira do salão, qual aplicativo de caixa você usa?',
    'Poderia dividir onde consigo esse Planner?',
    'Qual valor das suas progressivas?',
    'Minha maior vontade é abrir um salão mas não entendo nada de salão',
    'EU QUERO REPRESENTAR SABARÁ E REGIÃO 🩵',
    'ESTOU PREPARADA! Sempre me inspirei em você e no teu salão',
]

OFERTAS = [
    dict(
        id='dez', n=1, nome='Operação Dezembro', cor='#FF2D87',
        chamada='Montar o time antes do pico — com data de corte',
        dor='Dezembro é o mês que salva o ano do salão. E eu vou chegar nele '
            'sozinha, atendendo tudo, pra faturar o mesmo de sempre com o dobro '
            'do cansaço.',
        mec='Não é curso de equipe. São <b>30 dias de implantação</b> pra ela chegar '
            'em dezembro com gente treinada no seu POP. O prazo não é inventado: '
            'dezembro acontece com ou sem ela.',
        calc='O Teto de Dezembro',
        calcOque='Mostra o <b>teto que ela não consegue furar sozinha</b> — e, do lado, '
                 'o mesmo dezembro com uma e com duas pessoas. A oferta é a diferença '
                 'entre os dois números.',
        entrega=['o POP que você usa no Lavou Tá Liso',
                 'roteiro de contratação (onde achar, o que perguntar, teste prático)',
                 'as 2 primeiras semanas de treinamento, dia a dia',
                 'escala de dezembro e tabela de comissão'],
        evid=['671 comentários no post de equipe + 32 clientes num dia (04/12/2025)',
              '«batemos um novo recorde» em 06/12/2025 — o pico é documentado por você',
              '3 mil alunas já aprenderam exatamente isto com você'],
        risco='Exige que ela tenha caixa pra contratar. Quem está muito apertada '
              'olha o preço da auxiliar antes de olhar o seu.',
        forte='É o que você mais provou, e o relógio vem de graça.'),

    dict(
        id='time', n=2, nome='O Time Lavou Tá Liso', cor='#2F6FD0',
        chamada='Formação de técnica — entrar pro time, não assistir aula',
        dor='Eu quero fazer parte de algo maior do que o meu salão sozinho. '
            'Já levantei a mão pra você e fiquei sem resposta.',
        mec='<b>Formação de técnica certificada</b> no seu método, com turma por '
            'região. A palavra não é «aprenda comigo» — é <b>entre pro time</b>, '
            'que é exatamente o que puxou 12.969 comentários.',
        calc='Quanto vale a sua cadeira',
        calcOque='Põe lado a lado o que ela fatura hoje e o que faturaria cobrando '
                 'como técnica formada, com protocolo e nome por trás. Dois números '
                 'na mesma tela.',
        entrega=['formação no protocolo completo',
                 'certificado e direito de se dizer técnica formada por você',
                 'material de divulgação pronto pra região dela',
                 'turma fechada por região'],
        evid=['12.969 comentários no chamado de 24/05/2026 — o maior do perfil',
              '«ESTOU PREPARADA», «quero representar minha região» — nas palavras delas',
              'dezenas cobrando retorno: a fila existe e está parada'],
        risco='⚠️ <b>Mexe com a franquia.</b> Em 29/12/2025 você encerrou os cursos '
              '«em respeito aos novos franqueados». Formar técnica pode conflitar — '
              'isso precisa estar resolvido antes, não depois.',
        forte='É o maior desejo bruto que existe na sua conta, e já está represado.'),

    dict(
        id='conta', n=3, nome='A Conta do Salão', cor='#1F7A4C',
        chamada='Precificação e caixa em 21 dias',
        dor='Eu trabalho o mês inteiro, entra dinheiro, e no dia 30 não sobra. '
            'E eu não sei dizer se é o preço, se é o custo, ou se sou eu.',
        mec='<b>21 dias</b> pra ela saber o custo de cada serviço, refazer a tabela '
            'de preço e ter um caixa que fecha. É literalmente a pergunta que elas '
            'fazem sozinhas no seu perfil.',
        calc='A Conta que Ninguém Faz',
        calcOque='Ela põe um serviço, o produto, o tempo e o preço. A tela devolve '
                 '<b>quanto sobra por hora da mão dela</b> e <b>qual preço fecha a '
                 'conta</b>. Em 3 minutos ela sai com um número que não tinha.',
        entrega=['planilha de custo por serviço, já com os seus campos',
                 'a tabela de preço refeita com ela',
                 'controle de caixa semanal (o que entra, o que sai, o que sobra)',
                 '4 semanas de acompanhamento'],
        evid=['«Como você organiza a questão financeira, qual aplicativo de caixa?» — pergunta espontânea',
              '«Qual valor das suas progressivas?» — preço é curiosidade declarada',
              '2.516 comentários em «a conta fecha, o trabalho devolve» (26/02/2024)'],
        risco='É a de menor status. Vende alívio, não sonho — e alívio costuma '
              'ter teto de preço mais baixo que transformação.',
        forte='É a mais barata de provar: a calculadora já entrega valor antes da venda.'),
]


# ════════════════════════════════════════════════════════════════════════
CALCS = {
 'dez': """
  <div class="cl">
   <div class="cl-in">
    <label>Preço médio do serviço<input type="number" id="d-pre" value="250" step="10"></label>
    <label>Quanto tempo leva (horas)<input type="number" id="d-dur" value="3" step="0.5"></label>
    <label>Horas que ela atende por dia<input type="number" id="d-hd" value="8" step="1"></label>
    <label>Dias de dezembro que vai abrir<input type="number" id="d-dias" value="24" step="1"></label>
    <label>Cadeiras no salão<input type="number" id="d-cad" value="3" step="1"></label>
   </div>
   <div class="cl-out" id="d-out"></div>
  </div>""",
 'time': """
  <div class="cl">
   <div class="cl-in">
    <label>O que ela cobra hoje<input type="number" id="t-hoje" value="180" step="10"></label>
    <label>Clientes por semana<input type="number" id="t-sem" value="12" step="1"></label>
    <label>O que cobraria como técnica formada<input type="number" id="t-dep" value="280" step="10"></label>
   </div>
   <div class="cl-out" id="t-out"></div>
  </div>""",
 'conta': """
  <div class="cl">
   <div class="cl-in">
    <label>Preço que ela cobra<input type="number" id="c-pre" value="250" step="10"></label>
    <label>Produto gasto no serviço<input type="number" id="c-prod" value="60" step="5"></label>
    <label>Tempo do serviço (horas)<input type="number" id="c-h" value="3" step="0.5"></label>
    <label>Custo fixo do salão no mês<input type="number" id="c-fix" value="4500" step="100"></label>
    <label>Atendimentos no mês<input type="number" id="c-qt" value="60" step="5"></label>
    <label>Quanto ela quer ganhar por hora<input type="number" id="c-alvo" value="60" step="10"></label>
   </div>
   <div class="cl-out" id="c-out"></div>
  </div>""",
}

evid_html = ''.join(
    f'<li><b>{n}</b><span>{t}</span><small>{dt} · {por}</small></li>'
    for n, t, dt, por in EVID)
perg_html = ''.join(f'<li>“{p}”</li>' for p in PERG)

cards = ''
for o in OFERTAS:
    cards += f"""
 <article class="of" id="of-{o['id']}" style="--c:{o['cor']}">
  <div class="of-cab">
   <span class="of-n">{o['n']}</span>
   <div><h2>{o['nome']}</h2><p class="of-ch">{o['chamada']}</p></div>
  </div>

  <div class="bl bl-dor"><span class="bl-t">A dor, na voz dela</span>
   <p class="dor">“{o['dor']}”</p></div>

  <div class="bl"><span class="bl-t">O mecanismo</span><p>{o['mec']}</p></div>

  <div class="bl bl-cal"><span class="bl-t">A isca · {o['calc']}</span>
   <p>{o['calcOque']}</p>
   <div class="cal-dem"><span class="cal-rot">mexa nos números — é a calculadora de verdade</span>
   {CALCS[o['id']]}</div></div>

  <div class="bl"><span class="bl-t">O que ela leva</span>
   <ul class="ent">{''.join(f'<li>{x}</li>' for x in o['entrega'])}</ul></div>

  <div class="bl bl-ev"><span class="bl-t">Por que eu acho que vende — medido</span>
   <ul class="ev">{''.join(f'<li>{x}</li>' for x in o['evid'])}</ul></div>

  <div class="bl bl-ri"><span class="bl-t">O risco</span><p>{o['risco']}</p></div>

  <div class="of-pe"><b>Em uma frase:</b> {o['forte']}
   <button class="esc" data-of="{o['id']}" data-nome="{o['nome']}">escolher esta</button></div>
 </article>"""

CSS = """
:root{--bg:#F4F4F6;--sup:#FFF;--txt:#1A0A12;--txt2:#7B6B74;--linha:#E4DFE4;
 --marca:#FFE27A;--ok:#1F7A4C;--az:#0A84FF;
 --f:-apple-system,'SF Pro Text','Helvetica Neue','Inter',Arial,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--txt);font-family:var(--f);line-height:1.5;
 -webkit-font-smoothing:antialiased}
.wrap{max-width:1420px;margin:0 auto;padding:26px 22px 70px}
h1{font-size:30px;font-weight:800;letter-spacing:-.03em}
.sub{font-size:14.5px;color:var(--txt2);margin-top:6px;max-width:92ch}

/* a base de evidência */
.base{margin:22px 0 30px;border:1.6px solid var(--linha);border-radius:18px;
 background:var(--sup);padding:20px 22px}
.base h2{font-size:17px;font-weight:800;letter-spacing:-.02em}
.base>p{font-size:13px;color:var(--txt2);margin-top:3px}
.ev-g{list-style:none;display:grid;gap:9px;margin-top:14px;
 grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.ev-g li{border:1.4px solid var(--linha);border-radius:13px;padding:11px 13px}
.ev-g b{display:block;font-size:22px;font-weight:800;letter-spacing:-.02em}
.ev-g span{display:block;font-size:12.5px;margin-top:1px}
.ev-g small{display:block;font-size:11px;color:var(--txt2);margin-top:5px}
.perg{list-style:none;display:grid;gap:6px;margin-top:16px}
.perg li{font-size:13px;color:var(--txt);background:#FFFBEC;border:1px solid #F0E3B6;
 border-radius:10px;padding:8px 11px}
.perg-t{font-size:12px;font-weight:800;color:var(--txt2);text-transform:uppercase;
 letter-spacing:.7px;margin-top:18px}

/* as três ofertas */
.gr{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;align-items:start}
.of{background:var(--sup);border:1.8px solid var(--linha);border-radius:20px;overflow:hidden;
 display:flex;flex-direction:column}
.of.sel{border-color:var(--c);box-shadow:0 0 0 3px color-mix(in srgb,var(--c) 22%,transparent)}
.of-cab{display:flex;gap:12px;align-items:flex-start;padding:18px 20px 14px;
 border-bottom:1px solid var(--linha);background:color-mix(in srgb,var(--c) 7%,#fff)}
.of-n{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;flex:none;
 background:var(--c);color:#fff;font-size:17px;font-weight:800}
.of h2{font-size:19px;font-weight:800;letter-spacing:-.02em;line-height:1.15}
.of-ch{font-size:12.5px;color:var(--txt2);margin-top:2px}
.bl{padding:14px 20px;border-bottom:1px solid var(--linha)}
.bl-t{display:block;font-size:10.5px;font-weight:800;color:var(--txt2);
 text-transform:uppercase;letter-spacing:.7px;margin-bottom:7px}
.bl p{font-size:13.5px;color:var(--txt2)}
.bl p b,.bl li b{color:var(--txt)}
.bl-dor{background:#FBFAFB}
.dor{font-size:14.5px!important;color:var(--txt)!important;font-style:italic;line-height:1.5}
.ent,.ev{list-style:none;display:grid;gap:6px}
.ent li{font-size:13px;padding-left:18px;position:relative}
.ent li::before{content:"";position:absolute;left:2px;top:7px;width:7px;height:7px;
 border-radius:2px;background:var(--c)}
.ev li{font-size:12.5px;color:var(--txt2);padding-left:18px;position:relative}
.ev li::before{content:"✓";position:absolute;left:0;color:var(--ok);font-weight:800}
.bl-ev{background:#F7FBF8}
.bl-ri{background:#FFF7F9}
.bl-ri p{color:var(--txt)}
.of-pe{margin-top:auto;padding:15px 20px 18px;font-size:13px;color:var(--txt2)}
.of-pe b{color:var(--txt)}
.esc{display:block;width:100%;margin-top:12px;font:inherit;font-size:15px;font-weight:700;
 padding:12px;cursor:pointer;border:none;border-radius:12px;background:var(--c);color:#fff}
.of.sel .esc::after{content:" ✓"}

/* a calculadora de verdade */
.bl-cal{background:#F6F8FC}
.cal-dem{margin-top:11px;border:1.4px solid var(--linha);border-radius:14px;background:var(--sup);
 padding:12px}
.cal-rot{display:block;font-size:10.5px;font-weight:700;color:var(--az);margin-bottom:9px}
.cl-in{display:grid;gap:8px}
.cl-in label{display:grid;gap:3px;font-size:11.5px;color:var(--txt2);font-weight:600}
.cl-in input{font:inherit;font-size:14px;padding:8px 10px;border:1.4px solid var(--linha);
 border-radius:9px;background:#FBFAFB;color:var(--txt);width:100%}
.cl-out{margin-top:12px;padding-top:12px;border-top:1px dashed var(--linha);display:grid;gap:7px}
.ln{display:flex;align-items:baseline;justify-content:space-between;gap:10px;font-size:13px}
.ln span{color:var(--txt2)}
.ln i{font-style:normal;opacity:.65;font-size:11px}
.ln b{font-size:15px;font-weight:700;white-space:nowrap}
.ln.destaque{background:color-mix(in srgb,var(--c) 10%,#fff);border-radius:10px;
 padding:9px 11px;margin-top:3px}
.ln.destaque b{font-size:20px;font-weight:800;color:var(--c)}
.ln.destaque span{color:var(--txt);font-weight:600}
.frase{font-size:12.5px;color:var(--txt);background:var(--marca);border-radius:9px;
 padding:8px 10px;margin-top:4px;line-height:1.45}
.alerta{font-size:12.5px;color:#fff;background:#C2185B;border-radius:9px;padding:8px 10px;
 margin-top:4px;font-weight:600}

.nt{font-size:12.5px;color:var(--txt2);margin-top:22px;max-width:94ch}
.nt b{color:var(--txt)}
.escolhido{position:sticky;bottom:16px;margin-top:20px;background:var(--txt);color:#fff;
 border-radius:14px;padding:13px 18px;font-size:14px;display:flex;align-items:center;gap:12px}
.escolhido[hidden]{display:none}
.escolhido b{font-size:16px}
.escolhido button{margin-left:auto;font:inherit;font-size:12.5px;font-weight:700;padding:7px 13px;
 cursor:pointer;border:1.5px solid rgba(255,255,255,.35);border-radius:9px;background:transparent;
 color:#fff}
@media(max-width:1150px){.gr{grid-template-columns:1fr;max-width:620px}}
"""

JS = r"""
var rs=function(v){return 'R$ '+(Math.round(v)).toLocaleString('pt-BR')};
function num(id){var e=document.getElementById(id);return e?(parseFloat(e.value)||0):0}
function ouve(ids,fn){ids.forEach(function(i){var e=document.getElementById(i);
  if(e){['input','change'].forEach(function(ev){e.addEventListener(ev,fn)})}}); fn();}

/* ① O TETO DE DEZEMBRO — capacidade limitada por HORAS e por CADEIRAS.
   ⚠️ Duas pessoas não dobram o faturamento se só há duas cadeiras: o teto é
   o menor entre gente e cadeira. Fingir que dobra seria inventar número. */
ouve(['d-pre','d-dur','d-hd','d-dias','d-cad'],function(){
  var pre=num('d-pre'), dur=num('d-dur'), hd=num('d-hd'), dias=num('d-dias'), cad=num('d-cad');
  var o=document.getElementById('d-out'); if(!o)return;
  if(dur<=0||hd<=0||dias<=0){o.innerHTML='<p class="frase">preencha o tempo, as horas e os dias.</p>';return}
  function fat(pessoas){var p=Math.min(pessoas,Math.max(1,cad));
    return Math.floor(p*hd*dias/dur)*pre;}
  var s=fat(1), um=fat(2), dois=fat(3);
  var atend=Math.floor(hd*dias/dur);
  var dif=um-s;
  o.innerHTML=
   '<div class="ln"><span>Atendimentos que cabem na SUA mão</span><b>'+atend+'</b></div>'+
   '<div class="ln"><span>Dezembro sozinha</span><b>'+rs(s)+'</b></div>'+
   '<div class="ln"><span>Com +1 pessoa treinada</span><b>'+rs(um)+'</b></div>'+
   '<div class="ln"><span>Com +2 pessoas</span><b>'+rs(dois)+'</b></div>'+
   (cad<2
     ? '<div class="alerta">Com 1 cadeira, gente a mais não aumenta nada. '+
       'O teto aqui é a cadeira, não a mão.</div>'
     : '<div class="ln destaque"><span>O que ela deixa na mesa por ir sozinha</span><b>'+
       rs(dif)+'</b></div>'+
       '<div class="frase">É esse número que a oferta tem que custar menos que ele.</div>');
});

/* ② QUANTO VALE A SUA CADEIRA — dois números na mesma tela, sem projeção
   de «vai vender mais»: a mesma quantidade de clientes, outro preço. */
ouve(['t-hoje','t-sem','t-dep'],function(){
  var h=num('t-hoje'), s=num('t-sem'), d=num('t-dep');
  var o=document.getElementById('t-out'); if(!o)return;
  /* ⚠️ ARREDONDA ANTES DE MULTIPLICAR. Mostrar «52 clientes» e calcular sobre
     51,96 faz a tela exibir R$ 9.353 onde 52×180 dá R$ 9.360 — a conta não
     fecha com ela mesma, e é exatamente o que a lei do financeiro proíbe:
     as parcelas e o resultado têm que bater na mesma tela. */
  var mes=Math.round(s*4.33);
  var ah=h*mes, ad=d*mes, dif=ad-ah;
  o.innerHTML=
   '<div class="ln"><span>Clientes por mês <i>(' + s + '/semana × 4,33)</i></span><b>'+mes+'</b></div>'+
   '<div class="ln"><span>Hoje</span><b>'+rs(ah)+'</b></div>'+
   '<div class="ln"><span>Cobrando como técnica formada</span><b>'+rs(ad)+'</b></div>'+
   (dif>0
     ? '<div class="ln destaque"><span>Diferença por mês</span><b>'+rs(dif)+'</b></div>'+
       '<div class="frase">Mesma quantidade de clientes — só o preço muda. '+
       'Em um ano: <b>'+rs(dif*12)+'</b>.</div>'
     : '<div class="alerta">O preço de técnica está igual ou menor que o de hoje. '+
       'Sem diferença, não há oferta.</div>');
});

/* ③ A CONTA QUE NINGUÉM FAZ — a única das três que pode devolver número
   NEGATIVO, e devolve mesmo. É o ponto: ela precisa ver que não fecha. */
ouve(['c-pre','c-prod','c-h','c-fix','c-qt','c-alvo'],function(){
  var pre=num('c-pre'), prod=num('c-prod'), h=num('c-h'),
      fix=num('c-fix'), qt=num('c-qt'), alvo=num('c-alvo');
  var o=document.getElementById('c-out'); if(!o)return;
  if(h<=0||qt<=0){o.innerHTML='<p class="frase">preencha o tempo e os atendimentos.</p>';return}
  var fixPor=fix/qt;
  var sobra=pre-prod-fixPor;
  var porHora=sobra/h;
  var preJusto=prod+fixPor+alvo*h;
  o.innerHTML=
   '<div class="ln"><span>Custo fixo que cabe em cada atendimento</span><b>'+rs(fixPor)+'</b></div>'+
   '<div class="ln"><span>Sobra por atendimento</span><b>'+rs(sobra)+'</b></div>'+
   '<div class="ln destaque"><span>Sobra por HORA da sua mão</span><b>'+rs(porHora)+'</b></div>'+
   (porHora<0
     ? '<div class="alerta">Nesse preço você está PAGANDO '+rs(-porHora)+' por hora pra trabalhar.</div>'
     : (porHora<alvo
        ? '<div class="frase">Você quer '+rs(alvo)+'/hora e está ganhando '+rs(porHora)+
          '/hora.</div>'
        : '<div class="frase">Acima do que você pediu. Essa conta fecha.</div>'))+
   '<div class="ln"><span>Preço que fecha a conta</span><b>'+rs(preJusto)+'</b></div>'+
   (preJusto>pre
     ? '<div class="frase">Faltam <b>'+rs(preJusto-pre)+'</b> no seu preço.</div>'
     : '');
});

/* escolher */
(function(){
 var K='oferta-escolhida';
 var barra=document.getElementById('barra'), nome=document.getElementById('barra-nome');
 function pinta(){
   var v=localStorage.getItem(K);
   document.querySelectorAll('.of').forEach(function(o){
     o.classList.toggle('sel',o.id==='of-'+v);});
   if(v){var b=document.querySelector('.esc[data-of="'+v+'"]');
     nome.textContent=b?b.dataset.nome:v; barra.hidden=false;}
   else barra.hidden=true;
 }
 document.addEventListener('click',function(e){
   var b=e.target.closest('.esc');
   if(b){localStorage.setItem(K,b.dataset.of);pinta();
     barra.scrollIntoView({behavior:'smooth',block:'nearest'});return;}
   if(e.target.id==='barra-x'){localStorage.removeItem(K);pinta();}
 });
 pinta();
})();
"""

HTML = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>As 3 ofertas · escolher</title><style>{CSS}</style></head><body>
<div class="wrap">
 <h1>Três ofertas pra você escolher</h1>
 <p class="sub">Nenhuma delas saiu de achismo. Colhi <b>296 posts</b> e li
  <b>398 comentários</b> do @izabelalaila em 24/10/2026, e cada oferta carrega a
  evidência que a sustenta — com data e contagem. <b>As três calculadoras funcionam
  aqui dentro:</b> mexa nos números do seu salão e veja o que cada isca cospe. É
  assim que dá pra saber se ela entrega um número que faz comprar.</p>

 <section class="base">
  <h2>O que o seu público já respondeu</h2>
  <p>Os ganchos que mais puxaram comentário na sua conta, do maior pro menor.</p>
  <ul class="ev-g">{evid_html}</ul>
  <p class="perg-t">E o que elas perguntam sozinhas, sem você pedir</p>
  <ul class="perg">{perg_html}</ul>
 </section>

 <div class="gr">{cards}</div>

 <div class="escolhido" id="barra" hidden>
  Você escolheu: <b id="barra-nome"></b>
  <button id="barra-x">trocar</button>
 </div>

 <p class="nt">⚠️ <b>O que as calculadoras NÃO fazem:</b> nenhuma projeta venda nova.
  Elas só fazem a aritmética do que já existe — preço, custo, tempo e quantidade —
  porque «quantas clientes novas você vai ter» não é uma conta, é um chute.
  <br><br>⚠️ <b>Antes de qualquer uma:</b> em 29/12/2025 você anunciou o encerramento de
  todos os cursos, «em respeito aos novos franqueados». Voltar a vender precisa de uma
  virada honesta na história — a oferta 2 é a que mais esbarra nisso.</p>
</div>
<script>{JS}</script></body></html>"""

saida = os.path.join(DIR, 'ofertas.html')
open(saida, 'w').write(HTML)
print(f'✅ {saida}  ({len(HTML.encode()) // 1024} KB)')
