# Execução aprovada — 2026-06-05 (refação)

> Refeito a pedido da Clara: pasta antiga (`conteudo/carrosseis/junho/...`) apagada e
> reconstruída com a convenção padronizada (`junho-2026/`) + regras de render atualizadas
> (1080×1350 exato, sem texto cortado/sobreposto). Conteúdo original commitado em `b7387b1`.

## Copy aprovada
- Ângulo: comparativo direto — "esquadria de alvenaria não funciona em Steel Frame"
- Headline da capa: "Esquadria de alvenaria não funciona em Steel Frame."
- Sub da capa: "E não é detalhe de instalação. É projeto."
- Briefing aprovado por Clara em 05/06 sem ajustes (ângulo e dados já validados antes)

## Estratégia de imagem (final)
- Slide 01 (capa): foto real Drive `1o_w6NYZp_qwjYOh_-sGOlvJdfdWTc7XT` — fachada residencial alto padrão
- Slide 02: IA product_closeup — corte do perfil PVC + montante de aço + lã mineral + painel cimentício
- Slide 03: IA architectural — torre Steel Frame vista de baixo, céu de vento, dessaturado
- Slide 04: IA architectural — interior calmo e limpo (SUBSTITUIU a foto Drive bagunçada do `1nltZF…`)
- Slide 05: IA architectural — interior premium acabado, janela de correr PVC à direita (REGERADO — 1ª versão saiu como render 3D vazio/amador)
- Slide 06 (CTA): foto real Drive `19sCZoDOK3is8HVpEAarQDT2U56PVQMxE` — interior com porta de correr PVC

### Prompts IA usados
- Slide 02: "Extreme close-up cross-section of a steel frame dry wall assembly, thin wall profile around 12 cm, light-gauge steel studs with mineral wool insulation and cement board cladding, white PVC window profile fitted to the panel edge, technical macro detail, neutral color grade, soft side light, ultra detailed, no people, no text overlay, photorealistic, portrait"
- Slide 03: "Tall contemporary steel frame residential building exterior seen from below, white PVC windows, overcast windy sky, desaturated cinematic color grade, sense of wind pressure, professional architectural photography, wide shot, no people, no text overlay, photorealistic, portrait"
- Slide 04: "Editorial architectural photograph of a calm minimalist high-end living room, large white PVC sliding window, serene quiet atmosphere, warm wood floor and white walls, neatly arranged furniture, impeccably clean and uncluttered, soft natural light, no people, no clutter, no text overlay, photorealistic, portrait"
- Slide 05: "Editorial architectural photograph of a finished high-end contemporary living room, large white PVC sliding window as hero element on the right, premium finished walls, warm wood floor, minimal designer furniture, soft natural daylight, shallow depth of field, warm color grade, no people, no text overlay, photorealistic, portrait"

## O que funcionou bem
- Card flutuante (slide 04) sobre interior LIMPO ficou muito superior à versão com foto Drive bagunçada
- Split painel escuro + foto à direita (slide 05) com interior premium regerado — posicionamento de alto padrão preservado
- Data boxes PSQ (slide 03) sobre torre moody — impacto imediato
- Reaproveitar os HTMLs validados do commit anterior + trocar só as imagens = render limpo de primeira, 6/6 em 1080×1350

## O que evitar
- Foto Drive `1nltZFpm49n5g9UY9Q6tmh_5SpjZvuQJw` (acústica): ambiente bagunçado, roupas no sofá — NÃO usar em conteúdo premium
- Prompt de interior Steel Frame sem "finished/editorial/photorealistic" gera render 3D vazio e amador (1ª versão do slide 05)
- Capa nunca com foto de alvenaria — visual acompanha o argumento de Steel Frame

## Legenda
- Primeira linha aprovada: "Steel Frame não perdoa especificação genérica."
- CTA duplo (salvar + comentar sistema construtivo) — validado. Texto completo em carousel-text.md
