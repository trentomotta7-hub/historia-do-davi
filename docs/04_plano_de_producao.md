# Plano de produção — como os episódios são feitos na prática

Este documento fecha o buraco entre roteiro e arquivo MP4. Ele define a ordem das etapas, os prompts de referência que garantem continuidade visual, o orçamento de geração por episódio e o comando de montagem. Os dois scripts do pipeline estão em `/home/ubuntu/serie_davi/pipeline/`.

## 1. Ordem obrigatória das etapas

A série é **narration-led**: o áudio manda, a imagem segue. Fazer o contrário é o que produz episódios com a imagem sobrando no fim.

1. Escolher a voz definitiva (audição A ou B) e congelar a ID.
2. Gerar a narração do episódio inteira, num só take, e **medir a duração real com `ffprobe`**.
3. Se passar de 62 s, cortar frases no roteiro e regerar. Só usar ajuste de velocidade (`atempo` até ±4%) para fechar diferença pequena.
4. Transcrever o áudio gerado para obter os timestamps reais por frase → isso produz a legenda SRT/ASS com sincronismo verdadeiro, sem trabalho manual.
5. Gerar as **referências visuais** (pessoa e lugar) — uma vez só para a temporada inteira.
6. Gerar os clipes de vídeo com as referências anexadas, na duração fechada pelo áudio (não antes).
7. Montar com o script do pipeline: vídeo + narração + cama musical + legendas queimadas + cartelas, exportando em 1080×1920 a −14 LUFS.
8. Conferir frames de controle (início de bloco, meio, gancho) e o som final.

## 2. Referências visuais a criar antes de qualquer episódio

Regra: uma imagem-mestra por personagem e uma por localização. Todo clipe subsequente usa essas imagens como referência, e não descrições soltas. Sem isso, no terceiro episódio o Davi vira outra pessoa.

**Davi (mestre de identidade).** Gerar com GPT Image 2.5 em 9:16, 2K, e depois derivar close e plano americano por img2img dessa mesma imagem:

```
3D animated feature style, Pixar-like rendering, subsurface scattering skin. A 20-year-old
Brazilian young man from a coastal port town: short dark brown hair swept up and back, thick
eyebrows, large warm brown eyes, light tan skin, faint stubble. Full floral tattoo sleeve on
his RIGHT forearm and upper arm. Wearing a white linen button shirt with sleeves rolled to the
elbow, khaki shorts, brown loafers, simple wristwatch. Neutral friendly expression, slight
tiredness around the eyes. Standing in a modest bright kitchen, warm tungsten light, white
cabinets, tiled floor, wood table. Full body and a face close-up on the same sheet. Shallow
depth of field, soft cinematic lighting, high detail. Vertical 9:16. No text.
```

**A mãe** (derivada da mesma folha de estilo, mesmo renderizador):

```
Same 3D animated feature style. A Brazilian mother in her late 40s: brown hair in a low bun,
 thin-framed prescription glasses, lavender t-shirt, blue jeans, small gold earrings. Kind, tired, practical face. Standing at a kitchen counter with a coffee pot, warm light. Reference sheet: medium shot and close-up. No text.
```

**Sandro** — o mais importante travar, porque ele aparece de E4 a E10 e precisa ser simpático em todo plano:

```
Same 3D animated feature style. A 38-year-old Brazilian man, well-groomed, short dark hair, clean-shaven, warm open smile, cream polo shirt slightly expensive, gold watch, driving a clean white pickup. He always looks like a helpful neighbour, never threatening. Reference sheet: medium shot, close-up smiling, and him gesturing welcome with an open hand. No text.
```

**Cleber** (colelete laranja, crachá), **Ruan** (uniforme de loja), **Téo** (16 anos, mochila, uniforme grande demais) seguem a mesma fórmula, todos derivados do mesmo estilo descrito acima, para que a temporada inteira tenha uma única pele visual.

**Localizações** (uma imagem cada, usadas como referência espacial): cozinha com mesa de madeira e azulejo; quarto com janela dando para luzes de porto noturno; arara de loja de roupas; interior de ônibus urbano; pátio de terminal de contêiner ao amanhecer com luz de sódio; campo de terra de bairro com refletor.

Para o pátio do terminal, prompt-chave: `shipping terminal at 5:40 am, stacked containers, gantry cranes, sodium-orange lights against deep blue sky, forklift motion blur, no readable text, no logos, no people faces` — e **sem número de contêiner legível**, de propósito (regra de responsabilidade 1 do arco).

## 3. Estratégia de geração dos clipes

