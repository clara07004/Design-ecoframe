---
name: feedback-briefing-estrutura-pastas
description: "Convenção de pasta para conteúdo — tudo de um dia fica junto dentro de conteudo/[formato]/[mes]/dia-XX-tema/"
metadata:
  type: feedback
---

Briefings NÃO ficam em pasta separada. Todo o conteúdo de um dia fica dentro da pasta do formato (carrossel, estatico, reel), organizado por mês e dia.

**Por que:** O briefing é a origem do asset — faz sentido ficarem juntos. Evita navegar entre pastas diferentes para ver contexto e asset.

**Estrutura correta (carrossel):**
```
conteudo/carrosseis/[periodo]/dia-DD-tema/
  _briefing.md          ← briefing aprovado
  carousel-text.md      ← copy dos slides
  instagram/            ← img-slideXX.png (fundos) + slide-XX.html
    post pronto/        ← slide-XX.png finais (arquivos de publicar)
```

**Como aplicar:** Ao salvar qualquer briefing aprovado, criar dentro da pasta do formato correspondente: `conteudo/[formato]/[periodo]/dia-DD-[tema]/_briefing.md`. Nomes de formato reais: `carrosseis`, `post-estatico`, `reels`. Pasta nomeada pela data de publicação (`dia-DD`), ver [[nomenclatura-pasta-por-data-publicacao]]. Os PNGs finais ficam em `post pronto/`, ver [[post-pronto-subpasta-pngs]].

Relacionado: [[feedback-carousel-design-aprovado]]
