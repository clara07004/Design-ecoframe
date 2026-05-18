# Guia de Design — Agência Exemplo

> Exemplo preenchido pra você ter referência.
> Copie e adapte pro seu estilo em marca/DESIGN.md

---

```yaml
---
version: alpha
name: "Nome da Agência"
description: "Agência de performance — dark e bold"
status: configured
---

colors:
  primary: "#FF5C35"
  primary-active: "#E04420"
  primary-disabled: "#FF9C85"
  on-primary: "#F5F5F5"
  canvas: "#0F0F0F"
  surface-card: "#1A1A1A"
  ink: "#F5F5F5"
  body: "#C0C0C0"
  accent: "#FF5C35"

typography:
  display:
    fontFamily: "Syne"
    fontSize: "80px"
    fontWeight: "800"
    lineHeight: "1.0"
    letterSpacing: "-0.03em"
  heading:
    fontFamily: "Syne"
    fontSize: "36px"
    fontWeight: "700"
    lineHeight: "1.1"
  body:
    fontFamily: "DM Sans"
    fontSize: "16px"
    fontWeight: "400"
    lineHeight: "1.6"
  caption:
    fontFamily: "DM Sans"
    fontSize: "12px"
    fontWeight: "500"

spacing:
  xs: "8px"
  sm: "16px"
  md: "24px"
  lg: "40px"
  xl: "64px"
  section: "96px"

rounded:
  sm: "4px"
  md: "12px"
  lg: "12px"
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
- Dark e bold — interface de agência de performance sem frescura
- Laranja `#FF5C35` aparece só em CTAs e destaques críticos, não como cor de fundo
- Sem gradiente como fundo de seção inteira
- Sem verde em qualquer tom
- Cards com rounding máximo de 16px — acima parece infantil
- Sombras: não usar
