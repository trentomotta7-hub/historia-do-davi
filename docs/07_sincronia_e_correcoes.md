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
- `pipeline/retimed_e_legendas.py` — retemporização com piso de pausa e cue limitada ao fim da fala
- `dados/narracoes.json` — texto de narração de E4 a E12 já dividido em frases com marca de estilo (`P` narração / `C` citação)

O EP04 entregue permanece como está (a correção não re-renderiza o que já foi gasto). Para E5 em diante o pipeline v2 é o padrão, e o defeito relatado não deve reaparecer.
