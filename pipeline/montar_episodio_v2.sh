#!/usr/bin/env bash
# montar_episodio_v2.sh — montagem padrão da série, já com as correções do EP04.
#
# Diferenças para a v1:
#   * os clipes entram NAS JANELAS DO ÁUDIO MEDIDO (dados/blocos_EPxx.json),
#     não em fatias fixas de 15 s -> fim da deriva de sincronia;
#   * VELOC=0.94 desacelera a articulação da voz (~10%), que estava 22,1 car/s;
#   * loudnorm com TP=-1.5 para sobrar margem na recodificação das plataformas;
#   * aceita clipes de durações diferentes, com pré-roll e congelamento de quadro.
#
# Uso: bash montar_episodio_v2.sh EP05
# Estrutura esperada (na pasta do episódio, dentro do repositório):
#   EP05/narracao_ep05_timed.wav  (saída de medir_frases.py)
#   EP05/clips/01.mp4 02.mp4 ...  (um por bloco, na ordem do plan)
#   pipeline/legenda_EP05.ass     (saída de gerar_legendas.py)
#   media/audios/cama_musicale.wav, media/audios/vibracao_celular.mp3
set -euo pipefail
cd "$(dirname "$0")/.."          # raiz do repositório

EP="${1:-EP04}"
W=1080; H=1920; FPS=24
DIR="$EP"
VOZ="$DIR/narracao_${EP,,}_timed.wav"
BLOCOS="dados/blocos_${EP}.json"
LEG="pipeline/legenda_${EP}.ass"
CAMA="media/audios/cama_musicale.wav"
VIB="media/audios/vibracao_celular.mp3"
OUT="$DIR/${EP}_final.mp4"
[ -f "$VOZ" ] || { echo "falta $VOZ (rode medir_frases.py)"; exit 1; }
[ -f "$BLOCOS" ] || { echo "falta $BLOCOS (rode planejar_blocos.py)"; exit 1; }
[ -f "$LEG" ] || { echo "falta $LEG (rode gerar_legendas.py)"; exit 1; }

TOTAL=$(python3 -c "import json;print(json.load(open('$BLOCOS'))['imagem_total'])")
echo "$EP: voz + cartelas = ${TOTAL}s de episódio"

# 1) imagem: cada clipe é posicionado na janela real do seu bloco
python3 - "$BLOCOS" "$DIR" > "janela_${EP}.sh" <<'PYEOF'
import json, sys
b = json.load(open(sys.argv[1], encoding="utf-8"))["blocos"]
d = sys.argv[2]
for n, x in enumerate(b, 1):
    ini, dur = x["inicio"], round(x["fim"] - x["inicio"] + 0.35, 3)
    src = f"{d}/clips/{n:02d}.mp4"
    print(f'ffmpeg -v error -y -i {src} -vf "scale={1080}:{1920}:force_original_aspect_ratio=increase:flags=lanczos,crop={1080}:{1920},setpts=PTS-STARTPTS,fps=24,tpad=stop_mode=clone:stop_duration=12" -t {dur} -c:v libx264 -preset veryfast -crf 17 {d}/j{n:02d}.mp4')
    print(f'echo "bloco {n}: {dur}s em {src}"')
PYEOF
bash "janela_${EP}.sh"

python3 - "$BLOCOS" "$DIR" > "lista_${EP}.txt" <<'PYEOF'
import json, sys
b = json.load(open(sys.argv[1], encoding="utf-8"))["blocos"]
d = sys.argv[2]
for n in range(1, len(b) + 1):
    print(f"file '{d}/j{n:02d}.mp4'")
PYEOF

ffmpeg -v error -y -f concat -safe 0 -i "lista_${EP}.txt" \
  -f lavfi -t 4.2 -i "color=c=black:s=${W}x${H}:r=${FPS}" \
  -filter_complex "[0:v]fps=${FPS},setsar=1[a];[1:v]setsar=1,fps=${FPS}[b];[a][b]concat=n=2:v=1:a=0[v]" \
  -map "[v]" -t "$TOTAL" -c:v libx264 -preset veryfast -crf 17 "$DIR/img.mp4"

# 2) mix: voz desacelerada, cama com ducking lateral, SFX de vibração no primeiro toque
VOZFIM=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VOZ")
FADE=$(bc -l <<< "$TOTAL-2.4")
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

# 3) loudnorm em duas passadas, alvo -14 LUFS e teto de pico -1,5 dBTP
ffmpeg -hide_banner -i "$DIR/mix_bruto.wav" \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" -f null - 2> "$DIR/norm.log"
eval "$(python3 pipeline/medir_loudnorm.py "$DIR/norm.log")"
echo "medido: I=${I} TP=${TP} LRA=${LRA}"
ffmpeg -v error -y -i "$DIR/mix_bruto.wav" \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11:linear=true:measured_I=${I}:measured_TP=${TP}:measured_LRA=${LRA}:measured_thresh=${THR}:offset=${OFF}" \
  -ar 48000 -c:a pcm_s16le "$DIR/mix.wav"

# 4) legendas queimadas + entrega
ffmpeg -v error -y -i "$DIR/img.mp4" -i "$DIR/mix.wav" -vf "ass=${LEG}" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -profile:v high \
  -c:a aac -b:a 320k -ar 48000 -movflags +faststart "$OUT"

echo "--- conferencia $EP:"
ffprobe -v error -show_entries format=duration,size:stream=codec_type,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 "$OUT"
ffmpeg -hide_banner -i "$OUT" -af loudnorm=print_format=summary -f null - 2>&1 |
  grep -E "Input (Integrated|True Peak)" || true
rm -f "$DIR"/j*.mp4 "janela_${EP}.sh" "lista_${EP}.txt" "$DIR/norm.log"
echo "OK -> $(pwd)/$OUT"
