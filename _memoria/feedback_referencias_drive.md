---
name: feedback-referencias-drive
description: "Comportamento obrigatório no início de cada criação — ler arquivos do projeto, Drive e memória antes de qualquer produção visual"
metadata:
  type: feedback
---

Ao iniciar qualquer criação de conteúdo (briefing, carrossel, post estático, reel), seguir essa sequência obrigatória antes de produzir qualquer asset:

1. Ler `_contexto/empresa.md`, `_contexto/preferencias.md`, `_contexto/estrategia.md`
2. Ler `_contexto/referencias.md` para identificar as pastas do Drive relevantes
3. Acessar o Drive via MCP (`search_files` com o `parentId` da pasta correspondente) — especialmente "Fotos do Produto" (`1yMl_zKBySogepmeM7WTyihTYuXZFuZb6`) para referências visuais reais
4. Baixar imagens de referência com `download_file_content` (priorizar abaixo de 300KB)
5. Ler `marca/DESIGN.md` para identidade visual
6. Consultar a memória de designs aprovados ([[feedback-carousel-design-aprovado]]) para manter consistência visual

**Why:** A identidade visual da Ecoframe é construída com consistência entre posts. Usar referências reais do Drive e manter o padrão de design aprovado faz com que o estilo seja imediatamente reconhecível.

**How to apply:** Nunca pular essa etapa. Mesmo que o contexto pareça suficiente, verificar Drive e memória garante que referências visuais atualizadas sejam usadas.

Relacionado: [[reference-drive]], [[feedback-carousel-design-aprovado]]
