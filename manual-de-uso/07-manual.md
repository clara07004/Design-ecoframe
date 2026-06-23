# Manual do Burro — Fluxo Completo de Produção

Duas rotinas. Uma por mês, uma por dia de publicação.

---

## ROTINA 1 — Uma vez por mês: Calendário Comercial

O calendário define o que vai ser postado no mês inteiro. Roda uma vez e serve de base para todos os dias.

### Passo 1 — Abrir o Claude Code nesse projeto

Abrir o Claude Code com o workspace `Design-ecoframe`.

### Passo 2 — Pedir o calendário

Digite:

```
/calendario-comercial
```

O sistema vai perguntar o período (ex.: julho 2026) e montar o calendário completo.

### Passo 3 — Revisar e aprovar

O Claude vai entregar:

- **Lista de posts** — tema, formato (carrossel, reels, estático), dia da semana
- **Justificativa estratégica** de cada escolha

Leia com calma. Você pode pedir ajustes antes de aprovar — ex.: "troca o post do dia 10 por algo sobre Steel Frame" ou "tira o post do dia 25, feriado".

Quando estiver satisfeita, diga: `aprovado` ou `pode gerar`.

### Passo 4 — Aguardar os 3 entregáveis obrigatórios

O sistema gera automaticamente dentro de `conteudo/calendarios/[periodo]/`:

1. `calendario-detalhado.md` — lista completa, post por post, com tema, formato e janela de publicação
2. `_aprovado.md` — registro do que foi aprovado (não apagar — serve de referência futura)
3. `dashboard.html` — grade visual do mês inteiro

Se quiser ver o dashboard renderizado em PNG, diga "renderiza o dashboard". Se não precisar, pode pular.

### Pronto. Calendário do mês feito.

Não precisa rodar de novo até o próximo mês.

---

## ROTINA 2 — A cada dia de publicação: Do Briefing ao Story

Essa é a rotina de produção do dia. Roda um conteúdo por vez.

**Duração estimada:** 30–60 minutos por carrossel, dependendo de quantas revisões.

---

### Etapa 1 — Briefing (5 min)

Digite:

```
/briefing-unity
```

O Claude vai perguntar:

- Qual post do calendário você quer produzir hoje (ex.: "dia 17 — linhas de PVC por vão")
- Confirmar o formato (se for carrossel, já vai direto — não precisa confirmar)

Ele vai gerar um briefing completo com:
- Objetivo do post
- Mensagem central
- Avatar (para quem é)
- Referências de tom e visual

**Leia e aprove.** Se algo não faz sentido, corrija antes de avançar. Esse é o documento-guia do conteúdo inteiro.

---

### Etapa 2 — Prompts de Imagem (5–10 min)

```
/gerador-de-prompts-de-imagem
```

O Claude vai criar prompts de IA para:
- A imagem da capa do carrossel
- As imagens de fundo de cada slide

Revise se os prompts fazem sentido visualmente com o tema. Você pode pedir ajuste — ex.: "capa mais sombria" ou "foto mais aberta, mostrando a fachada inteira".

Aprove os prompts.

---

### Etapa 3 — Geração de Imagens (5–15 min)

```
/gpt-image2-unity
```

O Claude vai rodar o script de geração e entregar as imagens.

Se alguma imagem ficou fora do que você esperava, diga qual e peça nova versão — ex.: "a imagem do slide 3 ficou muito escura, gera de novo".

Quando as imagens estiverem aprovadas, siga.

> **Dica:** se tiver fotos reais de obra disponíveis no Drive, diga "usa as fotos do Drive" antes dessa etapa. Imagem real é sempre melhor que IA.

---

### Etapa 4 — Carrossel: Texto + HTML + PNG (10–20 min)

```
/carrossel-unity
```

O Claude vai montar todos os slides com:
- Texto de cada slide (título, corpo, CTA)
- HTML estilizado com a identidade visual da Ecoframe
- PNG renderizado pronto para upload

Revise slide por slide. Itens para checar:
- Texto está claro e objetivo?
- Logo aparece corretamente?
- Nenhum texto está cortado?
- CTA do último slide está claro?

Se precisar ajustar um slide, indique qual e o que mudar — ex.: "slide 4, simplifica o texto" ou "slide 6, o título ficou grande demais".

Aprove o carrossel.

---

### Etapa 5 — Legenda (5 min)

```
/legenda-para-carrossel
```

O Claude vai escrever a legenda completa do Instagram:
- Primeira linha (aparece no feed antes de deslizar)
- Corpo da legenda (aprofunda sem repetir os slides)
- CTA orientado para salvar o post

Revise e aprove. Pequenos ajustes de tom são normais aqui.

---

### Etapa 6 — Publicação no Instagram (5 min)

```
/publicar-social-unity
```

O Claude vai mostrar exatamente o que vai publicar (imagens + legenda) e pedir confirmação explícita antes de qualquer coisa.

**O sistema nunca publica automaticamente — sempre pede aprovação.**

Quando confirmar, ele vai:
1. Fazer upload das imagens no imgbb (hospedagem temporária)
2. Enviar o carrossel para o Instagram via Meta Graph API
3. Confirmar que o post foi publicado com o link direto

---

### Etapa 7 — Story (manual, fora do sistema por enquanto)

Hoje o story é feito manualmente. O fluxo recomendado:

1. Pegar o primeiro slide do carrossel (PNG já está na pasta do conteúdo)
2. Adicionar sticker de enquete, contagem ou link para o perfil
3. Publicar no Instagram Stories diretamente pelo celular ou pelo Creator Studio

> O sistema de publicação automática de stories está previsto para V2.

---

## Resumo rápido (cola no Post-it)

**Uma vez por mês:**
```
/calendario-comercial → revisar → aprovar
```

**A cada post:**
```
/briefing-unity
/gerador-de-prompts-de-imagem
/gpt-image2-unity
/carrossel-unity
/legenda-para-carrossel
/publicar-social-unity
```
Story → manual no celular.

---

## Se algo der errado

| Problema | O que fazer |
|---|---|
| Imagem não gerou | Peça de novo: "gera de novo a imagem do slide X" |
| Erro de token Meta | Checar `credentials/meta_token_expira_em.txt` — pode ter expirado |
| Texto cortado no slide | Pedir versão mais curta do texto daquele slide |
| Post publicou errado | Deletar manualmente no Instagram e rodar `/publicar-social-unity` de novo |
| Não sabe em que passo está | Perguntar "em que etapa estamos?" — o Claude retoma de onde parou |
