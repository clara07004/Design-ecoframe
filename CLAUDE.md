# Unity Content — Claude Code OS

## O que é esse workspace

> **Este projeto é uma base/template.** Não é executado diretamente aqui — projetos reais são replicados a partir deste. Credenciais, contexto (`_contexto/`) e outputs (`conteudo/`) ficam no projeto replicado, não aqui. Nunca tentar testar, executar scripts ou verificar configurações neste workspace.

Sistema de automação do processo de criação de conteúdo para redes sociais do Grupo Unity. Orquestra skills de IA para ir da definição estratégica até a entrega do pacote de conteúdo pronto para publicação.

**Empresa:** Ecoframe — Esquadrias em PVC de alta performance (Steel Frame, Drywall, arquitetura contemporânea).

**Estrutura de pastas:**
- `_contexto/` — memória do sistema (não apagar)
- `_testes/` — posts e carrosseis de referência (ver regra abaixo)
- `marca/` — DESIGN.md e identidade visual
- `dados/` — arquivos para análise (CSV, PDF, prints, referências)
- `templates/skills/` — templates de skills prontos pra personalizar com /mapear
- `templates/ferramentas/catalogo.md` — APIs e ferramentas disponíveis pra usar em skills
- `credentials/` — credenciais e tokens (não committar)

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (se existirem e estiverem configurados):

1. `_contexto/empresa.md` — quem é o usuário, o que faz, como funciona o negócio
2. `_contexto/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_contexto/estrategia.md` — foco atual, prioridades, o que pode esperar
4. `_contexto/referencias.md` — pastas do Google Drive com material de referência visual

Usar essas informações como base pra qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considerar o foco atual descrito em `estrategia.md`.

Para qualquer tarefa visual (carrossel, proposta, slide, landing page), consultar `marca/DESIGN.md` como referência de estilo.

**Referência de posts aprovados:** antes de criar qualquer carrossel ou post estático, listar os conteúdos em `_testes/` e abrir ao menos um exemplo do mesmo formato (carrossel → `_testes/carrosseis/`, post estático → `_testes/post-estatico/`). Ler o `.md` de briefing e abrir os PNGs para entender o padrão visual consolidado — paleta, tipografia, densidade de texto por slide, posicionamento de logo e CTA. Usar como referência obrigatória de design, não como template a copiar literalmente. O objetivo é manter consistência com o estilo visual já aprovado pela marca.

**Referências visuais do Drive:** quando `_contexto/referencias.md` tiver pastas configuradas, consultá-las antes de criar qualquer conteúdo visual. Usar o MCP do Google Drive para listar os arquivos da pasta relevante (`search_files` com `parentId = 'ID_DA_PASTA'`) e baixar as imagens com `download_file_content`. Priorizar imagens menores que 300KB para caber no contexto. Usar o material encontrado como referência de estilo, produto e padrão visual — não como template a copiar literalmente.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas usar o contexto naturalmente.

---

## Conhecimento técnico do produto (consulta obrigatória)

**Antes de gerar calendário, briefing, roteiro, carrossel ou post estático**, ler os arquivos relevantes em `produtos/`. Esse diretório consolida toda a documentação técnica oficial (catálogos, manuais, relatórios PSQ) da Primeira Linha e da Sincol.

A Ecoframe é uma marca de **alto padrão** com ticket alto — o conteúdo precisa:

- **Ser realista e verdadeiro:** nunca inventar dimensões, ensaios, classes de vento ou valores de isolação acústica. Tudo precisa estar lastreado em `produtos/`
- **Conter especificações técnicas reais:** citar linhas (iTEC / euroTEC / TECplus-100 / MAXXI), perfis (FC-55/75/100/130), normas (NBR 10821, EN 12608, NBR 15.575), valores ensaiados (Rw 32-36 dB, 1820 Pa de vento, soldabilidade 44-47 MPa)
- **Permitir que o cliente conheça o produto pelo post:** o conteúdo é parte da qualificação do lead, não decoração visual
- **Manter o posicionamento premium:** vocabulário técnico-arquitetônico, sem foco em preço, sem comparações genéricas sem lastro

