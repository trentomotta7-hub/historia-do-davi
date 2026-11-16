#!/usr/bin/env bash
# Monta um episódio da série do Davi a partir de: clipes + narração + cama musical + legenda ASS.
# Uso:  ./montar_episodio.sh 4  EP04
#       $1 = numero do episodio (para nome)   $2 = pasta de trabalho
#
# Estrutura esperada da pasta de trabalho:
#   EP04/clips/*.mp4        -> clipes já na ordem definitiva (ordenados por nome)
#   EP04/narracao.wav       -> narração REAL medida (voz única da temporada)
#   EP04/cama.wav           -> trilha/ambiente contínuo (instrumental, sem vocal)
#   EP04/legenda.ass        -> legenda com timestamps do áudio real (copy do template)
set -euo pipefail

EP="${1:-04}"
DIR="${2:-EP$EP}"
cd "$DIR"

W=1080; H=1920; FPS=24
OUT="EP${EP}_final.mp4"

# 1) duração real da narração (é ela que define o episódio)
NAR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 narracao.wav)
echo "narração: ${NAR}s"

# 2) concatena os clipes, normalizando resolução/fps/amostragem
rm -f lista.txt
for f in clips/*.mp4; do printf "file '%s'\n" "$(realpath "$f")" >> lista.txt; done
ffmpeg -v error -y -f concat -safe 0 -i lista.txt -an \
  -vf "scale=${W}:${H}:flags=lanczos,fps=${FPS},setsar=1" -c:v libx264 -preset medium -crf 18 bruto.mp4
BRUTO=$(ffprobe -v error -show_entries format=duration -of csv=p=0 bruto.mp4)
echo "imagem bruta: ${BRUTO}s (delta vs narração: $(bc -l <<< "$BRUTO - $NAR")s)"

# 3) preenche sobra de imagem congelando o último frame, ou corta o excedente
if (( $(bc -l <<< "$BRUTO < $NAR + 4.0") )); then
  ffmpeg -v error -y -i bruto.mp4 -vf "tpad=stop_mode=clone:stop_duration=8" -c:v libx264 -crf 18 bruto2.mp4
else
  cp bruto.mp4 bruto2.mp4
fi
# duração final = narração + 4s de cartelas
TOTAL=$(bc -l <<< "$NAR + 4")
ffmpeg -v error -y -i bruto2.mp4 -t "$TOTAL" -c copy bruto3.mp4

# 4) mix: voz na frente, cama a -18dB, normalização -14 LUFS
ffmpeg -v error -y -i bruto3.mp4 -i narracao.wav -i cama.wav -filter_complex \
"[1:a]aresample=48000,acompress=threshold=0.12:ratio=3:attack=8:release=180[v];\
 [2:a]aresample=48000,volume=0.13,afade=t=out:st=$(bc -l <<< "$TOTAL-2"):d=2[m];\
 [v][m]amix=inputs=2:duration=first:normalize=0[a]" \
-map 0:v -map "[a]" -af "loudnorm=I=-14:TP=-1:LRA=11" -c:v copy -c:a aac -b:a 320k mix.mp4

# 5) queima legenda + exporta
ffmpeg -v error -y -i mix.mp4 -vf "ass=legenda.ass" -c:v libx264 -preset slow -crf 18 \
  -pix_fmt yuv420p -c:a copy -movflags +faststart "$OUT"

ffprobe -v error -show_entries format=duration -show_entries stream=codec_type,width,height \
  -of default=noprint_wrappers=1 "$OUT"
echo "OK -> $(pwd)/$OUT"
