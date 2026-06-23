---
name: feedback-carousel-design-aprovado
description: Padrões visuais e técnicas CSS aprovados para carrosseis Instagram da Ecoframe — baseado no carrossel eficiencia-energetica (aprovado 2026-05-25)
metadata:
  type: feedback
---

# Padrões de Design Aprovados — Carrossel Instagram Ecoframe

Aprovado explicitamente pela usuária em 2026-05-25: "gostei muito desse resultado, salve esse estilo de design na memoria. a marca imponente, sempre uma foto de fundo, design fluido."

Reafirmado em 2026-05-25 (carrossel dia-04): "está seguindo a mesma linha visual o que realmente causa uma impressão de identidade visual da empresa, onde ao ver o estilo de design já vai ser logo associado à marca."

**Why:** Consistência visual entre posts faz com que o público associe o estilo à marca antes de ler o nome. A combinação foto arquitetônica + gradiente escuro + tipografia Poppins Bold é a identidade visual da Ecoframe nas redes sociais.

**How to apply:** Usar esses padrões como template obrigatório para todos os carrosseis e posts. Nunca voltar a design só com gráficos. Verificar Drive antes de criar qualquer visual — fotos reais de produto têm prioridade sobre imagens geradas por IA.

---

## Regra central

**Todo slide = foto real + gradiente overlay + conteúdo tipográfico.** Nunca só gráfico.

---

## Padrão de overlay (gradiente sobre foto)

### Texto na base do slide (mais comum)
```html
<!-- Gradiente base: escurece de baixo para cima -->
<div style="position:absolute;inset:0;background:linear-gradient(to top,
  rgba(6,10,24,0.97) 0%,
  rgba(6,10,24,0.88) 35%,
  rgba(6,10,24,0.55) 58%,
  rgba(6,10,24,0.22) 78%,
  rgba(6,10,24,0.08) 100%);"></div>
<!-- Overlay topo para legibilidade do logo -->
<div style="position:absolute;top:0;left:0;width:100%;height:200px;background:linear-gradient(to bottom, rgba(6,10,24,0.72) 0%, transparent 100%);"></div>
```

### Texto distribuído pelo slide (slide tipo editorial)
```html
<!-- Overlay diagonal + vinheta radial -->
<div style="position:absolute;inset:0;background:linear-gradient(160deg,
  rgba(6,10,24,0.88) 0%,
  rgba(6,10,24,0.72) 50%,
  rgba(6,10,24,0.55) 100%);"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at center, transparent 40%, rgba(6,10,24,0.55) 100%);"></div>
```

### Slide CTA centralizado
```html
<!-- Overlay uniforme forte + vinheta -->
<div style="position:absolute;inset:0;background:rgba(6,10,24,0.78);"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at center, transparent 25%, rgba(6,10,24,0.50) 100%);"></div>
```

### Slide com foto no topo (split foto + texto)
```html
<!-- Foto ocupa top 580px -->
<img src="./img-slideXX.png" style="position:absolute;top:0;left:0;width:100%;height:580px;object-fit:cover;object-position:center top;">
<!-- Dissolve foto no fundo escuro -->
<div style="position:absolute;top:0;left:0;width:100%;height:580px;background:linear-gradient(to bottom, rgba(6,10,24,0.10) 0%, rgba(6,10,24,0.30) 55%, rgba(6,10,24,1.0) 100%);"></div>
<!-- Overlay topo para logo -->
<div style="position:absolute;top:0;left:0;width:100%;height:160px;background:linear-gradient(to bottom, rgba(6,10,24,0.75) 0%, transparent 100%);"></div>
```

---

## Header padrão (logo + tagline)

**Caminho correto do logo:** `../../../../../marca/logos/logo-branco.png` (5 níveis acima de `instagram/`)

```html
<div style="display:flex;align-items:center;gap:10px;flex-shrink:0;">
  <img src="../../../../../marca/logos/logo-branco.png" style="height:48px;object-fit:contain;">
  <span style="width:1.5px;height:22px;background:#4A61A0;margin:0 10px;display:inline-block;"></span>
  <span style="font-family:'Montserrat',sans-serif;font-size:16px;font-weight:700;color:#4A61A0;letter-spacing:0.14em;text-transform:uppercase;">Esquadrias em PVC</span>
</div>
```

