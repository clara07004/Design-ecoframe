# Unity Content — Claude Code OS

## O que é esse workspace

Sistema de automação do processo de criação de conteúdo para redes sociais do Grupo Unity. Orquestra skills de IA para ir da definição estratégica até a entrega do pacote de conteúdo pronto para publicação.

**Empresa piloto:** Construção a seco (drywall / steel frame).

**Estrutura de pastas:**
- `_contexto/` — memória do sistema (não apagar)
- `marca/` — design-guide e identidade visual
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

Usar essas informações como base pra qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considerar o foco atual descrito em `estrategia.md`.

Para qualquer tarefa visual (carrossel, proposta, slide, landing page), consultar `marca/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas usar o contexto naturalmente.

---

## Skills disponíveis

**Skills do sistema CCOS (genéricas):**
- `/iniciar` — carrega o contexto do negócio no começo de cada sessão
- `/setup` — configura o sistema pro seu negócio (rodar na primeira vez)
- `/syncar` — salva o trabalho no GitHub (commit + push)
- `/mapear` — entrevista processos repetitivos e cria skills personalizadas

**Skills de conteúdo Unity:**
- `/briefing-unity` — gera briefing completo a partir do calendario-comercial + contexto da marca
- `/carrossel-unity` — gera carrossel HTML → PNG via Playwright (Instagram/TikTok)
- `/gpt-image2-unity` — geração de imagem via GPT Image 2 (OAuth ChatGPT, sem custo extra)
- `/nanobanana-unity` — geração de imagem via Gemini (grátis, fallback)
- `/image-gen-unity` — geração de imagem via FAL API (pago, contingência)
- `/publicar-social-unity` — publica em Instagram, TikTok, LinkedIn
- `/triagem-youtube-unity` — análise editorial para YouTube

**Skills genéricas instaladas:**
- `/copywriting` — copy de marketing para qualquer página
- `/brainstorming` — exploração criativa antes de implementar
- `/frontend-design` — interfaces web de alta qualidade
- `/landing-page-design` — landing pages otimizadas para conversão
- `/ai-seo` — otimização para IA e motores de busca
- `/ads` — auditoria e otimização de campanhas pagas
- `/adversarial-review` — revisão crítica cross-model

---

## Fluxo principal de conteúdo

```
/calendario → [aprova] → /briefing-unity → [aprova] → /carrossel-unity
                                                      → /gpt-image2-unity (→ /nanobanana → /image-gen)
                                                      → /roteiro-unity (V1)
                                          → [aprova] → /publicar-social-unity
```

**Aprovação humana obrigatória** em cada etapa crítica — o fluxo para e aguarda antes de avançar.

---

## Regras do sistema

- Antes de executar qualquer tarefa, verificar se existe uma skill relevante em `.claude/skills/`
- Se encontrar, seguir as instruções da skill
- Conteúdo da empresa piloto: sempre manter o contexto de drywall/steel frame
- Arquivos de credenciais: nunca commitar (estão no .gitignore)

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
