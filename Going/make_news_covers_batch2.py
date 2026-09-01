"""
สร้างรูปปกข่าวชุดที่ 2 — 4 เรื่องใหม่ (News/<slug>/cover.webp)
ใช้แนวทางเดียวกับ make_news_covers.py ชุดแรกทุกประการ:
วาดภาพประกอบเอง ไม่ดาวน์โหลดรูปจากที่ใด เพื่อเลี่ยงความเสี่ยงลิขสิทธิ์/เครื่องหมายการค้า
(ข่าวชุดนี้มีชื่อบริษัทจริงหลายราย เช่น CICC/Nasdaq/CME — จึงไม่มีโลโก้หรือตราสัญลักษณ์ใดในภาพ)
โทนสี: แดงเข้ม #b6291a + ครีม/ดำ ตามโทนสถาบันของเว็บ
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 1200, 630
CREAM = (245, 239, 230)
CREAM_DARK = (230, 221, 206)
RED = (182, 41, 26)
RED_DARK = (120, 27, 17)
INK = (26, 21, 18)
INK_SOFT = (90, 82, 74)

NEWS_DIR = r"C:\RedStarTrust\News"


def base_canvas():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([16, 16, W - 16, H - 16], outline=RED_DARK, width=2)
    return img, d


def save(img, slug):
    out_dir = os.path.join(NEWS_DIR, slug)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "cover.webp")
    img.save(path, "WEBP", quality=80, method=6)
    size_kb = os.path.getsize(path) / 1024
    print(f"{slug}: {size_kb:.1f} KB")


# 6) CICC ควบรวม Dongxing + Cinda — สามกล่องรวมเป็นกล่องเดียว
def cover_cicc_merger():
    img, d = base_canvas()
    # สามกล่องต้นทางฝั่งซ้าย
    boxes = [(150, 150), (150, 285), (150, 420)]
    sizes = [(190, 90), (150, 70), (150, 70)]
    for i, ((bx, by), (bw, bh)) in enumerate(zip(boxes, sizes)):
        fill = RED if i == 0 else CREAM_DARK
        outline = RED_DARK if i == 0 else INK_SOFT
        d.rectangle([bx, by, bx + bw, by + bh], fill=fill, outline=outline, width=3)
    # เส้นโยงเข้ากล่องผลลัพธ์
    target = (760, 275, 1050, 405)
    for (bx, by), (bw, bh) in zip(boxes, sizes):
        d.line([(bx + bw, by + bh // 2), (690, 340), (target[0], 340)],
               fill=INK_SOFT, width=3)
    # กล่องผลลัพธ์ใหญ่
    d.rectangle(list(target), fill=RED, outline=RED_DARK, width=4)
    # แถบแสดงขนาดสินทรัพย์ที่โตขึ้น ใต้กล่องผลลัพธ์
    for i, w in enumerate([120, 200, 290]):
        y = 450 + i * 26
        d.rectangle([760, y, 760 + w, y + 14], fill=CREAM_DARK, outline=INK_SOFT)
    save(img, "cicc-dongxing-cinda-merger-regulatory-stage")


# 7) Offerpad ย้ายตลาด NYSE -> Nasdaq — ตัวย่อเดิมย้ายข้ามสองกระดาน
def cover_offerpad_transfer():
    img, d = base_canvas()
    # กระดานสองฝั่ง (ไม่ใส่ชื่อตลาดจริง เป็นกล่องนามธรรม)
    d.rectangle([120, 190, 430, 440], fill=CREAM_DARK, outline=INK_SOFT, width=3)
    d.rectangle([770, 190, 1080, 440], fill=CREAM_DARK, outline=RED_DARK, width=3)
    # แถวข้อมูลจาง ๆ ในกระดานทั้งสอง
    for bx in (120, 770):
        for r in range(4):
            y = 230 + r * 45
            d.line([bx + 30, y, bx + 200, y], fill=INK_SOFT, width=4)
    # ป้ายตัวย่อที่ย้ายข้าม (กล่องแดงเดียวกันทั้งสองฝั่ง = ตัวย่อไม่เปลี่ยน)
    d.rectangle([470, 285, 590, 345], fill=CREAM_DARK, outline=INK_SOFT, width=3)
    d.rectangle([610, 285, 730, 345], fill=RED, outline=RED_DARK, width=3)
    # ลูกศรย้าย
    d.line([(595, 315), (605, 315)], fill=INK, width=4)
    d.polygon([(735, 315), (715, 300), (715, 330)], fill=RED_DARK)
    save(img, "offerpad-transfers-listing-nyse-to-nasdaq")


# 8) CME แฟกเตอร์หุ้น 5 แบบ — แยกกราฟออกเป็นช่องคนละช่อง
def cover_cme_factors():
    img, d = base_canvas()
    panel_w, gap = 200, 24
    start_x = (W - (panel_w * 5 + gap * 4)) // 2
    for i in range(5):
        px = start_x + i * (panel_w + gap)
        py0, py1 = 170, 460
        d.rectangle([px, py0, px + panel_w, py1], fill=CREAM_DARK, outline=INK_SOFT, width=2)
        # กราฟเส้นในแต่ละช่อง รูปทรงต่างกันตามแฟกเตอร์
        pts = []
        for k in range(7):
            x = px + 20 + k * ((panel_w - 40) / 6)
            phase = i * 1.1
            y = (py0 + py1) / 2 - 55 * math.sin(k * 0.75 + phase) + (k * 4 if i % 2 == 0 else -k * 3)
            y = max(py0 + 22, min(py1 - 22, y))
            pts.append((x, y))
        color = RED if i == 3 else INK_SOFT
        width = 5 if i == 3 else 3
        d.line(pts, fill=color, width=width, joint="curve")
    save(img, "cme-emini-equity-factor-futures-launch")


# 9) CFTC พลังประมวลผล — ตู้เซิร์ฟเวอร์คู่กับกระดานราคา
def cover_cftc_compute():
    img, d = base_canvas()
    # ตู้เซิร์ฟเวอร์ฝั่งซ้าย
    for c in range(3):
        rx = 130 + c * 120
        d.rectangle([rx, 160, rx + 90, 470], fill=CREAM_DARK, outline=INK_SOFT, width=3)
        for u in range(9):
            uy = 180 + u * 32
            d.rectangle([rx + 12, uy, rx + 78, uy + 18], fill=CREAM, outline=INK_SOFT)
            # ไฟสถานะจุดเล็ก
            dot = RED if (c + u) % 4 == 0 else INK_SOFT
            d.ellipse([rx + 66, uy + 6, rx + 72, uy + 12], fill=dot)
    # กระดานราคาฝั่งขวา
    d.rectangle([620, 160, 1070, 470], fill=INK, outline=RED_DARK, width=3)
    pts = []
    for k in range(22):
        x = 645 + k * ((1070 - 670) / 21)
        y = 400 - (k * 8) + 40 * math.sin(k * 0.9)
        y = max(200, min(440, y))
        pts.append((x, y))
    d.line(pts, fill=RED, width=4, joint="curve")
    # เส้นกริดจาง ๆ บนกระดาน
    for g in range(4):
        gy = 220 + g * 65
        d.line([640, gy, 1050, gy], fill=(60, 50, 44), width=1)
    save(img, "cftc-compute-derivatives-request-for-comment")


if __name__ == "__main__":
    cover_cicc_merger()
    cover_offerpad_transfer()
    cover_cme_factors()
    cover_cftc_compute()
    print("done")
