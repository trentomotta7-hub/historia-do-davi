# INTELIGÊNCIA DA SÉRIE — fonte única de verdade

Este arquivo é a memória do projeto. **Qualquer sessão nova deve ler este arquivo antes de gerar qualquer coisa.** Ele existe para que a série continue com a mesma cabeça, mesmo que o agente, o modelo ou o computador mudem.

## 1. O que é a série

Documentário-drama animado em vertical (9:16), episódios de **60 a 63 s**, sobre **Davi, 20 anos, de Navegantes (SC)**, aliciado para tráfico internacional de drogas pelo "cara boa" do bairro. Tom: factual, seco, sem moralismo, sem trilha de pena. A série é útil porque **mostra o método do aliciamento, não o crime**.

Fase atual: E1–E3 existem (produção anterior do autor). **E4 foi produzido por esta pipeline** e está em `media/final/EP04_quem_liga.mp4`. E5–E12 estão roteirizados, aguardando produção.

## 2. Voz (não trocar nunca)

| Parâmetro | Valor travado |
|---|---|
| Voz | `pt-br-storyteller-5` (Voz A) |
| Idioma | `pt-BR`, uma única vez por episódio, sem estilo no prompt de voz |
| Locutor | masculino, barítono grave, F0 104–128 Hz |
| Taxa de articulação pura | ~22 caracteres/segundo **dentro** da fala |
| Taxa percebida no episódio | ~12,5 caracteres/segundo **incluindo pausas** |
| Pausas | ~39% do tempo do episódio é silêncio entre frases |

Amostras comparativas em `media/audios/amostra_voz_A_*.wav` e `amostra_voz_B_*.wav`. A Voz B é mais grave e mais lenta; é a alternativa se um dia a A soar apressada demais.

**Regra de ouro:** o minuto não se fecha escrevendo mais texto, e sim respeitando as pausas. Texto-alvo por episódio: **660 a 720 caracteres**.

## 3. Escrita narrativa (o "jeito" da série)

1. Frases de **5 a 8 palavras**. Quase todas começam com o nome ou com "E".
2. **Terceira pessoa colada no personagem**: narra o que ele faz e o que ele sente sem explicar. "Davi desligou e ficou no chão."
3. Mensagem de celular é **lida em voz alta pelo narrador**, no mesmo tom baixo, entre aspas. A friez da leitura é o que assusta.
4. **Uma decisão por episódio.** Nunca duas.
5. Nunca moralizar, nunca julgar, nunca dizer "e ele percebeu que estava errado".
6. Terminar no ar: última frase é um golpe curto, com corte seco.
7. Refrão emocional recorrente (a série inteira se mede por ele): **a mãe perguntando algo simples na cozinha** — "Tá tudo bem?" / "Perguntou se ele havia dormido".
8. Nunca mostrar dinheiro como solução. Dinheiro na série é **dívida**, não conforto.

Exemplo canônico (E4, trecho final):

> E ninguém falou em dinheiro. Na cozinha, a mãe perguntou quem era. "Um amigo. Do time." E foi a primeira vez que ele gostou de responder.

## 4. Personagens e locações (bíblia visual)

Render 3D estilo animação de longa-metragem, pele com subsurface, olhos grandes, luz volumétrica, grão fino. **Toda imagem nova anexa a folha de identidade do personagem como referência** — sem isso, no terceiro episódio o Davi vira outra pessoa.

| Chave | Arquivo | Papel |
|---|---|---|
| `davi` | `media/referencias/davi_mestre.png` | protagonista, 20 anos, camisa de linho branco manga dobrada, **tatuagem floral no braço DIREITO**, berm cáqui, sapato marrom |
| `mae` | `media/referencias/mae_mestre.png` | mãe, ~48 anos, coque baixo, óculos de aro fino, camiseta lilás |
| `sandro` | `media/referencias/sandro_mestre.png` | recrutador, 38 anos, polo creme, watch dourado, **pickup branca**. Sempre gentil, nunca ameaçador |
| `loc_quarto_noite` | quarto, luz azul da janela com luzes laranja do porto |
| `loc_cozinha_noite` | cozinha, lâmpada tungstênio sobre mesa de madeira, azulejo branco |
| `loc_campo_bairro` | campo de terra ao fim de tarde, refletor, gol torto |
| `loc_casa_carro` | fachada da casa com pickup branca na calçada |

Prompts integrais e reusáveis em `prompts/referencias.json`.

**Regras de responsabilidade visual:** nenhum número de contêiner legível, nenhuma marca de terminal, nenhum logo real, rosto do Davi nunca coberto por legenda ou marca d'água.

