# -*- coding: utf-8 -*-
"""
Inject 5 real WCB news articles into build-mockup.py, replacing placeholder
featured-article slots. One-shot helper script, not part of the regular build.
Run once from C:\\RedStarTrust\\Noting, then delete or keep for reference.
"""
import json
import os

NEWS_DIR = r"C:\RedStarTrust\News"
BUILD_PY = r"C:\RedStarTrust\Noting\design\build-mockup.py"

ARTICLES_DATA = [
    {
        "slug": "thai-broker-market-share-18-aug-2026",
        "c": "stocks",
        "d": "2026-08-28",
        "m": 4,
        "t": "มาร์เก็ตแชร์โบรกเกอร์ 18 ส.ค. 69 KKPS นำที่ 24.33% ทิ้งห่างอันดับสองเกือบ 3 เท่า",
        "x": "รายงานส่วนแบ่งตลาดโบรกเกอร์ประจำวันที่ 18 ส.ค. 2569 บล.เกียรตินาคินภัทร (KKPS) ครองอันดับหนึ่งที่ 24.33% ขณะที่ KGI ตามมาที่ 9.19% และ JPM ที่ 8.25% บนมูลค่าการซื้อขายหลักทรัพย์รวมทั้งวัน 83,308.95 ล้านบาท",
        "cap": "KKPS ครองมาร์เก็ตแชร์อันดับหนึ่งที่ 24.33% ในวันที่ 18 ส.ค. 2569 — ข้อมูลจาก Aspen/ตลาดหลักทรัพย์แห่งประเทศไทย",
        "key": [
            "KKPS ครองมาร์เก็ตแชร์อันดับหนึ่งที่ 24.33%",
            "อันดับสอง KGI อยู่ที่ 9.19% ห่างกันเกือบ 3 เท่า",
            "มูลค่าซื้อขายรวมทั้งตลาดวันนั้น 83,308.95 ล้านบาท",
        ],
        "s": [
            [
                "ภาพรวมของวัน",
                "วันซื้อขายวันเดียว โบรกเกอร์รายเดียวรับคำสั่งซื้อขายไว้เกือบหนึ่งในสี่ของทั้งตลาด รายงานส่วนแบ่งตลาด 10 อันดับสูงสุดประจำวันที่ <b>18 ส.ค. 2569</b> ระบุว่า <b>บล.เกียรตินาคินภัทร (KKPS)</b> ครองอันดับหนึ่งที่ <b>24.33%</b> บนมูลค่าการซื้อขายรวมทั้งวัน <b>83,308.95 ล้านบาท</b>",
                "อันดับสองอย่าง <b>KGI อยู่ที่ 9.19%</b> ตามด้วย JPM 8.25% และ UBS 5.91% — กลุ่มนี้เรียงตัวกันในกรอบใกล้เคียงกัน ขณะที่หัวตารางยืนอยู่คนละระดับ",
            ],
            [
                "ช่องว่างที่บอกอะไรได้บ้าง",
                "ตัวเลข 24.33% ของ KKPS ทิ้งห่างอันดับสองไปเกือบสามเท่า สะท้อนว่ากระแสคำสั่งซื้อขายของวันนั้นกระจุกตัวอยู่ที่โบรกเกอร์รายเดียวมากเป็นพิเศษ ส่วนอันดับ 5–10 (MST, CGSI, BLS, KINGSFORD, FSS, INVX) เกาะกลุ่มกันแคบในกรอบ 2.82–5.21%",
            ],
            [
                "อ่านตารางนี้อย่างไร",
                "เกณฑ์จัดอันดับคือมูลค่ารวมคำสั่งซื้อ-ขายที่นักลงทุนส่งผ่านนายหน้าแต่ละราย ไม่ใช่ผลประกอบการหรือขนาดสินทรัพย์ของโบรกเกอร์ และเป็นภาพของ <b>วันซื้อขายวันเดียว</b> ไม่ใช่ส่วนแบ่งสะสมรายเดือนหรือรายปี ข้อมูลจาก Aspen/ตลาดหลักทรัพย์แห่งประเทศไทย เผยแพร่ 19 ส.ค. 2569",
            ],
        ],
    },
    {
        "slug": "nasdaq-trading-halt-rules-update-2026",
        "c": "stocks",
        "d": "2026-08-28",
        "m": 4,
        "t": "Nasdaq ปรับกฎหยุดพักการซื้อขาย มีผล 10 ส.ค. 2026 ครอบคลุมสามตลาดในเครือ",
        "x": "Nasdaq ออกประกาศ Equity Trader Alert #2026-38 แก้ไขกฎการหยุดพักการซื้อขายให้สอดคล้องกันทั้งสามตลาดในเครือ ได้แก่ Nasdaq, Nasdaq Texas และ Nasdaq PSX มีผล 10 สิงหาคม 2026",
        "cap": "Nasdaq แก้ไขกฎการหยุดพักการซื้อขายให้เป็นชุดเดียวกันทั้งสามตลาดในเครือ มีผล 10 สิงหาคม 2026",
        "key": [
            "มีผลบังคับ 10 สิงหาคม 2026 กับ Nasdaq, Nasdaq Texas และ Nasdaq PSX",
            "จัดระเบียบ 3 เรื่อง: อำนาจสั่งหยุด, ขั้นตอนเปิดซื้อขายใหม่, การหยุดเชิงปฏิบัติการ",
            "อ้างอิงเอกสารยื่นกฎ 4 ฉบับ รวมถึง Nasdaq UTP Amendment 50",
        ],
        "s": [
            [
                "ประกาศคืออะไร มีผลเมื่อไร",
                "เอกสารฉบับนี้คือ <b>Equity Trader Alert #2026-38</b> ซึ่ง Nasdaq ออกประกาศเมื่อ 8 กรกฎาคม 2026 และให้มีผลบังคับใช้ตั้งแต่ <b>10 สิงหาคม 2026</b> ครอบคลุมสามตลาด: The Nasdaq Stock Market, Nasdaq Texas (NTX) และ Nasdaq PSX",
                "การแก้ไขจัดระเบียบเรื่องหลักไว้สามเรื่อง ทั้งหมดว่าด้วยการหยุดพักการซื้อขาย (trading halt) หรือการที่ตลาดสั่งพักซื้อขายหลักทรัพย์ตัวใดตัวหนึ่งไว้ชั่วคราว",
            ],
            [
                "สามเรื่องที่ถูกจัดระเบียบใหม่",
                "1) <b>อำนาจสั่งหยุดเชิงกำกับดูแล</b> — แยกการหยุดตามดุลพินิจกับการหยุดภาคบังคับออกจากกันชัดเจน 2) <b>ขั้นตอนกลับมาเปิดซื้อขาย</b> — กำหนดว่าตลาดที่หุ้นจดทะเบียนหลักจะเริ่มกระบวนการอย่างไร 3) <b>การหยุดเชิงปฏิบัติการ</b> — ตลาดในเครือมีดุลพินิจสั่งหยุดเฉพาะตลาดของตัวเองได้",
            ],
            [
                "เอกสารอ้างอิงและการเตรียมระบบ",
                "การแก้ไขอ้างอิงเอกสารยื่นกฎรวม 4 ฉบับ รวมถึง Nasdaq UTP Amendment 50 และเปิดให้ทดสอบระบบ Saturday UAT ในวันที่ 8 สิงหาคม 2026 ก่อนกฎใหม่มีผลจริง 10 สิงหาคม 2026",
            ],
        ],
    },
    {
        "slug": "ice-economic-indicator-futures-launch",
        "c": "futures",
        "d": "2026-08-28",
        "m": 5,
        "t": "ICE เปิดฟิวเจอร์สอิงตัวชี้วัดเศรษฐกิจชุดแรก พนันทิศทางดอกเบี้ยเฟด ECB และ BoE",
        "x": "Intercontinental Exchange ประกาศเตรียมเปิดสัญญาฟิวเจอร์สอิงตัวชี้วัดเศรษฐกิจชุดแรกของบริษัท อ้างอิงมติอัตราดอกเบี้ยของธนาคารกลางสหรัฐ ยุโรป และอังกฤษ พร้อมสัญญาอิงคลังก๊าซธรรมชาติสหรัฐ กำหนดเปิดซื้อขาย 10 สิงหาคม 2026",
        "cap": "ICE เตรียมเปิดฟิวเจอร์สอิงมติดอกเบี้ยของเฟด ECB และ BoE พร้อมสัญญาอิงคลังก๊าซธรรมชาติสหรัฐ",
        "key": [
            "ฟิวเจอร์สอิงมติดอกเบี้ยของเฟด ECB และ BoE เป็นชุดแรกของ ICE",
            "เพิ่มสัญญาอิงระดับก๊าซธรรมชาติในคลังสหรัฐที่ EIA เผยแพร่รายสัปดาห์",
            "กำหนดเปิดซื้อขาย 10 สิงหาคม 2026 ขึ้นกับการดำเนินการด้านกำกับดูแล",
        ],
        "s": [
            [
                "ICE ประกาศอะไร",
                "Intercontinental Exchange, Inc. (NYSE: ICE) ประกาศเมื่อ 29 มิถุนายน 2026 เตรียมเปิด <b>สัญญาฟิวเจอร์สอิงตัวชี้วัดเศรษฐกิจชุดแรกของบริษัท</b> — จุดต่างจากฟิวเจอร์สทั่วไปคือสัญญาชุดนี้ผูกกับผลการตัดสินใจเชิงนโยบายและตัวเลขที่หน่วยงานรัฐประกาศ ไม่ใช่ราคาน้ำมันหรือดัชนีหุ้นแบบเดิม",
            ],
            [
                "สัญญาอิงอะไรบ้าง",
                "กลุ่มแรกอิง <b>มติอัตราดอกเบี้ยของธนาคารกลางสหรัฐ ธนาคารกลางยุโรป และธนาคารกลางอังกฤษ</b> ตามรอบประชุมนโยบายที่กำหนดไว้ล่วงหน้า กลุ่มที่สองอิง <b>ระดับก๊าซธรรมชาติในคลังของสหรัฐ</b> ที่ EIA เผยแพร่รายสัปดาห์ ทั้งหมดเป็นสัญญาชำระราคาด้วยเงินสด (cash-settled) ซื้อขายบนตลาดและหักบัญชีผ่านสำนักหักบัญชีกลาง",
            ],
            [
                "กำหนดการและที่มา",
                "ประกาศเผยแพร่ผ่าน BUSINESS WIRE กำหนดวันเปิดซื้อขายไว้ที่ <b>10 สิงหาคม 2026 ขึ้นอยู่กับการดำเนินการด้านกำกับดูแลให้แล้วเสร็จ</b> สัญญาชุดนี้ตามมาหลัง ICE เพิ่งเปิดบริการ ICE Polymarket Signals and Sentiment ซึ่งให้ฟีดข้อมูลความน่าจะเป็นจากตลาดทำนายเช่นกัน",
            ],
        ],
    },
    {
        "slug": "sec-thailand-major-shareholder-futures-rules",
        "c": "futures",
        "d": "2026-08-28",
        "m": 5,
        "t": "ก.ล.ต. ขยายนิยามผู้ถือหุ้นรายใหญ่ธุรกิจฟิวเจอร์ส นับรวมคู่สมรสและอำนาจตั้งถอดกรรมการ",
        "x": "ก.ล.ต. ปรับปรุงหลักเกณฑ์ผู้ถือหุ้นรายใหญ่ของผู้ประกอบธุรกิจสัญญาซื้อขายล่วงหน้าให้สอดคล้องกับธุรกิจหลักทรัพย์และสินทรัพย์ดิจิทัล มีผล 16 สิงหาคม 2026 ให้ผู้ประกอบธุรกิจทบทวนสถานะผู้ถือหุ้นภายใน 180 วัน",
        "cap": "หลักเกณฑ์ผู้ถือหุ้นรายใหญ่ฉบับใหม่ของ ก.ล.ต. สำหรับธุรกิจสัญญาซื้อขายล่วงหน้า มีผล 16 สิงหาคม 2026",
        "key": [
            "หลักเกณฑ์มีผลบังคับ 16 สิงหาคม 2026",
            "นิยามครอบคลุมผู้มีอำนาจตั้งหรือถอดกรรมการตั้งแต่กึ่งหนึ่ง ทั้งทางตรงและทางอ้อม",
            "ผู้ประกอบธุรกิจต้องทบทวนสถานะผู้ถือหุ้นและยื่นขอความเห็นชอบภายใน 180 วัน",
        ],
        "s": [
            [
                "ก.ล.ต. ปรับอะไร",
                "สำนักงานคณะกรรมการกำกับหลักทรัพย์และตลาดหลักทรัพย์ (ก.ล.ต.) ปรับปรุงหลักเกณฑ์ผู้ถือหุ้นรายใหญ่ของ <b>ผู้ประกอบธุรกิจสัญญาซื้อขายล่วงหน้า</b> ให้สอดคล้องกับธุรกิจหลักทรัพย์และธุรกิจสินทรัพย์ดิจิทัล หลักเกณฑ์นี้มีผลใช้บังคับตั้งแต่ <b>16 สิงหาคม 2026</b>",
            ],
            [
                "นิยามใหม่ไล่ไปถึงอำนาจตั้งและถอดกรรมการ",
                "หัวใจของการแก้ไขคือขยายนิยาม \u201cผู้ถือหุ้นรายใหญ่\u201d ให้ครอบคลุมถึงผู้มีอำนาจควบคุมการแต่งตั้งหรือถอดถอนกรรมการตั้งแต่กึ่งหนึ่งของกรรมการทั้งหมด <b>ไม่ว่าทางตรงหรือทางอ้อม</b> — นับรวมคู่สมรส ผู้อยู่กินฉันสามีภริยา บุตรที่ยังไม่บรรลุนิติภาวะ และกรณี acting in concert ที่หลายฝ่ายร่วมกันลงมติไปทางเดียวกัน",
            ],
            [
                "180 วันที่ธุรกิจต้องกลับไปตรวจโครงสร้างตัวเอง",
                "ผู้ประกอบธุรกิจต้องทบทวนสถานะผู้ถือหุ้นรายใหญ่และยื่นขอความเห็นชอบผู้ถือหุ้นที่ยังไม่เคยได้รับความเห็นชอบ <b>ภายใน 180 วัน</b> นับแต่วันที่หลักเกณฑ์มีผลใช้บังคับ ก.ล.ต. ระบุเหตุผลว่าเพื่อเพิ่มความโปร่งใสและลดความเสี่ยงด้านการฟอกเงิน",
            ],
        ],
    },
    {
        "slug": "ic-blast-esports-multi-year-partnership",
        "c": "fx",
        "d": "2026-08-28",
        "m": 5,
        "t": "IC จับมือ BLAST ขยายกลยุทธ์สปอนเซอร์สู่อีสปอร์ต ด้วยดีลหลายปีบนสองเกมของ Valve",
        "x": "BLAST ประกาศตั้ง IC ผู้ให้บริการเทรดออนไลน์ระดับโลก เป็น Official Online Trading Partner ของ BLAST Premier และ BLAST Slam ด้วยสัญญาหลายปี ครอบคลุมระบบนิเวศ Counter-Strike และ Dota 2 ต่อยอดจากพอร์ตสปอนเซอร์เดิมที่มี Formula 1",
        "cap": "IC เข้าเป็น Official Online Trading Partner ของ BLAST Premier และ BLAST Slam ด้วยสัญญาหลายปี",
        "key": [
            "ดีลหลายปีครอบคลุม Counter-Strike และ Dota 2 ของ BLAST",
            "IC เปิดตัวที่ BLAST Premier Bounty มอลตา 25 กรกฎาคม–3 สิงหาคม 2026",
            "เวทีเปิดตัวมี 32 ทีม ชิงเงินรางวัลรวม 1,150,000 ดอลลาร์",
        ],
        "s": [
            [
                "ดีลหลายปีที่พา IC เข้าอีสปอร์ตเป็นครั้งแรก",
                "BLAST บริษัท competitive entertainment ประกาศเมื่อ 14 กรกฎาคม 2026 ที่โคเปนเฮเกน ตั้ง <b>IC</b> เป็น <b>Official Online Trading Partner</b> ของ BLAST Premier และ BLAST Slam ด้วยสัญญาหลายปี ครอบคลุมระบบนิเวศ Counter-Strike และ Dota 2 ระดับนานาชาติของ BLAST — ก้าวแรกของ IC ในอีสปอร์ต",
            ],
            [
                "IC จะไปปรากฏตรงไหนบ้าง",
                "สิทธิ์ที่ได้เดินผ่านการถ่ายทอดสด อีเวนต์ในสนาม คอนเทนต์ออริจินัล และประสบการณ์ออนไลน์บน BLAST.tv จุดที่ใกล้ธุรกิจของ IC ที่สุดคือการเป็นผู้นำเสนอ <b>BLAST Higher Lower</b> เกมทายมูลค่าสกิน Counter-Strike 2 ซึ่งวางอยู่บนมูลค่า การเปรียบเทียบราคา และการตัดสินใจเร็ว — ปัจจัยเดียวกับการเทรดออนไลน์",
            ],
            [
                "ต่อยอดจาก Formula 1 และเวทีเปิดตัว",
                "IC มีสปอนเซอร์มอเตอร์สปอร์ตอยู่ก่อนแล้วผ่านทีม Toyota Gazoo Racing Haas F1 Team โดยผูกทั้งสองดีลไว้กับคำว่าความแม่นยำ ประสิทธิภาพ และเทคโนโลยี BLAST กำหนดให้ <b>BLAST Premier Bounty ที่มอลตา (25 ก.ค.–3 ส.ค. 2026)</b> เป็นเวทีเปิดตัว มี 32 ทีมชิงเงินรางวัลรวม 1,150,000 ดอลลาร์สหรัฐ",
            ],
        ],
    },
]


