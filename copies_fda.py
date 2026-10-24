#!/usr/bin/env python3
"""As 153 copies da OPERAÇÃO FIM DE ANO — 3 por post da Duda, nos 51.

Cada trio adapta a MECÂNICA do post dela (o que aquele post faz) para a nossa
oferta e para o tom medido da @izabelalaila: grandeza e transbordo, sonho,
fome, nada herdado, o trabalho devolve, não esperar a hora perfeita.

⚠️ Os três primeiros do enigma são os vídeos que ela desenhou: elevador de
   preto com máscara → a máscara sai → sala de reunião com o telão.

Índice = a ordem cronológica dos 51 posts (posts-lancamento.json).
Formato: (ângulo, palavra-chave, copy).
"""

C = {}

# ══ 1 · O ENIGMA (0–6) ════════════════════════════════════════════════════
C[0] = [  # Duda: «o número 3 nunca fez tanto sentido» — enigma com número
 ('O elevador', 'OPERAÇÃO',
  '<i>[reel: ela sozinha no elevador, toda de preto, máscara preta. Sem falar. '
  'A porta fecha. Na tela, só a data piscando: 01.11]</i><br><br>'
  'Começou.<br><br>Comenta <b>OPERAÇÃO</b> que eu te conto primeiro. 🖤'),
 ('Os 60 dias', '60 DIAS',
  '<b>60 dias.</b><br><br>É o que separa quem vira o ano de quem recomeça em '
  'janeiro pela quarta vez.<br><br>Na nossa área o ano inteiro se decide em '
  'novembro e dezembro — e eu vou mostrar exatamente como.<br><br>'
  'Comenta <b>60 DIAS</b> 👇'),
 ('Janeiro', 'JANEIRO',
  'Todo mundo promete que janeiro vai ser diferente.<br><br>'
  '<b>Quem é da área da beleza não espera janeiro.</b><br><br>'
  'A gente faz acontecer agora, enquanto a agenda enche sozinha.<br><br>'
  'Comenta <b>JANEIRO</b> e eu te explico por quê 👇'),
]
C[1] = [  # Duda: «como você decide lidar com essa CHUVA» — a escolha
 ('A máscara sai', 'OPERAÇÃO',
  '<i>[reel: mesmo elevador, mesma roupa. Ela leva a mão à máscara e tira — '
  'corta no meio do movimento, antes do rosto inteiro aparecer]</i><br><br>'
  '«Não é sobre esconder. É sobre o tempo certo de mostrar.»<br><br>'
  'Todo grande vencedor já pensou em parar. Eu escolhi continuar — e esse fim '
  'de ano vai ser a prova.<br><br>Comenta <b>OPERAÇÃO</b> 🖤'),
 ('Os dois dezembros', 'QUAL',
  'Existem dois dezembros.<br><br>O que te deixa exausta e sem dinheiro.<br>'
  'E o que vira o seu ano.<br><br>É a mesma agenda cheia. O que muda é o que '
  'você fez em <b>novembro</b>.<br><br>Comenta <b>QUAL</b> você quer 👇'),
 ('A chuva', 'CHUVA',
  'Dezembro é chuva: vem com ou sem você pronta.<br><br>'
  'Tem quem se molhe reclamando. E tem quem já tenha montado o telhado em '
  'novembro.<br><br><b>Dezembro não pergunta se você está pronta. Ele vem.</b>'
  '<br><br>Comenta <b>CHUVA</b> 👇'),
]
C[2] = [  # Duda: «o SEU normal depende do seu AMBIENTE»
 ('O telão', 'OPERAÇÃO',
  '<i>[reel: a porta do elevador abre na sala de reunião. A equipe inteira '
  'sentada, de preto, esperando. Ela entra e senta na cabeceira. O telão '
  'acende: OPERAÇÃO FIM DE ANO]</i><br><br>'
  '<b>Imagina ser tão grande ao ponto de engrandecer outras pessoas também.</b>'
  '<br><br>Esse fim de ano eu não vou subir sozinha.<br><br>'
  'Comenta <b>OPERAÇÃO</b> que eu te mostro o plano 🖤'),
 ('O normal', 'NORMAL',
  'O seu normal depende de quem está em volta.<br><br>'
  'Tem gente que acha normal passar dezembro inteiro de pé e fechar o mês sem '
  'saber se sobrou.<br><br>Isso não é normal. <b>Isso é falta de conta.</b>'
  '<br><br>Comenta <b>NORMAL</b> 👇'),
 ('Sozinha', 'SOZINHA',
  'Você consegue atender dezembro sozinha.<br><br>A pergunta é outra: '
  '<b>você consegue FATURAR dezembro sozinha?</b><br><br>'
  'Sozinha você atende. Com time, você fatura.<br><br>Comenta <b>SOZINHA</b> 👇'),
]
C[3] = [  # Duda: «87 body splashs» — o excesso vira espelho
 ('O estoque', 'ESTOQUE',
  'Quantos produtos você comprou esse ano achando que era isso que faltava?'
  '<br><br>Quase nunca é o produto. É o <b>preço</b> que você cobra por usar ele.'
  '<br><br>Comenta <b>ESTOQUE</b> 👇'),
 ('O movimento', 'CHEIO',
  '<b>Salão cheio não é salão lucrativo.</b><br><br>'
  'Dá pra atender 12 por dia em dezembro e fechar o mês no vermelho. '
  'Eu já fechei — e demorei pra entender por quê.<br><br>'
  'Comenta <b>CHEIO</b> se você já sentiu isso 👇'),
 ('O que falta', 'FALTA',
  'Não falta cliente no seu fim de ano.<br><br>Falta <b>preço certo</b>, '
  'falta <b>mão</b> e falta <b>plano</b>.<br><br>E as três coisas se resolvem '
  'em novembro — não em dezembro.<br><br>Comenta <b>FALTA</b> 👇'),
]
C[4] = [  # Duda: «quem mais tem o marido igual ao meu» — vida/meme
 ('O bastidor', None,
  '<i>[vídeo leve: o bastidor da equipe montando a sala, rindo, erro de '
  'gravação]</i><br><br>Por trás de toda operação séria tem um time que ri '
  'junto.<br><br>Marca aqui quem você levaria pro seu time 👇'),
 ('A rotina de novembro', None,
  'Novembro na área da beleza é assim: você acorda cedo, atende o dia inteiro, '
  'e ainda tem que pensar no que vem.<br><br>Quem é da área sabe. 🖤'),
 ('O meme do fim de ano', None,
  'Dezembro chegando e a gente: «esse ano eu me organizo».<br><br>'
  'Marca a amiga que fala isso todo ano 😂'),
]
C[5] = [  # Duda: «digita de 1 a 15 por qual você vai começar AMANHÃ»
 ('Os 4 buracos', 'DIAGNÓSTICO',
  'Tem 4 buracos por onde o fim de ano escapa:<br>1 · preço errado<br>'
  '2 · sem gente<br>3 · sem plano de conteúdo<br>4 · sem saber o que sobra'
  '<br><br>Comenta o <b>NÚMERO</b> do seu e eu te digo por onde começar 👇'),
 ('A lista de novembro', 'LISTA',
  'Fiz a lista do que PRECISA estar pronto até 15 de novembro pra dezembro '
  'não te atropelar.<br><br>São 7 coisas. Nenhuma delas é postar mais.<br><br>'
  'Comenta <b>LISTA</b> 👇'),
 ('Por onde começar', 'COMEÇO',
  'Se você só puder arrumar UMA coisa antes de dezembro, arruma o <b>preço</b>.'
  '<br><br>Porque agenda cheia com preço errado é só cansaço com testemunha.'
  '<br><br>Comenta <b>COMEÇO</b> 👇'),
]
C[6] = [  # Duda: «atenção: altas chances de você se identificar»
 ('O aviso', 'EU',
  '🚨 Altas chances de você se identificar com esse post.<br><br>'
  'Se em janeiro desse ano você olhou pra trás e pensou «trabalhei tanto, '
  'cadê o dinheiro?» — esse fim de ano é a sua chance de não repetir.<br><br>'
  'Comenta <b>EU</b> 👇'),
 ('O espelho de janeiro', 'JANEIRO',
  'Lembra de janeiro?<br><br>A conta do cartão, a agenda vazia, e a sensação '
  'de que dezembro passou e você só trabalhou.<br><br>'
  '<b>Dezembro é onde isso se decide.</b> Já começou.<br><br>'
  'Comenta <b>JANEIRO</b> 👇'),
 ('Vai incomodar', 'POSSO',
  'Vou falar uma coisa essa semana que vai incomodar muita cabeleireira.'
  '<br><br>Mas é o que me fez parar de terminar dezembro cansada e começar '
  'a terminar dezembro <b>rica</b>.<br><br>Comenta <b>POSSO</b> 👇'),
]

