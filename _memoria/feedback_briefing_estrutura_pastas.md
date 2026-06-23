---
name: feedback-briefing-estrutura-pastas
description: "Convenção de pasta para conteúdo — tudo de um dia fica junto dentro de conteudo/[formato]/[mes]/dia-XX-tema/"
metadata:
  type: feedback
---

Briefings NÃO ficam em pasta separada. Todo o conteúdo de um dia fica dentro da pasta do formato (carrossel, estatico, reel), organizado por mês e dia.

**Por que:** O briefing é a origem do asset — faz sentido ficarem juntos. Evita navegar entre pastas diferentes para ver contexto e asset.

**Estrutura correta:**
```
conteudo/carrosseis/junho/dia-03-eficiencia-energetica/
  _briefing.md          ← briefing aprovado
  carousel-text.md      ← copy dos slides
  imagens-geradas/      ← opções geradas antes da seleção
  instagram/            ← slides HTML + PNG finais
```

**Como aplicar:** Ao salvar qualquer briefing aprovado, criar dentro da pasta do formato correspondente: `conteudo/[formato]/[mes]/dia-XX-[tema]/_briefing.md`. Formatos: carrosseis, estaticos, reels.

Relacionado: [[feedback-carousel-design-aprovado]]
