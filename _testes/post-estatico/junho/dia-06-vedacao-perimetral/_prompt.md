# Prompt de Imagem — Dia 06 | Vedação Perimetral

## Configuração técnica
- **Modelo:** GPT Image 2 (gpt-image-1) via `gerar-imagem.py`
- **Proporção:** square (1024×1024) — post estático Instagram feed
- **Estética:** product_closeup — macro arquitetônico técnico
- **Status:** prompt pronto · aguardando comando explícito da Clara para executar

---

## Prompt principal (inglês — para GPT Image 2)

```
Architectural macro close-up of a high-performance white matte PVC window frame meeting a drywall and concrete perimeter wall, photographed from a tight three-quarter angle that reveals the construction interface in cross-section detail. The image shows the precise junction zone: the white PVC profile on the left, a galvanized steel sub-frame (contramarco) embedded behind it, a visible black butyl sealing tape compressing the gap, and the raw edge of the drywall and concrete substrate on the right. Soft natural side light from a window out of frame, slightly diffused, creates gentle shadows that emphasize the millimetric tolerance of the joint. The PVC surface shows its characteristic matte velvety finish. The metal accessories (corner bracket, fastener heads) are visible but discreet. Construction dust on the concrete is minimal but present — this is a real building site, not a studio render. Color palette restricted to off-white, warm concrete grey, drywall cream, and the muted dark of the butyl seal. Sharp focus on the sealing interface, very shallow depth of field falling off into the wall depth. Photographed with a 100mm macro lens, f/5.6, ISO 200, daylight balance. Editorial architectural photography style — Vitrocsa catalog, B&B Italia detail shots, Saint-Gobain technical brochure quality. No people, no logos visible on materials, no text overlays. Premium, technical, intentional. The frame is positioned in the upper-left two-thirds of the composition, leaving the lower third available for typographic overlay.
```

---

## Prompt de fallback (mais simples — nanobanana se GPT falhar)

```
Architectural macro photo: white matte PVC window frame meeting drywall and concrete wall, showing the construction interface with visible butyl sealing tape and steel sub-frame behind. Natural side light, sharp focus on the joint, shallow depth of field. Editorial premium quality, no people, no text. Composition leaves lower third clear for text overlay.
```

---

## Justificativa da escolha de prompt

**Por que product_closeup e não architectural_installation:**
O tema é o **detalhe que desaparece** quando a obra fica pronta. Foto de janela instalada em ambiente acabado (`architectural_installation`) esconde justamente o ponto que o post quer mostrar — a interface esquadria-alvenaria, a fita butílica, o contramarco. Close-up é o único enquadramento que torna o argumento visível.

**Por que IA e não Drive:**
O acervo do Drive (`1yMl_zKBySogepmeM7WTyihTYuXZFuZb6`, ~20 fotos) é majoritariamente ambiência de obra finalizada e fachada — não há macro de junção construtiva com fita butílica visível. Para esse tema específico, IA dá controle cirúrgico de enquadramento que foto de obra não daria. Fotos do Drive permanecem prioritárias para temas de **ambiência/produto instalado** (próximos posts).

**Composição com texto em mente:**
O prompt instrui explicitamente "leaving the lower third available for typographic overlay" — isso garante que a foto comporte o gradiente escuro na base + headline + body + spec bar + logo + tagline sem competir visualmente.

---

## Sequência de execução (quando aprovado)

```bash
python ".claude/skills/gpt-image2-unity/gerar-imagem.py" \
  --prompt "<prompt principal acima>" \
  --aspect-ratio square \
  --output "conteudo/post-estatico/junho/dia-06-vedacao-perimetral/img-post.png"
```

**Não executar até receber comando explícito da Clara.**
