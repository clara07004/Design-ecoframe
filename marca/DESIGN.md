---
version: "1.0"
name: "Ecoframe"
description: "Esquadrias em PVC de alta performance — Manual de Marca v1.0"
status: configured
---

colors:
  primary: "#4A61A0"           # Azul Ecoframe — ícone, estrutura, elementos principais
  primary-active: "#3a4f8a"    # Azul escurecido para hover/ativo
  primary-disabled: "#9aacd0"  # Azul desbotado para estados desabilitados
  on-primary: "#FFFFFF"        # Texto branco sobre fundo azul
  secondary: "#2C6D14"         # Verde Ecoframe — "eco", folha, tagline "Esquadrias de PVC"
  on-secondary: "#FFFFFF"
  canvas: "#F5F5F0"            # Off-white — fundo principal, backgrounds
  surface-card: "#FFFFFF"      # Branco puro — cards e superfícies
  ink: "#1A1A1A"               # Preto — texto principal
  body: "#1A1A1A"
  accent: "#2C6D14"            # Verde como acento
  muted: "#6B6B6B"             # Cinza — textos secundários, legendas

  # Paleta de suporte
  white: "#FFFFFF"
  black: "#1A1A1A"
  off-white: "#F5F5F0"
  gray: "#6B6B6B"

  # DESCONTINUADA — não usar
  # teal: "#203D4A"  — paleta teal oficialmente descontinuada. Atualizar qualquer material que use essa cor.

typography:
  display:
    fontFamily: "Poppins"
    fontSize: "100px"
    fontWeight: "700"          # Bold
    lineHeight: "1.1"
    letterSpacing: "-0.02em"
  heading:
    fontFamily: "Poppins"
    fontSize: "70px"
    fontWeight: "700"          # Bold
    lineHeight: "1.2"
  subheading:
    fontFamily: "Poppins"
    fontSize: "48px"
    fontWeight: "600"
    lineHeight: "1.3"
  body:
    fontFamily: "Montserrat"
    fontSize: "32px"           # corpo de texto SEMPRE 32px (valor fixo, não variar)
    fontWeight: "400"
    lineHeight: "1.5"
  label:
    fontFamily: "Montserrat"
    fontSize: "22px"
    fontWeight: "700"          # Bold — para labels e labels técnicos
    lineHeight: "1.3"
  caption:
    fontFamily: "Montserrat"
    fontSize: "20px"
    fontWeight: "400"
    lineHeight: "1.4"

  # Regras de uso
  # - Poppins: títulos, identidade da marca, headlines
  # - Montserrat: corpo, labels, notas técnicas, legendas
  # - Mínimo 12px digital / 9pt impresso
  # - Não misturar mais de 2 famílias tipográficas
  # - Sem fontes serifadas em materiais digitais

spacing:
  xs: "16px"
  sm: "24px"
  md: "40px"
  lg: "64px"
  xl: "96px"
  section: "160px"

rounded:
  sm: "4px"
  md: "8px"
  lg: "16px"
  pill: "9999px"

# Logo
# - Nome: "ecoframe" (tudo minúsculo)
# - "eco" em Poppins Light + "frame" em Poppins Bold
# - Versão principal: Vertical Azul + Verde
# - Versões aprovadas: Vertical Verde, Negativo Fundo Verde, Monocromático Preto
# - Tamanho mínimo: 80px digital / 20mm impresso
# - Não alterar cores fora da paleta oficial
# - Não aplicar sombras, contornos ou efeitos
# - Não distorcer ou esticar
# - Não recriar com fontes diferentes
# - Não usar versão teal (#203D4A) — descontinuada

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "16px 32px"
    height: "52px"
    fontFamily: "Montserrat"
    fontWeight: "700"
    fontSize: "16px"

  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: "16px 32px"

  card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "40px"
    border: "1px solid #E5E5E0"

  tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    fontFamily: "Montserrat"
    fontWeight: "700"
    fontSize: "12px"

# Regras de uso das cores
# PODE:
# - Azul Ecoframe com fundo branco — combinação principal
# - Verde Ecoframe em tagline e destaques sobre fundo claro
# - Logo branco sobre fundo Azul — versão negativo
# - Texto escuro (#1A1A1A) sobre Off-White para leitura longa
#
# NÃO PODE:
# - Azul + Verde sobrepostos sem elemento neutro entre eles
# - Usar teal #203D4A — paleta completamente descontinuada
# - Alterar os valores HEX das cores primárias
# - Usar Verde como grafismo de fundo complexo

