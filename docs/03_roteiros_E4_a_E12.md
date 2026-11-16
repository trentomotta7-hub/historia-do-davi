# Roteiros E4 a E12 — prontos para gravar

Padrão de cada episódio: **9:16, 576×1024 (ou 1080×1920 na exportação final), 24 fps, 58–62 s**, narração única em pt-BR, legendas queimadas, cartela de fase no fim (2 s) e cartela de canais de ajuda (2 s).
As colunas de tempo são alvos de montagem: depois de gerar a narração, meça o áudio real com `ffprobe` e redistribua os tempos. No método narration-led o áudio manda e a imagem segue.

Convenções deste documento:
- **Narração / legenda** = texto exato que entra queimado no quadro, no mesmo momento da fala. Texto entre aspas " " é mensagem do celular ou fala de personagem citada (peso regular); o resto é narração (peso bold).
- **IMAGEM** = plano, enquadramento, movimento, luz. Cada linha é um clipe de 4 a 6 s, sem corte interno.
- **SOM** = o que existe além da voz.
- No fim de cada episódio, o bloco `NARAÇÃO P/ TTS` é o texto corrido, verbatim, pronto para colar na ferramenta de voz (mesma voz em todos os episódios).

---

# EPISÓDIO 4 — "Quem liga"
**Fase:** 2 — Vínculo · **Decisão:** atender um número que ele reconhece · **Paleta:** 70% azul-noturno, 30% cozinha quente

| # | Tempo | Narração / legenda | Imagem | Som |
|---|---|---|---|---|
| 1 | 0,0–3,2 | **Davi ficou com o dedo sobre o botão.** | Close no celular na mão dele, tela acesa mostrando número de Navegantes; luz da tela pintando o queixo. Câmera parada, 35 mm. | Zumbido baixo; respiração |
| 2 | 3,2–6,4 | **O número não era desconhecido.** | Insert da tela; fora de foco, o porto ao fundo pela janela. | Drone grave entra |
| 3 | 6,4–9,8 | **Ele atendeu no terceiro toque.** | Polegar desliza; plano médio dele na cama, luz azul, abajur apagado. | Bipe de chamada |
| 4 | 9,8–13,6 | **Do outro lado, uma voz que ele conhecia.** | Close no rosto, luz da tela; ele senta na beirada. | Voz do outro lado abafada, sem palavra |
| 5 | 13,6–17,4 | "Davi, meu filho. Aqui é o Sandro." | Insert da tela com a chamada em andamento; o nome "Sandro" digitado no contato. | Voz masculina quente, fora de quadro |
| 6 | 17,4–21,0 | **Sandro. O cara boa do bairro.** | Flash-back curto, mais claro: Sandro entregando bola e coletes para crianças no campo de terra, todos rindo. Luz de fim de tarde. | Ambiente de campo, risada distante |
| 7 | 21,0–25,0 | **Quem patrocinava o time e pagava o aluguel do campo.** | Plano de Sandro acendendo o refletor do campo com a chave do carro no bolso. | Clique de refletor, zumbido de sódio |
| 8 | 25,0–29,5 | **Quem levou a mãe dele ao hospital e não quis receber nada.** | Flash-back: carro branco na frente de casa, mãe no banco da frente, Sandro na calçada recusando o dinheiro com a mão. | Porta de carro, motor |
| 9 | 29,5–33,0 | **"Aquele número é nosso, tranquilo."** | Volta ao quarto. Davi encosta as costas na cabeceira, o rosto relaxa. | Voz ao telefone |
| 10 | 33,0–37,0 | **"Não é nada errado. Só quero te mostrar uma coisa."** | Insert: a mão dele aperta o lençol. A luz da tela treme no teto. | — |
| 11 | 37,0–40,0 | **Davi perguntou o que era.** | Contraplano dele de perfil, janela atrás com as luzes do porto. | — |
| 12 | 40,0–43,5 | **Sandro riu baixo.** | Close só na boca dele se abrindo em meio sorriso. | Risada curta ao telefone |
| 13 | 43,5–48,0 | "Coisa de gente em que a gente confia." | Davi olha a tela depois de desligar; o contato agora com nome salvo. | Bipe de desligar; drone sobe |
| 14 | 48,0–51,0 | **A ligação durou um minuto e quarenta.** | Insert do cronômetro da chamada; o quarto mudo atrás dele. | — |
| 15 | 51,0–53,5 | **Foi o suficiente.** | Davi deita de novo, mãos atrás da cabeça, luz azul da janela no teto. | Drone |
| 16 | 53,5–56,5 | **E ninguém falou em dinheiro.** | Plano americano na cozinha, luz do teto acesa, mãe lavando louça de costas. | Torneira, louça |
| 17 | 56,5–59,0 | **"Quem era?" — perguntou a mãe.** | Contra-campo: mãe secando a mão no pano, óculos embaçados pelo vapor. | Torneira cessa |
| 18 | 59,0–61,5 | **"Um amigo. Do time."** | Davi de frente, meio sorriso, o celular na mesa entre os dois. | — |
| 19 | 61,5–64,5 | **E foi a primeira vez que ele gostou de responder.** | Ele pega o celular. Corte seco para preto. | Drone corta a zero |
| 20 | 64,5–66,5 | — | **Cartela:** `FASE 2 — VÍNCULO` + `181 · Comunica PF · CVV 188` | Silêncio com um tom grave |

**NARAÇÃO P/ TTS**
```
Davi ficou com o dedo sobre o botão. O número não era desconhecido. Ele atendeu no terceiro toque. Do outro lado, uma voz que ele conhecia. "Davi, meu filho. Aqui é o Sandro." Sandro. O cara boa do bairro. Quem patrocinava o time e pagava o aluguel do campo. Quem levou a mãe dele ao hospital e não quis receber nada. "Aquele número é nosso, tranquilo. Não é nada errado. Só quero te mostrar uma coisa." Davi perguntou o que era. Sandro riu baixo. "Coisa de gente em que a gente confia." A ligação durou um minuto e quarenta. Foi o suficiente. E ninguém falou em dinheiro. Na cozinha, a mãe perguntou quem era. "Um amigo. Do time." E foi a primeira vez que ele gostou de responder.
```

