---
name: feedback-calendario-entregas-obrigatorias
description: "Todo calendário de novo mês gera 3 arquivos obrigatórios — calendario-detalhado.md, _aprovado.md e dashboard.html visual. O dashboard nunca é opcional."
metadata:
  type: feedback
---

Sempre que rodar `/calendario-comercial` para um mês (ou qualquer período fechado), gerar dentro de `conteudo/calendarios/[periodo]/` os TRÊS arquivos:

1. **`calendario-detalhado.md`** — post a post, numerado, com data/dia/tipo/formato/tema/status. Alimenta os `/briefing-unity` posteriores. Marcar ⚠️ em apagões (com horário-limite) e 🏆 em picos.
2. **`_aprovado.md`** — memória da aprovação: tema narrativo, mix, ajustes feitos, apagões confirmados, picos, o que evitar.
3. **`dashboard.html`** — grid visual derivado direto do `calendario-detalhado.md`, usando o template `templates/dashboard-calendario.html`. Identidade visual da marca (Poppins + Montserrat, Azul `#4A61A0`, off-white texturizado), canvas 1920×1080 landscape.

Após gerar o HTML do dashboard, perguntar:
> "Dashboard HTML pronto em [caminho]/dashboard.html. Quer que eu renderize o PNG agora via Playwright?"

O `dashboard.png` só é gerado após confirmação explícita.

**Why:** A Clara pediu que isso virasse regra do repositório e do agente (em 27/05/2026) porque a versão visual do calendário é o que dá leitura imediata do mês — sem ele, o calendário fica só em texto e perde força de planejamento. Os 3 arquivos juntos fecham o ciclo: visão (dashboard), execução (detalhado) e governança (aprovado).

**How to apply:** Vale para qualquer pedido tipo "monta calendário de [mês]", "calendário comercial de [período]", "planejamento de [mês]". Nunca entregar só o resumo da skill — sempre materializar os 3 arquivos. Se faltar algum, é entrega incompleta.

Relacionado: [[feedback-calendario-comercial]]
