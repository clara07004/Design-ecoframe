import json, base64, re, os

# Ler o JSONL da sessão atual para encontrar o base64 dos logos
jsonl_path = r"C:\Users\clara\.claude\projects\C--Users-clara-Documents-Design-ecoframe\f793debd-ca2d-4d8a-90bc-5e980a023a8f.jsonl"

logos = {}

with open(jsonl_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            obj = json.loads(line)
        except:
            continue

        # Buscar em tool_result com content que tenha base64 de imagem PNG
        content = json.dumps(obj)

        # Encontrar entradas com título "ecoframe 8.png" e "ecoframe 7.png"
        for title in ["ecoframe 7.png", "ecoframe 8.png"]:
            if title in content:
                # Extrair o campo "content" do JSON de resultado do Drive
                pattern = r'"content"\s*:\s*"([A-Za-z0-9+/=]{1000,})"'
                matches = re.findall(pattern, content)
                for m in matches:
                    if len(m) > 5000:  # base64 de PNG deve ser grande
                        if "7.png" in content and title == "ecoframe 7.png":
                            logos["logo-cor"] = m
                        elif "8.png" in content and title == "ecoframe 8.png":
                            logos["logo-branco"] = m

out_dir = os.path.dirname(os.path.abspath(__file__))

for name, b64 in logos.items():
    path = os.path.join(out_dir, f"{name}.png")
    data = base64.b64decode(b64)
    with open(path, "wb") as f:
        f.write(data)
    print(f"Salvo: {path} ({len(data)} bytes)")

if not logos:
    print("Nenhum logo encontrado. Tentando abordagem alternativa...")
    # Busca mais ampla
    with open(jsonl_path, "r", encoding="utf-8") as f:
        full = f.read()

    for title, name in [("ecoframe 8.png", "logo-branco"), ("ecoframe 7.png", "logo-cor")]:
        idx = full.find(title)
        if idx == -1:
            print(f"  {title}: não encontrado")
            continue
        # Pegar contexto ao redor
        chunk = full[max(0,idx-5000):idx+5000]
        pattern = r'"content"\s*:\s*"([A-Za-z0-9+/=]{500,})"'
        m = re.search(pattern, chunk)
        if m:
            b64 = m.group(1)
            data = base64.b64decode(b64 + "==")  # padding extra por segurança
            path = os.path.join(out_dir, f"{name}.png")
            with open(path, "wb") as f:
                f.write(data)
            print(f"  Salvo: {path} ({len(data)} bytes)")
        else:
            print(f"  {title}: base64 não encontrado no contexto")