---

# EPISÓDIO 5 — "Sem compromisso"
**Fase:** 3 — Vantagem · **Decisão:** ouvir a proposta e dizer não · **Paleta:** manhã clara, terminal em luz dura de dia (primeira vez que a luz do porto entra no quadro por inteiro)

| # | Tempo | Narração / legenda | Imagem | Som |
|---|---|---|---|---|
| 1 | 0,0–3,0 | **Sábado. Nove da manhã.** | Davi na calçada, camisa limpa, boné na mão. Luz alta. | Pássaros, motor distante |
| 2 | 3,0–6,0 | **Davi acordou antes do alarme.** | Insert do celular na mesa de cabeceira marcando 5h40, quarto ainda escuro. | — |
| 3 | 6,0–9,5 | **Sandro desceu do carro com café para dois.** | Carro branco, motorista de camisa social, sorriso largo; plano médio de Davi recebendo o copo. | Porta, copo de papel |
| 4 | 9,5–12,5 | "Traz só o boné. É uma volta." | Sandro apontando o terminal com o copo na mão. | — |
| 5 | 12,5–16,5 | **A portaria era uma parede de vidro e papel.** | Travelling lateral lento: catracas, painel de crachás, mural de normas de segurança, câmeras. | Portaria, cancela |
| 6 | 16,5–20,5 | **Sandro falou com todo mundo pelo nome.** | Planos curtos encadeados: guarda, conferente, motorista. Cada um responde com o nome de Sandro. | Vozes sobrepostas, baixas |
| 7 | 20,5–24,0 | **Davi entendeu que aquilo era poder de verdade.** | Davi parado no meio do fluxo de pessoas que andam rápido; ele é o único parado. | Ruído industrial contínuo |
| 8 | 24,0–28,5 | "Chega carga que precisa de conferência rápida." | Interior do pátio: contêineres empilhados, empilhadeira passando ao fundo desfocada. | Diesel, alarme de ré |
| 9 | 28,5–32,0 | "Você abre, confere o lacre e me manda o número." | Insert da mão de Sandro desenhando no ar o gesto de abrir e apontar. | — |
| 10 | 32,0–35,0 | **"Duzentos reais por visita."** | Rosto de Davi, meio de perfil, olhando o contêiner. | Empilhadeira |
| 11 | 35,0–38,0 | **Davi perguntou o que tinha dentro.** | Ele vira para Sandro. Plano dos dois, enquadramento fechado. | — |
| 12 | 38,0–41,5 | "Se eu soubesse, não te trazia aqui." | Sandro rindo. Davi rindo. Os dois no sol. | Risadas |
| 13 | 41,5–45,0 | **Foi a primeira resposta que não respondeu nada.** | Insert: a lateral de um contêiner com número borrado de propósito. | — |
| 14 | 45,0–48,5 | **Na saída, ele parou.** | Davi parado na sombra da portaria, cancela abrindo. | Cancela |
| 15 | 48,5–51,5 | "Hoje não dá, Sandro." | Ele fala sem encarar. Sandro de mãos no bolso. | — |
| 16 | 51,5–55,0 | **Sandro deu de ombros e sorriu.** | Close no rosto de Sandro: nenhuma irritação, só afeto. | — |
| 17 | 55,0–58,0 | "Tranquilo, meu filho. A porta tá aberta." | Sandro acenando ao entrar no carro. Davi sozinho na calçada. | Porta, motor |
| 18 | 58,0–61,0 | **Ninguém cobrando nada.** | Volta à loja: Davi dobrando camisa na arara, luz quente, sorriso pequeno e triste. | Cabide |
| 19 | 61,0–64,0 | **E foi por isso que ele não esqueceu.** | Sobreposição suave: a tela do celular no vidro da vitrine. Drone grave entra. | — |
| 20 | 64,0–66,0 | — | **Cartela:** `FASE 3 — VANTAGEM` + canais | Corte seco |

**NARAÇÃO P/ TTS**
```
Sábado. Nove da manhã. Davi acordou antes do alarme. Sandro desceu do carro com café para dois. "Traz só o boné. É uma volta." A portaria era uma parede de vidro e papel. Sandro falou com todo mundo pelo nome. Guarda, conferente, motorista. Davi entendeu que aquilo era poder de verdade. "Chega carga que precisa de conferência rápida. Você abre, confere o lacre e me manda o número. Duzentos reais por visita." Davi perguntou o que tinha dentro. "Se eu soubesse, não te trazia aqui." Foi a primeira resposta que não respondeu nada. Na saída, ele parou. "Hoje não dá, Sandro." Sandro deu de ombros e sorriu. "Tranquilo, meu filho. A porta tá aberta." Ninguém cobrando nada. E foi por isso que ele não esqueceu.
```

---

# EPISÓDIO 6 — "A segunda chamada"
**Fase:** 3 — Vantagem (virada) · **Decisão:** ligar de volta · **Paleta:** loja e cozinha em luz de dia fechando para noite; a ligação é o primeiro quadro totalmente azul do episódio

