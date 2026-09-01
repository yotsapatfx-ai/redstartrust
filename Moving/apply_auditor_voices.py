# -*- coding: utf-8 -*-
"""
ปรับคำเขียนบล็อก Auditor Voices ตามเวอร์ชันใหม่ที่ Boss ส่งมา
งานตาม Moving/TASK-AUDITOR-VOICES.md — ใช้ถ้อยคำของ Boss ตรง ๆ ไม่แต่งเพิ่ม
เพิ่มฟิลด์ d: (หมวดถนัด) ซึ่งโครงสร้างเดิมไม่มี
"""
import io
import json
import re

BUILD_PY = r'C:\RedStarTrust\Noting\design\build-mockup.py'

VOICES = [
    {
        "i": "ธ",
        "n": "ธนกฤต วงษ์อำไพ",
        "d": "โครงสร้างโบรกเกอร์",
        "r": "หัวหน้าฝ่ายตรวจสอบใบอนุญาตและโครงสร้างบริษัท",
        "q": "โบรกเกอร์ที่น่าเชื่อถือ ไม่ได้วัดจากการตลาด แต่<b>พิสูจน์ได้จากใบอนุญาต การแยกเงินลูกค้า และความโปร่งใสของโครงสร้างองค์กร</b>",
        "t": ["Regulation", "Corporate Structure"],
    },
    {
        "i": "น",
        "n": "นที เจริญวงศ์",
        "d": "ต้นทุนการเทรด",
        "r": "ผู้เชี่ยวชาญด้าน Execution, Spread และ Slippage",
        "q": "Spread ต่ำไม่มีความหมาย หากคำสั่งถูกรีโควตหรือ Slippage สูง สิ่งที่ต้องวัดคือ <b>‘ต้นทุนจริง’ หลังเปิดและปิดออเดอร์</b>",
        "t": ["Execution Test", "Slippage Analysis"],
    },
    {
        "i": "ก",
        "n": "กันตินา ศรีสุวรรณ",
        "d": "กฎหมายการเงิน",
        "r": "ที่ปรึกษาด้านกฎหมายการเงินและข้อพิพาทลูกค้า",
        "q": "ก่อนเปิดบัญชี สิ่งที่ควรอ่านไม่ใช่โบนัส แต่คือ <b>Client Agreement และนโยบายการคุ้มครองเงินฝาก</b> เพราะนั่นคือสิทธิ์ที่แท้จริงของผู้ลงทุน",
        "t": ["Client Agreement", "Investor Protection"],
    },
    {
        "i": "พ",
        "n": "พีระพล อินทรพิทักษ์",
        "d": "บริการลูกค้า",
        "r": "ผู้ตรวจสอบคุณภาพฝ่ายบริการและกระบวนการถอนเงิน",
        "q": "<b>คุณภาพของโบรกเกอร์ถูกวัดในวันที่เกิดปัญหา ไม่ใช่วันที่ฝากเงิน</b> ทีมซัพพอร์ตที่แก้ไขได้จริง คือมาตรฐานที่เราประเมิน",
        "t": ["Withdrawal Test", "Support Quality"],
    },
]


def esc(s):
    """เขียนเป็น \\uXXXX ให้ตรงสไตล์ไฟล์เดิมที่เป็น ASCII ล้วน"""
    out = json.dumps(s, ensure_ascii=True)
    return out


def build_block():
    rows = []
    for v in VOICES:
        tags = ", ".join(esc(t) for t in v["t"])
        rows.append(
            "  {i: " + esc(v["i"]) + ", n: " + esc(v["n"]) + ",\n"
            "   d: " + esc(v["d"]) + ",\n"
            "   r: " + esc(v["r"]) + ",\n"
            "   q: " + esc(v["q"]) + ",\n"
            "   t: [" + tags + "]}"
        )
    return "var AW_VOICE = [\n" + ",\n".join(rows) + "\n];\n"


def main():
    s = io.open(BUILD_PY, encoding="utf-8").read()

    # ---- 1) แทนที่ข้อมูล AW_VOICE ทั้งก้อน ----
    i = s.index("var AW_VOICE = [")
    j = s.index("function awVoices", i)
    old_len = j - i
    s = s[:i] + build_block() + "\n" + s[j:]
    print("AW_VOICE replaced:", old_len, "->", len(build_block()))

    # ---- 2) เพิ่มการแสดงผลหมวดถนัด (d) ลงในการ์ด ----
    old_card = (
        "'<span><span class=\"nm\">' + v.n + '</span><span class=\"rl\">' + v.r + '</span></span></div>' +"
    )
    new_card = (
        "'<span><span class=\"nm\">' + v.n + '</span>' +\n"
        "        (v.d ? '<span class=\"dm\">' + v.d + '</span>' : \"\") +\n"
        "        '<span class=\"rl\">' + v.r + '</span></span></div>' +"
    )
    if s.count(old_card) != 1:
        raise SystemExit("ABORT: card markup anchor not found exactly once")
    s = s.replace(old_card, new_card)
    print("card markup updated")

    # ---- 3) เพิ่ม CSS ของหมวดถนัด ต่อท้ายกฎ .aw-vc .nm ----
    anchor = "  .aw-vc .rl { display: block; margin-top: 3px; font-size: 11px; line-height: 1.5;\n    color: #E8D9A6; }"
    css = (
        "  .aw-vc .dm { display: inline-block; margin-top: 5px; font-family: 'IBM Plex Sans', sans-serif;\n"
        "    font-size: 10px; font-weight: 700; letter-spacing: 0.04em; color: #14120C;\n"
        "    background: linear-gradient(160deg, #E6CE86 0%, #C9A227 100%);\n"
        "    border-radius: 999px; padding: 2px 9px; }\n"
        "  .aw-vc .rl { display: block; margin-top: 5px; font-size: 11px; line-height: 1.5;\n"
        "    color: #E8D9A6; }"
    )
    if s.count(anchor) != 1:
        raise SystemExit("ABORT: CSS anchor not found exactly once")
    s = s.replace(anchor, css)
    print("CSS added")

    io.open(BUILD_PY, "w", encoding="utf-8").write(s)
    print("OK")


if __name__ == "__main__":
    main()
