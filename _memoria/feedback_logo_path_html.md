---
name: feedback-logo-path-html
description: Caminho correto para o logo-branco.png nos HTMLs de carrossel — 5 níveis acima da pasta instagram/
metadata:
  type: feedback
---

O logo está em `marca/logos/logo-branco.png` na raiz do projeto.

Os HTMLs ficam em `conteudo/carrosseis/[mes]/[dia]/instagram/slide-XX.html` — 5 níveis abaixo da raiz.

**Caminho correto:** `../../../../../marca/logos/logo-branco.png`

**Caminho errado (bug antigo):** `../../../../marca/logos/logo-branco.png` — resolve para `conteudo/marca/logos/` que não existe.

**Why:** Bug detectado quando o logo não apareceu nos slides renderizados. Verificar logo no slide-01 antes de renderizar os demais.

**How to apply:** Sempre usar 5 `../` para o logo em HTMLs dentro de `instagram/`. Verificar logo no slide-01 antes de renderizar os demais.
