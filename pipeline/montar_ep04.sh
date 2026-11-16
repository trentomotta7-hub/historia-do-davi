#!/usr/bin/env bash
# EP04 — montagem final. Entrada: bloco1..4.mp4 + narracao_ep04_timed.wav + cama + vibracao + legenda_ep04.ass
# A linha de tempo é definida pelo AUDIO real (método narration-led): ~57,6 s de voz + cartelas.
set -euo pipefail
cd "$(dirname "$0")"

W=1080; H=1920; FPS=24
VOZ=narracao_ep04_timed.wav
CAMA=../piloto/cama_teste.wav
VIB=../piloto/vibracao.mp3
LEG=legenda_ep04.ass
TOTAL=$(python3 -c "import json;print(json.load(open('blocos_ep04.json'))['imagem_total'])")
FADE=$(bc -l <<< "$TOTAL-2.4")
echo "duracao alvo: ${TOTAL}s"

# 1) imagem: os 4 blocos normalizados para 1080x1920/24fps sem distorcao + preto final
ffmpeg -v error -y -i bloco1.mp4 -i bloco2.mp4 -i bloco3.mp4 -i bloco4.mp4 \
  -f lavfi -t 2.2 -i "color=c=black:s=${W}x${H}:r=${FPS}" \
  -filter_complex "\
[0:v]scale=${W}:${H}:force_original_aspect_ratio=increase:flags=lanczos,crop=${W}:${H},setsar=1,fps=${FPS}[v0];\
[1:v]scale=${W}:${H}:force_original_aspect_ratio=increase:flags=lanczos,crop=${W}:${H},setsar=1,fps=${FPS}[v1];\
[2:v]scale=${W}:${H}:force_original_aspect_ratio=increase:flags=lanczos,crop=${W}:${H},setsar=1,fps=${FPS}[v2];\
[3:v]scale=${W}:${H}:force_original_aspect_ratio=increase:flags=lanczos,crop=${W}:${H},setsar=1,fps=${FPS}[v3];\
[4:v]scale=${W}:${H},setsar=1,fps=${FPS}[v4];\
[v0][v1][v2][v3][v4]concat=n=5:v=1:a=0[v]" \
  -map "[v]" -t "$TOTAL" -c:v libx264 -preset veryfast -crf 17 img.mp4

# 2) mix bruto: voz comprimida na frente, cama com ducking lateral sob a voz, vibracao pontual
ffmpeg -v error -y -i "$VOZ" -stream_loop -1 -i "$CAMA" -i "$VIB" \
  -f lavfi -t "$TOTAL" -i "anullsrc=r=48000:cl=stereo" \
  -filter_complex "\
[0:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,highpass=f=85,acompressor=threshold=0.09:ratio=2.6:attack=12:release=220:makeup=1.6[vozfull];\
[vozfull]asplit=2[vozsc][vozmix];\
[1:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,atrim=0:${TOTAL},volume=0.20,afade=t=in:d=2,afade=t=out:st=${FADE}:d=2.2[cama];\
[cama][vozsc]sidechaincompress=threshold=0.035:ratio=8:attack=70:release=520[camaduck];\
[2:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,adelay=5300|5300,volume=0.38[vib];\
[vozmix][camaduck][vib][3:a]amix=inputs=4:duration=longest:dropout_transition=0:normalize=0,atrim=0:${TOTAL},asetpts=PTS-STARTPTS,volume=1.55[mix]" \
  -map "[mix]" -c:a pcm_s24le mix_bruto.wav

# 3) loudnorm em duas passadas para fechar em -14 LUFS integrado de verdade
ffmpeg -hide_banner -i mix_bruto.wav \
  -af "loudnorm=I=-14:TP=-1:LRA=11:print_format=json" -f null - 2> norm.log
eval "$(python3 medir_loudnorm.py norm.log)"
echo "medido: I=${I} TP=${TP} LRA=${LRA} thresh=${THR}"

ffmpeg -v error -y -i mix_bruto.wav \
  -af "loudnorm=I=-14:TP=-1:LRA=11:linear=true:measured_I=${I}:measured_TP=${TP}:measured_LRA=${LRA}:measured_thresh=${THR}:offset=${OFF}" \
  -ar 48000 -c:a pcm_s16le mix.wav

# 4) legendas queimadas + exportacao final
ffmpeg -v error -y -i img.mp4 -i mix.wav -vf "ass=${LEG}" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -profile:v high \
  -c:a aac -b:a 320k -ar 48000 -movflags +faststart EP04_final.mp4

echo "--- conferencia:"
ffprobe -v error -show_entries format=duration,size:stream=codec_type,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 EP04_final.mp4
ffmpeg -hide_banner -i EP04_final.mp4 -af loudnorm=print_format=summary -f null - 2>&1 |
  grep -E "Input (Integrated|True Peak|Loudness range)" || true
echo "OK -> $(pwd)/EP04_final.mp4"
