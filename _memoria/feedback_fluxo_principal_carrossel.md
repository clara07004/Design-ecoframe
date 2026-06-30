---
name: feedback-fluxo-principal-carrossel
description: "Sequência confirmada como fluxo principal de produção de carrossel — 5 comandos em ordem, com imagens geradas para todos os slides antes de entrar no carrossel-unity"
metadata:
  type: feedback
---

Este é o fluxo principal confirmado pela Clara para produção de carrossel. Sempre seguir essa sequência, nessa ordem. Começa no BRIEFING, não nos hooks.

```
/briefing-unity
    ↓ [aprovado]
/gerador-de-prompts-de-imagem
    ↓ [prompts aprovados]
/gpt-image2-unity
    ↓ [imagens aprovadas]
/carrossel-unity
    ↓ [slides aprovados]
/legenda-para-carrossel
```

**Detalhes de execução:**

- `/gerador-de-prompts-de-imagem`: gerar prompts para TODOS os slides que receberão foto — capa + todos os slides de critério/conteúdo. Não apenas a capa.
- `/gpt-image2-unity`: gerar TODAS as imagens antes de entrar no carrossel-unity. Capa e slides internos = `portrait` (1024×1536) — todo o feed Instagram usa portrait. Ver [[feedback-proporcoes-imagem]].
- `/carrossel-unity`: entrar já com todas as imagens geradas e aprovadas. A skill recebe as imagens prontas e monta os HTMLs + renderiza.
- `/legenda-para-carrossel`: sempre ao final, nunca improvisar manualmente.

**NÃO usar** o fluxo rápido (`/carrossel-unity` faz tudo) nem `/hooks-para-carrossel` como ponto de partida — o `/hooks-para-carrossel` é auxiliar opcional, só quando ela quiser explorar capas. Fluxo rápido só sob pedido ou tarefa pontual.

**Why:** a geração de imagem para todos os slides antes de entrar no carrossel evita interrupções no fluxo de produção e garante aprovação visual completa antes da montagem dos slides. A Clara prefere controle total — quando as imagens são geradas dentro do carrossel (fluxo rápido), o usuário não tem controle granular sobre cada slide.

**How to apply:** sempre que a tarefa for produzir um carrossel, propor essa sequência. Se o usuário quiser pular etapas, ele indica — não assumir atalho por padrão.

Relacionado: [[feedback-carousel-design-aprovado]], [[feedback-proporcoes-imagem]]
