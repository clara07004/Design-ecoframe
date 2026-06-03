---
name: feedback-carousel-design-aprovado
description: Padrões CSS/tipográficos aprovados, catálogo de componentes e mapa de fotos testadas para carrossel Ecoframe.
metadata:
  type: feedback
---

Catálogo de padrões CSS, componentes e fotos **aprovados** para carrossel. Consultar **antes
de inventar componente novo**. Fonte viva dos snippets completos: os carrosséis de junho 2026
([dia-02](../../conteudo/carrosseis/junho/dia-02-5-criterios-especificacao/),
[dia-03](../../conteudo/carrosseis/junho/dia-03-eficiencia-energetica/),
[dia-04](../../conteudo/carrosseis/junho/dia-04-especificacao-tecnica/)) — o template visual oficial.

**Why:** a Ecoframe constrói identidade visual no feed — o público precisa reconhecer um post
da marca antes de ler o nome. Inventar componente fora do catálogo quebra esse reconhecimento.

**How to apply:** copiar a estrutura de junho, manter rigorosamente header, gradiente, paleta,
escala e componentes. Inovação visual nesse nível **não** está autorizada.

---

## Canvas e base (extraído dos HTMLs de junho)

```css
body { width:1080px; height:1350px; overflow:hidden; background:#060a18; }
/* container raiz: position:relative; width:1080px; height:1350px; overflow:hidden; */
/* padding do conteúdo: 64px 80px 72px */
```

## Header padrão (todos os slides)

```html
<div style="display:flex;align-items:center;gap:10px;flex-shrink:0;">
  <img src="../../../../../marca/logos/logo-branco.png" style="height:48px;object-fit:contain;">
  <span style="width:1.5px;height:22px;background:#4A61A0;margin:0 10px;display:inline-block;"></span>
  <span style="font-family:'Montserrat',sans-serif;font-size:16px;font-weight:700;color:#4A61A0;letter-spacing:0.14em;text-transform:uppercase;">Esquadrias em PVC</span>
</div>
```
> Logo no header dos slides de junho = `height:48px`. (O DESIGN.md cita "mínimo 80px digital" —
> divergência real entre regra e prática; usar 48px no header até a Clara decidir. Ver [[feedback-logo-path-html]].)

## Overlay de gradiente para texto na base (mais comum)

```html
<div style="position:absolute;inset:0;background:linear-gradient(to top,
  rgba(6,10,24,0.97) 0%, rgba(6,10,24,0.88) 40%, rgba(6,10,24,0.50) 65%, rgba(6,10,24,0.12) 100%);"></div>
<div style="position:absolute;top:0;left:0;width:100%;height:200px;
  background:linear-gradient(to bottom, rgba(6,10,24,0.72) 0%, transparent 100%);"></div>
```
**Direção do gradiente segue a posição do conteúdo.** Texto na base → bottom→top. Texto à
esquerda → left→right. Nunca overlay sólido cobrindo a imagem.

## Glow blob de profundidade (canto)

```html
<div style="position:absolute;bottom:-60px;left:-60px;width:280px;height:280px;
  border-radius:50%;background:rgba(74,97,160,0.18);filter:blur(55px);"></div>
```

## Divider de seção

```html
<div style="width:48px;height:3px;background:#4A61A0;border-radius:2px;margin-bottom:24px;"></div>
```

## Headline padrão (slide escuro)

```css
font-family:'Poppins'; font-size:88px; font-weight:700; color:#FFFFFF;
line-height:1.06; letter-spacing:-0.022em;
```

## Lista numerada (icon circle + texto)

```html
<div style="display:flex;align-items:flex-start;gap:24px;">
  <div style="width:48px;height:48px;border-radius:50%;background:rgba(74,97,160,0.25);
    border:1.5px solid rgba(74,97,160,0.55);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:4px;">
    <span style="font-family:'Montserrat';font-size:16px;font-weight:700;color:#4A61A0;">01</span>
  </div>
  <div style="font-family:'Poppins';font-size:44px;font-weight:400;color:rgba(255,255,255,0.86);line-height:1.40;">Texto do passo.</div>
</div>
```

## Dissolve suave em split foto + texto

```html
<img src="./img-slideXX.png" style="position:absolute;top:0;left:0;width:100%;height:580px;object-fit:cover;">
<div style="position:absolute;top:0;left:0;width:100%;height:580px;
  background:linear-gradient(to bottom, rgba(6,10,24,0.10) 0%, rgba(6,10,24,0.30) 55%, rgba(6,10,24,1.0) 100%);"></div>
```

---

## Catálogo de elementos gráficos (DESIGN.md → graphic_elements)

| Componente | Descrição | Cor |
|---|---|---|
| **Text highlight box** | Retângulo sólido atrás de palavra-chave (nome de linha, spec, prova) | Azul `#4A61A0` (fundo claro) / Branco (fundo azul). Padding 4–8px, quase reto |
| **Hand-drawn loop** | Oval/loop orgânico circundando sujeito ou produto | Azul `#4A61A0`, traço fino imperfeito (não geométrico) |
| **White bracket frame** | Colchete decorativo aberto nos cantos do headline | Branco puro |
| **Floating card** | Card branco arredondado flutuante + soft shadow | Radius 16–24px, sombra ambiente suave |
| **Sound wave lines** | 2–3 linhas curvas paralelas flanqueando elemento (acústica/térmica) | Azul ou branco conforme fundo |
| **Icon circle** | Círculo azul cheio com ícone de linha branco | Fill azul `#4A61A0`, ícone branco outline |
| **Accent blob** | Forma orgânica azul aparecendo pelo canto (transição p/ CTA) | Azul `#4A61A0`, só a borda aparece |
| **Pill CTA** | Cápsula só com borda (outline), texto pequeno | Branco (fundo escuro) / Azul (fundo claro), radius 9999px |
| **Spec bar** | Barra base com specs técnicos | `Rw: XX dB \| Ug: X,X W/m²K \| Linha: euroTEC / iTEC / MAXXI` |

---

## Mapa de fotos do Drive já testadas

Pasta "Fotos do Produto": `1yMl_zKBySogepmeM7WTyihTYuXZFuZb6`. Priorizar <300KB.

| Uso | ID |
|---|---|
| Térmica / luz / conforto | `1nltZFpm49n5g9UY9Q6tmh_5SpjZvuQJw` |
| Especificação / projeto | `1jNxW31bytaFUa4jgfrz_ghbJIAToKz7g` |
| CTA / alto padrão | `19sCZoDOK3is8HVpEAarQDT2U56PVQMxE` |
| Fachada residencial | `1o_w6NYZp_qwjYOh_-sGOlvJdfdWTc7XT` |
| Panoramas externos | `1eCv6-NxvYMawjaS42uNLyEObJ7hAPw3l` |

> Esses IDs estão chumbados no agente e aqui — confirmar que ainda apontam para a foto certa
> antes de baixar (não há auditoria automática). Baixar via MCP Drive e salvar como `img-slideXX.jpg`.

Relacionados: [[feedback-fonte-mobile]] · [[feedback-logo-path-html]] · [[feedback-proporcoes-imagem]] · [[feedback-design-direcao]]
</content>
