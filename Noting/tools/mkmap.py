# -*- coding: utf-8 -*-
import json, io, math

SRC = r"C:\Users\Yotsa\AppData\Local\Temp\claude\C--RedStarTrust\6e517f0d-2b03-4c69-8c22-85120add71b5\scratchpad\world.geojson"
OUT = r"C:\Users\Yotsa\AppData\Local\Temp\claude\C--RedStarTrust\6e517f0d-2b03-4c69-8c22-85120add71b5\scratchpad\worldpaths.js"

RX = [1.0000,0.9986,0.9954,0.9900,0.9822,0.9730,0.9600,0.9427,0.9216,0.8962,
      0.8679,0.8350,0.7986,0.7597,0.7186,0.6732,0.6213,0.5722,0.5322]
RY = [0.0000,0.0620,0.1240,0.1860,0.2480,0.3100,0.3720,0.4340,0.4958,0.5571,
      0.6176,0.6769,0.7346,0.7903,0.8435,0.8936,0.9394,0.9761,1.0000]

def robinson(lon, lat):
    s = 1.0 if lat >= 0 else -1.0
    a = abs(lat)
    if a > 90: a = 90.0
    i = int(a // 5)
    if i >= 18:
        xf, yf = RX[18], RY[18]
    else:
        t = (a - i*5) / 5.0
        xf = RX[i] + (RX[i+1]-RX[i])*t
        yf = RY[i] + (RY[i+1]-RY[i])*t
    x = 0.8487 * xf * math.radians(lon)
    y = 1.3523 * yf * s
    return x, y

def rings(geom):
    t = geom["type"]; c = geom["coordinates"]
    if t == "Polygon": return [c[0]]
    if t == "MultiPolygon": return [p[0] for p in c]
    return []

data = json.load(io.open(SRC, encoding="utf-8"))
SKIP = {"ATA"}  # แอนตาร์กติกา

feats = []
minx = miny = 1e9; maxx = maxy = -1e9
for f in data["features"]:
    p = f["properties"]
    a3 = p.get("ADM0_A3") or ""
    if a3 in SKIP: continue
    iso = p.get("ISO_A2_EH") or p.get("ISO_A2") or ""
    if iso in ("-99", "", None): iso = a3
    name = p.get("ADMIN") or a3
    polys = []
    for r in rings(f["geometry"]):
        pts = []
        for lon, lat in r:
            if lat < -60: lat = -60.0
            pts.append(robinson(lon, lat))
        xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
        if not xs: continue
        w = max(xs)-min(xs); h = max(ys)-min(ys)
        if w < 0.012 and h < 0.012:   # ตัดเกาะจิ๋ว
            continue
        polys.append(pts)
        minx = min(minx, min(xs)); maxx = max(maxx, max(xs))
        miny = min(miny, min(ys)); maxy = max(maxy, max(ys))
    if polys:
        feats.append((iso, name, polys))

W = 1000.0
scale = W / (maxx - minx)
H = (maxy - miny) * scale

def sx(x): return (x - minx) * scale
def sy(y): return (maxy - y) * scale

paths = {}
cents = {}
for iso, name, polys in feats:
    d = []
    best = None; bestarea = -1
    for pts in polys:
        prev = None
        seg = []
        for (x, y) in pts:
            X = round(sx(x), 1); Y = round(sy(y), 1)
            if prev == (X, Y): continue
            seg.append(("M" if prev is None else "L") + str(X) + " " + str(Y))
            prev = (X, Y)
        if len(seg) < 3: continue
        d.append("".join(seg) + "Z")
        xs = [sx(q[0]) for q in pts]; ys = [sy(q[1]) for q in pts]
        area = (max(xs)-min(xs)) * (max(ys)-min(ys))
        if area > bestarea:
            bestarea = area
            best = (round(sum(xs)/len(xs), 1), round(sum(ys)/len(ys), 1))
    if not d: continue
    if iso in paths:
        paths[iso] += "".join(d)
    else:
        paths[iso] = "".join(d)
        cents[iso] = best

# เขตอำนาจขนาดเล็กที่แผนที่ 110m ไม่มีรูปร่าง — ใช้หมุดแทน (lon, lat)
SMALL = {
    "MU": (57.55, -20.28), "SC": (55.49, -4.62),  "SG": (103.82, 1.35),
    "MT": (14.51, 35.90),  "HK": (114.17, 22.32), "VG": (-64.62, 18.42),
    "KY": (-81.25, 19.31), "BM": (-64.75, 32.31), "VU": (168.32, -17.74),
    "CW": (-68.99, 12.17), "LC": (-60.98, 13.91), "KN": (-62.75, 17.35),
    "MH": (171.18, 7.13),  "CK": (-159.78, -21.24), "BS": (-77.40, 25.05),
    "LI": (9.55, 47.17),   "MC": (7.42, 43.74),   "AD": (1.52, 42.51),
    "SM": (12.46, 43.94),  "LU": (6.13, 49.61),   "BB": (-59.54, 13.19),
    "AG": (-61.80, 17.06), "DM": (-61.37, 15.41), "VC": (-61.19, 13.25),
    "GI": (-5.35, 36.14),  "JE": (-2.11, 49.21),  "IM": (-4.55, 54.24),
    "GG": (-2.58, 49.46),  "AI": (-63.06, 18.22), "TC": (-71.13, 21.69),
}
PIN = {}
for k, (lo, la) in SMALL.items():
    x, y = robinson(lo, la)
    PIN[k] = [round(sx(x), 1), round(sy(y), 1)]

out = io.open(OUT, "w", encoding="utf-8")
out.write("/* แผนที่โลก Robinson projection · ที่มา Natural Earth 110m (public domain) */\n")
out.write("const MAP_W=%d,MAP_H=%d;\n" % (int(W), int(round(H))))
out.write("const WORLD=" + json.dumps(paths, separators=(",", ":")) + ";\n")
out.write("const CENT=" + json.dumps(cents, separators=(",", ":")) + ";\n")
out.write("const PIN=" + json.dumps(PIN, separators=(",", ":")) + ";\n")
out.close()

import os
print("countries:", len(paths))
print("size KB:", round(os.path.getsize(OUT)/1024, 1))
print("viewBox: 0 0 %d %d" % (int(W), int(round(H))))
for k in ["TH","AU","CY","GB","MU","MY","VN","ID","PH","SG"]:
    print(k, "ok" if k in paths else "MISSING", cents.get(k))
