# Manual de Uso — Ecoframe Content OS

Documentação completa do sistema de produção de conteúdo.

---

## Por onde começar

| Situação | Vá para |
|---|---|
| Nunca usei esse sistema antes | [00 — Visão Geral](00-visao-geral.md) |
| Quero entender o que cada arquivo faz | [01 — Estrutura do Repositório](01-estrutura-do-repositorio.md) |
| Preciso configurar as credenciais e o contexto | [02 — Configuração Inicial](02-configuracao-inicial.md) |
| Quero produzir conteúdo agora | [03 — Fluxo Completo](03-fluxo-completo.md) |
| Quero saber o que cada skill faz | [04 — Referência de Skills](04-referencia-de-skills.md) |
| Encontrei um erro | [05 — Resolução de Problemas](05-resolucao-de-problemas.md) |

---

## Os 5 arquivos do manual

### [00 — Visão Geral](00-visao-geral.md)
O que é o CCOS, como o sistema funciona, a diferença entre skills e motores, por que existem checkpoints de aprovação, o que o sistema produz e quais os pré-requisitos.

### [01 — Estrutura do Repositório](01-estrutura-do-repositorio.md)
Cada pasta, arquivo e skill explicados individualmente. Inclui o mapa completo de arquivos e a função de cada um.

### [02 — Configuração Inicial](02-configuracao-inicial.md)
Passo a passo completo para deixar o sistema pronto: instalação de dependências, configuração de credenciais de API, preenchimento dos arquivos de contexto e checklist de verificação.

### [03 — Fluxo Completo](03-fluxo-completo.md)
Como usar o sistema para gerar conteúdo do zero ao post pronto. Cobre o fluxo completo (calendário → briefing → produção → publicação) e os atalhos para entrar no meio do fluxo.

### [04 — Referência de Skills](04-referencia-de-skills.md)
Descrição detalhada de cada skill: para que serve, quando usar, o que precisa como input, o que entrega como output, e tabelas de referência rápida.

### [05 — Resolução de Problemas](05-resolucao-de-problemas.md)
Erros comuns e soluções: API key não encontrada, Playwright não instalado, DESIGN.md não configurado, token da Meta expirado, e perguntas frequentes.

---

## Fluxo resumido em 4 passos

```
1. /calendario-comercial   →  mapa estratégico do mês
        ↓ aprova
2. /briefing-unity         →  briefing de um post específico
        ↓ aprova
3. /carrossel-unity        →  carrossel completo (slides + imagens + PNGs)
   /estatico-unity         →  post estático (foto IA + layout + PNG)
   /roteiro-unity          →  roteiro de vídeo
        ↓ aprova
4. /publicar-social-unity  →  publica no Instagram/TikTok/LinkedIn
```

**Aprovação humana obrigatória em cada etapa — nada avança sem sua confirmação.**

---

## Onde está cada coisa

| O que você procura | Onde está |
|---|---|
| Contexto da empresa | `_contexto/empresa.md` |
| Tom de voz da marca | `_contexto/preferencias.md` |
| Estratégia e prioridades | `_contexto/estrategia.md` |
| Identidade visual | `marca/DESIGN.md` |
| API key OpenAI | `credentials/openai_key.txt` |
| Token Meta (Instagram) | `credentials/meta.txt` |
| Posts gerados | `conteudo/` |
| Histórico aprovado | `conteudo/[tipo]/[tema]/_aprovado.md` |
