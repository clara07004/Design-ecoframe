# Fluxo Completo — Do Calendário ao Post Pronto

## Visão do fluxo

```
/calendario-comercial
        ↓ você aprova
/briefing-unity
        ↓ você aprova
        ├── formato carrossel  →  /carrossel-unity
        ├── formato imagem     →  /estatico-unity
        └── formato vídeo      →  /roteiro-unity
        ↓ você aprova
/publicar-social-unity  (opcional — publicação automática)
```

Você pode entrar no fluxo em qualquer etapa. Se já sabe o que quer postar, pode pular direto para `/briefing-unity`. Se já tem o briefing aprovado, pode pular direto para a skill de produção.

---

## Etapa 1 — Calendário Comercial

**Quando usar:** no início de cada mês, para mapear as oportunidades do período.

**Como chamar:**
```
/calendario-comercial
```

**O que acontece:**

1. O Claude lê `_contexto/empresa.md` e `_contexto/estrategia.md`
2. Pergunta qual período cobrir e qual a frequência de postagem
3. Faz pesquisa na web sobre eventos culturais, esportivos e de entretenimento do período
4. Classifica as semanas em janelas quentes (🟢), mornas (🟡) e frias (🔴)
5. Monta um mapa de oportunidades cruzando produto × momento cultural
6. Propõe um tema narrativo que conecta as ações do mês

**Checkpoint:** o calendário é apresentado completo. Você pode:
- **Aprovar** → o calendário é salvo em `conteudo/calendarios/[periodo]/`
- **Editar** → ajustar semanas ou janelas específicas
- **Pedir ajuste** → mudar o tema narrativo ou a ênfase de produto

**Exemplo de conversa:**
```
Você: /calendario-comercial
Claude: Qual período você quer cobrir?
Você: Junho 2026
Claude: [pesquisa eventos do período]
Claude: [apresenta o mapa de oportunidades]
Você: Aprovo. A semana 2 com foco em isolamento acústico está perfeito.
```

---

## Etapa 2 — Briefing

**Quando usar:** após o calendário aprovado, para cada post ou série de posts que você vai produzir.

**Como chamar:**
```
/briefing-unity
```

**O que o Claude precisa saber:**
- Qual janela do calendário (semana, tema, produto)
- Plataforma (Instagram, TikTok, LinkedIn)
- Formato pretendido (carrossel, imagem, vídeo) — se já tiver ideia

**O que o Claude entrega:**
1. **Gancho** — primeira frase do post (a linha de abertura)
2. **Copy base** — texto completo adaptado por plataforma
3. **Formato recomendado** — carrossel, imagem ou vídeo, com justificativa
4. **Orientações visuais** — paleta dominante, estilo de imagem, elementos obrigatórios
5. **Hashtags** — por plataforma (Instagram, TikTok, LinkedIn)
6. **Metadados** — skill a acionar, data ideal de publicação

**Checkpoint:** o briefing é apresentado com três opções:
```
[A] Aprovar e gerar asset
[E] Editar
[C] Cancelar
```

Se você escolher **[A]**, o Claude informa qual skill acionar e pode já iniciar.

**Exemplo de conversa:**
```
Você: /briefing-unity
       Janela: semana 2 de junho — isolamento acústico
       Produto: linha euroTEC
       Plataforma: Instagram
       Formato: carrossel
Claude: [entrega briefing completo]
Você: A — vamos pro carrossel
Claude: Vou acionar /carrossel-unity com este briefing. Posso começar?
Você: Sim
```

---

## Etapa 3a — Carrossel

**Quando usar:** para conteúdo educativo, comparativo ou de autoridade em múltiplos slides.

**Como chamar:**
```
/carrossel-unity
```

O briefing aprovado deve estar em contexto (ou o Claude vai perguntar o tema).

### Fase 1 — Texto

O Claude lê os arquivos de contexto e produz:
- 3 opções de título para a capa (você escolhe uma)
- 8-10 slides com texto completo, organizados em: capa → contexto → desenvolvimento → implicação → CTA

O texto segue `_contexto/preferencias.md` — tom técnico acessível, sem travessões, sem bullet points disfarçados.

**Checkpoint:** você vê o texto completo e as 3 opções de capa. Escolhe a capa e aprova (ou pede ajustes).

### Fase 1.5 — Imagens

Após o texto aprovado, o Claude identifica quais slides se beneficiam de imagem:
- **Slide 1 (capa):** SEMPRE recebe imagem — obrigatório
- **Slides de impacto** (dados, fatos, revelações): opcional, máximo 2 adicionais
- **Slides tipográficos** (listas, texto longo): sem imagem — layout clean

Para cada imagem, o Claude constrói um prompt em inglês e mostra todos antes de gerar.

**Checkpoint:** você confirma os prompts antes de qualquer geração (antes de gastar crédito).

Após confirmação, o script Python é executado para cada imagem:
```powershell
python ".claude/skills/gpt-image2-unity/gerar-imagem.py" "PROMPT" "conteudo/carrosseis/TEMA/instagram/img-slide01.png" "portrait"
```

Cada imagem leva 60–180 segundos. O Claude avisa antes de executar.

**Checkpoint:** você vê as imagens geradas e aprova ou pede regeneração individual.

### Fase 2 — Visual (HTML + PNG)

Com o texto e imagens aprovados, o Claude monta um HTML por slide (1080×1350px) aplicando:
- Cores do `marca/DESIGN.md`
- Tipografia do `marca/DESIGN.md`
- Layout diferente para cada slide (não repete o mesmo template)
- Imagens como fundo com overlay gradiente

O slide 1 é renderizado primeiro e mostrado:
```powershell
npx.cmd playwright screenshot --viewport-size=1080,1350 --full-page "file:///CAMINHO/slide-01.html" "CAMINHO/slide-01.png"
```