Arquivos de consulta principais:
- `produtos/README.md` — índice de todos os tópicos
- `produtos/visao-geral.md` — características e vantagens do PVC
- `produtos/tipologias-aplicacoes.md` — janelas/portas com limites dimensionais por linha
- `produtos/normas-desempenho.md` — NBR + EN + classes de vento por região
- `produtos/linhas-perfis/linha-{itec,eurotec,tecplus100,maxxi}.md` — uma por linha técnica
- `produtos/perfis-acessorios-vidros.md` — códigos completos
- `produtos/instalacao-manutencao/relatorios-tecnicos.md` — resumo PSQ (Rw, Pa, ensaios)
- `produtos/certificacao-aqua.md` — AQUA/HQE para conteúdo de sustentabilidade
- `produtos/portas-sincol/` — coleções Sincol (Touch, Sincolors, Impressione, Sinkit, Kit Fogo)
- `produtos/fotos-obras/` — acervo visual real (priorizar sobre IA quando possível)

**Frases genéricas para revisar:** "qualidade superior", "máxima durabilidade", "tecnologia avançada" sem citar dado técnico = reescrever com número real do PSQ ou da norma.

---

## Skills disponíveis

**Skills do sistema CCOS (genéricas):**
- `/setup` — configura o sistema pro seu negócio (rodar na primeira vez)
- `/syncar` — salva o trabalho no GitHub (commit + push)
- `/mapear` — entrevista processos repetitivos e cria skills personalizadas

**Skills de conteúdo Unity:**
- `/calendario-comercial` — mapa de oportunidades do período (quando e o quê postar)
- `/briefing-unity` — briefing completo de um tema: objetivo, mensagem, formato, referências
- `/carrossel-unity` — produção de carrossel: texto + HTML + PNG via Playwright
- `/estatico-unity` — produção de post card único: foto IA + HTML + PNG via Playwright
- `/roteiro-unity` — roteiro de vídeo para Reels/TikTok (orgânico via Ogilvy, tráfego via Schwartz)
- `/publicar-social-unity` — publica conteúdo aprovado no Instagram, TikTok, LinkedIn
- `/triagem-youtube-unity` — análise editorial para YouTube

**Skills de pesquisa e ideação:**
- `/gerador-de-angulos-para-um-tema` — 10 lentes criativas para explorar um tema antes do briefing
- `/gerador-de-angulos-de-conteudo` — matrix perspectivas × audiência × formatos narrativos, 10 ângulos únicos
- `/banco-de-objecoes-do-avatar` — mapeia 6 tipos de objeção por ICP com resposta em conteúdo

**Skills de copy e distribuição:**
- `/hooks-para-carrossel` — 5 opções de capa para carrossel com direção visual (usar antes do /carrossel-unity)
- `/hooks-para-instagram-reels` — 7 tipos de hook combinados (primeiro frame + frase de abertura)
- `/legenda-para-carrossel` — legenda orientada a save com CTA específico
- `/legenda-para-reel` — legenda que complementa o vídeo sem repetir o script
- `/legenda-para-post-estatico` — 4 tipos de legenda para post estático
- `/carrossel-de-quebra-de-objecao` — carrossel de fundo de funil em 3 movimentos (nomeação → reframe → prova)
- `/1-conteudo-em-7-formatos` — repurposing: transforma 1 conteúdo em Reel, Carrossel, Story, Thread, LinkedIn, E-mail e Post estático

**Skills de imagem:**
- `/gerador-de-prompts-de-imagem` — prompt estruturado para gpt-image-1 (usar antes de gerar imagem)
- `/gerador-de-prompts-para-imagens-de-produto` — prompts para as 3 estéticas de produto da Ecoframe (dark_lifestyle, architectural_installation, product_closeup)

**Motores (usados internamente pelas skills de produção):**
- `/gpt-image2-unity` — gera foto de fundo via GPT Image 2 (motor de imagem do carrossel e post estático)
- `/nanobanana-unity` — fallback de imagem via Gemini (grátis)
- `/image-gen-unity` — contingência de imagem via FAL API (pago)
- `/ogilvy-copy` — copy de marca e conteúdo orgânico (motor do roteiro orgânico)
- `/schwartz-copy` — copy de resposta direta (motor do roteiro de tráfego pago)

---

## Fluxo principal de conteúdo

### Etapa 1 — Ideação e planejamento (sempre)

```
/gerador-de-angulos-para-um-tema   ← 10 lentes criativas para um tema
    ou
/gerador-de-angulos-de-conteudo    ← matrix perspectivas × audiência × formatos
    ↓ [escolhe ângulo]
/calendario-comercial              ← quando e o quê postar
    ↓ [aprova calendário]
/briefing-unity                    ← define objetivo, mensagem e formato
    ↓ [aprova briefing]
```

**REGRA OBRIGATÓRIA — Calendário de novo mês entrega SEMPRE 3 arquivos**

