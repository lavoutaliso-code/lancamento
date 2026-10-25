#!/usr/bin/env python3
"""Classifica o público medido: sozinha × tem estrutura × educadora.

⚠️ O QUE ISTO É: leitura do SINAL que a própria pessoa escreveu na bio.
   Faturamento e nº de funcionárias NÃO existem em API nenhuma do Instagram —
   quem disser que mediu isso, inventou.
⚠️ Comentarista ≠ seguidora. Esta é a fatia que SE MEXE — e num lançamento
   por comentário é ela que compra. É a população certa pra esta pergunta,
   e é por isso que o recorte é esse e não «os seguidores».
"""
import json, os, re, sys, statistics as st

DIR = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(DIR, 'publico-izabela.json')))
P = d['perfis']

# ── os sinais, em ordem de prioridade ────────────────────────────────────
# educadora primeiro: quem vende curso é PAR, não cliente — e usa as mesmas
# palavras de equipe ("minhas alunas", "mentora"), então tem de sair antes.
EDUCA = re.compile(
    r'\b(alunas?|mentor[ia]|mentora|professor|instrutora|educadora|academy|'
    r'curso|cursos|formaç|capacit|workshop|palestrante|treinamentos?\b|'
    r'ensino|habilitad|certificaç)', re.I)

ESTRUTURA = re.compile(
    r'(\bequipe\b|\bnosso time\b|\bnossa\s+equipe\b|nossas?\s+profissionais|'
    r'\bcolaborador|\bfuncion[áa]ri|\bvagas?\b|contratando|\bCEO\b|'
    r'\bfranquia|\bunidades?\b|\bfilial|\bs[óo]cia|\bgerente|'
    r'corpo t[ée]cnico|nossa casa|venha nos conhecer)', re.I)

# casa própria: tem ponto fixo com nome de marca — nem sozinha-nômade,
# nem necessariamente com equipe
CASA = re.compile(r'(\bsal[ãa]o\b|\bstudio\b|\bst[úu]dio\b|\bespa[çc]o\b|'
                  r'\bbeauty\b|\bhair\b|\bcentro\b|\bclinic|\bateli[êe])', re.I)

SOZINHA = re.compile(r'(atendo\b|agende comigo|comigo\b|minha agenda|sou cabele|'
                     r'especialista em|atendimento personalizado|'
                     r'\bautônoma|a domic[íi]lio)', re.I)


def classe(p):
    t = (p.get('bio') or '') + ' ' + (p.get('contexto') or '') + ' ' + p['u']
    if EDUCA.search(t):
        return 'EDUCADORA (vende curso — é par, não cliente)'
    if ESTRUTURA.search(t):
        return 'TEM ESTRUTURA (equipe/CEO/vagas na bio)'
    if CASA.search(t):
        return 'CASA PRÓPRIA (salão/studio, equipe não declarada)'
    if SOZINHA.search(t):
        return 'SOZINHA (fala no singular, atende ela)'
    return 'NÃO DÁ PRA DIZER'


grupos = {}
for p in P:
    grupos.setdefault(classe(p), []).append(p)

tot = len(P)
print(f'POPULAÇÃO: {tot} perfis que comentaram nos posts dela '
      f'(de {d["falhas"] + tot} tentados)\n')
print(f'{"grupo":48} {"n":>4} {"%":>6} {"mediana seg":>12}')
print('─' * 74)
for k, v in sorted(grupos.items(), key=lambda x: -len(x[1])):
    segs = [x['seguidores'] for x in v if x['seguidores'] is not None]
    med = st.median(segs) if segs else 0
    print(f'{k:48} {len(v):4} {100 * len(v) / tot:5.1f}% {med:12,.0f}')

# ── tamanho de audiência: quem é grande e quem é pequena ────────────────
segs = sorted([p['seguidores'] for p in P if p['seguidores'] is not None])
print(f'\nSEGUIDORES de quem comenta — n={len(segs)}')
for rot, lo, hi in [('até 1 mil', 0, 1000), ('1–5 mil', 1000, 5000),
                    ('5–20 mil', 5000, 20000), ('20–100 mil', 20000, 100000),
                    ('100 mil +', 100000, 10**9)]:
    n = sum(1 for s in segs if lo <= s < hi)
    print(f'  {rot:12} {n:4}  {100 * n / len(segs):5.1f}%  {"█" * round(40 * n / len(segs))}')
print(f'  mediana: {st.median(segs):,.0f} · média: {sum(segs) / len(segs):,.0f}')

# ── as palavras que mais aparecem nas bios ──────────────────────────────
PARAR = set('de da do e em a o com para por no na os as um uma que se sua seu '
            'mais seus suas sou aqui você vc eu meu minha nos à é ao dos das'.split())
cont = {}
for p in P:
    for w in re.findall(r"[a-zà-úA-ZÀ-Ú]{3,}", (p.get('bio') or '').lower()):
        if w in PARAR:
            continue
        cont[w] = cont.get(w, 0) + 1
print('\nPALAVRAS mais escritas nas bios (quem comenta se apresenta como quê):')
for w, n in sorted(cont.items(), key=lambda x: -x[1])[:22]:
    print(f'  {w:18} {n:3}', end='\n' if n % 3 == 0 else '')
print()

json.dump({k: [x['u'] for x in v] for k, v in grupos.items()},
          open(os.path.join(DIR, 'publico-classificado.json'), 'w'),
          ensure_ascii=False, indent=1)
