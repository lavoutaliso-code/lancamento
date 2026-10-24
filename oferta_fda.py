#!/usr/bin/env python3
"""OPERAÇÃO FIM DE ANO — a oferta montada, os jargões e a arquitetura do enigma.

⚠️ O TOM NÃO FOI INVENTADO. Os salvos dela não deram pra ler (a sessão do
   Chrome não está logada no Instagram), então o tom saiu de onde dava pra
   medir: as 165 legendas com texto dos 296 posts colhidos em 24/10/2026.
   Cada bordão abaixo tem a data e o post de onde veio. O exemplo que ela deu
   — «imagina ser tão grande ao ponto de engrandecer outras pessoas também?» —
   é exatamente a mesma família de frase que ela já escreve.
"""

# ── A OFERTA ──────────────────────────────────────────────────────────────
OFERTA = dict(
    nome='OPERAÇÃO FIM DE ANO',
    tipo='mentoria',
    janela='novembro e dezembro',
    promessa='Chegar em janeiro com o ano virado — não com a conta de luz paga.',
    dor='Na área da beleza o ano inteiro se decide em dois meses. Quem chega em '
        'novembro sozinha, sem preço certo e sem time, trabalha o fim de ano '
        'inteiro e só descobre em janeiro que não sobrou.',
    porque_agora='Dezembro acontece com ou sem ela. É o único mês em que a agenda '
                 'enche sozinha — e o único em que dá pra errar o ano inteiro de uma vez.',
    pilares=[
        dict(n=1, nome='MARKETING — o planner dos 60 dias',
             oque='O que postar em novembro e dezembro, dia a dia, com a estratégia '
                  'pronta. Ela não decide o que postar: ela executa.',
             entrega=['calendário de 60 dias com o post de cada dia',
                      'as estruturas prontas (story, reel, carrossel)',
                      'as campanhas de novembro e as de dezembro, separadas',
                      'o que fazer na semana do Natal e na virada']),
        dict(n=2, nome='PREÇO — a conta que fecha',
             oque='A calculadora grátis diz SE o preço dela está certo. Aqui ela '
                  'aprende QUAL é o certo — e refaz a tabela inteira.',
             entrega=['custo real por serviço, com produto, tempo e custo fixo',
                      'a tabela de preço de fim de ano refeita',
                      'quanto cobrar a mais em dezembro sem perder cliente',
                      'o piso abaixo do qual ela não atende']),
        dict(n=3, nome='TIME — montar e faturar 10× no pico',
             oque='Contratar, treinar pelo POP e dividir a agenda a tempo de aguentar '
                  'dezembro. É o que já foi feito no Lavou Tá Liso: 32 clientes num dia.',
             entrega=['roteiro de contratação: onde achar, o que perguntar, teste prático',
                      'o POP do Lavou Tá Liso',
                      'as 2 primeiras semanas de treinamento, dia a dia',
                      'escala de dezembro e tabela de comissão']),
        dict(n=4, nome='DINHEIRO — não descobrir em janeiro',
             oque='Gestão financeira do fim de ano: saber no dia 10 de dezembro se o '
                  'mês vai fechar, e não no dia 10 de janeiro.',
             entrega=['controle de caixa semanal (entra, sai, sobra)',
                      'quanto separar pro 13º, pro imposto e pro estoque',
                      'a meta de dezembro quebrada por semana',
                      'o fechamento de dezembro, feito junto']),
    ],
    isca=dict(nome='A Conta que Ninguém Faz',
              oque='Calculadora de precificação grátis. Ela põe um serviço, o produto, '
                   'o tempo e o preço — e descobre quanto sobra por hora da mão dela.',
              trava='⚠️ A grátis diz SE está certo. NÃO diz qual é o certo. '
                    'O preço que fecha a conta é o primeiro dia da mentoria.'),
)

