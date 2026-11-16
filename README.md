# A História do Davi — série documental animada (1 minuto por episódio)

Repositório público do projeto: **roteiros, bíblia visual, pipeline de produção, mídia gerada e memória de decisões**. Ele existe para que qualquer sessão de IA (ou qualquer pessoa) clone, leia dois arquivos e continue a produção exatamente de onde parou, com a mesma voz, o mesmo visual e o mesmo custo.

> Comece por **[INTELIGENCIA.md](INTELIGENCIA.md)** e depois por **[CONTINUA_AQUI.md](CONTINUA_AQUI.md)**. Estão escritos para o agente, não para o humano curioso.

```bash
git clone https://github.com/trentomotta7-hub/historia-do-davi
```

O clone traz tudo o que é preciso para retomar a produção em outra sessão, inclusive a mídia já gerada. A pipeline foi executada a partir de um clone limpo e reproduz os tempos, blocos e legendas do EP04 sem ajuste nenhum.

## Estado da série

| Ep | Título | Fase da história | Estado | Arquivo |
|---|---|---|---|---|
| E1 | (produção original do autor) | 1 — Aproximação | entregue, serve de referência de estilo | `media/final/EP01_original.mp4` |
| E2 | (produção original do autor) | 1 — Aproximação | entregue | `media/final/EP02_original.mp4` |
| E3 | (produção original do autor) | 1 → 2 | entregue; é o episódio mais bem resolvido, use como gabarito | `media/final/EP03_original.mp4` |
| **E4** | **"Quem liga"** | **2 — Vínculo** | **produzido nesta pipeline, 61,9 s, −14 LUFS** | `media/final/EP04_quem_liga.mp4` |
| E4 | trecho de aprovação de visual | 2 | material de teste aprovado | `media/final/EP04_trecho_aprovacao.mp4` |
| E5–E12 | roteirizados, com shot list e narração pronta | 3 → Saída | aguardando produção | `docs/03_roteiros_E4_a_E12.md` |

A sinopse do arco, os números reais que o sustentam e as fontes estão em `docs/02` e `docs/08`.

## Mapa do repositório

```
INTELIGENCIA.md        ← fonte única de verdade: voz, escrita, visual, legenda, áudio, custo
CONTINUA_AQUI.md       ← protocolo de retomada em sessão nova, na ordem
docs/
  01_analise_e_guia_de_estilo.md   análise medida dos 3 vídeos originais (ritmo, pausas, legendas)
  02_arco_da_temporada_E4_a_E12.md arco fundamentado, 9 episódios
  03_roteiros_E4_a_E12.md          roteiro cena a cena + narração literal para TTS
  04_plano_de_producao.md          referências, prompts, orçamento
  05_estrategia_de_custo.md        três rotas; a escolhida é a econômica
  06_ficha_de_producao_EP04.md     números reais do episódio produzido
  07_sincronia_e_correcoes.md      o defeito relatado pelo autor, causa e correção
  08_fontes_pesquisa.md            URLs e dados citados
pipeline/              código executável, já testado contra mídia real
  extrair_narracoes.py   roteiro → dados/narracoes.json (frases, estilo, locação)
  medir_frases.py        áudio → tempo real de cada frase + áudio retemporizado
  planejar_blocos.py     tempos → janelas de clipe (a correção da sincronia)
  gerar_legendas.py      tempos → ASS com cue terminando no fim da fala
  montar_episodio_v2.sh  clipes nas janelas reais + mix + loudnorm + legendas
  montar_ep04.sh, retimed_e_legendas.py   v1, preservada por honestidade histórica
prompts/               prompts exatos de geração (imagem, vídeo, voz, música, SFX)
dados/                 JSON intermediários versionados: narração, tempos, blocos, plano
media/
  final/               episódios entregues (E1–E4)
  referencias/         folhas de identidade e locações (redimensionadas, 810 px)
  audios/              narração crua e retemporizada do E4, cama musical, vibração, amostras de voz
  conferencia/         folhas de quadros usadas na aprovação
```

## Como rodar

Dependências: `ffmpeg ≥ 6` (filtros usados: `loudnorm`, `acompressor`, `sidechaincompress`, `ass`, `tpad`), Python 3 com stdlib apenas. A geração de mídia em si (voz, imagem, vídeo, música) é feita pelas ferramentas de geração do ambiente Manus com os prompts literalmente copiados de `prompts/prompts_geracao.json` — o repositório guarda os prompts e a matemática, não as chaves de API.

Para remontar um episódio já gerado:

```bash
python3 pipeline/extrair_narracoes.py
python3 pipeline/medir_frases.py EP05 EP05/narracao_ep05.wav
python3 pipeline/planejar_blocos.py EP05     # manda gerar um clipe por bloco, com a duração pedida
python3 pipeline/gerar_legendas.py EP05 "FASE 3 — VANTAGEM"
bash pipeline/montar_episodio_v2.sh EP05
```

## Convenções inegociáveis

- Vertical 1080×1920, 24 fps, H.264 CRF 18, AAC 48 kHz, −14 LUFS, pico abaixo de −1,5 dBTP.
- Narração **sempre** com `pt-br-storyteller-5`, uma chamada por episódio, texto verbatim do roteiro.
- Áudio dos clipes gerados **desligado**: som é voz + cama com ducking + vibração de celular.
- Legenda só existe enquanto existe fala; citação em peso regular, narração em bold.
- Cartela de fase no fim e canais de ajuda sobre preto (`181`, `gov.br/pf`, `CVV 188`).
- Nenhum contêiner legível, nenhuma placa legível, nenhuma marca real, nenhum nome real de investigado.

## Licença e uso

Roteiros, vídeos, imagens e áudio deste repositório são obra encomendada pelo mantenedor do projeto e **não são livres para reutilização comercial**. O código da pipeline (`pipeline/`) é fornecido sob MIT para que a técnica possa ser estudada e adaptada. A série trata de aliciamento para tráfico de drogas com intenção preventiva: os episódios terminam com canais reais de denúncia e apoio.