# =============================================================================
# ESTILO DE IMAGEM — Referência @ecophon_brasil
# Para uso pelos motores de geração de imagem (gpt-image2, etc.)
# Fonte: análise visual direta do perfil em 2026-05-21
# =============================================================================

image_style:

  # ---------------------------------------------------------------------------
  # FILOSOFIA VISUAL — princípios que regem todos os posts
  # ---------------------------------------------------------------------------
  visual_philosophy:

    feel: "Fluido, divertido e acolhedor — nunca frio ou corporativo"

    forbidden_aesthetic: "Estética de revista: layouts muito simétricos, quadriculados ou com cara de template pronto transmitem frieza e distância — exatamente o oposto do que queremos"

    background_rule: |
      OBRIGATÓRIO: toda imagem precisa ter um fundo com elementos visuais.
      Texturas, gradientes, formas, ilustrações, padrões, fotografias ou qualquer
      composição que dê profundidade e vida ao post.
      Fundo chapado com cor sólida + texto por cima é INACEITÁVEL — parece
      informe corporativo, não conteúdo de Instagram.

    avoid:
      - "Layouts retos, muito centrados e simétricos demais"
      - "Espaços vazios excessivos sem intenção"
      - "Tipografia única com fundo liso — independente de quão 'clean' pareça"
      - "Qualquer coisa que pareça saída de template de PowerPoint ou Canva genérico"

    pursue:
      - "Composições com camadas: fundo com textura ou elemento visual + elementos decorativos + texto"
      - "Formas orgânicas, elementos gráficos sobrepostos, uso inteligente de cor"
      - "Sensação de movimento e cuidado na montagem — como se tivesse sido pensado, não gerado automaticamente"
      - "Design que convida a olhar, não apenas a ler"

  # ---------------------------------------------------------------------------
  # FOTOGRAFIA — como devem ser as fotos
  # ---------------------------------------------------------------------------
  photography:

    dark_lifestyle:
      description: "Pessoas em ação no ambiente de uso do produto"
      mood: "Moody, atmosférico, slightly desaturated"
      lighting: "Ambient natural, soft side light, no harsh flash"
      color_grade: "Cool-neutral to warm shadows, not overexposed"
      subjects: "Real people, candid or near-candid poses — architect reviewing project, worker on site, couple viewing a property"
      framing: "Often cropped tight, subject off-center, environmental context visible"
      ecoframe_subjects: "Arquiteto revisando projeto em obra de Steel Frame, construtora instalando esquadrias, proprietário apreciando janelas prontas"

    architectural_installation:
      description: "Foto real do produto instalado em projeto acabado"
      mood: "Clean, premium, natural light dominant"
      lighting: "Bright window light, natural diffuse — produto visível no contexto real"
      color_grade: "Warm and natural — wood tones, concrete, white walls"
      framing: "Wide to mid shot — mostra o ambiente completo com produto integrado"
      ecoframe_subjects: "Fachada acabada com esquadrias de PVC, interior com janelas euroTEC/iTEC instaladas, detalhe de canto e perfil"

    product_closeup:
      description: "Macro/detalhe da superfície e estrutura do produto"
      mood: "Técnico e elegante simultaneamente"
      framing: "Close-up extremo — textura de superfície, corte transversal de perfil PVC multi-câmara, canto de esquadria"
      color_grade: "Neutro, fiel às cores reais do produto"
      ecoframe_subjects: "Seção transversal perfil PVC mostrando câmaras internas, detalhe do sistema de vedação, textura superficial do PVC"

  # ---------------------------------------------------------------------------
  # BACKGROUNDS — tipos de fundo por slide
  # ---------------------------------------------------------------------------
  backgrounds:

    off_white_textured:
      use: "Slides educativos, infográficos, textos principais"
      color: "#F5F5F0 aproximado — cream/warm off-white"
      texture: "Paper ou linen texture sutil, quase imperceptível. Às vezes: wireframe de losango ou grid diagonal fino em cinza claro translúcido sobreposto"
      feel: "Leve, limpo, premium — como papel de alta qualidade"

    solid_accent:
      use: "Slides de CTA final, fechamento, produto destaque"
      color: "Azul Ecoframe #4A61A0 — fundo sólido completo"
      texture: "Opcional: grid diagonal sutil em tom ligeiramente mais escuro"
      feel: "Impacto, energia, marca — quebra visual da sequência"

    full_bleed_dark:
      use: "Cover (capa), slides de problema, slides de transição"
      description: "Foto ocupa 100% do slide, tom escuro predominante"
      overlay: "Nenhum overlay opaco — texto sobreposto diretamente"
      text_color: "Branco puro ou branco com sombra suave"

    full_bleed_bright:
      use: "Slides de solução com produto instalado"
      description: "Foto ocupando 100%, tom claro/natural, produto visível no ambiente"
      text: "Texto em Azul Ecoframe ou branco (dependendo do fundo da foto)"

    split_dynamic:
      use: "Slides de contexto/problema"
      layout: "60% foto escura (esq) + 40% painel azul sólido (dir), com borda curva/arco na divisão — não hard cut"
      text: "Apenas no painel azul, cor branca ou off-white"

  # ---------------------------------------------------------------------------
  # ELEMENTOS GRÁFICOS — os 'assets' de design recorrentes
  # ---------------------------------------------------------------------------
  graphic_elements:

    text_highlight_box:
      description: "Retângulo sólido atrás de palavras-chave dentro do corpo de texto"
      color: "Azul Ecoframe #4A61A0 (sobre fundo claro) ou Branco (sobre fundo azul)"
      text_color: "Branco (se box azul) ou Azul (se box branco)"
      usage: "Destacar: nome do produto (iTEC, euroTEC, TECplus100), specs técnicos (Rw dB, Ug W/m²K), frases de prova técnica"
      style: "Padding pequeno (4-8px), sem border-radius exagerado — retângulo quase reto"

    hand_drawn_loop:
      description: "Oval ou loop desenhado à mão em traço fino, circunda o sujeito ou produto"
      color: "Azul Ecoframe #4A61A0 (como Ecophon usa amarelo)"
      style: "Brush stroke thin, slightly imperfect — NOT geometric — organic hand annotation feel"
      usage: "Cover slides sobre pessoa/ambiente, slides de produto para chamar atenção"

    white_bracket_frame:
      description: "Forma geométrica angular em branco — tipo colchete estilizado ou 'Z' com cantos arredondados, circunda o headline"
      color: "Branco puro"
      usage: "Cover escuro — cria uma moldura de destaque ao redor do título central"
      style: "Open bracket shape — não é retângulo fechado, apenas arestas decorativas nos cantos"

    floating_card:
      description: "Retângulo branco arredondado flutuando sobre a foto, com soft glow/sombra suave"
      radius: "16-24px"
      shadow: "Soft ambient shadow, não hard drop shadow"
      usage: "Container de informação técnica ou copy secundária em slides full-bleed"
      paired_with: "Sound wave lines flanking the card"

    sound_wave_lines:
      description: "Duas ou três linhas curvas paralelas em cada lado de um elemento, simulando ondas sonoras irradiando"
      color: "Azul Ecoframe #4A61A0 ou branco dependendo do fundo"
      usage: "Flanquear o floating_card ou elemento central — indica desempenho acústico/termico"
      ecoframe_adaptation: "Usar para indicar isolamento acústico (Rw) ou isolamento térmico (Ug) — ondas de calor ou de som"

    icon_circle:
      description: "Círculo sólido preenchido com ícone de linha branco dentro"
      fill: "Azul Ecoframe #4A61A0"
      icon: "Branco, estilo outline/line icon"
      usage: "Infográficos 'Regra simples' — comparações SEM vs COM esquadria de alto desempenho"
      icon_subjects_ecoframe: "Janela com raios de sol (térmica), ondas sonoras (acústica), gota d'água (impermeabilização), folha (eco), ferramenta (instalação)"

    accent_blob:
      description: "Forma orgânica grande em Azul Ecoframe #4A61A0 aparecendo parcialmente por um dos cantos"
      usage: "Canto superior-direito ou direito dos slides de solução — sinaliza transição para produto/CTA"
      style: "Quarto de círculo ou forma orgânica — só a borda aparece, resto cortado pela margem"

    pill_cta:
      description: "Botão de contorno pill/cápsula com texto pequeno"
      style: "Outline (border only, sem preenchimento) — Branco sobre fundos escuros, Azul sobre fundos claros"
      radius: "9999px (pill completo)"
      usage: "Pergunta CTA no cover ('Seu projeto inclui isso?'), CTA final ('link da bio')"

    spec_bar:
      description: "Barra horizontal na base do slide com especificações técnicas"
      style: "Fundo azul escuro ou cinza escuro, texto branco, labels pequenos"
      usage: "Slides de produto específico"
      ecoframe_specs: "Rw: XX dB | Ug: X,X W/m²K | Linha: euroTEC / iTEC / MAXXI"

  # ---------------------------------------------------------------------------
  # TEMPLATES DE LAYOUT — os 7 modelos identificados
  # ---------------------------------------------------------------------------
  layout_templates:

    T1_cover_atmosferico:
      name: "Cover Atmosférico"
      background: "Full-bleed dark photo"
      elements:
        - "White bracket frame centered (middle third)"
        - "Mixed-weight white headline: small sans label + large display + bold statement"
        - "Pill CTA at bottom (question form)"
      palette: "Dark image + pure white elements + optional accent loop"
      prompt_style: "Cinematic, moody, wide angle environmental photo with people, f/2.8 style, dark and atmospheric"

    T2_problema_highlight:
      name: "Problema com Highlight"
      background: "Off-white textured"
      elements:
        - "Dark charcoal headline, large scale, left-aligned or centered"
        - "Body text in gray, regular weight"
        - "Inline text highlight boxes (solid accent color behind key phrases)"
      palette: "Off-white + charcoal + Azul highlight"
      no_photo: true

    T3_regra_simples:
      name: "Regra Simples"
      background: "Off-white textured"
      elements:
        - "Title 'Regra simples' — gray, medium weight, top"
        - "2 rows: [icon circle] + [highlight label] + [gray body]"
        - "Very high whitespace, no photos"
      palette: "Off-white + gray text + Azul circles + Azul highlight boxes"
      no_photo: true

    T4_split_dinamico:
      name: "Split Dinâmico"
      background: "Left dark photo (60%) + right solid Azul panel (40%), curved arc boundary"
      elements:
        - "Text on Azul panel only, white color"
        - "Bold headline + regular body"
      palette: "Dark photo + Azul #4A61A0 + white text"

    T5_photo_floating_card:
      name: "Full Photo com Floating Card"
      background: "Full-bleed lifestyle/architectural photo"
      elements:
        - "Floating white rounded card with text"
        - "Sound wave curved lines flanking the card"
        - "Accent highlight within card text"
      palette: "Atmospheric photo + white card + Azul highlight"

    T6_solucao_produto:
      name: "Solução Produto"
      background: "Off-white textured"
      elements:
        - "Left: headline with accent-color box behind product name"
        - "Right: rounded-arch photo container (installation photo)"
        - "Bottom left: product material close-up"
        - "Thin hand-drawn loop around the main composition"
      palette: "Off-white + Azul highlights + real product photos"

    T7_cta_acento:
      name: "CTA Acento"
      background: "Solid Azul #4A61A0 (full slide)"
      elements:
        - "Logo Ecoframe white, centered"
        - "Short punchy headline in white"
        - "Pill CTA button outline in white"
        - "Previous slide photo peeking from one edge (continuity)"
        - "Optional: subtle diamond texture on Azul background"
      palette: "Azul #4A61A0 + white elements"

  # ---------------------------------------------------------------------------
  # HIERARQUIA TIPOGRÁFICA NAS IMAGENS
  # ---------------------------------------------------------------------------
  image_typography:
    cover_label: "Montserrat 400, small (14-16px equiv), uppercase or sentence case"
    cover_headline: "Poppins 700, very large (60-80px equiv), white on dark"
    slide_headline: "Poppins 700, large (40-56px equiv), dark charcoal on light bg"
    body_text: "Montserrat 400, medium (20-24px equiv)"
    highlight_text: "Same font/weight as surrounding — only background changes"
    cta_text: "Montserrat 700, small (14-16px equiv)"

  # ---------------------------------------------------------------------------
  # ADAPTAÇÃO: o que muda de Ecophon → Ecoframe
  # ---------------------------------------------------------------------------
  ecoframe_adaptation:
    accent_color: "Amarelo Ecophon (#F5C518) → Azul Ecoframe (#4A61A0)"
    cta_slide: "Fundo amarelo sólido → Fundo Azul sólido"
    split_panel: "Painel amarelo → Painel Azul"
    highlight_box: "Box amarelo → Box Azul (texto branco dentro)"
    icon_circles: "Círculos amarelos → Círculos Azul Ecoframe"
    hand_drawn: "Loop amarelo → Loop Azul"
    accent_blob: "Blob amarelo → Blob Azul"
    product_photos: "Forros acústicos em lã de vidro → Esquadrias PVC iTEC / euroTEC / MAXXI"
    lifestyle_context: "Academia, escritório, hospital → Obra Steel Frame, fachada alto padrão, interior residencial contemporâneo"
    spec_bar_values: "NRC (absorção sonora) → Rw dB (isolamento acústico) + Ug W/m²K (transmissão térmica)"
    infographic_contrast: "Sem tratamento acústico vs Com Ecophon → Esquadria alumínio comum vs Esquadria PVC alta performance"
