# -*- coding: utf-8 -*-
"""แปลงไอคอนที่ดึงมาให้เป็น PNG 128px ตัดขอบโปร่งออก แล้วทำเป็น data URI ฝังในหน้าเว็บ"""
import os, io, json, base64, glob
from PIL import Image

SRC = r"C:\Users\Yotsa\AppData\Local\Temp\claude\C--RedStarTrust\6e517f0d-2b03-4c69-8c22-85120add71b5\scratchpad\logos"
OUT_JS = os.path.join(SRC, "logo_data.js")
OUT_DIR = r"C:\RedStarTrust\Noting\prototype\logos"

SLUGS = ["exness","ic-markets","xm","pepperstone","fp-markets","eightcap",
         "tickmill","axi","hfm","ig","oanda","equiti"]

data, report = {}, []

for slug in SLUGS:
    hit = None
    for ext in ("svg","png","ico","jpg","webp"):
        p = os.path.join(SRC, slug + "." + ext)
        if os.path.exists(p):
            hit = (p, ext); break
    if not hit:
        report.append((slug, "MISSING", 0, "")); continue
    p, ext = hit

    if ext == "svg":
        raw = open(p, "rb").read()
        if len(raw) > 60000:
            report.append((slug, "SVG-TOO-BIG", len(raw), "")); continue
        uri = "data:image/svg+xml;base64," + base64.b64encode(raw).decode()
        data[slug] = uri
        open(os.path.join(OUT_DIR, slug + ".svg"), "wb").write(raw)
        report.append((slug, "svg", len(raw), "vector"))
        continue

    im = Image.open(p)
    if ext == "ico":
        # เลือกเฟรมที่ใหญ่ที่สุดในไฟล์ ico
        try:
            sizes = sorted(im.ico.sizes())
            im = im.ico.getimage(sizes[-1])
        except Exception:
            im.seek(0)
    im = im.convert("RGBA")
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    w, h = im.size
    scale = 128.0 / max(w, h)
    if scale < 1:
        im = im.resize((max(1, int(w*scale)), max(1, int(h*scale))), Image.LANCZOS)
    # ตรวจว่าไม่ใช่ภาพว่าง
    alpha = im.getchannel("A")
    solid = sum(1 for v in alpha.getdata() if v > 24)
    frac = solid / float(im.size[0]*im.size[1])
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    raw = buf.getvalue()
    note = "%dx%d from %dx%d, ink %d%%" % (im.size[0], im.size[1], w, h, round(frac*100))
    if frac < 0.02:
        report.append((slug, "BLANK-SKIP", len(raw), note)); continue
    data[slug] = "data:image/png;base64," + base64.b64encode(raw).decode()
    open(os.path.join(OUT_DIR, slug + ".png"), "wb").write(raw)
    report.append((slug, "png", len(raw), note))

js = "var LOGO_DATA=" + json.dumps(data, separators=(",", ":")) + ";\n"
open(OUT_JS, "w", encoding="utf-8").write(js)

for r in report:
    print("%-12s %-14s %7dB  %s" % r)
print("\nฝังได้ %d/%d  ·  ขนาดรวม %.1f KB" % (len(data), len(SLUGS), len(js)/1024.0))
