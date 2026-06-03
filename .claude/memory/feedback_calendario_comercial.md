---
name: feedback-calendario-comercial
description: Regras do calendário comercial — 3 entregas obrigatórias e pesquisa que vai além da cultural.
metadata:
  type: feedback
---

Ao rodar `/calendario-comercial` para um mês (ou período fechado), gerar **sempre 3 arquivos**
em `conteudo/calendarios/[periodo]/`.

**Why:** o calendário alimenta os briefings posteriores; sem os 3 artefatos o histórico de
aprovação e a visão do mês se perdem.

**How to apply:**
1. `calendario-detalhado.md` — post a post, numerado, com tema/formato/janela/status
2. `_aprovado.md` — memória da aprovação: tema narrativo, mix, apagões, picos, ajustes, o que evitar
3. `dashboard.html` — grid visual do mês, derivado do detalhado, via `templates/dashboard-calendario.html`
   (identidade da marca, canvas 1920×1080)

O dashboard **não é opcional** — entrega obrigatória junto com o calendário, mesmo sem pedido
explícito. Após gerar o HTML, perguntar se renderiza o PNG via Playwright (esse passo é opcional).

**Pesquisa de tendências — a cultural padrão não basta para a Ecoframe.** Sempre adicionar:
- **X (Twitter)** — debate técnico de arquitetos/engenheiros em tempo real: Steel Frame, Drywall,
  eficiência energética, NBR 15575, alto padrão. `WebSearch` com queries tipo
  `"arquitetura X.com [mês] [ano]"`, `"NBR 15575 X discussão"`, `"esquadrias PVC X arquiteto"`.
- Instagram de referência (`@ecophon_brasil`, arquitetos especificadores, construtoras Steel Frame)
- LinkedIn de arquitetura · mídia setorial (Galeria da Arquitetura, ArchDaily Brasil, PINI)

Cruzar o que pega no X com o calendário comercial — janela quente surge de sinal de conversa,
não só de evento agendado. Ver [[feedback-consulta-produtos-obrigatoria]].
</content>
