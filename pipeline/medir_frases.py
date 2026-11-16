#!/usr/bin/env python3
"""medir_frases.py — etapa 3 da pipeline v2 (áudio primeiro, imagem depois).

Faz três coisas, nesta ordem:
  1. mede onde realmente começa e termina cada bloco de fala (silencedetect);
  2. alinha monotonicamente esses blocos com as frases do roteiro (programação
     dinâmica, porque a voz às vezes respira dentro da frase);
  3. retemporiza o áudio alongando pausas com PISO e com REFORÇO em frases-golpe,
     e escreve dados/tempos_EPxx.json com t0/t1 reais de cada frase.

É esse JSON que o planejar_blocos.py usa para cortar a imagem na fronteira da
fala. Sem ele, a imagem atrasa três ou quatro segundos — defeito do EP04.

Uso: python3 pipeline/medir_frases.py EP05 [narracao_ep05.wav]
"""
import json
import os
import re
import subprocess as sp
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAUSA_MIN = 0.90     # piso de silêncio entre frases
REFORCO_GOLPE = 0.55 # pausa extra depois de frase curta e de golpe
ALVO_TOTAL = 58.0    # segundos de voz antes das cartelas

ep = sys.argv[1] if len(sys.argv) > 1 else "EP04"
wav = sys.argv[2] if len(sys.argv) > 2 else os.path.join(RAIZ, f"{ep}/narracao_{ep.lower()}.wav")

narr = json.load(open(os.path.join(RAIZ, "dados", "narracoes.json"), encoding="utf-8"))[ep]
FR = [(f["estilo"], f["texto"], f["i"]) for f in narr["frases"]]

# 1) blocos de fala medidos
r = sp.run(["ffmpeg", "-hide_banner", "-i", wav, "-af",
            "silencedetect=noise=-38dB:d=0.22", "-f", "null", "-"],
           capture_output=True, text=True).stderr
sil, ini = [], None
for ln in r.splitlines():
    m = re.search(r"silence_start: ([\d.]+)", ln)
    if m:
        ini = float(m.group(1))
    m = re.search(r"silence_end: ([\d.]+)", ln)
    if m and ini is not None:
        sil.append((ini, float(m.group(1))))
        ini = None
dur = float(sp.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                    "-of", "csv=p=0", wav], capture_output=True, text=True).stdout)
chunks, prev = [], 0.0
for s, e in sil:
    if s - prev > 0.05:
        chunks.append((prev, s))
    prev = e
if dur - prev > 0.05:
    chunks.append((prev, dur))

nf, nc = len(FR), len(chunks)
fala_pura = sum(e - s for s, e in chunks)
print(f"{ep}: {nc} blocos de fala | articulação {fala_pura:.2f}s "
      f"= {sum(len(t) for _, t, _ in FR) / fala_pura:.1f} car/s | "
      f"pausas {dur - fala_pura:.2f}s ({(dur - fala_pura) / dur * 100:.0f}%)")

# 2) alinhamento frase <-> blocos
taxa = fala_pura / sum(len(t) for _, t, _ in FR)
INF = float("inf")
best = [[INF] * (nc + 1) for _ in range(nf + 1)]
back = [[0] * (nc + 1) for _ in range(nf + 1)]
best[0][0] = 0.0
for i in range(1, nf + 1):
    ncar = len(FR[i - 1][1])
    for j in range(i, nc + 1):
        for k in range(i - 1, j):
            span = chunks[k][1] - chunks[j - 1][0]
            c = (span - ncar * taxa) ** 2
            if best[i - 1][k] + c < best[i][j]:
                best[i][j] = best[i - 1][k] + c
                back[i][j] = k
j, assign = nc, [None] * nf
for i in range(nf, 0, -1):
    k = back[i][j]
    assign[i - 1] = (k, j)
    j = k

# 3) nova linha de tempo com piso e reforço de golpe
gaps = [(chunks[n][1], chunks[n + 1][0]) for n in range(len(chunks) - 1)]
def pausa_para(frase_idx):
    """Pausa depois da frase: piso, extra se for golpe curto, mais se fechar cena."""
    txt = FR[frase_idx][1]
    base = max(PAUSA_MIN, 0.35)
    if len(txt) <= 24 or txt.rstrip(".””").endswith(("!", "?")):
        base += REFORCO_GOLPE
    return base

# pausa alvo por gap: atribuída à frase que termina naquele bloco de fala
fim_de_frase = {}
for fi, (k, j) in enumerate(assign):
    fim_de_frase[j - 1] = fi
novas_pausas = []
for n in range(len(gaps)):
    fi = fim_de_frase.get(n, None)
    medida = gaps[n][1] - gaps[n][0]
    alvo = max(medida, pausa_para(fi) if fi is not None else PAUSA_MIN)
    novas_pausas.append(alvo)

# ajustar para fechar no alvo total sem estourar
def total_com(pesos):
    return 0.25 + sum(e - s for s, e in chunks) + sum(pesos)
escala = 1.0
if total_com(novas_pausas) > ALVO_TOTAL and novas_pausas:
    excesso = total_com(novas_pausas) - ALVO_TOTAL
    red = min(excesso, sum(p - PAUSA_MIN for p in novas_pausas))
    disponivel = sum(p - PAUSA_MIN for p in novas_pausas) or 1
    novas_pausas = [PAUSA_MIN + (p - PAUSA_MIN) * (1 - red / disponivel) for p in novas_pausas]

nova, t = [], 0.25
for n, (s, e) in enumerate(chunks):
    nova.append((t, e - s))
    t += (e - s) + (novas_pausas[n] if n < len(novas_pausas) else 0)
voz_total = t
print(f"nova linha de tempo da voz: {voz_total:.2f}s | pausas "
      f"{min(novas_pausas):.2f}-{max(novas_pausas):.2f}s")

# escrever áudio retemporizado
os.makedirs(f"seg_{ep}", exist_ok=True)
ordem = []
for n, (s, e) in enumerate(chunks):
    f = f"seg_{ep}/a{n:02d}.wav"
    sp.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{s:.4f}", "-t", f"{e - s:.4f}",
            "-i", wav, "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", f], check=True)
    ordem.append(f)
    if n < len(novas_pausas):
        g = f"seg_{ep}/g{n:02d}.wav"
        sp.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
                "anullsrc=r=48000:cl=mono", "-t", f"{novas_pausas[n]:.4f}",
                "-c:a", "pcm_s16le", g], check=True)
        ordem.append(g)
open(f"lista_{ep}.txt", "w").write("\n".join(f"file '{o}'" for o in ordem) + "\n")
saida = f"narracao_{ep.lower()}_timed.wav"
sp.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i",
        f"lista_{ep}.txt", "-c:a", "pcm_s16le", "-ar", "48000", saida], check=True)

fr_out = []
for fi, (k, j) in enumerate(assign):
    fr_out.append({"i": FR[fi][2], "estilo": FR[fi][0], "texto": FR[fi][1],
                   "t0": round(nova[k][0], 3), "t1": round(nova[j - 1][0] + nova[j - 1][1], 3)})
os.makedirs(os.path.join(RAIZ, "dados"), exist_ok=True)
json.dump({"episodio": ep, "voz_total": round(voz_total, 3),
           "articulacao_carpor_segundo": round(sum(len(t) for _, t, _ in FR) / fala_pura, 2),
           "frases": fr_out},
          open(os.path.join(RAIZ, "dados", f"tempos_{ep}.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print(f"gerado: {saida} e dados/tempos_{ep}.json")
