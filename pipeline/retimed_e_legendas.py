#!/usr/bin/env python3
"""EP04 — retemporiza a narracao (alongando as pausas entre frases, que e o
respiro do estilo da serie) e gera a legenda ASS ja alinhada na nova linha de
tempo. Tudo local: nada aqui consome credito de geracao.

Uso: python3 retimed_e_legendas.py
Saida: narracao_ep04_timed.wav, legenda_ep04.ass, blocos_ep04.json
"""
import json
import re
import subprocess as sp

SRC = "narracao_ep04.wav"
ALVO_TOTAL = 58.0         # segundos de linha de tempo de voz antes das cartelas
MAX_CHARS_LINHA = 26      # legenda em no maximo 2 linhas de ate ~26 caracteres
MAX_CHARS_CUE = 52

# 1) segmentos de fala reais, medidos por silencedetect
out = sp.run(["ffmpeg", "-hide_banner", "-i", SRC, "-af",
              "silencedetect=noise=-38dB:d=0.22", "-f", "null", "-"],
             capture_output=True, text=True).stderr
sil = []
start = None
for line in out.splitlines():
    m = re.search(r"silence_start: ([\d.]+)", line)
    if m:
        start = float(m.group(1))
    m = re.search(r"silence_end: ([\d.]+)", line)
    if m and start is not None:
        sil.append((start, float(m.group(1))))
        start = None
dur = float(sp.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                    "-of", "csv=p=0", SRC], capture_output=True, text=True).stdout)

chunks = []               # (inicio, fim) de cada bloco de fala
prev = 0.0
for s, e in sil:
    if s - prev > 0.05:
        chunks.append((prev, s))
    prev = e
if dur - prev > 0.05:
    chunks.append((prev, dur))
print(f"{len(chunks)} blocos de fala, {dur:.2f}s de audio")

# 2) frases na ordem exata do roteiro, com marcador de estilo
FRASES = [
    ("P", "Davi ficou com o dedo sobre o botão."),
    ("P", "O número não era desconhecido."),
    ("P", "Ele atendeu no terceiro toque."),
    ("P", "Do outro lado, uma voz que ele conhecia."),
    ("C", "“Davi, meu filho. Aqui é o Sandro.”"),
    ("P", "Sandro."),
    ("P", "O cara boa do bairro."),
    ("P", "Quem patrocinava o time e pagava o aluguel do campo."),
    ("P", "Quem levou a mãe dele ao hospital e não quis receber nada."),
    ("C", "“Aquele número é nosso, tranquilo. Não é nada errado. Só quero te mostrar uma coisa.”"),
    ("P", "Davi perguntou o que era."),
    ("P", "Sandro riu baixo."),
    ("C", "“Coisa de gente em que a gente confia.”"),
    ("P", "A ligação durou um minuto e quarenta."),
    ("P", "Foi o suficiente."),
    ("P", "E ninguém falou em dinheiro."),
    ("P", "Na cozinha, a mãe perguntou quem era."),
    ("C", "“Um amigo. Do time.”"),
    ("P", "E foi a primeira vez que ele gostou de responder."),
]
nf, nc = len(FRASES), len(chunks)
total_chars = sum(len(t) for _, t in FRASES)
taxa = sum(e - s for s, e in chunks) / total_chars   # s/caractere observado

# 3) alinhamento monototico frase <-> blocos de fala (programacao dinamica)
INF = float("inf")
best = [[INF] * (nc + 1) for _ in range(nf + 1)]
back = [[0] * (nc + 1) for _ in range(nf + 1)]
best[0][0] = 0.0
for i in range(1, nf + 1):
    for j in range(i, nc + 1):
        for k in range(i - 1, j):
            span = chunks[k][1] - chunks[j - 1][0] if k < j else 0
            exp = len(FRASES[i - 1][1]) * taxa
            cost = (span - exp) ** 2
            if best[i - 1][k] + cost < best[i][j]:
                best[i][j] = best[i - 1][k] + cost
                back[i][j] = k
j, limites = nc, []
for i in range(nf, 0, -1):
    k = back[i][j]
    limites.append((k, j))
    j = k
limites.reverse()
frase_chunk = [None] * nf
for idx, (k, j) in enumerate(limites):
    frase_chunk[idx] = (k, j)
print("alinhamento:", [f"{a}-{b}" for a, b in frase_chunk])

# 4) nova linha de tempo: cada pausa interna vira pausa_base + extra
gaps = []
for n in range(len(chunks) - 1):
    gaps.append((chunks[n][1], chunks[n + 1][0]))
# a duracao total ja inclui as pausas que a voz fez sozinha; distribuir apenas
# o que falta para chegar ao alvo, sem esticar nada alem disso
extra = max(0.0, (ALVO_TOTAL - dur) / len(gaps))
sil_total = sum(e - s for s, e in sil)
print(f"fala real {dur - sil_total:.2f}s | pausas naturais {sil_total:.2f}s "
      f"({sil_total / dur * 100:.0f}% do tempo) | pausa adicional: +{extra:.3f}s por respiro")

nova = []           # (start, dur) de cada bloco de fala na nova timeline
t = 0.25            # respiro de abertura, como nos originais
para_fase = []      # onde comeca cada frase ja na nova timeline
ptr = 0
for n, (s, e) in enumerate(chunks):
    nova.append((t, e - s))
    t += (e - s)
    if n < len(gaps):
        t += (gaps[n][1] - gaps[n][0]) + extra
nova_total = t
print(f"timeline de voz: {nova_total:.2f}s")

idx_de_frase = {}
for fi, (k, j) in enumerate(frase_chunk):
    idx_de_frase[fi] = k
