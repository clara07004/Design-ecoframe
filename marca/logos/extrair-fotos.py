import json, base64, os, re

tool_results_dir = r"C:\Users\clara\.claude\projects\C--Users-clara-Documents-Design-ecoframe\f793debd-ca2d-4d8a-90bc-5e980a023a8f\tool-results"
output_dir = r"C:\Users\clara\Documents\Design-ecoframe\dados\fotos-produto-preview"
os.makedirs(output_dir, exist_ok=True)

files = [f for f in os.listdir(tool_results_dir) if "download_file_content" in f]
files.sort()

# Only the 6 most recent ones
recent = files[-6:]

for i, fname in enumerate(recent):
    path = os.path.join(tool_results_dir, fname)
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    try:
        data = json.loads(raw)
        b64 = data.get("content", "")
        title = data.get("title", f"foto-{i+1}")
        safe_title = re.sub(r'[^a-zA-Z0-9\-_]', '-', title)[:40]
        img_bytes = base64.b64decode(b64)
        out_path = os.path.join(output_dir, f"{i+1:02d}-{safe_title}.jpg")
        with open(out_path, "wb") as out:
            out.write(img_bytes)
        print(f"Salvo: {out_path} ({len(img_bytes)} bytes)")
    except Exception as e:
        print(f"Erro em {fname}: {e}")

print("Pronto.")
