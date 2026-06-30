---
name: post-pronto-subpasta-pngs
description: "O PNG final renderizado de cada conteúdo vai numa subpasta 'post pronto', separado das imagens de fundo e dos HTMLs, pra facilitar a seleção do arquivo de publicar."
metadata:
  type: feedback
---

O PNG final renderizado (o arquivo que será publicado) fica isolado numa subpasta chamada **`post pronto`**, separado das imagens de fundo (`img-*.png`) e dos HTMLs.

- **Carrossel** (`conteudo/carrosseis/[periodo]/[dia]/instagram/`): os `slide-XX.png` finais vão para `instagram/post pronto/`. Fundos (`img-slideXX.png`) e HTMLs (`slide-XX.html`) ficam em `instagram/`.
- **Post estático** (`conteudo/post-estatico/[periodo]/[dia]/`): o `post-01.png` (e variações como `post-01-story.png`) vai para `post pronto/` direto na pasta do dia. Foto (`img-post.png`), HTML e `prompt.txt` ficam na pasta do dia.
- **TikTok:** mantém a estrutura atual, sem subpasta `post pronto`.

**Why:** a Clara pediu (2026-06-30) porque tudo ficava misturado na pasta `instagram/` (fundos + HTMLs + PNG final), e selecionar só o PNG de publicar era chato.

**How to apply:** renderizar o screenshot já gravando o PNG final em `post pronto/` — o destino do screenshot é independente da pasta do HTML, e o HTML referencia o fundo por caminho relativo (`./img-slideXX.png`), então não quebra fundo nem logo. A validação de dimensão (`validar-dimensao.py`) roda sobre o PNG em `post pronto/`; a de overflow (`validar-overflow.js`) continua sobre os HTMLs em `instagram/`. A publicação aponta `--pasta .../instagram/post pronto/` (carrossel) e `--imagem .../post pronto/post-01.png` (estático). Registrado no CLAUDE.md e nas skills /carrossel-unity, /estatico-unity e /publicar-social-unity.

Relacionado: [[feedback-briefing-estrutura-pastas]], [[nomenclatura-pasta-por-data-publicacao]], [[validar-overflow-antes-de-publicar]]
