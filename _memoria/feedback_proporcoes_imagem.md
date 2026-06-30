---
name: feedback-proporcoes-imagem
description: Proporções corretas por formato e plataforma para geração de imagem
metadata:
  type: feedback
---

Proporções corretas para geração de imagem no contexto Ecoframe:

- **Instagram feed / carrossel / post estático** → `portrait` (1024×1536)
- **Instagram Stories / Reels / TikTok** → `portrait` (1024×1536)
- **LinkedIn capa / banner** → `landscape` (1536×1024, proporção 3:2)

**Why:** o slide/post de feed é renderizado em 1080×1350 (4:5). As skills `carrossel-unity` e `estatico-unity` geram a foto de fundo em `portrait` (1024×1536) para encaixar em 1080×1350 via `object-fit:cover`. `square` (1024×1024) foi descontinuado para feed — sobra corte lateral pior no canvas 4:5.

**How to apply:** Ao montar o comando de geração (`gerar-imagem.py "PROMPT" "...img.png" "portrait"`) para carrossel, post estático, Story, Reel ou TikTok do Instagram, usar sempre `portrait`. `landscape` só para LinkedIn capa/banner.

Relacionado: [[feedback-fluxo-principal-carrossel]]