Toda vez que rodar `/calendario-comercial` para um mês (ou qualquer período fechado), gerar dentro de `conteudo/calendarios/[periodo]/`:

1. **`calendario-detalhado.md`** — post a post, numerado, com tema/formato/janela/status (alimenta os `/briefing-unity` posteriores)
2. **`_aprovado.md`** — memória da aprovação: tema narrativo, mix, apagões, picos, ajustes feitos, o que evitar
3. **`dashboard.html`** — grid visual do mês inteiro, derivado direto do `calendario-detalhado.md`, usando o template `templates/dashboard-calendario.html` (identidade visual da marca, canvas 1920×1080)

O dashboard **não é opcional** — é entrega obrigatória junto com o calendário, mesmo que o usuário não peça explicitamente. Após gerar o HTML, perguntar se renderiza o PNG via Playwright (esse passo sim é opcional).

A skill `/calendario-comercial` já tem a especificação completa na seção "8. ENTREGAS OBRIGATÓRIAS" — seguir literalmente.

---

### Etapa 2 — Produção (escolher o fluxo pelo formato)

**REGRA OBRIGATÓRIA — Confirmar o formato antes de produzir (exceto carrossel)**

Quando o conteúdo de um dia estiver marcado no calendário como **Reel, post estático, vídeo ou qualquer formato que NÃO seja carrossel**, SEMPRE perguntar ao usuário qual o formato do conteúdo antes de gerar qualquer coisa (hook, roteiro, briefing, prompt, imagem, HTML). Não assumir o formato do calendário automaticamente — ele é sugestão, a decisão final é do usuário. Quando o formato for **carrossel**, seguir direto o fluxo sem perguntar.

**REGRA OBRIGATÓRIA — Nomenclatura da pasta de produção pela DATA DE PUBLICAÇÃO**

A pasta de produção de cada conteúdo é nomeada pela **data de publicação** no formato `dia-DD-tema-curto` (ex.: conteúdo que publica em 17/07 → `dia-17-linhas-pvc-vao`). **Nunca usar o número do post do calendário** — em meses com domingos sem post ou apagões, o número do post deixa de coincidir com o dia do mês (ex.: Post 15 publica em 17/07). O `DD` é sempre o dia em que o conteúdo vai ao ar.

#### Carrossel

**FLUXO PRINCIPAL ★ — usar SEMPRE este, a menos que o usuário peça explicitamente outro.** Quando o calendário já existe, começa no `/briefing-unity` (não nos hooks):
```
/briefing-unity                  ← ponto de partida (calendário já aprovado)
    ↓ [aprova briefing]
/gerador-de-prompts-de-imagem    ← FLUXO PRINCIPAL ★ — prompts da capa + de cada slide
    ↓ [aprova os prompts]
/gpt-image2-unity                ← gera todas as imagens (capa + slides)
    ↓ [aprova as imagens]
/carrossel-unity                 ← monta os HTMLs + renderiza PNG
    ↓ [aprova]
/legenda-para-carrossel
    ↓ [aprova o conteúdo final]
/publicar-social-unity           ← publicação
```

**Fluxo rápido (alternativa) — só quando o usuário pedir, ou para algo pontual sem controle granular de imagem:** `/carrossel-unity` cuida de tudo internamente (texto + prompt + imagem IA + HTML + PNG):
```
/carrossel-unity        ← texto + geração de imagem + HTML + PNG (tudo em um)
    ↓
/legenda-para-carrossel
```

> `/hooks-para-carrossel` é skill **auxiliar opcional** — usar só quando o usuário quiser explorar opções de capa antes. Não é etapa do fluxo principal.

**Observação:** quando houver fotos reais de produto disponíveis no Google Drive (`_contexto/referencias.md` → pasta "Fotos do Produto"), priorizá-las em vez de gerar imagem IA. Buscar via MCP Drive (`search_files` na pasta `1yMl_zKBySogepmeM7WTyihTYuXZFuZb6`), baixar com `download_file_content`, extrair via Python e salvar como `img-slideXX.jpg` na pasta do carrossel. Resultado superior ao de qualquer geração IA.

---

#### Post estático

```
/gerador-de-prompts-para-imagens-de-produto   ← ou /gerador-de-prompts-de-imagem
    ↓ [aprova prompt]
/gpt-image2-unity                             ← gera foto de fundo
    ↓ [aprova imagem]
/estatico-unity                               ← monta HTML + renderiza PNG
    ↓
/legenda-para-post-estatico
```

---

#### Vídeo (Reels / TikTok)

