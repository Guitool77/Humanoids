from pathlib import Path
import os
import random

# dossier du script python
base_dir = Path(__file__).parent

# sous dossier contenant les images
folder = base_dir / "noah_tech_shapes"

files = [f for f in os.listdir(folder)
         if f.lower().endswith((".webp", ".jpg", ".png", ".jpeg", ".gif"))]

random.shuffle(files)

for i, f in enumerate(files):
    ext = os.path.splitext(f)[1]
    new_name = f"img_tech_shapes{i:04d}{ext}"

    os.rename(
        folder / f,
        folder / new_name
    )