# ══ 2 · A DOR COM NOME (7–23) ═════════════════════════════════════════════
C[7] = [  # Duda: «3 problemas diferentes do mesmo jeito · DIAGNÓSTICO»
 ('A conta que ninguém faz', 'CONTA',
  'Você sabe quanto <b>sobra por hora</b> da sua mão numa progressiva?<br><br>'
  'Não é o preço. É o preço menos o produto, menos o aluguel, menos a luz — '
  'dividido pelas horas que você ficou de pé.<br><br>'
  'Fiz uma calculadora que faz essa conta em 3 minutos.<br><br>'
  'Comenta <b>CONTA</b> 👇'),
 ('Três buracos, um remendo', 'DIAGNÓSTICO',
  'Talvez você esteja tentando resolver <b>três problemas diferentes do mesmo '
  'jeito</b>: preço, gente e plano.<br><br>Postar mais não conserta preço. '
  'Baixar preço não conserta falta de gente.<br><br>'
  'Comenta <b>DIAGNÓSTICO</b> e eu te digo qual é o seu 👇'),
 ('O dia 10 de janeiro', '10',
  'O pior dia do ano não é 31 de dezembro.<br><br>É <b>10 de janeiro</b>, '
  'quando a conta chega e você descobre que trabalhou o fim de ano inteiro '
  'e não sobrou.<br><br>Comenta <b>10</b> 👇'),
]
C[8] = [  # Duda: «todos os mais votados usam redes sociais» — carona/dado
 ('O dado', None,
  'Dezembro responde por boa parte do ano de um salão — e é o único mês em que '
  'a cliente procura você, em vez de você procurar ela.<br><br>'
  'Quem entende isso para de brigar por desconto em março.'),
 ('A comparação', None,
  'Todo salão que você admira tem uma coisa em comum: <b>eles não improvisam '
  'dezembro</b>.<br><br>Quando chega novembro, o plano já existe.'),
 ('O que elas fazem', None,
  'O que as donas de salão que faturam alto fazem em novembro?<br><br>'
  'Contratam. Reprecificam. E deixam o conteúdo de dezembro pronto.<br><br>'
  'Nada disso dá pra fazer no dia 20.'),
]
C[9] = [  # Duda: «PAVOR da número 5» — lista curta de alcance
 ('Os 5 erros', '5',
  '5 erros que fazem o fim de ano render menos:<br>1 · dar desconto em dezembro'
  '<br>2 · atender sozinha<br>3 · não aumentar preço<br>4 · não separar o 13º'
  '<br>5 · achar que janeiro conserta<br><br><b>Pavor do número 5.</b>'),
 ('O erro mais caro', None,
  'O erro mais caro do fim de ano não é cobrar barato.<br><br>'
  'É <b>não saber</b> que está cobrando barato.'),
 ('O que não fazer', None,
  'Dezembro não é mês de promoção. É mês de <b>preço cheio</b>.<br><br>'
  'Quem dá desconto no único mês em que a cliente paga sem reclamar, '
  'paga pra trabalhar.'),
]
C[10] = [  # Duda: «seu conteúdo não tá dando errado» — a tese de graça
 ('A tese', 'OPERAÇÃO',
  'Seu fim de ano não vai dar errado por falta de esforço.<br><br>'
  'Vai dar errado porque <b>esforço sem preço certo é só cansaço</b>, e '
  '<b>agenda cheia sem time é teto</b>.<br><br>São três coisas diferentes: '
  'marketing, preço e gente. Cada uma tem a sua conta.<br><br>'
  'Comenta <b>OPERAÇÃO</b> 👇'),
 ('Não é você', 'ONDE',
  'Você não é ruim de gestão.<br><br>Você só nunca sentou pra fazer a conta — '
  'porque ninguém te ensinou qual é.<br><br>Comenta <b>ONDE</b> que eu te mostro '
  'onde o seu dinheiro está vazando 👇'),
 ('Três contas', 'TRÊS',
  'Pra virar o fim de ano você precisa de três números:<br>'
  '• quanto <b>sobra</b> por hora da sua mão<br>'
  '• quanto cabe na sua agenda <b>sozinha</b><br>'
  '• quanto cabe <b>com mais uma pessoa</b><br><br>'
  'Comenta <b>TRÊS</b> 👇'),
]
C[11] = [  # Duda: «vida normal não é vida insuficiente» — inspira
 ('Algo grande', None,
  'Você está criando algo grande, mesmo quando parece pequeno.<br><br>'
  'Cada cliente que volta, cada mês que fecha, cada vez que você não desistiu — '
  'isso é construção.<br><br>E esse fim de ano é a hora de colher. 🖤'),
 ('Sem herdar', None,
  '<b>Nada herdado, tudo conquistado.</b><br><br>'
  'Ninguém te deu salão, cliente ou cadeira. Você construiu.<br><br>'
  'Agora é hora de cobrar o preço de quem construiu.'),
 ('Não mude de sonho', None,
  'Recalcule a rota, mude a estratégia, mude de produto se precisar.<br><br>'
  '<b>Mas não mude de sonho.</b>'),
]
C[12] = [  # Duda: «a estratégia da CEBOLA» — ensina algo pequeno e batiza
 ('A conta de três camadas', 'CAMADAS',
  'A conta do seu serviço tem 3 camadas:<br>'
  '🧅 o produto que você gasta<br>🧅 o custo fixo que cabe nele<br>'
  '🧅 o que sobra pra sua mão<br><br>'
  'Quase todo mundo só enxerga a primeira.<br><br>Comenta <b>CAMADAS</b> 👇'),
 ('A escada de dezembro', 'ESCADA',
  'Dezembro tem 3 degraus: <b>preço</b>, <b>gente</b> e <b>plano</b>.<br><br>'
  'Pular um não adianta — você cai do mesmo jeito, só mais tarde.<br><br>'
  'Comenta <b>ESCADA</b> 👇'),
 ('O método dos 60', '60',
  'Chamo de Operação porque tem data de início e data de fim: '
  '<b>01/11 a 31/12</b>.<br><br>Não é um curso que você faz quando der. '
  'É uma operação que acontece agora.<br><br>Comenta <b>60</b> 👇'),
]
C[13] = [  # Duda: «Prazer, Duda» — se apresenta no meio
 ('Prazer, Izabela', None,
  'Pra quem chegou agora: prazer, eu sou a Izabela. 🖤<br><br>'
  'Comecei atendendo sozinha. Hoje tenho equipe, POP e já atendi '
  '32 clientes de progressiva num único dia.<br><br>'
  '<b>Nada herdado, tudo conquistado.</b> E eu vou te mostrar o caminho.'),
 ('O que já construí', None,
  'Mais de 3 mil mulheres já aprenderam comigo a montar equipe, sair do '
  'operacional e lotar a agenda.<br><br>'
  'Transbordei na vida delas o que testei aqui dentro.<br><br>'
  'Agora vem a maior operação de todas.'),
 ('De onde eu vim', None,
  'Já passei o fim de ano inteiro de pé, atendendo, feliz com a agenda cheia — '
  'e chorei em janeiro quando fiz a conta.<br><br>'
  'Eu sei exatamente onde dói. Por isso essa operação existe.'),
]
C[14] = [  # Duda: «você não é ruim em conteúdo, gasta energia no lugar errado»
 ('O lugar errado', 'ENERGIA',
  'Você gasta energia correndo atrás de cliente nova em novembro.<br><br>'
  'E dezembro inteiro atendendo por um preço que você fez em março.<br><br>'
  'Comenta <b>ENERGIA</b> 👇'),
 ('O preço de março', 'PREÇO',
  'Seu preço é de quando? <b>Março?</b><br><br>'
  'O produto subiu, a luz subiu, o aluguel subiu. Só o seu preço ficou parado.'
  '<br><br>Comenta <b>PREÇO</b> 👇'),
 ('O que não é culpa sua', 'ONDE',
  'Não é falta de esforço — você já trabalha demais.<br><br>'
  '<b>É falta de conta.</b> E conta se resolve numa tarde.<br><br>'
  'Comenta <b>ONDE</b> 👇'),
]
C[15] = [  # Duda: «EU SOU DESSAS» — leve
 ('Eu sou dessas', None,
  'Eu sou dessas que já reprecificou tudo em novembro e dorme tranquila '
  'em dezembro.<br><br>E você, é dessas ou das que descobre em janeiro? 👀'),
 ('Time dos que planejam', None,
  'Tem o time que improvisa dezembro.<br>E o time que chega em novembro '
  'com tudo pronto.<br><br>Qual é o seu? 🖤'),
 ('Confesso', None,
  'Confesso: eu já fui das que achava que agenda cheia era sinônimo de '
  'mês bom.<br><br>Levei um susto quando fiz a conta.'),
]
C[16] = [  # Duda: «olhar pra menina que você foi» — data/conexão
 ('A menina que você foi', None,
  'Olha pra menina que começou atendendo na sala de casa.<br><br>'
  'Pra ela, o que hoje te parece pouco já era um sonho gigante.<br><br>'
  'Esse fim de ano é por ela também. 🖤'),
 ('O sonho grande', None,
  '<b>Grande sonho da área da beleza não se realiza em janeiro.</b><br><br>'
  'Se realiza em dezembro — quando a agenda enche e o preço está certo.'),
 ('Engrandecer', None,
  'Imagina ser tão grande ao ponto de engrandecer outras pessoas também.<br><br>'
  'É isso que uma equipe faz: multiplica o que você construiu sozinha.'),
]
C[17] = [  # Duda: carona na Viih Tube — assunto quente + autoridade
 ('A carona', 'VIEWS',
  'Vi uma cabeleireira bater <b>300 mil views</b> essa semana — e ela me '
  'contou que não entrou uma cliente.<br><br>Alcance não paga aluguel. '
  '<b>Agenda com preço certo paga.</b><br><br>Comenta <b>VIEWS</b> 👇'),
 ('A análise', 'ANÁLISE',
  'Isso não é ataque a ninguém. É análise de quem está <b>atrás da cadeira</b>, '
  'com equipe e com conta pra fechar.<br><br>Comenta <b>ANÁLISE</b> 👇'),
 ('O que paga a conta', 'PAGA',
  'Viralizar é ótimo. <b>Depender disso é outra história.</b><br><br>'
  'O que paga a conta de janeiro é a cliente que sentou na sua cadeira em '
  'dezembro, por um preço que fecha.<br><br>Comenta <b>PAGA</b> 👇'),
]
C[18] = [  # Duda: «o que tem de errado com o SEU conteúdo» — diagnóstico direto
 ('O diagnóstico', 'CONTA',
  'Quer saber se o SEU preço está certo?<br><br>'
  'Fiz uma calculadora: você põe o serviço, o produto, o tempo e o valor — '
  'e ela te diz <b>quanto sobra por hora da sua mão</b>.<br><br>'
  'É grátis e leva 3 minutos. Comenta <b>CONTA</b> 👇'),
 ('O número que dói', 'HORA',
  'Tem um número que quase ninguém da nossa área conhece: '
  '<b>quanto você ganha por hora</b>.<br><br>'
  'Quando eu descobri o meu, mudei a tabela inteira na mesma semana.<br><br>'
  'Comenta <b>HORA</b> 👇'),
 ('Terceira vez', 'CONTA',
  'Vou repetir porque é importante: <b>faça a conta antes de dezembro.</b>'
  '<br><br>Depois do dia 20 você não muda mais preço — só aguenta.<br><br>'
  'Comenta <b>CONTA</b> 👇'),
]
C[19] = [  # Duda: «parece que todo mundo já chegou»
 ('A comparação', None,
  'Abre o Instagram e parece que todo mundo já chegou.<br><br>'
  'Não chegou. A maioria está igual a você: agenda cheia, cabeça cheia e '
  'conta apertada.<br><br>A diferença vai ser o que você fizer nos próximos 60 dias.'),
 ('O seu normal', 'NORMAL',
  'O seu normal não é o normal dela.<br><br>Mas o fim de ano é o mesmo pra '
  'todo mundo: <b>dois meses</b>.<br><br>Comenta <b>NORMAL</b> 👇'),
 ('Sem pressa, com prazo', None,
  'Não é sobre correr. É sobre ter <b>prazo</b>.<br><br>'
  'E o prazo desse ano termina em 31 de dezembro.'),
]
C[20] = [  # Duda: mantra curto
 ('O mantra', None,
  'Repete comigo: <b>o trabalho devolve.</b><br><br>'
  'Mas devolve pra quem cobra o preço certo. 🖤'),
 ('Fome', None,
  'A vida não é sobre quem tem mais talento. É sobre <b>quem tem mais fome</b>.'
  '<br><br>Fome de virar o ano. Fome de não repetir janeiro.'),
 ('Continuar', None,
  'Todo grande vencedor já pensou em parar.<br><br>'
  'Mas escolheu continuar — e continuou <b>com estratégia</b>, não só com força.'),
]
C[21] = [  # Duda: «a humilhação vira ouro» + puxa pro link
 ('Vai virar ouro', None,
  'Todo mês apertado que você passou vai virar ouro na sua mão — '
  'se você aprender a <b>fazer a conta</b>.<br><br>'
  'E eu vou te ensinar nesses 60 dias.'),
 ('A virada', 'VIRAR',
  'Já chorei em janeiro olhando pro extrato depois de um dezembro lotado.'
  '<br><br>Hoje dezembro é o mês que eu mais espero.<br><br>'
  'O que mudou não foi a agenda. Foi a <b>conta</b>.<br><br>'
  'Comenta <b>VIRAR</b> 👇'),
 ('Contar a sua', None,
  'Se você soubesse contar a sua virada, metade das suas clientes já teria '
  'indicado você.<br><br>Isso também está no planner dos 60 dias.'),
]
C[22] = [  # Duda: «se chegou até o final, você já sabe o que comentar»
 ('Chegou até o fim', 'OPERAÇÃO',
  'Se você chegou até aqui, é porque esse fim de ano importa pra você.'
  '<br><br>Então você já sabe o que comentar 👇<br><br><b>OPERAÇÃO</b> 🖤'),
 ('O teste', 'EU TOPO',
  'Teste rápido: você já sabe quanto quer faturar em dezembro?<br><br>'
  'Se a resposta foi «não sei, o máximo que der» — a gente precisa conversar.'
  '<br><br>Comenta <b>EU TOPO</b> 👇'),
 ('A fofoca boa', 'FOFOCA',
  'Vou contar uma fofoca: já tem gente montando equipe pra dezembro '
  '<b>desde setembro</b>.<br><br>E você?<br><br>Comenta <b>FOFOCA</b> 👇'),
]
C[23] = [  # Duda: «conteúdo tem que virar rotina» — convite ao desafio
 ('60 dias comigo', 'OPERAÇÃO',
  'Não adianta eu te dar uma dica solta.<br><br>'
  'O que vira o ano é <b>60 dias seguidos</b> com o plano certo: preço, gente, '
  'conteúdo e caixa.<br><br>É isso que é a Operação Fim de Ano.<br><br>'
  'Comenta <b>OPERAÇÃO</b> 👇'),
 ('Rotina, não surto', 'ROTINA',
  'Fim de ano bom não é surto de dezembro. É <b>rotina de novembro</b>.'
  '<br><br>Comenta <b>ROTINA</b> 👇'),
 ('Identidade', 'EU QUERO',
  'Chega uma hora que organizar o salão deixa de ser tarefa e vira <b>quem você é</b>.'
  '<br><br>É nessa mulher que eu quero te transformar em 60 dias.<br><br>'
  'Comenta <b>EU QUERO</b> 👇'),
]

