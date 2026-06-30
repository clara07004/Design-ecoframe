---
name: ctas-fixos-dois-modelos
description: "A marca usa dois CTAs fixos (PNG pronto) para fechar os posts, escolhidos pelo objetivo — não se inventa CTA por post."
metadata:
  type: feedback
---

A Ecoframe padronizou **dois modelos fixos de CTA** para fechar os posts. Não se escreve nem se desenha CTA novo por post: escolhe-se um dos dois pelo objetivo do conteúdo e usa-se exatamente como está no repo.

- **CTA 1 — Conversão** (`marca/ctas/post pronto/cta-01.png`): fundo Azul sólido. Para post que **vende** (produto, linha específica, fundo de funil, quebra de objeção). Headline "Especificar a esquadria certa começa com uma conversa." + botão "Solicite seu orçamento pelo direct" + apoio com o site esquadrias.fastsistemasconstrutivos.com.br como destino do especialista. Visual: foto premium (janela PVC na hora dourada) no topo dissolvendo no painel Azul.
- **CTA 2 — Salvamento** (`marca/ctas/post pronto/cta-02.png`): foto full-bleed + gradiente. Para post que **ensina** (educativo, autoridade, topo de funil, técnico). Headline "Quem especifica bem, guarda referência." + pill "Salve este post para consultar depois."

Regra de bolso: **vende → CTA 1, ensina → CTA 2.**

**Why:** a Clara pediu (2026-06-30) para padronizar os CTAs em dois modelos fixos em vez de cada post ter o seu, e que entrassem como PNG pronto. Na primeira versão o CTA 2 dizia "Salve agora. Especifique melhor depois." — ela vetou porque "especifique melhor depois" sugere que a marca não é boa o suficiente para ser pensada agora e empurra o alto padrão para segundo plano. Reescrito para posicionar o save como atitude de quem especifica bem (referência técnica), sem adiamento.

**How to apply:** os PNGs já estão renderizados (1080×1350) em `marca/ctas/post pronto/`. No carrossel, o último slide é o PNG do CTA escolhido, copiado para a pasta `post pronto/` do conteúdo com o próximo número da sequência (ex.: `slide-09.png`) — não montar HTML de CTA. No post estático, usar a linha de ação do modelo escolhido como CTA do card, ou reaproveitar o PNG pronto quando fechar uma sequência. **O repo versiona só os PNGs prontos** (`cta-01.png`/`cta-02.png`); os arquivos-fonte (`.html` + foto de fundo `img-cta.png`) ficam locais na máquina de origem, fora do git, pra manter o repo leve. Re-render documentado em `marca/ctas/README.md`. Registrado nas skills /carrossel-unity e /estatico-unity. Copy sem travessão e sem vícios de IA.

Relacionado: [[banir-vicios-linguagem-ia]], [[post-pronto-subpasta-pngs]], [[feedback-carousel-design-aprovado]], [[feedback-logo-slides]]
