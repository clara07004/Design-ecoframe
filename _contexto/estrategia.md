# Estratégia — Unity Content

**Foco atual:** MVP — conectar as peças que já existem

**Prioridade imediata:**
- Construir a skill `briefing-unity` (conecta calendario-comercial + contexto CCOS)
- Implementar gates de aprovação conversacionais no fluxo
- Validar com 10 conteúdos produzidos pelo fluxo completo

**Fluxo MVP:**
```
/calendario → [aprova] → /briefing-unity → [aprova] → /carrossel-unity ou /gpt-image2-unity → [aprova] → /publicar-social-unity
```

**Métricas de validação do MVP:**
- Tempo total por conteúdo vs. processo anterior
- Taxa de aprovação sem ajuste
- Qualidade percebida

---

## Instalação das skills (ordem de fluxo)

```
/calendario → /briefing-unity → /schwartz-copy + /ogilvy-copy → /carrossel ou /gpt-image2 → /publicar-social
```

| # | Skill | Origem | Status |
|---|---|---|---|
| 1 | `calendario-comercial` | Local (modelo-cliente) | ✅ Instalada |
| ✅ | `briefing-unity` | Criada neste projeto | ✅ Instalada |
| 2a | `schwartz-copy` | github.com/duduesh/schwartz-copy | 🔜 Próxima |
| 2b | `ogilvy-copy` | github.com/duduesh/ogilvy-copy | 🔜 Próxima |
| 3a | `carrossel-unity` | github.com/duduesh/carrossel-ratos | 🔜 Antes da 1ª run |
| 3b | `gpt-image2-unity` | github.com/duduesh/gpt-image2-ratos | 🔜 Antes da 1ª run |
| 3c | `nanobanana-unity` | github.com/duduesh/nanobanana-ratos | 🔜 Fallback |
| 3d | `image-gen-unity` | github.com/duduesh/image-gen-ratos | 🔜 Contingência |
| 4 | `publicar-social-unity` | github.com/duduesh/publicar-social-ratos | 🔜 Quando chegar na publicação |
| V1 | `triagem-youtube-unity` | github.com/duduesh/triagem-youtube-ratos | 🔜 V1 |

---

**Próximos passos (V1):**
- Deploy em n8n Cloud ou VPS (acesso remoto para o time)
- Integração com a biblioteca técnica via Supabase RAG
- Skill `roteiro-unity` para conteúdo em vídeo

---

<!-- Atualizar conforme o projeto evolui. -->
