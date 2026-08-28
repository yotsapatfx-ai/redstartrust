# -*- coding: utf-8 -*-
"""สร้างชิ้นส่วนแผนที่สำหรับ mockup: เส้น path ของประเทศ + ตำแหน่งหมุด 7 จุด"""
import io, json, math, re

DATA = r"C:\Users\Yotsa\AppData\Local\Temp\claude\C--RedStarTrust\6e517f0d-2b03-4c69-8c22-85120add71b5\scratchpad\worldpaths.js"
OUTP = r"C:\Users\Yotsa\AppData\Local\Temp\claude\C--RedStarTrust\6e517f0d-2b03-4c69-8c22-85120add71b5\scratchpad\map_paths.txt"
OUTC = r"C:\Users\Yotsa\AppData\Local\Temp\claude\C--RedStarTrust\6e517f0d-2b03-4c69-8c22-85120add71b5\scratchpad\pins.json"

src = io.open(DATA, encoding="utf-8").read()
W = int(re.search(r"MAP_W=(\d+)", src).group(1))
H = int(re.search(r"MAP_H=(\d+)", src).group(1))
world = json.loads(re.search(r"const WORLD=(\{.*?\});\n", src, re.S).group(1))

HILITE = {"AU", "GB", "US", "CY", "AE", "ZA", "SG"}

parts = []
for iso, d in world.items():
    hi = ' data-hi="1"' if iso in HILITE else ""
    parts.append('<path d="%s"%s></path>' % (d, hi))
io.open(OUTP, "w", encoding="utf-8").write("".join(parts))

# ---- ตำแหน่งหมุด: ใช้พิกัดจริงแล้วฉายด้วย Robinson เหมือนตอนสร้างแผนที่ ----
RX = [1.0000,0.9986,0.9954,0.9900,0.9822,0.9730,0.9600,0.9427,0.9216,0.8962,
      0.8679,0.8350,0.7986,0.7597,0.7186,0.6732,0.6213,0.5722,0.5322]
RY = [0.0000,0.0620,0.1240,0.1860,0.2480,0.3100,0.3720,0.4340,0.4958,0.5571,
      0.6176,0.6769,0.7346,0.7903,0.8435,0.8936,0.9394,0.9761,1.0000]

def robinson(lon, lat):
    s = 1.0 if lat >= 0 else -1.0
    a = min(abs(lat), 90.0)
    i = int(a // 5)
    if i >= 18:
        xf, yf = RX[18], RY[18]
    else:
        t = (a - i*5) / 5.0
        xf = RX[i] + (RX[i+1]-RX[i])*t
        yf = RY[i] + (RY[i+1]-RY[i])*t
    return 0.8487*xf*math.radians(lon), 1.3523*yf*s

# ค่าคงที่ของกรอบเดิม: x0 = ค่า x ที่ lon=-180, ช่วง y จาก +83.6N ถึง 60S
x_min, _ = robinson(-180, 0)
x_max, _ = robinson(180, 0)
scale = W / (x_max - x_min)
_, y_top = robinson(0, 83.63)      # ปลายเหนือสุดของกรีนแลนด์ในชุดข้อมูล
_, y_bot = robinson(0, -60)
# ปรับ y_top ให้ตรงกับ H ที่สร้างไว้จริง
y_top = y_bot + H/scale

def px(lon, lat):
    x, y = robinson(lon, lat)
    return round((x - x_min)*scale, 1), round((y_top - y)*scale, 1)

PLACES = [
    ("AU", "Australia", 134.0, -25.5),
    ("GB", "United Kingdom", -2.0, 53.5),
    ("US", "USA", -98.0, 39.5),
    ("CY", "Cyprus", 33.2, 35.0),
    ("AE", "UAE", 54.0, 24.2),
    ("SG", "Singapore", 103.8, 1.4),
    ("ZA", "South Africa", 25.0, -29.5),
]
pins = []
for iso, name, lo, la in PLACES:
    x, y = px(lo, la)
    pins.append({"iso": iso, "name": name,
                 "left": round(x/W*100, 2), "top": round(y/H*100, 2)})
io.open(OUTC, "w", encoding="utf-8").write(json.dumps(pins, ensure_ascii=False, indent=1))

import os
print("viewBox 0 0 %d %d" % (W, H))
print("paths KB:", round(os.path.getsize(OUTP)/1024, 1))
for p in pins:
    print(p["iso"], p["left"], p["top"])
