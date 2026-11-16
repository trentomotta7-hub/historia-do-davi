#!/usr/bin/env bash
# montar_segmentos.sh <EP> — montagem quando os clipes já existem e foram recolocados
# nas janelas reais por reaproveitar_clipes.py (EP04) ou gerados por bloco (E5+).
# A voz entra no tempo já medido: não há atempo aqui, a desaceleração foi feita
# antes da medição, para que áudio, legenda e imagem nasçam do mesmo relógio.
set -euo pipefail
cd "$(dirname "$0")/.."
EP="${1:-EP04}"
W=1080; H=1920; FPS=24
DIR="$EP"
VOZ="$DIR/narracao_${EP,,}_timed.wav"
JAN="$DIR/janelas.json"
LEG="pipeline/legenda_${EP}.ass"
CAMA="media/audios/cama_musicale.wav"
VIB="media/audios/vibracao_celular.mp3"
OUT="$DIR/${EP}_final.mp4"
TOTAL=$(python3 -c "import json;print(json.load(open('$JAN'))['imagem_total'])")
PRETO=$(python3 -c "import json;print(json.load(open('$JAN'))['preto_canais'])")
FADE=$(bc -l <<< "$TOTAL-2.4")
echo "$EP: ${TOTAL}s de episódio (voz $(python3 -c "import json;print(json.load(open('$JAN'))['voz_total'])")s)"

python3 - "$JAN" "$DIR" > lista_"$EP".txt <<'PYEOF'
import json,sys
d=sys.argv[2]
for s in json.load(open(sys.argv[1],encoding="utf-8"))["segmentos"]:
    print("file '%s/segments/%02d.mp4'" % (d, s["n"]))
PYEOF

ffmpeg -v error -y -f concat -safe 0 -i lista_"$EP".txt \
  -f lavfi -t "$PRETO" -i "color=c=black:s=${W}x${H}:r=${FPS}" \
  -filter_complex "[0:v]fps=${FPS},setsar=1,format=yuv420p[a];[1:v]setsar=1,fps=${FPS}[b];[a][b]concat=n=2:v=1:a=0[v]" \
  -map "[v]" -t "$TOTAL" -c:v libx264 -preset veryfast -crf 17 "$DIR/img.mp4"

ffmpeg -v error -y -i "$VOZ" -stream_loop -1 -i "$CAMA" -i "$VIB" \
  -f lavfi -t "$TOTAL" -i "anullsrc=r=48000:cl=stereo" \
  -filter_complex "\
[0:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,highpass=f=85,acompressor=threshold=0.09:ratio=2.6:attack=12:release=220:makeup=1.6[vf];\
[vf]asplit=2[vsc][vmx];\
[1:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,atrim=0:${TOTAL},volume=0.20,afade=t=in:d=2,afade=t=out:st=${FADE}:d=2.2[cama];\
[cama][vsc]sidechaincompress=threshold=0.035:ratio=8:attack=70:release=520[cd];\
[2:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,adelay=4200|4200,volume=0.36[vs];\
[vmx][cd][vs][3:a]amix=inputs=4:duration=longest:dropout_transition=0:normalize=0,atrim=0:${TOTAL},asetpts=PTS-STARTPTS,volume=1.50[m]" \
  -map "[m]" -c:a pcm_s24le "$DIR/mix_bruto.wav"

ffmpeg -hide_banner -i "$DIR/mix_bruto.wav" -af "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" -f null - 2> "$DIR/norm.log"
eval "$(python3 pipeline/medir_loudnorm.py "$DIR/norm.log")"
ffmpeg -v error -y -i "$DIR/mix_bruto.wav" \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11:linear=true:measured_I=${I}:measured_TP=${TP}:measured_LRA=${LRA}:measured_thresh=${THR}:offset=${OFF}" \
  -ar 48000 -c:a pcm_s16le "$DIR/mix.wav"

ffmpeg -v error -y -i "$DIR/img.mp4" -i "$DIR/mix.wav" -vf "ass=${LEG}" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -profile:v high \
  -c:a aac -b:a 320k -ar 48000 -movflags +faststart "$OUT"

echo "--- conferencia:"
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 "$OUT"
ffmpeg -hide_banner -i "$OUT" -af loudnorm=print_format=summary -f null - 2>&1 | grep -E "Input (Integrated|True Peak)" || true
rm -f lista_"$EP".txt "$DIR/norm.log" "$DIR/img.mp4" "$DIR/mix_bruto.wav" "$DIR/mix.wav"
echo "OK -> $(pwd)/$OUT"
