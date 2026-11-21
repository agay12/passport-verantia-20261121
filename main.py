"""Passport spread entrypoint: the spread is rendered into the repository as
entry.png (fonts in fonts/), and this entrypoint copies it to the sandbox's
output directory (MAKEFUN_OUTPUT_DIR, default /output)."""
import os
import shutil

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))
print("entry.png written to", OUT)