| # | Tempo | Narração / legenda | Imagem | Som |
|---|---|---|---|---|
| 1 | 0,0–3,2 | **Na segunda, a loja avisou que ia reduzir.** | Cartaz na porta dos fundos, caneta marcando três nomes; mão de Davi no vidro. | Interior de loja, rádio baixo |
| 2 | 3,2–6,8 | **Cinco das dezessete vagas.** | Plano dele no caixa, cliente passando cartão; a fila anda. | Bip de maquininha |
| 3 | 6,8–10,2 | **Na terça, a consulta da mãe atrasou de novo.** | Envelope do posto de saúde sobre a mesa da cozinha; a mão dela abre. | — |
| 4 | 10,2–13,5 | **Três meses de fila para uma cirurgia de hérnia.** | Close do papel com a data carimbada; desfoca. | Papel |
| 5 | 13,5–17,0 | **Particular, o valor que ele não tinha.** | Davi de costas olhando a tela do celular com a calculadora aberta. | Toque de calculadora |
| 6 | 17,0–20,0 | **Ele fez a conta duas vezes.** | Insert da tela: dois cálculos, o mesmo resultado. | — |
| 7 | 20,0–23,5 | **Na quarta, lavou a camisa do sábado.** | Tanque da cozinha, sabão, água escorrendo; Davi esfregando a gola. | Água, sabão |
| 8 | 23,5–26,5 | **Ninguém entendeu por quê.** | Mãe na porta, pano no ombro, olhando sem perguntar. | — |
| 9 | 26,5–29,0 | **Ele decorou o número antes de salvar.** | Quarto escuro; ele com o telefone no joelho, digitando e apagando. | — |
| 10 | 29,0–32,0 | **Nunca tinha feito isso na vida.** | Insert da tela com o número marcado, a agenda fechada. | — |
| 11 | 32,0–35,0 | **Às nove e dez, Davi discou.** | O polegar desliza; o rosto dele iluminado de baixo. | DTMF |
| 12 | 35,0–38,0 | **Do outro lado, atenderam no segundo toque.** | Close do rosto; a luz da tela acende o quarto. | Toque de chamada curto |
| 13 | 38,0–41,5 | "Pensei que você ia ligar mais cedo." | Plano médio: ele sentado no chão do quarto, costas na cama, celular no ouvido. | — |
| 14 | 41,5–45,0 | **Não tinha vitória nenhuma naquela voz.** | Insert do queixo dele apertado, olhos no teto. | — |
| 15 | 45,0–48,0 | **Só a calma de quem estava certo.** | A janela com as luzes do porto; agora o porto está mais perto que nunca. | Drone grave |
| 16 | 48,0–51,0 | "Sábado. Leva só o documento." | Tela do celular, a mensagem escrita em uma linha. | Bip |
| 17 | 51,0–54,0 | **Davi desligou e ficou no chão.** | Ele escorrega até sentar no chão; a tela apaga; só resta a luz azul da janela. | Silêncio quase total |
| 18 | 54,0–56,5 | **A mãe chamou para jantar.** | Corredor visto do chão: a luz da cozinha entrando em faixa sob a porta. | Talheres ao longe |
| 19 | 56,5–59,0 | **Ele respondeu que já ia.** | Ele fica parado. Não se levanta ainda. | — |
| 20 | 59,0–62,5 | **E ali ele quis o dinheiro.** | Close final: os olhos dele abertos no escuro, o porto refletido neles. | Drone sobe e corta |
| 21 | 62,5–66,0 | **Ninguém obrigou. Foi ele.** | Preto com a cartela: `FASE 3 — VANTAGEM` + canais | Corte a zero |

**NARAÇÃO P/ TTS**
```
Na segunda, a loja avisou que ia reduzir. Cinco das dezessete vagas. Na terça, a consulta da mãe atrasou de novo. Três meses de fila para uma cirurgia de hérnia. Particular, o valor que ele não tinha. Ele fez a conta duas vezes. Na quarta, lavou a camisa do sábado. Ninguém entendeu por quê. Ele decorou o número antes de salvar. Nunca tinha feito isso na vida. Às nove e dez, Davi discou. Do outro lado, atenderam no segundo toque. "Pensei que você ia ligar mais cedo." Não tinha vitória nenhuma naquela voz. Só a calma de quem estava certo. "Sábado. Leva só o documento." Davi desligou e ficou no chão. A mãe chamou para jantar. Ele respondeu que já ia. E ali ele quis o dinheiro. Ninguém obrigou. Foi ele.
```

---

# EPISÓDIO 7 — "O lacre"
**Fase:** 4 — Dependência · **Decisão:** fazer o primeiro "favor" dentro do terminal · **Paleta:** amanhecer azul-petróleo, luz de sódio laranja no pátio; primeira aparição do porto em plano geral

| # | Tempo | Narração / legenda | Imagem | Som |
|---|---|---|---|---|
| 1 | 0,0–3,0 | **Sábado. Cinco e quarenta da manhã.** | Céu azul-escuro sobre o cais; Davi de moto, farol, respiração visível. | Moto, gaivotas |
| 2 | 3,0–6,0 | **O porto acordava antes da cidade.** | Plano geral: guindastes, contêineres empilhados, luzes de sódio acesas com o céu escuro. | Diesel de empilhadeira |
| 3 | 6,0–9,5 | **Cleber estava na portaria.** | Homem de colete laranja na catraca, olhando o próprio crachá; não olha para Davi. | Cancela |
| 4 | 9,5–13,5 | "Você é meu primo. Fica perto de mim e não fala." | Plano dos dois caminhando; Cleber com as mãos no bolso, ombros duros. | Passos em cascalho |
| 5 | 13,5–17,0 | **O pátio tinha barulho de ferro e cheiro de madeira.** | Travelling de um palete de madeira embalado, plástico transparente. | Empilhadeira, madeira |
| 6 | 17,0–20,5 | **Sandro apontou um número pintado.** | Mão de Sandro em primeiro plano; fora de foco, a lateral de um contêiner com número ilegível. | — |
| 7 | 20,5–24,5 | "Confere o lacre e me manda o número do novo." | Insert: a corrente e o lacre de plástico pendurados na porta. | Metal |
| 8 | 24,5–28,0 | **O lacre velho estava partido.** | Mãos de Davi abrindo a porta com cuidado; a fresta deixa sair luz. | Rangido de porta |
| 9 | 28,0–31,5 | **Ele trocou sem entender por que era tão fácil.** | Ele fecha, encaixa o novo, dá um puxão para testar. | Clique do lacre |
| 10 | 31,5–35,0 | **Uma mochila passou de mão em mão perto da porta.** | Ao fundo, desfocada e cortada pela borda do quadro: três figuras, um volume. Davi não vira. | Vozes ininteligíveis |
| 11 | 35,0–38,0 | **Davi não viu o que tinha dentro.** | Close só do rosto dele, olhos no chão, maxilar tenso. | — |
| 12 | 38,0–41,0 | **Foi a parte combinada.** | Sandro assina um papel na cabine de um caminhão. | Caneta |
| 13 | 41,0–44,5 | **No portão, um envelope pardo, fino.** | Mão entrega o envelope; Davi recebe com as duas mãos, sem jeito. | Papel |
| 14 | 44,5–48,0 | "Dois mil. Só hoje." | Estacionamento deserto; ele abre, conta as notas com o polegar. | Notas, vento |
| 15 | 48,0–51,5 | **Duas consultas. Três meses de aluguel.** | Sobreposição: o papel da cirurgia da mãe e o envelope na mesa dele. | — |
| 16 | 51,5–55,0 | **Uma vez só, ele pensou.** | Davi na moto, capacete na mão, parado. | Motor ligando |
| 17 | 55,0–58,5 | **Na saída, o motorista perguntou o nome dele.** | Janela do caminhão abaixa; mão para fora; Davi responde. | Caminhão |
| 18 | 58,5–62,5 | "É você? Falam tanto de você aqui dentro." | Close no rosto de Davi: ele sorri sem querer. É o que dói. | Motor morre; drone corta |
| 19 | 62,5–65,0 | — | **Cartela:** `FASE 4 — DEPENDÊNCIA` + canais | — |

