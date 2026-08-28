# -*- coding: utf-8 -*-
"""ดึงไอคอนแบรนด์จากโดเมนทางการของโบรกเกอร์เอง — อ่าน <link rel=icon> จากหน้าแรกก่อน
ถ้าไม่ได้ค่อยถอยไปใช้บริการ favicon ที่มิเรอร์ไฟล์จากโดเมนเดิม"""
import os, re, ssl, json
from urllib.parse import urljoin
from urllib.request import Request, urlopen

OUT = r"C:\Users\Yotsa\AppData\Local\Temp\claude\C--RedStarTrust\6e517f0d-2b03-4c69-8c22-85120add71b5\scratchpad\logos"
os.makedirs(OUT, exist_ok=True)

SITES = [
    ("exness",      "https://www.exness.com/"),
    ("ic-markets",  "https://www.icmarkets.com/global/en/"),
    ("xm",          "https://www.xm.com/"),
    ("pepperstone", "https://pepperstone.com/en/"),
    ("fp-markets",  "https://www.fpmarkets.com/"),
    ("eightcap",    "https://www.eightcap.com/"),
    ("tickmill",    "https://www.tickmill.com/"),
    ("axi",         "https://www.axi.com/"),
    ("hfm",         "https://www.hfm.com/"),
    ("ig",          "https://www.ig.com/en"),
    ("oanda",       "https://www.oanda.com/"),
    ("equiti",      "https://www.equiti.com/"),
]
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

def get(url, timeout=15):
    r = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    return urlopen(r, timeout=timeout, context=CTX).read()

def sniff(b):
    if b[:8] == b"\x89PNG\r\n\x1a\n": return "png"
    if b[:3] == b"\xff\xd8\xff":      return "jpg"
    if b[:4] == b"RIFF" and b[8:12] == b"WEBP": return "webp"
    if b[:4] == b"\x00\x00\x01\x00":  return "ico"
    head = b[:400].lstrip()
    if head[:5] == b"<?xml" or head[:4] == b"<svg": return "svg"
    return None

def icons_from_html(html, base):
    out = []
    for m in re.finditer(r"<link[^>]+>", html, re.I):
        tag = m.group(0)
        if not re.search(r'rel\s*=\s*["\'][^"\']*icon', tag, re.I):
            continue
        h = re.search(r'href\s*=\s*["\']([^"\']+)', tag, re.I)
        if not h:
            continue
        sz = re.search(r'sizes\s*=\s*["\'](\d+)', tag, re.I)
        n = int(sz.group(1)) if sz else (256 if h.group(1).lower().endswith(".svg") else 32)
        out.append((n, urljoin(base, h.group(1))))
    out.sort(key=lambda t: -t[0])
    return out

results = []
for slug, url in SITES:
    picked = None
    try:
        html = get(url).decode("utf-8", "ignore")
        cands = icons_from_html(html, url)
    except Exception as e:
        cands = []
    for n, u in cands[:6]:
        try:
            b = get(u, 12)
        except Exception:
            continue
        k = sniff(b)
        if k and len(b) > 400:
            open(os.path.join(OUT, slug + "." + k), "wb").write(b)
            picked = (k, len(b), n, u, "โดเมนทางการ")
            break
    if not picked:
        dom = url.split("/")[2].replace("www.", "")
        try:
            b = get("https://icons.duckduckgo.com/ip3/%s.ico" % dom, 12)
            k = sniff(b)
            if k and len(b) > 400:
                open(os.path.join(OUT, slug + "." + k), "wb").write(b)
                picked = (k, len(b), "?", dom, "บริการ favicon (มิเรอร์จากโดเมนเดิม)")
        except Exception:
            pass
    results.append((slug, picked))
    print("%-12s %s" % (slug, ("%s %sB size=%s  [%s]" % (picked[0], picked[1], picked[2], picked[4])) if picked else "FAILED"))

json.dump([{"slug": s, "ok": bool(p), "kind": p[0] if p else None,
            "bytes": p[1] if p else 0, "src": p[3] if p else None,
            "how": p[4] if p else None} for s, p in results],
          open(os.path.join(OUT, "_manifest.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("\nได้", sum(1 for _, p in results if p), "จาก", len(results))
