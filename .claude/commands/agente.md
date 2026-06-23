---
name: agente
description: >
  Convoca o agente de design da Ecoframe para direção criativa, revisão de carrossel/post,
  decisão de layout, escolha de ângulo visual, direção de arte ou qualquer tarefa que envolva
  identidade visual e produção de conteúdo da marca.
---

# /agente — Designer Ecoframe

Invoque imediatamente o agente `designer-ecoframe` com o pedido do usuário.

Use o Agent tool com `subagent_type: "designer-ecoframe"` e passe como prompt:
- O que o usuário pediu (verbatim ou parafraseado com contexto completo)
- O contexto relevante da conversa atual (arquivos abertos, decisões já tomadas, briefing em andamento)
- Qualquer arquivo ou dado que o designer precise consultar para responder

O agente tem acesso a todas as ferramentas e ao `marca/DESIGN.md`, `_testes/`, `_contexto/` e `produtos/`. Não resuma nem filtre o pedido — passe tudo que for relevante para que ele tome a melhor decisão criativa.

Após receber a resposta do agente, apresente-a diretamente ao usuário sem adicionar camadas de interpretação.
