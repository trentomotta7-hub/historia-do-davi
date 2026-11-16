# 07 — O defeito do EP04 e a correção aplicada

Documento aberto por reclamação direta do autor: *"a fala está acelerada, diferente do que está aparecendo na tela; ele fala e depois aparece que ele está falando; a sincronia só fecha três ou quatro segundos depois"*. Isso é real, tem causa identificada e foi corrigido no pipeline. Fica aqui para que o defeito não volte em episódio nenhum.

## Diagnóstico: três problemas distintos, não um

### 1. Deriva de fronteiras (o problema principal, estrutural)

No EP04 a narração foi gerada, medida e **retemporizada** (pausas alongadas), mas os blocos de vídeo foram cortados em **janelas fixas de 15 s**, decididas antes da medição.

- A voz real: frase 1 em 0,25 s, frase 19 terminando em 57,65 s.
- A imagem: blocos em 0–15 / 15–30 / 30–45 / 45–60.

Como o retemporizou empurrou cada frase para mais tarde em relação ao plano original, dentro de um mesmo bloco o conteúdo já havia mudado de assunto antes do corte de imagem. Consequência medida: a frase *"Sandro riu baixo"* (32,7–36,2 s) caiu sobre o close da mão no lençol, que pertence à frase anterior; e *"Do outro lado, uma voz que ele conhecia"* entrou antes do plano de rosto que a sustenta. É exatamente o "fala e depois aparece" relatado.

**Correção:** a fronteira do bloco de vídeo passa a ser **derivada do áudio medido**, não escolhida antes. `pipeline/planejar_blocos.py` lê o JSON de tempos de frase e agrupa frases consecutivas em blocos de até 15 s, respeitando dois tipos de quebra: mudança de cena (marcada no roteiro) e acumulo de tempo. Cada clipe é então gerado com `duration_seconds` **igual à duração do seu bloco** (o tier econômico aceita de 5 a 15 s). Por construção, o corte de imagem acontece na fronteira da frase — não há como a imagem se atrasar.

### 2. Percepção de fala acelerada

Medição da narração do EP04: **30,05 s de articulação pura** para 681 caracteres = **22,7 caracteres/segundo** dentro da fala. Os episódios originais medem taxa percebida de ~12,5 caracteres/segundo (com pausas) e articulação pura em torno de 19–20. A Voz A é, portanto, cerca de **10 a 15% mais rápida que o narrador original** no corpo da frase — e como ela também fala em bloco corrido, a diferença é percebida como "atropelando a tela".

**Correção em duas camadas, ambas no pipeline v2:**

- `VELOC=0.94` (parâmetro no `montar_episodio_v2.sh`): aplica `atempo` na voz antes do mix, baixando a articulação para ~21,4 caracteres/segundo. Até ±6% de `atempo` não soa artificial em português porque não altera o timbre perceptível.
- `PAUSA_MIN=0.9`: o retemporizador passa a **travar um piso de pausa** entre frases, em vez de distribuir igualmente. Frases curtas e golpes ("Foi o suficiente.", "Ninguém obrigou. Foi ele.") recebem pausa maior que a média, porque é o silêncio delas que faz o efeito.

Se ainda soar rápido depois disso, a alternativa correta é trocar para a **Voz B** (`pt-br-storyteller-11`, F0 mais grave e articulação naturalmente mais lenta), regenerando só o áudio e remontando — o visual já gerado é reaproveitado.

### 3. Cue de legenda mais longa que a fala

O gerador de ASS atribuía a cada cue o intervalo entre o início da frase e o início da seguinte, o que incluía a pausa. Resultado: a legenda continuava na tela com o narrador calado, reforçando a sensação de descompasso.

**Correção:** cue termina no **fim do último bloco de fala da frase**, mais um respiro fixo de 0,25 s de cauda. Sem fala, sem legenda.

## Correções visuais menores registradas

| Problema | Correção |
|---|---|
| Tela do celular com ícones e números inventados | Regra de prompt: quando a frase é citação lida em voz alta, pedir **tela apagada ou fora de foco**. A informação vem da narração, nunca do insert |
| Tatuagem às vezes no braço errado | Reforçar no prompt "floral tattoo sleeve on his **RIGHT** forearm" em todo clipe que mostre antebraço, e anexar a folha de identidade como referência |
| Pico verdadeiro em −0,9 dBTP | Segunda passada de loudnorm com `TP=-1.5`, sobrando margem para a recodificação das plataformas |
| Traço do rosto variando entre planos do mesmo bloco | Aceitável no tier econômico; se um close for crítico (E9, cena-espelho), gerar aquele único clipe no tier de topo em 480p e fazer upscale |

## Estado atual do pipeline

Arquivos novos neste repositório, já com as correções:

