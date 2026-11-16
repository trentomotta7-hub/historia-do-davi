#!/usr/bin/env python3
"""planejar_blocos.py — corrige a deriva de sincronia do EP04.

O bloco de VÍDEO passa a nascer da fronteira real da FALA medida, e não de
janelas fixas de 15 s. Regras:

  * quebra obrigatória quando muda a locação entre frases consecutivas;
  * quebra quando o bloco ia passar de DUR_MAX (o tier econômico aceita 5 a 15 s);
  * bloco mínimo de DUR_MIN, exceto no último;
  * frases muito curtas ("Sandro." / "Foi o suficiente.") nunca abrem bloco próprio
    se o bloco anterior puder recebê-las sem estourar DUR_MAX.

Entrada : dados/tempos_EPxx.json  (sai de medir_frases.py: t0/t1 reais por frase)
          dados/narracoes.json    (locação por frase)
Saída   : dados/blocos_EPxx.json  (o que a geração de vídeo deve executar)

Uso: python3 pipeline/planejar_blocos.py EP05
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUR_MAX = 15.0
DUR_MIN = 5.0
RESPIRO_FIM = 0.6      # silêncio mantido na imagem depois da última frase do bloco

ep = sys.argv[1] if len(sys.argv) > 1 else "EP04"
tempos = json.load(open(os.path.join(RAIZ, "dados", f"tempos_{ep}.json"), encoding="utf-8"))
narr = json.load(open(os.path.join(RAIZ, "dados", "narracoes.json"), encoding="utf-8"))[ep]

fr = tempos["frases"]
loc = {f["i"]: f["local"] for f in narr["frases"]}
img = {f["i"]: f.get("imagem", "") for f in narr["frases"]}

blocos, atual = [], []


def fechar(lista):
    if not lista:
        return None
    ini = lista[0]["t0"] - 0.25
    fim = lista[-1]["t1"] + RESPIRO_FIM
    return {
        "bloco": len(blocos) + 1,
        "inicio": round(ini, 3),
        "fim": round(fim, 3),
        "duracao": round(fim - ini, 3),
        "frases": [f["texto"] for f in lista],
        "locais": sorted({loc[f["i"]] for f in lista}),
        "planos": [img[f["i"]] for f in lista if img.get(f["i"])],
    }


for n, f in enumerate(fr):
    prox = fr[n + 1] if n + 1 < len(fr) else None
    atual.append(f)
    if prox is None:
        b = fechar(atual)
        if b and b["duracao"] < DUR_MIN and blocos:
            # bloco curto demais: fundir com o anterior
            anterior = fechar(blocos[-1]["frases"] and atual)
        if b:
            blocos.append(b)
        break
    muda_loc = loc[f["i"]] != loc[prox["i"]]
    estoura = (prox["t1"] + RESPIRO_FIM - (atual[0]["t0"] - 0.25)) > DUR_MAX
    if muda_loc or estoura:
        blocos.append(fechar(atual))
        atual = []

# fundir blocos finais menores que DUR_MIN quando o anterior não estourar
def tent_fundir(bl):
    out = []
    for b in bl:
        if out and b["duracao"] < DUR_MIN:
            prev = out[-1]
            if (b["fim"] - prev["inicio"]) <= DUR_MAX + 1.2:
                prev["fim"] = b["fim"]
                prev["duracao"] = round(b["fim"] - prev["inicio"], 3)
                prev["frases"] += b["frases"]
                prev["locais"] = sorted(set(prev["locais"]) | set(b["locais"]))
                prev["planos"] += b["planos"]
                continue
        out.append(dict(b))
    for n, b in enumerate(out, 1):
        b["bloco"] = n
    return out


blocos = tent_fundir(blocos)
voz_fim = fr[-1]["t1"]
# O tier econômico aceita de 5 a 15 s. Bloco curto não vira clipe de 3 s: ganha
# pré-roll (a imagem entra um pouco antes da frase) e mantém a fronteira de saída.
for b in blocos:
    d = b["duracao"]
    if d < 5.0:
        falta = 5.0 - d
        b["inicio_pedido"] = round(max(0.0, b["inicio"] - falta), 3)
        b["duracao_pedido"] = round(b["inicio"] - b["inicio_pedido"] + d, 3)
    elif d > 15.0:
        b["inicio_pedido"] = b["inicio"]
        b["duracao_pedido"] = 15.0
        b["aviso"] = "bloco acima de 15 s: dividir em dois clipes na frase indicada"
    else:
        b["inicio_pedido"] = b["inicio"]
        b["duracao_pedido"] = d
total_imagem = round(blocos[-1]["fim"] + 4.0, 3)   # + cartela de fase + cartela de canais

json.dump({"episodio": ep, "voz_total": round(voz_fim, 3),
           "imagem_total": total_imagem, "dur_max": DUR_MAX,
           "chamadas_de_video": len(blocos), "blocos": blocos},
          open(os.path.join(RAIZ, "dados", f"blocos_{ep}.json"), "w",
               encoding="utf-8"), ensure_ascii=False, indent=2)

print(f"{ep}: {len(fr)} frases -> {len(blocos)} blocos (chamadas de vídeo)")
for b in blocos:
    print(f"  #{b['bloco']} {b['inicio']:6.2f}-{b['fim']:6.2f}s  pede {b['duracao_pedido']:5.2f}s  "
          f"{'/'.join(l.replace('loc_','') for l in b['locais']):28s} {len(b['frases'])} frases")
print(f"imagem total: {total_imagem}s | duração pedida por clipe: "
      f"{', '.join(str(b['duracao_pedido']) for b in blocos)}")