```
/hooks-para-instagram-reels   ← hook do primeiro frame + frase de abertura
    ↓ [escolhe hook]
/roteiro-unity                ← roteiro completo (motor: ogilvy-copy ou schwartz-copy)
    ↓
/legenda-para-reel
```

---

### Etapa 3 — Distribuição (opcional)

```
/1-conteudo-em-7-formatos   ← transforma o conteúdo aprovado em 7 formatos diferentes
    ↓
/publicar-social-unity       ← publica no Instagram, TikTok, LinkedIn
```

---

### Fluxo alternativo — fundo de funil

```
/banco-de-objecoes-do-avatar      ← mapeia objeções por ICP
    ↓ [escolhe objeção]
/carrossel-de-quebra-de-objecao   ← carrossel em 3 movimentos: nomeação → reframe → prova
    ↓
/carrossel-unity  +  /legenda-para-carrossel
```

---

**Aprovação humana obrigatória** em cada etapa — o fluxo para e aguarda antes de avançar.

---

## Regras do sistema

- Antes de executar qualquer tarefa, verificar se existe uma skill relevante em `.claude/skills/`
- Se encontrar, seguir as instruções da skill
- Conteúdo da empresa: sempre manter o contexto da Ecoframe — esquadrias em PVC, premium técnico, Steel Frame e Drywall
- Arquivos de credenciais: nunca commitar (estão no .gitignore)

### Copy humanizada — banimento de vícios de linguagem de IA (regra absoluta)

Toda copy que vai ao público (legenda, slide de carrossel, post estático, roteiro, headline, CTA, e-mail) precisa soar escrita por uma pessoa. **Nunca usar travessão (— ou –) em copy**, e nunca usar os vícios de linguagem típicos de IA. A lista completa de termos, estruturas e maneirismos banidos, mais a orientação de como humanizar, está em `_contexto/preferencias.md` na seção "Banimento de vícios de linguagem de IA" — consultar e aplicar em qualquer skill de copy. Ao terminar uma copy, reler caçando esses itens; achou um, reescreve.

### Organização do output — subpasta "post pronto"

O PNG final renderizado de cada conteúdo (o arquivo que vai ser publicado) deve ficar isolado numa subpasta chamada **`post pronto`**, separado das imagens de fundo (`img-*.png`) e dos HTMLs. Isso vale para Instagram e facilita selecionar o arquivo certo na hora de publicar.

- **Carrossel** (`conteudo/carrosseis/[periodo]/[dia]/instagram/`): os `slide-XX.png` finais vão para `instagram/post pronto/`. As imagens de fundo (`img-slideXX.png`) e os HTMLs (`slide-XX.html`) continuam em `instagram/`.
- **Post estático** (`conteudo/post-estatico/[periodo]/[dia]/`): o `post-01.png` final (e variações como `post-01-story.png`) vai para `post pronto/` direto na pasta do dia. A foto de fundo (`img-post.png`), o HTML e o `prompt.txt` continuam na pasta do dia.
- **TikTok**: mantém a estrutura atual, sem subpasta `post pronto`.
- Os HTMLs referenciam as imagens de fundo por caminho relativo (`./img-slideXX.png`) e continuam na mesma pasta delas, então mover só o PNG final não quebra render nem logo. Render normalmente e, no fim, mover o PNG final para `post pronto/`.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe uma skill relevante em `.claude/skills/` ou `.claude/commands/`.
Se encontrar, seguir as instruções da skill.
Se não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível, perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o padrão de repetição for claro.

---

## Aprender com correções

Quando o usuário corrigir algo ou dar instrução permanente ("na verdade é assim", "não faça mais isso", "sempre que...", "evita..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde salvar:

- **Sobre o negócio** → `_contexto/empresa.md`
- **Sobre preferências e estilo** → `_contexto/preferencias.md`
- **Sobre prioridades e foco atual** → `_contexto/estrategia.md`
- **Regra de comportamento nessa pasta** → `CLAUDE.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro.

---

## Criação de skills

Quando o usuário pedir pra criar uma nova skill:

1. Verificar se existe um template relevante em `templates/skills/`
2. Perguntar: "Essa skill é específica pra esse projeto ou vai ser útil em qualquer projeto?"
   - Específica desse negócio → `.claude/skills/nome-da-skill/SKILL.md` (local)
   - Útil em qualquer projeto → `~/.claude/skills/nome-da-skill/SKILL.md` (global)
3. Ler `_contexto/empresa.md` e `_contexto/preferencias.md` pra calibrar o conteúdo ao contexto
4. Se a skill precisar de arquivos de apoio, criar dentro da pasta da skill
