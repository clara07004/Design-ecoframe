---
name: feedback-geracao-imagem
description: Nunca executar geração de imagem sem comando explícito — prompt e geração são etapas separadas
metadata:
  type: feedback
---

Nunca rodar o script de geração de imagem (gerar-imagem.py ou qualquer motor de imagem) sem que a usuária acione explicitamente um comando de geração (/gpt-image2-unity, /nanobanana-unity, /image-gen-unity ou instrução direta como "gera agora", "roda o script").

**Why:** A construção do prompt e a geração da imagem são etapas separadas. A usuária pode estar refinando o prompt antes de gerar. Executar antes da hora desperdiça crédito de API e quebra o fluxo de aprovação.

**How to apply:** Após gerar ou enriquecer um prompt, sempre parar e aguardar. Só executar o script quando houver comando explícito de geração.
