#!/usr/bin/env python3
"""gerar_legendas.py — legenda ASS montada sobre o áudio REAL já retemporizado.

Regras (medidas nos episódios 1 a 3 e corrigidas depois do EP04):
  * corpo 66 px em 1080x1920, 2 linhas no máximo, contorno 3,8, MarginV 340;
  * estilo Padrao = bold para narração; Cita = regular para fala citada;
  * a cue termina no FIM da fala + 0,25 s de cauda. Sem fala, sem legenda.
    (No EP04 a cue ocupava a pausa inteira e reforçava a sensação de atraso.)
  * cartela de fase sobre o último plano + cartela de canais sobre preto.

Uso: python3 pipeline/gerar_legendas.py EP05 "FASE 3 — VANTAGEM"
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_LINHA, MAX_CUE, CAUDA = 26, 52, 0.25

ep = sys.argv[1] if len(sys.argv) > 1 else "EP04"
fase = sys.argv[2] if len(sys.argv) > 2 else "FASE 2 — VÍNCULO"

tempos = json.load(open(os.path.join(RAIZ, "dados", f"tempos_{ep}.json"), encoding="utf-8"))

CARTELA = """[Script Info]
; %(ep)s - legenda gerada sobre o audio medido (%(voz).2f s de voz)
Title: A histÃ³ria do Davi - %(ep)s
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Padrao,DejaVu Sans,66,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0.4,0,1,3.8,0.8,2,60,60,340,1
Style: Cita,DejaVu Sans,64,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,0,0,0,0,100,100,0.2,0,1,3.2,0.6,2,60,60,340,1
Style: Cartela,DejaVu Sans,80,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,3.0,0,1,4.5,0.8,5,60,60,300,1
Style: Canais,DejaVu Sans,46,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,0,0,0,0,100,100,0.6,0,1,2.6,0.5,2,60,60,150,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def empacota(txt):
    words, rows, cur = txt.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > MAX_LINHA and cur:
            rows.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        rows.append(cur)
    if len(rows) > 2:
        me = -(-len(rows) // 2)
        rows = [" ".join(rows[:me]), " ".join(rows[me:])]
    return "\\N".join(rows)


def dividir(txt):
    t = txt.strip()
    if len(t) <= MAX_CUE:
        return [t]
    words = t.split()
    best, bd = 1, 1e9
    for i in range(1, len(words)):
        acc = len(" ".join(words[:i]))
        if abs(acc - len(t) / 2) < bd:
            bd, best = abs(acc - len(t) / 2), i
    return [" ".join(words[:best]).strip(), " ".join(words[best:]).strip()]


def tc(x):
    m = int(x // 60); s = x % 60
    return f"0:{m:02d}:{s:05.2f}"


voz_fim = tempos["voz_total"]
linhas = []
for f in tempos["frases"]:
    t0, t1 = f["t0"], min(f["t1"] + CAUDA, voz_fim)
    partes = dividir(f["texto"])
    tot = sum(len(p) for p in partes) or 1
    cur = t0
    for p in partes:
        d = (t1 - t0) * len(p) / tot
        est = "Cita" if f["estilo"] == "C" else "Padrao"
        linhas.append(f"Dialogue: 0,{tc(cur)},{tc(cur + d)},{est},,0,0,0,,{empacota(p)}")
        cur += d

linhas.append(f"Dialogue: 1,{tc(voz_fim + 0.15)},{tc(voz_fim + 2.0)},Cartela,,0,0,0,,"
              f"{{\\an5}}{fase}")
linhas.append("Dialogue: 1," + tc(voz_fim + 2.2) + "," + tc(voz_fim + 4.2) +
              ",Canais,,0,0,0,,{\\an2}Disque Denúncia 181 · anônimo e gratuito"
              "\\NComunica PF: gov.br/pf   |   CVV 188 · 24h")

saida = os.path.join(RAIZ, "pipeline", f"legenda_{ep}.ass")
open(saida, "w", encoding="utf-8").write(
    CARTELA % {"ep": ep, "voz": voz_fim} + "\n".join(linhas) + "\n")
print(f"{ep}: {len(linhas) - 2} cues de fala + 2 cartelas -> {saida}")
print(f"voz termina em {voz_fim:.2f}s | episode final: {voz_fim + 4.2:.2f}s")