# ── OS JARGÕES ────────────────────────────────────────────────────────────
# Os que ELA já usa (medidos, com data) e os novos, construídos na mesma família.
JARGOES_DELA = [
    ('Nada herdado, tudo conquistado', '2026-04', 94),
    ('A vida não é sobre quem tem mais talento… é sobre quem tem mais fome', '2025-11', 53),
    ('Todo grande vencedor já pensou em parar, mas escolheu continuar', '2026-??', 60),
    ('Recalcule a rota, mude a estratégia, mude até de ramo… mas não mude de sonho', '2025-??', 57),
    ('Transbordei na vida de outras pessoas', '2025-12', 304),
    ('Você está criando algo grande, mesmo quando parece pequeno', '2024-08', 13),
    ('Lá na frente a conta fecha, e fechou! O trabalho devolve', '2024-02', 2516),
    ('Ganha quem executa', '2026-01', 7),
    ('Meu papel é construir um time de alta performance, pra juntos vencermos campeonatos',
     '2026-05', 17),
    ('Não espera a hora perfeita', '2024-??', 9),
]

JARGOES_NOVOS = [
    ('Quem é da área da beleza não espera janeiro.',
     'o carro-chefe — serve de assinatura em todo post de fim de ano'),
    ('Grande sonho da beleza não se realiza em janeiro. Se realiza em dezembro.',
     'para o enigma e para a abertura do carrinho'),
    ('Você tem 60 dias pra virar o ano. Depois disso, é só mais um ano.',
     'o relógio — usa quando entra a contagem'),
    ('Dezembro não pergunta se você está pronta. Ele vem.',
     'para a dor: tira a desculpa de preparo'),
    ('Imagina ser tão grande ao ponto de engrandecer outras pessoas também.',
     'a frase dela — abre o enigma do time, fecha a venda do pilar TIME'),
    ('Trabalhar o fim de ano inteiro e descobrir em janeiro que não sobrou — '
     'isso tem nome: preço errado.',
     'a ponte da dor para o pilar PREÇO'),
    ('Sozinha você atende. Com time, você fatura.',
     'a ponte da dor para o pilar TIME'),
    ('Não é mais um fim de ano. É O fim de ano.',
     'fechamento de carrinho'),
]

# ── A ARQUITETURA DO ENIGMA (a ideia dela, detalhada) ─────────────────────
ENIGMA = [
    dict(d='DIA 1', peca='reel · elevador',
         cena='Ela sozinha no elevador, toda de preto, máscara preta no rosto. '
              'Sem falar. Porta fecha. Corta.',
         texto='Nenhum texto na tela além de uma data piscando: 01.11',
         legenda='Começou.\n\nComenta <b>OPERAÇÃO</b> que eu te conto primeiro. 🖤',
         kw='OPERAÇÃO'),
    dict(d='DIA 2', peca='reel · a máscara sai',
         cena='Mesmo elevador, mesma roupa. Ela leva a mão à máscara e tira — '
              'corta no meio do movimento, antes de mostrar o rosto inteiro.',
         texto='«Não é sobre esconder. É sobre o tempo certo de mostrar.»',
         legenda='Todo grande vencedor já pensou em parar. Eu escolhi continuar — '
                 'e esse fim de ano vai ser a prova.\n\nComenta <b>OPERAÇÃO</b>. 🖤',
         kw='OPERAÇÃO'),
    dict(d='DIA 3', peca='reel · a sala de reunião',
         cena='Porta do elevador abre na sala de reunião. A equipe inteira sentada, '
              'de preto, esperando. Ela entra e senta na cabeceira. '
              'O telão acende: <b>OPERAÇÃO FIM DE ANO</b>.',
         texto='O telão é a única coisa escrita no vídeo',
         legenda='Imagina ser tão grande ao ponto de engrandecer outras pessoas também.\n\n'
                 'Esse fim de ano eu não vou subir sozinha.\n\n'
                 'Comenta <b>OPERAÇÃO</b> que eu te mostro o plano. 🖤',
         kw='OPERAÇÃO'),
]
