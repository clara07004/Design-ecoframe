---
name: validar-overflow-antes-de-publicar
description: sempre rodar validar-overflow.js (não só validar-dimensao) antes de publicar carrossel/estático — texto cortado no canto já vazou em produção
metadata:
  type: feedback
---

Antes de publicar qualquer carrossel ou post estático, rodar AS DUAS validações: `validar-dimensao.py` (tamanho do canvas) **e** `validar-overflow.js` (texto que sangra para fora do canvas). Ambas em `.claude/skills/publicar-social-unity/`. Exit 1 em qualquer uma bloqueia a publicação.

**Why:** a Clara reportou que conteúdo cortado no canto inferior direito "já aconteceu em outros conteúdos" — no carrossel de 05/06 (steel-frame-compatibilidade) a spec bar do slide 5 ("Vento 1.820 Pa") transbordava 28px à direita e foi publicada assim. A `validar-dimensao.py` passou porque o canvas continuava 1080×1350; ela não enxerga texto vazando dentro do canvas. A conferência visual também falhou — corte de poucos px no canto passa batido no olho.

**How to apply:** causa-raiz recorrente = barra horizontal (spec bar/rodapé) com `display:flex` + `white-space:nowrap` cuja soma (textos + gaps + padding) passa de 1080px e o último item é cortado. Padrão seguro: `justify-content:space-between` + `flex-wrap:nowrap` + `overflow:hidden`, padding lateral ≤56px, `letter-spacing` ≤0.04em em uppercase, ~4 itens curtos no máximo. Depois de renderizar, SEMPRE confirmar com `validar-overflow.js` — nunca confiar só no olho.