**NARAÇÃO P/ TTS**
```
Sábado. Cinco e quarenta da manhã. O porto acordava antes da cidade. Cleber estava na portaria. "Você é meu primo. Fica perto de mim e não fala." O pátio tinha barulho de ferro e cheiro de madeira. Sandro apontou um número pintado. "Confere o lacre e me manda o número do novo." O lacre velho estava partido. Ele trocou sem entender por que era tão fácil. Uma mochila passou de mão em mão perto da porta. Davi não viu o que tinha dentro. Foi a parte combinada. No portão, um envelope pardo, fino. "Dois mil. Só hoje." Duas consultas. Três meses de aluguel. Uma vez só, ele pensou. Na saída, o motorista perguntou o nome dele. "É você? Falam tanto de você aqui dentro."
```

---

# EPISÓDIO 8 — "Dinheiro bom"
**Fase:** 4 — Dependência · **Decisão:** aceitar o envelope e mentir olhando nos olhos · **Paleta:** é o episódio mais claro da série — e é exatamente aí que o perigo mora

| # | Tempo | Narração / legenda | Imagem | Som |
|---|---|---|---|---|
| 1 | 0,0–3,0 | **Davi não gastou nada naquele dia.** | O envelope dentro da gaveta da mesa, em cima da caderneta de luz. | Gaveta |
| 2 | 3,0–6,0 | **Deixou lá dois dias, olhando.** | Ele na cadeira diante da mesa, sem tocar em nada; luz de manhã entrando. | Relógio |
| 3 | 6,0–9,5 | **Na quinta, pagou a consulta em particular.** | Balcão de clínica, cartão recusado, dinheiro contado sobre o balcão. | Impressora de recibo |
| 4 | 9,5–13,0 | **Na sexta, a cirurgia saiu em três semanas.** | Papel com data; a mão da mãe segurando o papel com as duas mãos. | — |
| 5 | 13,0–17,0 | **No corredor do posto, ela chorou.** | Plano de costas: mãe sentada no banco de plástico, ombros; Davi de pé ao lado, mãos nos bolsos. | Passos, porta |
| 6 | 17,0–20,5 | **Não era da doença. Era do alívio.** | Close no rosto dela, sem lágrima exagerada, só cansaço que sai. | — |
| 7 | 20,5–24,0 | **Em casa, a pergunta de sempre.** | Cozinha à noite, luz quente, a mesa posta. Ela senta, ele também. | Talheres |
| 8 | 24,0–27,0 | "De onde veio esse dinheiro?" | Ela pergunta sem acusação; as duas mãos na caneca. | — |
| 9 | 27,0–30,5 | **"Fechamento de meta. Ainda não caiu na conta."** | Davi responde olhando nos olhos dela. Ele treinou. | — |
| 10 | 30,5–34,0 | **Dessa vez, ele mentiu bem.** | Ela assente e volta a comer; ele também volta a comer. | Louça |
| 11 | 34,0–37,5 | **E ela acreditou porque queria acreditar.** | Insert do prato dos dois, o mesmo gesto de garfo. | — |
| 12 | 37,5–41,5 | **Mentir bem também é um trabalho.** | Davi na pia, lavando o prato, sozinho, a luz da cozinha agora fria. | Água |
| 13 | 41,5–45,0 | **No sábado, a mensagem acordou às seis.** | Tela no criado: "Sexta. Mesma hora." Luz do quarto ainda azul. | Bip |
| 14 | 45,0–48,0 | **Davi olhou sem responder.** | Ele senta na cama, telefone na mão, o polegar parado. | — |
| 15 | 48,0–51,0 | **E respondeu.** | Insert da digitação: duas letras. | Teclado |
| 16 | 51,0–54,0 | "Tá bom." — **Duas palavras.** | Ele apoia o celular no joelho e olha a janela. | — |
| 17 | 54,0–57,5 | **Foi a primeira vez que aceitou sem perguntar o quê.** | Plano geral do quarto: ele pequeno, a cidade grande lá fora. | Drone |
| 18 | 57,5–61,0 | **À noite, veio um número que ele nem salvou.** | Tela: "Foi fácil, né? Tem mais." | Bip final |
| 19 | 61,0–63,5 | — | **Cartela:** `FASE 4 — DEPENDÊNCIA` + canais | Corte |

