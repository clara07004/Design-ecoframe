---
name: feedback-fonte-mobile
description: "Padrão de tamanho de fonte para carrosseis Instagram — aumentado para legibilidade mobile, incluindo pessoas com dificuldade de visão"
metadata:
  type: feedback
---

O canvas é 1080px mas é exibido em ~375px na tela do celular (fator ~0.35x), então as fontes precisam de hierarquia clara e corpo legível.

**Regra fixa do corpo:** o **texto de corpo** (prosa/descrição) é **sempre 32px** — valor fixo, não mínimo, não variar. Definido em `marca/DESIGN.md` (`typography.body.fontSize: 32px`) e nas skills `carrossel-unity` e `estatico-unity`.

**Escala de referência para carrosseis e posts Instagram:**

| Elemento | Tamanho |
|---|---|
| Headline principal / capa (destaque) | 62–96px (hierarquia, conforme densidade) |
| **Corpo de texto (prosa/descrição)** | **32px — FIXO** |
| Label uppercase | 16–18px |
| Tagline header (logo area) | 16px |
| CTA button text | 24px |
| Nota de rodapé / caption | 28px |

**Why:** o corpo em 32px é o que está nos carrosséis aprovados (julho dia-01 e dia-17 usavam ~30px) e no `DESIGN.md`. O padrão antigo de 44–46px foi abandonado (decisão da Clara em 2026-06-30) — ficava grande demais e nunca foi seguido na prática. 32px mantém legibilidade com densidade de texto adequada.

**How to apply:** corpo SEMPRE 32px em todos os HTMLs de carrossel e post estático. Se o texto não couber, cortar texto (menos palavras/linhas) — NUNCA mexer no 32px. Headlines variam por hierarquia; só o corpo é travado.

Relacionado: [[feedback-carousel-design-aprovado]]
