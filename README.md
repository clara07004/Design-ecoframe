# Design Ecoframe — Sistema de Conteúdo

Workspace de automação do processo de criação de conteúdo para redes sociais da **Ecoframe**, rodando sobre Claude Code OS (CCOS). Orquestra skills de IA para ir da definição estratégica do tema até a entrega do pacote de conteúdo pronto para publicação — calendário, briefing, copy, imagem, carrossel/post/vídeo e publicação.

**Objetivo:** reduzir o tempo entre "temos algo para comunicar" e "post aprovado pronto para publicar", mantendo qualidade editorial, lastro técnico e consistência visual de marca.

---

## A Ecoframe

Fabricação e venda consultiva de **esquadrias em PVC de alta performance** para projetos em Steel Frame, Drywall e arquitetura contemporânea. Foco em conforto termoacústico, eficiência energética, durabilidade, baixa manutenção e acabamento superior.

- **Posicionamento:** premium técnico — desempenho aplicado à arquitetura contemporânea. Não é marca popular nem grife artificial.
- **Modelo de negócio:** venda consultiva por orçamento (sem e-commerce, sem preço exposto). Lead entra por formulário, WhatsApp ou comercial.
- **Fornecedor de perfis:** Primeira Linha — linhas **iTEC, euroTEC, TECplus100 e MAXXI**. Portas em parceria com a Sincol.
- **ICP:** (1) arquitetos e especificadores, (2) construtores de Steel Frame / Drywall, (3) proprietários de imóveis de alto padrão.

Contexto completo do negócio em [_contexto/empresa.md](_contexto/empresa.md), [_contexto/estrategia.md](_contexto/estrategia.md) e [_contexto/preferencias.md](_contexto/preferencias.md).

### Tom de voz

Técnico, elegante, seguro e consultivo. Premium técnico, levemente formal, técnico acessível. **Nunca** disputar por preço/custo-benefício, nem prometer desempenho absoluto sem laudo. Comparativo com alumínio sempre consultivo, nunca agressivo. Detalhes em [_contexto/preferencias.md](_contexto/preferencias.md).

### Lastro técnico obrigatório

Por ser marca de ticket alto, o conteúdo precisa ser **verdadeiro e específico**: citar linhas, perfis (FC-55/75/100/130), normas (NBR 10821, EN 12608, NBR 15.575) e valores ensaiados (Rw 32–36 dB, vento 1820 Pa, soldabilidade 44–47 MPa). Nada de "qualidade superior" genérico. Toda especificação sai de [produtos/](produtos/) — ver índice em [produtos/README.md](produtos/README.md).

---

## Estrutura do repositório

```
Design-ecoframe/
├── CLAUDE.md                  ← instruções operacionais do agente (ler primeiro)
├── _contexto/                 ← memória do negócio (empresa, estratégia, preferências, referências)
├── _memoria/                  ← memória portátil do agente (sincronizada via instalar-memoria.ps1)
├── _testes/                   ← posts e carrosseis aprovados, referência obrigatória de design
│   ├── carrosseis/
│   └── post-estatico/
├── marca/                     ← DESIGN.md (identidade visual) + logos
├── produtos/                  ← documentação técnica oficial (catálogos, manuais, PSQ)
│   ├── linhas-perfis/         ← uma por linha (iTEC, euroTEC, TECplus100, MAXXI)
│   ├── portas-sincol/         ← coleções Sincol
│   ├── fotos-obras/           ← acervo visual real (priorizar sobre IA)
│   └── ...                    ← normas, tipologias, certificação AQUA, etc.
├── dados/                     ← arquivos para análise (CSV, PDF, prints, referências)
├── templates/                 ← templates de skills, ferramentas, dashboard de calendário
├── conteudo/                  ← OUTPUT: calendários e carrosseis produzidos
│   ├── calendarios/
│   └── carrosseis/
├── manual-de-uso/             ← guia de uso passo a passo (começar por LEIA-PRIMEIRO.md)
├── credentials/               ← credenciais e tokens (NÃO committar)
├── .env.example               ← modelo de variáveis de ambiente
└── .claude/                   ← skills, comandos, agentes e settings
    ├── skills/                ← 21 skills de conteúdo
    ├── commands/              ← comandos do sistema (setup, syncar, mapear, atualizar, agente)
    └── agents/                ← designer-ecoframe (diretor de arte)
```