for fi in range(nf):
    para_fase.append(nova[idx_de_frase[fi]][0])
fim_frase = []
for fi in range(nf):
    last_j = frase_chunk[fi][1] - 1
    fim_frase.append(nova[last_j][0] + nova[last_j][1])

# 5) escrever audio retemporizado extraindo cada bloco como arquivo e usando o
#    concat demuxer (grafo de filtro gigante aqui e frágil e nao vale a pena)
import os
os.makedirs("seg", exist_ok=True)
newgap = [(gaps[n][1] - gaps[n][0]) + extra for n in range(len(gaps))]
for n, (s, e) in enumerate(chunks):
    sp.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{s:.4f}", "-t", f"{e - s:.4f}",
            "-i", SRC, "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le",
            f"seg/a{n:02d}.wav"], check=True)
for n, g in enumerate(newgap):
    sp.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
            f"anullsrc=r=44100:cl=mono", "-t", f"{g:.4f}", "-c:a", "pcm_s16le",
            f"seg/g{n:02d}.wav"], check=True)
ordem = []
for n in range(len(chunks)):
    ordem.append(f"seg/a{n:02d}.wav")
    if n < len(newgap):
        ordem.append(f"seg/g{n:02d}.wav")
open("lista_concat.txt", "w").write("\n".join(f"file '{o}'" for o in ordem) + "\n")
sp.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
        "-i", "lista_concat.txt", "-c:a", "pcm_s16le", "-ar", "44100",
        "narracao_ep04_timed.wav"], check=True)

# 6) legenda ASS: cue por frase; frase longa divide em duas cues
def linhas(txt, maxc=MAX_CHARS_LINHA):
    """Empacota palavras em no maximo 2 linhas de ate maxc caracteres."""
    words, rows, cur = txt.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > maxc and cur:
            rows.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        rows.append(cur)
    if len(rows) > 2:
        me = -(-len(rows) // 2)
        rows = [" ".join(rows[:me]), " ".join(rows[me:])]
    return rows


def partes(txt):
    """1 cue para frase curta, 2 cues balanceadas para frase longa."""
    t = txt.strip()
    if len(t) <= MAX_CHARS_CUE:
        return [t]
    words = t.split()
    cut, best, bd = 1, 1, 1e9
    for i in range(1, len(words)):
        acc = len(" ".join(words[:i]))
        if abs(acc - len(t) / 2) < bd:
            bd, best = abs(acc - len(t) / 2), i
        cut = best
    return [" ".join(words[:cut]).strip(), " ".join(words[cut:]).strip()]


def tc(x):
    m = int(x // 60); s = x % 60
    return f"0:{m:02d}:{s:05.2f}"


eventos = []
for fi, (st, txt) in enumerate(FRASES):
    t0, t1 = para_fase[fi], fim_frase[fi]
    ps = partes(txt)
    tot = sum(len(x) for x in ps) or 1
    cur = t0
    for n, ptxt in enumerate(ps):
        d = (t1 - t0) * len(ptxt) / tot
        a, b = cur, cur + d
        cur = b
        body = "\\N".join(linhas(ptxt))
        if len(ps) == 2 and n == 0 and ptxt.count(" ") == 0:
            pass
        eventos.append((a, b, st, body))

HEAD = """[Script Info]
; EP04 - legenda gerada sobre a linha de tempo real do audio retemporizado
Title: Davi EP04
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
linhas_out = []
for a, b, st, txt in eventos:
    if b - a < 0.55:
        b = a + 0.55
    stl = "Cita" if st == "C" else "Padrao"
    txt = txt.replace(chr(93), chr(8220))
    linhas_out.append(f"Dialogue: 0,{tc(a)},{tc(b)},{stl},,0,0,0,,{txt}")

FIM_IMG = nova_total + 2.0
linhas_out.append(f"Dialogue: 1,{tc(nova_total + 0.15)},{tc(FIM_IMG)},Cartela,,0,0,0,,"
                  "{\\an5}FASE 2 \u2014 VÍNCULO")
linhas_out.append("Dialogue: 1," + tc(FIM_IMG + 0.2) + "," + tc(FIM_IMG + 2.2) +
                  ",Canais,,0,0,0,,{\\an2}Disque Denúncia 181 \u00b7 anônimo e gratuito"
                  "\\NComunica PF: gov.br/pf   |   CVV 188 \u00b7 24h")
open("legenda_ep04.ass", "w", encoding="utf-8").write(HEAD + "\n".join(linhas_out) + "\n")

# 7) blocos de imagem (4 chamadas de 15s) e onde cada um entra
alvos = [0.0, 15.0, 30.0, 45.0]
blocos = []
for n, ini in enumerate(alvos):
    fim = alvos[n + 1] if n + 1 < len(alvos) else FIM_IMG + 2.2
    fs = [FRASES[i][1] for i in range(nf) if ini <= para_fase[i] < fim]
    blocos.append({"bloco": n + 1, "video_inicio": ini, "video_fim": round(fim, 2), "frases": fs})
json.dump({"voz_total": round(nova_total, 3), "imagem_total": round(FIM_IMG + 2.2, 3),
           "pausa_extra": round(extra, 4),
           "frases": [{"i": i, "estilo": FRASES[i][0], "t0": round(para_fase[i], 3),
                        "t1": round(fim_frase[i], 3), "texto": FRASES[i][1]} for i in range(nf)],
           "blocos": blocos},
          open("blocos_ep04.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"legenda: {len(eventos)} cues | voz {nova_total:.1f}s | final {FIM_IMG + 2.2:.1f}s")
