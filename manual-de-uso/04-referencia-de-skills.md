# Referência de Skills — O Que Cada Uma Faz

## Como invocar uma skill

Skills são chamadas com `/nome-da-skill` no início da mensagem. O Claude lê o arquivo `SKILL.md` correspondente em `.claude/skills/[nome]/` e segue as instruções.

Você também pode descrever o que quer em linguagem natural — o Claude identifica a skill relevante automaticamente. Por exemplo, "faz um carrossel sobre isolamento acústico" aciona `/carrossel-unity` sem você precisar digitar o comando.

---

## Skills de produção de conteúdo

### `/calendario-comercial`
**Arquivo:** `.claude/skills/calendario-comercial/SKILL.md`

**Para que serve:** Cria o mapa estratégico de oportunidades do mês. Cruza eventos culturais, esportivos e de entretenimento com os produtos e objetivos da empresa para identificar quando postar e com qual ângulo.

**Quando usar:** Uma vez por mês, antes de começar a produção de conteúdo.

**O que precisa ter:**
- `_contexto/empresa.md` configurado
- `_contexto/estrategia.md` configurado
- Acesso à internet (para pesquisar eventos do período)

**O que entrega:**
- Radar cultural do período
- Mapa de oportunidades por semana (🟢🟡🔴)
- Tema narrativo do mês
- Alertas e riscos
- Arquivo salvo em `conteudo/calendarios/[periodo]/`

**Metodologia:** Framework MOMENTO (Mídia, Oportunidades, Metas, Eventos, Narrativa, Timing, Objeções)

---

### `/briefing-unity`
**Arquivo:** `.claude/skills/briefing-unity/briefing-unity.md`

**Para que serve:** Gera o briefing completo de um post específico — gancho, copy, formato, orientações visuais, hashtags. É a ponte entre o calendário estratégico e a produção do asset.

**Quando usar:** Para cada post que vai produzir, após o calendário aprovado. Pode ser usado sem calendário se você já souber o tema.

**O que precisa ter:**
- Tema ou janela do calendário
- Plataforma destino
- Formato pretendido (opcional — o Claude pode recomendar)

**O que entrega:**
1. Gancho (linha de abertura do post)
2. Copy por plataforma
3. Formato recomendado com justificativa
4. Orientações visuais
5. Hashtags por plataforma
6. Metadados (skill a acionar, data ideal)

**Checkpoint de saída:** `[A] Aprovar / [E] Editar / [C] Cancelar`

---

### `/carrossel-unity`
**Arquivo:** `.claude/skills/carrossel-unity/SKILL.md`

**Para que serve:** Produz um carrossel completo — do texto ao PNG renderizado, pronto para publicar.

**Quando usar:** Quando o briefing define formato "carrossel" ou você quer um post de múltiplos slides.

**Fases:**
1. **Texto** (8–10 slides) + 3 opções de capa
2. **Imagens** via GPT Image 2 (capa obrigatória + até 2 slides de impacto)
3. **HTML + PNG** via Playwright — um arquivo por slide

**Checkpoints:** após texto, após imagens, após slide 1 renderizado, após todos os slides

**Dimensões:** Instagram 1080×1350px | TikTok 1080×1920px (opcional)

**Output:**
```
conteudo/carrosseis/[tema]/instagram/
  img-slide01.png
  slide-01.html → slide-01.png
  slide-02.html → slide-02.png
  ...
```

**Regras importantes:**
- Cada slide tem layout visual diferente (nunca repete template)
- Fonte nunca abaixo dos valores mínimos do DESIGN.md
- Texto em excesso: cortar parágrafo, nunca reduzir fonte
- Sem labels de seção, eyebrows ou badges de série nos slides

---

### `/estatico-unity`
**Arquivo:** `.claude/skills/estatico-unity/SKILL.md`

**Para que serve:** Produz um post estático (card único) — foto de fundo gerada por IA + copy + identidade visual, tudo montado em HTML e renderizado em PNG.

**Quando usar:** Quando o briefing define formato "imagem" ou você quer um post de alto impacto visual com texto mínimo.

**Fases:**
1. **Copy + prompt da foto** — extraídos do briefing ou fornecidos diretamente
2. **Foto de fundo** via GPT Image 2 (portrait 1024×1536)
3. **HTML** (1080×1350px) com foto + overlay + copy + logo → **PNG**

**Checkpoints:** após copy e prompt, após foto gerada, após post renderizado

**Regra crítica:** fundo de cor sólida é proibido. O post estático SEMPRE tem foto de fundo gerada por IA. Se a OpenAI falhar, tenta Gemini, depois FAL API. Só para se todos os três falharem.

**Output:**
```
conteudo/imagens/[tema]/
  foto-fundo.png
  prompt.txt
  post-01.html
  post-01.png          ← arquivo final para publicar
```

---

### `/roteiro-unity`
**Arquivo:** `.claude/skills/roteiro-unity/SKILL.md`

**Para que serve:** Produz roteiros de vídeo para Instagram Reels e TikTok.

**Quando usar:** Quando o briefing define formato "vídeo" ou você quer produzir conteúdo para Reels.

**Dois modos:**
- **Orgânico** (conteúdo de autoridade, educação, marca) → usa metodologia Ogilvy
- **Tráfego pago** (conversão, resposta direta) → usa metodologia Schwartz

**Output:** roteiro com duração por cena, narração, orientações de câmera e edição.

---

## Motores (usados internamente pelas skills)

### `/gpt-image2-unity`
**Arquivo:** `.claude/skills/gpt-image2-unity/SKILL.md`
**Script:** `.claude/skills/gpt-image2-unity/gerar-imagem.py`