**NARAÇÃO P/ TTS**
```
Davi não gastou nada naquele dia. Deixou lá dois dias, olhando. Na quinta, pagou a consulta em particular. Na sexta, a cirurgia saiu em três semanas. No corredor do posto, ela chorou. Não era da doença. Era do alívio. Em casa, a pergunta de sempre. "De onde veio esse dinheiro?" "Fechamento de meta. Ainda não caiu na conta." Dessa vez, ele mentiu bem. E ela acreditou porque queria acreditar. Mentir bem também é um trabalho. No sábado, a mensagem acordou às seis. "Sexta. Mesma hora." Davi olhou sem responder. E respondeu. "Tá bom." Duas palavras. Foi a primeira vez que aceitou sem perguntar o quê. À noite, veio um número que ele nem salvou. "Foi fácil, né? Tem mais."
```

---

# EPISÓDIO 9 — "Indicação de confiança"
**Fase:** 4 — Dependência (virada estrutural) · **Decisão:** indicar outra pessoa · **Paleta:** luz do dia na loja e no boteco da esquina; tudo parece normal — e é isso que é violento

| # | Tempo | Narração / legenda | Imagem | Som |
|---|---|---|---|---|
| 1 | 0,0–3,0 | **Depois de três sábados, Davi já entrava no pátio sem medo.** | Davi caminhando no terminal com o passo de quem trabalha ali; ninguém o aborda. | Ambiente de porto |
| 2 | 3,0–6,0 | **Aí Sandro pediu outra coisa.** | Cafeteria de esquina, dois copos; Sandro mexe no açúcar. | Colher |
| 3 | 6,0–9,5 | "Preciso de mais um. Alguém de confiança." | Close no rosto de Davi; ele entende que a palavra é a dele. | — |
| 4 | 9,5–13,0 | **"Você escolhe. Você responde por ele."** | Sandro empurra o guardanapo com um valor escrito. | Papel |
| 5 | 13,0–16,0 | **Quinhentos por indicação.** | Insert do guardanapo: "500". Davi não pega o papel. | — |
| 6 | 16,0–19,5 | **Davi pensou em Ruan, do caixa da loja.** | Loja: Ruan trocando moedas na frente do caixa, foto da filha no mural. | Moedas |
| 7 | 19,5–23,0 | **Ruan tinha dívida no cartão e uma filha de dois anos.** | Close da tela do celular de Ruan com o app do banco em vermelho. | — |
| 8 | 23,0–26,0 | **Ele marcou um café e explicou pouco.** | Mesmo boteco, agora dois copos de plástico; Davi falando baixo. | — |
| 9 | 26,0–29,5 | "É carga lícita. Você confere. Paga bem." | **A frase idêntica à que Davi ouviu no E5.** Reenquadramento espelhado do E5, mesma composição. | Colher |
| 10 | 29,5–33,0 | **Ruan perguntou o que ele tinha perguntado.** | Close no rosto de Ruan, a mesma desconfiança simpática. | — |
| 11 | 33,0–36,5 | **E Davi deu a mesma resposta que recebeu.** | Davi rindo, sem graça. Corte seco. | Risada curta |
| 12 | 36,5–40,0 | **Naquele segundo, ele entendeu o que tinha virado.** | Plano de Davi sozinho na mesa; a cadeira vazia de Ruan. | Zumbido |
| 13 | 40,0–43,5 | **Na semana seguinte, Sandro pediu mais um.** | Tela: "Só um menino. Ajeitado, discreto." | Bip |
| 14 | 43,5–46,5 | **Davi disse que não.** | Ele num banco de praça, telefone na orelha, negando com a cabeça. | — |
| 15 | 46,5–49,5 | **Sandro não insistiu.** | Silêncio do outro lado; ele ouve a respiração. | — |
| 16 | 49,5–52,5 | **Só falou o valor de novo.** | Tela: o número de antes, com um zero a mais. | — |
| 17 | 52,5–56,0 | **Téo tinha dezesseis anos e era irmão do Ruan.** | Téo na loja, uniforme grande demais, carregando caixa, sorrindo para o irmão. | Caixas |
| 18 | 56,0–59,5 | **Davi levou ele numa terça, de manhã.** | Os dois na calçada às 5h40; a mesma luz azul do E7. | Moto |
| 19 | 59,5–63,0 | **Na saída, o menino agradeceu com um abraço.** | Téo de boné novo, abraçando Davi no estacionamento. | — |
| 20 | 63,0–66,0 | **E perguntou quando voltava.** | Rosto de Davi por cima do ombro do menino. Corte seco. | Corte a zero |
| 21 | 66,0–68,0 | — | **Cartela:** `FASE 4 — DEPENDÊNCIA` + canais | — |

Este episódio tem 68 s: é o único em que a quebra de padrão é intencional, porque é o episódio em que Davi quebra o padrão da série. Se precisar de 60 s, corte as linhas 5, 7 e 15.

**NARAÇÃO P/ TTS**
```
Depois de três sábados, Davi já entrava no pátio sem medo. Aí Sandro pediu outra coisa. "Preciso de mais um. Alguém de confiança. Você escolhe. Você responde por ele." Quinhentos por indicação. Davi pensou em Ruan, do caixa da loja. Ruan tinha dívida no cartão e uma filha de dois anos. Ele marcou um café e explicou pouco. "É carga lícita. Você confere. Paga bem." Ruan perguntou o que ele tinha perguntado. E Davi deu a mesma resposta que recebeu. Naquele segundo, ele entendeu o que tinha virado. Na semana seguinte, Sandro pediu mais um. "Só um menino. Ajeitado, discreto." Davi disse que não. Sandro não insistiu. Só falou o valor de novo. Téo tinha dezesseis anos e era irmão do Ruan. Davi levou ele numa terça, de manhã. Na saída, o menino agradeceu com um abraço. E perguntou quando voltava.
```

---

# EPISÓDIO 10 — "O porto acordou"
**Fase:** 5 — Coerção · **Decisão:** ficar quando todo mundo some · **Paleta:** manhã cinza, luz de sirene azul cruzando os quadros; o porto nunca esteve tão frio

