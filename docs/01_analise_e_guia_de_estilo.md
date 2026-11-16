# A história do Davi — análise dos episódios 1 a 3 e guia de estilo

Documento de trabalho para continuar a série com a mesma voz, o mesmo visual e o mesmo ritmo. Todas as métricas abaixo foram medidas nos três arquivos originais (transcrição com timestamps, análise do áudio, medição de pixels dos frames). Nada aqui é opinião solta: onde há número, ele veio do arquivo.

---

## 1. O que já existe (ordem correta dos episódios)

Os arquivos vieram fora de ordem. A sequência narrativa real é esta:

| # | Arquivo | Duração | Função na história | Última frase (gancho) |
|---|---|---|---|---|
| **E1** | `21f9ad92…mp4` | 30,2 s | Retrato do personagem e da cidade. Cria a tese: ser confiável é um ativo. | "…pode colocar uma escolha difícil bem na frente dele." |
| **E2** | `d0929eda…mp4` | 61,6 s | O primeiro contato. A mensagem vaga, o dinheiro rápido, o "confia em mim". | "Davi olhou pras luzes do porto. E naquela noite não dormiu." |
| **E3** | `d349aa15…mp4` | 62,9 s | A noite em claro e a descoberta do real motivo da escolha: o nome dele. | "Atender podia revelar quem tava por trás. Mas por que escolheram justamente ele?" |

Formato comum aos três: **9:16, 576×1024, 24 fps, AAC 44,1 kHz estéreo**, narração contínua em português do Brasil, legendas queimadas dentro do quadro, sem trilha de marca, sem locução de abertura. E1 é curto de propósito (30 s, funciona como isca/anúncio); E2 e E3 estão na faixa de 60 s que você quer padronizar.

---

## 2. A fórmula narrativa (o DNA da série)

O que faz os três episódios soarem como a mesma série não é o tema, é a mecânica. São sete regras:

**2.1 Frases curtas, quase telegráficas.** A média é de 5 a 8 palavras por frase, com períodos secos: "Amanheceu." / "Não dormira." / "Dessa vez não mentiu." O verbo costuma ser o último som antes da pausa. Frases de uma ou duas palavras aparecem de propósito, para criar respiração e peso.

**2.2 Terceira pessoa colada no personagem.** O narrador sabe o que Davi pensa ("não era apenas dinheiro", "mas não tava"), mas nunca sabe o que os outros pensam. Isso mantém o público dentro da cabeça dele e mantém o inimigo invisível.

**2.3 As mensagens são lidas em voz alta.** Todo texto de celular vira fala, entre aspas, no mesmo tom baixo da narração: "Pensamos em você porque as pessoas confiam no seu nome." A mensagem nunca é gritada, nunca muda de voz: a frieza é o que assusta.

**2.4 Um episódio, uma decisão.** E1 = quem ele é. E2 = o convite. E3 = ele não consegue mais fingir. Nenhum episódio tem duas viradas.

**2.5 A mãe é o barômetro moral.** Em todos os episódios há uma cena de cozinha em que ela pergunta algo simples ("Tá tudo bem?", "Perguntou se ele havia dormido") e ele responde. A série inteira se mede por quantas vezes, e com quanta verdade, ele responde essa pergunta. É o coração emocional: a cada episódio o público aprende a esperar a pergunta.

**2.6 Zero moralismo.** O narrador não condena, não explica o crime, não dá conselhos. Ele só mostra o custo. Essa é a decisão mais importante da série e a que dá credibilidade: o espectador não se sente ensinado, se sente perto.

**2.7 Corte no ar.** Todo episódio termina no meio de uma ação — o dedo sobre o botão de atender, a luz do porto, a mensagem nova. Nunca com conclusão. E3 termina com a única pergunta direta ao público da temporada, que é o gancho perfeito para E4.

**Estrutura de blocos (reproduzível em qualquer episódio de 60 s):**

| Bloco | Tempo | Função | Exemplo (E3) |
|---|---|---|---|
| A — Isca | 0–6 s | Frase de impacto ou eco da mensagem anterior | "Dinheiro rápido. Confia em mim. Amanhã você vai entender." |
| B — Rotina quebrada | 6–20 s | O lugar comum mostrando sinal de desgaste | Amanheceu na janela, mensagem de ontem aberta |
| C — Fricção | 20–40 s | A revelação que aperta | "…as pessoas confiam no seu nome" |
| D — Teste emocional | 40–55 s | A pergunta da mãe / o medo visível | "Não consegui", dessa vez não mentiu |
| E — Corte no ar | 55–62 s | Ação interrompida + pergunta | O número desconhecido ligando |

---

## 3. A voz do narrador (medida, não estimada)

