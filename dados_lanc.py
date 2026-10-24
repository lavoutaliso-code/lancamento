#!/usr/bin/env python3
"""Os dados do nosso lançamento: 4 categorias × 3 momentos × (1 ref + 3 copies + 1 slot).

A ORDEM É SEMPRE 1 → 3 → 1:
  1 · a referência real da Duda naquele momento (capa do post, clicável)
  3 · três copies adaptadas pro nicho dela — ângulos diferentes, não 3 redações
  1 · um slot pontilhado pro post QUE ELA VAI FAZER

⚠️ A linha do tempo corre PRO LADO dentro da categoria (momento 1 → 2 → 3)
   e PRA BAIXO entre categorias (enigma → dor → entrega → carrinho).

⚠️ Nada de moldura de celular: a capa aparece grande, com canto arredondado,
   no formato real do post — reel 9:16 ou feed 4:5.

⚠️ A dor é hipótese: «a cliente vem uma vez e some». Trocar a dor não muda a
   estrutura, só o texto das 36 copies.
"""

CATEGORIAS = [
    dict(chave='enigma', n=1, nome='O enigma', janela='dias 1–3',
         oque='Diz que vem coisa e não diz o quê. Só pede uma palavra.',
         momentos=[
             dict(code='DeHoHmfFT_3', data='05/10', cm=952, fmt='feed', kw='3X',
                  dela='O número 3 nunca fez tanto sentido 👀 Digita 3X aqui nos comentários '
                       'pra ficar por dentro de TUDO que vai acontecer nessa Black Friday',
                  porque='um número sem explicação + palavra no comentário',
                  copies=[
                      ('O número', '21', '<b>21 dias.</b> É só isso que separa a cliente que '
                       'volta da que some pra sempre.<br><br>Descobri isso olhando a agenda de '
                       '3 anos — e agora vem coisa aí.<br><br>Comenta <b>21</b> 👇'),
                      ('A data', '12', 'Guarda essa data: <b>12 de novembro</b>.<br><br>'
                       'Não vou dizer o que é ainda. Só sei que quem entender isso antes '
                       'vai começar dezembro com a agenda cheia.<br><br>Comenta <b>12</b> 👇'),
                      ('O objeto', 'BANCADA', 'Tem uma coisa em cima da minha bancada há 3 anos '
                       'que mudou o meu salão.<br><br><b>Não é produto. Não é equipamento.</b><br><br>'
                       'Comenta <b>BANCADA</b> que eu mostro 👇'),
                  ]),
             dict(code='DeKK-nwPTVx', data='06/10', cm=545, fmt='reel', kw='EU TOPO',
                  dela='Será mesmo que você precisa de 87 body splashs na sua prateleira do '
                       'banheiro? 👀 Esse vídeo não é uma crítica a pessoas…',
                  porque='pega um exagero do cotidiano e vira espelho',
                  copies=[
                      ('O excesso', 'ESTANTE', 'Quantos produtos você tem na prateleira que '
                       '<b>nunca usou numa cliente</b>?<br><br>A gente compra coisa achando que '
                       'é isso que falta. Quase nunca é.<br><br>Comenta <b>ESTANTE</b> 👇'),
                      ('A comparação', 'CHEIO', '<b>Salão cheio não é salão lucrativo.</b><br><br>'
                       'Dá pra atender 12 por dia e fechar o mês no vermelho. Eu já fechei.<br><br>'
                       'Comenta <b>CHEIO</b> se você já sentiu isso 👇'),
                      ('A provocação', '8', 'Você tem 40 clientes… ou tem <b>8 que voltam '
                       'sempre</b> e 32 que passaram?<br><br>São negócios completamente '
                       'diferentes.<br><br>Comenta <b>8</b> 👇'),
                  ]),
             dict(code='DeMqIA-ldFF', data='07/10', cm=235, fmt='feed', kw='EU TOPO',
                  dela='🚨Atenção: altas chances de você se identificar com esse post. '
                       'E se isso aconteceu, você já sabe o que fazer',
                  porque='avisa que vai doer antes de doer — e já pede a palavra',
                  copies=[
                      ('O espelho', 'EU', 'Se você já terminou o mês <b>cansada e sem dinheiro '
                       'na mão</b>, esse post é seu.<br><br>Não é falta de trabalho. É outra '
                       'coisa, e eu vou falar dela essa semana.<br><br>Comenta <b>EU</b> 👇'),
                      ('O aviso', 'POSSO', 'Vou falar uma coisa que vai <b>incomodar</b> muita '
                       'cabeleireira.<br><br>Mas é o que mudou meu salão.<br><br>'
                       'Comenta <b>POSSO</b> que eu posto 👇'),
                      ('A contagem', 'AVISA', 'Faltam poucos dias pra eu abrir uma coisa que '
                       'eu guardo há 3 anos.<br><br>Quem comentar <b>AVISA</b> eu chamo primeiro, '
                       'antes de qualquer post 👇'),
                  ])]),

    dict(chave='dor', n=2, nome='A dor com nome', janela='dias 4–10',
         oque='Para de falar de você. Nomeia o problema de quem assiste.',
         momentos=[
             dict(code='DePQbDiFYSU', data='08/10', cm=406, fmt='feed', kw='DIAGNÓSTICO',
                  dela='Talvez você só esteja tentando resolver 3 problemas diferentes do mesmo '
                       'jeito 👀 Comenta DIAGNÓSTICO e eu te mando uma análise',
                  porque='divide a dor em 3 e oferece diagnóstico — a pessoa se classifica sozinha',
                  copies=[
                      ('O diagnóstico', 'DIAGNÓSTICO', 'Sua cliente não sumiu porque não gostou.'
                       '<br><b>Sumiu porque ninguém chamou.</b><br><br>E tem 3 motivos diferentes '
                       'pra isso — você provavelmente trata os três do mesmo jeito.<br><br>'
                       'Comenta <b>DIAGNÓSTICO</b> que eu te digo em qual você trava 👇'),
                      ('A conta', 'CONTA', 'Você não precisa de mais cliente nova.<br>'
                       '<b>Precisa que a antiga volte.</b><br><br>Cliente nova custa anúncio, '
                       'tempo e desconto. Cliente antiga custa <b>uma mensagem</b>.<br><br>'
                       'Comenta <b>CONTA</b> 👇'),
                      ('A pergunta que dói', 'QUANTAS', 'Quantas mulheres sentaram na sua cadeira '
                       'esse ano?<br><br>Agora a difícil: <b>de quantas você lembra o nome?</b>'
                       '<br><br>Não é memória ruim. É falta de sistema.<br><br>'
                       'Comenta <b>QUANTAS</b> 👇'),
                  ]),
             dict(code='DeWzkzSFY9s', data='11/10', cm=166, fmt='feed', kw='DIAGNÓSTICO',
                  dela='Você não é ruim em conteúdo. Você só pode estar gastando energia demais '
                       'no lugar errado. Por isso eu criei um diagnóstico…',
                  porque='absolve a pessoa antes de apontar o erro — tira a culpa, mantém o problema',
                  copies=[
                      ('A absolvição', 'ONDE', '<b>Você não é ruim de atendimento.</b><br><br>'
                       'Você só está gastando energia na parte errada do mês.<br><br>'
                       'Comenta <b>ONDE</b> que eu te mostro em que semana você está perdendo 👇'),
                      ('O lugar errado', 'DIA 20', 'Você corre atrás de cliente nova no <b>dia 1</b> '
                       'e esquece de quem já pagou no <b>dia 20</b>.<br><br>É aí que o mês escapa.'
                       '<br><br>Comenta <b>DIA 20</b> 👇'),
                      ('O cansaço', 'ORDEM', 'Não é falta de esforço — você já trabalha demais.'
                       '<br><b>É falta de ordem.</b><br><br>E ordem se resolve numa folha de papel.'
                       '<br><br>Comenta <b>ORDEM</b> 👇'),
                  ]),
             dict(code='DeZ6x_pvkON', data='12/10', cm=733, fmt='reel', kw='EU TOPO',
                  dela='Esse vídeo não é um ataque à Viih Tube, é uma análise de uma expert que '
                       'está no mercado de infoprodutos há 6 anos…',
                  porque='pega carona em assunto quente do nicho e vira autoridade',
                  copies=[
                      ('A carona', 'VIEWS', 'Vi uma cabeleireira bater <b>300 mil views</b> essa '
                       'semana — e ela me disse que <b>não entrou uma cliente</b>.<br><br>'
                       'Esse vídeo não é crítica. É a conta que ninguém faz.<br><br>'
                       'Comenta <b>VIEWS</b> 👇'),
                      ('A análise', 'ANÁLISE', 'Isso não é ataque a ninguém. É <b>análise de quem '
                       'está atrás da cadeira há 8 anos</b> e já errou cada uma dessas.<br><br>'
                       'Comenta <b>ANÁLISE</b> que eu abro o resto 👇'),
                      ('O contraponto', 'DEPENDER', 'Viralizar é ótimo. <b>Depender disso é outra '
                       'história.</b><br><br>O que paga a conta de luz é a cliente que volta em '
                       'novembro — não a que curtiu em outubro.<br><br>Comenta <b>DEPENDER</b> 👇'),
                  ])]),

    dict(chave='entrega', n=3, nome='A entrega de graça', janela='dias 11–15',
         oque='Dá pronto o menor pedaço útil. Quem pega, levanta a mão.',
         momentos=[
             dict(code='DehFS3FFWL1', data='15/10', cm=617, fmt='feed', kw='ESTRUTURA',
                  dela='Comente ESTRUTURA aqui pra receber 3 sequências prontas de stories pra '
                       'você postar hoje 👇🏼🔥',
                  porque='promete uso HOJE — não é material pra guardar, é pra usar à noite',
                  copies=[
                      ('As mensagens prontas', 'VOLTA', 'Comenta <b>VOLTA</b> que eu te mando '
                       '<b>as 3 mensagens</b> que eu uso pra chamar cliente que sumiu.<br><br>'
                       'Copia, troca o nome, manda <b>hoje à noite</b> 👇'),
                      ('A ficha', 'FICHA', 'Fiz uma <b>ficha de uma página</b> pra você descobrir, '
                       'hoje, quem não volta ao seu salão há mais de 60 dias.<br><br>'
                       'Imprime, preenche em 10 minutos, e leva um susto.<br><br>'
                       'Comenta <b>FICHA</b> 👇'),
                      ('Os 3 tipos', 'OS 3', 'Tem 3 tipos de cliente no seu caderno:<br>• a que '
                       'sumiu<br>• a que veio <b>uma vez só</b><br>• a que vem sempre e você nunca '
                       'agradeceu<br><br>Cada uma precisa de uma mensagem diferente. Escrevi as três.'
                       '<br><br>Comenta <b>OS 3</b> 👇'),
                  ]),
             dict(code='DeiAEf7lctQ', data='15/10', cm=1151, fmt='feed', kw='ESTRUTURA',
                  dela='Mermã, comenta ESTRUTURA que eu te mando 3 conteúdos prontos pra copiar, '
                       'adaptar ao seu negócio e postar 👇🏼',
                  porque='repete a MESMA oferta no mesmo dia, de noite — e foi o maior de todos',
                  copies=[
                      ('Copia e cola', 'COPIA', 'Mermã, comenta <b>COPIA</b> que eu te mando '
                       '3 textos prontos pra você mandar hoje à noite.<br><br>'
                       '<b>Só troca o nome.</b> Nem precisa pensar 👇'),
                      ('O roteiro de 10 min', '10', 'Um roteiro de <b>10 minutos</b> pro fim do '
                       'expediente que faz cliente voltar.<br><br>É o que eu faço enquanto '
                       'varro o chão.<br><br>Comenta <b>10</b> 👇'),
                      ('A tabela', 'TABELA', 'Uma tabela de uma página pra saber <b>quem chamar '
                       'essa semana</b> — sem depender da memória.<br><br>'
                       'Comenta <b>TABELA</b> que eu mando 👇'),
                  ]),
             dict(code='DerYvZDFcVB', data='19/10', cm=404, fmt='feed', kw='ESTRUTURA',
                  dela='E se o seu problema é justamente pensar "tá, mas eu posto o quê?", '
                       'comenta ESTRUTURA que eu te mando 3 estruturas prontas…',
                  porque='nomeia a trava exata com as palavras que a pessoa usa na cabeça',
                  copies=[
                      ('O que mandar', 'O QUE', 'E se o seu problema é justamente <b>«tá, mas eu '
                       'mando o quê pra ela?»</b> —<br><br>comenta <b>O QUE</b> que eu te mando '
                       'as 3 mensagens prontas 👇'),
                      ('O calendário', '7 DIAS', 'Montei o <b>calendário de 7 dias</b> de mensagem '
                       'pra cliente antiga: o que mandar na segunda, na quarta e no sábado.<br><br>'
                       'Comenta <b>7 DIAS</b> 👇'),
                      ('A trava', 'TRAVA', 'Você <b>sabe</b> que tem que chamar.<br>'
                       'Você trava na hora de escrever.<br><br>É só isso. E tem conserto de '
                       '1 página.<br><br>Comenta <b>TRAVA</b> 👇'),
                  ])]),

    dict(chave='carrinho', n=4, nome='O carrinho aberto', janela='dias 17–19',
         oque='Oferta nomeada, prazo curto, cupom por comentário.',
         momentos=[
             dict(code='DevGVj4DReg', data='21/10', cm=571, fmt='feed', kw='METODO3X',
                  dela='💰✅ OFERTA DE PRÉ BLACK FRIDAY DISPONÍVEL! Durante 63 dias, você vai '
                       'postar junto comigo, no Método Venda 3x…',
                  porque='abre nomeando a oferta e o prazo na primeira linha',
                  copies=[
                      ('Abriu', 'MEU', '<b>ABRIU.</b> 💰<br><br>São 63 dias comigo dentro do seu '
                       'salão: eu mando o que fazer, você faz, a cliente volta.<br><br>'
                       '<b>Até sexta</b> com preço de pré-Black Friday.<br><br>'
                       'Digita <b>MEU</b> que o cupom vai no direct 👇'),
                      ('O prazo é agenda', 'TURMA', 'O preço sobe sexta — e não é ameaça de '
                       'vendedora, <b>é agenda</b>: segunda a turma começa, e quem entra depois '
                       'perde a primeira semana.<br><br>Digita <b>TURMA</b> 👇'),
                      ('O difícil dos dois lados', '63', 'Você vai escolher um difícil de qualquer '
                       'jeito.<br><br>O de continuar abrindo a agenda e vendo buraco.<br>'
                       'Ou o de mudar alguma coisa por <b>63 dias</b>.<br><br>'
                       'Os dois cansam. Só um termina diferente.<br><br>Digita <b>63</b> 👇'),
                  ]),
             dict(code='DexRn6wvsLi', data='21/10', cm=197, fmt='reel', kw='M3X',
                  dela='Mais alguém ouvindo essa música no repeat desde o desfile da Victorias '
                       'Secret? 😮‍💨 Nem sempre aquilo que não tem RECONHECIMENTO é porque é ruim…',
                  porque='vende por dentro de um assunto leve — a oferta entra no fim, sem anúncio',
                  copies=[
                      ('O reconhecimento', 'VISTA', 'Seu salão não é pequeno.<br>'
                       '<b>Ele só não foi visto ainda.</b><br><br>Nem sempre o que não tem '
                       'reconhecimento é ruim — às vezes só falta quem mostre.<br><br>'
                       'Digita <b>VISTA</b> 👇'),
                      ('A objeção do caro', 'CARO', 'Toda vez que você julga uma coisa «cara», '
                       'você se limita sem perceber.<br><br>Digita <b>CARO</b> que eu te mostro a '
                       'conta de quanto custa <b>não</b> fazer 👇'),
                      ('A prova', 'PROVA', '<b>3 clientes minhas voltaram essa semana</b> usando '
                       'exatamente o que está lá dentro.<br><br>Não é promessa, é o print.<br><br>'
                       'Digita <b>PROVA</b> 👇'),
                  ]),
             dict(code='DezvAn6G8ZP', data='22/10', cm=314, fmt='feed', kw='M3X',
                  dela='Qual você escolheu: 1, 2 ou 3? 👀 No fim, as três tinham praticamente a '
                       'mesma mensagem: não deixa pra janeiro o que você ainda pode começar agora',
                  porque='usa um joguinho pra entregar escassez sem parecer cobrança',
                  copies=[
                      ('Janeiro', 'AGORA', 'Não deixa pra <b>janeiro</b> o que dá pra começar '
                       '<b>quinta</b>.<br><br>Em janeiro você vai estar cansada do Natal e a '
                       'agenda vazia vai doer igual.<br><br>Digita <b>AGORA</b> 👇'),
                      ('O último aviso', 'ÚLTIMA', '<b>Amanhã acaba.</b><br><br>Depois volta o '
                       'preço cheio, e a próxima turma é só em fevereiro.<br><br>'
                       'Digita <b>ÚLTIMA</b> 👇'),
                      ('A escolha', 'A SUA', 'Qual você escolheu: <b>1, 2 ou 3</b>?<br><br>'
                       'No fim as três diziam a mesma coisa — e o prazo das três acaba junto.'
                       '<br><br>Digita <b>A SUA</b> 👇'),
                  ])]),
]

SLOT_ROT = 'O meu post desta etapa'