# ══ 3 · A ENTREGA DE GRAÇA (24–36) ═══════════════════════════════════════
# ⚠️ A isca é SEMPRE a calculadora, de ângulos diferentes. Ela diz SE o preço
#    está certo — nunca QUAL é o certo. O certo é o 1º dia da mentoria.
C[24] = [  # Duda: «3 sequências prontas de stories, pra postar HOJE»
 ('A calculadora', 'CONTA',
  'Comenta <b>CONTA</b> que eu te mando a <b>calculadora de precificação</b>.'
  '<br><br>Você põe o serviço, o produto, o tempo e o que cobra — e ela te diz '
  '<b>quanto sobra por hora da sua mão</b>.<br><br>'
  'É grátis, leva 3 minutos, e você vai levar um susto 👇'),
 ('A ficha dos 60 dias', 'FICHA',
  'Fiz uma ficha de uma página com <b>as 7 coisas que precisam estar prontas '
  'até 15 de novembro</b>.<br><br>Imprime, marca o que já tem, e você vê na '
  'hora onde está atrasada.<br><br>Comenta <b>FICHA</b> 👇'),
 ('Os 3 preços', 'OS 3',
  'Todo salão tem 3 preços:<br>• o que você <b>cobra</b><br>'
  '• o que você <b>acha</b> que sobra<br>• o que <b>realmente</b> sobra'
  '<br><br>A calculadora mostra o terceiro. Comenta <b>OS 3</b> 👇'),
]
C[25] = [  # Duda: «gancho visual — chamei sua atenção?» — ensina usando
 ('Prova no próprio post', None,
  'Reparou que você leu até aqui?<br><br>Isso é gancho — e está no planner '
  'de 60 dias, pronto pra você copiar.'),
 ('O que é um gancho', None,
  'Gancho não é frase bonita. É a frase que faz a cliente <b>parar o dedo</b>.'
  '<br><br>No planner tem 30 prontos pra novembro e dezembro.'),
 ('Mostra como faz', None,
  'A primeira linha decide tudo. O resto do post só entrega o que ela prometeu.'
  '<br><br>Testa hoje: escreve a frase mais forte primeiro.'),
]
C[26] = [  # Duda: «comenta ESTRUTURA que eu te mando 3 conteúdos prontos» (o maior)
 ('A calculadora, de novo', 'CONTA',
  'Mermã, comenta <b>CONTA</b> que eu te mando a calculadora de precificação.'
  '<br><br>Ela não vai te dizer o preço certo — isso é a Operação.<br>'
  'Ela vai te dizer <b>se o seu está errado</b>.<br><br>'
  'E pra 8 em cada 10, está 👇'),
 ('Copia e usa hoje', 'PLANNER',
  'Comenta <b>PLANNER</b> que eu te mando <b>3 posts prontos</b> de novembro — '
  'o texto na íntegra, do jeito que eu uso.<br><br>'
  'Copia, troca o nome do seu salão, posta hoje à noite 👇'),
 ('A tabela em branco', 'TABELA',
  'Uma tabela de uma página pra você listar seus serviços e descobrir qual '
  'deles está <b>pagando pra trabalhar</b>.<br><br>Comenta <b>TABELA</b> 👇'),
]
C[27] = [  # Duda: «a salada de R$90» — carona em preço
 ('O preço que choca', None,
  'Um prato de R$ 90 vira assunto, e um alisamento de R$ 400 vira «caro».'
  '<br><br>A diferença não é o valor. É <b>quem sustenta o preço sem pedir '
  'desculpa</b>.'),
 ('Posicionamento', None,
  'Preço alto sem entrega é arrogância.<br>'
  'Preço baixo com entrega grande é <b>burrice financeira</b>.<br><br>'
  'O certo está na conta — não no achismo.'),
 ('O que o caro ensina', None,
  'Quem cobra caro não cobra pelo produto. Cobra pela <b>certeza</b> que entrega.'
  '<br><br>E certeza se constrói com POP, equipe treinada e padrão.'),
]
C[28] = [  # Duda: «faltam 4 DIAS» — primeiro relógio
 ('O relógio começa', 'OPERAÇÃO',
  'Ser dona de salão é viver entre «eu nasci pra isso» e «quem me mandou».'
  '<br><br>Mas tem uma data que não muda: <b>31 de dezembro</b>.<br><br>'
  'E dela até aqui são 60 dias. Comenta <b>OPERAÇÃO</b> 👇'),
 ('Contagem', 'DIAS',
  '⏳ Faltam <b>poucos dias</b> pra eu abrir a Operação Fim de Ano.<br><br>'
  'Quem entra agora começa novembro com o plano na mão. Quem entra em '
  'dezembro entra correndo.<br><br>Comenta <b>DIAS</b> 👇'),
 ('A janela', 'JANELA',
  'A janela de virar o ano na beleza é curta: abre em novembro e fecha no '
  'dia 31.<br><br>Depois disso é janeiro — e janeiro não salva ninguém.<br><br>'
  'Comenta <b>JANELA</b> 👇'),
]
C[29] = [  # Duda: «por que pulam seus stories» — a trava exata
 ('Por que ninguém agenda', 'AGENDA',
  'Suas clientes veem seus stories e não agendam.<br><br>'
  'Não é o algoritmo. É que você mostra o <b>trabalho</b> e nunca mostra '
  'a <b>vaga</b>.<br><br>Comenta <b>AGENDA</b> 👇'),
 ('A trava de escrever', 'TRAVA',
  'Você sabe que precisa postar. Trava na hora de escrever.<br><br>'
  'Por isso o planner vem com o texto <b>pronto</b> — não com «dicas».<br><br>'
  'Comenta <b>TRAVA</b> 👇'),
 ('Última chamada da isca', 'CONTA',
  'Última vez que eu mando a calculadora antes de abrir a Operação.<br><br>'
  'Comenta <b>CONTA</b> 👇'),
]
C[30] = [  # Duda: «repetição ensina a lidar com o medo» — convite disfarçado
 ('Repetição', None,
  'Com a quantidade certa de repetições, seu corpo aprende a não ter medo.'
  '<br><br>Postar todo dia em novembro é isso: treino pra dezembro.'),
 ('Eu vou', 'COMIGO',
  'Eu vou postar todo dia nesses 60 dias.<br><br>Se você for também, '
  'comenta <b>COMIGO</b> que eu te mando o calendário 👇'),
 ('Não espera estar pronta', None,
  '<b>Não espera a hora perfeita.</b><br><br>'
  'Dezembro não pergunta se você está pronta. Ele vem.'),
]
C[31] = [  # Duda: «não precisa esperar janeiro» — tira a desculpa (o jargão dela!)
 ('Não espera janeiro', 'JANEIRO',
  'Você não precisa esperar janeiro, a segunda-feira perfeita ou a rotina ideal.'
  '<br><br><b>Quem é da área da beleza não espera janeiro.</b><br>'
  'A gente faz acontecer no fim do ano.<br><br>Comenta <b>JANEIRO</b> 👇'),
 ('Onde o sonho se realiza', 'SONHO',
  'Grande sonho na nossa área não se realiza em janeiro.<br><br>'
  '<b>Se realiza em dezembro.</b><br><br>Se você perde esse momento, '
  'você perdeu o ano.<br><br>Comenta <b>SONHO</b> 👇'),
 ('Começar antes de estar pronta', 'COMEÇO',
  'Começar do zero não é fácil — mas é aí que você descobre que é feita de '
  'coragem.<br><br>Comenta <b>COMEÇO</b> 👇'),
]
C[32] = [  # Duda: «essa regra MUDA a vida» — humor leve
 ('A regra', None,
  'Regra que mudou meu fim de ano: <b>nada de desconto em dezembro</b>.'
  '<br><br>Concorda? 🔥'),
 ('A outra regra', None,
  'Segunda regra: a agenda de dezembro fecha em novembro.<br><br>'
  'Quem abre agenda em dezembro só pega sobra.'),
 ('A terceira', None,
  'Terceira regra: você não atende de graça em dezembro «pra fidelizar».'
  '<br><br>Fideliza com padrão, não com preço.'),
]
C[33] = [  # Duda: «eu fui desafiada e isso mudou minha vida» — 1ª menção à oferta
 ('A origem', 'OPERAÇÃO',
  'No meu começo, eu passei um fim de ano inteiro de pé e chorei em janeiro '
  'fazendo a conta.<br><br>Alguém me sentou e me mostrou os números. '
  'Aquilo mudou a minha vida.<br><br>'
  '<b>Agora é a minha vez de fazer isso por você.</b><br><br>'
  'Comenta <b>OPERAÇÃO</b> 👇'),
 ('Transbordar', 'OPERAÇÃO',
  'Eu transbordei na vida de mais de 3 mil mulheres o que testei aqui dentro.'
  '<br><br>Esse fim de ano vai ser o maior de todos — e eu não vou subir sozinha.'
  '<br><br>Comenta <b>OPERAÇÃO</b> 👇'),
 ('O que vem aí', 'PLANO',
  'Operação Fim de Ano: <b>60 dias</b>, quatro frentes — marketing, preço, '
  'time e caixa.<br><br>Começa 01/11. Comenta <b>PLANO</b> 👇'),
]
C[34] = [  # Duda: «tá, mas eu posto o quê?» + convida pro ao vivo
 ('O planner resolve', 'PLANNER',
  'E se o seu problema é «tá, mas eu posto o quê em novembro?» —<br><br>'
  'o planner da Operação tem <b>os 60 dias escritos</b>. Você abre, copia e posta.'
  '<br><br>Comenta <b>PLANNER</b> 👇'),
 ('Amanhã eu mostro', 'AO VIVO',
  'Amanhã às 20h eu abro a Operação Fim de Ano <b>ao vivo</b> e mostro o plano '
  'inteiro — dia por dia.<br><br>Comenta <b>AO VIVO</b> que eu te mando o link 👇'),
 ('O calendário', 'CALENDÁRIO',
  'Montei o calendário de 60 dias: o que postar, quando aumentar o preço e '
  'quando contratar.<br><br>Comenta <b>CALENDÁRIO</b> 👇'),
]
C[35] = [  # Duda: conteúdo leve que emenda no ao vivo
 ('O bastidor que emenda', 'AO VIVO',
  '<i>[bastidor leve do salão em novembro]</i><br><br>'
  'Você veio pelo vídeo, mas o recado é outro: <b>amanhã, 20h</b>, eu abro '
  'a Operação ao vivo.<br><br>Comenta <b>AO VIVO</b> 👇'),
 ('O que vou mostrar', 'AO VIVO',
  'No ao vivo de amanhã eu mostro:<br>• a conta que eu faço antes de dezembro'
  '<br>• como contratei a primeira auxiliar<br>• o calendário dos 60 dias'
  '<br><br>Comenta <b>AO VIVO</b> 👇'),
 ('É de graça', 'AO VIVO',
  'O ao vivo é de graça e não fica gravado.<br><br>'
  'Quem estiver lá vai sair com a conta feita.<br><br>Comenta <b>AO VIVO</b> 👇'),
]
C[36] = [  # Duda: «insegurança tem cheiro» — último enigma antes de abrir
 ('A insegurança', 'OPERAÇÃO',
  'Insegurança tem cheiro — e a cliente sente no seu preço.<br><br>'
  'Quem não sabe quanto sobra, cobra com medo.<br><br>'
  'Comenta <b>OPERAÇÃO</b> se você quer entrar em dezembro sem medo 👇'),
 ('Falta pouco', 'OPERAÇÃO',
  'Falta pouco pra abrir.<br><br>'
  'E quando abrir, a turma de novembro fecha rápido — porque eu só consigo '
  'acompanhar um número de pessoas por vez.<br><br>Comenta <b>OPERAÇÃO</b> 👇'),
 ('O último aviso antes', 'AVISA',
  'Quem comentar <b>AVISA</b> eu chamo no direct antes de qualquer post 👇'),
]

