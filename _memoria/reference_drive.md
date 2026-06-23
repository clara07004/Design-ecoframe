---
name: reference-drive-ecoframe
description: "IDs das pastas do Google Drive da Ecoframe — material base, logos, fotos de produto, catálogos técnicos, referências visuais e PDFs específicos por linha de produto"
metadata:
  type: reference
---

# Google Drive — Estrutura de Pastas Ecoframe

**Pasta raiz:** `0AMsBWrb3TtHBUk9PVA`
https://drive.google.com/drive/u/1/folders/0AMsBWrb3TtHBUk9PVA

## Material Base (Primeira Linha) — ⭐ pasta crítica
**ID:** `19qRG_eTIuj65_XCjVfwGurYsRMlXH5h2`
Contém duas subpastas: **Fotos** e **Catálogo**.

Toda a documentação técnica da fabricante Primeira Linha (esquadrias em PVC) e da parceira Sincol (portas de madeira) está organizada aqui. Foi processada e consolidada em `produtos/` no repositório local — usar essa pasta como fonte ao invés de re-ler os PDFs.

## Identidade Visual
**ID:** `1SQnjs_fX7KzzGlch9B4KB1SO2xcm3C6y`
Logos PNG (Asset 23-29, ecoframe 7-10), Manual de Marca PDF.

Manual de Marca PDF: ID `1IXVW6bXfz-qoNooWMti9bvajVOMiwUrf`

Subpasta Manual de Marca: `1la7OG8bnOXpBxnxWIQ_E5n909inrKPrj`

## Fotos do Produto (obras reais)
**ID:** `1yMl_zKBySogepmeM7WTyihTYuXZFuZb6`
**23 fotos JPEG** (79KB–551KB) na pasta principal — fachadas brancas e pretas, mansões, cartela de cores Lechler. Subpasta **"LeAnge - Mar"** (ID `1_CrvL9sxza0gUG18hP0uegOS9p__2wDb`) com **90 fotos HEIC** (1,5–4MB cada) do projeto cliente. Está dentro de Material Base.

**Importante:** inventário completo com IDs e classificação em `produtos/fotos-obras/README.md` e `produtos/fotos-obras/leange-mar/inventario.md`. **8 amostras JPEG** já baixadas e disponíveis em `produtos/fotos-obras/amostras-jpeg/` para uso direto. Fotos HEIC precisam de conversão antes do uso (não exibem em Windows nativamente).

## Catálogo Técnico (subpasta de Material Base)
**ID:** `19dBEQLjpSNZiGVrumPi891fcj_fUcekQ`

### PDFs Primeira Linha (esquadrias em PVC)
- `Catálogo TECNICO - 2022.pdf` — ID `1Jly1koMxixFJD2QQfL2RYTZEPX0SlypG`
- `Cataogo Comercial - 2022.pdf` — ID `16KVf_dcTJfFepacFDUilB642MYaUu96J`
- `Apresentação 1ª Linha.pdf` — ID `1R7y4R7GyB_k2jKGOJPI4wdfnxUvzeiQv`
- `COMO USAR A LINHA CERTA.pdf` — ID `1G-aJFVmSdfxMSe7TKgUQ7QnJKJZ0-JuY`
- `MANUAL DE INSTALAÇÃO 2022.pdf` — ID `13rGvZoSOl86IlMiJvmTdbTyVaG7nWvjF`
- `Orientações Gerais - Limpeza rev-4.pdf` — ID `1DS_kHhrCwppSTk4mSIF1kkxnn1baOiMd`
- `PROCESSO AQUA.pdf` — ID `1NnRg7N6XZDY234fJVfve7cqe9izHcUIK`
- `RELATORIO TÉCNICO euroTEC.pdf` — ID `1mSn8Ayat3YIjzmr1B_ZbDUz2kGTLo08e` (PSQ)
- `RELATORIO TÉCNICO TECplus100.pdf` — ID `1Br9Uf1b8wUJ9Va8TNazsHfNUuPznPrky` (PSQ)

### PDFs Sincol (portas de madeira — parceira)
- `manual_sinkit.pdf` — ID `1ZXk7v6XoTBYr_rpx5uKUn-qZk_pqWj24`
- `Catalogo_Oficial_Sincol_2026.pdf` — ID `1hao8tmnl5cugf_6k_9StttKgWox5cJoP` (54MB — não legível via API, baixar e abrir manualmente)
- `Sincol_KitResistenteaoFogo_REV1.pdf` — ID `1-b92SeF0VAas9kSlHPAki_GBjAN50lU8`
- `Impressione_30102025_REV00.pdf` — ID `196GhacLptoTkMzVOWkTwGJKZ2oE7aIBu`
- `ColecaoTouch_Comercial_01102025_REV00.pdf` — ID `1D-zDdBbhISP_5gCyifK0sWw2YT-TfSjE`
- `colecao-sincolors.pdf` — ID `1aueBXhdnmGuxHCCzluHiX8yd-keQ-iFM`
- `LinhaGourmet2022.pdf` — ID `1IbBP_YlSdoXUAuA8uykaeLjq4XdEY0rH`

## Referências de Estilo (Ecophon France)
**ID:** `1alyGkuiSZAzhpfE6s1QKNEduzYi1V073`
Posts Instagram da Ecophon France — ambientes arquitetônicos clean, foco em desempenho acústico. Usar como referência de estilo visual, não de produto.

---

## Importante: produtos/ no repositório

A pasta `produtos/` no repositório foi criada a partir desses PDFs e contém especificações consolidadas em Markdown. **Antes de ler os PDFs diretamente**, consultar:

- `produtos/README.md` — índice geral
- `produtos/visao-geral.md` — sobre o produto
- `produtos/linhas-perfis/linha-{itec,eurotec,tecplus100,maxxi}.md` — uma por linha
- `produtos/tipologias-aplicacoes.md` — tipologias com limites dimensionais
- `produtos/normas-desempenho.md` — NBR e EN, classes de vento, isolação
- `produtos/perfis-acessorios-vidros.md` — códigos completos
- `produtos/instalacao-manutencao/{manual-instalacao,limpeza-manutencao,relatorios-tecnicos}.md`
- `produtos/certificacao-aqua.md` — selos AQUA/HQE
- `produtos/portas-sincol/` — coleções Sincol