| # | Tempo | Narração / legenda | Imagem | Som |
|---|---|---|---|---|
| 1 | 0,0–3,0 | **Na terça seguinte, o terminal acordou diferente.** | Portão com veículos brancos parados em fila; ninguém andando. | Rádios de segurança |
| 2 | 3,0–6,5 | **Três carros na portaria, sem placa de empresa.** | Insert: agentes de colete, sem rosto, abrindo porta. | Portas, rádio |
| 3 | 6,5–10,0 | **Crachá recolhido. Nove afastados.** | Quadro de avisos sendo esvaziado; um crachá ficando para trás na parede. | Fita adesiva |
| 4 | 10,0–13,5 | **Cleber não atendeu o telefone o dia inteiro.** | Davi andando na calçada com o celular na orelha; o nome "CLEBER" na tela. | Toque que cai |
| 5 | 13,5–17,0 | **À noite, passou no grupo do bairro.** | Tela do celular com prints e áudios; dedos deslizando rápido. | Bip de áudio |
| 6 | 17,0–21,0 | **Operação. Dezesseis mandados. Um bloqueio de milhões.** | Notícia em rede social local, texto grande, nome de cidade; nada de rosto. | — |
| 7 | 21,0–24,0 | **Ninguém falou o nome de ninguém.** | Close no rosto de Davi lendo deitado, luz azul no teto. | — |
| 8 | 24,0–27,0 | **E todo mundo sabia qual era.** | Ele bloqueia a tela. Escuridão. | Corte de som |
| 9 | 27,0–30,5 | **Sandro ligou na quinta.** | Tela com "Sandro" — o nome salvo no E4 agora assusta. | Toque |
| 10 | 30,5–34,5 | "É a última. Depois você nunca mais me vê." | Plano espelhado ao do E4: mesma cama, mesma luz, a voz do outro lado mais mansa. | — |
| 11 | 34,5–38,0 | **Quarenta mil pra fechar a história dele.** | Insert: o número digitado num papel, a caligrafia de Davi copiando. | — |
| 12 | 38,0–41,0 | **Davi pediu prazo.** | Ele na cozinha, de madrugada, luz do fogão acesa sem ninguém cozinhando. | Geladeira |
| 13 | 41,0–45,0 | **Sandro respondeu com uma foto.** | Tela: Téo, de boné, na portaria do terminal, com um crachá de visitante. | Bip |
| 14 | 45,0–48,5 | "Cuida do menino, então vem." | Close na mandíbula de Davi; ele não respira direito por dois segundos. | Respiração |
| 15 | 48,5–52,5 | **Aí ele entendeu os três sábados.** | Montagem rápida e seca: o café, o pátio, o envelope — três planos, um segundo cada. | Drone |
| 16 | 52,5–56,0 | **Não era pagamento. Era fiador.** | Ele devolve o celular na mesa, tela para baixo. | — |
| 17 | 56,0–59,5 | **Na sexta, acordou às quatro.** | Quarto escuro; ele de pé, camisa do sábado lavada no braço. | — |
| 18 | 59,5–62,5 | **Pegou a chave da moto.** | Insert da mão fechando na chave sobre a mesa da entrada. | Chave |
| 19 | 62,5–66,0 | **E ficou com a mão na maçaneta.** | Plano longo: a porta, a luz da rua entrando embaixo dele. Ele não abre. | Silêncio |
| 20 | 66,0–68,0 | — | **Cartela:** `FASE 5 — COERÇÃO` + canais | Corte |

**NARAÇÃO P/ TTS**
```
Na terça seguinte, o terminal acordou diferente. Três carros na portaria, sem placa de empresa. Crachá recolhido. Nove afastados. Cleber não atendeu o telefone o dia inteiro. À noite, passou no grupo do bairro. Operação. Dezesseis mandados. Um bloqueio de milhões. Ninguém falou o nome de ninguém. E todo mundo sabia qual era. Sandro ligou na quinta. "É a última. Depois você nunca mais me vê." Quarenta mil pra fechar a história dele. Davi pediu prazo. Sandro respondeu com uma foto. "Cuida do menino, então vem." Aí ele entendeu os três sábados. Não era pagamento. Era fiador. Na sexta, acordou às quatro. Pegou a chave da moto. E ficou com a mão na maçaneta.
```

---

# EPISÓDIO 11 — "A mãe perguntou de novo"
**Fase:** Saída · **Decisão:** contar a verdade inteira · **Paleta:** volta à luz quente da cozinha — a primeira cena de verdade desde o E3. A música sai quase inteira

