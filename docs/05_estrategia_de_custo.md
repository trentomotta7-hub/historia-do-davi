# Estratégia de custo — produzir a temporada pagando menos sem perder o visual

A série dos episódios 1 a 3 é, na prática, **barata de imitar**: os planos são longos, a câmera quase não se move, e quase tudo é personagem parado olhando uma tela. Isso significa que a maior parte do quadro não precisa ser gerada como vídeo. O custo de um episódio é dirigido por três variáveis, e só por elas:

1. **Número de chamadas de geração de vídeo** (não o número de planos — dá para fazer um episódio com 4 chamadas de 15 s em vez de 20 de 5 s).
2. **Tier do modelo** (`minimax-h3` é a rota de custo baixo em 768p; `seedance-2-0-fast` é o meio; `seedance-2-5` é o topo, com resolução 480p/720p — gerar em 480p e fazer upscale na montagem reduz ainda mais).
3. **Duração pedida por chamada** (cada segundo extra de clipe é custo extra; clipe de 5 s com um único movimento rende mais que clipe de 10 s parado).

## As três rotas

### Rota A — Híbrida, recomendada (≈ 70% mais barata que gerar tudo em vídeo)
Imagem ainda é o ativo mais barato da casa. Então:

- Para **cada plano** do shot list, gera-se **uma chave de imagem** (o quadro principal) no modelo de imagem já usado nas referências.
- Só os planos com **movimento real e visível** viram clipe de vídeo: o polegar deslizando para atender, a empilhadeira cruzando o pátio, o envelope sendo aberto, o celular vibrando na mesa. Em um episódio de 20 planos, isso é **4 a 5 clipes**, não 20.
- Os outros 15 planos entram como **push-in/pull-out lento em still** (Ken Burns em FFmpeg, custo zero de geração), exatamente como os episódios originais já se comportam.
- Tier de vídeo: `minimax-h3` 768p para os inserts de objeto e mãos; `seedance-2-5` em 480p **somente** para os closes de rosto em que a emoção é o conteúdo (em média 2 por episódio).

Contagem por episódio de 60 s: **~20 imagens + 4 a 5 clipes + 2 clipes premium**. Comparado com a Rota C: menos da metade das chamadas caras.

### Rota B — Vídeo econômico em blocos longos
Se preferir movimento em tudo: **4 chamadas de 15 s em `minimax-h3`** por episódio (60 s), com as referências de personagem e locação anexadas, e cortes internos descritos no próprio prompt. Uma única chamada cobre vários blocos do shot list, o que corta o custo administrativo e melhora a consistência entre planos vizinhos. Rende mais movimento que a Rota A, mas o rosto sai menos confiável, principalmente em close.

### Rota C — Qualidade de topo (não é o que você pediu)
`seedance-2-5` em 720p, ~1 clipe por plano. É a rota cara. Só vale para o episódio 9 (a cena-espelho do café) e para o final da temporada, se você quiser um "filme" e não uma série de rede social.

## O que fazer mesmo para gastar menos (independente da rota)

- **Gerar a narração antes, sempre.** O erro mais caro desta produção é gerar vídeo primeiro e depois descobrir que a fala tem 70 s: vira clipe sobrando, e clipe sobrando é dinheiro jogado fora.
- **Bloco de narração = bloco de clipe.** Agrupar 2 ou 3 frases do shot list em um plano único de 5 a 6 s, em vez de um plano por frase. Reduz de ~20 para ~11 unidades por episódio sem mudança visível no resultado, porque o ritmo da série é lento.
- **Upscale na montagem, não na geração.** Pedir 480p/768p e escalar para 1080×1920 com `lanczos` no FFmpeg. Os originais são 576×1024, então ninguém vai notar — e você paga menos por segundo gerado.
- **Reaproveitar locação.** Cozinha, quarto e loja aparecem em quase todos os episódios. Uma imagem de referência por locação serve para a temporada inteira; o que muda é só a luz (dia/noite), que se resolve no prompt, não com nova geração.
- **Reusar clipe quando a frase é a mesma cena.** No E8, por exemplo, "ele ficou olhando a gaveta" e "na quinta pagou a consulta" podem dividir o mesmo plano de 6 s com dois cortes de legenda.
- **Reservar retrabalho.** Historicamente 20 a 30% dos clipes voltam. Orçar 3 retries por episódio evita regenerar a coisa toda depois.

## Estimativa por episódio na Rota A

| Item | Quantidade | Observação |
|---|---|---|
| Narração | 1 chamada | texto verbatim do roteiro, voz congelada da temporada |
| Camada musical | 1 chamada por temporada | gerar 90 s uma vez e fatiar para todos os episódios |
| Imagens-chave | ~20 chamadas de imagem | 9:16, mesmas referências |
| Clipes `minimax-h3` | 4 a 5 de 5 s | mãos, objetos, veículos, portaria |
| Clipes `seedance-2-5` | 2 de 5 s, 480p | closes de rosto críticos |
| Legendas e cartelas | custo zero | ASS renderizado no FFmpeg |
| Retries previstos | +3 clipes | margem de segurança |

Para a temporada completa (E4 a E12), o total na Rota A é **~180 imagens + ~45 clipes econômicos + ~18 clipes premium**, contra ~184 clipes de vídeo da abordagem "tudo em vídeo" — que é a diferença de custo real que você pediu para cortar.
