"""Render an invented passport spread for The Passport Page of a Country That Isn't There.

The Republic of Verantia - a small mountain republic between two larger neighbours.
One image, 1024x1024, written to MAKEFUN_OUTPUT_DIR (or /output) as entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
INK = (42, 54, 66)
CREAM = (238, 231, 214)
CREAM2 = (244, 238, 224)
COVER = (21, 63, 55)
GOLD = (150, 122, 58)
RED = (146, 48, 48)
BLUE = (44, 70, 104)

FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
FD = FONTS if os.path.isdir(FONTS) and os.listdir(FONTS) else "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)

serif_b = lambda s: F("DejaVuSerif-Bold.ttf", s)
serif = lambda s: F("DejaVuSerif.ttf", s)
sans = lambda s: F("DejaVuSans.ttf", s)
sans_b = lambda s: F("DejaVuSans-Bold.ttf", s)
mono = lambda s: F("DejaVuSansMono.ttf", s)
mono_b = lambda s: F("DejaVuSansMono-Bold.ttf", s)

img = Image.new("RGB", (W, H), COVER)
d = ImageDraw.Draw(img)

# ------- spread geometry: two pages with a fold down the middle
PX0, PX1, PY0, PY1 = 18, 1006, 44, 980
d.rectangle([PX0, PY0, PX1, PY1], fill=CREAM)
d.line([(W // 2, PY0), (W // 2, PY1)], fill=(210, 200, 180), width=3)
# page gutters / cover reveal
d.rectangle([PX0, PY0, PX0 + 6, PY1], fill=(16, 48, 42))
d.rectangle([PX1 - 6, PY0, PX1, PY1], fill=(16, 48, 42))
d.rectangle([W // 2 - 2, PY0, W // 2 + 2, PY1], fill=(206, 195, 172))

def guilloche(draw, box, color=(206, 196, 174), step=7):
    x0, y0, x1, y1 = box
    for x in range(x0, x1, step):
        draw.line([(x, y0), (x + 40, y1)], fill=color, width=1)

guilloche(d, (W // 2 + 20, PY0 + 14, PX1 - 14, PY1 - 14))

def label(pos, text, f, fill=INK, anchor=None):
    d.text(pos, text, font=f, fill=fill, anchor=anchor)

# ================= LEFT PAGE: visa & stamps =================
LX = PX0 + 30
label((LX, PY0 + 26), "REPUBLIC OF VERANTIA", serif_b(26))
label((LX, PY0 + 60), "VISAS - VIZES - VYSES", serif(15), GOLD)
d.line([(LX, PY0 + 88), (W // 2 - 30, PY0 + 88)], fill=GOLD, width=2)

# visa vignette (the telling detail of paperwork)
vx0, vy0, vx1, vy1 = LX, PY0 + 110, W // 2 - 34, PY0 + 400
d.rectangle([vx0, vy0, vx1, vy1], outline=BLUE, width=3)
d.rectangle([vx0 + 8, vy0 + 8, vx1 - 8, vy1 - 8], outline=BLUE, width=1)
label((vx0 + 18, vy0 + 16), "REPUBLIC OF OSTMARK", sans_b(17), BLUE)
label((vx0 + 18, vy0 + 40), "VISA - SINGLE ENTRY", sans(14), BLUE)
label((vx0 + 18, vy0 + 62), "No. OM-77341-V", mono(13), BLUE)
label((vx0 + 18, vy0 + 84), "HOLDERS OF THIS VISA MAY NOT", sans(11), RED)
label((vx0 + 18, vy0 + 100), "TRAVEL NORTH OF THE GREY MERIDIAN.", sans(11), RED)
label((vx0 + 18, vy0 + 116), "FEE PAID: 40 MARKS", sans(11), BLUE)
d.rectangle([vx1 - 230, vy1 - 52, vx1 - 126, vy1 - 14], outline=BLUE, width=2)
label((vx1 - 178, vy1 - 44), "40", mono_b(20), BLUE, anchor="mm")
label((vx1 - 178, vy1 - 30), "MARKS", mono(9), BLUE, anchor="mm")
d.rectangle([vx1 - 132, vy1 - 84, vx1 - 40, vy1 - 60], outline=GOLD, width=2)
label((vx1 - 86, vy1 - 72), "VALID 90 DAYS", sans(10), GOLD, anchor="mm")

def stamp(cx, cy, r, top, bottom, date, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=4)
    d.ellipse([cx - r + 7, cy - r + 7, cx + r - 7, cy + r - 7], outline=color, width=2)
    d.text((cx, cy - r * 0.52), top, font=sans_b(max(11, r // 5)), fill=color, anchor="mm")
    d.text((cx, cy + r * 0.5), bottom, font=sans_b(max(11, r // 5)), fill=color, anchor="mm")
    d.text((cx, cy), date, font=mono_b(max(12, r // 4)), fill=color, anchor="mm")

# stamps of neighbouring countries, dates agree with the data page (issued 02 FEB 2026)
stamp(160, 640, 62, "PORT OF KEL AMARAN", "ARRIVAL", "12 MAR 2026", (60, 104, 96))
stamp(350, 800, 56, "FED. REP. OSTMARK", "DEPARTURE", "08 SEP 2026", RED)
stamp(130, 860, 48, "GREY MERIDIAN POST", "EXIT", "09 SEP 2026", (110, 84, 40))
label((LX, PY1 - 44), "Passport No. V-2048117", mono(14), INK)

# ================= RIGHT PAGE: data page =================
RX = W // 2 + 26
label((RX, PY0 + 20), "REPUBLIC OF VERANTIA", serif_b(24))
label((RX, PY0 + 52), "PASSPORT - PASAPORTE - PASZPORT", serif(13), GOLD)
d.line([(RX, PY0 + 78), (PX1 - 30, PY0 + 78)], fill=GOLD, width=2)

fx0, fy0, fx1, fy1 = RX + 6, PY0 + 100, RX + 208, PY0 + 360
d.rectangle([fx0, fy0, fx1, fy1], fill=CREAM2, outline=(180, 170, 150), width=1)
# portrait: simple procedural face
fcx, fcy = (fx0 + fx1) // 2, fy0 + 118
d.ellipse([fcx - 46, fcy - 50, fcx + 46, fcy + 42], fill=(214, 178, 148), outline=(120, 90, 70), width=2)
d.ellipse([fcx - 52, fcy - 66, fcx - 24, fcy - 52], fill=(60, 44, 36))
d.ellipse([fcx + 24, fcy - 66, fcx + 52, fcy - 52], fill=(60, 44, 36))
d.rectangle([fcx - 52, fcy - 56, fcx + 52, fcy - 40], fill=(60, 44, 36))
d.ellipse([fcx - 20, fcy - 8, fcx - 8, fcy + 2], fill=INK)
d.ellipse([fcx + 8, fcy - 8, fcx + 20, fcy + 2], fill=INK)
d.line([(fcx - 14, fcy + 24), (fcx + 14, fcy + 24)], fill=(120, 70, 60), width=2)
d.rectangle([fcx - 46, fcy + 42, fcx + 46, fy1 - 24], fill=(70, 82, 94))
d.polygon([(fcx - 46, fy1 - 24), (fcx + 46, fy1 - 24), (fcx + 30, fy1 - 34), (fcx - 30, fy1 - 34)], fill=(70, 82, 94))
label((fcx, fy1 - 16), "TYPE  VRT-DOC 2026", mono(11), CREAM2, anchor="mm")

rows = [
    ("SURNAME", "THELANDRI"),
    ("GIVEN NAMES", "MARO VANDER"),
    ("NATIONALITY", "VERANTIAN"),
    ("DATE OF BIRTH", "14 JUN 1992"),
    ("PLACE OF BIRTH", "CORVANE"),
    ("DATE OF ISSUE", "02 FEB 2026"),
    ("DATE OF EXPIRY", "01 FEB 2036"),
    ("AUTHORITY", "MINISTRY OF INTERIOR"),
]
ry = PY0 + 104
for k, v in rows:
    label((fx1 + 24, ry), k, sans(11), (120, 110, 90))
    label((fx1 + 24, ry + 14), v, sans_b(14), INK)
    ry += 30
label((RX + 6, PY0 + 392), "HOLDER'S SIGNATURE", sans(11), (120, 110, 90))
d.line([(RX + 6, PY0 + 430), (RX + 230, PY0 + 430)], fill=INK, width=1)
d.line([(RX + 14, PY0 + 424), (RX + 60, PY0 + 414), (RX + 110, PY0 + 426), (RX + 150, PY0 + 416)], fill=INK, width=2)

# language column telling detail: three official languages with a fee note
label((RX + 6, PY0 + 452), "OFFICIAL LANGUAGES: MERIDIAN - ANGLIC - VYSIC", sans(12), GOLD)
label((RX + 6, PY0 + 470), "ISSUE FEE: 25 CROWNS (PAID)", sans(12), GOLD)

# machine-readable strip
mz0, mz1 = RX + 4, PX1 - 26
my = PY1 - 96
d.rectangle([mz0, my, mz1, my + 66], fill=CREAM2, outline=(180, 170, 150))
label((mz0 + 10, my + 10), "P<VRTTHELANDRI<<MARO<VANDER<<<<<<<<<<<", mono_b(15), INK)
label((mz0 + 10, my + 38), "V2048117<8VRT9206142M3602011<<<<<<<<<<<<<02", mono_b(15), INK)

# spine title on the fold
d.text((W // 2, PY1 - 10), "", font=sans(10), fill=COVER)

os.makedirs(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), exist_ok=True)
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
img.save(OUT, "PNG")
print("wrote", OUT, os.path.getsize(OUT), "bytes")
