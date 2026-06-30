# CTAs padrão — slide final dos posts

Dois modelos fixos de CTA. **Não criar CTA novo por post.** Escolher um dos dois conforme o objetivo do conteúdo e usar a copy exatamente como está aqui.

| Modelo | Quando usar | Visual | PNG pronto |
|---|---|---|---|
| **CTA 1 — Conversão** | Post que vende: produto, linha específica, fundo de funil, quebra de objeção | Fundo Azul sólido (#4A61A0) | `post pronto/cta-01.png` |
| **CTA 2 — Salvamento** | Post que ensina: educativo, autoridade, topo de funil, técnico | Foto full-bleed + gradiente | `post pronto/cta-02.png` |

Regra de bolso: **post que vende → CTA 1. Post que ensina → CTA 2.**

---

## Copy fixa

### CTA 1 — Conversão / falar com especialista
- **Label:** PRÓXIMO PASSO
- **Headline:** Especificar a esquadria certa começa com uma conversa.
- **Corpo (32px):** Fale com quem domina as linhas de PVC e dimensiona cada vão do seu projeto.
- **Botão:** SOLICITE SEU ORÇAMENTO PELO DIRECT →
- **Linha de apoio:** Ou fale com um especialista no site — esquadrias.fastsistemasconstrutivos.com.br

### CTA 2 — Salvamento / referência
- **Label:** REFERÊNCIA TÉCNICA
- **Headline:** Quem especifica bem, guarda referência.
- **Corpo (32px):** Salve este post e tenha os dados do PVC de alto padrão à mão na hora de projetar.
- **Pill:** SALVE ESTE POST PARA CONSULTAR DEPOIS

---

## Como aplicar na produção

Os CTAs já estão **renderizados em PNG 1080×1350** em `post pronto/`. Não precisa montar nada por post:

1. Escolher o modelo pelo objetivo (vende → CTA 1, ensina → CTA 2).
2. Usar o PNG de `post pronto/` **como o último slide do carrossel** (ou como o post estático fechando a sequência). É só copiar o arquivo para a pasta `post pronto/` do conteúdo.

Pronto. A copy e o visual são fixos; não se reescreve CTA por post.

## Arquivos-fonte e re-render

O **repo versiona só os PNGs prontos** (`post pronto/cta-01.png` e `cta-02.png`) — é o que basta pra aplicar nos posts em qualquer máquina. Os arquivos-fonte (`.html` + foto de fundo `img-cta.png`) ficam **locais na máquina de origem, fora do git** (no `.gitignore`), pra manter o repo leve. Quem tiver os fontes localmente pode editar e re-renderizar; quem só clonou o repo usa os PNGs prontos como estão.

Os `.html` são os geradores dos PNGs. Caminhos relativos a `marca/ctas/` (logo em `../logos/logo-branco.png`, foto de fundo do CTA 2 em `./img-cta.png`). Para re-renderizar após editar um HTML (precisa dos fontes locais):

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
npx.cmd playwright screenshot --viewport-size=1080,1350 "file:///C:/Users/Clara Barbosa/Documents/Projetos_Claude/Design-ecoframe/marca/ctas/cta-01-especialista.html" "C:/Users/Clara Barbosa/Documents/Projetos_Claude/Design-ecoframe/marca/ctas/post pronto/cta-01.png"
```

Para trocar o fundo do CTA 2, substituir `img-cta.png` (priorizar foto real do Drive, alto padrão) e re-renderizar.

Sem travessão e sem vícios de IA na copy (regra de `_contexto/preferencias.md`).
