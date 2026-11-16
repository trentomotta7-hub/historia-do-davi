# Ficha de produção — EP04 "Quem liga" (episódio entregue)

Esta ficha registra os números reais do primeiro episódio produzido e vira a receita repetível para E5 a E12. Tudo abaixo foi medido, não estimado.

## Resultado entregue

| Item | Valor medido |
|---|---|
| Arquivo | `EP04/EP04_final.mp4` |
| Duração | **61,87 s** |
| Vídeo | H.264, 1080×1920, 24 fps, CRF 18, ~42,7 MB |
| Áudio | AAC 48 kHz estéreo, **−14,1 LUFS** integrado, pico verdadeiro −0,9 dBTP |
| Narração | Voz A (`pt-br-storyteller-5`), 681 caracteres, 19 frases |
| Legendas | 21 cues + 2 cartelas, ASS queimado, dois estilos (bold narração / regular citação) |

## Como o tempo foi fechado (o número que importa)

A narração crua saiu em **49,36 s**, não nos 54,5 s estimados. A medição por detecção de silêncio mostrou a razão real:

- fala efetiva: **30,05 s**
- pausas que a própria voz já faz entre frases: **19,31 s = 39% do tempo**

Isso confirma o dado dos episódios originais (metade do quadro em silêncio) e muda a forma de orçar: **não é preciso escrever mais texto para chegar a um minuto — é preciso respeitar as pausas.** Para este episódio foram acrescentados apenas **+0,376 s em cada um dos 23 respiro internos**, levando a voz a 57,6 s, mais 2 s de cartela de fase e 2 s de cartela de canais = 61,9 s.

Regra para os próximos: escreva 660–720 caracteres, gere, meça com `silencedetect`, e complete o tempo só com pausa. Nunca engarrafar texto nem acelerar a voz.

## Gasto real de geração (rota econômica)

| Chamada | O que gerou | Tier |
|---|---|---|
| 1× fala | narração completa de uma vez | voz |
| 2× imagem | cozinha e campo de terra (referências que faltavam) | imagem topo |
| 3× vídeo | blocos 2, 3 e 4, 15 s cada, retrato 768p | **econômico, zero premium** |
| reaproveitado | bloco 1 = clipe do teste de aprovação já gerado | — |
| 1× música | cama grave de 90 s gerada uma vez para a temporada | música |

Total por episódio nesta rota: **3 a 4 chamadas de vídeo e 5 a 20 chamadas de imagem**, com as referências de personagem e locação já travadas. Como a temporada inteira precisa de mais 8 episódios, o custo marginal desce ainda mais: cozinha, quarto, campo, casa com carro e as cinco folhas de identidade já existem e servem para todos.

## O que ficou bom e o que ajustar na próxima passada

**Funcionou:** a virada de paleta dentro do episódio (quarto azul → flashback dourado → cozinha quente) lê exatamente como convite sedutor; o plano do Sandro recusando o dinheiro da mãe na frente de casa é o melhor quadro do episódio e não precisa de legenda para ser entendido; o meio-sorriso final do Davi fechou a frase-tema.

**Ajustar:**

1. **Deriva de aúdio-imagem.** Os blocos de vídeo foram fatiados em janelas fixas de 15 s, mas a narração retemporizada empurrou cada frase para mais tarde. O resultado é que duas frases caem sobre um corte que não é o delas ("Sandro riu baixo" sobre o close da mão no lençol). Correção nos próximos: gerar os blocos já casados com as fronteiras do JSON `blocos_ep04.json` (frase → `t0`), ou deixar o corte acontecer no marco real da frase e mover a imagem, não o contrário.
2. **Pico verdadeiro a −0,9 dBTP** em vez de −1,0. Nada crítico, mas fixo `TP=-1.5` na segunda passada de loudnorm dos próximos episódios para sobrar margem na recodificação das plataformas.
3. **Telas de celular com ícones inventados.** O modelo desenha UI plausível, não legível. Como nos originais a mensagem é *lida em voz alta* pela narração e nunca mostrada legível, a regra certa é pedir tela apagada ou desfocada sempre que a frase for citação.
4. **A cartela de fase entrou sobre o último plano** (57,8–59,7 s) em vez de preto. Ficou melhor assim; mantenho como padrão da série.

## Pipeline reproduzível

```bash
cd serie_davi/EP05
python3 ../EP04/retimed_e_legendas.py     # mesmo script, mudar SRC e FRASES
bash ../EP04/montar_ep04.sh               # mesma montagem, blocos 1..4
```

Arquivos que já existem e servem para todos os episódios: as cinco folhas de identidade (`davi`, `mãe`, `sandro`, mais `cleber`/`ruan`/`teo` quando entrarem) e as locações `quarto_noite`, `cozinha_noite`, `campo_bairro`, `casa_carro`, além da cama musical e da vibração de celular.
