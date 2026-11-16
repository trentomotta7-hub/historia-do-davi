#!/usr/bin/env python3
"""reaproveitar_clipes.py - conserta a deriva de um episodio JA gerado, sem gerar nada novo.

Cada clipe de 15 s do tier economico foi promptado em tres planos internos
(Shot 1 0-5s, Shot 2 5-10s, Shot 3 10-15s), cada um desenhado para frases
especificas da narracao. Este script recorta esses planos e os recoloca nas
janelas reais medidas do audio. O corte passa a acontecer na fronteira da frase
usando material que ja existe.

Uso: python3 pipeline/reaproveitar_clipes.py EP04 [dir_com_blocos]
Saida: <dir>/segments/NN.mp4 + <dir>/janelas.json
"""
import json, os, subprocess as sp, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ep = sys.argv[1] if len(sys.argv) > 1 else "EP04"
SRC = sys.argv[2] if len(sys.argv) > 2 else os.path.join(RAIZ, ep)
tempos = json.load(open(os.path.join(RAIZ, "dados", "tempos_%s.json" % ep), encoding="utf-8"))
F = dict((f["i"], f) for f in tempos["frases"])
VOZ = tempos["voz_total"]
PREROLL, POST, CARTELA_FASE, PRETO = 0.30, 0.40, 2.0, 2.2
W, H, FPS = 1080, 1920, 24

MAPA = [
    ([1, 2],     "bloco1",  0.0,  5.0),
    ([3, 4],     "bloco1",  5.0, 10.0),
    ([5, 6, 7],  "bloco1", 10.0, 15.0),
    ([8],        "bloco2",  0.0,  2.6),
    ([9],        "bloco2",  5.0,  8.6),
    ([10],       "bloco2", 10.0, 13.6),
    ([11],       "bloco3",  0.0,  5.0),
    ([12],       "bloco3",  5.0,  9.0),
    ([13, 14],   "bloco3",  9.0, 13.8),
    ([15],       "bloco2", 11.4, 15.0),
    ([16],       "bloco4",  0.0,  2.2),
    ([17, 18],   "bloco4",  5.0, 10.0),
    ([19],       "bloco4", 10.0, 15.0),
]

seg, anterior = [], 0.0
for k, (fr, bloco, i0, i1) in enumerate(MAPA):
    ini = max(anterior, F[fr[0]]["t0"] - PREROLL)
    if k + 1 < len(MAPA):
        prox = MAPA[k + 1][0][0]
        fim = min(max(F[prox]["t0"] - PREROLL, F[fr[-1]]["t1"] + POST), VOZ)
    else:
        fim = round(VOZ + CARTELA_FASE, 3)
    origem = round(i1 - i0, 3)
    janela = round(fim - ini, 3)
    seg.append({"n": k + 1, "frases": fr, "src": bloco + ".mp4", "in": i0, "out": i1,
                "origem": origem, "inicio": round(ini, 3), "fim": round(fim, 3),
                "janela": janela, "congelar": round(max(0.0, janela - origem), 3)})
    anterior = fim

total = round(seg[-1]["fim"] + PRETO, 3)
os.makedirs(os.path.join(SRC, "segments"), exist_ok=True)
for s in seg:
    vf = ("scale=%d:%d:force_original_aspect_ratio=increase:flags=lanczos,crop=%d:%d,"
          "setsar=1,fps=%d" % (W, H, W, H, FPS))
    if s["congelar"] > 0.05:
        vf += ",tpad=stop_mode=clone:stop_duration=%.3f" % s["congelar"]
    sp.run(["ffmpeg", "-v", "error", "-y", "-ss", "%.3f" % s["in"], "-t", "%.3f" % s["origem"],
            "-i", os.path.join(SRC, s["src"]), "-vf", vf, "-an",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "17",
            "-t", "%.3f" % s["janela"],
            os.path.join(SRC, "segments", "%02d.mp4" % s["n"])], check=True)

json.dump({"episodio": ep, "voz_total": round(VOZ, 3), "imagem_total": total,
           "preto_canais": PRETO, "segmentos": seg},
          open(os.path.join(SRC, "janelas.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

deriva = max(abs(s["inicio"] - max(0.0, F[s["frases"][0]]["t0"] - PREROLL)) for s in seg)
print("%s: %d segmentos reaproveitados, zero geracao nova" % (ep, len(seg)))
for s in seg:
    extra = ("  congela %.2fs" % s["congelar"]) if s["congelar"] > 0.05 else ""
    print("  #%02d %6.2f-%6.2fs janela %5.2fs <- %s [%.0f-%.0fs] frases %d-%d%s"
          % (s["n"], s["inicio"], s["fim"], s["janela"], s["src"], s["in"], s["out"],
             s["frases"][0], s["frases"][-1], extra))
print("imagem total: %.2fs | voz: %.2fs | deriva maxima restante: %.2fs"
      % (total, VOZ, deriva))