| Métrica | E1 (30 s) | E2 (61 s) | E3 (63 s) | Leitura |
|---|---|---|---|---|
| Frequência fundamental (F0 mediana) | 128 Hz | 107 Hz | 104 Hz | **Masculino, barítono grave.** Faixa alvo 100–130 Hz |
| Taxa de fala | 13,4 car/s | 10,6 car/s | 12,7 car/s | **≈ 12,5 caracteres/segundo**, sem pressa |
| Ocupação de fala | 55 % | 47 % | 57 % | Quase metade do tempo é silêncio: trilha e imagem seguram |
| Camada abaixo da voz (piso/voz) | 9 % | 12 % | 16 % | Existe **cama contínua de música/ambiente** a −18/−12 dB da voz |
| Energia em sub-graves (20–120 Hz) | baixa | alta | alta | E2 e E3 têm drone grave sustentado; E1 é mais seco |

Perfil em palavras: homem adulto, voz grave e limpa, tom de **conversa baixa de quem conhece a cidade**, sem locução publicitária, sem suspense forçado de trailer. Ele conta como quem já viu isso acontecer. As pausas são longas e não têm música de tensão por cima.

### Candidatas de voz para os novos episódios

Como clonagem de voz não é permitida na ferramenta, o caminho é a voz sintética mais próxima do perfil medido. Gerei quatro amostras com o texto real do E3 e medi as mesmas métricas:

| Voz (ID exato) | F0 | car/s | Ocupação | Julgamento técnico |
|---|---|---|---|---|
| `pt-br-storyteller-5` | 97,6 Hz | 12,4 | 55 % | **Melhor ritmo e respiração.** Levemente mais grave que o original |
| `pt-br-storyteller-11` | 116,8 Hz | 12,9 | 62 % | **Melhor casamento de timbre** (dentro da faixa 100–130 Hz) |
| `pt-br-storyteller-6` | 109,6 Hz | 14,1 | 53 % | Timbre bom, mas fala rápido demais (preciso de 20–25% a mais de pausa) |
| `pt-br-podcaster-9` | 92,0 Hz | 13,1 | 41 % | Estilo radiofonizado, amplitude emocional grande demais para a série |

As duas finalistas são **A (`storyteller-5`)** e **B (`storyteller-11`)**. Ouça os arquivos de audição e escolha: A é mais perto do *jeito* de falar do original; B é mais perto da *altura* da voz. Uma vez escolhida, essa ID fica congelada para todos os episódios.

---

## 4. Como dimensionar o roteiro (para fechar em 60 s)

Regra prática derivada das medidas, já validada contra E2 e E3:

- **60 s de vídeo = 740 a 800 caracteres de narração** (≈ 125 a 140 palavras).
- **24 a 26 blocos de legenda** por episódio (bloco = 1 ideia, 1 a 2 linhas).
- **34 a 38 caracteres por linha** no máximo.
- Deixe **2 a 4 segundos de silêncio por episódio** — sem voz, só trilha e imagem. É o que faz a série não virar podcast.
- Frases do narrador: até 9 palavras. Mensagens de celular: até 12, sempre entre aspas.
- Truque de contagem: escreva o texto, some os caracteres, divida por 12,5. Se der mais de 60, corte frases antes de pensar em acelerar a voz.

---

## 5. Gramática visual

**Render.** Animação 3D estilo longa de animação (olhos grandes, pele suave, proporções levemente estilizadas, iluminação física). Nada de realismo fotográfico: o estilo animado é o que permite contar essa história sem sensacionalismo e sem parecer notícia policial.

**Geometria.** 9:16, personagem centralizado ou em terços, planos médios e americanos, com **inserts de mãos e celular** ocupando o terço inferior. Câmera estável, sem microfonía de handheld; movimento lento de aproximação. Sem transição chamativa: corte seco a cada bloco.

**Paleta por estado emocional** — este é o dispositivo visual da série:

| Momento | Cor e luz |
|---|---|
| Dia, casa, loja, ônibus | Quente e clara: tungstênio 3.200–4.000 K, creme, madeira, branco, azul de dia |
| Noite, quarto, janela | Azul-petróleo frio + um único practical quente (abajur) + **a tela do celular iluminando o rosto** |
| O porto | Luzes de container amarelas/laranjas ao fundo, desfocadas, sempre por uma janela ou no horizonte |

A série inteira é um deslocamento dessa paleta: quanto mais o convite avança, mais o quadro fica azul-noturno e mais a única fonte de luz quente vira a tela do celular.

**Motivos que voltam** (use sempre, são a assinatura): o busão, a arara de roupas da loja, a pia e os azulejos da cozinha, a mesa de madeira com o copo, a janela com o porto, a tela do celular em close, as mãos sobre a mesa.