# ══ 4 · O AO VIVO (37–39) ════════════════════════════════════════════════
C[37] = [  # Duda: «ela acreditou antes de ter garantia» — chama pro ao vivo
 ('Hoje é o dia', 'AO VIVO',
  'Por trás de toda mulher que decidiu empreender, tem uma versão dela que '
  'acreditou <b>antes de ter garantia</b>.<br><br>'
  '<b>Hoje às 20h</b> eu abro a Operação Fim de Ano ao vivo.<br><br>'
  'Comenta <b>AO VIVO</b> que eu te mando o link 👇'),
 ('Engrandecer', 'AO VIVO',
  'Imagina ser tão grande ao ponto de engrandecer outras pessoas também.'
  '<br><br>É isso que eu vou mostrar hoje, 20h.<br><br>Comenta <b>AO VIVO</b> 👇'),
 ('Última chamada', 'AO VIVO',
  'Começa em 1 hora.<br><br>Leva papel, caneta e o seu preço de hoje — '
  'a gente vai fazer a conta junto.<br><br>Comenta <b>AO VIVO</b> 👇'),
]
C[38] = [  # Duda: lista rápida no dia do evento
 ('As 4 frentes', None,
  'As 4 frentes da Operação:<br>1 · marketing (o planner de 60 dias)<br>'
  '2 · preço (a conta que fecha)<br>3 · time (montar e treinar)<br>'
  '4 · caixa (não descobrir em janeiro)<br><br>'
  '<b>A 4ª é a principal</b> — e é a que ninguém faz.'),
 ('O que mais me perguntam', None,
  'A pergunta que mais chega aqui: «como você organiza a parte financeira '
  'do salão?»<br><br>Hoje, 20h, eu mostro.'),
 ('Sem enrolação', None,
  'Hoje não tem enrolação: 40 minutos, a conta feita e o plano na tela.'),
]
C[39] = [  # Duda: brincadeira de completar — alcance no dia
 ('Completa a frase', None,
  'Eu digo <b>OPERAÇÃO</b> e vocês dizem… 👇🖤'),
 ('Quem tá dentro', None,
  'Comenta aí de qual cidade você tá assistindo — quero ver o mapa dessa '
  'operação 🗺️🖤'),
 ('O time', None,
  'Marca a amiga que vai virar o fim de ano com você 👇'),
]

