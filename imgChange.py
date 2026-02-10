import os
import re
from PIL import Image

cartella_target = r"C:\Users\ext-andrea.ruzzenent\Documents\ruzzeglobant.github.io\3326a99fc5ccd74646b7a069d57cb192_20251110"

estensioni_immagini = (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp")

# Pattern dei file da ESCLUDERE
# - contiene T_
# - termina ESATTAMENTE con _M, _C o _N
pattern_esclusi = re.compile(r"T_.*_(M|C|N)$", re.IGNORECASE)

for root, dirs, files in os.walk(cartella_target):
    for file in files:
        nome, ext = os.path.splitext(file)

        if ext.lower() not in estensioni_immagini:
            continue

        # 👉 Se matcha il pattern, lo SKIPPIAMO
        if pattern_esclusi.match(nome):
            print(f"SKIP → {file}")
            continue

        percorso = os.path.join(root, file)

        try:
            img = Image.open(percorso).convert("RGBA")
            w, h = img.size

            img_trasparente = Image.new("RGBA", (w, h), (0, 0, 0, 0))

            # JPG/JPEG/BMP → PNG
            if ext.lower() in (".jpg", ".jpeg", ".bmp"):
                nuovo_percorso = os.path.join(root, nome + ".png")
                img_trasparente.save(nuovo_percorso, "PNG")
                os.remove(percorso)
            else:
                img_trasparente.save(percorso)

            print(f"MODIFICATO → {file}")

        except Exception as e:
            print(f"ERRORE → {file}: {e}")
