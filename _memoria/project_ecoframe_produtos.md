---
name: project-ecoframe-produtos
description: "Conhecimento técnico consolidado dos produtos Ecoframe — 4 linhas de esquadrias em PVC (iTEC, euroTEC, TECplus-100, MAXXI) + portas de madeira Sincol (parceira). Sempre consultar produtos/ no repositório antes de criar conteúdo técnico."
metadata:
  type: project
---

# Produtos Ecoframe — Visão Consolidada

A Ecoframe comercializa esquadrias em PVC fabricadas pela **Primeira Linha Ind. Com. Imp. Esquadrias em uPVC Ltda** (Itapevi/SP, fundada em 2002) e portas de madeira da **Sincol S/A** (Caçador/SC). Material base oficial está em `produtos/` no repositório local.

**Por que:** roteiros, calendários, briefings e qualquer conteúdo técnico precisam refletir os dados certos das linhas, tipologias e desempenho — não inventar valores.

**Como aplicar:** sempre que mencionar nome de linha, dimensão máxima, perfil, isolação acústica, classe de vento, ou outro dado técnico de produto, conferir em `produtos/`. Em dúvida sobre qual arquivo, começar pelo `produtos/README.md`.

## As 4 linhas de esquadrias em PVC

| Linha | Posicionamento | Folha de correr | Largura×Altura máx (correr 2 folhas) | Tipologias possíveis |
|---|---|---|---|---|
| **iTEC** | Leve | FC-55 (37×55mm) | 2.400×1.600mm | Correr, maximar |
| **euroTEC** | Intermediário (mais versátil) | FC-75 (37×75mm) | 2.400×2.300mm | Tudo — correr, abrir, oscilobatente, maximar, guilhotina, fixo |
| **TECplus-100** | Pesado | FC-100 (42×100mm) | 3.600×2.600mm | Correr, abrir e oscilobatente pesados, guilhotina motorizada |
| **MAXXI** | Extra pesado | FC-130 (50×84mm) | 5.000×3.200mm | Correr de grandes vãos especiais |

## Desempenho documentado (PSQ)

Janela de correr 2 folhas 1.600×1.600mm — euroTEC e TECplus100:

- **Estanqueidade à água:** patamar máximo — todas regiões I-V até 30 pavimentos
- **Cargas distribuídas (vento):** sem falha até 1.820 Pa ensaio / 2.730 Pa segurança
- **Isolação sonora (Rw):** 32 dB (sem persiana 4mm) / 34 dB (com persiana 4mm) / 36 dB (com persiana 8mm)
- **Soldabilidade dos cantos:** 44–47 MPa (exigido ≥35 MPa)
- **Composto PVC:** atende EN 12608:2003 — chumbo ≤0,10%, Vicat ≥75°C

## Garantia
- Perfis: **10 anos** | Acessórios: **5 anos** | Vida útil esperada: **>40 anos**

## Mercado e identidade
- 40.000+ fornecimentos concluídos
- Foco: residencial médio/alto padrão, hotelaria, hospitalar
- Equipes próprias de instalação treinadas

## Portas Sincol — parceira
Certificada ABNT N° 352.013/22 (NBR 15530-2:2018 + NBR 15530-3:2023). Coleções: Touch, Sincolors, Impressione, Gourmet. Produtos: Sinkit (kit pronto), Kit Resistente ao Fogo (Classe 1 / 30 min).

## Quando usar
- Conteúdo técnico sobre estanqueidade, vento, acústica → `produtos/normas-desempenho.md`
- Briefing sobre uma linha específica → `produtos/linhas-perfis/linha-{nome}.md`
- Roteiro sobre tipologia (oscilobatente, maximar, guilhotina) → `produtos/tipologias-aplicacoes.md`
- Conteúdo de sustentabilidade → `produtos/certificacao-aqua.md`
- Conteúdo sobre portas → `produtos/portas-sincol/`