**Checkpoint:** você vê o slide 1. Se aprovado, o Claude renderiza os demais.

**Checkpoint final:** você vê todos os slides renderizados e aprova.

### Fase 3 — Versão TikTok (opcional)

Após aprovar o carrossel, o Claude pergunta se quer a versão TikTok (1080×1920). Se sim, adapta os HTMLs e renderiza novamente.

**Output final:**
```
conteudo/carrosseis/[tema]/
  carousel-text.md
  instagram/
    img-slide01.png    ← imagem da capa
    slide-01.html → slide-01.png
    slide-02.html → slide-02.png
    ...
  tiktok/ (se solicitado)
    slide-01.html → slide-01.png
    ...
  _aprovado.md         ← histórico da execução aprovada
```

---

## Etapa 3b — Post Estático

**Quando usar:** para um card único — foto impactante com texto sobreposto.

**Como chamar:**
```
/estatico-unity
```

### Fase 1 — Copy e prompt

O Claude extrai do briefing:
- Headline (frase de impacto, máximo 10 palavras)
- Tagline/categoria
- Texto de apoio (1-2 frases)

E constrói o prompt da foto de fundo em inglês.

**Checkpoint:** você vê a copy extraída + o prompt da foto antes de qualquer geração.

### Fase 2 — Geração da foto

```powershell
python ".claude/skills/gpt-image2-unity/gerar-imagem.py" "PROMPT" "conteudo/imagens/TEMA/foto-fundo.png" "portrait"
```

**Checkpoint:** você vê a foto gerada e aprova (ou pede refinamento do prompt).

### Fase 3 — Montagem e renderização

O Claude monta o HTML (1080×1350px) com:
- Foto de fundo em full-bleed (100% do card)
- Overlay gradiente suave
- Logo da Ecoframe no topo
- Copy na base (tagline → separador → headline → texto de apoio)
- Cores e tipografia do DESIGN.md

Renderiza e mostra o resultado.

**Checkpoint final:** você aprova. O arquivo `post-01.png` é o post final pronto para publicar.

**Output final:**
```
conteudo/imagens/[tema]/
  foto-fundo.png     ← foto gerada
  prompt.txt         ← prompt usado (referência para variações)
  post-01.html       ← layout
  post-01.png        ← post final
  _aprovado.md       ← histórico
```

---

## Etapa 3c — Roteiro de Vídeo

**Quando usar:** para Reels do Instagram ou TikTok.

**Como chamar:**
```
/roteiro-unity
```

O Claude pergunta se é conteúdo orgânico (autoridade, educação) ou tráfego pago (conversão). Baseado na resposta:
- Orgânico → usa metodologia Ogilvy (big idea, copy de marca)
- Pago → usa metodologia Schwartz (consciência do cliente, resposta direta)

**Output:** roteiro com tempo por cena, narração sugerida, orientações de câmera e montagem.

---

## Etapa 4 — Publicação (opcional)

**Quando usar:** para publicar automaticamente no Instagram após aprovação do post.

**Como chamar:**
```
/publicar-social-unity
```

Requer `credentials/meta.txt` configurado com o token da Meta. Publica o arquivo PNG aprovado com a legenda gerada no briefing.

---

## Fluxo rápido — sem calendário

Se você já sabe o que quer postar e não precisa do calendário:

```
Você: /briefing-unity
      Tema: diferença entre PVC e alumínio
      Plataforma: Instagram
      Formato: carrossel
Claude: [entrega briefing]
Você: A
Claude: [inicia /carrossel-unity]
[... fases com checkpoints ...]
Claude: [entrega carrossel pronto]
```

---

## Fluxo ultra-rápido — direto para produção

Se já tem o briefing aprovado e quer ir direto para o conteúdo:

```
Você: /carrossel-unity
      Tema: isolamento acústico das esquadrias euroTEC
      Ângulo: comparativo técnico com alumínio
      Público: arquitetos e construtores
```

O Claude vai perguntar o que faltar e iniciar a Fase 1 diretamente.

---

## Comandos de manutenção

### `/syncar`
Salva o estado atual no GitHub (commit + push). Use ao final de uma sessão produtiva ou quando quiser garantir backup.

```
Você: /syncar
Claude: [faz commit e push]
```

### `/mapear`
Entrevista você sobre processos repetitivos e cria skills personalizadas. Use quando identificar uma tarefa que faz sempre e quer automatizar.

### `/setup`
Configura o sistema para um novo negócio. Use quando for adaptar o repositório para outro cliente.

---

## Dicas de uso

**Corrija e o sistema aprende:**
Se o Claude fizer algo errado, corrija diretamente ("na verdade, evite sempre mencionar preço"). O Claude vai perguntar se quer salvar isso como regra permanente. Se sim, salva em `_contexto/preferencias.md` e nunca comete o mesmo erro.

**Use os `_aprovado.md` a seu favor:**
Depois que um carrossel ou post é aprovado, o arquivo `_aprovado.md` registra o que funcionou. Na próxima execução do mesmo tema, o Claude lê esse histórico e parte de um nível de qualidade mais alto.

**Regenere apenas o que precisa:**
Se um slide ficou ruim mas os outros estão bons, você pode pedir para regenerar só aquele. "O slide 3 ficou confuso — refaz só ele com outro ângulo." O Claude edita o HTML e re-renderiza somente o slide afetado.

**Prompt de imagem é iterativo:**
Se a foto de fundo não ficou boa, descreva o que faltou e o Claude ajusta o prompt e gera novamente. "A foto ficou muito escura e sem produto visível — quero uma cena mais iluminada, com esquadrias de PVC claramente visíveis num interior contemporâneo."