- `pipeline/planejar_blocos.py` — deriva blocos de imagem do áudio medido
- `pipeline/montar_episodio_v2.sh` — montagem genérica com `VELOC`, `PAUSA_MIN`, cartelas e loudnorm em duas passadas
- `pipeline/medir_frases.py` e `pipeline/gerar_legendas.py` — retemporização com piso de pausa e cue limitada ao fim da fala
- `pipeline/extrair_narracoes.py` — roteiro → frases com estilo e locação (scanner de aspas, não regex)
- `dados/narracoes.json` — texto de narração de E4 a E12 já dividido em frases com marca de estilo (`P` narração / `C` citação)

O EP04 entregue permanece como está (a correção não re-renderiza o que já foi gasto). Para E5 em diante o pipeline v2 é o padrão, e o defeito relatado não deve reaparecer.

## Re medição do mesmo áudio com a pipeline v2 (executada, não projetada)

Rodando `medir_frases.py` + `planejar_blocos.py` + `gerar_legendas.py` sobre a narração crua do EP04 que está versionada em `media/audios/EP04_narracao_crua.wav`:

| grandeza | v1 (episódio entregue) | v2 (planejamento corrigido) |
|---|---|---|
| frases reconhecidas | 19 | 19 |
| citações preservadas inteiras | 4, duas delas partidas no meio | 4, nenhuma partida |
| voz retemporizada | 57,60 s (pausas distribuídas por igual) | **54,02 s** (piso de pausa + reforço no golpe) |
| blocos de imagem | 4 janelas fixas de 15 s | **6 blocos** nas fronteiras reais: 15,00 / 5,00 / 6,84 / 13,81 / 5,00 / 10,40 s |
| quebra de cena casada com a fala | não | sim — o flashback do campo e o da casa viram blocos próprios |
| cues de legenda | 21, ocupando a pausa inteira | **21 + 2 cartelas**, terminando no fim da fala |

A v2 ficou 3,6 s mais curta exatamente por parar de inflar pausa uniformemente: devolve silêncio nas frases longas e concentra silêncio depois do golpe. É a leitura dos episódios originais.

Refazer o EP04 com a correção pede 6 clipes novos (3 reaproveitáveis do próprio episódio). Ficou registrado como pendência em `CONTINUA_AQUI.md`, não como tarefa imediata: a verba rende mais começando pelo E5, onde o defeito ainda não existe.

## Segundo relato do autor: "o vídeo está adiantado para a narração"

Confirmado, e a causa é mais específica do que a primeira diagnose. No EP04 entregue eu fiz as coisas em ordem invertida:

1. gerei os 4 clipes de 15 s contra o tempo **estimado** do roteiro;
2. gerei a voz;
3. **estichei as pausas da voz depois disso**, para chegar perto do minuto.

Ou seja: a imagem foi cortada no relógio de 49 s da voz crua, e a voz que toca em cima é a de 57,6 s. Toda frase passou a cair ~0,3 a 0,5 s depois do plano que a ilustra, e o efeito acumula — no fim do episódio a imagem corre quase um segundo à frente. É literalmente "primeiro aparece, depois ele fala".

### Correção definitiva, aplicada sem gerar mídia nova

Como cada clipe de 15 s do tier econômico foi promptado em três planos internos (`Shot 1 0-5s`, `Shot 2 5-10s`, `Shot 3 10-15s`), o material já contém cortes compatíveis com frases individuais. `reaproveitar_clipes.py` recorta esses 12 planos internos, acrescenta um décimo terceiro recorte onde a frase pedia outra respiração, e reposiciona cada recorte na janela medida da sua frase (`início = t0 − 0,30 s`, `fim = início do próximo recorte`). Resultado: **deriva máxima 0,00 s por construção**, com congelamento máximo de 1,49 s em um único segmento.

Passos executados sobre mídia que já existia:

| etapa | arquivo | custo |
|---|---|---|
| desacelerar a voz | `atempo=0.94` → 52,49 s | zero chamadas |
| medir o áudio desacelerado | `medir_frases.py` → voz retemporizada 56,42 s | zero |
| recortar e reposicionar planos | `reaproveitar_clipes.py` → 13 segmentos | zero |
| legenda sobre o novo relógio | 21 cues + 2 cartelas | zero |
| montagem + loudnorm −14 LUFS / −1,4 dBTP | `EP04_final.mp4`, 60,62 s, 37,5 MB | zero |

### Regra nova que entrou na pipeline

A desaceleração aconteceu **antes** da medição, não dentro do mix. Medir o tempo de uma voz e tocar outra é a mesma família de erro que gerou a primeira deriva: áudio, legenda e imagem precisam nascer do mesmo arquivo medido. `montar_episodio_v2.sh` não tem mais `atempo` no grafo de mix — o passo 2.5 do `CONTINUA_AQUI.md` aplica `atempo` no bruto e o passo 3 mede o resultado.

Estado atual do EP04: `media/final/EP04_quem_liga.mp4` (v2). Os quadros de conferência frase a frase estão em `media/conferencia/EP04_v2_sincronia_A.jpg` e `_B.jpg` — um quadro por segmento, capturado no meio da frase que ele ilustra.
