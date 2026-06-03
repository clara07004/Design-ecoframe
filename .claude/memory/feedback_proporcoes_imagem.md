---
name: feedback-proporcoes-imagem
description: Proporções de imagem por tipo de slide e relação com o canvas 1080×1350.
metadata:
  type: feedback
---

Proporção da imagem gerada por tipo de slide.

**Why:** imagem na proporção errada distorce ou corta mal no canvas do slide.

**How to apply:**
- **Capa** = `square` (1024×1024)
- **Slides internos** = `portrait` (1024×1536)

O canvas do slide renderizado é **1080×1350** (4:5). A imagem `portrait` 1024×1536 (2:3) é mais
alta que o canvas, então `object-fit:cover` corta topo/base — comportamento esperado, a foto
preenche sem deformar. Posicionar via `object-position` quando o assunto não estiver centrado.

Nunca esticar (`object-fit:fill`) nem deixar barra vazia. Ver [[feedback-carousel-design-aprovado]].
</content>