# ══ 5 · O CARRINHO ABERTO (40–50) ════════════════════════════════════════
C[40] = [  # Duda: «OFERTA DE PRÉ BLACK FRIDAY DISPONÍVEL» — abre
 ('Abriu', 'OPERAÇÃO',
  '🖤 <b>ABRIU A OPERAÇÃO FIM DE ANO.</b><br><br>'
  '60 dias comigo dentro do seu salão — de 01/11 a 31/12:<br>'
  '✔️ o planner com os 60 dias de conteúdo prontos<br>'
  '✔️ a tabela de preço refeita, com a conta que fecha<br>'
  '✔️ como montar e treinar seu time a tempo do pico<br>'
  '✔️ o caixa semanal, pra você não descobrir em janeiro<br><br>'
  '<b>Até sexta</b> com o valor de abertura.<br><br>'
  'Digita <b>OPERAÇÃO</b> que eu te mando o link 👇'),
 ('A conta da oferta', 'VALE',
  'Se a Operação te fizer acertar <b>R$ 50</b> no preço de cada serviço, '
  'e você atender 60 pessoas em dezembro —<br><br>ela se paga na primeira '
  'semana.<br><br>Digita <b>VALE</b> 👇'),
 ('Não é mais um curso', 'OPERAÇÃO',
  'Não é um curso que você assiste quando der.<br><br>'
  'É uma <b>operação com data</b>: começa 01/11, termina 31/12, e eu vou '
  'estar do lado.<br><br>Digita <b>OPERAÇÃO</b> 👇'),
]
C[41] = [  # Duda: «você tem até sexta» — prazo
 ('Até sexta', 'OPERAÇÃO',
  'Você tem até <b>SEXTA</b> pra entrar na Operação com o valor de abertura.'
  '<br><br>Depois de sexta, novembro já começou — e a gente perde a primeira '
  'semana.<br><br>Digita <b>OPERAÇÃO</b> 👇'),
 ('O prazo é agenda', 'TURMA',
  'O preço sobe sexta, e não é ameaça de vendedora: <b>é agenda</b>.<br><br>'
  'Dia 01/11 a turma começa junto, e quem entra depois entra correndo.<br><br>'
  'Digita <b>TURMA</b> 👇'),
 ('Quantas vagas', 'VAGA',
  'Eu acompanho de perto. Por isso a turma de novembro tem número fechado.'
  '<br><br>Digita <b>VAGA</b> pra saber se ainda tem 👇'),
]
C[42] = [  # Duda: Victoria's Secret — vende por dentro de assunto leve
 ('Reconhecimento', 'VISTA',
  'Nem sempre o que não tem reconhecimento é porque é ruim.<br><br>'
  'Seu salão não é pequeno. <b>Ele só não foi visto ainda.</b><br><br>'
  'E dezembro é o mês em que dá pra ser vista.<br><br>Digita <b>VISTA</b> 👇'),
 ('O caro', 'CARO',
  'Toda vez que você julga uma coisa «cara», você se limita sem perceber.'
  '<br><br>Digita <b>CARO</b> que eu te mostro a conta de quanto custa '
  '<b>não</b> fazer esse fim de ano direito 👇'),
 ('O palco', 'PALCO',
  'Dezembro é o único mês em que a cliente procura VOCÊ.<br><br>'
  'É o seu palco. A pergunta é se você vai subir preparada.<br><br>'
  'Digita <b>PALCO</b> 👇'),
]
C[43] = [  # Duda: «imaginar o que pode mudar se der certo»
 ('E se der certo', 'OPERAÇÃO',
  'A gente pensa tanto no que pode dar errado que esquece de imaginar o que '
  'muda <b>se der certo</b>.<br><br>Um dezembro com preço certo e time montado '
  'paga o ano inteiro.<br><br>Digita <b>OPERAÇÃO</b> 👇'),
 ('O sonho grande', 'SONHO',
  '<b>Grande sonho da beleza se realiza em dezembro.</b><br><br>'
  'A reforma, o carro, a viagem, a casa — tudo que você adiou esse ano cabe '
  'em dois meses bem feitos.<br><br>Digita <b>SONHO</b> 👇'),
 ('Imagina', 'IMAGINA',
  'Imagina ser tão grande ao ponto de engrandecer outras pessoas também.'
  '<br><br>Imagina fechar dezembro com time treinado e dinheiro no caixa.'
  '<br><br>Digita <b>IMAGINA</b> 👇'),
]
C[44] = [  # Duda: erro técnico vira bastidor — transparência
 ('O bastidor', 'OPERAÇÃO',
  '<i>[vídeo em que ela não consegue falar / erro de gravação]</i><br><br>'
  'Já que não deu pra falar, escrevi aqui:<br>'
  '✔️ a Operação abre até sexta<br>✔️ são 60 dias, de 01/11 a 31/12<br>'
  '✔️ quatro frentes: marketing, preço, time e caixa<br><br>'
  'Digita <b>OPERAÇÃO</b> 👇'),
 ('As dúvidas', 'DÚVIDA',
  'Juntei as 5 perguntas que mais chegaram no direct sobre a Operação.'
  '<br><br>Digita <b>DÚVIDA</b> que eu te respondo uma por uma 👇'),
 ('Sem filtro', None,
  'Não vou fingir que é fácil montar equipe em novembro.<br><br>'
  'É difícil. Mas é menos difícil que passar mais um janeiro fazendo conta '
  'de quanto faltou.'),
]
C[45] = [  # Duda: «qual você escolheu 1, 2 ou 3» — joguinho com escassez
 ('1, 2 ou 3', 'A MINHA',
  'Qual você escolheu?<br>1 · continuar como está<br>2 · tentar sozinha de novo'
  '<br>3 · virar o ano em 60 dias<br><br>No fim, as três dão no mesmo lugar '
  'em janeiro — menos uma.<br><br>Digita <b>A MINHA</b> 👇'),
 ('Não deixa pra janeiro', 'AGORA',
  '<b>Não deixa pra janeiro o que dá pra começar amanhã.</b><br><br>'
  'Em janeiro você vai estar cansada do Natal, com a agenda vazia e a conta '
  'do cartão chegando.<br><br>Digita <b>AGORA</b> 👇'),
 ('O relógio', 'RELÓGIO',
  '⏳ Faltam 2 dias pro valor de abertura acabar.<br><br>'
  'E 7 pra novembro começar.<br><br>Digita <b>RELÓGIO</b> 👇'),
]
C[46] = [  # Duda: «viralizar é ótimo, depender é outra história»
 ('O que paga', 'OPERAÇÃO',
  'Viralizar é ótimo. <b>Depender disso é outra história.</b><br><br>'
  'O que paga janeiro é a cliente que sentou na sua cadeira em dezembro, '
  'por um preço que fecha a conta.<br><br>Digita <b>OPERAÇÃO</b> 👇'),
 ('Alcance x agenda', 'AGENDA',
  'Alcance enche o feed. <b>Plano enche a agenda.</b><br><br>'
  'E preço certo enche o caixa.<br><br>Digita <b>AGENDA</b> 👇'),
 ('O trabalho devolve', 'DEVOLVE',
  'Lá na frente a conta fecha — <b>o trabalho devolve</b>.<br><br>'
  'Mas devolve pra quem cobra certo e não trabalha sozinha.<br><br>'
  'Digita <b>DEVOLVE</b> 👇'),
]
C[47] = [  # Duda: «você vai escolher um difícil de qualquer jeito»
 ('Os dois difíceis', 'ESCOLHO',
  'Você vai escolher um difícil de qualquer jeito.<br><br>'
  'O difícil de atravessar mais um dezembro sozinha, de pé, sem saber se sobra.'
  '<br>Ou o difícil de mudar o preço e contratar alguém em 60 dias.<br><br>'
  '<b>Os dois cansam. Só um termina diferente.</b><br><br>'
  'Digita <b>ESCOLHO</b> 👇'),
 ('Último dia', 'ÚLTIMO',
  '🖤 <b>Hoje é o último dia</b> do valor de abertura.<br><br>'
  'Amanhã a Operação continua — só que mais cara e com a primeira semana '
  'já andando.<br><br>Digita <b>ÚLTIMO</b> 👇'),
 ('Fome', 'FOME',
  'A vida não é sobre quem tem mais talento. É sobre <b>quem tem mais fome</b>.'
  '<br><br>Se você sente essa fome, digita <b>FOME</b> 👇'),
]
C[48] = [  # Duda: responde a objeção do «caro» publicamente
 ('A objeção', 'CARO',
  'Chegou esse comentário: «achei caro».<br><br>'
  'Caro é passar dezembro inteiro de pé e descobrir em janeiro que não sobrou.'
  '<br><br>Faz a conta comigo: digita <b>CARO</b> 👇'),
 ('Quanto custa não fazer', 'CUSTA',
  'Se você errar R$ 40 no preço de 60 atendimentos em dezembro, '
  'são <b>R$ 2.400</b> que você deixou na mesa — num mês só.<br><br>'
  'Digita <b>CUSTA</b> 👇'),
 ('Não é gasto', 'INVESTE',
  'Isso não sai do seu bolso. Sai do que você <b>já está perdendo</b> sem saber.'
  '<br><br>Digita <b>INVESTE</b> 👇'),
]
C[49] = [  # Duda: lista o que tem lá dentro
 ('O que tem dentro', 'OPERAÇÃO',
  'O que você leva na Operação Fim de Ano:<br>'
  '🖤 planner com os 60 dias de conteúdo prontos<br>'
  '🖤 calculadora + tabela de preço refeita com você<br>'
  '🖤 roteiro de contratação e o POP do meu salão<br>'
  '🖤 controle de caixa semanal e a meta quebrada por semana<br>'
  '🖤 acompanhamento até 31/12<br><br>Digita <b>OPERAÇÃO</b> 👇'),
 ('Pra quem é', 'PRA MIM',
  'É pra você que:<br>• atende sozinha e já não dá conta<br>'
  '• desconfia que o preço está errado<br>'
  '• quer montar time mas não sabe por onde<br>'
  '• não quer repetir janeiro<br><br>Digita <b>PRA MIM</b> 👇'),
 ('Pra quem NÃO é', None,
  'Não é pra quem quer fórmula mágica nem pra quem não vai executar.<br><br>'
  'São 60 dias de trabalho. <b>Ganha quem executa.</b>'),
]
C[50] = [  # Duda: prova social no último post
 ('A prova', None,
  '🖤 Fechamos a turma de novembro.<br><br>'
  'Obrigada a cada uma que decidiu não esperar janeiro.<br><br>'
  '<b>A operação começa dia 01.</b> Bora virar esse ano.'),
 ('O time montado', None,
  'Olha o tamanho dessa operação. 🖤<br><br>'
  'Imagina ser tão grande ao ponto de engrandecer outras pessoas também — '
  'é literalmente isso acontecendo aqui.'),
 ('Pra quem ficou de fora', 'FILA',
  'Ficou de fora? A próxima turma só em fevereiro — e aí o fim de ano '
  'já passou.<br><br>Digita <b>FILA</b> pra entrar na lista de espera 👇'),
]

assert len(C) == 51 and all(len(v) == 3 for v in C.values()), \
    f'faltam copies: {len(C)} posts, tamanhos {sorted({len(v) for v in C.values()})}'
COPIES_FDA = C
