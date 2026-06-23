---
name: feedback-proporcoes-imagem
description: Proporções corretas por formato e plataforma para geração de imagem
metadata:
  type: feedback
---

Proporções corretas para geração de imagem no contexto Ecoframe:

- **Instagram feed / carrossel** → `square` (1024×1024, proporção 1:1)
- **Instagram Stories / Reels / TikTok** → `portrait` (1024×1536, proporção 9:16)
- **LinkedIn capa / banner** → `landscape` (1536×1024, proporção 3:2)

**Why:** "portrait" no script é 9:16 (Stories), não 4:5 feed. Para qualquer post de feed ou carrossel do Instagram, usar sempre `square`.

**How to apply:** Ao montar o comando de geração para carrossel ou post estático do Instagram, sempre usar `square`. Só usar `portrait` quando for Story, Reel ou TikTok.
