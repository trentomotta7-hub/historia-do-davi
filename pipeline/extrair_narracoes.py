#!/usr/bin/env python3
"""extrair_narracoes.py — transforma o roteiro em dados executáveis.

Lê docs/03_roteiros_E4_a_E12.md e produz dados/narracoes.json: para cada episódio,
a lista de frases com estilo (P = narração, C = fala citada), a coluna Imagem da
shot list e a locação deduzida. Todo o resto da pipeline consome esse JSON.

A segmentação usa um scanner de estado, não regex: a voz cita frases inteiras e
uma quebra dentro da aspa ("“Sábado." / "Leva só o documento.”") faria a legenda
e o corte de cena errarem juntos.

Uso: python3 pipeline/extrair_narracoes.py [caminho_do_roteiro]
"""
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "docs", "03_roteiros_E4_a_E12.md")
OUT = os.path.join(RAIZ, "dados", "narracoes.json")

AB, FE = "\u201c", "\u201d"
PUNT = ".!?"
MAIUS = re.compile(r"[A-ZÀ-ÚÕÃÂÉÊÍÓÔÜá-ú]")

PRIOR = [
    ("loc_casa_carro", ["flash-back: carro", "carro branco", "pickup", "portão",
                        "casa dele", "hospital", "calçada"]),
    ("loc_campo_bairro", ["campo de terra", "refletor", "coletes", "bola", "crianças",
                          "gramado", "aluguel do campo"]),
    ("loc_terminal_patio", ["terminal", "pátio", "empilhadeira", "contêiner", "conteiner",
                            "lacre", "guindaste", "pórtico", "carga"]),
    ("loc_portaria", ["portaria", "crachá", "cracha", "cerca", "cancela", "documento"]),
    ("loc_loja", ["loja", "arara", "vitrine", "uniforme", "colega", "caixa da loja"]),
    ("loc_onibus", ["onibus", "ônibus", "rodoviária", "catraca", "ponto de"]),
    ("loc_banco", ["banco", "agência", "agencia", "caixa eletrônico", "transferência"]),
    ("loc_cozinha_noite", ["cozinha", "louça", "caneca", "fogão", "bule", "pia",
                           "gaveta", "envelope de tudo", "mesa da cozinha"]),
    ("loc_rua_bairro", ["rua", "bicicleta", "boteco", "esquina", "calçada da"]),
    ("loc_quarto_noite", ["quarto", "cama", "lençol", "beirada", "janela", "abajur",
                          "celular na mão", "tela", "cronômetro", "rosto", "polegar",
                          "escuro", "teto"]),
]


def local_de(img, anterior="loc_quarto_noite"):
    """Locação pela coluna Imagem da shot list, com prioridade.

    Nunca pela palavra dita: em EP04 a palavra 'time' na fala herdava o campo de
    futebol e o corte de cena ia para o lugar errado.
    """
    s = (img or "").lower()
    if not s:
        return anterior
    for loc, kws in PRIOR:
        if any(k in s for k in kws):
            return loc
    return anterior


def aspas(txt):
    """Converte toda aspa em par balanceado “ ” alternando (o roteiro usa retas)."""
    out, aberto = [], False
    for ch in txt:
        if ch in ('"', AB, FE):
            out.append(AB if not aberto else FE)
            aberto = not aberto
        else:
            out.append(ch)
    return "".join(out)


def frases_de(paragrafo):
    """[(estilo, frase)] com fronteiras reais: não quebra dentro de citação."""
    txt = aspas(paragrafo).strip()
    n, i, dentro, atual, out = len(txt), 0, False, [], []
    while i < n:
        ch = txt[i]
        if ch == AB:
            dentro = True
        elif ch == FE:
            dentro = False
        atual.append(ch)
        if ch in PUNT:
            j = i + 1
            while j < n and txt[j] == FE:          # consome fechamento da citação
                atual.append(txt[j]); dentro = False; j += 1
            k = j
            while k < n and txt[k] == " ":
                k += 1
            if k < n and (MAIUS.match(txt[k]) or txt[k] == AB) and not dentro:
                out.append("".join(atual).strip())
                atual = []
                i = k - 1
        i += 1
    if "".join(atual).strip():
        out.append("".join(atual).strip())
    limpas = []
    for s in out:
        if not s:
            continue
        while s.endswith(FE + FE):          # aspa dobrada do roteiro
            s = s[:-1]
        limpas.append(s)
    return [("C" if (s.startswith(AB) or s.endswith(FE)) else "P", s) for s in limpas]


def mapa_da_shot_list(bloco):
    """Frase dita -> coluna Imagem, pela shot list do episódio."""
    mapa = {}
    for ln in re.findall(r"^\| \d+ \|.*$", bloco, re.M):
        cols = [c.strip() for c in ln.strip("|").split("|")]
        if len(cols) < 5:
            continue
        fala = cols[2].strip("*_").strip()
        fala = re.sub(r"^[" + AB + FE + r"\"']+|[" + AB + FE + r"\"']+$", "", fala).strip()
        if fala and fala != "—":
            mapa[fala.lower()[:34]] = cols[3].strip()
    return mapa


def chave(txt):
    return re.sub(r"[*" + AB + FE + r"\"']", "", txt).strip().lower()[:34]


texto = open(SRC, encoding="utf-8").read()
episodios = {}

for bloco in re.split(r"# EPISÓDIO ", texto)[1:]:
    ep = int(bloco.split(" ")[0])
    titulo = bloco.splitlines()[0].split("—")[-1].strip()
    m = re.search(r"\*\*NARAÇÃO P/ TTS\*\*\s*```(.*?)```", bloco, re.S)
    if not m:
        print(f"AVISO: EP{ep} sem bloco de narração")
        continue
    par = m.group(1).strip()
    fase = re.search(r"\*\*Fase:\*\*\s*([^·]+)", bloco)
    mapa = mapa_da_shot_list(bloco)

    frases, ant = [], "loc_quarto_noite"
    for i, (est, txt) in enumerate(frases_de(par), 1):
        img = mapa.get(chave(txt), "")
        loc = local_de(img, ant)
        ant = loc
        frases.append({"i": i, "estilo": est, "texto": txt, "imagem": img,
                       "local": loc, "linha_shotlist": bool(img)})

    episodios[f"EP{ep:02d}"] = {
        "episodio": ep, "titulo": titulo,
        "fase": (fase.group(1).strip() if fase else ""),
        "caracteres": len(par), "frases": frases,
    }

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(episodios, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

ruins = 0
for k, v in episodios.items():
    fs = v["frases"]
    cit = sum(1 for f in fs if f["estilo"] == "C")
    abertos = sum(1 for f in fs if f["texto"].startswith(AB) and not f["texto"].endswith(FE))
    ruins += abertos
    print(f"{k} {v['titulo'][:26]:28s} {len(fs):3d} frases ({cit:2d} cit.) "
          f"{v['caracteres']:4d} car  {len(set(f['local'] for f in fs))} loc  "
          f"citação partida: {abertos}")
print(f"\ngravado em {OUT} | citações partidas restantes: {ruins}")
