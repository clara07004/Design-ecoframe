---
name: feedback-logo-slides
description: "Logo Ecoframe sempre presente nos slides — usar arquivo PNG, nunca texto"
metadata:
  type: feedback
---

A logo da Ecoframe deve estar presente em TODOS os slides de carrossel e posts estáticos, mesmo que de forma minimalista.

**Arquivos disponíveis:**
- Fundo escuro → `marca/logos/logo-branco.png`
- Fundo claro → `marca/logos/logo-cor.png`

**Implementação HTML (caminho relativo do instagram/):**
```html
<img src="../../../../../marca/logos/logo-branco.png" style="height:48px;object-fit:contain;">
```

**Why:** Exigência da usuária — logo nunca pode estar ausente. Texto tipográfico ("ecoframe" em Poppins) não substitui o arquivo de logo.

**How to apply:** Em qualquer HTML de slide, sempre usar `<img>` com o arquivo PNG real. **Altura padrão do header = 48px** — é o que está nos carrosséis aprovados (julho dia-01 e dia-17, todos com `height:48px`) e na skill `carrossel-unity`. O "mínimo 80px" do manual de marca (`project-ecoframe-design`) vale para uso geral do logo, não para o header dos slides — não aplicar 80px aqui. Escolher logo-branco para fundos escuros, logo-cor para fundos claros.