**Personagem — Davi, 20 anos.** Cabelo castanho escuro penteado para cima e para trás, sobrancelha marcada, olhos grandes castanhos, pele morena clara, barba por fazer discreta. **Tatuagem floral no braço direito** (sobe do punho até o cotovelo), camisa social de linho branco com manga dobrada, bermuda cáqui, mocassim marrom, relógio de pulso. É o figurino fixo dos três episódios: mantenha, ele é o que faz o público reconhecer o personagem entre episódios.

**Personagem — a mãe.** Cabelo castanho preso em coque baixo, óculos de grau, blusa lilás, jeans. Sempre em contra-campo à mesa da cozinha ou na bancada. Ela nunca aparece "errada": ela só pergunta.

**Regra de cena que ainda não foi usada e precisa entrar:** o **porto não aparece por dentro** nos três episódios. Isso é uma escolha — e um limite. A partir de E8, a série precisa entrar no terminal, e é aí que a coerência visual vai ser testada. Reference de localização precisa ser criada antes (ver documento de produção).

---

## 6. Legendas: especificação exata para replicar

Medidas nos frames originais:

- **Posição:** bloco centralizado horizontalmente, centro vertical em **≈ 88% da altura** do quadro (a ~100 px da base em 1024).
- **Largura do bloco:** 60 a 68% da largura do quadro; **máximo 2 linhas**.
- **Altura de letra:** ≈ 28–34 px em quadro de 576 px de largura (≈ 55–65 px em 1080).
- **Cor e contorno:** branco puro com contorno preto de traço médio (cerca de 20–25% do corpo da fonte). Sem caixa de fundo, sem sombra difusa.
- **Dois estilos, e essa distinção importa:**
  - **Narração:** peso **bold**, sem aspas, pontuação final. Ex.: "Com os amigos, é o cara que escuta e aparece quando precisam."
  - **Mensagem do celular:** peso **regular**, envolvida em aspas curvas “ ”, terminando com ponto dentro da aspas. Ex.: “Pensamos em você porque as pessoas confiam no seu nome.”
- **Sincronismo:** legenda só existe enquanto há fala. Nos silêncios o quadro fica limpo (confirmado em frame do E3 em t=34 s e t=53 s, sem texto). É isso que dá o ar "limpo" do original.
- **Quebra de linha:** por ideia, nunca no meio de um nome próprio, e nunca deixando artigo sozinho no fim da linha.

Único ajuste recomendado: no Reels/TikTok a faixa dos 15% finais é coberta por legenda de interface, botões e descrição. **Subir o bloco para 80–82%** nos novos episódios muda a leitura no celular e não altera o estilo.

---

## 7. Som

- **Voz na frente:** limpa, sem reverberação de estúdio, level estável. Alvo de entrega: **−14 LUFS integrado** para rede social (pico −1 dBTP).
- **Cama:** música/ambiente contínua a −18/−12 dB da voz (a medição deu 9–16%). É drone grave + textura, não trilha melódica. Nas cenas de dia, entra o ambiente real: ônibus, porta, cozinha.
- **Punctuation SFX da série:** a vibração do celular. É o único "susto" sonoro usado, e funciona porque ele sempre chega antes da resposta emocional. Mantê-lo.
- **O que não tem, e não deve ter:** whoosh de transição, riser de trailer, música que cresce no gancho, sting de impacto. A série é contida e é isso que a diferencia.
- Trilha recomendada para os novos episódios: pulso grave lento (55–70 BPM), notas longas, sem batida de percussão; nas cenas de cozinha, tirar a música quase a zero e deixar só o ambiente.

---

## 8. Diagnóstico final: o que está bom e o que a série ainda deve

**Mantém tudo:** a contenção do narrador, a regra de uma decisão por episódio, a mãe como medidor moral, a paleta que esfria ao longo da história, o celular como antagonista silencioso.

**Ganha com o ajuste:** (1) padronizar 58–62 s em todos os episódios, inclusive o primeiro, que hoje tem 30 s e por isso funciona melhor como anúncio da série do que como episódio 1; (2) carteola de abertura de 0,8 s com "parte X / 12", que resolve a ordem dos episódios em perfil; (3) lacre de prevenção nos últimos 3 s, com número real de denúncia, que transforma a série em serviço público e protege o conteúdo de moderação; (4) entrar no porto, com reference visual próprio, para E8 em diante não quebrar a coerência; (5) um antagonista com rosto e nome, porque a série hoje tem um inimigo sem cara — o que é bom até certo ponto, e depois cobra juros.

O E3 parou exatamente no melhor lugar possível: o dedo dele sobre o botão de atender. A continuação natural tem que responder *quem liga* — e a resposta mais incômoda e mais verdadeira é que é alguém de quem ele já gosta.
