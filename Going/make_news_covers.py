"""
สร้างรูปปกข่าวทั้ง 5 เรื่อง (News/<slug>/cover.webp)
งานตาม Going/TASK-NEWS-PUBLISH.md ข้อ 4 — วาดภาพประกอบเอง ไม่ใช้รูปจากอินเทอร์เน็ต
เพื่อเลี่ยงความเสี่ยงลิขสิทธิ์/เครื่องหมายการค้า (โดยเฉพาะข่าว IC x BLAST ที่มีแบรนด์จริงเกี่ยวข้อง)
โทนสี: แดงเข้ม #b6291a + ครีม/ดำ ตามโทนสถาบันของเว็บ (อ้างอิง CORE-PILLAR.md)
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 1200, 630
CREAM = (245, 239, 230)
CREAM_DARK = (230, 221, 206)
RED = (182, 41, 26)      # #b6291a
RED_DARK = (120, 27, 17)
INK = (26, 21, 18)
INK_SOFT = (90, 82, 74)

NEWS_DIR = r"C:\RedStarTrust\News"


def base_canvas():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    # เส้นกรอบบางสไตล์สถาบัน
    d.rectangle([16, 16, W - 16, H - 16], outline=RED_DARK, width=2)
    return img, d


def save(img, slug):
    out_dir = os.path.join(NEWS_DIR, slug)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "cover.webp")
    img.save(path, "WEBP", quality=80, method=6)
    size_kb = os.path.getsize(path) / 1024
    print(f"{slug}: {size_kb:.1f} KB -> {path}")


# 1) มาร์เก็ตแชร์โบรกเกอร์ — กราฟแท่งจริงจากข้อมูลในบทความ
def cover_market_share():
    img, d = base_canvas()
    data = [
        ("KKPS", 24.33), ("KGI", 9.19), ("JPM", 8.25), ("UBS", 5.91),
        ("MST", 5.21), ("CGSI", 4.58), ("BLS", 4.04), ("KGF", 3.56),
        ("FSS", 3.34), ("INVX", 2.82),
    ]
    max_v = max(v for _, v in data)
    chart_left, chart_right = 90, W - 90
    baseline = H - 120
    top = 90
    n = len(data)
    gap = 18
    bar_w = (chart_right - chart_left - gap * (n - 1)) / n
    for i, (name, v) in enumerate(data):
        bar_h = (v / max_v) * (baseline - top)
        x0 = chart_left + i * (bar_w + gap)
        x1 = x0 + bar_w
        y1 = baseline
        y0 = baseline - bar_h
        color = RED if i == 0 else CREAM_DARK
        outline = RED_DARK if i == 0 else INK_SOFT
        d.rectangle([x0, y0, x1, y1], fill=color, outline=outline, width=2)
    d.line([chart_left - 20, baseline, chart_right + 20, baseline], fill=INK, width=3)
    save(img, "thai-broker-market-share-18-aug-2026")


# 2) Nasdaq halt — ป้าย HALT นามธรรม ไม่มีโลโก้จริง
def cover_trading_halt():
    img, d = base_canvas()
    cx, cy = W // 2, H // 2
    # แถบราคากระพริบ (แนวคิดหน้าจอกระดาน) เป็นเส้นกราฟนามธรรม
    pts = []
    for i in range(40):
        x = 120 + i * ((W - 240) / 39)
        y = cy - 60 + 40 * math.sin(i * 0.5) - i * 0.3
        pts.append((x, y))
    d.line(pts, fill=CREAM_DARK, width=4, joint="curve")
    # กล่อง HALT ตรงกลาง
    box_w, box_h = 360, 120
    bx0, by0 = cx - box_w // 2, cy - box_h // 2 + 40
    bx1, by1 = cx + box_w // 2, cy + box_h // 2 + 40
    d.rectangle([bx0, by0, bx1, by1], fill=RED, outline=RED_DARK, width=4)
    # แถบทแยงกันไหว้ (คอนเซปต์ป้ายเตือน) แทนตัวหนังสือ
    stripe_gap = 26
    for i in range(-4, 12):
        x0 = bx0 + i * stripe_gap
        d.line([(x0, by1), (x0 + (by1 - by0), by0)], fill=CREAM, width=8)
    d.rectangle([bx0, by0, bx1, by1], outline=RED_DARK, width=4)
    save(img, "nasdaq-trading-halt-rules-update-2026")


# 3) ICE futures — สามกราฟเส้นแทนสามธนาคารกลาง
def cover_ice_futures():
    img, d = base_canvas()
    labels_y = [170, 330, 490]
    colors = [RED, INK, INK_SOFT]
    for row, y_base in enumerate(labels_y):
        pts = []
        for i in range(30):
            x = 110 + i * ((W - 220) / 29)
            y = y_base + 30 * math.sin(i * 0.4 + row * 2) - (i * 0.15 if row != 0 else -i * 0.15)
            pts.append((x, y))
        d.line(pts, fill=colors[row], width=5, joint="curve")
        d.line([90, y_base, W - 90, y_base], fill=CREAM_DARK, width=1)
    save(img, "ice-economic-indicator-futures-launch")


# 4) ก.ล.ต. ผู้ถือหุ้นรายใหญ่ — เอกสาร + ผังโครงสร้างถือหุ้นหลายชั้น
def cover_sec_shareholder():
    img, d = base_canvas()
    # เอกสารซ้อนกันมุมซ้าย
    for i, off in enumerate([0, 16, 32]):
        x0, y0 = 110 + off, 130 + off
        x1, y1 = 380 + off, 480 + off
        fill = CREAM if i < 2 else CREAM_DARK
        d.rectangle([x0, y0, x1, y1], fill=fill, outline=INK_SOFT, width=2)
        for li in range(6):
            ly = y0 + 40 + li * 40
            d.line([x0 + 24, ly, x1 - 24, ly], fill=INK_SOFT, width=3)
    # ผังโครงสร้างถือหุ้นหลายชั้น ฝั่งขวา
    nodes = [
        (900, 150), (780, 300), (1020, 300),
        (700, 460), (860, 460), (960, 460), (1100, 460),
    ]
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    for a, b in edges:
        d.line([nodes[a], nodes[b]], fill=INK_SOFT, width=3)
    for i, (x, y) in enumerate(nodes):
        r = 26 if i == 0 else 18
        color = RED if i == 0 else CREAM_DARK
        d.ellipse([x - r, y - r, x + r, y + r], fill=color, outline=RED_DARK if i == 0 else INK_SOFT, width=3)
    save(img, "sec-thailand-major-shareholder-futures-rules")


# 5) IC x BLAST อีสปอร์ต — เวทีนามธรรม ไม่มีโลโก้แบรนด์จริงใด ๆ (เลี่ยงประเด็นลิขสิทธิ์)
def cover_esports_sponsorship():
    img, d = base_canvas()
    # เวทีเปล่า
    stage_top = 420
    d.polygon([(60, H - 40), (W - 60, H - 40), (W - 180, stage_top), (180, stage_top)],
              fill=CREAM_DARK, outline=INK_SOFT)
    # จอถ่ายทอดสดตรงกลางเวที — แสดงกราฟราคานามธรรมแทนโลโก้จริงใด ๆ
    screen_w, screen_h = 420, 200
    sx0, sy0 = (W - screen_w) // 2, 120
    sx1, sy1 = sx0 + screen_w, sy0 + screen_h
    d.rectangle([sx0, sy0, sx1, sy1], fill=INK, outline=RED_DARK, width=6)
    pts = []
    for i in range(24):
        x = sx0 + 20 + i * ((screen_w - 40) / 23)
        y = sy0 + screen_h - 30 - (i * 6 % 140)
        pts.append((x, y))
    d.line(pts, fill=RED, width=4, joint="curve")
    # แสงสปอตไลต์คู่ ทรงกรวย
    for cx in (300, W - 300):
        d.polygon([(cx - 10, 0), (cx + 10, 0), (cx + 140, stage_top), (cx - 140, stage_top)],
                  fill=(238, 224, 205))
    # วาดเวทีทับแสงอีกที ให้ขอบคมสวยงาม
    d.polygon([(60, H - 40), (W - 60, H - 40), (W - 180, stage_top), (180, stage_top)],
              fill=CREAM_DARK, outline=INK_SOFT, width=2)
    save(img, "ic-blast-esports-multi-year-partnership")


if __name__ == "__main__":
    cover_market_share()
    cover_trading_halt()
    cover_ice_futures()
    cover_sec_shareholder()
    cover_esports_sponsorship()
    print("done")