- **Modelo:** Seedance 2.5 para os planos de rosto e de Porto (onde a consistência do personagem é cobrada); MiniMax H3 para inserts de objeto sem personagem (celular na mesa, envelope, lacre, papel da consulta), onde custo importa e ninguém repara se o braço tem tatuagem.
- **Proporção e resolução:** retrato, 720p na geração, upscale para 1080×1920 na montagem.
- **Duração por clipe:** 5 ou 6 s, correspondendo a uma linha do shot list. Não pedir clipe de 60 s.
- **Áudio do modelo: desligado.** A voz é gerada separadamente e é ela que dá o tempo. Os clipes entram mudos e recebem ambiente + trilha na montagem — assim a narração nunca briga com som de IA.
- **Referências por clipe:** sempre a imagem-mestra do personagem em cena + a imagem da localização. Bindar explicitamente no prompt (`@image1 = Davi identity, @image2 = kitchen`).
- **Continuidade:** registrar no shot list o estado de entrada e saída de cada plano (posição, luz, objeto na mão), porque o corte do episódio 9 (café espelhado ao do episódio 5) depende de repetir enquadramento, não de descrever a cena de novo.

**Orçamento por episódio (~62 s):** 1 narração + 13 a 19 clipes. Estimativa de tempo de produção por episódio: **1 a 2 dias de trabalho real** (geração de clipes é o gargalo, com retrabalho de 20 a 30%). Para E4 a E12, considere **≈ 130 clipes**. Se quiser reduzir antes de gastar, o caminho é gerar 6 s de clipe por bloco narrativo maior (agregando 2 linhas do shot list em 1 plano), o que leva a ~11 clipes por episódio.

## 4. Especificação técnica final

| Parâmetro | Valor |
|---|---|
| Entrega | MP4 H.264 High, 1080×1920, 24 fps, CRF 18 |
| Áudio | AAC 320 kbps, 48 kHz, estéreo, **−14 LUFS integrado**, pico ≤ −1 dBTP |
| Voz | Mono, sem reverb, processada apenas com de-esser e compressão leve |
| Cama musical | −18 dB abaixo da voz; fade-out de 2 s no fim |
| Legendas | Queimadas (ASS, 2 estilos: bold narração / regular aspas), MargemV 260 |
| Cartelas | `FASE n — NOME` (2 s) + canais de ajuda (2 s), no mesmo tipo de letra |
| Identidade | Logotipo/marca da série nunca sobre o rosto do personagem |

## 5. Comandos de montagem (resumo)

Tudo está no script `pipeline/montar_episodio.sh`. O equivalente manual, na ordem:

```bash
# 1. medir a narração real
ffprobe -v error -show_entries format=duration -of csv=p=0 narracao_ep4.wav

# 2. juntar os clipes já na ordem e no corte do áudio
ffmpeg -f concat -safe 0 -i lista_clips.txt -c copy bruto.mp4

# 3. mixar voz + cama e normalizar a -14 LUFS
ffmpeg -i bruto.mp4 -i narracao_ep4.wav -i cama.wav -filter_complex \
 "[1:a]volume=1.0[v];[2:a]volume=0.13[m];[v][m]amix=inputs=2:normalize=0[a]" \
 -map 0:v -map "[a]" -af "loudnorm=I=-14:TP=-1:LRA=11" mix.mp4

# 4. queimar legenda ASS + cartelas e exportar
ffmpeg -i mix.mp4 -vf "scale=1080:1920:flags=lanczos,ass=legenda.ass" \
 -c:v libx264 -crf 18 -preset slow -c:a copy -movflags +faststart EP04_final.mp4
```

O arquivo `pipeline/legenda.ass` já vem com os dois estilos medidos nos vídeos originais: `Padrão` (bold, narração) e `Cita` (regular, mensagens do celular), bloco centralizado a ~80% da altura, contorno preto de 3,5 px em escala 1080.

## 6. O que preciso de você para começar

1. **Voz:** audição A (`pt-br-storyteller-5`) ou B (`pt-br-storyteller-11`). Ouça os quatro arquivos e escolha.
2. **Episódio-piloto:** recomendo **E4**, porque ele é curto de gerar (18 planos), apresenta Sandro e fecha a pergunta deixada em aberto no E3.
3. **Formato de entrega:** só MP4, ou MP4 + capa/thumb + texto de legenda para o post (descrição, hashtags e o texto da cartela de ajuda).
4. **Se a temporada inteira for aprovada depois do piloto**, a ordem de produção mais eficiente é E4 → E5 → E6 (mesmas locações, menos referência nova) e só depois E7 em diante, que é onde entram as locações de terminal.
