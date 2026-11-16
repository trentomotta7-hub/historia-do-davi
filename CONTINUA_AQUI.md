# CONTINUA AQUI — protocolo de retomada

Este arquivo existe para o caso de uso real do projeto: **clonar o repositório numa sessão nova de IA e continuar produzindo sem reexplicar nada**. Siga a ordem. Não pule etapa, porque cada etapa anterior economiza uma chamada de geração depois.

## Passo -1 — obter o projeto

```bash
git clone https://github.com/trentomotta7-hub/historia-do-davi
cd historia-do-davi
```

O repositório é público e já contém os episódios entregues, as referências visuais, a cama musical, a vibração de celular, as duas amostras de voz e todos os JSON intermediários do E4. Nada precisa ser regenerado para retomar, exceto a mídia do episódio novo.

A pipeline foi testada a partir de um clone limpo: os passos 1, 3, 4 e 5 rodam sem ajuste e reproduzem exatamente os tempos e blocos do EP04 (`54,02 s de voz`, `6 blocos`, `21 cues + 2 cartelas`).

## Passo 0 — ler antes de gerar qualquer coisa

1. `INTELIGENCIA.md` (voz, escrita, bíblia visual, legenda, áudio, custo).
2. `docs/07_sincronia_e_correcoes.md` (**por que a ordem é áudio primeiro, imagem depois**).
3. `docs/06_ficha_de_producao_EP04.md` (o que já foi gasto e o que ficou pendente).

Se você, agente, estiver tentado a gerar vídeo primeiro: parado. É exatamente isso que produziu o episódio dessincronizado.

## Passo 1 — escolher o episódio e preparar o texto

```bash
python3 pipeline/extrair_narracoes.py     # regenera dados/narracoes.json a partir do roteiro
```

Confira na saída: frases contadas, citações balanceadas (`citação partida: 0`), locações. Se aparecer citação partida, não siga — o defeito vai para a legenda e para o corte de cena juntos.

Episódio tem entre 655 e 805 caracteres de narração. Se você reescrever trecho, mantenha essa faixa e a regra de 5 a 8 palavras por frase (seção 3 do `INTELIGENCIA.md`).

## Passo 2 — gerar a voz (1 chamada)

Voz `pt-br-storyteller-5`, idioma `pt-BR`, **uma chamada por episódio**, texto verbatim. Salve como `EPxx/narracao_epxx.wav`.

Nada de instruções de estilo no prompt de voz. A emoção da série está nas pausas, e as pausas são construídas no passo 3, não pedidas ao locutor.

## Passo 3 — medir o áudio real (0 chamadas)

```bash
python3 pipeline/medir_frases.py EP05 EP05/narracao_ep05.wav
```

Isso imprime a taxa de articulação real, as porcentagens de pausa, escreve `narracao_ep05_timed.wav` e `dados/tempos_EP05.json`. Números esperados, calibrados no E4: articulação 21–23 car/s, pausa natural ~39% do tempo, voz retemporizada 54–58 s, pausa mínima travada em 0,9 s com reforço de 0,55 s depois de frase-golpe.

Se a voz retemporizada passar de 58 s, **não acelere**: corte uma frase redundante no roteiro e volte ao passo 1.

## Passo 4 — planejar os clipes a partir do tempo medido (0 chamadas)

```bash
python3 pipeline/planejar_blocos.py EP05
```

Saída: um bloco por clipe, com `inicio`, `fim` e a **duração a pedir** para o gerador (entre 5 e 15 s). Blocos quebram quando muda a locação. É isto que elimina o "ele fala e três segundos depois aparece o que ele falou".

Gere então **um clipe por bloco** no tier econômico, retrato 768p, `generate_audio=false`, anexando como referência a folha do personagem e da locação (`prompts/prompts_geracao.json` → chaves `referencias` e `clipes_EPxx`; para episódio novo, escreva o prompt no mesmo formato: `Shot 1 (0-5s): …` com enquadramento, luz e movimento de câmera). Salve como `EP05/clips/01.mp4`, `02.mp4`… na ordem dos blocos.