## 5. Paleta como narrativa

O convite entra pela temperatura de cor:

- E1–E3 (antes): dia quente, tungstênio.
- E4–E6: quarto à noite; a **única luz quente passa a ser a tela do celular**.
- Flashbacks de favor prestado: **dourado de fim de tarde** (é assim que o bem feito é lembrado).
- E7 em diante (terminal): azul-petróleo + sódio laranja, 5h40 da manhã.
- Saída (E11–E12): luz do dia voltando na cozinha.

Um plano geral do porto por episódio, no máximo, até o E12.

## 6. Legendas e cartelas (especificação medida nos originais)

| Parâmetro | Valor |
|---|---|
| Corpo | 66 px em 1080 (equivale a ~34 px em 576, como nos originais) |
| Fonte | DejaVu Sans (original é sans grotesca parecida) |
| Bloco | 2 linhas no máximo, centrado, `MarginV=340` (~82% da altura) |
| Contorno | 3,8 px preto, sombra 0,8 |
| **Estilo 1 — `Padrao`** | **bold**, narração |
| **Estilo 2 — `Cita`** | peso **regular**, aspas curvas, para mensagens do celular |
| Duração da cue | existe enquanto existe fala. Sem fala, sem legenda |

Cartelas no fim, nesta ordem e sem música nova:

1. `FASE n — NOME` (2 s) sobre o último plano.
2. Canais de ajuda (2 s) sobre preto:
   `Disque Denúncia 181 · anônimo e gratuito` / `Comunica PF: gov.br/pf | CVV 188 · 24h`

As seis fases: Aproximação → Vínculo → Vantagem → Dependência → Coerção → Saída. **Este dispositivo é a razão de existir da nova temporada**: transforma a série em mapa reconhecível e protege o conteúdo nas plataformas (conteúdo educativo sobre prevenção).

## 7. Especificação técnica de entrega

1080×1920, 24 fps, H.264 High CRF 18, AAC 48 kHz, **−14 LUFS integrado**, pico abaixo de −1 dBTP, `-movflags +faststart`. Camada musical a ~−18 dB da voz, com *sidechain ducking* sob a narração; fade-out de 2 s no fim. Vídeo dos clipes entra **mudo**: som é sempre voz + cama + SFX pontual (vibração do celular é a assinatura sonora da série).

## 8. Roteiro de produção de um episódio (ordem obrigatória)

```
1. extrair a narração do roteiro           -> dados/narracoes.json  (já pronto para E4-E12)
2. gerar a voz, UMA chamada por episódio   -> narracao_epXX.wav
3. medir o audio real (silencedetect + DP) -> tempo real de cada frase
4. planejar BLOCOS a partir dessas fronteiras -> planejar_blocos.py  (corrige a sincronia)
5. gerar um clipe por bloco, com a DURACAO EXATA do bloco (5 a 15 s)
6. gerar legenda ASS sobre o audio real    -> retimed_e_legendas.py
7. montar: imagem + voz + cama + legendas  -> montar_episodio_v2.sh
8. conferir frames, loudness e sincronia frase-a-plano
```

**Nada de gerar vídeo antes de medir a voz.** É essa inversão que produz a imagem descolada da fala.

## 9. Custo (rota econômica, a escolhida do autor)

Tier econômico (`minimax-h3`, retrato, 768p) para todos os clipes; imagens de referência geradas uma única vez e reusadas a temporada inteira; música gerada uma vez. Por episódio: **3 a 4 chamadas de vídeo de 15 s** e 5 a 20 chamadas de imagem quando faltam locações novas. Detalhes e alternativas em `docs/05_estrategia_de_custo.md`.

## 10. Base factual (não inventar acima disto)

Pesquisa real que sustenta o arco, com fontes, em `docs/02_arco_da_temporada_E4_a_E12.md`: operação da Polícia Federal de maio de 2026 sobre grupo que usava os portos de **Navegantes, Itapoá e Imbituba** (18 presos, bloqueio de até R$ 646 milhões, ~4,6 t apreendidas); 40,5 kg de cocaína encontrados em carga lícita de pellets em Itapoá com destino a Gênova; perfil de idade média ~26 anos e penas ~4 anos para quem transporta; definição de aliciamento pela UNODC. Canais reais de ajuda: **181**, **Comunica PF**, **CVV 188**.

Regra editorial: nada de números de contêiner reais, nada de nomes reais de presos, nada de acusação a empresas reais. A série é ficção verossímil com método documentado.