def load_b64(slug):
    p = os.path.join(NEWS_DIR, slug, "cover.b64.txt")
    with open(p, "r", encoding="ascii") as f:
        return f.read().strip()


def js_str(s):
    return json.dumps(s, ensure_ascii=False)


def build_articles_js():
    parts = []
    for a in ARTICLES_DATA:
        b64 = load_b64(a["slug"])
        img = "data:image/webp;base64," + b64
        parts.append(
            "  {c:" + js_str(a["c"]) + ", d:" + js_str(a["d"]) + ", m:" + str(a["m"]) +
            ",\n   t:" + js_str(a["t"]) + ",\n   x:" + js_str(a["x"]) +
            ",\n   img:" + js_str(img) + "}"
        )
    return ",\n".join(parts)


def build_art_body_js():
    parts = []
    for a in ARTICLES_DATA:
        sections = ",\n       ".join(
            "[" + ",\n        ".join(js_str(line) for line in sec) + "]"
            for sec in a["s"]
        )
        keys = ",\n         ".join(js_str(k) for k in a["key"])
        parts.append(
            "  {cap: " + js_str(a["cap"]) + ",\n" +
            "   s: [" + sections + "],\n" +
            "   key: [" + keys + "]}"
        )
    return ",\n".join(parts)


def main():
    with open(BUILD_PY, "r", encoding="utf-8") as f:
        content = f.read()

    # 1) Insert into ARTICLES array (before its closing "];", which is
    #    immediately followed by "var ART_ART = {")
    art_start = content.index("var ARTICLES = [")
    art_art_start = content.index("var ART_ART = {", art_start)
    block = content[art_start:art_art_start]
    ins = block.rindex("\n];")
    new_articles_js = build_articles_js()
    block = block[:ins] + ",\n" + new_articles_js + block[ins:]
    content = content[:art_start] + block + content[art_art_start:]

    # 2) Insert artCover() right after artArt() function definition
    artfn_start = content.index("function artArt(i){")
    close_idx = content.index("\n}\n", artfn_start) + len("\n}\n")
    art_cover_fn = (
        "function artCover(a, i){\n"
        "  if (a && a.img) {\n"
        "    return '<img class=\"art-art\" src=\"' + a.img + '\" alt=\"\" ' +\n"
        "      'style=\"width:100%;height:100%;object-fit:cover;display:block\" aria-hidden=\"true\">';\n"
        "  }\n"
        "  return artArt(i);\n"
        "}\n"
    )
    content = content[:close_idx] + art_cover_fn + content[close_idx:]

    # 3) Insert into ART_BODY array (before its closing "];", followed by "var naIdx = 0;")
    artbody_start = content.index("var ART_BODY = [")
    naidx_marker = content.index("var naIdx = 0;", artbody_start)
    block = content[artbody_start:naidx_marker]
    ins = block.rindex("\n];")
    new_art_body_js = build_art_body_js()
    block = block[:ins] + ",\n" + new_art_body_js + block[ins:]
    content = content[:artbody_start] + block + content[naidx_marker:]

    # 4) Rewire the 4 cover render call sites from artArt(...) to artCover(a, ...)
    replacements = [
        ("artArt(naIdx)", "artCover(a, naIdx)"),
        ("artArt(x.i)", "artCover(x.a, x.i)"),
        ("artArt(ARTICLES.indexOf(a))", "artCover(a, ARTICLES.indexOf(a))"),
        ("artArt(ix)", "artCover(a, ix)"),
    ]
    for old, new in replacements:
        n = content.count(old)
        if n != 1:
            raise SystemExit("ABORT: expected exactly 1 occurrence of " + repr(old) + " found " + str(n))
        content = content.replace(old, new)

    with open(BUILD_PY, "w", encoding="utf-8") as f:
        f.write(content)

    print("OK: injected 5 articles + 5 bodies, added artCover(), rewired 4 call sites")


if __name__ == "__main__":
    main()