---

## Escala tipográfica aprovada (atualizada 2026-05-25)

Fontes aumentadas para legibilidade mobile — canvas 1080px exibido a ~0.35x no feed do Instagram.

| Elemento | Fonte | Tamanho | Peso | Cor |
|---|---|---|---|---|
| Display/punchline | Poppins | 92–96px | 700 | #FFFFFF |
| Headline slide | Poppins | 84–90px | 700 | #FFFFFF |
| Body principal | Poppins | 44–46px | 400 | rgba(255,255,255,0.84–0.88) |
| Body secundário / subtítulo | Poppins | 40–42px | 300 | rgba(255,255,255,0.50–0.55) |
| Nota / caption | Montserrat | 28px | 400 | rgba(255,255,255,0.42) |
| Label uppercase | Montserrat | 18px | 700 | #4A61A0 |
| Tagline header (logo area) | Montserrat | 16px | 700 | #4A61A0 |
| CTA button | Montserrat | 24px | 700 | #ffffff |

**Regra:** Se o texto não couber com essas fontes, cortar o texto — nunca reduzir a fonte.

---

## Elementos de acento aprovados

**Divider:**
```html
<div style="width:48px;height:3px;background:#4A61A0;border-radius:2px;margin-bottom:32px;"></div>
```

**Badge/chip de métrica:**
```html
<div style="padding:10px 20px;background:#4A61A0;border-radius:8px;">
  <span style="font-family:'Montserrat',sans-serif;font-size:22px;font-weight:700;color:#ffffff;letter-spacing:0.06em;">W/m²K</span>
</div>
```

**Pill de produto (outline):**
```html
<div style="border:1.5px solid rgba(74,97,160,0.60);border-radius:9999px;padding:12px 32px;">
  <span style="font-family:'Montserrat',sans-serif;font-size:16px;font-weight:700;color:#4A61A0;letter-spacing:0.08em;">euroTEC</span>
</div>
```

**Botão CTA sólido:**
```html
<div style="background:#4A61A0;border-radius:9999px;padding:26px 80px;">
  <span style="font-family:'Montserrat',sans-serif;font-size:24px;font-weight:700;color:#ffffff;letter-spacing:0.10em;text-transform:uppercase;">Link na bio →</span>
</div>
```

**Cards comparativos (destaque vs neutro):**
```html
<!-- Destaque (PVC / produto principal) -->
<div style="flex:1;padding:28px 24px;background:rgba(74,97,160,0.18);border:1.5px solid rgba(74,97,160,0.45);border-radius:12px;">
<!-- Neutro (comparativo) -->
<div style="flex:1;padding:28px 24px;background:rgba(255,255,255,0.04);border:1.5px solid rgba(255,255,255,0.12);border-radius:12px;">
```

---

## Seleção de fotos do Drive por tipo de slide

- **Conteúdo térmico/luz/conforto:** interior com janelas altas e luz natural (ID: `1nltZFpm49n5g9UY9Q6tmh_5SpjZvuQJw`)
- **Especificação/projeto/resultado:** casa modernista com piscina, enquadramento clean (ID: `1jNxW31bytaFUa4jgfrz_ghbJIAToKz7g`)
- **CTA/premium/alto padrão:** interior com porta de correr e sala de jantar (ID: `19sCZoDOK3is8HVpEAarQDT2U56PVQMxE`)
- **Fachada residencial com esquadrias:** casa branca frontal dois pavimentos (ID: `1o_w6NYZp_qwjYOh_-sGOlvJdfdWTc7XT`)
- **Esquadrias panorâmicas externas:** casa com grandes painéis de vidro + piscina (ID: `1eCv6-NxvYMawjaS42uNLyEObJ7hAPw3l`)

Pasta completa no Drive: `1yMl_zKBySogepmeM7WTyihTYuXZFuZb6` (~23 fotos disponíveis). Ver [[reference-drive]].
