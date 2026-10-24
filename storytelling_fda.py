#!/usr/bin/env python3
"""Três storytellings para a OPERAÇÃO FIM DE ANO — pra ela escolher ANTES das copies.

⚠️ As três são histórias DIFERENTES, não três versões da mesma: muda o
   PROTAGONISTA (o time · ela · a cliente), muda o TEMPO (presente de missão ·
   passado · futuro) e muda o que a audiência fica esperando.
   Se duas puderem virar uma só trocando adjetivo, não são duas.

⚠️ Os 5 atos e os números de dias/posts NÃO foram inventados: são a estrutura
   medida do lançamento da @mariaeduardasv (analise-lancamento.json),
   19 dias, 51 posts — o mesmo esqueleto que já está no site.
"""

# a régua medida: ato | dias | posts | comentários que a Duda fez em cada um
ATOS = [
    ('enigma',  'O enigma',          3, 7,  2204),
    ('dor',     'A dor com nome',    7, 17, 3806),
    ('entrega', 'A entrega de graça', 5, 13, 3486),
    ('aovivo',  'O ao vivo',         1, 3,  162),
    ('venda',   'O carrinho',        3, 11, 1251),
]

HISTORIAS = [

 dict(
  id='A', nome='A OPERAÇÃO',
  sub='um filme de missão — e ela é quem comanda',
  log='Existe uma operação em curso. Ninguém sabe o alvo. No fim, descobre-se '
      'que o alvo é dezembro — e que dá pra entrar nela.',
  quem='O TIME. Ela aparece como comandante, não como professora.',
  tempo='Presente, conspirativo. Tudo está acontecendo agora, e você está de fora.',
  gancho='«Quem está dentro?» — a audiência passa 19 dias querendo ser convocada.',
  cor='#1A1A1F', acc='#FF2D87',
  atos=[
   ('enigma', 'O RECRUTAMENTO',
    'Três reels sem explicação. Ela de preto no elevador, máscara. A máscara sai. '
    'A porta abre na sala de reunião e o telão acende: OPERAÇÃO FIM DE ANO. '
    'Nenhum post diz o que é. Só a palavra.',
    'A palavra OPERAÇÃO nos comentários. Quem comenta entra numa lista — e recebe '
    'a resposta como se fosse convocação, não propaganda.'),
   ('dor', 'O BRIEFING DO ALVO',
    'O alvo é dezembro. E dezembro tem quatro inimigos, nomeados um a um: '
    '① o preço que não fecha · ② a agenda que só cabe você · ③ o time que não existe · '
    '④ o caixa que você só vê em janeiro. Um inimigo por dois dias, com o dano que cada um causa.',
    'Cada inimigo tem palavra própria. Aqui a audiência para de achar bonito e '
    'começa a se reconhecer.'),
   ('entrega', 'O EQUIPAMENTO',
    'Toda operação entrega equipamento antes. O dela é A Conta que Ninguém Faz: '
    'o detector que aponta onde está o vazamento. Grátis, e ela mostra o próprio número nele.',
    'A trava fica explícita e vira parte da história: o detector acusa o vazamento, '
    'o conserto é dentro da operação.'),
   ('aovivo', 'A REUNIÃO DE COMANDO',
    'O ao vivo é o briefing final, com o telão atrás. Ela abre o mapa dos 60 dias '
    'na frente de todo mundo e diz quantos postos existem.',
    'É o único dia em que ela mostra a operação inteira. Quem não entra, viu tudo e ficou de fora.'),
   ('venda', 'O ALISTAMENTO',
    'Carrinho = postos. Não é «vagas limitadas» de propaganda: é quantas pessoas '
    'cabem numa operação que ela vai acompanhar por 60 dias.',
    'Fecha com a sala de reunião cheia — a mesma imagem do dia 3, agora explicada.'),
  ],
  jargoes=[
   ('Imagina ser tão grande ao ponto de engrandecer outras pessoas também.',
    'abre o terceiro reel do enigma, na sala de reunião'),
   ('Meu papel é construir um time de alta performance, pra juntos vencermos campeonatos.',
    'é dela, de 05/2026 — vira a fala do comando no ao vivo'),
   ('Não é mais um fim de ano. É O fim de ano.', 'o fecho do carrinho'),
   ('Quem é da área da beleza não espera janeiro.', 'assinatura, todo post'),
  ],
  enigma='Literal — é exatamente a sequência que você desenhou. Elevador, máscara, '
         'telão. Nesta história o enigma não é um truque de abertura: é a cena de '
         'recrutamento, e a sala de reunião volta no último dia.',
  pede='A mais produzida das três. Pede 3 reels com direção (preto, elevador, sala), '
       'a equipe em cena pelo menos duas vezes, e constância de estética nos 19 dias.',
  risco='Fala pouco de dor concreta no começo. Se o ato 2 não nomear os quatro '
        'inimigos com dureza, a operação vira só bonita — e bonito não vende mentoria.'),

 dict(
  id='B', nome='O DEZEMBRO QUE ME QUEBROU',
  sub='testemunho — ela conta o ano que quase a tirou do jogo',
  log='Ela teve o mês mais cheio da vida e o janeiro mais vazio. Conta como foi, '
      'o que descobriu, e por que nunca mais.',
  quem='ELA. Primeira pessoa, passado real, com número na tela.',
  tempo='Passado → presente. Começa atrás e chega aqui.',
  gancho='«O que aconteceu com ela?» — a audiência fica pelo desfecho, não pela oferta.',
  cor='#201519', acc='#E8B33A',
  atos=[
   ('enigma', 'O QUE ELA NÃO EXPLICA',
    'Três posts sem resposta: a foto de uma agenda lotada, um print cortado, e a frase '
    '«esse foi o mês mais cheio da minha vida — e o pior». Ela não responde ninguém nos comentários.',
    'O silêncio é o gancho. Na história B o enigma não é cinema, é uma pessoa '
    'segurando uma confissão.'),
   ('dor', 'A CONFISSÃO',
    'Sete dias contando o dezembro em que trabalhou todos os dias e janeiro chegou devendo. '
    'Cada erro com nome e com o que custou: o preço que ela fez «pra não perder a cliente», '
    'o encaixe que virou prejuízo, o 13º que ninguém separou.',
    'A audiência não se identifica com uma ideia — se identifica com uma história que já viveu.'),
   ('entrega', 'A CONTA QUE EU NÃO FAZIA',
    'Ela entrega a calculadora como o instrumento que a salvou, não como brinde. '
    '«Esse número aqui foi o que me acordou.» Mostra o dela, de verdade.',
    'A isca deixa de ser ferramenta e vira capítulo: é o objeto que vira a história.'),
   ('aovivo', 'ABRIR A PLANILHA',
    'Ao vivo com a conta na tela. Ela refaz, no ar, o cálculo de um serviço real — '
    'e mostra quanto sobrava por hora da mão dela antes.',
    'O ao vivo é a prova. Em B a prova precisa ser aritmética, não discurso.'),
   ('venda', 'EU NÃO QUERO ISSO PRA VOCÊ',
    'O carrinho não é «últimas vagas». É: eu levei três anos pra descobrir, você tem 60 dias — '
    'e eu vou junto.',
    'Fecha onde abriu: a mesma agenda lotada do dia 1, agora com a conta fechando.'),
  ],
  jargoes=[
   ('Lá na frente a conta fecha, e fechou! O trabalho devolve.',
    'é dela, de 02/2024 — o post de MAIOR alcance que você já fez: 2.516 comentários. '
    'É a tese inteira desta história'),
   ('Todo grande vencedor já pensou em parar, mas escolheu continuar.',
    'o fundo do poço, no meio do ato 2'),
   ('Nada herdado, tudo conquistado.', 'a virada'),
   ('Trabalhar o fim de ano inteiro e descobrir em janeiro que não sobrou — '
    'isso tem nome: preço errado.', 'a ponte da confissão para a oferta'),
  ],
  enigma='Invertido, e fica mais forte assim: a máscara preta é o que você usava '
         'quando estava quebrada e postava sorrindo. Tirar a máscara é contar a verdade. '
         'A sala de reunião no fim não é segredo — é onde você chegou depois.',
  pede='Vulnerabilidade e UM número verdadeiro do passado. Sem o número a história '
       'não para de pé, e não dá pra inventar — a audiência sente.',
  risco='Expõe erro antigo na frente de quem te vê como referência. E prende a '
        'história a você: se você não quiser repetir esse assunto depois, o lançamento '
        'seguinte começa do zero.'),

 dict(
  id='C', nome='31 DE DEZEMBRO, DOIS LUGARES',
  sub='espelho — a protagonista é ela, não você',
  log='No dia 31 de dezembro você vai estar em um de dois lugares. Os dois já estão '
      'sendo decididos agora, em novembro.',
  quem='A CLIENTE. Narrado em segunda pessoa: «você».',
  tempo='Futuro. A história acontece num dia que ainda não chegou.',
  gancho='«Em qual das duas eu vou estar?» — a audiência não acompanha uma pessoa, '
         'se acompanha.',
  cor='#141A20', acc='#36C2A6',
  atos=[
   ('enigma', 'AS DUAS CENAS',
    'Três posts mostrando o MESMO 31 de dezembro em dois lugares — mesma hora, mesma '
    'data no canto da tela, duas realidades. Nenhum texto diz qual é qual.',
    'O enigma aqui é uma pergunta, não um segredo: qual das duas é a sua?'),
   ('dor', 'AS QUATRO BIFURCAÇÕES',
    'Cada dor vira uma data: «o dia 3 de novembro decide o seu 31 de dezembro». '
    'Quatro decisões — preço, agenda, time, caixa — e o que cada uma faz com as duas linhas.',
    'A dor sai do passado e vira relógio. Ninguém se defende de uma lembrança, '
    'mas todo mundo se mexe diante de uma data.'),
   ('entrega', 'O ESPELHO',
    'A calculadora entra como teste de linha: «descubra, em 2 minutos, em qual das '
    'duas você está hoje». Ela devolve a linha, não o conserto.',
    'É a entrega mais natural das três — a isca já É o espelho da história.'),
   ('aovivo', 'O MAPA DESENHADO',
    'Ao vivo desenhando as duas linhas do tempo lado a lado, de novembro a dezembro, '
    'e marcando onde elas se separam.',
    'O ao vivo é o momento em que a metáfora vira plano: 60 dias, marcados.'),
   ('venda', 'A PORTA ENTRE AS LINHAS',
    'O carrinho é a passagem de uma linha para a outra — e ela fecha, porque depois '
    'de novembro não dá mais tempo de mudar dezembro.',
    'A urgência é do calendário, não da propaganda. É a única das três em que o prazo '
    'é verdadeiro por natureza.'),
  ],
  jargoes=[
   ('Grande sonho da beleza não se realiza em janeiro. Se realiza em dezembro.',
    'a frase-título da história'),
   ('Você tem 60 dias pra virar o ano. Depois disso, é só mais um ano.', 'o relógio'),
   ('Recalcule a rota, mude a estratégia, mude até de ramo… mas não mude de sonho.',
    'é dela, de 2025 — fecha o ato das bifurcações'),
   ('Dezembro não pergunta se você está pronta. Ele vem.', 'tira a desculpa de preparo'),
  ],
  enigma='A máscara vira a outra versão de você. No reel das duas cenas, a mulher '
         'mascarada é a linha que não mudou nada. Quando a máscara sai, aparece a '
         'mesma pessoa — e é esse o susto.',
  pede='A mais fácil de gravar: pouca produção, muito roteiro e edição. Você aparece '
       'menos e o argumento aparece mais.',
  risco='É a mais fria das três — vende bem e constrói marca devagar. E tem uma '
        'armadilha: se as duas linhas virarem caricatura (a coitada × a vencedora), '
        'ofende exatamente quem está na linha ruim e precisa comprar.'),
]