---

## Configuração inicial

1. **Credenciais** — copie o modelo e preencha:
   ```bash
   cp .env.example .env
   ```
   A chave da OpenAI também é lida de `credentials/openai_key.txt`.

| Variável / Arquivo | Serviço | Notas |
|---|---|---|
| `credentials/openai_key.txt` | OpenAI API | usada pelo `gpt-image2-unity` e `carrossel-unity` |
| `GEMINI_API_KEY` | Google Gemini | grátis — fallback de imagem (`nanobanana-unity`) |
| `META_APP_ID` / `META_APP_SECRET` | Meta / Facebook | [developers.facebook.com](https://developers.facebook.com) |
| `META_ACCESS_TOKEN` | Meta Graph API | ⚠️ expira em 60 dias — renovar no Graph API Explorer |
| `IMGBB_API_KEY` | imgbb | hospedagem de imagens para publicação no Instagram |
| `FAL_KEY` | FAL API | pago — contingência de imagem (`image-gen-unity`) |

2. **MCPs conectados:** Google Drive (referências visuais e fotos reais), Canva, Notion, Slack, Microsoft Learn.

3. **Memória portátil:** ao clonar em outra máquina, rode `instalar-memoria.ps1` para restaurar a memória do agente.

Passo a passo detalhado em [manual-de-uso/02-configuracao-inicial.md](manual-de-uso/02-configuracao-inicial.md).

---

## Fluxo principal de conteúdo

**Aprovação humana obrigatória em cada etapa** — o fluxo para e aguarda antes de avançar.

### Etapa 1 — Ideação e planejamento

```
/gerador-de-angulos-para-um-tema   (10 lentes criativas)
  ou /gerador-de-angulos-de-conteudo (matriz perspectiva × audiência × formato)
        ↓ [escolhe ângulo]
/calendario-comercial              quando e o quê postar
        ↓ [aprova calendário]
/briefing-unity                    objetivo, mensagem, formato, referências
        ↓ [aprova briefing]
```

> **Calendário de novo mês entrega SEMPRE 3 arquivos** em `conteudo/calendarios/[periodo]/`: `calendario-detalhado.md`, `_aprovado.md` e `dashboard.html` (grid visual derivado do template, identidade da marca). O dashboard não é opcional.

### Etapa 2 — Produção

**Carrossel** (fluxo principal — começa no briefing quando o calendário já existe):
```
/briefing-unity → /gerador-de-prompts-de-imagem → /gpt-image2-unity
  → /carrossel-unity → /legenda-para-carrossel → /publicar-social-unity
```

**Post estático:**
```
/gerador-de-prompts-para-imagens-de-produto → /gpt-image2-unity
  → /estatico-unity → /legenda-para-post-estatico
```

**Vídeo (Reels / TikTok):**
```
/hooks-para-instagram-reels → /roteiro-unity → /legenda-para-reel
```

**Fundo de funil:**
```
/banco-de-objecoes-do-avatar → /carrossel-de-quebra-de-objecao
  → /carrossel-unity + /legenda-para-carrossel
```

### Etapa 3 — Distribuição (opcional)
```
/1-conteudo-em-7-formatos → /publicar-social-unity
```

**Regras de produção:**
- **Confirmar o formato antes de produzir** (exceto carrossel) — o calendário é sugestão, a decisão é do usuário.
- **Pasta nomeada pela DATA DE PUBLICAÇÃO:** `dia-DD-tema-curto` (ex.: publica em 17/07 → `dia-17-linhas-pvc-vao`). Nunca usar o número do post.
- **Referência de design:** antes de qualquer carrossel/post, abrir um exemplo aprovado em [_testes/](_testes/) e consultar [marca/DESIGN.md](marca/DESIGN.md). Quando houver foto real no Drive, priorizar sobre imagem IA.

Fluxo completo em [manual-de-uso/03-fluxo-completo.md](manual-de-uso/03-fluxo-completo.md).

---

## Skills instaladas

### Sistema CCOS (comandos)
| Comando | O que faz |
|---|---|
| `/setup` | configura o sistema pro negócio (primeira vez) |
| `/syncar` | salva o trabalho no GitHub (commit + push) |
| `/atualizar` | baixa as mudanças do GitHub (git pull) |
| `/mapear` | entrevista processos repetitivos e cria skills personalizadas |
| `/agente` | convoca o agente designer-ecoframe para direção criativa |

### Ideação e pesquisa
| Skill | O que faz |
|---|---|
| `/gerador-de-angulos-para-um-tema` | 10 lentes criativas para um tema |
| `/gerador-de-angulos-de-conteudo` | matriz perspectiva × audiência × formato → 10 ângulos |
| `/banco-de-objecoes-do-avatar` | objeções por ICP com resposta em conteúdo |
| `/calendario-comercial` | mapa de oportunidades do período |
| `/briefing-unity` | briefing completo: objetivo, mensagem, formato, referências |

### Copy e distribuição
| Skill | O que faz |
|---|---|
| `/hooks-para-carrossel` | 5 opções de capa para carrossel |
| `/hooks-para-instagram-reels` | 7 tipos de hook (primeiro frame + frase) |
| `/legenda-para-carrossel` · `/legenda-para-reel` · `/legenda-para-post-estatico` | legendas por formato |
| `/carrossel-de-quebra-de-objecao` | carrossel de fundo de funil (nomeação → reframe → prova) |
| `/1-conteudo-em-7-formatos` | repurposing: 1 conteúdo → 7 formatos |

### Produção de assets
| Skill | O que faz |
|---|---|
| `/carrossel-unity` | carrossel completo: texto + HTML + PNG via Playwright |
| `/estatico-unity` | post card único: foto IA + HTML + PNG |
| `/roteiro-unity` | roteiro de vídeo Reels/TikTok |
| `/gerador-de-prompts-de-imagem` | prompt estruturado para gpt-image-1 |
| `/gerador-de-prompts-para-imagens-de-produto` | prompts para as 3 estéticas de produto Ecoframe |
| `/publicar-social-unity` | publica no Instagram via Meta Graph API |

### Motores (uso interno das skills)
| Motor | O que faz |
|---|---|
| `/gpt-image2-unity` | imagem via GPT Image 2 (OpenAI) — padrão |
| `/nanobanana-unity` | fallback de imagem via Gemini (grátis) |
| `/image-gen-unity` | contingência de imagem via FAL (pago) |
| `/ogilvy-copy` | copy de marca / orgânico (motor do roteiro orgânico) |
| `/schwartz-copy` | copy de resposta direta (motor do roteiro de tráfego) |

### Agente
| Agente | O que faz |
|---|---|
| `designer-ecoframe` | diretor de design e arte — direção criativa, revisão de carrossel/post, escolha de ângulo visual e coordenação do fluxo de produção. Convocar via `/agente` ou "preciso do designer". |

---

## Publicação

- **Plataforma principal:** Instagram. **Frequência:** 6x/semana (terça a domingo; segunda sem post).
- **Fins de semana:** sábado e domingo via agendamento (`--agendar`), não manualmente.
- Publicação via `/publicar-social-unity` (Meta Graph API) — **exige aprovação humana explícita; nunca publica automaticamente.**

---

## Referências visuais (Google Drive)

Quando uma tarefa visual exigir, consultar as pastas configuradas em [_contexto/referencias.md](_contexto/referencias.md) via MCP Google Drive:
- **Identidade Visual** — logos, assets, Manual de Marca
- **Fotos do Produto** — ~20 imagens de obra real (priorizar sobre IA)
- **Catálogo Técnico** — documentação Primeira Linha (linhas, laudos PSQ, AQUA)
- **Referência de estilo** — @ecophon_brasil (mesma categoria construtiva, mesmo público premium)

---

## Multi-empresa

Este workspace é a base de conteúdo da Ecoframe dentro do Grupo Unity. Cada empresa opera com workspace CCOS independente — repositório, contexto, credenciais e histórico isolados. O CLAUDE.md trata este projeto como **base/template**: não executar scripts nem testar configurações aqui — projetos reais são replicados a partir dele.

---

## Documentação

- [CLAUDE.md](CLAUDE.md) — instruções operacionais completas do agente
- [manual-de-uso/](manual-de-uso/) — guia passo a passo (começar por [LEIA-PRIMEIRO.md](manual-de-uso/LEIA-PRIMEIRO.md))
- [produtos/README.md](produtos/README.md) — índice da documentação técnica
- [marca/DESIGN.md](marca/DESIGN.md) — identidade visual e especificação de design
