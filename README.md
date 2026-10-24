# lançamento

A estrutura do lançamento da @izabelalaila, montada em cima do que a
@mariaeduardasv fez entre **05/10 e 23/10/2026** — medido, não lembrado.

**No ar:** https://lavoutaliso-code.github.io/lancamento/

## O que a tela é

Os **51 posts** dela do lançamento, na ordem, dentro de 5 categorias
(o enigma · a dor com nome · a entrega de graça · o ao vivo · o carrinho).
Cada post é uma ramificação:

    ① a referência dela  →  ②②② três ideias de adaptação  →  ③ o meu post

Clicar no **+** abre o card de agendamento: arquivo → feed/dump/reels →
dia e hora → legenda. Ao confirmar, **o post entra na fila do Instagram dela
e o servidor publica sozinho na hora marcada.**

## Como o agendamento funciona (o caminho que já existia)

Repete o Postador do painel performance, provado em 23/10:

1. `POST /painel-midia?perfil=lai&id=&nome=&tipo=` — sobe o arquivo cru
2. `GET  /painel-gestao?perfil=lai` — lê o pacote inteiro e a `rev`
3. `POST /painel-gestao` — acrescenta em `conteudo.postador` e **devolve tudo**,
   com `base` = a rev lida
4. a ronda do backend acorda de minuto em minuto e publica pela Graph API

⚠️ **Devolver o pacote inteiro não é capricho.** `POST /painel-gestao` grava
`pessoal + conteudo + mapas` de uma vez; mandar só o postador apagaria pauta,
mapa e demanda dela. O `base` é a trava contra sobrescrita: se a rev andou
entre a leitura e a escrita, o servidor recusa e a tela relê.

⚠️ **A hora é de Brasília.** O seletor do navegador devolve a hora local do
aparelho; o carimbo `-03:00` é montado à mão. É o mesmo erro de 3 horas que já
custou 18 cartões corrigidos no caixa.

## O que está medido e o que é hipótese

| | |
|---|---|
| os 51 posts, datas, formatos e comentários | **medido** na conta dela |
| as capas | baixadas dos posts reais |
| a dor («a cliente vem uma vez e some») | **hipótese** — trocar a dor não muda a estrutura, muda as 153 ideias |
| as palavras-chave | rascunho — nenhuma vai pro ar sem funil que mede |

## As 3 ofertas (ofertas.html)

**https://lavoutaliso-code.github.io/lancamento/ofertas.html**

Três ofertas pra escolher, cada uma com a dor na voz do público, o mecanismo,
a isca e **o risco**. As três calculadoras **funcionam na página** — ela mexe
nos números do salão e vê o que cada isca cospe.

Base: **296 posts** e **398 comentários** colhidos da @izabelalaila em
24/10/2026. Cada evidência citada tem data e contagem.

⚠️ As calculadoras **não projetam venda**. Fazem a aritmética do que já existe
(preço, custo, tempo, quantidade), porque «quantas clientes novas você vai ter»
não é conta, é chute.

⚠️ Em 29/12/2025 ela anunciou o encerramento de todos os cursos «em respeito
aos novos franqueados». Voltar a vender precisa de uma virada honesta — a
oferta 2 (formação de técnica) é a que mais esbarra nisso.

## Arquivos

- `index.html` — o site (autocontido, capas embutidas)
- `gera-site.py` — monta o HTML
- `ideias51.py` — as 153 ideias de adaptação
- `posts-lancamento.json` — os 51 posts colhidos
- `ofertas.html` + `gera-ofertas.py` — as 3 ofertas com calculadora
- `dossie-izabelalaila.json` — 296 posts dela
- `comentarios-izabela.json` — 398 comentários lidos

Gerar de novo: `python3 gera-site.py`