Regras que evitam retrabalho:

- Telas de celular: pedir **apagadas ou fora de foco**. A informação da mensagem é lida pela narração.
- Antebraço visível: repetir "floral tattoo sleeve on his **RIGHT** forearm".
- Flashback de favor: dourado de fim de tarde. Presente: azul-noturno. Nunca misture os dois no mesmo bloco sem um corte seco.
- Um plano geral do porto por episódio, no máximo.

## Passo 5 — legenda sobre o áudio medido (0 chamadas)

```bash
python3 pipeline/gerar_legendas.py EP05 "FASE 3 — VANTAGEM"
```

A cue termina no fim da fala + 0,25 s. Sem fala, sem legenda. Cartela de fase sobre o último plano, canais de ajuda sobre preto nos 2 s finais.

## Passo 6 — montagem (0 chamadas)

```bash
bash pipeline/montar_episodio_v2.sh EP05
```

O script posiciona cada clipe na janela real do bloco (com pré-roll e congelamento de quadro se o clipe vier curto), desacelera a voz em `VELOC=0.94`, aplica ducking lateral da cama sob a narração, fecha loudnorm em −14 LUFS com teto −1,5 dBTP e queima a legenda. Conferência impressa ao final: duração, tamanho, LUFS, pico.

## Passo 7 — controle de qualidade obrigatório

1. **Sincronia frase-a-plano:** extraia um frame no meio de cada frase (`ffmpeg -ss <(t0+t1)/2>`) e confirme que o quadro mostra o que a frase diz. Se duas frases seguidas caírem no mesmo plano errado, o erro está no passo 4, não na montagem.
2. **Legenda:** nenhum quadro sem fala com legenda acesa; citação em peso regular.
3. **Áudio:** −14 ± 0,5 LUFS; pico ≤ −1,0 dBTP; cama audível só nas pausas.
4. **Continuidade:** tatuagem no braço direito, camisa de linho branco, bermuda cáqui, relógio no pulso esquerdo.
5. **Cartelas:** fase correta (Aproximação → Vínculo → Vantagem → Dependência → Coerção → Saída) e canais no fim.

## Pendências abertas (o que já se sabe, para não redescobrir)

| Item | Situação |
|---|---|
| EP04 ficou dessincronizado em ~2 frases e a voz 10–15% mais rápida que o narrador original | **não re-renderizado** (custo). A correção vale a partir do E5. Refazer o E4 custaria 6 clipes |
| Locações novas ainda sem referência | terminal/pátio, portaria, ônibus, loja, boteco, banco — 5 a 6 imagens, geradas uma vez para a temporada |
| Personagens coadjuvantes sem folha | Cleber, Ruan, Téo entram a partir do E7/E9; gerar `cleber_mestre.png` etc. antes de precisar |
| Pico de −0,9 dBTP no E4 | corrigido no v2 com teto −1,5 |
| Distribuição | nada publicado ainda; vertical 9:16 já está pronto para Reels/Shorts/TikTok |

## Orçamento por episódio na rota escolhida

3 a 6 chamadas de vídeo de 5–15 s (tier econômico), 1 de voz, 0 a 2 de imagem quando a locação é nova, música e SFX já existentes no repositório. Estimativa agregada de E5 a E12 em `dados/plano_provisional_E5_E12.md`: ~44 clipes, ~530 s de vídeo gerado.

## Regra de convivência com o autor

Ele aprova **visual em trecho de 15 s antes do episódio inteiro** e **voz antes de gerar imagem**. Já derrubou uma rota por custo ("quero mais barato com qualidade") e já reclamou de sincronia — as duas coisas viraram código neste repositório. Não volte a discutir gosto sem mostrar frame; mostre o quadro.
