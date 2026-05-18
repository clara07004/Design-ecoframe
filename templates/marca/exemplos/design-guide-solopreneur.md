# Guia de Design — Solopreneur Exemplo

> Exemplo preenchido pra você ter referência.
> Copie e adapte pro seu estilo em marca/DESIGN.md

---

```yaml
---
version: alpha
name: "Nome da Marca"
description: "Solopreneur — marca pessoal editorial e quente"
status: configured
---

colors:
  primary: "#C96442"
  primary-active: "#A84F32"
  primary-disabled: "#E8B5A0"
  on-primary: "#FAF7F2"
  canvas: "#FAF7F2"
  surface-card: "#F3EFE8"
  ink: "#1C1917"
  body: "#3D3530"
  accent: "#C96442"

typography:
  display:
    fontFamily: "Instrument Serif"
    fontSize: "72px"
    fontWeight: "400"
    lineHeight: "1.1"
    letterSpacing: "-0.02em"
  heading:
    fontFamily: "Instrument Serif"
    fontSize: "40px"
    fontWeight: "400"
    lineHeight: "1.2"
  body:
    fontFamily: "Bricolage Grotesque"
    fontSize: "18px"
    fontWeight: "400"
    lineHeight: "1.6"
  caption:
    fontFamily: "Bricolage Grotesque"
    fontSize: "13px"
    fontWeight: "500"

spacing:
  xs: "8px"
  sm: "16px"
  md: "24px"
  lg: "40px"
  xl: "64px"
  section: "96px"

rounded:
  sm: "8px"
  md: "20px"
  lg: "20px"
  pill: "9999px"

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    padding: "14px 28px"
    height: "48px"
  card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "32px"
```

---

**Notas de estilo:**
- Tom quente, humano e editorial — tons terrosos com fundo off-white
- Bordas dashed, arredondadas — parece um livro bonito ou diário de marca pessoal
- Sombras sutis: `0 4px 20px rgba(0,0,0,0.06)`
- Nunca fundo branco puro — sempre usar o off-white `#FAF7F2`
- Amarelo-limão como acento destoa do tom quente — evitar