| # | Tempo | Narração / legenda | Imagem | Som |
|---|---|---|---|---|
| 1 | 0,0–3,0 | **Davi não foi.** | A chave sobre a mesa da entrada. Plano fixo, três segundos. | Silêncio de casa |
| 2 | 3,0–6,0 | **Deixou a chave e voltou pro quarto.** | Ele deitado de cara para o teto, botas ainda nos pés. | Molas da cama |
| 3 | 6,0–9,5 | **Às seis e meia, a mãe estava na cozinha.** | Ela acendendo o fogão; a luz quente volta a ser a fonte principal do quadro. | Fósforo, chama |
| 4 | 9,5–12,5 | **E fez a pergunta de sempre.** | Ela vira com o bule na mão. Não desconfiada. Só mãe. | Café sendo passado |
| 5 | 12,5–15,5 | "Tá tudo bem?" | Mesmo enquadramento do E2 e do E3, mesma mesa, mesma caneca. | — |
| 6 | 15,5–18,5 | **Davi sentou.** | Ele puxa a cadeira devagar. O tempo do plano é o tempo dele. | Cadeira no piso |
| 7 | 18,5–22,0 | **E contou.** | Plano médio dos dois; nenhuma imagem de flashback ainda. | Respiração |
| 8 | 22,0–26,0 | **Contou do sábado, do envelope, do número do contêiner.** | **Aqui entram os flashbacks, em cores dessaturadas, 0,8 s cada:** o café, a mão no lacre, o envelope. | Som dos flashbacks, seco |
| 9 | 26,0–29,5 | **Contou do Téo.** | Volta à cozinha; a mão dela para de segurar o bule. | — |
| 10 | 29,5–33,0 | **Ele não chorou. Ela também não.** | Dois planos alternados, curtos, sem música. | Geladeira |
| 11 | 33,0–36,5 | **A primeira pergunta dela não foi sobre dinheiro.** | Ela ainda com as mãos na caneca, olhando o piso antes de olhar ele. | — |
| 12 | 36,5–39,0 | **Foi sobre o menino.** | Close no rosto dela: nenhuma surpresa, só decisão. | — |
| 13 | 39,0–42,5 | **Ela ouviu inteira com as duas mãos na caneca.** | Insert das mãos dela, os dedos brancos de aperto. | — |
| 14 | 42,5–47,0 | "Você não fez isso sozinho. E não vai sair sozinho." | Ela olha para ele. Sem susto, sem bronca. Uma frase de comando. | Silêncio |
| 15 | 47,0–50,0 | **Ela pegou o telefone do filho.** | Ela estende a mão pela mesa; ele entrega. | — |
| 16 | 50,0–53,0 | **Tirou do armário o envelope de tudo.** | Papelada: exames, contas, protocolo do posto, data da cirurgia. | Papel |
| 17 | 53,0–56,5 | **E colocou na mesa, na ordem das datas.** | As mãos dos dois arrumando os papéis em fila. | — |
| 18 | 56,5–60,0 | **Às sete e vinte, os dois estavam na mesa.** | Plano geral da cozinha com as duas canecas e a papelada; luz da manhã entrando. | Pássaros |
| 19 | 60,0–63,5 | **O celular vibrou quatorze vezes.** | Tela com as notificações empilhadas; o celular tremendo na madeira da mesa. | Vibração, várias |
| 20 | 63,5–66,0 | **Davi olhou pra tela.** | Ele olha; a mãe não tira os olhos dele. | — |
| 21 | 66,0–69,0 | **E não respondeu nenhuma.** | Ele vira o celular para baixo. Corte para preto. | Corte de vibração |
| 22 | 69,0–71,0 | — | **Cartela:** `SAÍDA` + canais | — |

**NARAÇÃO P/ TTS**
```
Davi não foi. Deixou a chave e voltou pro quarto. Às seis e meia, a mãe estava na cozinha. E fez a pergunta de sempre. "Tá tudo bem?" Davi sentou. E contou. Contou do sábado, do envelope, do número do contêiner. Contou do Téo. Ele não chorou. Ela também não. A primeira pergunta dela não foi sobre dinheiro. Foi sobre o menino. Ela ouviu inteira, com as duas mãos na caneca. "Você não fez isso sozinho. E não vai sair sozinho." Ela pegou o telefone do filho. Tirou do armário o envelope de tudo. E colocou na mesa, na ordem das datas. Às sete e vinte, os dois estavam na mesa. O celular vibrou quatorze vezes. Davi olhou pra tela. E não respondeu nenhuma.
```

---

# EPISÓDIO 12 — "Anônimo"
**Fase:** Saída (resolução e custo) · **Decisão:** ligar e não desligar antes do fim · **Paleta:** dia cheio, luz dura, sem filtro; é o episódio visualmente mais "documental" da série

| # | Tempo | Narração / legenda | Imagem | Som |
|---|---|---|---|---|
| 1 | 0,0–3,0 | **Às oito, Davi estava na calçada.** | Ele sentado no meio-fio na frente de casa, telefone na mão, cidade acordando. | Tráfego leve |
| 2 | 3,0–7,0 | **Ligou para um número de três dígitos que não pede nome.** | Insert da tela: `181`. Os três algarismos grandes, sem contato salvo. | Toque |
| 3 | 7,0–11,0 | **Dois minutos. Ele não disse quem era.** | Plano de longe, ele de costas, telefone na orelha; ninguém atrás dele. | Voz atendente, abafada |
| 4 | 11,0–15,0 | **Falou o portão, a carga, o turno.** | Close na boca dele falando baixo, rápido, como quem tem medo de ser interrompido. | — |
| 5 | 15,0–18,5 | **E falou o nome do menino de dezesseis anos.** | Ele para um segundo antes de falar o nome. É a única hesitação do episódio. | — |
| 6 | 18,5–22,0 | **O segundo telefonema foi com a mãe ao lado.** | Cozinha; o viva-voz na mesa, a mão dela sobre a dele. | — |
| 7 | 22,0–25,5 | **Uma defensoria pública às nove da manhã.** | Corredor de instituição pública, senhas de papel, banco de plástico. | Numeração |
| 8 | 25,5–29,5 | **No mesmo dia, ele levou o Téo para a casa do avô.** | Estrada para Gaspar; mochila no ombro do menino; Davi devolvendo o capacete. | Motor |
| 9 | 29,5–33,0 | **Na semana seguinte, a loja o chamou de volta.** | Vitrine da loja com o nome dele na lista de recontratação. | — |
| 10 | 33,0–36,0 | **Sandro nunca mais ligou.** | Tela com o último contato, três semanas antes, sem resposta. | — |
| 11 | 36,0–39,5 | **Dois amigos do time pararam de responder.** | Grupo de WhatsApp com duas mensagens visualizadas e não respondidas. | Bip |
| 12 | 39,5–43,0 | **No bairro, ele virou "o que falou".** | Davi na calçada; dois homens de camisa de time viram o rosto ao lado, sem cumprimentar. | Vozes baixas |
| 13 | 43,0–46,5 | **Ouviu coisas na rua que ninguém devia ouvir aos vinte.** | Ele andando com a cabeça baixa, mãos no bolso, campo de terra ao fundo. | — |
| 14 | 46,5–50,0 | **E não perdeu nada que valia alguma coisa.** | Close: a caneca da mãe na mesa da cozinha, limpa, dois lugares postos. | — |
| 15 | 50,0–53,0 | **A cirurgia aconteceu.** | Ela no corredor, touca descartável, fazendo sinal de joia, com vergonha e riso. | — |
| 16 | 53,0–56,5 | **A carteira dele ficou vazia por seis meses.** | Geladeira com contas presas por imã; o calendário virando duas folhas. | Papel |
| 17 | 56,5–60,0 | **Ninguém devolve os sábados que ele perdeu.** | Ele na moto, sozinho, no mesmo horário azul do E7. | Motor |
| 18 | 60,0–63,5 | **Mas em abril, o irmão do Ruan voltou a estudar.** | Téo de mochila na porta de escola estadual, dia claro. | Sino de escola |
| 19 | 63,5–67,0 | **Denunciar não apaga o que aconteceu.** | Plano fixo da janela do quarto; as luzes do porto ao fundo, finalmente vistas de dia. | — |
| 20 | 67,0–70,0 | **Apaga o que ia acontecer.** | Corte para preto sobre a última frase. | Silêncio |
| 21 | 70,0–74,0 | — | **Cartela de dados (4 s, texto parado):** números da temporada | Tono grave |
| 22 | 74,0–76,0 | — | **Cartela final:** `SAÍDA · 181 · Comunica PF · CVV 188` + `Temporada 2: "Meu irmão quer falar com você."` | Corte |