**Para que serve:** Gera imagens usando o modelo `gpt-image-1` da OpenAI.

**Quando chamar diretamente:** quando precisar de uma imagem avulsa, fora do fluxo de carrossel ou post estático.

**Parâmetros do script:**
```powershell
python "gerar-imagem.py" "PROMPT_EM_INGLÊS" "CAMINHO_DE_SAÍDA.png" "ASPECT_RATIO"
```

**Aspect ratios:**
- `square` → 1024×1024 (Instagram feed quadrado)
- `portrait` → 1024×1536 (Instagram/TikTok vertical)
- `landscape` → 1536×1024 (LinkedIn banner)

**Leitura da API key:** o script procura em `credentials/openai_key.txt`. Se não encontrar, busca na variável de ambiente `OPENAI_API_KEY`.

**Exit codes:**
- `0` — sucesso
- `2` — API key não encontrada
- `4` — erro de API (quota, prompt inválido, etc.)

**Cadeia de fallback:**
```
GPT Image 2 (OpenAI) → nanobanana-unity (Gemini, grátis) → image-gen-unity (FAL API, pago)
```

**Custo aproximado:** $0,02–$0,10 por imagem (quality: high)

**Regras de prompt:**
- Sempre em inglês
- Incluir estilo fotográfico: `professional photography`, `architectural photography`
- Incluir: `no text overlay`, `no watermarks`, `no people` (a menos que o briefing peça)
- Nunca: obras com EPI incorreto, texto embutido na imagem, ilustrações genéricas

---

### `/ogilvy-copy`
**Arquivo:** `.claude/skills/ogilvy-copy/SKILL.md`

**Para que serve:** Motor de escrita baseado na metodologia de David Ogilvy. Usado para copy de marca, conteúdo orgânico, construção de autoridade.

**Princípios aplicados:**
- Pesquisa profunda antes de escrever
- Big idea que conecta produto e desejo humano
- Headlines informativas (não enigmáticas)
- Copy que vende sem parecer que está vendendo
- Foco no benefício real, não no produto em si

**Usado por:** `/roteiro-unity` (modo orgânico), `/briefing-unity`

---

### `/schwartz-copy`
**Arquivo:** `.claude/skills/schwartz-copy/SKILL.md`

**Para que serve:** Motor de escrita baseado na metodologia de Eugene Schwartz. Usado para copy de resposta direta, tráfego pago, conversão.

**Princípios aplicados:**
- Identificar o nível de consciência do cliente
- Mecanismo único que explica como o produto funciona
- Headlines que capturam a atenção no estado certo
- Copy que move o leitor pelo funil de decisão

**Usado por:** `/roteiro-unity` (modo tráfego pago), `/briefing-unity` (para conversão)

---

## Comandos do sistema

### `/syncar`
**Arquivo:** `.claude/commands/syncar.md`

**Para que serve:** Salva o estado atual do repositório no GitHub (git add + commit + push).

**Quando usar:**
- Ao final de uma sessão produtiva
- Antes de uma pausa longa
- Sempre que quiser garantir backup do conteúdo gerado

**O que faz:**
1. Verifica se o git está configurado
2. Identifica arquivos novos e modificados
3. Faz commit com mensagem descritiva
4. Faz push para o repositório remoto

---

### `/setup`
**Arquivo:** `.claude/commands/setup.md`

**Para que serve:** Configura o sistema para um novo negócio. Guia o preenchimento dos arquivos de contexto e do DESIGN.md através de uma entrevista estruturada.

**Quando usar:** na primeira vez que usar o repositório para um novo cliente, ou quando quiser reconfigurar completamente.

---

### `/mapear`
**Arquivo:** `.claude/commands/mapear.md`

**Para que serve:** Entrevista você sobre processos repetitivos e cria skills personalizadas.

**Quando usar:** quando identificar uma tarefa que faz frequentemente e quer automatizar com uma skill específica.

**Perguntas durante o /mapear:**
- Qual é a tarefa?
- Quantas vezes por semana/mês você faz isso?
- Quais são os passos?
- Qual é o output esperado?
- É específica desta empresa ou útil em qualquer projeto?

---

## Tabela resumo — skills por formato de conteúdo

| Formato | Skill principal | Motor de imagem | Motor de copy |
|---|---|---|---|
| Carrossel Instagram | `/carrossel-unity` | `gpt-image2-unity` | Direto na skill |
| Post estático | `/estatico-unity` | `gpt-image2-unity` | Direto na skill |
| Reel/TikTok orgânico | `/roteiro-unity` | — | `ogilvy-copy` |
| Reel/TikTok pago | `/roteiro-unity` | — | `schwartz-copy` |
| Imagem avulsa | `/gpt-image2-unity` | — | — |
| Calendário | `/calendario-comercial` | — | — |
| Briefing | `/briefing-unity` | — | `ogilvy-copy` ou `schwartz-copy` |

---

## Tabela resumo — skills por objetivo

| Objetivo | Skill |
|---|---|
| Mapear o mês estrategicamente | `/calendario-comercial` |
| Definir o que um post vai comunicar | `/briefing-unity` |
| Ensinar algo ao público | `/carrossel-unity` |
| Impacto visual rápido no feed | `/estatico-unity` |
| Conteúdo em vídeo (orgânico) | `/roteiro-unity` |
| Anúncio em vídeo (tráfego pago) | `/roteiro-unity` |
| Gerar uma foto avulsa | `/gpt-image2-unity` |
| Salvar o trabalho no GitHub | `/syncar` |
| Criar uma nova skill personalizada | `/mapear` |