**NARAÇÃO P/ TTS**
```
Às oito, Davi estava na calçada. Ligou para um número de três dígitos que não pede nome. Dois minutos. Ele não disse quem era. Falou o portão, a carga, o turno. E falou o nome do menino de dezesseis anos. O segundo telefonema foi com a mãe ao lado. Uma defensoria pública às nove da manhã. No mesmo dia, ele levou o Téo para a casa do avô. Na semana seguinte, a loja o chamou de volta. Sandro nunca mais ligou. Dois amigos do time pararam de responder. No bairro, ele virou "o que falou". Ouviu coisas na rua que ninguém devia ouvir aos vinte. E não perdeu nada que valia alguma coisa. A cirurgia aconteceu. A carteira dele ficou vazia por seis meses. Ninguém devolve os sábados que ele perdeu. Mas em abril, o irmão do Ruan voltou a estudar. Denunciar não apaga o que aconteceu. Apaga o que ia acontecer.
```

## Cartela de dados do final da temporada (texto parado, 4 s)

```
RECEITA FEDERAL APREENDEU 23,7 t DE COCAÍNA
EM ÁREAS PORTUÁRIAS EM 2022 E 14,8 t EM 2023

EM 2025, MAIS DE 2,3 t RETIDAS SÓ NOS PORTOS
DO PARANÁ E DE SANTA CATARINA

EM MAIO DE 2026, A PF PRENDEU 18 PESSOAS E
BLOQUEOU ATÉ R$ 646 MI DE UM GRUPO QUE USAVA
OS PORTOS DE NAVEGANTES, ITAPOÁ E IMBITUBA

VOCÊ NÃO PRECISA DIZER SEU NOME
DISQUE DENÚNCIA 181 · COMUNICA PF (gov.br/pf) · CVV 188
```

## Notas de continuidade entre episódios

- **A mesma camisa.** A camisa de linho branco do figurino de Davi é a do E1. Ela aparece lavada em E6, usada em E7, E9 e E10. Em E11 ele está de camiseta em casa. Não invente roupa nova fora do terminal.
- **A tatuagem no braço direito** é o marcador de identidade mais forte do personagem: toda vez que a mão de Davi entra em close (celular, lacre, envelope, chave), ela precisa estar no quadro.
- **Os três enquadramentos repetidos da cozinha** (E2, E3, E8, E11) devem ser literalmente o mesmo ângulo. É o refrão visual, e o E11 só funciona se for a mesma mesa com as mesmas canecas.
- **A frase-espelho do E5 e do E9** ("É carga lícita. Você confere. Paga bem.") deve ser reencenada com a mesma composição de quadro e a mesma distância de câmera, agora com Ruan no lugar de Davi. É a espinha moral da temporada inteira e vale mais que qualquer discurso.
- **Sandro nunca aparece sem estar sendo gentil.** Em todos os planos dele, alguém sorri para ele antes de ele falar.
- **O porto entra em plano geral uma única vez por episódio, no máximo**, até o E12, onde ele aparece de dia — que é a primeira vez que a cidade é vista inteira, sem o azul.

| Ep | Título | Caracteres de narração | Áudio estimado | Com cartelas | Clipes a gerar |
|---|---|---|---|---|---|
| E4 | Quem liga | 681 | 54,5 s | 58,5 s | 20 |
| E5 | Sem compromisso | 710 | 56,8 s | 60,8 s | 20 |
| E6 | A segunda chamada | 708 | 56,6 s | 60,6 s | 21 |
| E7 | O lacre | 668 | 53,4 s | 57,4 s | 19 |
| E8 | Dinheiro bom | 673 | 53,8 s | 57,8 s | 19 |
| E9 | Indicação de confiança | 799 | 63,9 s | 67,9 s | 21 |
| E10 | O porto acordou | 661 | 52,9 s | 56,9 s | 20 |
| E11 | A mãe perguntou de novo | 655 | 52,4 s | 56,4 s | 22 |
| E12 | Anônimo | 805 | 64,4 s | 68,4 s | 22 |

Estimativa de áudio a 12,5 caracteres/segundo, que é a taxa medida nos três episódios originais e confirmada na audição das vozes candidatas. Total da temporada: **6.360 caracteres de narração e 184 clipes**, dos quais cerca de 60 são inserts de objeto sem personagem e podem ir para o modelo mais barato. Se a meta for travar tudo entre 60 e 62 s, os episódios que pedem acréscimo são E7, E10 e E11 — adicionar duas frases de 8 a 10 palavras em cada um.
