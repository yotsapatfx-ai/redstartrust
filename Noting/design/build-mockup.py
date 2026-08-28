# -*- coding: utf-8 -*-
"""แปลง Main.dc.html เป็นหน้า mockup เดี่ยว ๆ ที่เปิดดูได้เลย (Figma-frame style)"""
import io, re, os

SRC = r"C:\RedStarTrust\Noting\design\Main.dc.html"
OUT = r"C:\RedStarTrust\Noting\design\redstartrust-homepage-mockup.html"

src = io.open(SRC, encoding="utf-8").read()

helmet = re.search(r"<helmet>(.*?)</helmet>", src, re.S).group(1).strip()
body = re.search(r"</helmet>(.*?)</x-dc>", src, re.S).group(1).strip()

HEAD = """<title>RedStarTrust Homepage</title>
""" + helmet + """
<style>
  :root { color-scheme: light; }
  html, body { margin: 0; background: #E7E9EE; }
  body { font-family: Inter, 'IBM Plex Sans Thai', system-ui, sans-serif; }
  .stage { padding: 28px 24px 56px; }
  .bar {
    max-width: 1440px; margin: 0 auto 14px; display: flex; align-items: center;
    justify-content: space-between; gap: 16px; flex-wrap: wrap;
  }
  .lbl {
    font-family: 'IBM Plex Sans', Inter, sans-serif; font-size: 12.5px; font-weight: 600;
    letter-spacing: 0.04em; text-transform: uppercase; color: #5C6675;
  }
  .lbl b { color: #101828; font-weight: 600; }
  .zoom { display: flex; gap: 6px; }
  .zoom button {
    font: inherit; font-size: 12.5px; font-weight: 500; color: #475467; background: #FFFFFF;
    border: 1px solid #D0D5DD; border-radius: 999px; padding: 5px 14px; cursor: pointer;
  }
  .zoom button[aria-pressed="true"] { background: #D92D20; border-color: #D92D20; color: #FFFFFF; }
  .zoom button:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }
  .viewport { overflow: auto; }
  .frame {
    margin: 0 auto; background: #FFFFFF; box-shadow: 0 24px 60px -20px rgba(16,24,40,0.28);
    transform-origin: top left; width: 1440px;
  }
  .map-svg path { fill: #E4E7EC; stroke: #FFFFFF; stroke-width: 0.6; }
  .map-svg path[data-hi="1"] { fill: #D0D5DD; }
  .map-svg path[data-vol="1"] { fill: #F7CFCB; }
  .map-svg path[data-vol="2"] { fill: #EDA49D; }
  .map-svg path[data-vol="3"] { fill: #E0655B; }
  .map-svg path[data-vol="4"] { fill: #B42318; }

  /* ── แถบอธิบายสีวอลลุ่มใต้แผนที่ ── */
  .vol-key { display: flex; align-items: center; gap: 8px 14px; flex-wrap: wrap;
    margin-top: 13px; font-size: 11.5px; color: #667085; line-height: 1.5; }
  .vol-key .t { font-weight: 600; color: #475467; }
  .vol-key select {
    appearance: none; -webkit-appearance: none; font: inherit; font-size: 11.5px; font-weight: 600;
    color: #101828; background-color: #FFFFFF;
    background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%23475467' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
    background-repeat: no-repeat; background-position: right 8px center;
    border: 1px solid #D0D5DD; border-radius: 8px; padding: 4px 25px 4px 9px;
    cursor: pointer; transition: border-color .15s;
  }
  .vol-key select:hover { border-color: #98A2B3; }
  .vol-key select:focus-visible { outline: none; border-color: #D92D20; box-shadow: 0 0 0 3px #FEF3F2; }
  .vz-tag { font-size: 11.5px; font-weight: 600; color: #B42318; background: #FEF3F2;
    border: 1px solid #FECDCA; border-radius: 999px; padding: 3px 10px; }
  .vol-scale { display: inline-flex; align-items: center; gap: 7px; }
  .vol-scale i { display: inline-flex; gap: 3px; }
  .vol-scale i b { width: 22px; height: 9px; border-radius: 2px; display: block; }
  .vol-na { display: inline-flex; align-items: center; gap: 6px; }
  .vol-na b { width: 12px; height: 9px; border-radius: 2px; background: #E4E7EC;
    border: 1px solid #D0D5DD; display: block; }

  /* ── วอลลุ่มการเทรดรายโซน ── */
  .vol-zones { margin-top: 40px; border: 1px solid #EAECF0; border-radius: 16px;
    background: #FFFFFF; overflow: hidden; }
  .vz-head { display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap;
    padding: 15px 20px; border-bottom: 1px solid #EAECF0; background: #F5F7FA; }
  .vz-head h3 { margin: 0; font-size: 16px; font-weight: 600; letter-spacing: -0.01em; color: #101828; }
  .vz-head span { font-size: 12.5px; color: #667085; }
  .vz-row { display: grid; grid-template-columns: 176px minmax(0, 1.05fr) 74px minmax(0, 1.6fr);
    align-items: center; gap: 18px; padding: 12px 20px; border-bottom: 1px solid #F5F7FA; }
  .vz-row:last-child { border-bottom: 0; }
  .vz-name { font-size: 14px; font-weight: 600; color: #101828; letter-spacing: -0.01em; }
  .vz-name i { display: block; font-style: normal; font-size: 11.5px; font-weight: 400;
    color: #667085; margin-top: 2px; }
  .vz-bar { height: 13px; border-radius: 999px; background: #F2F4F7;
    border: 1px solid #E4E7EC; overflow: hidden; }
  .vz-bar b { display: block; height: 100%; border-radius: 999px;
    background: linear-gradient(90deg, #E8483E, #D92D20); }
  .vz-pct { font-family: 'IBM Plex Sans', sans-serif; font-size: 15px; font-weight: 700;
    font-variant-numeric: tabular-nums; color: #101828; text-align: right; }
  .vz-top { display: flex; gap: 5px 18px; flex-wrap: wrap; font-size: 12.5px; color: #667085; }
  .vz-top b { color: #475467; font-weight: 600; }
  .vz-note { margin: 0; padding: 12px 20px; background: #F5F7FA; border-top: 1px solid #EAECF0;
    font-size: 11.5px; line-height: 1.6; color: #667085; }
  .vz-note b { color: #475467; font-weight: 600; }

  /* ── บทความและข่าว ── */
  .art-head { display: flex; flex-direction: column; gap: 9px; margin-bottom: 24px; max-width: 820px; }
  /* เส้นแดงคั่นหัวบล็อก — ใช้เหมือนกันทุกบล็อกทั้งห้าหน้า */
  .sec-rule { display: block; height: 2px; background: #D92D20; border-radius: 2px; margin-bottom: 26px; }
  /* คำว่า Red ในชื่อแบรนด์เป็นสีแดง ทั้งหัวเว็บ ท้ายเว็บ และหัวข้อ RED STAR */
  .wm-red { color: #D92D20 !important; font-style: normal; }

  /* ── หน้าต่างตัวอย่าง EA ── */
  .ea-modal { position: fixed; inset: 0; z-index: 90; display: flex; align-items: center;
    justify-content: center; padding: 32px 20px; }
  .ea-mask { position: absolute; inset: 0; background: rgba(16,24,40,0.55); }
  .ea-dlg { position: relative; z-index: 1; width: 100%; max-width: 1040px; max-height: 88vh;
    display: flex; flex-direction: column; background: #FFFFFF; border-radius: 18px;
    box-shadow: 0 32px 64px -20px rgba(16,24,40,0.4); overflow: hidden; }
  .ea-dtop { display: flex; align-items: flex-start; justify-content: space-between; gap: 16px;
    padding: 20px 24px 16px; border-bottom: 1px solid #EAECF0; }
  .ea-dtop h3 { margin: 7px 0 0; font-size: 21px; font-weight: 700; letter-spacing: -0.02em; color: #101828; }
  .ea-x { width: 34px; height: 34px; border-radius: 50%; border: 1px solid #EAECF0; background: #FFFFFF;
    color: #667085; font-size: 21px; line-height: 1; cursor: pointer; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center; transition: border-color .15s, color .15s; }
  .ea-x:hover { border-color: #D0D5DD; color: #101828; }
  .ea-x:focus-visible, .ea-dfoot a:focus-visible, .ea-dfoot button:focus-visible {
    outline: 2px solid #D92D20; outline-offset: 2px; }
  .ea-dbody { display: grid; grid-template-columns: minmax(0, 1.08fr) minmax(0, 1fr);
    gap: 24px; padding: 22px 24px; overflow-y: auto; }
  .ea-dfoot { display: flex; align-items: center; gap: 12px; flex-wrap: wrap;
    padding: 16px 24px; border-top: 1px solid #EAECF0; background: #F5F7FA; }
  .ea-fnote { flex: 1; min-width: 220px; font-size: 11.5px; line-height: 1.6; color: #667085; }
  .ea-fnote b { color: #B42318; font-weight: 700; }

  /* จำลองหน้าจอ MetaTrader */
  .mt-win { border: 1px solid #1D2939; border-radius: 12px; overflow: hidden; background: #0F1620; }
  .mt-bar { display: flex; align-items: center; gap: 8px; padding: 9px 12px; background: #101828;
    border-bottom: 1px solid #1D2939; font-size: 11.5px; color: #98A2B3; }
  .mt-bar i { width: 9px; height: 9px; border-radius: 50%; background: #344054; display: inline-block; }
  .mt-stage { position: relative; height: 190px; }
  .mt-stage svg { display: block; width: 100%; height: 100%; }
  .mt-panel { position: absolute; right: 12px; top: 12px; width: 178px; background: rgba(16,24,40,0.94);
    border: 1px solid #344054; border-radius: 9px; overflow: hidden; }
  .mt-panel .hd { display: flex; align-items: center; gap: 6px; padding: 7px 10px;
    background: #D92D20; color: #FFFFFF; font-size: 10.5px; font-weight: 700; letter-spacing: 0.03em; }
  .mt-panel .rw { display: flex; align-items: baseline; justify-content: space-between; gap: 8px;
    padding: 6px 10px; border-bottom: 1px solid #1D2939; font-size: 11px; color: #98A2B3; }
  .mt-panel .rw:last-child { border-bottom: 0; }
  .mt-panel .rw b { font-family: 'IBM Plex Sans', sans-serif; font-size: 12.5px;
    font-weight: 700; color: #FFFFFF; }
  .mt-panel .rw b.g { color: #6CE9A6; }
  .mt-panel .rw b.r { color: #FDA29B; }
  .mt-cap { margin: 10px 0 0; font-size: 11.5px; line-height: 1.65; color: #667085; }

  .ea-det h5 { margin: 0 0 9px; font-size: 12px; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; color: #B42318; }
  .ea-det > p { margin: 0 0 18px; font-size: 13.5px; line-height: 1.7; color: #475467; }
  .ea-steps { margin: 0 0 18px; padding: 0; list-style: none; counter-reset: st;
    display: flex; flex-direction: column; gap: 11px; }
  .ea-steps li { counter-increment: st; position: relative; padding-left: 32px;
    font-size: 13px; line-height: 1.65; color: #475467; }
  .ea-steps li::before { content: counter(st); position: absolute; left: 0; top: 0;
    width: 22px; height: 22px; border-radius: 7px; background: #FEF3F2; color: #B42318;
    font-family: 'IBM Plex Sans', sans-serif; font-size: 11.5px; font-weight: 700;
    display: flex; align-items: center; justify-content: center; }
  .ea-req { display: flex; flex-wrap: wrap; gap: 7px; }
  .ea-req span { font-size: 12px; color: #475467; background: #F5F7FA; border: 1px solid #EAECF0;
    border-radius: 999px; padding: 5px 11px; }

  /* ตัวเลขขยับ + บันทึกเหตุการณ์ไหลเข้า */
  .mt-panel .hd .live { margin-left: auto; display: inline-flex; align-items: center; gap: 5px;
    font-size: 9.5px; letter-spacing: 0.06em; }
  .mt-panel .hd .live i { width: 6px; height: 6px; border-radius: 50%; background: #FFFFFF;
    display: inline-block; animation: eapulse 1.5s ease-in-out infinite; }
  @keyframes eapulse { 0%,100% { opacity: 1; } 50% { opacity: .25; } }
  .mt-panel .rw b { transition: color .18s, background-color .18s; border-radius: 4px; padding: 0 3px; }
  .mt-panel .rw b.tick { background: rgba(217,45,32,0.35); color: #FFFFFF; }
  .mt-feed { margin-top: 10px; border: 1px solid #1D2939; border-radius: 11px;
    background: #0F1620; overflow: hidden; }
  .mt-fhd { display: flex; align-items: center; gap: 9px; padding: 8px 12px;
    background: #101828; border-bottom: 1px solid #1D2939; font-size: 11px; color: #98A2B3; }
  .mt-fhd b { color: #FFFFFF; font-weight: 600; font-size: 11.5px; }
  .mt-fhd .cnt { margin-left: auto; font-family: 'IBM Plex Sans', sans-serif; font-size: 11px; color: #98A2B3; }
  .mt-fbtn { border: 1px solid #344054; background: transparent; color: #98A2B3; border-radius: 7px;
    padding: 3px 9px; font: inherit; font-size: 10.5px; cursor: pointer; transition: color .15s, border-color .15s; }
  .mt-fbtn:hover { color: #FFFFFF; border-color: #667085; }
  .mt-fbtn:focus-visible { outline: 2px solid #D92D20; outline-offset: 1px; }
  .mt-rows { height: 112px; overflow: hidden;
    -webkit-mask-image: linear-gradient(180deg, #000 0, #000 84px, rgba(0,0,0,0) 112px);
    mask-image: linear-gradient(180deg, #000 0, #000 84px, rgba(0,0,0,0) 112px); }
  .mt-row { display: flex; align-items: flex-start; gap: 9px; padding: 7px 12px;
    border-bottom: 1px solid #161F2C; font-size: 11.5px; line-height: 1.5; color: #98A2B3;
    animation: eain .35s ease both; }
  @keyframes eain { from { opacity: 0; transform: translateY(-6px); } to { opacity: 1; transform: none; } }
  .mt-row time { font-family: 'IBM Plex Sans', sans-serif; font-size: 10.5px; color: #98A2B3;
    flex-shrink: 0; padding-top: 1px; }
  .mt-tag { flex-shrink: 0; font-size: 9.5px; font-weight: 700; letter-spacing: 0.05em;
    border-radius: 5px; padding: 2px 6px; }
  .mt-tag.open { background: rgba(6,118,71,0.22); color: #6CE9A6; }
  .mt-tag.close { background: rgba(180,35,24,0.24); color: #FDA29B; }
  .mt-tag.log { background: rgba(152,162,179,0.16); color: #C3C9D5; }
  .mt-tag.send { background: rgba(217,45,32,0.24); color: #FFFFFF; }
  .mt-row span b { color: #E4E7EC; font-weight: 600; }

  /* \u0e41\u0e16\u0e1a\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e42\u0e1a\u0e23\u0e01\u0e2d\u0e37\u0e48\u0e19 */
  .mt-cmp { margin-top: 12px; border: 1px solid #EAECF0; border-left: 4px solid #D92D20;
    border-radius: 12px; background: #FFFFFF; padding: 15px 17px 16px; }
  .mt-cmph { display: flex; align-items: baseline; gap: 9px; margin-bottom: 11px; }
  .mt-cmph b { font-size: 12.5px; font-weight: 700; color: #101828; }
  .mt-cmph span { margin-left: auto; font-size: 10.5px; color: #667085; }
  .mt-vd { display: flex; align-items: baseline; gap: 10px; margin: 0 0 13px; }
  .mt-vd em { font-style: normal; font-family: 'IBM Plex Sans', sans-serif; font-size: 31px;
    font-weight: 700; line-height: 1; letter-spacing: -0.02em; }
  .mt-vd em.bad { color: #B42318; }
  .mt-vd em.good { color: #067647; }
  .mt-vd i { font-style: normal; font-size: 12px; line-height: 1.45; color: #475467; }
  .mt-cr { display: grid; grid-template-columns: 148px minmax(0, 1fr) 78px;
    align-items: center; gap: 11px; margin-bottom: 8px; font-size: 11.5px; color: #475467; }
  .mt-cr:last-of-type { margin-bottom: 0; }
  .mt-cr.me { color: #101828; font-weight: 700; }
  .mt-ct { height: 10px; border-radius: 5px; background: #F2F4F7; overflow: hidden; }
  .mt-ct i { display: block; height: 100%; border-radius: 5px; background: #D0D5DD;
    transition: width .55s ease, background .3s; }
  .mt-cr.me .mt-ct i { background: #D92D20; }
  .mt-cr.me.good .mt-ct i { background: #067647; }
  .mt-cr.best .mt-ct i { background: #667085; }
  .mt-cv { text-align: right; font-family: 'IBM Plex Sans', sans-serif;
    font-size: 11.5px; color: #101828; }
  .mt-cr.me .mt-cv { font-size: 13.5px; font-weight: 700; }
  .mt-rank { margin-top: 12px; padding-top: 11px; border-top: 1px solid #F2F4F7;
    font-size: 11.5px; line-height: 1.6; color: #475467; }
  .mt-rank b { color: #B42318; font-weight: 700; }

  /* ── RedStar EA Suite ── */
  .ea-dash { border: 1px solid #EAECF0; border-radius: 18px; background: #FFFFFF; overflow: hidden;
    margin-bottom: 34px; }
  .ea-dhead { display: flex; align-items: center; justify-content: space-between; gap: 16px;
    flex-wrap: wrap; padding: 15px 22px; background: #101828; }
  .ea-dhead h3 { margin: 0; font-size: 15.5px; font-weight: 600; color: #FFFFFF; letter-spacing: -0.01em; }
  .ea-dhead span { font-size: 12px; color: #98A2B3; }
  .ea-tiles { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));
    border-bottom: 1px solid #EAECF0; }
  .ea-tile { padding: 20px 22px; border-right: 1px solid #F0F2F5; }
  .ea-tile:last-child { border-right: 0; }
  .ea-tile .ic { width: 32px; height: 32px; border-radius: 9px; background: #FEF3F2;
    display: flex; align-items: center; justify-content: center; margin-bottom: 11px; }
  .ea-tile .lb { display: block; font-size: 13px; font-weight: 600; color: #475467; }
  .ea-tile .vl { display: block; font-family: 'IBM Plex Sans', sans-serif; font-size: 30px;
    font-weight: 700; letter-spacing: -0.035em; color: #101828; line-height: 1.1; margin: 5px 0 4px; }
  .ea-tile .sb { display: block; font-size: 11.5px; color: #667085; }
  .ea-panes { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .ea-pane { padding: 20px 22px; border-right: 1px solid #F0F2F5; }
  .ea-pane:last-child { border-right: 0; }
  .ea-pane h4 { margin: 0 0 13px; font-size: 14px; font-weight: 600; color: #101828; letter-spacing: -0.01em; }
  .ea-hist { background: #F5F7FA; border: 1px solid #EAECF0; border-radius: 10px;
    padding: 10px 13px; font-size: 12.5px; color: #475467; }
  .ea-arrow { width: 1px; height: 16px; background: #D0D5DD; margin: 0 auto; }
  .ea-save { border: 1.5px solid #067647; background: #F0FBF5; border-radius: 12px; padding: 13px 15px; }
  .ea-save b { display: block; font-size: 14.5px; font-weight: 700; color: #05603A; }
  .ea-save span { display: block; font-size: 12px; color: #067647; margin: 3px 0 2px; }
  .ea-save em { font-style: normal; font-family: 'IBM Plex Sans', sans-serif; font-size: 25px;
    font-weight: 700; letter-spacing: -0.03em; color: #05603A; }
  .ea-kv { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .ea-k { border: 1px solid #EAECF0; border-radius: 11px; padding: 12px 13px; }
  .ea-k .st { display: flex; align-items: center; gap: 6px; font-size: 11.5px; font-weight: 600; }
  .ea-k .st.ok { color: #067647; }
  .ea-k .st.warn { color: #B54708; }
  .ea-k .nm { display: block; font-size: 12.5px; color: #475467; margin: 7px 0 2px; }
  .ea-k .vv { display: block; font-family: 'IBM Plex Sans', sans-serif; font-size: 21px;
    font-weight: 700; letter-spacing: -0.03em; color: #101828; }
  .ea-al { border-radius: 11px; padding: 11px 13px; margin-bottom: 9px; }
  .ea-al:last-child { margin-bottom: 0; }
  .ea-al.hi { background: #FEF3F2; border: 1px solid #FECDCA; }
  .ea-al.md { background: #FEF6EE; border: 1px solid #F5DFC4; }
  .ea-al b { display: flex; align-items: center; gap: 7px; font-size: 13.5px; font-weight: 600; color: #101828; }
  .ea-al i { width: 8px; height: 8px; border-radius: 50%; display: inline-block; }
  .ea-al.hi i { background: #D92D20; }
  .ea-al.md i { background: #F5A623; }
  .ea-al span { display: block; font-size: 12px; line-height: 1.6; color: #475467; margin-top: 4px; }
  .ea-dnote { padding: 12px 22px; background: #F5F7FA; border-top: 1px solid #EAECF0;
    font-size: 11.5px; line-height: 1.7; color: #667085; }
  .ea-dnote b { color: #475467; font-weight: 600; }

  .ea-dhead .dlive { display: inline-flex; align-items: center; gap: 6px; font-size: 11px;
    font-weight: 700; letter-spacing: 0.06em; color: #FFFFFF; background: #D92D20;
    border-radius: 999px; padding: 3px 10px 3px 8px; }
  .ea-dhead .dlive i { width: 6px; height: 6px; border-radius: 50%; background: #FFFFFF;
    animation: eapulse 1.5s ease-in-out infinite; }
  .ea-tile .vl.tk { color: #B42318; }
  .ea-tile .cmp { display: block; margin-top: 7px; font-size: 11.5px; line-height: 1.55; color: #667085; }
  .ea-tile .cmp b { font-weight: 700; }
  .ea-tile .cmp b.up { color: #B42318; }
  .ea-tile .cmp b.dn { color: #067647; }
  .ea-panes { grid-template-columns: minmax(0, 1.45fr) minmax(0, 1fr) minmax(0, 1fr); }
  .ea-pane h4 .pill { margin-left: 8px; font-size: 11px; font-weight: 600; color: #B42318;
    background: #FEF3F2; border-radius: 999px; padding: 2px 9px; vertical-align: 1px; }
  .ea-big { display: flex; align-items: baseline; gap: 10px; margin: 0 0 14px; }
  .ea-big em { font-style: normal; font-family: 'IBM Plex Sans', sans-serif; font-size: 34px;
    font-weight: 700; line-height: 1; letter-spacing: -0.03em; color: #B42318; }
  .ea-big em.dn { color: #067647; }
  .ea-big i { font-style: normal; font-size: 12px; line-height: 1.5; color: #475467; }
  .ea-brow { display: grid; grid-template-columns: 150px minmax(0, 1fr) 82px; align-items: center;
    gap: 11px; margin-bottom: 8px; font-size: 11.5px; color: #475467; }
  .ea-brow.me { color: #101828; font-weight: 700; }
  .ea-btube { height: 10px; border-radius: 5px; background: #F2F4F7; overflow: hidden; }
  .ea-btube i { display: block; height: 100%; border-radius: 5px; background: #D0D5DD;
    transition: width .55s ease; }
  .ea-brow.me .ea-btube i { background: #D92D20; }
  .ea-brow.bs .ea-btube i { background: #067647; }
  .ea-bv { text-align: right; font-family: 'IBM Plex Sans', sans-serif; font-size: 11.5px; color: #101828; }
  .ea-brow.me .ea-bv { font-size: 13.5px; }
  .ea-k .vv.tk { color: #B42318; }
  .ea-al .ct { font-family: 'IBM Plex Sans', sans-serif; font-weight: 700; color: #B42318; }

  /* \u0e2b\u0e19\u0e49\u0e32\u0e15\u0e48\u0e32\u0e07\u0e41\u0e2a\u0e14\u0e07\u0e1c\u0e25\u0e1a\u0e2d\u0e01\u0e2d\u0e30\u0e44\u0e23 */
  .ea-lg { border: 1px solid #EAECF0; border-radius: 18px; background: #FFFFFF;
    padding: 24px 26px 22px; margin-bottom: 22px; }
  .ea-lg > h4 { margin: 0 0 5px; font-size: 17px; font-weight: 700; color: #101828; letter-spacing: -0.015em; }
  .ea-lg > p { margin: 0 0 18px; font-size: 12.5px; line-height: 1.7; color: #667085; }
  .ea-lgg { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px; }
  .ea-lgi { border-top: 3px solid #D92D20; padding-top: 13px; }
  .ea-lgi .no { display: inline-flex; align-items: center; justify-content: center;
    width: 22px; height: 22px; border-radius: 50%; background: #D92D20; color: #FFFFFF;
    font-family: 'IBM Plex Sans', sans-serif; font-size: 12px; font-weight: 700; margin-bottom: 9px; }
  .ea-lgi h5 { margin: 0 0 6px; font-size: 13.5px; font-weight: 700; color: #101828; }
  .ea-lgi p { margin: 0 0 9px; font-size: 12px; line-height: 1.7; color: #475467; }
  .ea-lgi .rd { display: block; font-size: 11.5px; line-height: 1.7; color: #B42318;
    border-left: 2px solid #FECDCA; padding-left: 9px; }

  /* \u0e15\u0e31\u0e27\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e1a\u0e17\u0e1a\u0e32\u0e17\u0e2b\u0e19\u0e49\u0e32\u0e2a\u0e21\u0e31\u0e04\u0e23 */
  .role-pick { display: grid; grid-template-columns: 1fr 1fr; gap: 11px; margin: 0 0 18px; }
  .role-op { text-align: left; border: 1.5px solid #EAECF0; background: #FFFFFF; border-radius: 13px;
    padding: 14px 15px 15px; cursor: pointer; font: inherit; color: #101828;
    transition: border-color .16s, background .16s; }
  .role-op:hover { border-color: #D0D5DD; }
  .role-op[aria-checked="true"] { border-color: #D92D20; background: #FEF9F8; }
  .role-op:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }
  .role-ic { display: flex; align-items: center; justify-content: center; width: 32px; height: 32px;
    border-radius: 9px; background: #F5F7FA; color: #667085; margin-bottom: 10px; }
  .role-op[aria-checked="true"] .role-ic { background: #FEF3F2; color: #B42318; }
  .role-op b { display: block; font-size: 14px; font-weight: 700; margin-bottom: 3px; }
  .role-op span:last-child { display: block; font-size: 11.5px; line-height: 1.6; color: #667085; }
  .su-bnote { display: flex; gap: 9px; align-items: flex-start; margin: 2px 0 4px; padding: 12px 14px;
    background: #FEF6EE; border: 1px solid #F5DFC4; border-radius: 11px;
    font-size: 12px; line-height: 1.7; color: #93500B; }
  .su-bnote b { color: #7A3F08; font-weight: 700; }

  /* Broker Dashboard */
  .bd-crumb { display: flex; align-items: center; gap: 9px; margin-bottom: 18px;
    font-size: 12.5px; color: #667085; }
  .bd-crumb a { color: #B42318; text-decoration: none; font-weight: 600; }
  .bd-crumb a:hover { text-decoration: underline; }
  .bd-crumb b { color: #101828; font-weight: 700; }
  .bd-top { display: flex; align-items: center; gap: 16px; flex-wrap: wrap;
    border: 1px solid #EAECF0; border-radius: 18px; background: #FFFFFF; padding: 20px 24px; }
  .bd-logo { width: 52px; height: 52px; border-radius: 13px; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center; background: #101828;
    color: #FFFFFF; font-family: 'IBM Plex Sans', sans-serif; font-size: 17px;
    font-weight: 700; letter-spacing: 0.02em; }
  .bd-id { min-width: 0; }
  .bd-id h3 { margin: 0 0 5px; font-size: 19px; font-weight: 700; letter-spacing: -0.02em; color: #101828; }
  .bd-id .row { display: flex; align-items: center; gap: 9px; flex-wrap: wrap;
    font-size: 12px; color: #667085; }
  .bd-vf { display: inline-flex; align-items: center; gap: 5px; font-size: 11.5px; font-weight: 700;
    color: #067647; background: #F0FBF5; border: 1px solid #CFEBDC; border-radius: 999px; padding: 3px 10px; }
  .bd-who { margin-left: auto; text-align: right; font-size: 12px; line-height: 1.7; color: #667085; }
  .bd-who b { display: block; font-size: 13.5px; font-weight: 600; color: #101828; }
  .bd-out { margin-top: 6px; border: 1px solid #D0D5DD; background: #FFFFFF; color: #475467;
    border-radius: 8px; padding: 4px 12px; font: inherit; font-size: 11.5px; cursor: pointer; }
  .bd-out:hover { border-color: #667085; color: #101828; }
  .bd-out:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }

  .bd-due { display: flex; align-items: flex-start; gap: 13px; margin-top: 14px;
    border: 1.5px solid #FECDCA; background: #FEF3F2; border-radius: 14px; padding: 16px 19px; }
  .bd-due .ic { flex-shrink: 0; width: 30px; height: 30px; border-radius: 9px; background: #FFFFFF;
    display: flex; align-items: center; justify-content: center; }
  .bd-due b { display: block; font-size: 14.5px; font-weight: 700; color: #912018; margin-bottom: 4px; }
  .bd-due p { margin: 0; font-size: 12.5px; line-height: 1.7; color: #B42318; }
  .bd-due .cd { margin-left: auto; flex-shrink: 0; text-align: right; }
  .bd-due .cd em { display: block; font-style: normal; font-family: 'IBM Plex Sans', sans-serif;
    font-size: 26px; font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; color: #B42318; }
  .bd-due .cd span { font-size: 11px; color: #B42318; }

  .bd-kpi { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; margin-top: 14px; }
  .bd-k { border: 1px solid #EAECF0; border-radius: 14px; background: #FFFFFF; padding: 17px 19px; }
  .bd-k .lb { display: block; font-size: 12.5px; font-weight: 600; color: #475467; }
  .bd-k .vl { display: block; font-family: 'IBM Plex Sans', sans-serif; font-size: 29px;
    font-weight: 700; letter-spacing: -0.035em; color: #101828; line-height: 1.15; margin: 6px 0 4px; }
  .bd-k .vl.warn { color: #B42318; }
  .bd-k .cmp { display: block; font-size: 11.5px; line-height: 1.6; color: #667085; }
  .bd-k .cmp b.up { color: #B42318; font-weight: 700; }
  .bd-k .cmp b.dn { color: #067647; font-weight: 700; }

  .bd-case { border: 1px solid #EAECF0; border-radius: 16px; background: #FFFFFF;
    margin-bottom: 16px; overflow: hidden; }
  .bd-case.act { border-color: #FECDCA; }
  .bd-chead { display: flex; align-items: flex-start; gap: 13px; padding: 18px 20px 15px;
    border-bottom: 1px solid #F0F2F5; }
  .bd-sev { flex-shrink: 0; width: 34px; height: 34px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center; }
  .bd-sev.hi { background: #FEF3F2; }
  .bd-sev.md { background: #FEF6EE; }
  .bd-ct { flex: 1; min-width: 0; }
  .bd-ct h3 { margin: 0 0 5px; font-size: 16px; font-weight: 600; letter-spacing: -0.015em; color: #101828; }
  .bd-cmeta { display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
    font-size: 12px; color: #667085; }
  .bd-cmeta code { font-family: 'IBM Plex Sans', sans-serif; font-size: 11.5px;
    background: #F5F7FA; border: 1px solid #EAECF0; border-radius: 5px; padding: 1px 7px; color: #475467; }
  .bd-pill { flex-shrink: 0; font-size: 11.5px; font-weight: 600; border-radius: 999px; padding: 5px 12px; }
  .bd-pill.new { background: #FEF3F2; color: #912018; border: 1px solid #FECDCA; }
  .bd-pill.ack { background: #FEF6EE; color: #93500B; border: 1px solid #F5DFC4; }
  .bd-pill.sent { background: #F0FBF5; color: #05603A; border: 1px solid #CFEBDC; }
  .bd-pill.done { background: #F5F7FA; color: #475467; border: 1px solid #EAECF0; }
  .bd-cbody { padding: 16px 20px; font-size: 13.5px; line-height: 1.75; color: #475467; }
  .bd-cbody b { color: #101828; font-weight: 600; }
  .bd-ev { margin-top: 12px; display: flex; gap: 8px; flex-wrap: wrap; }
  .bd-ev span { font-size: 11.5px; color: #475467; background: #F5F7FA;
    border: 1px solid #EAECF0; border-radius: 7px; padding: 4px 10px; }

  .bd-tl { padding: 4px 20px 16px; }
  .bd-tl h4 { margin: 0 0 12px; font-size: 12px; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; color: #B42318; }
  .bd-step { position: relative; padding: 0 0 15px 26px; }
  .bd-step:last-child { padding-bottom: 0; }
  .bd-step::before { content: ""; position: absolute; left: 5px; top: 4px;
    width: 9px; height: 9px; border-radius: 50%; background: #D0D5DD; }
  .bd-step.on::before { background: #067647; }
  .bd-step.now::before { background: #D92D20; box-shadow: 0 0 0 4px #FEE4E2; }
  .bd-step::after { content: ""; position: absolute; left: 9px; top: 15px; bottom: 0; width: 1px;
    background: #EAECF0; }
  .bd-step:last-child::after { display: none; }
  .bd-step b { display: block; font-size: 13px; font-weight: 600; color: #101828; }
  .bd-step span { display: block; font-size: 12px; line-height: 1.7; color: #667085; margin-top: 2px; }

  .bd-act { border-top: 1px solid #F0F2F5; background: #F9FAFB; padding: 16px 20px 18px; }
  .bd-act h4 { margin: 0 0 11px; font-size: 13px; font-weight: 700; color: #101828; }
  .bd-kinds { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 11px; }
  .bd-kind { border: 1px solid #D0D5DD; background: #FFFFFF; color: #475467; border-radius: 999px;
    padding: 5px 13px; font: inherit; font-size: 12px; cursor: pointer;
    transition: border-color .15s, background .15s, color .15s; }
  .bd-kind:hover { border-color: #667085; color: #101828; }
  .bd-kind[aria-pressed="true"] { border-color: #D92D20; background: #FEF3F2; color: #912018; font-weight: 600; }
  .bd-kind:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }
  .bd-ta { width: 100%; min-height: 84px; border: 1px solid #D0D5DD; border-radius: 11px;
    background: #FFFFFF; padding: 11px 13px; font: inherit; font-size: 13px; line-height: 1.7;
    color: #101828; resize: vertical; }
  .bd-ta:focus-visible { outline: 2px solid #D92D20; outline-offset: 1px; border-color: #D92D20; }
  .bd-arow { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-top: 11px; }
  .bd-file { display: inline-flex; align-items: center; gap: 7px; border: 1px dashed #D0D5DD;
    background: #FFFFFF; color: #475467; border-radius: 9px; padding: 7px 13px;
    font: inherit; font-size: 12px; cursor: pointer; }
  .bd-file:hover { border-color: #667085; color: #101828; }
  .bd-file:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }
  .bd-send { margin-left: auto; }
  .bd-ackb { border: 1px solid #D92D20; background: #FFFFFF; color: #B42318; border-radius: 9px;
    padding: 8px 16px; font: inherit; font-size: 12.5px; font-weight: 600; cursor: pointer; }
  .bd-ackb:hover { background: #FEF3F2; }
  .bd-ackb:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }
  .bd-ackb[disabled] { border-color: #D0D5DD; color: #667085; cursor: default; background: #F5F7FA; }
  .bd-hint { font-size: 11.5px; line-height: 1.7; color: #667085; margin: 9px 0 0; }
  .bd-hint b { color: #B42318; font-weight: 700; }

  .bd-rules { border: 1px solid #EAECF0; border-left: 4px solid #D92D20; border-radius: 16px;
    background: #FFFFFF; padding: 24px 26px 22px; margin-top: 34px; }
  .bd-rules h4 { margin: 0 0 6px; font-size: 16px; font-weight: 700; color: #101828; letter-spacing: -0.015em; }
  .bd-rules > p { margin: 0 0 17px; font-size: 12.5px; line-height: 1.7; color: #667085; }
  .bd-rl { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px 22px; }
  .bd-rl div { border-top: 2px solid #F2F4F7; padding-top: 12px; }
  .bd-rl b { display: block; font-size: 13px; font-weight: 700; color: #101828; margin-bottom: 5px; }
  .bd-rl span { display: block; font-size: 12px; line-height: 1.75; color: #475467; }

  .al-cta { display: flex; align-items: center; gap: 18px; flex-wrap: wrap; margin-top: 30px;
    border: 1px solid #EAECF0; border-radius: 16px; background: #F9FAFB; padding: 20px 24px; }
  .al-cta .tx { min-width: 0; }
  .al-cta b { display: block; font-size: 15px; font-weight: 700; color: #101828; margin-bottom: 4px; }
  .al-cta span { display: block; font-size: 12.5px; line-height: 1.7; color: #667085; }
  .al-cta .bt { margin-left: auto; display: flex; gap: 10px; flex-wrap: wrap; }

  /* \u2550\u2550 RedStar Awards \u2014 Design Tokens (8pt grid) \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */
  .page[data-page="awards"], .page[data-page="awards2026"], .page[data-page="verify"],
  .page[data-page="brokerawards"], .page[data-page="partner"] {
    --aw-red: #B91C1C;      --aw-red-d: #7F1313;   --aw-red-l: #FDF2F2;
    --aw-red-e: #F6D5D5;    --aw-ink: #0A0A0A;     --aw-ink-2: #3F3F46;
    --aw-ink-3: #71717A;    --aw-line: #E4E4E7;    --aw-line-2: #F4F4F5;
    --aw-gold: #A98420;     --aw-gold-l: #FBF6E7;  --aw-gold-e: #EBDCA8;
    --aw-gold-t: #7A5C11;
    --aw-ok: #05603A;       --aw-ok-l: #ECFDF3;
    --s1: 8px;  --s2: 16px; --s3: 24px; --s4: 32px; --s5: 40px;
    --s6: 48px; --s7: 64px; --s8: 80px; --s9: 96px;
  }

  /* \u2500 Typography scale \u2500 */
  .aw-h1 { margin: 0; font-size: 46px; font-weight: 700; line-height: 1.1;
    letter-spacing: -0.035em; color: var(--aw-ink); }
  .aw-h2 { margin: 0 0 var(--s1); font-size: 30px; font-weight: 700; line-height: 1.2;
    letter-spacing: -0.03em; color: var(--aw-ink); }
  .aw-h3 { margin: 0 0 var(--s1); font-size: 19px; font-weight: 700; line-height: 1.3;
    letter-spacing: -0.02em; color: var(--aw-ink); }
  .aw-body { margin: 0; font-size: 14.5px; line-height: 1.75; color: var(--aw-ink-2); }
  .aw-cap { margin: 0; font-size: 11.5px; line-height: 1.6; letter-spacing: 0.06em;
    text-transform: uppercase; font-weight: 700; color: var(--aw-ink-3); }
  .aw-mono { font-family: 'IBM Plex Sans', sans-serif; font-variant-numeric: tabular-nums; }

  /* \u2500 Buttons \u2500 */
  .aw-btn { display: inline-flex; align-items: center; justify-content: center; gap: var(--s1);
    font: inherit; font-size: 14px; font-weight: 600; border-radius: 8px; padding: 12px 22px;
    cursor: pointer; text-decoration: none; border: 1px solid transparent;
    transition: background .18s ease, border-color .18s ease, color .18s ease, transform .18s ease; }
  .aw-btn:focus-visible { outline: 2px solid var(--aw-red); outline-offset: 3px; }
  .aw-btn.pri { background: var(--aw-red); border-color: var(--aw-red); color: #FFFFFF; }
  .aw-btn.pri:hover { background: var(--aw-red-d); border-color: var(--aw-red-d); }
  .aw-btn.out { background: transparent; border-color: var(--aw-line); color: var(--aw-ink); }
  .aw-btn.out:hover { border-color: var(--aw-ink-3); }
  .aw-btn.ghost { background: transparent; border-color: transparent; color: var(--aw-red);
    padding-left: 10px; padding-right: 10px; }
  .aw-btn.ghost:hover { background: var(--aw-red-l); }
  .aw-btn.sm { font-size: 12.5px; padding: 8px 15px; border-radius: 7px; }
  .aw-btn.onblk { border-color: rgba(255,255,255,0.28); color: #FFFFFF; }
  .aw-btn.onblk:hover { border-color: #FFFFFF; background: rgba(255,255,255,0.08); }

  /* \u2500 Badges \u2500 */
  .aw-tag { display: inline-flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700;
    letter-spacing: 0.05em; text-transform: uppercase; border-radius: 999px; padding: 4px 11px; }
  .aw-tag.vf { background: var(--aw-ok-l); color: var(--aw-ok); border: 1px solid #B7E4C7; }
  .aw-tag.win { background: var(--aw-red-l); color: var(--aw-red); border: 1px solid var(--aw-red-e); }
  .aw-tag.hof { background: var(--aw-gold-l); color: var(--aw-gold-t); border: 1px solid var(--aw-gold-e); }
  .aw-tag.rev { background: #FEF6EE; color: #93500B; border: 1px solid #F5DFC4; }

  /* \u2500 \u0e41\u0e16\u0e1a\u0e1a\u0e2d\u0e01\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07 \u2500 */
  .aw-demo { display: flex; align-items: center; gap: var(--s1); border-radius: 8px;
    background: #FEF6EE; border: 1px solid #F5DFC4; padding: 9px 14px;
    font-size: 11.5px; line-height: 1.6; color: #93500B; }
  .aw-demo b { color: #7A3F08; font-weight: 700; }

  /* \u2500 PAGE 1 Hero \u2500 */
  .aw-hero { position: relative; overflow: hidden; background: var(--aw-ink);
    padding: var(--s9) 0 var(--s8); }
  .aw-hwm { position: absolute; right: -60px; top: 50%; transform: translateY(-50%);
    width: 560px; opacity: 0.05; pointer-events: none; }
  .aw-hin { position: relative; width: 1200px; margin: 0 auto; }
  .aw-hin .aw-cap { color: rgba(255,255,255,0.55); margin-bottom: var(--s2); }
  .aw-hin h1 { margin: 0 0 var(--s3); font-size: 62px; font-weight: 700; line-height: 1.04;
    letter-spacing: -0.04em; color: #FFFFFF; max-width: 15ch; }
  .aw-hin h1 i { font-style: normal; color: var(--aw-red); }
  .aw-hin p { margin: 0 0 var(--s5); font-size: 16px; line-height: 1.8;
    color: rgba(255,255,255,0.7); max-width: 62ch; }
  .aw-hbt { display: flex; gap: var(--s2); flex-wrap: wrap; }
  .aw-hst { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: var(--s3); margin-top: var(--s8); padding-top: var(--s4);
    border-top: 1px solid rgba(255,255,255,0.12); }
  .aw-hst div b { display: block; font-family: 'IBM Plex Sans', sans-serif; font-size: 34px;
    font-weight: 700; letter-spacing: -0.035em; color: #FFFFFF; line-height: 1.1; }
  .aw-hst div span { display: block; margin-top: 6px; font-size: 12.5px; line-height: 1.6;
    color: rgba(255,255,255,0.6); }

  /* \u2500 Section head \u2500 */
  .aw-sec { padding-top: var(--s9); }
  .aw-shd { display: flex; align-items: flex-end; gap: var(--s3); margin-bottom: var(--s5); }
  .aw-shd .tx { min-width: 0; }
  .aw-shd .aw-cap { margin-bottom: 10px; color: var(--aw-red); }
  .aw-shd p { margin: 6px 0 0; font-size: 14px; line-height: 1.7; color: var(--aw-ink-3); max-width: 70ch; }
  .aw-shd .rt { margin-left: auto; flex-shrink: 0; }

  /* \u2500 Award category cards \u2500 */
  .aw-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--s3); }
  .aw-card { position: relative; border: 1px solid var(--aw-line); border-radius: 12px;
    background: #FFFFFF; padding: var(--s3); overflow: hidden; text-decoration: none;
    display: block; color: inherit;
    transition: border-color .22s ease, box-shadow .22s ease, transform .22s ease; }
  .aw-card::before { content: ""; position: absolute; left: 0; right: 0; top: 0; height: 3px;
    background: var(--aw-red); transform: scaleX(0); transform-origin: left;
    transition: transform .28s cubic-bezier(.2,.7,.3,1); }
  .aw-card:hover { border-color: #D4D4D8; box-shadow: 0 12px 32px -22px rgba(10,10,10,0.5);
    transform: translateY(-2px); }
  .aw-card:hover::before { transform: scaleX(1); }
  .aw-card:focus-visible { outline: 2px solid var(--aw-red); outline-offset: 3px; }
  .aw-card .ic { width: 40px; height: 40px; border-radius: 10px; background: var(--aw-red-l);
    display: flex; align-items: center; justify-content: center; margin-bottom: var(--s2); }
  .aw-card h3 { margin: 0 0 6px; font-size: 17px; font-weight: 700; letter-spacing: -0.02em;
    color: var(--aw-ink); }
  .aw-card p { margin: 0 0 var(--s2); font-size: 13px; line-height: 1.75; color: var(--aw-ink-3); }
  .aw-card .ft { display: flex; align-items: center; gap: var(--s1); padding-top: var(--s2);
    border-top: 1px solid var(--aw-line-2); font-size: 12px; color: var(--aw-ink-3); }
  .aw-card .ft b { color: var(--aw-ink); font-weight: 600; }
  .aw-card .ft .go { margin-left: auto; color: var(--aw-red); font-weight: 600; }

  /* \u2500 Hall of Fame strip \u2500 */
  .aw-hof { border: 1px solid var(--aw-line); border-radius: 12px; overflow: hidden; }
  .aw-hrow { display: grid; grid-template-columns: 56px minmax(0, 1fr) 150px 190px 120px;
    align-items: center; gap: var(--s2); padding: var(--s2) var(--s3);
    border-bottom: 1px solid var(--aw-line-2); }
  .aw-hrow:last-child { border-bottom: 0; }
  .aw-hrow.hd { background: #FAFAFA; padding-top: 12px; padding-bottom: 12px; }
  .aw-hrow.hd span { font-size: 11px; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; color: var(--aw-ink-3); }
  .aw-hno { font-family: 'IBM Plex Sans', sans-serif; font-size: 15px; font-weight: 700;
    color: var(--aw-gold-t); }
  .aw-hnm { display: flex; align-items: center; gap: 11px; min-width: 0; }
  .aw-hnm b { font-size: 14.5px; font-weight: 600; color: var(--aw-ink); }
  .aw-hnm span { font-size: 12px; color: var(--aw-ink-3); }
  .aw-hyr { display: flex; gap: 5px; flex-wrap: wrap; }
  .aw-hyr i { font-style: normal; font-family: 'IBM Plex Sans', sans-serif; font-size: 11px;
    font-weight: 600; color: var(--aw-ink-2); background: var(--aw-line-2);
    border-radius: 5px; padding: 2px 7px; }
  .aw-hcn { font-family: 'IBM Plex Sans', sans-serif; font-size: 20px; font-weight: 700;
    color: var(--aw-ink); text-align: right; }

  /* \u2500 Methodology \u2500 */
  .aw-meth { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: var(--s2); }
  .aw-mi { border-top: 2px solid var(--aw-red); padding-top: var(--s2); }
  .aw-mi b { display: block; font-family: 'IBM Plex Sans', sans-serif; font-size: 26px;
    font-weight: 700; letter-spacing: -0.03em; color: var(--aw-ink); line-height: 1.1; }
  .aw-mi em { display: block; font-style: normal; font-size: 13.5px; font-weight: 600;
    color: var(--aw-ink); margin: 8px 0 5px; }
  .aw-mi span { display: block; font-size: 12px; line-height: 1.7; color: var(--aw-ink-3); }

  /* \u2500 CTA verify \u2500 */
  .aw-cta { display: grid; grid-template-columns: minmax(0, 1fr) 380px; gap: var(--s6);
    align-items: center; background: var(--aw-ink); border-radius: 14px;
    padding: var(--s6); margin: var(--s9) 0 var(--s8); }
  .aw-cta h2 { margin: 0 0 var(--s2); font-size: 30px; font-weight: 700; line-height: 1.2;
    letter-spacing: -0.03em; color: #FFFFFF; }
  .aw-cta p { margin: 0 0 var(--s3); font-size: 14px; line-height: 1.8; color: rgba(255,255,255,0.66); }
  .aw-vbox { background: #FFFFFF; border-radius: 12px; padding: var(--s3); }
  .aw-vbox label { display: block; font-size: 12px; font-weight: 600; color: var(--aw-ink-2);
    margin-bottom: var(--s1); }
  .aw-vin { display: flex; gap: var(--s1); }
  .aw-vin input { flex: 1; min-width: 0; border: 1px solid var(--aw-line); border-radius: 8px;
    padding: 10px 12px; font: inherit; font-size: 13px; color: var(--aw-ink);
    font-family: 'IBM Plex Sans', sans-serif; }
  .aw-vin input:focus-visible { outline: 2px solid var(--aw-red); outline-offset: 1px;
    border-color: var(--aw-red); }
  .aw-cta .aw-vbox .aw-vhint { margin: 10px 0 0; font-size: 11.5px; line-height: 1.6;
    color: var(--aw-ink-3); }

  /* \u2500 PAGE 2 winners table \u2500 */
  .w26-ctl { display: flex; gap: var(--s2); flex-wrap: wrap; align-items: flex-end;
    margin-bottom: var(--s3); }
  .w26-f { display: flex; flex-direction: column; gap: 6px; }
  .w26-f span { font-size: 11px; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; color: var(--aw-ink-3); }
  .w26-f select { border: 1px solid var(--aw-line); border-radius: 8px; background: #FFFFFF;
    padding: 9px 12px; font: inherit; font-size: 13px; color: var(--aw-ink); min-width: 170px; }
  .w26-f select:focus-visible { outline: 2px solid var(--aw-red); outline-offset: 1px; }
  .w26-cnt { margin-left: auto; font-size: 12.5px; color: var(--aw-ink-3); padding-bottom: 10px; }
  .w26-wrap { border: 1px solid var(--aw-line); border-radius: 12px; overflow: hidden; }
  .w26 { width: 100%; border-collapse: collapse; }
  .w26 thead th { text-align: left; padding: 13px var(--s2); background: #FAFAFA;
    border-bottom: 1px solid var(--aw-line); font-size: 11px; font-weight: 700;
    letter-spacing: 0.05em; text-transform: uppercase; color: var(--aw-ink-3); }
  .w26 tbody td { padding: 14px var(--s2); border-bottom: 1px solid var(--aw-line-2);
    vertical-align: middle; font-size: 13.5px; color: var(--aw-ink-2); }
  .w26 tbody tr:last-child td { border-bottom: 0; }
  .w26 tbody tr { cursor: pointer; transition: background .15s ease; }
  .w26 tbody tr:hover { background: #FAFAFA; }
  .w26 tbody tr:focus-visible { outline: 2px solid var(--aw-red); outline-offset: -2px; }
  .w26-rk { font-family: 'IBM Plex Sans', sans-serif; font-size: 15px; font-weight: 700;
    color: var(--aw-ink); width: 62px; }
  .w26-rk.g { color: var(--aw-gold-t); }
  .w26-bk { display: flex; align-items: center; gap: 11px; }
  .w26-bk b { font-size: 14px; font-weight: 600; color: var(--aw-ink); }
  .w26-bk span { display: block; font-size: 11.5px; color: var(--aw-ink-3); margin-top: 2px; }
  .w26-sc { font-family: 'IBM Plex Sans', sans-serif; font-size: 16px; font-weight: 700;
    color: var(--aw-ink); }
  .w26-id { font-family: 'IBM Plex Sans', sans-serif; font-size: 11.5px; color: var(--aw-ink-3); }

  /* \u2500 PAGE 3 verify \u2500 */
  .vf-hero { display: grid; grid-template-columns: minmax(0, 1fr) 260px; gap: var(--s6);
    border: 1px solid var(--aw-line); border-top: 4px solid var(--aw-red); border-radius: 14px;
    background: #FFFFFF; padding: var(--s6); position: relative; overflow: hidden; }
  .vf-wm { position: absolute; right: -40px; bottom: -50px; width: 300px; opacity: 0.035;
    pointer-events: none; }
  .vf-l { position: relative; min-width: 0; }
  .vf-bk { display: flex; align-items: center; gap: var(--s2); margin-bottom: var(--s3); }
  .vf-bk .nm b { display: block; font-size: 17px; font-weight: 600; color: var(--aw-ink); }
  .vf-bk .nm span { font-size: 12.5px; color: var(--aw-ink-3); }
  .vf-aw { margin: 0 0 var(--s2); font-size: 38px; font-weight: 700; line-height: 1.15;
    letter-spacing: -0.035em; color: var(--aw-ink); }
  .vf-tags { display: flex; gap: var(--s1); flex-wrap: wrap; margin-bottom: var(--s4); }
  .vf-meta { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--s3);
    padding-top: var(--s3); border-top: 1px solid var(--aw-line-2); }
  .vf-meta div span { display: block; font-size: 11px; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; color: var(--aw-ink-3); margin-bottom: 6px; }
  .vf-meta div b { font-family: 'IBM Plex Sans', sans-serif; font-size: 15px; font-weight: 600;
    color: var(--aw-ink); }
  .vf-r { position: relative; display: flex; flex-direction: column; align-items: center;
    gap: var(--s2); }
  .vf-qr { border: 1px solid var(--aw-line); border-radius: 10px; padding: 12px; background: #FFFFFF; }
  .vf-qc { text-align: center; font-size: 11px; line-height: 1.6; color: var(--aw-ink-3); }
  .vf-seal { display: flex; flex-direction: column; align-items: center; gap: 6px;
    border: 1.5px solid var(--aw-ok); border-radius: 10px; background: var(--aw-ok-l);
    padding: 11px 18px; width: 100%; }
  .vf-seal b { font-size: 13px; font-weight: 700; letter-spacing: 0.06em; color: var(--aw-ok); }
  .vf-seal span { font-size: 11px; color: var(--aw-ok); }

  .vf-bars { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: var(--s3) var(--s6); }
  .vf-bar .lb { display: flex; align-items: baseline; justify-content: space-between;
    gap: var(--s2); margin-bottom: 8px; }
  .vf-bar .lb span { font-size: 13.5px; font-weight: 600; color: var(--aw-ink); }
  .vf-bar .lb i { font-style: normal; font-size: 12px; color: var(--aw-ink-3); }
  .vf-bar .lb b { font-family: 'IBM Plex Sans', sans-serif; font-size: 16px; font-weight: 700;
    color: var(--aw-ink); }
  .vf-tr { height: 8px; border-radius: 4px; background: var(--aw-line-2); overflow: hidden; }
  .vf-tr i { display: block; height: 100%; border-radius: 4px; background: var(--aw-red);
    width: 0; transition: width 1.1s cubic-bezier(.2,.7,.3,1); }
  .vf-tr i.gold { background: var(--aw-gold); }
  .vf-why { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--s3); }
  .vf-wi { border: 1px solid var(--aw-line); border-radius: 12px; padding: var(--s3); }
  .vf-wi .no { display: inline-flex; align-items: center; justify-content: center;
    width: 26px; height: 26px; border-radius: 50%; background: var(--aw-ink); color: #FFFFFF;
    font-family: 'IBM Plex Sans', sans-serif; font-size: 12px; font-weight: 700;
    margin-bottom: 12px; }
  .vf-wi b { display: block; font-size: 14.5px; font-weight: 700; color: var(--aw-ink);
    margin-bottom: 7px; }
  .vf-wi p { margin: 0 0 12px; font-size: 12.5px; line-height: 1.8; color: var(--aw-ink-2); }
  .vf-wi .src { font-size: 11.5px; line-height: 1.6; color: var(--aw-red);
    border-left: 2px solid var(--aw-red-e); padding-left: 10px; display: block; }

  /* \u2500 Timeline (\u0e43\u0e0a\u0e49\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e19\u0e49\u0e32 3 \u0e41\u0e25\u0e30 4) \u2500 */
  .aw-tl { position: relative; padding-left: 30px; }
  .aw-tl::before { content: ""; position: absolute; left: 7px; top: 8px; bottom: 8px;
    width: 2px; background: var(--aw-line); }
  .aw-ti { position: relative; padding-bottom: var(--s4); }
  .aw-ti:last-child { padding-bottom: 0; }
  .aw-ti::before { content: ""; position: absolute; left: -30px; top: 5px; width: 16px;
    height: 16px; border-radius: 50%; background: #FFFFFF; border: 3px solid var(--aw-line); }
  .aw-ti.on::before { border-color: var(--aw-red); }
  .aw-ti.gold::before { border-color: var(--aw-gold); }
  .aw-ti .yr { font-family: 'IBM Plex Sans', sans-serif; font-size: 13px; font-weight: 700;
    color: var(--aw-ink-3); letter-spacing: 0.02em; }
  .aw-ti h4 { margin: 5px 0 6px; font-size: 19px; font-weight: 700; letter-spacing: -0.02em;
    color: var(--aw-ink); }
  .aw-ti p { margin: 0 0 10px; font-size: 13px; line-height: 1.8; color: var(--aw-ink-3); }
  .aw-ti .rw { display: flex; align-items: center; gap: var(--s2); flex-wrap: wrap;
    font-size: 12px; color: var(--aw-ink-3); }
  .aw-ti .rw b { font-family: 'IBM Plex Sans', sans-serif; font-size: 14px; color: var(--aw-ink); }

  /* \u2500 PAGE 4 \u2500 */
  .ba-hero { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: var(--s6);
    align-items: center; border: 1px solid var(--aw-line); border-radius: 14px;
    background: #FFFFFF; padding: var(--s6); }
  .ba-id { display: flex; align-items: center; gap: var(--s3); margin-bottom: var(--s4); }
  .ba-id h2 { margin: 0 0 6px; font-size: 32px; font-weight: 700; letter-spacing: -0.03em;
    color: var(--aw-ink); }
  .ba-id span { font-size: 13px; color: var(--aw-ink-3); }
  .ba-st { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--s3);
    padding-top: var(--s3); border-top: 1px solid var(--aw-line-2); }
  .ba-st div b { display: block; font-family: 'IBM Plex Sans', sans-serif; font-size: 32px;
    font-weight: 700; letter-spacing: -0.035em; color: var(--aw-ink); line-height: 1.1; }
  .ba-st div span { display: block; margin-top: 5px; font-size: 12px; color: var(--aw-ink-3); }
  .ba-body { display: grid; grid-template-columns: minmax(0, 1fr) 380px; gap: var(--s7);
    margin-top: var(--s7); align-items: start; }
  .ba-tro { border: 1px solid var(--aw-gold-e); border-radius: 14px; overflow: hidden;
    background: #FFFFFF; }
  .ba-trh { background: var(--aw-ink); padding: var(--s3); text-align: center; }
  .ba-trh .aw-cap { color: var(--aw-gold); margin-bottom: 10px; }
  .ba-trh h4 { margin: 0; font-size: 21px; font-weight: 700; letter-spacing: -0.02em; color: #FFFFFF; }
  .ba-trb { padding: var(--s4) var(--s3) var(--s3); text-align: center;
    background: linear-gradient(180deg, var(--aw-gold-l) 0%, #FFFFFF 62%); }
  .ba-trb .yr { font-family: 'IBM Plex Sans', sans-serif; font-size: 44px; font-weight: 700;
    letter-spacing: -0.04em; color: var(--aw-gold); line-height: 1; margin-bottom: var(--s2); }
  .ba-trb p { margin: 0 0 var(--s3); font-size: 12.5px; line-height: 1.75; color: var(--aw-ink-2); }
  .ba-trf { border-top: 1px solid var(--aw-line-2); padding: 14px var(--s3);
    display: flex; align-items: center; gap: var(--s1); font-size: 11.5px; color: var(--aw-ink-3); }
  .ba-trf .aw-mono { margin-left: auto; color: var(--aw-ink-2); }

  /* \u2500 PAGE 5 partner \u2500 */
  .pt-shell { display: grid; grid-template-columns: 232px minmax(0, 1fr); gap: var(--s6);
    align-items: start; }
  .pt-side { border: 1px solid var(--aw-line); border-radius: 12px; padding: var(--s1);
    position: sticky; top: 24px; }
  .pt-side .who { padding: var(--s2); border-bottom: 1px solid var(--aw-line-2);
    margin-bottom: var(--s1); }
  .pt-side .who b { display: block; font-size: 14px; font-weight: 600; color: var(--aw-ink); }
  .pt-side .who span { font-size: 11.5px; color: var(--aw-ink-3); }
  .pt-nav { display: block; width: 100%; text-align: left; border: 0; background: transparent;
    border-radius: 8px; padding: 10px 14px; font: inherit; font-size: 13.5px;
    color: var(--aw-ink-2); cursor: pointer; transition: background .15s, color .15s; }
  .pt-nav:hover { background: var(--aw-line-2); color: var(--aw-ink); }
  .pt-nav[aria-current="true"] { background: var(--aw-red-l); color: var(--aw-red); font-weight: 600; }
  .pt-nav:focus-visible { outline: 2px solid var(--aw-red); outline-offset: -2px; }
  .pt-main { min-width: 0; }
  .pt-kpi { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: var(--s2); }
  .pt-k { border: 1px solid var(--aw-line); border-radius: 12px; padding: var(--s3); }
  .pt-k span { display: block; font-size: 12.5px; font-weight: 600; color: var(--aw-ink-3); }
  .pt-k b { display: block; font-family: 'IBM Plex Sans', sans-serif; font-size: 30px;
    font-weight: 700; letter-spacing: -0.035em; color: var(--aw-ink); margin: 8px 0 5px; line-height: 1.1; }
  .pt-k i { font-style: normal; font-size: 11.5px; color: var(--aw-ink-3); }
  .pt-k i.up { color: var(--aw-ok); font-weight: 600; }
  .pt-awd { border: 1px solid var(--aw-line); border-radius: 12px; padding: var(--s3);
    display: grid; grid-template-columns: 320px minmax(0, 1fr); gap: var(--s3);
    align-items: center; margin-bottom: var(--s2); }
  .pt-at h4 { margin: 0 0 5px; font-size: 16px; font-weight: 700; letter-spacing: -0.02em;
    color: var(--aw-ink); }
  .pt-at .aw-mono { font-size: 11.5px; color: var(--aw-ink-3); }
  .pt-abt { display: flex; gap: var(--s1); flex-wrap: wrap; margin-top: 14px; }
  .pt-emb { margin-top: var(--s2); border: 1px solid var(--aw-line); border-radius: 9px;
    background: #FAFAFA; padding: 11px 13px; font-family: 'IBM Plex Sans', sans-serif;
    font-size: 11px; line-height: 1.7; color: var(--aw-ink-2); overflow-x: auto;
    white-space: pre; }
  .pt-toast { position: fixed; left: 50%; bottom: 34px; transform: translate(-50%, 14px);
    background: var(--aw-ink); color: #FFFFFF; border-radius: 9px; padding: 11px 20px;
    font-size: 13px; opacity: 0; pointer-events: none; z-index: 60;
    transition: opacity .22s ease, transform .22s ease; }
  .pt-toast.on { opacity: 1; transform: translate(-50%, 0); }
  .pt-ch { border: 1px solid var(--aw-line); border-radius: 12px; padding: var(--s3); }
  .pt-ch h4 { margin: 0 0 var(--s3); font-size: 14.5px; font-weight: 700; color: var(--aw-ink); }
  .pt-2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--s2); }
  .pt-lg { list-style: none; margin: 0; padding: 0; }
  .pt-lg li { display: grid; grid-template-columns: 128px minmax(0, 1fr) 74px; align-items: center;
    gap: var(--s2); margin-bottom: 11px; font-size: 12.5px; color: var(--aw-ink-2); }
  .pt-lg li:last-child { margin-bottom: 0; }
  .pt-lg .tr { height: 8px; border-radius: 4px; background: var(--aw-line-2); overflow: hidden; }
  .pt-lg .tr i { display: block; height: 100%; border-radius: 4px; background: var(--aw-red); }
  .pt-lg .vv { text-align: right; font-family: 'IBM Plex Sans', sans-serif; color: var(--aw-ink);
    font-weight: 600; }

  /* \u2500 Badge system \u2500 */
  .page[data-page="awards"] .lg-tile, .page[data-page="awards2026"] .lg-tile,
  .page[data-page="verify"] .lg-tile, .page[data-page="brokerawards"] .lg-tile,
  .page[data-page="partner"] .lg-tile,
  .page[data-page="awards"] .lgmono, .page[data-page="awards2026"] .lgmono,
  .page[data-page="verify"] .lgmono, .page[data-page="brokerawards"] .lgmono,
  .page[data-page="partner"] .lgmono { color: #FFFFFF; font-weight: 700; }
  .aw-strow { display: inline-flex; align-items: center; gap: 3px; line-height: 0; }
  .aw-hofx { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: var(--s2); }
  .aw-hx { border: 1px solid var(--aw-line); border-radius: 12px; background: #FFFFFF;
    overflow: hidden; text-decoration: none; color: inherit; display: block;
    transition: border-color .22s ease, box-shadow .22s ease, transform .22s ease; }
  .aw-hx:hover { border-color: var(--aw-gold-e); box-shadow: 0 12px 32px -22px rgba(10,10,10,0.5);
    transform: translateY(-2px); }
  .aw-hx:focus-visible { outline: 2px solid var(--aw-red); outline-offset: 3px; }
  .aw-hxt { background: var(--aw-ink); padding: var(--s2) var(--s2) 14px; text-align: center; }
  .aw-hxt .aw-strow { margin-bottom: 10px; }
  .aw-hxt b { display: block; font-family: 'IBM Plex Sans', sans-serif; font-size: 30px;
    font-weight: 700; letter-spacing: -0.035em; color: #FFFFFF; line-height: 1; }
  .aw-hxt span { display: block; margin-top: 5px; font-size: 11px; font-weight: 700;
    letter-spacing: 0.06em; text-transform: uppercase; color: var(--aw-gold); }
  .aw-hxb { padding: var(--s2); text-align: center; }
  .aw-hxb .lg-tile { margin: 0 auto 10px; }
  .aw-hxb strong { display: block; font-size: 13.5px; font-weight: 600; color: var(--aw-ink); }
  .aw-hxb em { display: block; font-style: normal; font-size: 11.5px; color: var(--aw-ink-3);
    margin-top: 3px; }
  .aw-hxy { border-top: 1px solid var(--aw-line-2); padding: 10px var(--s2);
    display: flex; gap: 4px; flex-wrap: wrap; justify-content: center; }
  .aw-hxy i { font-style: normal; font-family: 'IBM Plex Sans', sans-serif; font-size: 10.5px;
    font-weight: 600; color: var(--aw-ink-2); background: var(--aw-line-2);
    border-radius: 5px; padding: 2px 7px; }
  .aw-mark { display: flex; align-items: center; gap: var(--s3); }
  .aw-mark .tx h3 { margin: 0 0 4px; font-size: 34px; font-weight: 700; letter-spacing: -0.035em;
    color: #FFFFFF; line-height: 1; }
  .aw-mark .tx h3 i { font-style: normal; color: var(--aw-red); }
  .aw-mark .tx span { font-size: 13px; font-weight: 600; letter-spacing: 0.14em;
    text-transform: uppercase; color: var(--aw-gold); }
  /* \u2500 \u0e2b\u0e19\u0e49\u0e32\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e01\u0e32\u0e23\u0e43\u0e2b\u0e49\u0e14\u0e32\u0e27 \u2500 */
  .page[data-page="criteria"] {
    --aw-red: #B91C1C;      --aw-red-d: #7F1313;   --aw-red-l: #FDF2F2;
    --aw-red-e: #F6D5D5;    --aw-ink: #0A0A0A;     --aw-ink-2: #3F3F46;
    --aw-ink-3: #71717A;    --aw-line: #E4E4E7;    --aw-line-2: #F4F4F5;
    --aw-gold: #A98420;     --aw-gold-l: #FBF6E7;  --aw-gold-e: #EBDCA8;
    --aw-gold-t: #7A5C11;   --aw-ok: #05603A;      --aw-ok-l: #ECFDF3;
    --s1: 8px;  --s2: 16px; --s3: 24px; --s4: 32px; --s5: 40px;
    --s6: 48px; --s7: 64px; --s8: 80px; --s9: 96px;
  }
  .page[data-page="criteria"] .lg-tile, .page[data-page="criteria"] .lgmono { color: #FFFFFF; }

  .cr-rule { display: grid; grid-template-columns: 64px minmax(0, 1fr); gap: var(--s3);
    border: 1px solid var(--aw-line); border-left: 4px solid var(--aw-red); border-radius: 14px;
    background: #FFFFFF; padding: var(--s4) var(--s5); align-items: start; }
  .cr-rule .st { display: flex; justify-content: center; padding-top: 4px; }
  .cr-rule h2 { margin: 0 0 10px; font-size: 24px; font-weight: 700; letter-spacing: -0.03em;
    color: var(--aw-ink); }
  .cr-rule p { margin: 0 0 var(--s2); font-size: 14px; line-height: 1.85; color: var(--aw-ink-2); }
  .cr-rule p:last-child { margin-bottom: 0; }
  .cr-rule b { color: var(--aw-ink); font-weight: 700; }
  .cr-rule .hl { background: var(--aw-red-l); border-radius: 4px; padding: 1px 5px; color: var(--aw-red); }

  .cr-lv { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--s3); }
  .cr-c { border: 1px solid var(--aw-line); border-radius: 14px; background: #FFFFFF;
    overflow: hidden; display: flex; flex-direction: column; }
  .cr-c.top { border-color: var(--aw-gold-e); box-shadow: 0 18px 44px -34px rgba(122,92,17,0.7); }
  .cr-ch { background: #FAFAFA; padding: var(--s3); text-align: center;
    border-bottom: 1px solid var(--aw-line); }
  .cr-c.top .cr-ch { background: var(--aw-ink); border-bottom-color: var(--aw-ink); }
  .cr-ch .aw-strow { margin-bottom: 12px; }
  .cr-ch h3 { margin: 0 0 5px; font-size: 20px; font-weight: 700; letter-spacing: -0.02em;
    color: var(--aw-ink); }
  .cr-c.top .cr-ch h3 { color: #FFFFFF; }
  .cr-ch span { font-size: 12px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
    color: var(--aw-ink-3); }
  .cr-c.top .cr-ch span { color: var(--aw-gold); }
  .cr-cb { padding: var(--s3); flex: 1; }
  .cr-cb .lead { margin: 0 0 var(--s3); font-size: 13px; line-height: 1.85; color: var(--aw-ink-2);
    padding-bottom: var(--s3); border-bottom: 1px solid var(--aw-line-2); }
  .cr-cb .lead b { color: var(--aw-ink); font-weight: 700; }
  .cr-li { display: grid; grid-template-columns: 20px minmax(0, 1fr); gap: 10px;
    margin-bottom: 13px; font-size: 12.5px; line-height: 1.8; color: var(--aw-ink-2); }
  .cr-li:last-child { margin-bottom: 0; }
  .cr-li .tick { width: 20px; height: 20px; border-radius: 50%; display: flex;
    align-items: center; justify-content: center; background: var(--aw-red-l); margin-top: 2px; }
  .cr-li.plus .tick { background: var(--aw-gold-l); }
  .cr-li b { color: var(--aw-ink); font-weight: 700; }
  .cr-cf { border-top: 1px solid var(--aw-line-2); background: #FAFAFA;
    padding: 14px var(--s3); font-size: 12px; line-height: 1.75; color: var(--aw-ink-3); }
  .cr-cf b { display: block; font-size: 11px; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; color: var(--aw-red); margin-bottom: 5px; }

  /* \u0e40\u0e2a\u0e49\u0e19\u0e17\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e2a\u0e15\u0e23\u0e35\u0e04 */
  .cr-path { border: 1px solid var(--aw-line); border-radius: 14px; background: #FFFFFF;
    padding: var(--s5); overflow-x: auto; }
  .cr-track { display: grid; grid-template-columns: repeat(8, minmax(96px, 1fr));
    gap: var(--s2); min-width: 900px; }
  .cr-q { text-align: center; }
  .cr-qd { height: 96px; display: flex; flex-direction: column; justify-content: flex-end;
    align-items: center; gap: 7px; margin-bottom: 12px; }
  .cr-bar { width: 100%; border-radius: 6px 6px 0 0; background: var(--aw-red); }
  .cr-bar.g { background: var(--aw-gold); }
  .cr-bar.x { background: repeating-linear-gradient(45deg, #F4F4F5, #F4F4F5 4px, #E4E4E7 4px, #E4E4E7 8px);
    border: 1px solid var(--aw-line); border-bottom: 0; }
  .cr-q .ql { font-family: 'IBM Plex Sans', sans-serif; font-size: 11.5px; font-weight: 600;
    color: var(--aw-ink-2); }
  .cr-q .qs { display: block; margin-top: 5px; font-size: 10.5px; line-height: 1.5;
    color: var(--aw-ink-3); }
  .cr-q.fail .ql { color: var(--aw-red); }
  .cr-note { margin: var(--s3) 0 0; font-size: 12.5px; line-height: 1.85; color: var(--aw-ink-2);
    border-left: 2px solid var(--aw-red-e); padding-left: var(--s2); }
  .cr-note b { color: var(--aw-ink); font-weight: 700; }

  .cr-tb { width: 100%; border-collapse: collapse; border: 1px solid var(--aw-line);
    border-radius: 12px; overflow: hidden; }
  .cr-tb thead th { text-align: left; padding: 12px var(--s2); background: #FAFAFA;
    border-bottom: 1px solid var(--aw-line); font-size: 11px; font-weight: 700;
    letter-spacing: 0.05em; text-transform: uppercase; color: var(--aw-ink-3); }
  .cr-tb td { padding: 14px var(--s2); border-bottom: 1px solid var(--aw-line-2);
    font-size: 13px; line-height: 1.8; color: var(--aw-ink-2); vertical-align: top; }
  .cr-tb tr:last-child td { border-bottom: 0; }
  .cr-tb td b { color: var(--aw-ink); font-weight: 600; }
  .cr-tb .no { width: 58px; font-family: 'IBM Plex Sans', sans-serif; font-weight: 700;
    color: var(--aw-red); }

  .cr-pil { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: var(--s2); }
  .cr-p { border-top: 2px solid var(--aw-red); padding-top: 13px; }
  .cr-p .cd { font-family: 'IBM Plex Sans', sans-serif; font-size: 12px; font-weight: 700;
    color: var(--aw-red); }
  .cr-p b { display: block; margin: 5px 0 4px; font-size: 13px; font-weight: 600; color: var(--aw-ink); }
  .cr-p span { display: block; font-family: 'IBM Plex Sans', sans-serif; font-size: 11.5px;
    color: var(--aw-ink-3); }

  .cr-warn { display: grid; grid-template-columns: 30px minmax(0, 1fr); gap: 13px;
    border: 1px solid #F5DFC4; background: #FEF6EE; border-radius: 12px;
    padding: var(--s3) var(--s4); margin-top: var(--s7); }
  .cr-warn .ic { display: flex; justify-content: center; padding-top: 2px; }
  .cr-warn b { display: block; font-size: 14px; font-weight: 700; color: #7A3F08; margin-bottom: 6px; }
  .cr-warn p { margin: 0 0 8px; font-size: 12.5px; line-height: 1.85; color: #93500B; }
  .cr-warn p:last-child { margin-bottom: 0; }
  .cr-warn code { font-family: 'IBM Plex Sans', sans-serif; font-size: 11.5px;
    background: #FFFFFF; border: 1px solid #F5DFC4; border-radius: 4px; padding: 1px 6px; }

  .bdg-wrap { display: flex; gap: var(--s3); flex-wrap: wrap; align-items: flex-end; }
  .bdg { display: block; border-radius: 6px; overflow: hidden; }
  .bdg-lb { margin-top: 10px; font-family: 'IBM Plex Sans', sans-serif; font-size: 11px;
    color: var(--aw-ink-3); }

  /* \u2500 \u0e1b\u0e38\u0e48\u0e21 Hall of Fame \u0e43\u0e19\u0e1a\u0e25\u0e47\u0e2d\u0e01 RED STAR \u2500 */
  .pk-hof { display: inline-flex; align-items: center; gap: 8px; margin-top: 14px;
    border: 1px solid #C9A227; background: #FFFFFF; color: #7A6329; border-radius: 999px;
    padding: 7px 16px 7px 13px; font: inherit; font-size: 13px; font-weight: 600;
    text-decoration: none; transition: background .18s, border-color .18s, color .18s; }
  .pk-hof:hover { background: #FBF6E7; border-color: #A98420; color: #6A5620; }
  .pk-hof:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }

  .ea-blocks { display: flex; flex-direction: column; gap: 22px; }
  .ea-block { display: grid; grid-template-columns: 452px minmax(0, 1fr);
    border: 1px solid #EAECF0; border-radius: 18px; background: #FFFFFF; overflow: hidden; }
  .ea-info { padding: 24px 26px; display: flex; flex-direction: column; gap: 12px;
    border-right: 1px solid #EAECF0; }
  .ea-demo { padding: 20px 22px; background: #F5F7FA; }
  .ea-got { display: flex; flex-direction: column; gap: 5px; font-size: 12.5px;
    line-height: 1.65; color: #667085; padding-top: 12px; border-top: 1px solid #F0F2F5; }
  .ea-got b { font-size: 11px; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; color: #B42318; margin-bottom: 2px; }
  .ea-got span { position: relative; padding-left: 15px; }
  .ea-got span::before { content: ""; position: absolute; left: 0; top: 8px; width: 5px; height: 5px;
    border-radius: 50%; background: #D0D5DD; }

  /* \u0e27\u0e34\u0e18\u0e35\u0e15\u0e34\u0e14\u0e15\u0e31\u0e49\u0e07 \u2014 \u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27 \u0e08\u0e36\u0e07\u0e40\u0e02\u0e35\u0e22\u0e19\u0e44\u0e27\u0e49\u0e17\u0e35\u0e48\u0e40\u0e14\u0e35\u0e22\u0e27 */
  .ea-install { margin-top: 24px; border: 1px solid #EAECF0; border-radius: 18px;
    background: #FFFFFF; padding: 24px 26px; display: grid;
    grid-template-columns: minmax(0, 1.6fr) minmax(0, 1fr); gap: 28px; align-items: start; }
  .ea-install h5 { margin: 0 0 12px; font-size: 12px; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; color: #B42318; }
  .ea-h4 { margin: 0; }
  .ea-top { display: flex; align-items: center; justify-content: space-between; gap: 10px; }
  .ea-ph { display: inline-block; }
  .ea-ph { font-size: 11px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase;
    color: #667085; background: #F5F7FA; border: 1px solid #EAECF0; border-radius: 999px; padding: 3px 10px; }
  .ea-h4 { display: block; font-size: 16.5px; font-weight: 600; letter-spacing: -0.015em;
    color: #101828; line-height: 1.35; }
  .ea-p { display: block; margin: 0; font-size: 13.5px; line-height: 1.7; color: #475467; }
  .ea-ul { display: flex; flex-direction: column; gap: 7px; margin: 0; padding: 0; list-style: none; }
  .ea-ul li, .ea-li { display: block; position: relative; padding-left: 19px;
    font-size: 13px; line-height: 1.65; color: #475467; }
  .ea-ul li::before, .ea-li::before { content: ""; position: absolute; left: 0; top: 7px;
    width: 7px; height: 7px; border-radius: 2px; background: #D92D20; }
  .ea-for { display: block; font-size: 12.5px; line-height: 1.65; color: #667085; padding-top: 12px;
    border-top: 1px solid #F0F2F5; }
  .ea-for b { display: block; font-size: 11px; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; color: #B42318; margin-bottom: 4px; }
  .ea-get { display: inline-flex; align-items: center; justify-content: center; gap: 8px;
    font-size: 14px; font-weight: 600; color: #FFFFFF; background: #D92D20; border: 1px solid #D92D20;
    border-radius: 10px; padding: 11px 16px; text-decoration: none;
    transition: background .15s, border-color .15s; }
  .ea-get:hover { background: #B42318; border-color: #B42318; color: #FFFFFF; }
  .ea-mem { font-size: 11.5px; color: #667085; }
  .ea-cta { margin-top: auto; padding-top: 4px; display: flex; align-items: center;
    gap: 11px; flex-wrap: wrap; }

  .ea-priv { margin-top: 34px; border: 1px solid #EAECF0; border-radius: 18px; background: #F5F7FA;
    padding: 26px 28px; }
  .ea-priv h3 { margin: 0 0 6px; font-size: 19px; font-weight: 700; letter-spacing: -0.02em; color: #101828; }
  .ea-priv > p { margin: 0 0 20px; font-size: 13.5px; line-height: 1.7; color: #475467; }
  .ea-cols { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; }
  .ea-col h5 { margin: 0 0 11px; font-size: 13px; font-weight: 700; letter-spacing: 0.03em;
    text-transform: uppercase; }
  .ea-col.yes h5 { color: #067647; }
  .ea-col.no h5 { color: #B42318; }
  .ea-col.w h5 { color: #475467; }
  .ea-col ul { margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 7px; }
  .ea-col li { display: flex; align-items: flex-start; gap: 8px; font-size: 13px; line-height: 1.6; color: #475467; }
  .ea-col li svg { flex-shrink: 0; margin-top: 3px; }
  .ea-w { display: flex; align-items: center; gap: 10px; font-size: 13px; color: #475467; }
  .ea-w .bar { flex: 1; height: 9px; border-radius: 999px; background: #E4E7EC; overflow: hidden; }
  .ea-w .bar b { display: block; height: 100%; border-radius: 999px; background: #D92D20; }
  .ea-w .pc { font-family: 'IBM Plex Sans', sans-serif; font-size: 12.5px; font-weight: 700;
    color: #101828; width: 34px; text-align: right; }
  .ea-w .nm { width: 96px; }
  .ea-pnote { margin: 20px 0 0; padding-top: 16px; border-top: 1px solid #EAECF0;
    font-size: 12px; line-height: 1.7; color: #667085; }
  .ea-pnote b { color: #B42318; font-weight: 700; }

  /* ── หน้า Broker Alerts ── */
  .al-card { border: 1px solid #EAECF0; border-radius: 16px; background: #FFFFFF;
    overflow: hidden; margin-bottom: 16px; }
  .al-head { display: flex; align-items: flex-start; gap: 14px; padding: 18px 20px 16px;
    border-bottom: 1px solid #F5F7FA; }
  .al-sev { width: 34px; height: 34px; border-radius: 10px; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center; }
  .al-sev.hi { background: #FEF3F2; }
  .al-sev.md { background: #FEF6EE; }
  .al-ttl { flex: 1; min-width: 0; }
  .al-ttl h3 { margin: 0 0 5px; font-size: 16.5px; font-weight: 600; letter-spacing: -0.015em;
    color: #101828; line-height: 1.4; }
  .al-meta { display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
    font-size: 12.5px; color: #667085; }
  .al-meta b { color: #475467; font-weight: 600; }
  .al-pill { flex-shrink: 0; font-size: 11.5px; font-weight: 600; border-radius: 999px;
    padding: 5px 12px; white-space: nowrap; }
  .al-pill.wait { background: #FEF6EE; color: #93500B; border: 1px solid #F5DFC4; }
  .al-pill.replied { background: #F0FBF5; color: #067647; border: 1px solid #CFEBDC; }
  .al-pill.closed { background: #F5F7FA; color: #475467; border: 1px solid #EAECF0; }
  .al-body { padding: 16px 20px; font-size: 13.5px; line-height: 1.75; color: #475467; }
  .al-body b { color: #101828; font-weight: 600; }
  .al-reply { margin: 0 20px 18px; padding: 15px 17px; background: #F5F7FA;
    border: 1px solid #EAECF0; border-left: 3px solid #D92D20; border-radius: 0 12px 12px 0; }
  .al-reply .who { display: flex; align-items: center; gap: 8px; margin-bottom: 7px;
    font-size: 12.5px; font-weight: 600; color: #101828; }
  .al-reply .tag { font-size: 11px; font-weight: 600; color: #B42318; background: #FEF3F2;
    border: 1px solid #FECDCA; border-radius: 999px; padding: 3px 9px; }
  .al-reply p { margin: 0; font-size: 13px; line-height: 1.75; color: #475467; }
  .al-note { padding: 12px 20px; background: #F5F7FA; border-top: 1px solid #EAECF0;
    font-size: 12px; line-height: 1.7; color: #667085; }
  .al-note b { color: #B42318; font-weight: 700; }
  .al-empty { border: 1px solid #EAECF0; border-radius: 16px; background: #FFFFFF;
    padding: 44px 20px; text-align: center; font-size: 14px; line-height: 1.7; color: #667085; }

  .edu-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; }
  .edu-card { border: 1px solid #EAECF0; border-radius: 16px; background: #FFFFFF; padding: 22px;
    display: flex; flex-direction: column; gap: 11px; }
  .edu-n { width: 34px; height: 34px; border-radius: 10px; background: #D92D20; color: #FFFFFF;
    font-family: 'IBM Plex Sans', sans-serif; font-size: 15px; font-weight: 700;
    display: flex; align-items: center; justify-content: center; }
  .edu-card h4 { margin: 0; font-size: 16px; font-weight: 600; letter-spacing: -0.015em;
    color: #101828; line-height: 1.4; }
  .edu-card p { margin: 0; font-size: 13.5px; line-height: 1.7; color: #475467; }
  .edu-eg { margin-top: auto; padding-top: 13px; border-top: 1px solid #F0F2F5;
    font-size: 12.5px; line-height: 1.7; color: #667085; }
  .edu-eg b { display: block; font-size: 11px; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; color: #B42318; margin-bottom: 4px; }

  /* ── แถบเตือนภัยโบรกเกอร์แบบเลื่อน ── */
  .tkr { display: flex; align-items: stretch; background: #101828; border-top: 1px solid #1D2939;
    border-bottom: 1px solid #1D2939; height: 46px; overflow: hidden; }
  .tkr-label { display: flex; align-items: center; gap: 9px; flex-shrink: 0; padding: 0 18px;
    background: #D92D20; color: #FFFFFF; font-size: 12.5px; font-weight: 700;
    letter-spacing: 0.02em; white-space: nowrap; }
  .tkr-scroll { flex: 1; min-width: 0; overflow-x: auto; overflow-y: hidden; cursor: grab;
    scrollbar-width: none; -ms-overflow-style: none;
    -webkit-mask-image: linear-gradient(to right, transparent 0, #000 26px, #000 calc(100% - 26px), transparent 100%);
    mask-image: linear-gradient(to right, transparent 0, #000 26px, #000 calc(100% - 26px), transparent 100%); }
  .tkr-scroll::-webkit-scrollbar { display: none; }
  .tkr-scroll:active { cursor: grabbing; }
  .tkr-scroll:focus-visible { outline: 2px solid #D92D20; outline-offset: -2px; }
  .tkr-track { display: flex; align-items: center; height: 46px; width: max-content; }
  .tkr-item { display: inline-flex; align-items: center; gap: 9px; padding: 0 26px;
    white-space: nowrap; font-size: 13px; color: #C3C9D5;
    border-right: 1px solid #1D2939; }
  .tkr-item b { color: #FFFFFF; font-weight: 600; }
  .tkr-item em { font-style: normal; color: #98A2B3; font-size: 12px;
    font-family: 'IBM Plex Sans', sans-serif; }
  .tkr-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
  .tkr-dot.hi { background: #F97066; box-shadow: 0 0 0 3px rgba(249,112,102,0.18); }
  .tkr-dot.md { background: #F5A623; box-shadow: 0 0 0 3px rgba(245,166,35,0.16); }
  .tkr-pause { flex-shrink: 0; width: 44px; border: 0; border-left: 1px solid #1D2939;
    background: #101828; color: #98A2B3; cursor: pointer; display: flex; align-items: center;
    justify-content: center; transition: color .15s, background .15s; }
  .tkr-pause:hover { color: #FFFFFF; background: #1D2939; }
  .tkr-pause:focus-visible { outline: 2px solid #D92D20; outline-offset: -2px; }
  .tkr-sample { display: inline-flex; align-items: center; gap: 6px; padding: 0 26px;
    white-space: nowrap; font-size: 12px; color: #98A2B3; border-right: 1px solid #1D2939; }
  .tkr-sample i { font-style: normal; color: #F5A623; font-weight: 700; }

  /* ── หน้าเข้าสู่ระบบ / สมัครสมาชิก ── */
  .auth-wrap { width: 1200px; margin: 0 auto; padding: 56px 0 0; display: grid;
    grid-template-columns: 560px minmax(0, 1fr); gap: 32px; align-items: start; }
  .auth-card { border: 1px solid #EAECF0; border-radius: 18px; background: #FFFFFF; padding: 30px 32px 32px; }
  .auth-card .sec-rule { margin-bottom: 20px; }
  .auth-h { margin: 0 0 8px; font-size: 32px; font-weight: 700; letter-spacing: -0.03em; color: #101828; }
  .auth-sub { margin: 0 0 18px; font-size: 15px; line-height: 1.65; color: #475467; }
  .auth-warn { display: flex; align-items: flex-start; gap: 9px; margin: 0 0 22px; padding: 12px 14px;
    background: #FEF6EE; border: 1px solid #F5DFC4; border-radius: 11px;
    font-size: 12.5px; line-height: 1.65; color: #93500B; }
  .auth-warn svg { flex-shrink: 0; margin-top: 2px; }
  .auth-warn b { color: #7A3F06; font-weight: 700; }
  .auth-form { display: flex; flex-direction: column; gap: 15px; }
  .fld { display: flex; flex-direction: column; gap: 7px; }
  .fld > span { font-size: 12.5px; font-weight: 600; color: #475467; }
  .fld input, .fld select { font: inherit; font-size: 14.5px; color: #101828; background: #FFFFFF;
    border: 1px solid #D0D5DD; border-radius: 10px; padding: 11px 14px; width: 100%; }
  .fld select { appearance: none; -webkit-appearance: none; cursor: pointer; padding-right: 40px;
    background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%23475467' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
    background-repeat: no-repeat; background-position: right 14px center; }
  .fld input::placeholder { color: #98A2B3; }
  .fld input:focus, .fld select:focus { outline: none; border-color: #D92D20; box-shadow: 0 0 0 3px #FEF3F2; }
  .fld-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  .fld-pw { position: relative; display: block; }
  .fld-pw input { padding-right: 44px; }
  .pw-eye { position: absolute; right: 6px; top: 50%; transform: translateY(-50%);
    background: transparent; border: 0; padding: 6px; cursor: pointer; line-height: 0; border-radius: 8px; }
  .pw-eye:hover svg { stroke: #101828; }
  .pw-eye:focus-visible { outline: 2px solid #D92D20; outline-offset: 1px; }
  .auth-row { display: flex; align-items: center; justify-content: space-between; gap: 14px; }
  .chk { display: inline-flex; align-items: flex-start; gap: 9px; font-size: 13.5px; color: #475467; cursor: pointer; }
  .chk input { width: 17px; height: 17px; accent-color: #D92D20; margin: 1px 0 0; flex-shrink: 0; }
  .chk-tos { line-height: 1.6; }
  .auth-link { color: #D92D20; font-weight: 600; }
  .auth-link:hover { color: #B42318; }
  .auth-submit { width: 100%; padding: 12px 18px; font-size: 15px; margin-top: 3px; }
  .auth-alt { margin: 18px 0 0; padding-top: 18px; border-top: 1px solid #F0F2F5;
    font-size: 13.5px; color: #475467; text-align: center; }
  .auth-side { border: 1px solid #EAECF0; border-radius: 18px; background: #F5F7FA; padding: 30px 30px 26px; }
  .auth-side h3 { margin: 0 0 16px; font-size: 19px; font-weight: 700; letter-spacing: -0.02em; color: #101828; }
  .auth-list { margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 15px; }
  .auth-list li { display: flex; flex-direction: column; gap: 3px; padding-left: 20px; position: relative; }
  .auth-list li::before { content: ""; position: absolute; left: 0; top: 7px; width: 8px; height: 8px;
    border-radius: 2px; background: #D92D20; }
  .auth-list b { font-size: 14.5px; font-weight: 600; color: #101828; }
  .auth-list span { font-size: 13px; line-height: 1.65; color: #475467; }
  .auth-note { margin: 22px 0 0; padding-top: 18px; border-top: 1px solid #EAECF0;
    font-size: 12.5px; line-height: 1.7; color: #667085; }
  .auth-note b { color: #B42318; font-weight: 700; }
  .art-head .art-h1 { margin: 0; font-size: 42px; line-height: 1.12; font-weight: 700;
    letter-spacing: -0.035em; color: #101828; }
  .art-h2 { display: block; font-size: 22px; line-height: 1.35; font-weight: 600;
    letter-spacing: -0.02em; color: #475467; }
  .art-eyebrow { display: inline-flex; align-items: center; gap: 10px; font-family: 'IBM Plex Sans', sans-serif;
    font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #B42318; }
  .art-eyebrow::before { content: ""; width: 26px; height: 2px; background: #D92D20; border-radius: 2px; }
  .art-head h2 { margin: 0; font-size: 34px; font-weight: 700; letter-spacing: -0.03em; color: #101828; }
  .art-head p { margin: 0; font-size: 16px; line-height: 1.65; color: #475467; }
  .art-ctl { display: flex; align-items: center; justify-content: space-between;
    gap: 16px 24px; flex-wrap: wrap; margin-bottom: 24px; }
  .art-cats { display: flex; gap: 8px; flex-wrap: wrap; }
  .art-cat { font: inherit; font-size: 13.5px; padding: 8px 17px; border-radius: 999px; cursor: pointer;
    border: 1px solid #EAECF0; background: #FFFFFF; color: #475467;
    transition: border-color .15s, background .15s, color .15s; }
  .art-cat:hover { border-color: #D0D5DD; color: #101828; }
  .art-cat[aria-pressed="true"] { background: #D92D20; border-color: #D92D20; color: #FFFFFF; font-weight: 600; }
  .art-cat:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }
  .art-qbox { min-width: 268px; }

  .art-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
  .art-card { border: 1px solid #EAECF0; border-radius: 16px; overflow: hidden; background: #FFFFFF;
    display: flex; flex-direction: column; cursor: pointer;
    transition: border-color .18s, box-shadow .18s, transform .18s; }
  .art-card:hover { border-color: #D0D5DD; box-shadow: 0 12px 28px -14px rgba(16,24,40,0.22);
    transform: translateY(-2px); }
  .art-card:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }
  .art-cover { position: relative; height: 168px; background: #101828; overflow: hidden; flex-shrink: 0; }
  .art-cover::before { content: ""; position: absolute; right: -12%; top: -34%; width: 74%; height: 128%;
    background: radial-gradient(closest-side, rgba(217,45,32,0.55), rgba(217,45,32,0) 72%); }
  .art-art { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 1; }
  .art-cover::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 58%; z-index: 1;
    background: linear-gradient(to top, rgba(16,24,40,0.92), rgba(16,24,40,0)); }
  .art-badge { position: absolute; left: 16px; top: 16px; z-index: 2; font-size: 11.5px; font-weight: 600;
    color: #101828; background: #FFFFFF; border-radius: 999px; padding: 4px 11px; }
  .art-star { position: absolute; left: 16px; bottom: 15px; z-index: 2; display: block; line-height: 0; }
  .art-mk { position: absolute; right: 16px; bottom: 17px; z-index: 2; font-family: 'IBM Plex Sans', sans-serif;
    font-size: 10.5px; font-weight: 600; letter-spacing: 0.16em; color: #98A2B3; text-transform: uppercase; }
  .art-body { padding: 17px 19px 19px; display: flex; flex-direction: column; gap: 8px; flex: 1; }
  .art-meta { display: flex; align-items: center; gap: 7px; font-size: 12px; color: #667085; }
  .art-title { margin: 0; font-size: 16.5px; font-weight: 600; line-height: 1.42;
    letter-spacing: -0.01em; color: #101828; }
  .art-ex { margin: 0; font-size: 13.5px; line-height: 1.65; color: #475467; }
  .art-more { margin-top: auto; padding-top: 12px; font-size: 13.5px; font-weight: 600; color: #D92D20;
    display: inline-flex; align-items: center; gap: 7px; }
  .art-card:hover .art-more { color: #B42318; }
  .art-card.feat { grid-column: span 2; flex-direction: row; }
  .art-card.feat .art-cover { height: auto; width: 344px; }
  .art-card.feat .art-body { padding: 30px 32px; gap: 11px; justify-content: center; }
  .art-card.feat .art-title { font-size: 23px; line-height: 1.34; letter-spacing: -0.022em; }
  .art-card.feat .art-ex { font-size: 14.5px; }
  .art-card.feat.solo { grid-column: 1 / -1; }
  .art-card.feat.solo .art-cover { width: 420px; }
  .art-empty { grid-column: 1 / -1; border: 1px solid #EAECF0; border-radius: 16px; background: #FFFFFF;
    padding: 46px 22px; text-align: center; font-size: 14px; line-height: 1.7; color: #667085; }
  .art-note { margin: 18px 0 0; font-size: 12px; line-height: 1.7; color: #667085; }
  .art-note b { color: #475467; font-weight: 600; }

  /* ── เมนูหลัก สี่หน้า ── */
  .mh-nav a { position: relative; padding-bottom: 4px; }
  .hero-dark .mh-nav a[aria-current="page"] { color: #101828 !important; font-weight: 600; }
  .mh-nav a[aria-current="page"]::after { content: ""; position: absolute; left: 0; right: 0; bottom: -1px;
    height: 2px; background: #D92D20; border-radius: 2px; }
  .mh-nav a:focus-visible { outline: 2px solid #D92D20; outline-offset: 3px; border-radius: 3px; }

  /* ── ปุ่มดูบทความทั้งหมด ── */
  .art-more-row { display: flex; align-items: center; justify-content: space-between;
    gap: 14px 26px; flex-wrap: wrap; margin-top: 26px; }
  .art-viewmore { display: inline-flex; align-items: center; gap: 9px; font-size: 14.5px; font-weight: 600;
    color: #FFFFFF; background: #D92D20; border: 1px solid #D92D20; border-radius: 10px;
    padding: 11px 22px; text-decoration: none; transition: background .15s, border-color .15s; }
  .art-viewmore:hover { background: #B42318; border-color: #B42318; color: #FFFFFF; }
  .art-viewmore:focus-visible { outline: 2px solid #D92D20; outline-offset: 3px; }
  .art-more-row .art-note { margin: 0; text-align: right; max-width: 660px; }

  /* ── หน้ารีวิวโบรกเกอร์ ── */
  .rv-tools { display: flex; align-items: flex-end; gap: 12px; flex-wrap: wrap; }
  .rv-tools .rk-pick > span { font-size: 11px; }
  .rv-tools .rk-pick select { min-width: 186px; font-size: 14px; padding: 9px 34px 9px 13px;
    background-position: right 12px center; }
  .rv-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; }
  .rv-card { border: 1px solid #EAECF0; border-radius: 16px; background: #FFFFFF; padding: 20px;
    display: flex; flex-direction: column; gap: 13px;
    transition: border-color .18s, box-shadow .18s, transform .18s; }
  .rv-card:hover { border-color: #D0D5DD; box-shadow: 0 12px 28px -14px rgba(16,24,40,0.22);
    transform: translateY(-2px); }
  .rv-top { display: flex; align-items: center; gap: 12px; }
  .rv-name { display: block; font-size: 16px; font-weight: 600; letter-spacing: -0.01em; color: #101828; }
  .rv-reg { display: block; font-size: 12px; color: #667085; margin-top: 2px; }
  .rv-mid { display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; }
  .rv-score { font-family: 'IBM Plex Sans', sans-serif; font-size: 27px; font-weight: 700;
    letter-spacing: -0.03em; color: #101828; font-variant-numeric: tabular-nums; line-height: 1; }
  .rv-of { font-size: 13px; color: #667085; margin-left: 3px; }
  .rv-cap { display: block; font-size: 11.5px; color: #667085; margin-top: 5px; }
  .rv-stars { display: flex; flex-direction: column; align-items: flex-end; gap: 4px; }
  .rv-stars .n { font-size: 11.5px; color: #475467; }
  .rv-meta { font-size: 12.5px; line-height: 1.65; color: #667085; padding-top: 12px;
    border-top: 1px solid #F0F2F5; }
  .rv-meta b { color: #475467; font-weight: 600; }
  .rv-cta { margin-top: auto; padding-top: 2px; }

  /* ── ตารางวอลลุ่มรายประเทศ ── */
  .an-wrap { margin-top: 26px; border: 1px solid #EAECF0; border-radius: 16px;
    background: #FFFFFF; overflow: hidden; }
  .an-row { display: grid; grid-template-columns: 54px minmax(0, 1.15fr) 168px minmax(0, 1.35fr) 82px;
    align-items: center; gap: 18px; padding: 10px 20px; border-bottom: 1px solid #F5F7FA; }
  .an-row:last-child { border-bottom: 0; }
  .an-row.hd { background: #F5F7FA; border-bottom: 1px solid #EAECF0; font-size: 12px;
    letter-spacing: 0.04em; text-transform: uppercase; color: #667085; padding: 12px 20px; }
  .an-rank { font-family: 'IBM Plex Sans', sans-serif; font-size: 13.5px; font-weight: 700;
    color: #667085; font-variant-numeric: tabular-nums; }
  .an-name { font-size: 14.5px; font-weight: 600; color: #101828; display: flex; align-items: center; gap: 9px; }
  .an-sw { width: 12px; height: 12px; border-radius: 3px; display: inline-block; flex-shrink: 0; }
  .an-zone { font-size: 13px; color: #475467; }
  .an-bar { height: 13px; border-radius: 999px; background: #F2F4F7;
    border: 1px solid #E4E7EC; overflow: hidden; }
  .an-bar b { display: block; height: 100%; border-radius: 999px;
    background: linear-gradient(90deg, #E8483E, #D92D20); }
  .an-pct { font-family: 'IBM Plex Sans', sans-serif; font-size: 14px; font-weight: 700;
    font-variant-numeric: tabular-nums; color: #101828; text-align: right; }
  .an-empty { padding: 40px 20px; text-align: center; font-size: 14px; color: #667085; }
  .map-svg path[data-vshare] { cursor: help; }
  .lgmono { line-height: 1; }
  [data-logo] { position: relative; overflow: hidden; }
  [data-logo] img { position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: contain; background: #FFFFFF; padding: 3px; }


  /* ── ตารางอันดับรายประเทศ ── */
  .rk-tabs { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; }
  .rk-tab {
    font: inherit; font-size: 14px; padding: 9px 18px; border-radius: 999px; cursor: pointer;
    border: 1px solid #EAECF0; background: #FFFFFF; color: #475467;
    display: inline-flex; align-items: center; gap: 8px;
    transition: border-color .15s, background .15s, color .15s;
  }
  .rk-tab:hover { border-color: #D0D5DD; color: #101828; }
  .rk-tab[aria-pressed="true"] { border: 1.5px solid #D92D20; background: #FEF3F2; color: #B42318; font-weight: 600; }
  .rk-tab .n { font-family: 'IBM Plex Sans', sans-serif; font-size: 12px; opacity: .7; }
  .rk-wrap { border: 1px solid #EAECF0; border-radius: 16px; overflow: hidden; background: #FFFFFF; }
  .rk-scroll { overflow-x: auto; }
  .rk-table { border-collapse: collapse; width: 100%; min-width: 1330px; font-size: 14.5px; }
  .rk-table thead th.num { min-width: 96px; }
  .rk-table thead th {
    text-align: left; background: #F5F7FA; color: #667085; font-weight: 500; font-size: 12px;
    letter-spacing: 0.04em; text-transform: uppercase; padding: 14px 18px;
    border-bottom: 1px solid #EAECF0; white-space: nowrap;
  }
  .rk-table thead th.num, .rk-table tbody td.num { text-align: right; }
  .rk-table tbody td { padding: 15px 18px; border-bottom: 1px solid #F0F2F5; vertical-align: middle; }
  .rk-table tbody tr:last-child td { border-bottom: 0; }
  .rk-table tbody tr:hover td { background: #FCFCFD; }
  .rk-rank { font-family: 'IBM Plex Sans', sans-serif; font-size: 16px; font-weight: 700; color: #667085; font-variant-numeric: tabular-nums; }
  .rk-rank.top { color: #D92D20; }
  .rk-name { display: flex; align-items: center; gap: 12px; }
  .rk-name .t { display: flex; flex-direction: column; gap: 2px; }
  .rk-name b { font-size: 15.5px; font-weight: 600; letter-spacing: -0.015em; }
  .rk-name .t span { font-size: 12.5px; color: #667085; }
  .rk-name .lgmono { color: #FFFFFF; font-size: 12px; }
  .rk-stars { display: flex; gap: 3px; }
  .rk-stars svg { width: 15px; height: 15px; fill: #D92D20; }
  .rk-total { font-family: 'IBM Plex Sans', sans-serif; font-size: 19px; font-weight: 700; letter-spacing: -0.03em; font-variant-numeric: tabular-nums; }
  .rk-sub { font-family: 'IBM Plex Sans', sans-serif; font-size: 14.5px; font-variant-numeric: tabular-nums; color: #475467; }
  .rk-sub.best { color: #B42318; font-weight: 600; }
  .rk-cta {
    display: inline-block; font-size: 13.5px; font-weight: 600; color: #D92D20;
    border: 1px solid #FECDCA; background: #FFFFFF; border-radius: 8px; padding: 7px 14px;
    white-space: nowrap; cursor: pointer; transition: background .15s, border-color .15s;
  }
  .rk-cta:hover { background: #FEF3F2; border-color: #D92D20; }
  .rk-note { font-size: 12.5px; color: #667085; margin: 14px 0 0; line-height: 1.7; }

  /* ── เทียบตัวต่อตัว ── */
  .cmp-picks { display: flex; align-items: flex-end; gap: 12px; flex-wrap: wrap; }
  .cmp-picks .rk-pick > span { font-size: 11px; }
  .cmp-picks .rk-pick select {
    min-width: 150px; font-size: 14px; padding: 9px 34px 9px 13px;
    background-position: right 12px center;
  }
  #cmp-cat { min-width: 168px; }
  #cmp-iso { min-width: 182px; }
  #cmp-year { min-width: 104px; }
  #cmp-sel-a, #cmp-sel-b { min-width: 212px; }
  .cmp-vs { font-size: 12.5px; color: #667085; letter-spacing: 0.04em; padding-bottom: 11px; }
  .cmp-grid { display: grid; grid-template-columns: minmax(0, 1fr) 372px; gap: 24px;
    align-items: start; margin-top: 18px; }
  .cmp-card { border: 1px solid #EAECF0; border-radius: 16px; overflow: hidden; background: #FFFFFF; }
  .cmp-head { display: grid; grid-template-columns: 132px 1fr 1fr; background: #F5F7FA; border-bottom: 1px solid #EAECF0; }
  .cmp-head > div { padding: 11px 14px; }
  .cmp-head .who { display: flex; align-items: center; gap: 10px; }
  .cmp-head .who b { font-size: 14.5px; font-weight: 600; letter-spacing: -0.02em; }
  .cmp-head .who > span > span { display: block; font-size: 11.5px; color: #667085; }
  .cmp-head .who .lgmono { display: inline; color: #FFFFFF; font-size: 11px; }
  .cmp-row { display: grid; grid-template-columns: 132px 1fr 1fr; border-bottom: 1px solid #F0F2F5; }
  .cmp-row:last-child { border-bottom: 0; }
  .cmp-row > div { padding: 8px 14px; display: flex; align-items: center; gap: 8px; }
  .cmp-label { color: #475467; font-size: 12.5px; }
  .cmp-val { font-family: 'IBM Plex Sans', sans-serif; font-size: 14.5px; font-weight: 600; font-variant-numeric: tabular-nums; color: #101828; }
  .cmp-win { background: #FEF3F2; }
  .cmp-win .cmp-val { color: #B42318; }
  .cmp-delta { font-family: 'IBM Plex Sans', sans-serif; font-size: 11px; font-weight: 600; color: #B42318; border: 1px solid #FECDCA; border-radius: 999px; padding: 1px 7px; }
  .cmp-tie { font-size: 12.5px; color: #667085; }
  .cmp-sum { display: flex; flex-wrap: wrap; gap: 7px 16px; align-items: center; padding: 10px 14px; background: #F5F7FA; border-top: 1px solid #EAECF0; font-size: 12px; color: #475467; }
  .cmp-sum b { color: #101828; }

  /* ── แผงสรุป RedStar Thinking — อ่านตัวเลขจากตารางด้านซ้าย ไม่สร้างข้อมูลใหม่ ── */
  .cmp-ai { border: 1px solid #EAECF0; border-radius: 16px; background: #FFFFFF; overflow: hidden; }
  .ai-head { display: flex; align-items: center; gap: 10px; padding: 13px 16px;
    background: #F5F7FA; border-bottom: 1px solid #EAECF0; }
  .ai-mark { width: 28px; height: 28px; border-radius: 8px; background: #D92D20;
    display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .ai-head b { font-size: 14px; font-weight: 600; color: #101828; letter-spacing: -0.01em; display: block; }
  .ai-head b + span { display: block; font-size: 11.5px; color: #667085; margin-top: 1px; }
  .ai-verdict { padding: 15px 16px; border-bottom: 1px solid #F0F2F5; }
  .ai-v { display: block; font-size: 17px; font-weight: 700; letter-spacing: -0.02em;
    color: #101828; line-height: 1.35; }
  .ai-s { display: block; margin-top: 6px; font-size: 12.5px; line-height: 1.6; color: #475467; }
  .ai-s b { color: #101828; font-weight: 600; }
  .ai-list { padding: 13px 16px; display: flex; flex-direction: column; gap: 11px; }
  .ai-item { display: flex; gap: 9px; font-size: 12.5px; line-height: 1.6; color: #475467; }
  .ai-item b { color: #101828; font-weight: 600; }
  .ai-ic { flex-shrink: 0; margin-top: 2px; }
  .ai-foot { padding: 11px 16px; background: #F5F7FA; border-top: 1px solid #EAECF0;
    font-size: 11px; line-height: 1.65; color: #667085; }
  .ai-foot b { color: #475467; font-weight: 600; }
  .ai-empty { padding: 28px 16px; text-align: center; font-size: 13px; color: #667085; line-height: 1.6; }


  /* ── หมวดสินทรัพย์ + กราฟ ── */
  .rk-cats { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px; }
  .rk-cat {
    font: inherit; font-size: 14.5px; font-weight: 500; padding: 10px 20px; border-radius: 10px;
    cursor: pointer; border: 1px solid #EAECF0; background: #FFFFFF; color: #475467;
    transition: border-color .15s, background .15s, color .15s;
  }
  .rk-cat:hover { border-color: #D0D5DD; color: #101828; }
  .rk-cat[aria-pressed="true"] { background: #101828; border-color: #101828; color: #FFFFFF; }
  .rk-charts { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px; margin-top: 36px; }
  .chart-card { border: 1px solid #EAECF0; border-radius: 16px; background: #FFFFFF; padding: 26px 26px 20px; }
  .chart-head { margin-bottom: 20px; }
  .chart-head h3 { margin: 0 0 6px; font-size: 19px; font-weight: 600; letter-spacing: -0.02em; }
  .chart-head p { margin: 0; font-size: 13.5px; color: #667085; line-height: 1.55; }
  .chart-card svg { display: block; width: 100%; height: auto; }
  .chart-card svg text { font-family: Inter, 'IBM Plex Sans Thai', sans-serif; }
  .chart-legend { display: flex; flex-wrap: wrap; gap: 8px 18px; margin-top: 16px; padding-top: 14px;
    border-top: 1px solid #F0F2F5; font-size: 12.5px; color: #475467; }
  .chart-legend span { display: inline-flex; align-items: center; gap: 7px; }
  .chart-legend i { width: 11px; height: 11px; border-radius: 3px; display: inline-block; }
  @media (max-width: 1000px) { .rk-charts { grid-template-columns: 1fr; } }


  /* ── ช่องค้นหาในการ์ดลอย ── */
  #hs-q:focus { outline: none; border-color: #D92D20; background: #FFFFFF; }
  .hs-type {
    font: inherit; font-size: 12.5px; padding: 6px 12px; border-radius: 999px; cursor: pointer;
    border: 1px solid #EAECF0; background: #FFFFFF; color: #475467;
    transition: border-color .15s, background .15s, color .15s;
  }
  .hs-type:hover { border-color: #D0D5DD; color: #101828; }
  .hs-type[aria-pressed="true"] { background: #101828; border-color: #101828; color: #FFFFFF; font-weight: 600; }
  .hs-hit {
    display: flex; align-items: center; gap: 11px; width: 100%; text-align: left;
    font: inherit; padding: 10px 12px; border-radius: 10px; cursor: pointer;
    border: 1px solid #EAECF0; background: #FFFFFF; transition: border-color .15s, background .15s;
  }
  .hs-hit:hover { border-color: #D0D5DD; background: #FCFCFD; }
  .hs-hit b { font-size: 14.5px; font-weight: 600; color: #101828; letter-spacing: -0.015em; }
  .hs-hit .sub { display: block; font-size: 12px; color: #667085; }
  .hs-hit .stars { display: flex; gap: 2px; margin-left: auto; }
  .hs-hit .stars svg { width: 12px; height: 12px; fill: #D92D20; }
  .hs-empty { font-size: 13px; color: #667085; line-height: 1.6; padding: 14px 2px; }
  .hs-count { font-size: 12px; color: #667085; padding: 2px 2px 0; }


  /* ── กราฟเส้นย่อในช่องตาราง ── */
  .mcell { display: flex; flex-direction: column; align-items: flex-end; gap: 3px; }
  .mcell .mval { font-family: 'IBM Plex Sans', sans-serif; font-size: 15px; font-weight: 600;
    font-variant-numeric: tabular-nums; color: #101828; line-height: 1; }
  .mcell .mtrend { font-size: 11px; font-weight: 500; letter-spacing: 0; white-space: nowrap; }
  .mcell .mtrend.down { color: #067647; }
  .mcell .mtrend.up { color: #B54708; }
  .mcell .mtrend.flat { color: #667085; }
  .rk-charts { grid-template-columns: 1fr !important; }


  /* ── ช่องกราฟย่อแบบกะทัดรัด สำหรับคะแนนรายด้าน ── */
  .mini { display: flex; flex-direction: column; align-items: flex-end; gap: 2px; }
  .mini .v { font-family: 'IBM Plex Sans', sans-serif; font-size: 14.5px; font-weight: 600;
    font-variant-numeric: tabular-nums; color: #101828; line-height: 1; }
  .mini .r { display: flex; align-items: center; gap: 5px; }
  .mini .d { font-family: 'IBM Plex Sans', sans-serif; font-size: 10.5px; font-weight: 600;
    font-variant-numeric: tabular-nums; white-space: nowrap; }
  .mini .d.down { color: #067647; }
  .mini .d.up { color: #B54708; }
  .mini .d.flat { color: #667085; }
  .rk-sub.best { color: #B42318; font-weight: 600; }
  .mini.best .v { color: #B42318; }


  /* ── ดรอปดาวน์เลือกหมวดและประเทศ ── */
  .rk-picks { display: flex; flex-wrap: wrap; align-items: flex-end; gap: 16px 20px; margin-bottom: 22px; }
  .rk-pick { display: flex; flex-direction: column; gap: 7px; }
  .rk-pick > span { font-size: 12px; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; color: #667085; }
  .rk-pick select {
    appearance: none; -webkit-appearance: none;
    font: inherit; font-size: 14.5px; font-weight: 500; color: #101828;
    background-color: #FFFFFF; background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%23475467' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
    background-repeat: no-repeat; background-position: right 14px center;
    border: 1px solid #EAECF0; border-radius: 10px; padding: 11px 42px 11px 15px;
    min-width: 232px; cursor: pointer; transition: border-color .15s;
  }
  .rk-pick select:hover { border-color: #D0D5DD; }
  .rk-pick select:focus-visible { outline: none; border-color: #D92D20; box-shadow: 0 0 0 3px #FEF3F2; }
  .rk-pick select option:disabled { color: #667085; }
  .rk-picknote { margin: 0 0 2px; font-size: 12.5px; color: #667085; line-height: 1.55; max-width: 34ch; }


  /* ── ตารางแบบกระชับ + ตรึงคอลัมน์รีวิว ── */
  .rk-table { min-width: 1150px !important; }
  .rk-table thead th { padding: 11px 12px !important; font-size: 10.5px !important; }
  .rk-table tbody td { padding: 11px 12px !important; }
  .rk-table thead th.num { min-width: 74px !important; }
  .rk-name { gap: 10px !important; }
  .rk-name b { font-size: 14.5px !important; }
  .rk-name .t span { font-size: 11.5px !important; }
  .rk-rank { font-size: 15px !important; }
  .rk-stars svg { width: 13px !important; height: 13px !important; }

  .mcell, .mini { align-items: flex-end; gap: 3px; }
  .mcell .top, .mini .top { display: flex; align-items: baseline; gap: 6px; }
  .mcell .mval { font-size: 14.5px; }
  .mcell .mtrend { font-size: 10.5px; }
  .mini .v { font-size: 14px; }
  .mini .d { font-size: 10px; }

  .rk-table th.rk-sticky, .rk-table td.rk-sticky {
    position: sticky; right: 0; z-index: 2; background: #FFFFFF;
    box-shadow: -10px 0 14px -12px rgba(16,24,40,0.25);
  }
  .rk-table thead th.rk-sticky { background: #F5F7FA; z-index: 3; }
  .rk-table tbody tr:hover td.rk-sticky { background: #FCFCFD; }
  .rk-cta { padding: 6px 12px !important; font-size: 12.5px !important; }


  /* ── ซูมแผนที่ ── */
  #map-stage { cursor: grab; touch-action: none; }
  #map-stage.dragging { cursor: grabbing; }
  .mapzoom { position: absolute; right: 0; top: 0; z-index: 5; display: flex; flex-direction: column; gap: 6px; }
  .mapzoom button {
    font: inherit; font-size: 15px; font-weight: 600; line-height: 1; color: #475467;
    width: 32px; height: 32px; border: 1px solid #EAECF0; background: #FFFFFF; border-radius: 8px;
    cursor: pointer; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 2px 6px rgba(16,24,40,0.08); transition: border-color .15s, color .15s;
  }
  .mapzoom button#zoom-reset { font-size: 10.5px; font-weight: 500; width: 32px; height: 26px; letter-spacing: 0; }
  .mapzoom button:hover { border-color: #D0D5DD; color: #101828; }
  .mapzoom button:disabled { opacity: .4; cursor: not-allowed; }
  .mapzoom button:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }


  /* แอตทริบิวต์ hidden ต้องชนะ display:flex ที่เขียนไว้ในสไตล์ของอิลิเมนต์ */
  [hidden] { display: none !important; }

  /* ── ผลค้นหาในการ์ด: จำกัดความสูง ไม่ให้การ์ดยาวจนบังเนื้อหาข้างล่าง ── */
  #card-results { max-height: 316px; overflow-y: auto; padding-right: 2px; }
  #card-results::-webkit-scrollbar { width: 6px; }
  #card-results::-webkit-scrollbar-thumb { background: #D0D5DD; border-radius: 999px; }
  .hs-bar { display: flex; align-items: center; justify-content: space-between; gap: 10px; }
  .hs-close {
    font: inherit; font-size: 12.5px; font-weight: 500; color: #475467; background: #FFFFFF;
    border: 1px solid #EAECF0; border-radius: 999px; padding: 5px 12px; cursor: pointer;
    display: inline-flex; align-items: center; gap: 6px; transition: border-color .15s, color .15s;
  }
  .hs-close:hover { border-color: #D0D5DD; color: #101828; }
  .hs-close:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }


  /* ── แถบบนสีเข้ม + ช่องค้นหาทั้งเว็บ ── */
  .masthead-dark { background: #101828; padding: 18px 0 20px; }
  .mh-inner { width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px; }
  .mh-row { display: flex; align-items: center; justify-content: space-between; gap: 24px; }
  .mh-brand { display: flex; align-items: center; gap: 10px; color: #FFFFFF;
    font-family: Inter, sans-serif; font-size: 19px; font-weight: 700; letter-spacing: -0.02em; }
  .mh-nav { display: flex; gap: 26px; }
  .mh-nav a { color: #D6DAE3; font-size: 14.5px; text-decoration: none; transition: color .15s; }
  .mh-nav a:hover { color: #FFFFFF; }
  .mh-search { position: relative; display: flex; align-items: center; gap: 12px;
    background: #1B2438; border: 1px solid #2A3448; border-radius: 12px; padding: 13px 18px; }
  .mh-search input { flex: 1; font: inherit; font-size: 15px; color: #FFFFFF;
    background: transparent; border: 0; outline: none; }
  .mh-search input::placeholder { color: #98A2B3; }
  #top-results { position: absolute; left: 0; right: 0; top: calc(100% + 8px); z-index: 40;
    background: #FFFFFF; border: 1px solid #EAECF0; border-radius: 12px; padding: 6px;
    box-shadow: 0 20px 40px -16px rgba(16,24,40,0.28); max-height: 300px; overflow-y: auto; }
  .tr-hit { display: flex; align-items: center; gap: 11px; width: 100%; text-align: left;
    font: inherit; padding: 9px 11px; border-radius: 9px; border: 0; background: transparent; cursor: pointer; }
  .tr-hit:hover, .tr-hit:focus-visible { background: #F5F7FA; outline: none; }
  .tr-hit b { font-size: 14.5px; font-weight: 600; color: #101828; }
  .tr-hit span.s { font-size: 12px; color: #667085; display: block; }
  .tr-hit .st { margin-left: auto; display: flex; gap: 2px; }
  .tr-hit .st svg { width: 12px; height: 12px; fill: #D92D20; }
  .tr-none { padding: 14px 12px; font-size: 13px; color: #667085; line-height: 1.6; }

  /* ── Hero ── */
  .hero-badges { display: flex; align-items: center; gap: 12px; margin-bottom: 18px; }
  .hb-pill { background: #FEF3F2; color: #B42318; border: 1px solid #FECDCA; border-radius: 999px;
    padding: 5px 13px; font-size: 12.5px; font-weight: 600; }
  .hb-note { font-size: 14px; color: #475467; }
  .hero-h1 { margin: 0 0 16px; font-size: 50px; line-height: 1.1; font-weight: 700;
    letter-spacing: -0.035em; max-width: 17ch; text-wrap: balance; }
  .hero-sub { margin: 0 0 26px; font-size: 17px; line-height: 1.65; color: #475467; max-width: 66ch; }
  .hero-sub b { color: #101828; font-weight: 600; }
  .hero-cta { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 44px; }
  .hc-primary, .hc-ghost { display: inline-flex; align-items: center; gap: 9px; text-decoration: none;
    font-size: 15.5px; font-weight: 600; padding: 13px 22px; border-radius: 10px; transition: background .16s, border-color .16s; }
  .hc-primary { background: #D92D20; color: #FFFFFF; }
  .hc-primary:hover { background: #B42318; color: #FFFFFF; }
  .hc-ghost { background: #FFFFFF; color: #101828; border: 1px solid #D0D5DD; }
  .hc-ghost:hover { border-color: #98A2B3; color: #101828; }
  .hero-stats { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 24px;
    margin: 0; padding-top: 28px; border-top: 1px solid #EAECF0; }
  .hero-stats > div { display: flex; flex-direction: column; gap: 8px; }
  .hero-stats dt { display: flex; align-items: center; gap: 8px; font-size: 13.5px; color: #475467; }
  .hero-stats dd { margin: 0; font-family: 'IBM Plex Sans', sans-serif; font-size: 30px; font-weight: 700;
    letter-spacing: -0.03em; font-variant-numeric: tabular-nums; color: #101828; line-height: 1; }

  .map-h2 { margin: 0; font-size: 34px; font-weight: 700; letter-spacing: -0.03em; }
  .map-sub { margin: 0; font-size: 16px; line-height: 1.6; color: #475467; max-width: 640px; }


  .map-head { display: flex; align-items: flex-end; justify-content: space-between;
    gap: 24px; flex-wrap: wrap; margin-bottom: 30px; }
  .map-head .rk-pick select { min-width: 190px; max-width: 220px;
    text-overflow: ellipsis; }
  .map-picks { display: flex; align-items: flex-end; gap: 14px; flex-wrap: wrap; }


  /* ── บล็อกหัวหน้าสีเข้ม ── */
  .hero-dark { background: #101828; padding: 26px 0 30px; }
  .hd-inner { width: 1200px; margin: 0 auto; }
  .hd-top { display: flex; align-items: center; gap: 20px; margin-bottom: 26px; }

  /* ── แถบปุ่มบนขวา: ภาษา · Login · สมัครสมาชิก ── */
  .hd-actions { display: flex; align-items: center; gap: 10px; }
  .lang-sw { display: inline-flex; border: 1px solid #EAECF0; border-radius: 999px;
    padding: 2px; background: #FFFFFF; }
  .lang-sw button { font: inherit; font-size: 12.5px; font-weight: 600; color: #667085;
    background: transparent; border: 0; border-radius: 999px; padding: 5px 13px; cursor: pointer;
    transition: background .15s, color .15s; }
  .lang-sw button:hover { color: #101828; }
  .lang-sw button[aria-pressed="true"] { background: #101828; color: #FFFFFF; }
  .btn-ghost, .btn-solid { font: inherit; font-size: 14px; font-weight: 600; border-radius: 10px;
    padding: 9px 18px; cursor: pointer; white-space: nowrap;
    transition: background .15s, border-color .15s, color .15s; }
  .btn-ghost { color: #475467; background: transparent; border: 1px solid #EAECF0; }
  .btn-ghost:hover { border-color: #D0D5DD; color: #101828; }
  .btn-solid { color: #FFFFFF; background: #D92D20; border: 1px solid #D92D20; }
  .btn-solid:hover { background: #B42318; border-color: #B42318; }
  .lang-sw button:focus-visible, .btn-ghost:focus-visible, .btn-solid:focus-visible {
    outline: 2px solid #D92D20; outline-offset: 2px; }
  .hd-top .mh-nav { flex: 1; }
  .hd-pill { background: rgba(217,45,32,0.16); color: #FF9A92; border: 1px solid rgba(217,45,32,0.45);
    border-radius: 999px; padding: 5px 13px; font-size: 12.5px; font-weight: 600; white-space: nowrap; }
  .hd-h1 { margin: 0 0 12px; font-size: 46px; line-height: 1.1; font-weight: 700; letter-spacing: -0.035em;
    color: #FFFFFF; max-width: 20ch; text-wrap: balance; }
  .hd-sub { margin: 0 0 26px; font-size: 16.5px; line-height: 1.6; color: #C3C9D5; max-width: 74ch; }
  .hd-stats { display: flex; flex-wrap: wrap; gap: 12px 28px; margin: 18px 0 0; }
  .hd-stats > div { display: flex; align-items: center; gap: 8px; font-size: 14px; color: #C3C9D5; }
  .hd-stats .hd-fine { flex-basis: 100%; font-size: 11.5px; color: #98A2B3; margin-top: -2px; }
  .hd-stats b { color: #FFFFFF; font-family: 'IBM Plex Sans', sans-serif; font-weight: 700;
    font-variant-numeric: tabular-nums; }

  /* ── การ์ด 3 อันดับแรกรายหมวด ── */
  .pk-block + .pk-block { margin-top: 52px; }
  .pk-head { display: flex; align-items: center; justify-content: space-between; gap: 20px;
    flex-wrap: wrap; margin-bottom: 18px; }
  .pk-title { display: flex; align-items: center; gap: 14px; }
  .pk-titxt { display: flex; flex-direction: column; gap: 3px; }
  .pk-award { font-size: 20px; font-weight: 600; letter-spacing: -0.012em; color: #B42318; line-height: 1.3; }
  .pk-title h2 { margin: 0; font-size: 46px; line-height: 1.06; font-weight: 700;
    letter-spacing: 0.005em; color: #101828; }
  .pk-title .cnt { font-size: 13.5px; color: #667085; }
  .pk-live { display: inline-flex; align-items: center; gap: 7px; background: #F5F7FA; border: 1px solid #EAECF0;
    border-radius: 999px; padding: 5px 13px; font-size: 12.5px; color: #475467; }
  .pk-live i { width: 7px; height: 7px; border-radius: 50%; background: #067647; display: inline-block; }
  .pk-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; }
  .pk-card { border: 1px solid #EAECF0; border-radius: 14px; background: #FFFFFF; overflow: hidden;
    display: flex; flex-direction: column; transition: border-color .18s, box-shadow .18s, transform .18s; }
  .pk-card:hover { border-color: #D0D5DD; box-shadow: 0 14px 30px -16px rgba(16,24,40,0.22); transform: translateY(-2px); }
  .pk-card.first { border-color: #FECDCA; }
  .pk-rank { display: flex; align-items: center; justify-content: center; gap: 8px;
    padding: 11px 14px; background: #F5F7FA; border-bottom: 1px solid #EAECF0;
    font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #475467; }
  .pk-card.first .pk-rank { background: #FEF3F2; border-bottom-color: #FECDCA; color: #B42318; }
  .pk-body { padding: 20px 20px 0; display: flex; flex-direction: column; gap: 12px; }
  .pk-logo { width: 60px; height: 60px; border: 1px solid #EAECF0; border-radius: 12px;
    display: inline-flex; align-items: center; justify-content: center;
    font-family: 'IBM Plex Sans', sans-serif; font-size: 15px; font-weight: 700; color: #FFFFFF; }
  .pk-name { font-size: 20px; font-weight: 700; letter-spacing: -0.02em; color: #101828; }
  .pk-loc { display: flex; align-items: center; gap: 6px; font-size: 13px; color: #667085; margin-top: -6px; }
  .pk-score { display: flex; align-items: baseline; gap: 4px; font-family: 'IBM Plex Sans', sans-serif; }
  .pk-score b { font-size: 32px; font-weight: 700; letter-spacing: -0.035em; color: #D92D20; line-height: 1; }
  .pk-score span { font-size: 15px; font-weight: 600; color: #667085; }
  .pk-stars { display: flex; gap: 3px; }
  .pk-stars svg { width: 17px; height: 17px; fill: #D92D20; }
  .pk-bars { border-top: 1px solid #F0F2F5; margin-top: 4px; padding: 14px 0 2px;
    display: flex; flex-direction: column; gap: 11px; }
  .pk-bar .lb { display: flex; justify-content: space-between; font-size: 13px; color: #475467; margin-bottom: 5px; }
  .pk-bar .lb b { font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; color: #101828;
    font-variant-numeric: tabular-nums; }
  .pk-bar .track { height: 6px; border-radius: 999px; background: #F0F2F5; overflow: hidden; }
  .pk-bar .fill { height: 100%; border-radius: 999px; background: #D92D20; }
  .pk-cta { margin-top: auto; border-top: 1px solid #F0F2F5; padding: 14px; text-align: center; }
  .pk-cta a { font-size: 14px; font-weight: 600; color: #D92D20; text-decoration: none; }
  .pk-cta a:hover { text-decoration: underline; }

  .scroll-cue { display: flex; justify-content: center; margin-top: 34px; }
  .scroll-cue a { width: 38px; height: 38px; border-radius: 50%; border: 1px solid #EAECF0; background: #FFFFFF;
    display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 8px rgba(16,24,40,0.08);
    transition: border-color .15s, transform .15s; }
  .scroll-cue a:hover { border-color: #D0D5DD; transform: translateY(2px); }


  /* SCALE-DOWN-PICKS — ย่อสเกลการ์ด 3 อันดับ (ไม่แตะบล็อกหัวด้านบน) */
  .pk-block + .pk-block { margin-top: 38px; }
  .pk-head { margin-bottom: 14px; }
  .pk-title h2 { font-size: 46px; }
  .pk-title .cnt { font-size: 13px; }
  .pk-live { font-size: 11.5px; padding: 4px 11px; }
  .pk-grid { gap: 16px; }
  .pk-card { border-radius: 12px; }
  .pk-rank { padding: 8px 12px; font-size: 10.5px; letter-spacing: 0.07em; }
  .pk-body { padding: 16px 16px 0; gap: 9px; }
  .pk-logo { width: 44px; height: 44px; border-radius: 10px; font-size: 12.5px; }
  .pk-name { font-size: 17px; }
  .pk-loc { font-size: 12px; margin-top: -4px; }
  .pk-loc svg { width: 12px; height: 12px; }
  .pk-score b { font-size: 26px; }
  .pk-score span { font-size: 13px; }
  .pk-stars svg { width: 14px; height: 14px; }
  .pk-bars { margin-top: 2px; padding: 11px 0 2px; gap: 9px; }
  .pk-bar .lb { font-size: 12px; margin-bottom: 4px; }
  .pk-bar .track { height: 5px; }
  .pk-cta { padding: 11px; }
  .pk-cta a { font-size: 13px; }
  .scroll-cue { margin-top: 26px; }


  /* WHITE-HERO — บล็อกหัวกลับเป็นพื้นขาว ใช้โทนสีเดิมของเว็บ */
  .hero-dark { background: #FFFFFF !important; border-bottom: 1px solid #EAECF0; padding: 24px 0 34px !important; }
  .hero-dark .mh-brand { color: #101828 !important; }
  .hero-dark .mh-nav a { color: #475467 !important; }
  .hero-dark .mh-nav a:hover { color: #101828 !important; }
  .hero-dark .hd-pill { background: #FEF3F2 !important; color: #B42318 !important; border-color: #FECDCA !important; }
  .hero-dark .hd-h1 { color: #101828 !important; }
  .hero-dark .hd-sub { color: #475467 !important; }
  .hero-dark .mh-search { background: #F5F7FA !important; border-color: #EAECF0 !important; }
  .hero-dark .mh-search input { color: #101828 !important; }
  .hero-dark .mh-search input::placeholder { color: #667085 !important; }
  .hero-dark .mh-search svg { stroke: #667085 !important; }
  .hero-dark .hd-stats > div { color: #475467 !important; }
  .hero-dark .hd-stats b { color: #101828 !important; }
  .hero-dark .hd-stats svg { stroke: #667085 !important; }
  .hero-dark .hd-stats .hd-fine { color: #667085 !important; }

  /* ── ผังใหม่: 3 คอลัมน์ · #1 ใหญ่ · #2/#3 เล็กเรียงคู่ใต้ ── */
  .pk-wrap { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
  .pk-col { display: flex; flex-direction: column; gap: 12px; }
  .pk-col > h2 { margin: 0 0 2px; font-size: 17px; font-weight: 700; letter-spacing: -0.02em; color: #101828; }
  .pk-rest { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }

  /* การ์ดเล็ก (#2 / #3) */
  .pk-mini { border: 1px solid #EAECF0; border-radius: 12px; background: #FFFFFF; overflow: hidden;
    display: flex; flex-direction: column; transition: border-color .18s, box-shadow .18s, transform .18s; }
  .pk-mini:hover { border-color: #D0D5DD; box-shadow: 0 10px 22px -14px rgba(16,24,40,0.2); transform: translateY(-2px); }
  .pk-mini .pk-rank { padding: 6px 10px; font-size: 10px; }
  .pk-mini .mb { padding: 12px; display: flex; flex-direction: column; gap: 7px; }
  .pk-mini .pk-logo { width: 32px; height: 32px; border-radius: 8px; font-size: 10.5px; }
  .pk-mini .nm { font-size: 14px; font-weight: 600; letter-spacing: -0.015em; color: #101828; }
  .pk-mini .lo { font-size: 11.5px; color: #667085; }
  .pk-mini .sc { display: flex; align-items: baseline; gap: 3px; font-family: 'IBM Plex Sans', sans-serif; }
  .pk-mini .sc b { font-size: 20px; font-weight: 700; letter-spacing: -0.03em; color: #101828; line-height: 1; }
  .pk-mini .sc span { font-size: 11.5px; color: #667085; font-weight: 600; }
  .pk-mini .st { display: flex; gap: 2px; }
  .pk-mini .st svg { width: 11px; height: 11px; fill: #D92D20; }
  .pk-mini .go { margin-top: auto; border-top: 1px solid #F0F2F5; padding: 9px 12px; text-align: center; }
  .pk-mini .go a { font-size: 12px; font-weight: 600; color: #D92D20; text-decoration: none; }
  .pk-mini .go a:hover { text-decoration: underline; }


  /* ── ตัวเลือกขอบเขตของบล็อก 3 อันดับแรก ── */
  .pk-head { align-items: flex-end; }
  .pk-picks-ctl { display: flex; align-items: flex-end; gap: 12px; flex-wrap: wrap; }
  .pk-picks-ctl .rk-pick > span { font-size: 11px; }
  .pk-picks-ctl .rk-pick select { min-width: 168px; padding: 9px 38px 9px 13px; font-size: 13.5px; }
  .pk-empty { border: 1px dashed #D0D5DD; border-radius: 12px; background: #FCFCFD;
    padding: 34px 20px; text-align: center; font-size: 13.5px; color: #667085; line-height: 1.6; }


  /* PREMIUM-GOLD — การ์ดอันดับ 1 กรอบทอง ดาวเด่นกว่าคะแนน */
  .pk-card.first {
    border: 1.5px solid #C9A227 !important;
    box-shadow: 0 0 0 3px #FBF3DF, 0 12px 28px -18px rgba(122,99,41,0.4);
  }
  .pk-card.first:hover {
    border-color: #B8912F !important;
    box-shadow: 0 0 0 3px #F7EBCD, 0 18px 34px -18px rgba(122,99,41,0.5);
  }
  .pk-card.first .pk-rank {
    background: #FBF3DF !important; border-bottom-color: #EFDFB4 !important; color: #7A6329 !important;
    letter-spacing: 0.1em;
  }
  .pk-card.first .pk-logo { border-color: #EFDFB4; }

  /* ── ลายดาวจางพื้นหลังการ์ด — ขึ้นเฉพาะการ์ดที่ได้ดาวตั้งแต่ 1 ดวงขึ้นไป ── */
  .pk-card[data-stars]:not([data-stars="0"]),
  .pk-mini[data-stars]:not([data-stars="0"]),
  .rv-card[data-stars]:not([data-stars="0"]) {
    background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20260'%3E%3Cg%20transform='translate(236%2020)%20scale(2.45)'%3E%3Cpath%20d='M32%208L38%2023.75L54.82%2024.58L41.7%2035.15L46.11%2051.42L32%2042.2L17.89%2051.42L22.3%2035.15L9.18%2024.58L26%2023.75Z'%20fill='%23D92D20'%20fill-opacity='0.055'/%3E%3C/g%3E%3Cpath%20d='M-24%20188%20C58%20156%20128%20214%20214%20178%20S352%20138%20424%20160M-24%20199%20C58%20167%20128%20225%20214%20189%20S352%20149%20424%20171M-24%20210%20C58%20178%20128%20236%20214%20200%20S352%20160%20424%20182M-24%20221%20C58%20189%20128%20247%20214%20211%20S352%20171%20424%20193M-24%20232%20C58%20200%20128%20258%20214%20222%20S352%20182%20424%20204M-24%20243%20C58%20211%20128%20269%20214%20233%20S352%20193%20424%20215M-24%20254%20C58%20222%20128%20280%20214%20244%20S352%20204%20424%20226'%20fill='none'%20stroke='%23D92D20'%20stroke-opacity='0.11'%20stroke-width='1'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center right;
  }

  /* ดาวเป็นพระเอก คะแนนรองลงมา */
  .pk-stars { gap: 5px !important; margin-top: 2px; }
  .pk-stars svg { width: 27px !important; height: 27px !important; fill: #D92D20 !important; }
  .pk-score { align-items: baseline; gap: 5px; }
  .pk-score b { font-size: 19px !important; color: #101828 !important; }
  .pk-score span { font-size: 12.5px !important; color: #667085 !important; }
  .pk-scorelbl { font-size: 11.5px; color: #667085; letter-spacing: 0.03em; }

  .pk-mini .st { gap: 3px; }
  .pk-mini .st svg { width: 15px !important; height: 15px !important; }
  .pk-mini .sc b { font-size: 16px !important; }
  .pk-mini .sc span { font-size: 11px !important; }


  /* GOLD-BOLD — แถบอันดับทองเข้ม · ดาวใหญ่ขึ้น มีขอบทอง */
  .pk-card.first .pk-rank {
    background: #7A6329 !important; border-bottom: 1px solid #5F4C1F !important;
    color: #FDF6E3 !important; font-weight: 700; letter-spacing: 0.12em;
  }
  .pk-card.first { box-shadow: 0 0 0 3px #F3E6C4, 0 14px 30px -18px rgba(95,76,31,0.45) !important; }
  .pk-card.first:hover { box-shadow: 0 0 0 3px #EBDBAE, 0 20px 36px -18px rgba(95,76,31,0.55) !important; }

  .pk-stars svg { width: 34px !important; height: 34px !important; overflow: visible; }
  .pk-mini .st svg { width: 18px !important; height: 18px !important; overflow: visible; }
  .pk-stars { gap: 6px !important; }
  .pk-mini .st { gap: 4px !important; }


  /* GOLD-CTA — ปุ่มรีวิวของการ์ดอันดับ 1 เป็นปุ่มทองเต็มใบ */
  .pk-card.first .pk-cta { padding: 12px; border-top-color: #EFDFB4; }
  .pk-card.first .pk-cta a {
    display: block; background: #7A6329; color: #FDF6E3 !important; border-radius: 8px;
    padding: 10px 14px; font-size: 13.5px; font-weight: 700; letter-spacing: 0.03em;
    text-decoration: none; transition: background .16s;
  }
  .pk-card.first .pk-cta a:hover { background: #5F4C1F; text-decoration: none; }
  .pk-card.first .pk-cta a:focus-visible { outline: 2px solid #C9A227; outline-offset: 2px; }


  /* MINI-CAT-BAR — ดาวอันดับ 1 ใหญ่ขึ้น · การ์ดเล็กแสดงชื่อหมวดแทนเลขอันดับ */
  .pk-stars svg { width: 44px !important; height: 44px !important; }
  .pk-stars { gap: 7px !important; margin: 4px 0 2px; }
  .pk-mini .pk-rank { letter-spacing: 0.1em; font-weight: 700; }


  /* ── ดาวโลโก้: แดง กรอบทอง แกนขาว มีเงา ── */
  .brand-star { overflow: visible; }
  .mh-brand { gap: 12px !important; font-size: 21px !important; }


  /* ── การ์ดแผนที่: ขึ้นเมื่อกดหมุดเท่านั้น ── */
  #card-search { margin-top: 16px; }
  .card-close {
    position: absolute; top: 12px; right: 12px; z-index: 4;
    width: 30px; height: 30px; border-radius: 50%; border: 1px solid #EAECF0; background: #FFFFFF;
    color: #667085; font: inherit; font-size: 19px; line-height: 1; cursor: pointer;
    display: flex; align-items: center; justify-content: center; transition: border-color .15s, color .15s;
  }
  .card-close:hover { border-color: #D0D5DD; color: #101828; }
  .card-close:focus-visible { outline: 2px solid #D92D20; outline-offset: 2px; }
  .map-hint {
    position: absolute; left: 50%; bottom: 14px; transform: translateX(-50%); z-index: 3;
    background: rgba(255,255,255,0.94); border: 1px solid #EAECF0; border-radius: 999px;
    padding: 7px 16px; font-size: 12.5px; color: #475467; white-space: nowrap;
    box-shadow: 0 4px 12px rgba(16,24,40,0.08); pointer-events: none;
  }


  /* ── ช่องค้นหาในแถบควบคุมตาราง ── */
  .rk-qbox { display: flex; align-items: center; gap: 9px; background: #FFFFFF;
    border: 1px solid #EAECF0; border-radius: 10px; padding: 0 14px; height: 43px; min-width: 218px; }
  .rk-qbox:focus-within { border-color: #D92D20; box-shadow: 0 0 0 3px #FEF3F2; }
  .rk-qbox input { flex: 1; font: inherit; font-size: 14.5px; color: #101828;
    background: transparent; border: 0; outline: none; min-width: 0; }
  .rk-qbox input::placeholder { color: #667085; }

  /* ── โลโก้: เงาเฉพาะด้านข้าง ── */
  .brand-star { filter: none !important; }


  /* ── การ์ดผู้ที่อันดับดีขึ้น / แย่ลง ข้างแผนที่ ── */
  #movers { position: absolute; right: 0; top: 0; width: 360px;
    display: flex; flex-direction: column; gap: 16px; }
  .mv-card { border: 1px solid #EAECF0; border-radius: 14px; background: #FFFFFF; overflow: hidden; }
  .mv-head { display: flex; align-items: center; gap: 9px; padding: 10px 14px;
    border-bottom: 1px solid #F0F2F5; font-size: 13.5px; font-weight: 700; letter-spacing: -0.01em; }
  .mv-card.up .mv-head { background: #F0FBF5; color: #067647; border-bottom-color: #CFEBDC; }
  .mv-card.down .mv-head { background: #FEF6EE; color: #B54708; border-bottom-color: #F5DFC4; }
  .mv-head .n { margin-left: auto; font-family: 'IBM Plex Sans', sans-serif; font-size: 12px; opacity: .8; }
  .mv-row { display: flex; align-items: center; gap: 10px; padding: 7px 14px; border-bottom: 1px solid #F5F7FA; }
  .mv-row:last-child { border-bottom: 0; }
  .mv-logo { width: 28px; height: 28px; border-radius: 7px; flex-shrink: 0;
    display: inline-flex; align-items: center; justify-content: center;
    font-family: 'IBM Plex Sans', sans-serif; font-size: 10px; font-weight: 700; color: #FFFFFF; }
  .mv-name { display: block; font-size: 13px; font-weight: 600; color: #101828; line-height: 1.3; }
  .mv-loc { display: block; font-size: 11px; color: #667085; line-height: 1.35; }
  .mv-delta { margin-left: auto; text-align: right; font-family: 'IBM Plex Sans', sans-serif; }
  .mv-delta b { display: block; font-size: 14.5px; font-weight: 700; font-variant-numeric: tabular-nums; }
  .mv-card.up .mv-delta b { color: #067647; }
  .mv-card.down .mv-delta b { color: #B54708; }
  .mv-delta span { font-size: 11px; color: #667085; font-variant-numeric: tabular-nums; }
  .mv-empty { padding: 22px 16px; font-size: 12.5px; color: #667085; line-height: 1.6; text-align: center; }
  .mv-note { font-size: 11.5px; color: #667085; line-height: 1.55; padding: 0 2px; }

  /* ── สถานะกดได้ ── */
  [data-pin] { cursor: pointer; transition: opacity .2s; }
  [data-pin] > div:first-child, [data-pin] > div:nth-child(2) { transition: border-color .15s, box-shadow .15s; }
  [data-region] { cursor: pointer; transition: border-color .15s, background .15s, color .15s; }
  [data-region]:hover { border-color: #D0D5DD; }
  [data-hof] { cursor: pointer; transition: border-color .18s, box-shadow .18s, transform .18s; }
  [data-hof]:hover { border-color: #D0D5DD; box-shadow: 0 12px 28px -14px rgba(16,24,40,0.22); transform: translateY(-2px); }
  .cta { cursor: pointer; transition: background .15s; }
  .cta:hover { background: #B42318 !important; }
  .pinlbl { font-size: 13px; font-weight: 600; color: #101828; white-space: nowrap; }
  #card { transition: box-shadow .2s; }
  [data-pin]:focus-visible, [data-region]:focus-visible, [data-hof]:focus-visible {
    outline: 2px solid #D92D20; outline-offset: 3px;
  }
</style>"""

PAGE = """<div class="stage">
  <div class="bar">
    <span class="lbl">Frame &middot; <b>Homepage &mdash; Desktop 1440</b></span>
    <div class="zoom" role="group" aria-label="ระดับการซูม">
      <button type="button" data-z="fit" aria-pressed="true">Fit</button>
      <button type="button" data-z="1" aria-pressed="false">100%</button>
    </div>
  </div>
  <div class="viewport" id="vp">
    <div class="frame" id="frame">
""" + body + """
    </div>
  </div>
</div>
<script>
  var frame = document.getElementById('frame');
  var vp = document.getElementById('vp');
  var mode = 'fit';
  function apply() {
    var avail = vp.clientWidth || document.documentElement.clientWidth || 1440;
    frame.style.transform = 'none';
    var h = frame.offsetHeight;
    var s = mode === 'fit' ? Math.max(0.2, Math.min(1, (avail - 2) / 1440)) : 1;
    frame.style.transform = 'scale(' + s + ')';
    vp.style.height = Math.ceil(h * s) + 'px';
    frame.style.marginLeft = s < 1 ? Math.max(0, (avail - 1440 * s) / 2) + 'px' : 'auto';
  }
  document.querySelectorAll('[data-z]').forEach(function (b) {
    b.addEventListener('click', function () {
      mode = b.dataset.z;
      document.querySelectorAll('[data-z]').forEach(function (o) {
        o.setAttribute('aria-pressed', String(o === b));
      });
      apply();
    });
  });
  window.addEventListener('resize', apply);
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(apply); }
  apply();
</script>

<script>
/* ── ข้อมูลสมมติทั้งหมด ใส่ไว้เพื่อทดสอบการกดใช้งานเท่านั้น ── */
/* ── ข้อมูลการ์ดบนแผนที่ ─────────────────────────
   ไม่ได้พิมพ์ค่าไว้ตายตัวอีกต่อไป แต่คำนวณจาก rkRows() ซึ่งเป็นเครื่องคำนวณ
   ตัวเดียวกับตารางอันดับด้านล่าง — เลือกหมวดไหน การ์ดกับตารางจึงตรงกันเสมอ
   คีย์ของ B เป็น "รหัสโบรก@รหัสประเทศ" เพราะโบรกรายเดียว
   เป็นอันดับหนึ่งได้หลายประเทศพร้อมกัน                                       */
var B = {};
var TOP = {};
var CNAME = {AU:"Australia", CY:"Cyprus", GB:"United Kingdom", SG:"Singapore", US:"USA", AE:"UAE", ZA:"South Africa"};
var REGION = {all:["US","GB","CY","AE","SG","ZA","AU"], eu:["GB","CY"], apac:["AU","SG"],
              me:["AE"], af:["ZA"], na:["US"], sa:[]};
var ISO_ALL = ["US","GB","CY","AE","SG","ZA","AU"];
var mapYear = 2026;
var STAR_D = "M12 2.6l2.7 6.1 6.6.7-4.9 4.4 1.4 6.5L12 16.9 6.2 20.3l1.4-6.5L2.7 9.4l6.6-.7z";
var cur = null, region = "all", mapCat = "fx";
/* คำกำกับจำนวนดาว — ดาวคือผ่าน/ไม่ผ่าน ไม่ใช่คะแนนเปรียบเทียบ */
var STAR_SUB = {3:"ระดับสูงสุด · ผ่านครบทุกข้อของระดับ 3 ดาว",
                2:"ผ่านครบทุกข้อของระดับ 2 ดาว",
                1:"ผ่านเกณฑ์บังคับครบทุกข้อในรอบล่าสุด"};
/* ชื่อหมวดแบบสั้น ใช้บนดรอปดาวน์แผนที่และการ์ด — ชื่อเต็มอยู่ที่ตารางอันดับ */
var CAT_SHORT = {fx:"Forex / CFD", futures:"ฟิวเจอร์ส", stocks:"หุ้น",
                 crypto:"คริปโต (CFD)", exchange:"Exchange", fund:"กองทุน"};
function catShort(k){ return CAT_SHORT[k] || CATS[k].n; }
function isoOpen(iso){ return !!TOP[iso]; }
function mapIsos(){ return (REGION[region] || []).filter(isoOpen); }
function buildMapData(){
  B = {}; TOP = {};
  if (typeof rkRows !== "function" || typeof CATS === "undefined" || typeof META === "undefined") { return; }
  ISO_ALL.forEach(function(iso){
    rkRows(mapCat, iso, mapYear).slice(0, 2).forEach(function(r, i){
      var m = META[r.id], key = r.id + "@" + iso;
      if (i === 0) { TOP[iso] = key; }
      B[key] = {id:r.id, n:m.n, mono:m.mono, iso:iso, c:CNAME[iso], reg:m.reg,
                stars:r.stars, score:r.total.toFixed(1), rank:"#" + (i + 1),
                rankTxt:"อันดับ " + (i + 1) + " ของ " + CNAME[iso] + " · " + catShort(mapCat),
                sub:STAR_SUB[r.stars] || STAR_SUB[1]};
    });
  });
}
function buildMapCatSelect(){
  var sel = document.getElementById("mapcat-sel");
  if (!sel || typeof CAT_ORDER === "undefined") { return; }
  sel.innerHTML = CAT_ORDER.map(function(k){
    var n = ISO_ALL.filter(function(iso){ return rkRows(k, iso, mapYear).length; }).length;
    return '<option value="' + k + '"' + (k === mapCat ? " selected" : "") + (n ? "" : " disabled") + '>' +
      catShort(k) + (n ? " (" + n + " ประเทศ)" : " — ยังไม่เปิดตรวจ") + '</option>';
  }).join("");
}
function buildMapYearSelect(){
  var sel = document.getElementById("mapyear-sel");
  if (!sel || typeof YEARS3 === "undefined") { return; }
  sel.innerHTML = YEARS3.slice().reverse().map(function(y){
    return '<option value="' + y + '"' + (y === mapYear ? " selected" : "") + '>' + y + '</option>';
  }).join("");
}
function setMapYear(y){
  var wasOpen = cardOpen, prevIso = B[cur] ? B[cur].iso : null;
  mapYear = y;
  buildMapData();
  buildMapCatSelect();
  buildMapYearSelect();
  setRegion(region);
  var list = mapIsos();
  if (!list.length) { return; }
  var iso = (prevIso && list.indexOf(prevIso) >= 0) ? prevIso : list[0];
  select(TOP[iso]);
  if (!wasOpen) { closeCard(); }
}
function setMapCat(c){
  var wasOpen = cardOpen, prevIso = B[cur] ? B[cur].iso : null;
  mapCat = c;
  buildMapData();
  buildMapCatSelect();
  buildMapYearSelect();
  setRegion(region);
  var list = mapIsos();
  if (!list.length) { return; }
  var iso = (prevIso && list.indexOf(prevIso) >= 0) ? prevIso : list[0];
  select(TOP[iso]);
  if (!wasOpen) { closeCard(); }
}

/* \u2500\u2500 \u0e14\u0e32\u0e27\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25 RedStar \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
   \u0e14\u0e32\u0e27\u0e14\u0e27\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e17\u0e31\u0e49\u0e07\u0e42\u0e25\u0e42\u0e01\u0e49\u0e40\u0e27\u0e47\u0e1a\u0e41\u0e25\u0e30\u0e14\u0e32\u0e27\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49\u0e43\u0e2b\u0e49\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25
   \u0e02\u0e19\u0e32\u0e14\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 15px \u0e15\u0e31\u0e14\u0e40\u0e2b\u0e25\u0e35\u0e48\u0e22\u0e21\u0e43\u0e19\u0e2d\u0e2d\u0e01 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e21\u0e2d\u0e07\u0e44\u0e21\u0e48\u0e40\u0e2b\u0e47\u0e19\u0e41\u0e25\u0e30\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e14\u0e39\u0e40\u0e25\u0e2d\u0e30       */
/* \u2500\u2500 \u0e41\u0e16\u0e1a\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e20\u0e31\u0e22\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
   \u0e0a\u0e37\u0e48\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e43\u0e19\u0e41\u0e16\u0e1a\u0e19\u0e35\u0e49 \u0e15\u0e31\u0e49\u0e07\u0e02\u0e36\u0e49\u0e19\u0e40\u0e2d\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e17\u0e35\u0e48\u0e21\u0e35\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e23\u0e34\u0e07
   \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e01\u0e32\u0e23\u0e0a\u0e35\u0e49\u0e27\u0e48\u0e32\u0e42\u0e1a\u0e23\u0e01\u0e23\u0e32\u0e22\u0e43\u0e14\u0e40\u0e16\u0e37\u0e48\u0e2d\u0e19 \u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35\u0e40\u0e2d\u0e01\u0e2a\u0e32\u0e23\u0e08\u0e32\u0e01\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e08\u0e23\u0e34\u0e07\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19          */
var ALERTS = [
  ["hi", "Apex Global FX", "\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15\u0e43\u0e19\u0e40\u0e02\u0e15\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e34\u0e14\u0e43\u0e2b\u0e49\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23", "14 \u0e21\u0e34.\u0e22. 2026"],
  ["hi", "Nova Prime Markets", "\u0e16\u0e39\u0e01\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e40\u0e1e\u0e34\u0e01\u0e16\u0e2d\u0e19\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15", "9 \u0e21\u0e34.\u0e22. 2026"],
  ["hi", "Sterling Wave Capital", "\u0e1e\u0e1a\u0e01\u0e32\u0e23\u0e1b\u0e0f\u0e34\u0e40\u0e2a\u0e18\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e16\u0e2d\u0e19\u0e40\u0e07\u0e34\u0e19\u0e0b\u0e49\u0e33\u0e2b\u0e25\u0e32\u0e22\u0e23\u0e32\u0e22", "6 \u0e21\u0e34.\u0e22. 2026"],
  ["md", "Orion Trade Group", "\u0e43\u0e0a\u0e49\u0e0a\u0e37\u0e48\u0e2d\u0e41\u0e25\u0e30\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e27\u0e47\u0e1a\u0e04\u0e25\u0e49\u0e32\u0e22\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e21\u0e35\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15", "2 \u0e21\u0e34.\u0e22. 2026"],
  ["hi", "Zen Peak Securities", "\u0e42\u0e06\u0e29\u0e13\u0e32\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19 \u0e1c\u0e34\u0e14\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e01\u0e32\u0e23\u0e01\u0e33\u0e01\u0e31\u0e1a", "30 \u0e1e.\u0e04. 2026"],
  ["md", "Halcyon FX Ltd", "\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e14\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e15\u0e32\u0e21\u0e17\u0e35\u0e48\u0e41\u0e08\u0e49\u0e07\u0e44\u0e27\u0e49", "27 \u0e1e.\u0e04. 2026"],
  ["md", "Vertex Bridge Markets", "\u0e22\u0e49\u0e32\u0e22\u0e40\u0e02\u0e15\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e01\u0e33\u0e01\u0e31\u0e1a 3 \u0e04\u0e23\u0e31\u0e49\u0e07\u0e43\u0e19 12 \u0e40\u0e14\u0e37\u0e2d\u0e19", "21 \u0e1e.\u0e04. 2026"],
  ["hi", "Crown Ridge Trading", "\u0e16\u0e39\u0e01\u0e02\u0e36\u0e49\u0e19\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e42\u0e14\u0e22\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e15\u0e48\u0e32\u0e07\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28", "18 \u0e1e.\u0e04. 2026"]
];
(function(){
  var track = document.getElementById("tkr-track");
  var box = document.getElementById("tkr-scroll");
  var btn = document.getElementById("tkr-pause");
  if (!track || !box) { return; }
  var one = ALERTS.map(function(a){
    return '<span class="tkr-item"><i class="tkr-dot ' + a[0] + '"></i>' +
      '<b>' + a[1] + '</b><span>' + a[2] + '</span><em>' + a[3] + '</em></span>';
  }).join("") +
  '<span class="tkr-sample"><i>\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07</i>' +
  '\u0e0a\u0e37\u0e48\u0e2d\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e43\u0e19\u0e41\u0e16\u0e1a\u0e19\u0e35\u0e49\u0e15\u0e31\u0e49\u0e07\u0e02\u0e36\u0e49\u0e19\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e17\u0e35\u0e48\u0e21\u0e35\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e23\u0e34\u0e07</span>';
  track.innerHTML = one + one;   /* \u0e2a\u0e2d\u0e07\u0e0a\u0e38\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e43\u0e2b\u0e49\u0e27\u0e19\u0e01\u0e25\u0e31\u0e1a\u0e44\u0e14\u0e49\u0e44\u0e21\u0e48\u0e2a\u0e30\u0e14\u0e38\u0e14 */

  var hover = false, held = false, off = false, last = 0, drag = null;
  function paused(){ return hover || held || off; }
  box.addEventListener("pointerenter", function(){ hover = true; });
  box.addEventListener("pointerleave", function(){ hover = false; });
  box.addEventListener("focusin", function(){ held = true; });
  box.addEventListener("focusout", function(){ held = false; });
  /* \u0e25\u0e32\u0e01\u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19\u0e40\u0e2d\u0e07\u0e44\u0e14\u0e49 */
  box.addEventListener("pointerdown", function(e){
    drag = {x: e.clientX, s: box.scrollLeft};
    try { box.setPointerCapture(e.pointerId); } catch (err) {}
  });
  box.addEventListener("pointermove", function(e){
    if (!drag) { return; }
    box.scrollLeft = drag.s - (e.clientX - drag.x);
  });
  ["pointerup", "pointercancel"].forEach(function(t){
    box.addEventListener(t, function(){ drag = null; });
  });
  /* \u0e25\u0e49\u0e2d\u0e40\u0e21\u0e32\u0e2a\u0e4c\u0e41\u0e19\u0e27\u0e15\u0e31\u0e49\u0e07\u0e43\u0e2b\u0e49\u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19\u0e41\u0e19\u0e27\u0e19\u0e2d\u0e19 */
  box.addEventListener("wheel", function(e){
    if (Math.abs(e.deltaY) <= Math.abs(e.deltaX)) { return; }
    e.preventDefault(); box.scrollLeft += e.deltaY;
  }, {passive: false});
  if (btn) {
    btn.addEventListener("click", function(){
      off = !off;
      btn.setAttribute("aria-pressed", String(off));
      btn.innerHTML = off
        ? '<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">' +
          '<path d="M8 5.2l11 6.8-11 6.8z"></path></svg>'
        : '<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">' +
          '<rect x="7" y="5" width="3.6" height="14" rx="1"></rect>' +
          '<rect x="13.4" y="5" width="3.6" height="14" rx="1"></rect></svg>';
      btn.setAttribute("aria-label", off ? "\u0e40\u0e25\u0e48\u0e19\u0e01\u0e32\u0e23\u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34"
                                        : "\u0e2b\u0e22\u0e38\u0e14\u0e01\u0e32\u0e23\u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34");
    });
  }
  function step(t){
    if (!last) { last = t; }
    var dt = Math.min(80, t - last); last = t;
    if (!paused() && !drag) { box.scrollLeft += dt * 0.05; }
    var half = track.scrollWidth / 2;
    if (half > 0) {
      if (box.scrollLeft >= half) { box.scrollLeft -= half; }
      else if (box.scrollLeft < 0) { box.scrollLeft += half; }
    }
    requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
})();

var AW_D = "M32 8L38 23.75L54.82 24.58L41.7 35.15L46.11 51.42L32 42.2L17.89 51.42L22.3 35.15L9.18 24.58L26 23.75Z";
var AW_FACET =
      '<path d="M32 32L26 23.75L32 8Z" fill="#F8B4AD"></path>' +
      '<path d="M32 32L32 8L38 23.75Z" fill="#F08A81"></path>' +
      '<path d="M32 32L38 23.75L54.82 24.58Z" fill="#E8483E"></path>' +
      '<path d="M32 32L54.82 24.58L41.7 35.15Z" fill="#B42318"></path>' +
      '<path d="M32 32L41.7 35.15L46.11 51.42Z" fill="#E8483E"></path>' +
      '<path d="M32 32L46.11 51.42L32 42.2Z" fill="#B42318"></path>' +
      '<path d="M32 32L32 42.2L17.89 51.42Z" fill="#E8483E"></path>' +
      '<path d="M32 32L17.89 51.42L22.3 35.15Z" fill="#B42318"></path>' +
      '<path d="M32 32L22.3 35.15L9.18 24.58Z" fill="#E8483E"></path>' +
      '<path d="M32 32L9.18 24.58L26 23.75Z" fill="#B42318"></path>';
function awardStar(size){
  var s = +size || 16;
  /* \u0e14\u0e32\u0e27\u0e14\u0e27\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e17\u0e38\u0e01\u0e08\u0e38\u0e14 \u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e41\u0e04\u0e48\u0e02\u0e19\u0e32\u0e14
     \u0e02\u0e2d\u0e1a\u0e1a\u0e32\u0e07\u0e25\u0e07\u0e15\u0e32\u0e21\u0e02\u0e19\u0e32\u0e14 \u0e41\u0e25\u0e30\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 11px \u0e08\u0e36\u0e07\u0e15\u0e31\u0e14\u0e40\u0e2b\u0e25\u0e35\u0e48\u0e22\u0e21\u0e43\u0e19\u0e2d\u0e2d\u0e01 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e08\u0e30\u0e01\u0e25\u0e32\u0e22\u0e40\u0e1b\u0e47\u0e19\u0e08\u0e38\u0e14\u0e21\u0e31\u0e27 */
  var big = s >= 11, w = s >= 30 ? "2.4" : (s >= 15 ? "2.8" : "3.4");
  return '<svg width="' + s + '" height="' + s + '" viewBox="0 0 64 64" fill="none" aria-hidden="true">' +
    '<path d="' + AW_D + '" fill="#D92D20" stroke="#A81E14" stroke-width="' + w +
    '" stroke-linejoin="round" paint-order="stroke"></path>' +
    (big ? AW_FACET + '<path d="' + AW_D + '" fill="none" stroke="#A81E14" stroke-width="1.6" ' +
      'stroke-linejoin="round"></path>' : '') + '</svg>';
}
function starHTML(n, size) {
  var h = "";
  for (var i = 0; i < n; i++) { h += awardStar(size); }
  return h;
}
function chipOf(pin) {
  var kids = Array.prototype.slice.call(pin.children);
  for (var i = 0; i < kids.length; i++) { if (kids[i].offsetWidth > 20) return kids[i]; }
  return kids[0];
}
function pointerOf(pin) {
  var kids = Array.prototype.slice.call(pin.children);
  for (var i = 0; i < kids.length; i++) { if (kids[i].offsetWidth <= 20) return kids[i]; }
  return null;
}
function initPins() {
  document.querySelectorAll('[data-pin]').forEach(function (pin) {
    pin.setAttribute('role', 'button');
    pin.setAttribute('tabindex', '0');
    pin.setAttribute('aria-label', 'ดูโบรกเกอร์อันดับหนึ่งของ ' + CNAME[pin.dataset.pin]);
    var chip = chipOf(pin);
    var lbl = chip.querySelector('span');
    if (!lbl) {
      lbl = document.createElement('span');
      lbl.textContent = CNAME[pin.dataset.pin];
      chip.appendChild(lbl);
    }
    lbl.className = 'pinlbl';
    lbl.style.display = 'none';
  });
}
function paintPins() {
  var iso = B[cur] ? B[cur].iso : null;
  document.querySelectorAll('[data-pin]').forEach(function (pin) {
    var on = pin.dataset.pin === iso;
    var chip = chipOf(pin), ptr = pointerOf(pin), lbl = chip.querySelector('.pinlbl');
    chip.style.border = on ? '1.5px solid #D92D20' : '1px solid #EAECF0';
    chip.style.boxShadow = on ? '0 8px 20px rgba(217,45,32,0.20)' : '0 6px 16px rgba(16,24,40,0.12)';
    chip.style.paddingRight = on ? '12px' : '8px';
    if (lbl) { lbl.style.display = on ? 'inline' : 'none'; }
    if (ptr) {
      var col = on ? '1.5px solid #D92D20' : '1px solid #EAECF0';
      var flipped = pin.hasAttribute('data-flip');
      ptr.style.borderRight = flipped ? '' : col;
      ptr.style.borderBottom = flipped ? '' : col;
      ptr.style.borderLeft = flipped ? col : '';
      ptr.style.borderTop = flipped ? col : '';
    }
  });
  if (window.__mapApply) { window.__mapApply(); }
  document.querySelectorAll('[data-hof]').forEach(function (c) {
    var on = c.dataset.hof === cur;
    c.style.border = on ? '1.5px solid #D92D20' : '1px solid #EAECF0';
  });
}
function select(id) {
  var b = B[id];
  if (!b) { return; }
  cur = id;
  document.getElementById('card-mono').textContent = b.mono;
  document.getElementById('card-name').textContent = b.n;
  document.getElementById('card-country').textContent = b.c;
  document.getElementById('card-reg').textContent = b.reg;
  document.getElementById('card-score').textContent = b.score;
  document.getElementById('card-rank').textContent = b.rank;
  document.getElementById('card-ranktxt').textContent = b.rankTxt;
  document.getElementById('card-startxt').textContent = b.stars + ' ดาว RedStar';
  document.getElementById('card-sub').textContent = b.sub;
  document.getElementById('card-stars').innerHTML = starHTML(b.stars, 24);
  document.getElementById('card-emblem').innerHTML = starHTML(b.stars, 9);
  var srcFlag = document.querySelector('[data-pin="' + b.iso + '"] svg[aria-label]');
  var slot = document.getElementById('card-cty').querySelector('svg');
  if (srcFlag && slot) {
    var clone = srcFlag.cloneNode(true);
    clone.setAttribute('width', '18');
    clone.setAttribute('height', '12');
    clone.removeAttribute('aria-label');
    clone.setAttribute('aria-hidden', 'true');
    clone.style.borderRadius = '2px';
    slot.parentNode.replaceChild(clone, slot);
  }
  var tile=document.getElementById('card-logo');
  if(tile){tile.setAttribute('data-logo',(LOGO_SLUG[b.id]||b.id)+'|'+b.mono);tile.removeAttribute('data-logo-slug');}
  paintLogos();
  openCard();
  paintPins();
}
var cardOpen = false;
function openCard(){
  cardOpen = true;
  var c = document.getElementById("card"); if (c) { c.hidden = false; }
  var h = document.getElementById("map-hint"); if (h) { h.hidden = true; }
}
function closeCard(){
  cardOpen = false;
  var c = document.getElementById("card"); if (c) { c.hidden = true; }
  var h = document.getElementById("map-hint"); if (h) { h.hidden = false; }
  hsQ = ""; hsType = "all";
  var q = document.getElementById("hs-q"); if (q) { q.value = ""; }
  if (typeof HS_TYPES !== "undefined" && typeof hsRender === "function") { hsRender(); }
}
function showEmpty(on) {
  if (on && !cardOpen) { return; }
  var e = document.getElementById('card-empty');
  if (!e) { return; }
  if (on) {
    var t = e.querySelector('.ce-t'), s = e.querySelector('.ce-s');
    var regionOpen = (REGION[region] || []).length > 0;
    if (t && s && regionOpen && typeof CATS !== "undefined") {
      t.textContent = 'ยังไม่เปิดตรวจหมวดนี้ในภูมิภาคนี้';
      s.textContent = 'หมวด' + CATS[mapCat].n + ' ยังไม่มีรายชื่อในขอบเขตที่เลือก — เราจะไม่ประกาศอันดับของขอบเขตที่ยังไม่ได้เข้าไปตรวจด้วยตัวเอง';
    } else if (t && s) {
      t.textContent = 'ยังไม่เปิดตรวจในภูมิภาคนี้';
      s.textContent = 'เราจะไม่ประกาศอันดับของภูมิภาคที่ยังไม่ได้เข้าไปตรวจด้วยตัวเอง';
    }
  }
  e.style.display = on ? 'flex' : 'none';
}
var REGION_NAME = {all:"ทั้งหมด", eu:"Europe", apac:"Asia Pacific", me:"Middle East",
                   af:"Africa", na:"North America", sa:"South America"};
function buildRegionSelect(){
  var sel = document.getElementById("region-sel");
  if (!sel) { return; }
  sel.innerHTML = ["all","eu","apac","me","af","na","sa"].map(function(k){
    var all = (REGION[k] || []).length, n = (REGION[k] || []).filter(isoOpen).length;
    return '<option value="' + k + '"' + (k === region ? " selected" : "") + (n ? "" : " disabled") + '>' +
      REGION_NAME[k] + (n ? " (" + n + " ประเทศ)" : (all ? " — ยังไม่มีในหมวดนี้" : " — ยังไม่เปิดตรวจ")) + '</option>';
  }).join("");
}
function setRegion(r) {
  region = r;
  buildRegionSelect();
  var list = mapIsos();
  document.querySelectorAll('[data-pin]').forEach(function (pin) {
    var on = list.indexOf(pin.dataset.pin) >= 0;
    pin.style.opacity = on ? '1' : '0.2';
    pin.style.pointerEvents = on ? 'auto' : 'none';
  });
  if (!list.length) { showEmpty(true); return; }
  showEmpty(false);
  if (typeof renderMovers === "function") { renderMovers(); }
  if (!B[cur] || list.indexOf(B[cur].iso) < 0) {
    var wasOpen = cardOpen;
    select(TOP[list[0]]);
    if (!wasOpen) { closeCard(); }
  }
}
function buildEmpty() {
  var card = document.getElementById('card');
  if (!card) { return; }
  var e = document.createElement('div');
  e.id = 'card-empty';
  e.style.cssText = 'display:none;position:absolute;left:0;top:0;right:0;bottom:0;background:#FFFFFF;' +
    'border-radius:16px;flex-direction:column;align-items:center;justify-content:center;gap:10px;' +
    'text-align:center;padding:32px;';
  e.innerHTML = '<span class="ce-t" style="font-family:Inter,sans-serif;font-size:18px;font-weight:600;color:#101828;">' +
    'ยังไม่เปิดตรวจในภูมิภาคนี้</span>' +
    '<span class="ce-s" style="font-size:14px;line-height:1.6;color:#475467;max-width:272px;">' +
    'เราจะไม่ประกาศอันดับของภูมิภาคที่ยังไม่ได้เข้าไปตรวจด้วยตัวเอง</span>';
  card.appendChild(e);
}

document.addEventListener('click', function (ev) {
  var pin = ev.target.closest('[data-pin]');
  if (pin) { select(TOP[pin.dataset.pin]); return; }
  var hof = ev.target.closest('[data-hof]');
  if (hof) {
    var hk = Object.keys(B).filter(function(k){ return k === hof.dataset.hof || B[k].id === hof.dataset.hof; })[0];
    if (!hk) { return; }
    if ((REGION[region] || []).indexOf(B[hk].iso) < 0) { setRegion('all'); }
    select(hk);
    document.querySelector('.map-svg').scrollIntoView({behavior: 'smooth', block: 'center'});
  }
});
document.addEventListener('keydown', function (ev) {
  if (ev.key !== 'Enter' && ev.key !== ' ') { return; }
  var t = ev.target.closest('[data-pin], [data-hof]');
  if (t) { ev.preventDefault(); t.click(); }
});
document.querySelectorAll('[data-hof]').forEach(function (el) {
  el.setAttribute('role', 'button');
  el.setAttribute('tabindex', '0');
});


/* ── ช่องโลโก้ ─────────────────────────────────────────────────
   ตัวยึดเป็นตัวย่อของโบรกเกอร์ · ถ้ามีไฟล์ logos/<slug>.svg (หรือ .png)
   วางไว้ข้างหน้าเว็บ ระบบจะสลับไปใช้ไฟล์จริงเองโดยไม่ต้องแก้โค้ด     */
var LOGO_SLUG={icm:"ic-markets",pep:"pepperstone",exness:"exness",tickmill:"tickmill",ig:"ig",oanda:"oanda",equiti:"equiti",hfm:"hfm"};
var LOGO_DATA={"exness":"data:image/png;base64,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","ic-markets":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADiklEQVR42u2WS0hcZxTHf9+dRxyTDkMcFceRRtILbUc0fUBpqQ+IoERoESIU3OnWQbqQdFVQGiGkrQGb4gN0WUliC7qI4sLEprUlNmjjjFURQRmNHUxH5xHtzJ3TRciojbbNoriZA3dzz+F8v4/zP+d8SkSEYzSNY7Y0QBogDZAGML9I8OPEJkOPbxFNRnGac/jw9EUytAzm5+fRNA1d1wEQERYWFhgbG2Nubg7DMNB1naqqKjweD0qpvaTyAuaLPZQzU07J+B5588ciWQouSXdXt+i6Lj09PSIikkgkpK+vTwoLC0UpJUDqKygokP7+fjEMI5XzUICftn+Q6+sd8vX6NZmO/JL6748+lII7TrF9a5LzNyuk6oMqsVqsAqQABgcHxeFwCCBms1l0XZezZ8+KyWQSQHJycmR8fPyfAT5duSS2SeTkJHJt7coeWHBS3ho6J9f9X8nd+3fF6XSmbtfb2yuRSETKysoEEKWUNDU1SSAQkOXlZamtrU3F1tfXSzweFxGRQzWgUGiAAkg+rdej2CNu/HaDtuLLXHj5ArOzswfVrGn4/X6mp6cByM/Px+v14nK5AGhubiYcDhOPx7FarUQiERwOx9EilDjEw/DHyTCDO7e46rtCzBylJbclJbT9m1wpxcrKCpFIBAC3201eXl7KX1payvDwcCrWarUe3QWJqPDnOryb+R4P1h7QsfU5O6eeUJz7GibT0Z2bTCYPAP3dt7u7i4iglMJisaCUen4OGGJgbEHbK5f57vwQr595lXjuE06cBmU5ukVFBLfbTWZmJgCBQICNjY2Uf2JigsrKSioqKmhoaCAUCj0/iDZ3Nvny1y+wWWxceuMTsmxZmDIE7cS/z4hkMonH46GoqAiA1dVVurq6CAaDrK2t0d3dzdTUFDMzM9hsNux2+14JEskEt1dv0zF3lcnYPdrOfYamtGeK/E8mItjtdrxeLz6fj3A4TGdnJ6OjoxiGweLiIgDZ2dk0NjZiNpv3ANZ31mnxf8ySWsKSA1qG2pcYkvIUJCmC7DvwsOdkXV0doVCI9vZ2AoHAgW5xuVy0trZSXl6+pxURke3EFjd//4YI24iC918q5+1T7wBwb/sO96M/o1BkmZ1czPoIm5ZJMBhkYGCAWCyGUorq6mqKi4tT5fD5fIyMjBwYxTU1NZSUlKBp2kGA/3vhPFP+sW3Dow5PvwfSAGmANADAX8xFJFgjzBaAAAAAAElFTkSuQmCC","xm":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACTUlEQVR42u2XPUsjQRjH/yMGzC4oKS00drrGQrEQ7iNE5GqLoIUEtPRLWNiljUbURjCCe5DOziB2gi+N+A1EU7hLUkh+V2jG7KmXcN7dNvnDwsw8PM/8dmaeeZEkARPAMRDw7xW89jUhSea1cCYppf+rmqRvBjiW9F3xyDdAIMmNCSA0AIpRfYpZPYAewBvAzo4kqVqtKpFIyBgjY4yOjo4iDo+PjxobG7P25eVlWzbGaGpqSmEYRnz29vasPZlM6uLi4s1oN0jHgasrADY2NpCEJIaGhri7uwOg2WyysLBgbdPT09RqNVtvfUtLSzbszc0NrutaW6FQYHt729rfACTwPAgCms0m2WzWOs3OztJoNNjc3LRtg4OD3N7eUq/X3wFIolQqEYYhmUzGti0uLrK+vk4+n/8EQIJcDoD7+3tGRkaQxPDwML7vk0gkbLCDgwOATwEcx4n8xPj4OPv7+xhjOgBIsLUFQLVaZWBggHK5zOjoqA22urpq3X4FmJubeweTTCbxfZ9UKoWkLgAcBy4vAbi+vmZ+ft4Gm5mZoV6vfwpwfn7O5ORkpK1YLLK2tmbr7QAd07BSqahSqXSdVq7r6vDwUK77cr7lcjmtrKzo+fn5Y4dOU9Df3/9uSH83BVevmbS7u4vneQTByx0nn89/OAJdLUJJZLPZrhZhC6AVo6XuADwPnp6+lIbtAO3qDPCXNqI/ByiVADg9PY3Me7lcjgR6eHggnU5Hdr2vAPRuRD2AHkCfpDDG/sM+SScxApzE/jhV2/P8RxzP858e/zdqYe4rqwAAAABJRU5ErkJggg==","pepperstone":"data:image/png;base64,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","fp-markets":"data:image/png;base64,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","eightcap":"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+CjxnPgo8cGF0aCBkPSJNIDI3Ni41MCA1MDcuNTQgQzI1Ny44Niw1MDkuMjEgMjUzLjM1LDUwOS4yMSAyMzQuNTAsNTA3LjQ4IEMxOTMuMzIsNTAzLjcxIDE2MS45Miw0OTIuOTMgMTI5LjAwLDQ3MS4yNCBDMTA3Ljg1LDQ1Ny4zMSA4Ny4yNyw0MzQuMzAgNzYuOTEsNDEzLjAwIEM2MC41MiwzNzkuMjkgNjAuNjIsMzQxLjE4IDc3LjE4LDMwNy41MyBDODQuMTMsMjkzLjQyIDkxLjcxLDI4My4xNiAxMDUuMjAsMjY5LjYwIEMxMTQuMTcsMjYwLjU5IDExNy44NiwyNTYuMjEgMTE3LjQ1LDI1NS4xMCBDMTE3LjEzLDI1NC4yMiAxMTMuNDAsMjUwLjM1IDEwOS4xNiwyNDYuNTAgQzk1LjQ4LDIzNC4wOCA4NC44OSwyMjAuMTMgNzcuMDYsMjA0LjIxIEM2MC42MSwxNzAuODAgNjAuNTcsMTMyLjc1IDc2Ljk0LDk4LjkwIEM5MC40NSw3MC45NyAxMTYuNzgsNDUuNTUgMTUwLjI5LDI4LjA4IEMxOTEuODMsNi40MiAyNDUuNjAsLTEuNTMgMjk1LjUwLDYuNjIgQzM0MC40MiwxMy45NiAzNzguOTEsMzIuNjkgNDA3LjA0LDYwLjkyIEM0MzQuMjcsODguMjMgNDQ3LjMxLDExNy41OSA0NDcuMjcsMTUxLjUwIEM0NDcuMjUsMTcxLjYwIDQ0My4xMCwxODguMTMgNDMzLjMzLDIwNy4wOCBDNDI1LjI2LDIyMi43MiA0MTcuNDYsMjMyLjc0IDQwMS42NSwyNDcuNzcgQzM5Ny40NCwyNTEuNzcgMzk0LjAwLDI1NS40NyAzOTQuMDAsMjU2LjAwIEMzOTQuMDAsMjU2LjUzIDM5Ny40NCwyNjAuMjMgNDAxLjY1LDI2NC4yMyBDNDA1Ljg2LDI2OC4yMyA0MTAuOTIsMjczLjIzIDQxMi45MCwyNzUuMzQgQzQyMy45NiwyODcuMTMgNDM2LjIxLDMwNy43MiA0NDEuMzAsMzIzLjEwIEM0NTEuMTMsMzUyLjc1IDQ0OC45MCwzODQuNTEgNDM0Ljk1LDQxMy41MCBDNDI1LjIzLDQzMy43MCA0MDMuNzYsNDU3LjU3IDM4My4wMCw0NzEuMjQgQzM0OS43Miw0OTMuMTYgMzE4LjY4LDUwMy43NCAyNzYuNTAsNTA3LjU0IFpNIDI0NC4wMCA0MjcuNDIgQzI0OS4wNSw0MjguMzIgMjcyLjY5LDQyNy4wMiAyNzkuMDAsNDI1LjUwIEMzMDAuMTIsNDIwLjQwIDMxOC42OCw0MDkuNzIgMzI5LjA0LDM5Ni43MSBDMzM1LjA2LDM4OS4xNSAzNDAuOTYsMzc2LjM1IDM0Mi4xMywzNjguMjggQzM0NS4zMCwzNDYuNDcgMzM0LjI4LDMyNC4zOCAzMTMuMDMsMzEwLjAxIEMzMDcuMjIsMzA2LjA4IDI1OC4zNiwyNTguMzggMjU3Ljc1LDI1Ni4wNCBDMjU3LjI0LDI1NC4xMSAzMDMuMzIsMjA4LjgyIDMxMS41MCwyMDMuMjAgQzMzMi41MywxODguNzYgMzQyLjQzLDE3MS44NCAzNDIuMzMsMTUwLjUwIEMzNDIuMjksMTQxLjQxIDM0MS45NywxMzkuNzQgMzM4LjgxLDEzMi4xNCBDMzM0LjMwLDEyMS4yOSAzMjcuNTEsMTEyLjIyIDMxOC41OSwxMDUuMTQgQzMxMS4yOSw5OS4zNCAyOTcuMTAsOTEuMzQgMjkxLjU2LDg5LjkyIEMyODkuODgsODkuNDggMjg0LjkwLDg4LjExIDI4MC41MCw4Ni44NyBDMjY5Ljg4LDgzLjg4IDI0My4yOCw4My42MCAyMzMuMDAsODYuMzcgQzIwMi42NCw5NC41NCAxODMuMjgsMTA4Ljk0IDE3My44NCwxMzAuMzcgQzE2Mi4wMywxNTcuMTggMTczLjYxLDE4Ni40MSAyMDMuNTAsMjA1LjI2IEMyMDcuNDgsMjA3Ljc2IDI1My45MiwyNTMuNzQgMjU0LjA5LDI1NS4zNCBDMjU0LjI4LDI1Ny4yMSAyMDYuMDQsMzA0LjY2IDE5Ny4yOCwzMTEuMjIgQzE4Ni45NiwzMTguOTQgMTgyLjQ4LDMyMy43MSAxNzcuMzEsMzMyLjQ4IEMxNTkuODMsMzYyLjE3IDE3Mi4zNCwzOTcuMjkgMjA3LjAwLDQxNS44MyBDMjE1LjQ2LDQyMC4zNSAyMjYuNjAsNDI0LjI4IDIzNS41MCw0MjUuODkgQzIzOC44MCw0MjYuNDkgMjQyLjYyLDQyNy4xOCAyNDQuMDAsNDI3LjQyIFoiIGZpbGw9InJnYig0NSwxODYsMTA1KSIvPgo8cGF0aCBkPSJNIDI5MC4wMCA1MDguMDYgQzI4My40NCw1MDkuMTMgMjQzLjMzLDUxMC4xMSAyMzUuMDAsNTA5LjQxIEMyMTEuODQsNTA3LjQ0IDE4OC4wNiw1MDEuNzEgMTY2LjAwLDQ5Mi43OSBDMTA4Ljk4LDQ2OS43MSA2OS42OCw0MjQuMjMgNjMuODEsMzc0LjUwIEM2Mi4yNywzNjEuNDkgNjMuNjIsMzQyLjI4IDY2LjkwLDMzMC41NSBDNzMuOTMsMzA1LjM4IDg0Ljk5LDI4Ny4xMCAxMDUuMzcsMjY3LjAxIEMxMTQuODcsMjU3LjY0IDExNy42MywyNTQuMDAgMTE1LjIxLDI1NC4wMCBDMTE0LjAxLDI1NC4wMCA5My41NywyMzMuMDggODkuODEsMjI4LjAwIEM3NC40OSwyMDcuMjkgNjUuODQsMTg1LjY3IDYzLjc2LDE2Mi44OSBDNjAuMjIsMTI0LjI0IDc0LjE4LDg4LjQ3IDEwNC4xNiw1OS40MiBDMTE1Ljc1LDQ4LjE4IDEyMS45OSw0My4xNyAxMzMuMDIsMzYuMjQgQzE2MC4wMCwxOS4yOCAxODUuMzUsMTAuMTUgMjIzLjAwLDMuODIgQzIzMy4yMCwyLjEwIDI3OC44NywyLjEyIDI4OS41MCwzLjg0IEMzMjUuMDMsOS42MSAzNTIuNDMsMTkuNTIgMzc4LjkwLDM2LjIwIEM0MDguNjAsNTQuOTIgNDMzLjA1LDg0LjI1IDQ0Mi40NywxMTIuNDcgQzQ1MC4wOCwxMzUuMjggNDUwLjg1LDE2Mi4wMiA0NDQuNTMsMTgzLjUwIEM0MzcuODMsMjA2LjMwIDQyNy4xMCwyMjMuOTIgNDA4LjMyLDI0My4wMCBDNDAxLjU1LDI0OS44OCAzOTYuMDEsMjU1Ljc3IDM5Ni4wMCwyNTYuMTEgQzM5Ni4wMCwyNTYuNDQgNDAwLjc3LDI2MS4zOSA0MDYuNTksMjY3LjExIEM0MTguMTMsMjc4LjQyIDQyMy4wNiwyODQuNDUgNDMwLjMwLDI5Ni4xMSBDNDQ3Ljk3LDMyNC41NCA0NTMuMzYsMzU5LjM0IDQ0NS4wMCwzOTEuMDAgQzQzNi40Myw0MjMuNDUgNDExLjc1LDQ1NS4xMCAzNzguOTAsNDc1LjgwIEMzNTIuNTMsNDkyLjQxIDMyNS4zNCw1MDIuMjggMjkwLjAwLDUwOC4wNiBaTSAyNzYuNTAgNTA3LjU0IEMzMTguNjgsNTAzLjc0IDM0OS43Miw0OTMuMTYgMzgzLjAwLDQ3MS4yNCBDNDAzLjc2LDQ1Ny41NyA0MjUuMjMsNDMzLjcwIDQzNC45NSw0MTMuNTAgQzQ0OC45MCwzODQuNTEgNDUxLjEzLDM1Mi43NSA0NDEuMzAsMzIzLjEwIEM0MzYuMjEsMzA3LjcyIDQyMy45NiwyODcuMTMgNDEyLjkwLDI3NS4zNCBDNDEwLjkyLDI3My4yMyA0MDUuODYsMjY4LjIzIDQwMS42NSwyNjQuMjMgQzM5Ny40NCwyNjAuMjMgMzk0LjAwLDI1Ni41MyAzOTQuMDAsMjU2LjAwIEMzOTQuMDAsMjU1LjQ3IDM5Ny40NCwyNTEuNzcgNDAxLjY1LDI0Ny43NyBDNDE3LjQ2LDIzMi43NCA0MjUuMjYsMjIyLjcyIDQzMy4zMywyMDcuMDggQzQ0My4xMCwxODguMTMgNDQ3LjI1LDE3MS42MCA0NDcuMjcsMTUxLjUwIEM0NDcuMzEsMTE3LjU5IDQzNC4yNyw4OC4yMyA0MDcuMDQsNjAuOTIgQzM3OC45MSwzMi42OSAzNDAuNDIsMTMuOTYgMjk1LjUwLDYuNjIgQzI0NS42MCwtMS41MyAxOTEuODMsNi40MiAxNTAuMjksMjguMDggQzExNi43OCw0NS41NSA5MC40NSw3MC45NyA3Ni45NCw5OC45MCBDNjAuNTcsMTMyLjc1IDYwLjYxLDE3MC44MCA3Ny4wNiwyMDQuMjEgQzg0Ljg5LDIyMC4xMyA5NS40OCwyMzQuMDggMTA5LjE2LDI0Ni41MCBDMTEzLjQwLDI1MC4zNSAxMTcuMTMsMjU0LjIyIDExNy40NSwyNTUuMTAgQzExNy44NiwyNTYuMjEgMTE0LjE3LDI2MC41OSAxMDUuMjAsMjY5LjYwIEM5MS43MSwyODMuMTYgODQuMTMsMjkzLjQyIDc3LjE4LDMwNy41MyBDNjAuNjIsMzQxLjE4IDYwLjUyLDM3OS4yOSA3Ni45MSw0MTMuMDAgQzg3LjI3LDQzNC4zMCAxMDcuODUsNDU3LjMxIDEyOS4wMCw0NzEuMjQgQzE2MS45Miw0OTIuOTMgMTkzLjMyLDUwMy43MSAyMzQuNTAsNTA3LjQ4IEMyNTMuMzUsNTA5LjIxIDI1Ny44Niw1MDkuMjEgMjc2LjUwLDUwNy41NCBaTSAyNDQuMDAgNDI3LjQyIEMyNDIuNjIsNDI3LjE4IDIzOC44MCw0MjYuNDkgMjM1LjUwLDQyNS44OSBDMjI2LjYwLDQyNC4yOCAyMTUuNDYsNDIwLjM1IDIwNy4wMCw0MTUuODMgQzE3Mi4zNCwzOTcuMjkgMTU5LjgzLDM2Mi4xNyAxNzcuMzEsMzMyLjQ4IEMxODIuNDgsMzIzLjcxIDE4Ni45NiwzMTguOTQgMTk3LjI4LDMxMS4yMiBDMjA2LjA0LDMwNC42NiAyNTQuMjgsMjU3LjIxIDI1NC4wOSwyNTUuMzQgQzI1My45MiwyNTMuNzQgMjA3LjQ4LDIwNy43NiAyMDMuNTAsMjA1LjI2IEMxNzMuNjEsMTg2LjQxIDE2Mi4wMywxNTcuMTggMTczLjg0LDEzMC4zNyBDMTgzLjI4LDEwOC45NCAyMDIuNjQsOTQuNTQgMjMzLjAwLDg2LjM3IEMyNDMuMjgsODMuNjAgMjY5Ljg4LDgzLjg4IDI4MC41MCw4Ni44NyBDMjg0LjkwLDg4LjExIDI4OS44OCw4OS40OCAyOTEuNTYsODkuOTIgQzI5Ny4xMCw5MS4zNCAzMTEuMjksOTkuMzQgMzE4LjU5LDEwNS4xNCBDMzI3LjUxLDExMi4yMiAzMzQuMzAsMTIxLjI5IDMzOC44MSwxMzIuMTQgQzM0MS45NywxMzkuNzQgMzQyLjI5LDE0MS40MSAzNDIuMzMsMTUwLjUwIEMzNDIuNDMsMTcxLjg0IDMzMi41MywxODguNzYgMzExLjUwLDIwMy4yMCBDMzAzLjMyLDIwOC44MiAyNTcuMjQsMjU0LjExIDI1Ny43NSwyNTYuMDQgQzI1OC4zNiwyNTguMzggMzA3LjIyLDMwNi4wOCAzMTMuMDMsMzEwLjAxIEMzMzQuMjgsMzI0LjM4IDM0NS4zMCwzNDYuNDcgMzQyLjEzLDM2OC4yOCBDMzQwLjk2LDM3Ni4zNSAzMzUuMDYsMzg5LjE1IDMyOS4wNCwzOTYuNzEgQzMxOC42OCw0MDkuNzIgMzAwLjEyLDQyMC40MCAyNzkuMDAsNDI1LjUwIEMyNzIuNjksNDI3LjAyIDI0OS4wNSw0MjguMzIgMjQ0LjAwLDQyNy40MiBaTSAyMzcuNTAgNDI0Ljg2IEMyNDguMjcsNDI3LjM3IDI3NC4yNyw0MjUuNzggMjg3LjAwLDQyMS44NSBDMzE5LjY2LDQxMS43NSAzNDEuMDIsMzg3LjIzIDM0MC45OSwzNTkuODYgQzM0MC45OCwzMzkuOTcgMzMwLjM3LDMyMy4yOSAzMDguMTUsMzA4LjIwIEMzMDYuMjksMzA2LjkzIDI5My45NiwyOTUuMTIgMjgwLjc2LDI4MS45NSBDMjY3LjU2LDI2OC43OCAyNTYuMjYsMjU3Ljk5IDI1NS42MywyNTcuOTkgQzI1NS4wMSwyNTcuOTggMjQzLjcwLDI2OC44NyAyMzAuNTAsMjgyLjE3IEMyMTcuMzAsMjk1LjQ4IDIwNS4xNCwzMDcuMzAgMjAzLjQ4LDMwOC40NCBDMTgxLjU0LDMyMy40NCAxNzEuMDIsMzQwLjEwIDE3MS4wMSwzNTkuODYgQzE3MC45OSwzODQuMzAgMTg3LjEzLDQwNS44MSAyMTQuNTAsNDE3Ljc5IEMyMjAuODksNDIwLjU4IDIyNi40Myw0MjIuMjkgMjM3LjUwLDQyNC44NiBaTSAyMzIuNTYgMjMwLjQxIEMyNDQuOTksMjQyLjg0IDI1NS41MiwyNTMuMDAgMjU1Ljk1LDI1My4wMCBDMjU2LjM4LDI1My4wMCAyNjYuODgsMjQyLjg3IDI3OS4yOCwyMzAuNDkgQzI5MS42OSwyMTguMTAgMzA0LjA0LDIwNi40OSAzMDYuNzMsMjA0LjY4IEMzMTUuODMsMTk4LjU2IDMxOS40OCwxOTUuNjQgMzI0LjI0LDE5MC42OCBDMzI5LjU2LDE4NS4xNCAzMzYuMDAsMTc1Ljg4IDMzNi4wMCwxNzMuNzggQzMzNi4wMCwxNzMuMDIgMzM2LjQxLDE3MS45NyAzMzYuOTEsMTcxLjQ1IEMzMzguODksMTY5LjM4IDM0MS4wMCwxNTkuMjIgMzQxLjAwLDE1MS43MiBDMzQxLjAwLDE0NC4yNCAzMzguODQsMTMzLjYzIDMzNi44OSwxMzEuNTUgQzMzNi40MCwxMzEuMDMgMzM2LjAwLDEyOS45OSAzMzYuMDAsMTI5LjI1IEMzMzYuMDAsMTI3LjAxIDMyOC4xNiwxMTYuMTYgMzIyLjY1LDExMC43OCBDMzE5LjgyLDEwOC4wMSAzMTQuNDcsMTAzLjc2IDMxMC43NywxMDEuMzQgQzMwMy4yMCw5Ni4zOCAyODYuNjEsODkuMzkgMjc4LjczLDg3Ljg1IEMyNzAuMDgsODYuMTUgMjQ2LjI4LDg1LjY1IDIzOC41MCw4Ny4wMCBDMjE5LjU3LDkwLjI5IDIwMS4xNiw5OS4xNCAxODkuNDUsMTEwLjU3IEMxODQuMDQsMTE1Ljg1IDE3Ni4wMCwxMjcuMDIgMTc2LjAwLDEyOS4yNSBDMTc2LjAwLDEyOS45OSAxNzUuNjAsMTMxLjAzIDE3NS4xMSwxMzEuNTUgQzE3My4xNiwxMzMuNjMgMTcxLjAwLDE0NC4yNCAxNzEuMDAsMTUxLjcyIEMxNzEuMDAsMTU5LjIyIDE3My4xMSwxNjkuMzggMTc1LjA5LDE3MS40NSBDMTc1LjU5LDE3MS45NyAxNzYuMDAsMTczLjAyIDE3Ni4wMCwxNzMuNzggQzE3Ni4wMCwxNzUuODggMTgyLjQ0LDE4NS4xNCAxODcuNzYsMTkwLjY4IEMxOTIuNTAsMTk1LjYyIDE5Ni4xOCwxOTguNTYgMjA1LjE2LDIwNC42MSBDMjA3Ljc5LDIwNi4zOCAyMjAuMTIsMjE3Ljk5IDIzMi41NiwyMzAuNDEgWiIgZmlsbD0icmdiKDEyNCwyMDgsMTU5KSIvPgo8cGF0aCBkPSJNIDI4MS4wMCA1MTEuMDAgQzI4MC4wMyw1MTEuNjMgMzIwLjMzLDUxMS45NyAzOTUuNzUsNTExLjk4IEwgNTEyLjAwIDUxMi4wMCBMIDExNi4wNiA1MTIuMDAgQzE5My4xOCw1MTIuMDAgMjMxLjkxLDUxMS42NiAyMzEuNTAsNTExLjAwIEMyMzEuMTYsNTEwLjQ1IDIyOS4yMiw1MTAuMDAgMjI3LjE5LDUxMC4wMCBDMjE4LjM5LDUwOS45OSAxODguMjMsNTAyLjkyIDE3My4xOCw0OTcuMzQgQzE0NC45MCw0ODYuODUgMTIzLjMwLDQ3My4zMCAxMDMuNDUsNDUzLjYxIEM3OS41Miw0MjkuODggNjcuMTUsNDA2LjQ5IDYyLjQ1LDM3Ni4wOSBDNjAuNjEsMzY0LjEyIDYwLjYyLDM1Ny41MSA2Mi41NCwzNDQuNzQgQzY3LjA3LDMxNC40NyA4MC4wNSwyODkuOTQgMTA0LjA1LDI2Ni4yOCBDMTA5LjUxLDI2MC45MCAxMTMuOTgsMjU2LjIxIDExMy45OSwyNTUuODUgQzExMy45OSwyNTUuNDkgMTExLjY5LDI1My4wMSAxMDguODcsMjUwLjM1IEM5Mi4xNCwyMzQuNTMgODIuNzUsMjIyLjQ0IDc0LjYwLDIwNi4yMSBDNjYuOTUsMTkwLjk4IDYxLjAwLDE2Ni44OSA2MS4wMCwxNTEuMTMgQzYxLjAwLDEzNS43NiA2Ni4yMCwxMTQuNTQgNzMuNzgsOTguOTQgQzgxLjc2LDgyLjUzIDg4LjEyLDczLjgyIDEwMi45Nyw1OC45NCBDMTEzLjY5LDQ4LjIxIDExOS4yMiw0My41OSAxMjkuNTAsMzYuNzkgQzE0OS4wMiwyMy44OSAxNzEuMDMsMTQuMDcgMTkyLjc1LDguNTYgQzIwNi4yMiw1LjE1IDIyMi43MiwyLjAxIDIyNy4xOSwyLjAwIEMyMjkuMjIsMi4wMCAyMzEuMTYsMS41NSAyMzEuNTAsMS4wMCBDMjMxLjkxLDAuMzQgMTkzLjE4LDAuMDAgMTE2LjA2LDAuMDAgTCA1MTIuMDAgMC4wMCBMIDM5NS43NSAwLjAyIEMzMjAuMzMsMC4wMyAyODAuMDMsMC4zNyAyODEuMDAsMS4wMCBDMjgxLjgzLDEuNTMgMjgzLjg1LDEuOTggMjg1LjUwLDEuOTkgQzI4Ny4xNSwyLjAwIDI5My4xOSwyLjkyIDI5OC45Myw0LjAzIEMzNDUuMTIsMTMuMDAgMzc4LjQ4LDI5LjMxIDQwNy4zNSw1Ny4wNSBDNDMyLjY2LDgxLjM3IDQ0Ni42MywxMDguNzIgNDUwLjAyLDE0MC41NiBDNDUxLjEyLDE1MC44OCA0NTEuMDcsMTU0LjIwIDQ0OS42NywxNjUuMDYgQzQ0Ny4wMywxODUuNDUgNDM5LjM1LDIwNS44NCA0MjguMjgsMjIxLjgyIEM0MjEuNDgsMjMxLjY0IDQxOS45MywyMzMuNDYgNDA4LjIzLDI0NS4yNSBMIDM5Ny41NyAyNTYuMDAgTCA0MDguMjMgMjY2Ljc1IEM0MTQuMTAsMjcyLjY2IDQxOS45NywyNzguODUgNDIxLjI4LDI4MC41MCBDNDQyLjY5LDMwNy40NyA0NTMuMjQsMzQwLjg1IDQ1MC4wMSwzNzEuNDQgQzQ0Ni42Niw0MDMuMjQgNDMyLjY3LDQzMC42MiA0MDcuMzUsNDU0Ljk1IEMzNzguNDgsNDgyLjY5IDM0NS4xMiw0OTkuMDAgMjk4LjkzLDUwNy45NyBDMjkzLjE5LDUwOS4wOCAyODcuMTUsNTEwLjAwIDI4NS41MCw1MTAuMDEgQzI4My44NSw1MTAuMDIgMjgxLjgzLDUxMC40NyAyODEuMDAsNTExLjAwIFpNIDI5MC4wMCA1MDguMDYgQzMyNS4zNCw1MDIuMjggMzUyLjUzLDQ5Mi40MSAzNzguOTAsNDc1LjgwIEM0MTEuNzUsNDU1LjEwIDQzNi40Myw0MjMuNDUgNDQ1LjAwLDM5MS4wMCBDNDUzLjM2LDM1OS4zNCA0NDcuOTcsMzI0LjU0IDQzMC4zMCwyOTYuMTEgQzQyMy4wNiwyODQuNDUgNDE4LjEzLDI3OC40MiA0MDYuNTksMjY3LjExIEM0MDAuNzcsMjYxLjM5IDM5Ni4wMCwyNTYuNDQgMzk2LjAwLDI1Ni4xMSBDMzk2LjAxLDI1NS43NyA0MDEuNTUsMjQ5Ljg4IDQwOC4zMiwyNDMuMDAgQzQyNy4xMCwyMjMuOTIgNDM3LjgzLDIwNi4zMCA0NDQuNTMsMTgzLjUwIEM0NTAuODUsMTYyLjAyIDQ1MC4wOCwxMzUuMjggNDQyLjQ3LDExMi40NyBDNDMzLjA1LDg0LjI1IDQwOC42MCw1NC45MiAzNzguOTAsMzYuMjAgQzM1Mi40MywxOS41MiAzMjUuMDMsOS42MSAyODkuNTAsMy44NCBDMjc4Ljg3LDIuMTIgMjMzLjIwLDIuMTAgMjIzLjAwLDMuODIgQzE4NS4zNSwxMC4xNSAxNjAuMDAsMTkuMjggMTMzLjAyLDM2LjI0IEMxMjEuOTksNDMuMTcgMTE1Ljc1LDQ4LjE4IDEwNC4xNiw1OS40MiBDNzQuMTgsODguNDcgNjAuMjIsMTI0LjI0IDYzLjc2LDE2Mi44OSBDNjUuODQsMTg1LjY3IDc0LjQ5LDIwNy4yOSA4OS44MSwyMjguMDAgQzkzLjU3LDIzMy4wOCAxMTQuMDEsMjU0LjAwIDExNS4yMSwyNTQuMDAgQzExNy42MywyNTQuMDAgMTE0Ljg3LDI1Ny42NCAxMDUuMzcsMjY3LjAxIEM4NC45OSwyODcuMTAgNzMuOTMsMzA1LjM4IDY2LjkwLDMzMC41NSBDNjMuNjIsMzQyLjI4IDYyLjI3LDM2MS40OSA2My44MSwzNzQuNTAgQzY5LjY4LDQyNC4yMyAxMDguOTgsNDY5LjcxIDE2Ni4wMCw0OTIuNzkgQzE4OC4wNiw1MDEuNzEgMjExLjg0LDUwNy40NCAyMzUuMDAsNTA5LjQxIEMyNDMuMzMsNTEwLjExIDI4My40NCw1MDkuMTMgMjkwLjAwLDUwOC4wNiBaTSAyMzcuNTAgNDI0Ljg2IEMyMjYuNDMsNDIyLjI5IDIyMC44OSw0MjAuNTggMjE0LjUwLDQxNy43OSBDMTg3LjEzLDQwNS44MSAxNzAuOTksMzg0LjMwIDE3MS4wMSwzNTkuODYgQzE3MS4wMiwzNDAuMTAgMTgxLjU0LDMyMy40NCAyMDMuNDgsMzA4LjQ0IEMyMDUuMTQsMzA3LjMwIDIxNy4zMCwyOTUuNDggMjMwLjUwLDI4Mi4xNyBDMjQzLjcwLDI2OC44NyAyNTUuMDEsMjU3Ljk4IDI1NS42MywyNTcuOTkgQzI1Ni4yNiwyNTcuOTkgMjY3LjU2LDI2OC43OCAyODAuNzYsMjgxLjk1IEMyOTMuOTYsMjk1LjEyIDMwNi4yOSwzMDYuOTMgMzA4LjE1LDMwOC4yMCBDMzMwLjM3LDMyMy4yOSAzNDAuOTgsMzM5Ljk3IDM0MC45OSwzNTkuODYgQzM0MS4wMiwzODcuMjMgMzE5LjY2LDQxMS43NSAyODcuMDAsNDIxLjg1IEMyNzQuMjcsNDI1Ljc4IDI0OC4yNyw0MjcuMzcgMjM3LjUwLDQyNC44NiBaTSAyMzIuNTYgMjMwLjQxIEMyMjAuMTIsMjE3Ljk5IDIwNy43OSwyMDYuMzggMjA1LjE2LDIwNC42MSBDMTk2LjE4LDE5OC41NiAxOTIuNTAsMTk1LjYyIDE4Ny43NiwxOTAuNjggQzE4Mi40NCwxODUuMTQgMTc2LjAwLDE3NS44OCAxNzYuMDAsMTczLjc4IEMxNzYuMDAsMTczLjAyIDE3NS41OSwxNzEuOTcgMTc1LjA5LDE3MS40NSBDMTczLjExLDE2OS4zOCAxNzEuMDAsMTU5LjIyIDE3MS4wMCwxNTEuNzIgQzE3MS4wMCwxNDQuMjQgMTczLjE2LDEzMy42MyAxNzUuMTEsMTMxLjU1IEMxNzUuNjAsMTMxLjAzIDE3Ni4wMCwxMjkuOTkgMTc2LjAwLDEyOS4yNSBDMTc2LjAwLDEyNy4wMiAxODQuMDQsMTE1Ljg1IDE4OS40NSwxMTAuNTcgQzIwMS4xNiw5OS4xNCAyMTkuNTcsOTAuMjkgMjM4LjUwLDg3LjAwIEMyNDYuMjgsODUuNjUgMjcwLjA4LDg2LjE1IDI3OC43Myw4Ny44NSBDMjg2LjYxLDg5LjM5IDMwMy4yMCw5Ni4zOCAzMTAuNzcsMTAxLjM0IEMzMTQuNDcsMTAzLjc2IDMxOS44MiwxMDguMDEgMzIyLjY1LDExMC43OCBDMzI4LjE2LDExNi4xNiAzMzYuMDAsMTI3LjAxIDMzNi4wMCwxMjkuMjUgQzMzNi4wMCwxMjkuOTkgMzM2LjQwLDEzMS4wMyAzMzYuODksMTMxLjU1IEMzMzguODQsMTMzLjYzIDM0MS4wMCwxNDQuMjQgMzQxLjAwLDE1MS43MiBDMzQxLjAwLDE1OS4yMiAzMzguODksMTY5LjM4IDMzNi45MSwxNzEuNDUgQzMzNi40MSwxNzEuOTcgMzM2LjAwLDE3My4wMiAzMzYuMDAsMTczLjc4IEMzMzYuMDAsMTc1Ljg4IDMyOS41NiwxODUuMTQgMzI0LjI0LDE5MC42OCBDMzE5LjQ4LDE5NS42NCAzMTUuODMsMTk4LjU2IDMwNi43MywyMDQuNjggQzMwNC4wNCwyMDYuNDkgMjkxLjY5LDIxOC4xMCAyNzkuMjgsMjMwLjQ5IEMyNjYuODgsMjQyLjg3IDI1Ni4zOCwyNTMuMDAgMjU1Ljk1LDI1My4wMCBDMjU1LjUyLDI1My4wMCAyNDQuOTksMjQyLjg0IDIzMi41NiwyMzAuNDEgWk0gMjQzLjUwIDQyNC4wMyBDMjY2LjQwLDQyNi43MCAyOTIuNTAsNDIwLjk3IDMwOS45NCw0MDkuNDYgQzM0OS4xOSwzODMuNTQgMzQ5LjUzLDMzOC40MSAzMTAuNjYsMzExLjgwIEMzMDcuNDUsMzA5LjYwIDI5NC4wNSwyOTcuMDUgMjgwLjg4LDI4My45MCBDMjY3LjcxLDI3MC43NiAyNTYuNDAsMjYwLjAwIDI1NS43NSwyNjAuMDAgQzI1NS4wOSwyNjAuMDAgMjQzLjA2LDI3MS4zNiAyMjkuMDIsMjg1LjI1IEMyMTQuOTksMjk5LjE0IDIwMC42MiwzMTIuNTMgMTk3LjEwLDMxNS4wMCBDMTg1LjAyLDMyMy40OSAxNzUuMzgsMzM4LjUwIDE3My4wNCwzNTIuNDYgQzE2Ny4yOCwzODYuNzIgMTk4LjkwLDQxOC44NCAyNDMuNTAsNDI0LjAzIFpNIDIzMi41MCAyMjguMjEgQzI0Ni45MywyNDIuNTMgMjU1LjExLDI0OS45NiAyNTYuMjYsMjQ5Ljc4IEMyNTcuMjMsMjQ5LjYyIDI2Ny44MSwyMzkuNzcgMjc5Ljc2LDIyNy44OSBDMjkyLjAyLDIxNS43MCAzMDQuMzMsMjA0LjQwIDMwOC4wMCwyMDEuOTcgQzMyNi43NCwxODkuNTYgMzM2LjA5LDE3Ni41NyAzMzkuMDgsMTU4Ljc5IEMzNDAuMTcsMTUyLjI5IDM0MC4xMywxNTAuMDUgMzM4Ljc3LDE0My4xMyBDMzM1LjM4LDEyNS45NCAzMjcuNDYsMTE0LjcyIDMxMC40NywxMDMuMDYgQzI5NC45Myw5Mi4zOSAyNzguNTIsODcuNzggMjU2LjAwLDg3Ljc2IEMyMzMuNTgsODcuNzMgMjE3LjQ4LDkyLjIyIDIwMS42NSwxMDIuOTAgQzE3OS44NSwxMTcuNjEgMTY5LjQ4LDEzOC4wOCAxNzMuMDYsMTU5LjM3IEMxNzUuOTUsMTc2LjU2IDE4NS4yOSwxODkuNDQgMjA0LjAwLDIwMi4wMCBDMjA3LjU3LDIwNC40MSAyMjAuNDAsMjE2LjIwIDIzMi41MCwyMjguMjEgWiIgZmlsbD0icmdiKDIwMiwyNDEsMjE3KSIvPgo8cGF0aCBkPSJNIDAuMDAgMjU2LjAwIEwgMC4wMCAwLjAwIEwgMTE2LjA2IDAuMDAgQzE5My4xOCwwLjAwIDIzMS45MSwwLjM0IDIzMS41MCwxLjAwIEMyMzEuMTYsMS41NSAyMjkuMjIsMi4wMCAyMjcuMTksMi4wMCBDMjIyLjcyLDIuMDEgMjA2LjIyLDUuMTUgMTkyLjc1LDguNTYgQzE3MS4wMywxNC4wNyAxNDkuMDIsMjMuODkgMTI5LjUwLDM2Ljc5IEMxMTkuMjIsNDMuNTkgMTEzLjY5LDQ4LjIxIDEwMi45Nyw1OC45NCBDODguMTIsNzMuODIgODEuNzYsODIuNTMgNzMuNzgsOTguOTQgQzY2LjIwLDExNC41NCA2MS4wMCwxMzUuNzYgNjEuMDAsMTUxLjEzIEM2MS4wMCwxNjYuODkgNjYuOTUsMTkwLjk4IDc0LjYwLDIwNi4yMSBDODIuNzUsMjIyLjQ0IDkyLjE0LDIzNC41MyAxMDguODcsMjUwLjM1IEMxMTEuNjksMjUzLjAxIDExMy45OSwyNTUuNDkgMTEzLjk5LDI1NS44NSBDMTEzLjk4LDI1Ni4yMSAxMDkuNTEsMjYwLjkwIDEwNC4wNSwyNjYuMjggQzgwLjA1LDI4OS45NCA2Ny4wNywzMTQuNDcgNjIuNTQsMzQ0Ljc0IEM2MC42MiwzNTcuNTEgNjAuNjEsMzY0LjEyIDYyLjQ1LDM3Ni4wOSBDNjcuMTUsNDA2LjQ5IDc5LjUyLDQyOS44OCAxMDMuNDUsNDUzLjYxIEMxMjMuMzAsNDczLjMwIDE0NC45MCw0ODYuODUgMTczLjE4LDQ5Ny4zNCBDMTg4LjIzLDUwMi45MiAyMTguMzksNTA5Ljk5IDIyNy4xOSw1MTAuMDAgQzIyOS4yMiw1MTAuMDAgMjMxLjE2LDUxMC40NSAyMzEuNTAsNTExLjAwIEMyMzEuOTEsNTExLjY2IDE5My4xOCw1MTIuMDAgMTE2LjA2LDUxMi4wMCBMIDAuMDAgNTEyLjAwIEwgMC4wMCAyNTYuMDAgWk0gMjgxLjAwIDUxMS4wMCBDMjgxLjgzLDUxMC40NyAyODMuODUsNTEwLjAyIDI4NS41MCw1MTAuMDEgQzI4Ny4xNSw1MTAuMDAgMjkzLjE5LDUwOS4wOCAyOTguOTMsNTA3Ljk3IEMzNDUuMTIsNDk5LjAwIDM3OC40OCw0ODIuNjkgNDA3LjM1LDQ1NC45NSBDNDMyLjY3LDQzMC42MiA0NDYuNjYsNDAzLjI0IDQ1MC4wMSwzNzEuNDQgQzQ1My4yNCwzNDAuODUgNDQyLjY5LDMwNy40NyA0MjEuMjgsMjgwLjUwIEM0MTkuOTcsMjc4Ljg1IDQxNC4xMCwyNzIuNjYgNDA4LjIzLDI2Ni43NSBMIDM5Ny41NyAyNTYuMDAgTCA0MDguMjMgMjQ1LjI1IEM0MTkuOTMsMjMzLjQ2IDQyMS40OCwyMzEuNjQgNDI4LjI4LDIyMS44MiBDNDM5LjM1LDIwNS44NCA0NDcuMDMsMTg1LjQ1IDQ0OS42NywxNjUuMDYgQzQ1MS4wNywxNTQuMjAgNDUxLjEyLDE1MC44OCA0NTAuMDIsMTQwLjU2IEM0NDYuNjMsMTA4LjcyIDQzMi42Niw4MS4zNyA0MDcuMzUsNTcuMDUgQzM3OC40OCwyOS4zMSAzNDUuMTIsMTMuMDAgMjk4LjkzLDQuMDMgQzI5My4xOSwyLjkyIDI4Ny4xNSwyLjAwIDI4NS41MCwxLjk5IEMyODMuODUsMS45OCAyODEuODMsMS41MyAyODEuMDAsMS4wMCBDMjgwLjAzLDAuMzcgMzIwLjMzLDAuMDMgMzk1Ljc1LDAuMDIgTCA1MTIuMDAgMC4wMCBMIDUxMi4wMCAyNTYuMDAgTCA1MTIuMDAgNTEyLjAwIEwgMzk1Ljc1IDUxMS45OCBDMzIwLjMzLDUxMS45NyAyODAuMDMsNTExLjYzIDI4MS4wMCw1MTEuMDAgWk0gMjQzLjUwIDQyNC4wMyBDMTk4LjkwLDQxOC44NCAxNjcuMjgsMzg2LjcyIDE3My4wNCwzNTIuNDYgQzE3NS4zOCwzMzguNTAgMTg1LjAyLDMyMy40OSAxOTcuMTAsMzE1LjAwIEMyMDAuNjIsMzEyLjUzIDIxNC45OSwyOTkuMTQgMjI5LjAyLDI4NS4yNSBDMjQzLjA2LDI3MS4zNiAyNTUuMDksMjYwLjAwIDI1NS43NSwyNjAuMDAgQzI1Ni40MCwyNjAuMDAgMjY3LjcxLDI3MC43NiAyODAuODgsMjgzLjkwIEMyOTQuMDUsMjk3LjA1IDMwNy40NSwzMDkuNjAgMzEwLjY2LDMxMS44MCBDMzQ5LjUzLDMzOC40MSAzNDkuMTksMzgzLjU0IDMwOS45NCw0MDkuNDYgQzI5Mi41MCw0MjAuOTcgMjY2LjQwLDQyNi43MCAyNDMuNTAsNDI0LjAzIFpNIDIzMi41MCAyMjguMjEgQzIyMC40MCwyMTYuMjAgMjA3LjU3LDIwNC40MSAyMDQuMDAsMjAyLjAwIEMxODUuMjksMTg5LjQ0IDE3NS45NSwxNzYuNTYgMTczLjA2LDE1OS4zNyBDMTY5LjQ4LDEzOC4wOCAxNzkuODUsMTE3LjYxIDIwMS42NSwxMDIuOTAgQzIxNy40OCw5Mi4yMiAyMzMuNTgsODcuNzMgMjU2LjAwLDg3Ljc2IEMyNzguNTIsODcuNzggMjk0LjkzLDkyLjM5IDMxMC40NywxMDMuMDYgQzMyNy40NiwxMTQuNzIgMzM1LjM4LDEyNS45NCAzMzguNzcsMTQzLjEzIEMzNDAuMTMsMTUwLjA1IDM0MC4xNywxNTIuMjkgMzM5LjA4LDE1OC43OSBDMzM2LjA5LDE3Ni41NyAzMjYuNzQsMTg5LjU2IDMwOC4wMCwyMDEuOTcgQzMwNC4zMywyMDQuNDAgMjkyLjAyLDIxNS43MCAyNzkuNzYsMjI3Ljg5IEMyNjcuODEsMjM5Ljc3IDI1Ny4yMywyNDkuNjIgMjU2LjI2LDI0OS43OCBDMjU1LjExLDI0OS45NiAyNDYuOTMsMjQyLjUzIDIzMi41MCwyMjguMjEgWiIgZmlsbD0icmdiKDI1NCwyNTQsMjU0KSIvPgo8L2c+Cjwvc3ZnPg==","tickmill":"data:image/png;base64,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","axi":"data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTExLjMxOTIgMTYuMTc1MUwwLjk5MjIzIDI5LjEyNTFDMC44MTQxMzggMjkuNDc1MSAwLjk5MjIyNyAzMC4wMDAyIDEuMzQ4NDEgMzAuMDAwMkg4LjgyNTlDOS4zNjAxOCAzMC4wMDAyIDkuNzE2MzYgMjkuODI1MiAxMC4wNzI1IDI5LjMwMDFMMTUuOTQ5NiAyMS45NTExTDIxLjgyNjYgMjkuMzAwMUMyMi4xODI4IDI5LjY1MDIgMjIuNTM4OSAzMC4wMDAyIDIzLjA3MzIgMzAuMDAwMkgzMC41NTA3QzMwLjkwNjkgMzAuMDAwMiAzMS4yNjMxIDI5LjQ3NTEgMzAuOTA2OSAyOS4xMjUxTDIwLjU3OTkgMTYuMTc1MUwzMS4wODUgMy4wNTAyQzMxLjI2MzEgMi43MDAxNCAzMS4wODUgMi4xNzUwNSAzMC43Mjg4IDIuMTc1MDVIMjMuMjUxM0MyMi43MTcgMi4xNzUwNSAyMi4zNjA4IDIuMzUwMDggMjIuMDA0NyAyLjg3NTE3TDE2LjEyNzYgMTAuMzk5MkwxMS4zMTkyIDE2LjE3NTFaIiBmaWxsPSIjRDExQzM2Ii8+CjxwYXRoIGQ9Ik0xMy42MzQ0IDcuNDI1OTNWNy4wNzU4N0wxMC4wNzI2IDIuNzAwMTJDOS43MTY0IDIuMzUwMDYgOS4zNjAyMSAyIDguODI1OTQgMkgxLjM0ODQ0QzAuOTkyMjYgMiAwLjYzNjA4IDIuNTI1MDkgMC45OTIyNjMgMi44NzUxNUw5LjAwNDAzIDEyLjg0OTZDOS4xODIxMiAxMy4wMjQ2IDkuMzYwMjEgMTMuMDI0NiA5LjM2MDIxIDEyLjg0OTZMMTMuNjM0NCA3LjQyMzYzVjcuNDI1OTNaIiBmaWxsPSIjRDExQzM2Ii8+Cjwvc3ZnPgo=","hfm":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAB40lEQVR42u2WParqYBCGX5NANGKhIVYWFoKlWNjpGlyBlTuxsg1kBy5BBAtRRLCLWoughRYBRUHIjyaZ09wjyYmJl8sRi5uBD8J8k+GZzF8SAAgfFAYflhggBvg4AAcAPM+j0Wggm80CADabDZbLZcCYZVnU63Xk83kAgKZpmM/nsG0b1WoVpVIJRNFdnUgkcD6fMZvNYFkWAIAkSSJVVelbFEWhP/PBd1KpFI3H44fdaDSidDpNAEhRFCIichwn8hARqapKkiQRAOIeuWAYH2UYvdfu2TteXWjePTbcO/JqmiZWqxUMwwgEwzAM1us17vf7+wA0TUO73cZ2u336RVzXhWma7wMgIui6DsMw/q4LfkoymUQulws4FQQBHMf9fhv+lGaziVqt9rR4isXiS6eZTAatVgvH49FXAwzDYL/fo9/vw3GccABRFCGK4j9HJYoiOp3O07vpdIrhcBgNYNv2Y0g8Sw/Lsu9NwWAwgCzLAT3P8+h2u6hUKpFOT6cTZFkOTcF3C4YCHA4HTCaTgF4QBFwul5dRXa9X9Ho97Ha7eBv+xwBhCy20C1zX9U29sBHrtfM+3243WJYF13Wh67rvLhIUAP3GD0m5XEahUAAAGIaBxWLxWDgvAeIijAFigE/KF/6GEPSOeoQfAAAAAElFTkSuQmCC","ig":"data:image/png;base64,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","oanda":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAR8UlEQVR42u2dSYxdV1rHf+fc6U3l8pBK4iEe4tiJqypWEifO2E2rQahpFKkXCLVgkw3qBWxYwJYdGxatllAjYAFCgFghNbBAIJFA1B3PSRy/KlfFQ+zYiWM7HupN9d6993wszn1+riSueytKlfOezyddxXGVnvzu+Z9v+H//7xzF468Lzh5Y0+4VOAA4cwBw5gDgzAHAmQOAMwcAZw4AzhwAnDkAOHMAcOYA4MwBwJkDgDMHAGcOAM4cAJw5ADgbIfPdK7gPpgCtQFbw+wIYcQAYCUuBTlIcAGSAibQDwNDv/FSg5sPjY/b/80wAT0EzhbMtB4DhzrgULCTwg4cJ/mQnNGO7uHneYtwn/bdrmD9vQE2DcUngcJoAgcabroGWwULKMg9AIphTTUjEgshVAUPq/mMD4z5qXxW6xu5+yffRppFAvQllZUOIA8AwAkBBLLCrDA8HdjfnmQFCDRcW4dMuBArHAwy7B5gag6pnAZC3nkYg1MipJrQS8PTKKgcHgG/R4huBkoc3WaPwPvZAFg0y03RM4NBbbFAbQ9TeMvSMDQl5uz9QyM0YmWvZULAKRJADwFqVfz2BvRXYGNpcQBWoGEINH7bhegy+ch5gqM2A2lezmXyR+I8lgGS2Ce3EAkAcAIbTEoGKh3q6hool3/1n7J+0DKbeXLXFdwBYS/r3kRC1q2RDQZG37iu43oMzHRsKXBI4xPF/0aAma6h1vgWDKlAxRBqZbcGtGILVSQAdAFgj+ldhy79Q5S/kXT82My3LGGpcCBha958IjAfIZA3pFUz+fIU0UqTehFLW/FEOAMPp/mOD2hahtkWWCSxS/4ca+aQLH3cs/btK7t8BYC2sJzBZgzEPYgrX/1JvQiPNbxfj9ACr68JXGu+/tJsVel8NpRSILP+hYptGEgsy08oSRrV6CYADQAEd3tdI+JaUf+M+TFUt/Vuklx8ouJ1YAihUq7n2DgDLWvw13nxw14KpzP1PV1ETof1zrvsXCDRyoQOfdW35hwPAGnft7H/1H2yDnWVbhqkct61BKYX5+8vIuaxxkyWAerqKqnpwM14KkGUUQ6betBrA9X4x3YADwDdZthl4NEK/PoHaEOS7bgNECrkWI7eTwe8mAmWNmqzZUFCkltcKOgapt75eCHIA+AZUOz1BPVWDkgefx9mCLrMSWZw3R2/DtR6UVKb+MbApQu2p5HuRu+v/mzGcbloJuBEHgPviBSZrqLKGTgpeTjmgsI2b+Zb1FpXslXYNPFmFDX6x+G8Eqh4y37bhwldr4gEcD8AXunZVDzVdhcUCWbtkmv1GCvUWBHclc4L9nFLBnSxZCJhpZsBTuNlA1nhKMjawtYT3WNn+WRdYNF9jrvSQjzo2a5dMy1/z0JM1VFJQ/OErpJmuevvXASCvazddg5pnF5ECZVukYLYJC1mWj1j699EItSNr/xb5HF8hV7vI+batIkQcANZctBlmWbtHsQVQCknF7tokA1GWSDJZg3VB5kkKhJJIw0wLbifOA9w3zf64D/tqxUSbWfzXDWPjfykb2uj//b4qKlDFxriUQgyks1kiuUbx3wGApapddpbRD4cFmzbW/acfdZDPuuDrQSI55sF0DboFkzmPLJFsZupfd0DEfRjaENRUFv8TU6BsI+vaNaCR2EVUCuIUtpfRm6Ni6t/+51xehEuLGVsoDgBratnQhpqqoYq+fM8mjTLbGnSBFNAVm0hWV5ZISr1lvUCwdvHfAeCu3c/GALU3G9rUKxjaOJ1x/3dp+fRkLaNypTD7aOrN/HYxQ8QE3ul/F6mBlUJE7uPQRoraW0Fv9It1AbOmjZzpZEMbetBB3BhaBrBX8LsHCm4lMNuwiaSRETgkSgRJU0QEMTlP9rvcL8Emdk5fTdagrAeNmzy34Sk7s9dOB2VbbGB3GTURrEj+Zc514Fq8KsOf98EDCJHvE2qFMflqRkHwtKYdJ6QixZom3yT8E6DiwfSY3cFFDm/ygE4m2vTuAlIqlv2reAM+v0ADyJxqQiu1ZWgqwwsAz/dIbyzwu7//A/74J79Dd7FnQ8Gy3VehUg755/94m7/46T+ha2VMata2/bulXHxoI3Pb6dUYOdO2BE7G/VP2rPonLej+PYV0DMy27ls25n+znl/A15y7fI1n9+1a2WbUmp/9zb8SxynK02uTEygFXYOaqqLX+dApwP8bgcjLWLt4cHJXkrV/d1WgbbKegOQCSa73kA/bgz7CMB8UKUagFHH0gzPMffQJxhiSNMUYc88nSQ3GCNu2TPDErq1It4fSau1yAJ2JNlfIv8tsc1AxaAWLAs+MobdFNpkb8+1pYPd6Kh5sCuFcBz7vZfo/GX4PoH2f3kKTtw6d4smdWzBpitZ6WQQaY9gwVuG1F/Yxc3wGPVZZfTKs7/7HPGRfFYnTYj17XyONxMb/PmhU9nklTXqiYeVcuad/CdQ08r83bMJYXvv4vypJoNYK0004/N4cP/nxby6bA9x5F0YINBw8MMnfBr+wnmS1JVF99m9XBb0ti/9FEtBQIWd7cPGu9q/BEj//dR3zn9dX/m+pevdl8VelDBQRKIUcf3+OhVYHT+fHc529+INP72bTpnHSOEGtNiHS79pN1WB8BUMbkbblXzP98vbpFz0rfRihw6KNEQgDLpy9zOlzlwd/l+M1RITd2zeze+9O6PbQq50HiB3aUJO1DGxSiDSSntihzTSr8+ULXkWt4uDJsHgAP/C4fWuBQyfns9ApuaxhagyVKOTAM3shTr7kjrXWaM9De7rg4y3v0ROx/frJKiymBeVf2H79bD/+F5gOWskk0cicFq4spXnk2Czm934Lz1PkcjzZD1957il+Xo6+xAWYZgeMWdmoVCmy7NpXqn9SmC6jJ4LiR7aVPOR0MzuzT9+XrH0oAGBEIAp55/gsn99uMrF+LMsD1DLNNfuzXzs4TXnjOJ1bDVTgIyIopXjuxWnWr6uQJKZQriYIJ06do3G7abl6+aL+T9DTNVTZt3IuT+WPiYUaTrUGQxupA8A9+QAVBVy8fJXZs5eYOLDvzkIu2zwCtjy8gZcmd/Pmm0dQpcC2VLs9/uiN13njR9+jl6b4y5SVImDEoLXmjT/9Gf/4d7/A37SeJLmr35AYe2bPZK3YLr7D2qWkM41MKv6FWUDcjSF3AcCgA5/kdpN3Dp+6szC55WBq0Erx3YOT0EvQaDytkE6XXx2rW6DI8gm1VhaAnlK8emAK5ftLO2xa2Yx/Y4B6olJc/pW1f5lrDYY2FO7KmGXTW6X51btzlnBbQVb/woFJ/FoZk8R2ccKA4yfmudlo43s6a5urez5eFvdffnYv4xvWkSTxUu/TM6gna7BxBfE/0siHHbgRFzvk+YEGgMImcZWQI+/Pc/3Ggh2ezKsGMpBM73mMrZsfwvQS+55Dn/NnL3Hu4yuoTDuwrBfIuId9u7ey+8kd0I0H9LKy/wY1WUX1hZwF6n/RyrJ/azi0MdSKINsY8vn8sxscen9+0CvIU2cbYevDG5nevxe6PRTghwE3b97m2MkPB5+d+zmG0Pd55dmnoBsP6OjUMm9qqlac/PEVNDP61x+dxV91SZjve8StNr88Plts4ZTVEPie5sVn9lphiQgoDSbl0NEZjLBsb+GLYejVF6agUsIk6UD+9WiE2lmyHDwF4n+okKsxnG9D6I2M+199TaAIeB5H35uj3e1l8TufFQR49cAk0boqadZNpBTx5rE6jXbnDnNY5HNeObCP8U3jmDhG+Z6t//fVUHeGNoowhh6czoY2AtZctjW0ADAAUUC9fpZLn90ApXLfXT9Ze356N49ueQTu5AEBH1+6ysm5CwWrCttefWTTOC/u3wOLPUv2eRpvqpqdvlUgBGRiz3SmWUww6gBwd1/A4IUB167d5OTp89nCmVwAiBHW1cq8/OyT0OmitUL7HqbR4v8OncwSc5NLRibGEPoerx18GlKDTrCNn6kx6wmKZPOehmZ2ZUtJj9TuX4MQAMr3MO1FjhydWdL5W75Vbl/yS889BdqyeP3u4KF35zMdR/Gd+OJzTxGNV0naMWp7Bb05LH5lS6Awl7twqbPmmv2RmAswqYEo4q1jdVIjhRK4/tq+dnCacH0NE8f2vZci3j85z6fXbmalnsmZ3RiUldsfexhpddFPjw2GNgrx/xr5IKN/fe0AsPK+gIFSwMm5C5z7+Eqh7mB/dz++/RH27NyKdGNb4wc+V658zon6uUxIkgMkrTHG8OhD69m/fy9Igjc1lnEBUrD9m13ZkoK7PPprhgHte3RvNfmfd07eoYpz28OpYUOtwisvTFp9gALfs2Xlr96doyi/bIygleKFyb2wKYInK8Vm9g0QYoc2TjftOQAiDgBfTyamodfj8HvzpMbQS1LinKcXx8RJwnP794DvYYxgFOD5HDpap92NC5aV9iv+xoEp/GcnSNfr7NSOAgxQoJFzHcsBjKD7XzMASNYePvHePFprylFI4HvLPuVSROD7/OjXD7J580Okvdh+WBTwfv0sl6/asjJvTfpl5fQTO3jit/eSBgaVFmUAM/lXK17TQxsYtevjjTEQhpw9f4k//LO/ZsvEOHFqlm0Pi1jX3enFxJ43KCujgBvXb3H8gzPseewRG048b3ltCkI0HvHD7+3ndOuXaK+GkTS//ds2Vv41YrX/mgNAMv19M075q7/8l0xPVySGZyPX42MQ+EhqUGEAnUUOHz3Fj3/4aiHVsWBHvr6/aRc/bR7CiMlXAXoKudGz7d9Qj2T8X/tzAhUEm9avrI8ukGSDpihly8pyxJvHZkmMwVe6sPZyqrSVLf4Yn5oOAZ4Fxr0SwJKG/pl94Wi6//tyPkCc5ieAS540XfLuxRgIA+Y//Ji5s5ds6zm3y6gRYGswzrPlRzAmziGSBFFg7j6zzzgA8G25gkf7Hp3bDd48XC9GCwOJpATa58XydpD03hu63/5tpfbO3nB1r2xxAPi6ZWWccCSTnRfhBHQWKl6tbKekItJ7chH29A+uxPBRx7r/EeP/hx4AfdXxiROzXL3VwPe8XA/d/6L7K1vZEa4jIUV/1bY2QOQhMw1YSEZK/TMyABABFQWc/+gK8+c/KagSUhiETX6N58tbEbGi06/sIqeCqbeselg7AHz7AGAMXuDTvrXA0feK08J9kLxceSwrDuXLu9/XdufPNu/bzL4DQNGpKgXvHK1jpGiX0e7m71R3UdIlYswXgkB2+tfFrr22LRjt3T/UADCpgVKJt0+c5najbYUk5IcBgMejCabD9aQmvpMcLrmyZbZpD38M9EgngMPtAUQgtO3hI5nq2BRQHacINS/ipeoOkGTpC9D2pE+pN0be9Q//QZFiVce0Orx9pPj0UX9G8TuVHXhKs4QR8EBupfb8n5IaWfp3NACgssXUmkPvzZMYY8fICkjPAZ4ub2PCqxKb1LKCaTb9c6Zt7wry9ciyfyNzVGy/zTxTP8vFT69nU0P5X1iAx8MNTEcTGElsZtBv/9azwx+90U8Ahx4Axgg69Ll29QbHPjg7aD3nJIKpGCId8nxlO4hBibL0bzu1V7Z64nKAYTHP0yTtRd55d3aporRAd/C71cfQKiAxJjuzL4YzbQi8ByL+jwQAjABRyKEjdRqdxcH08LKtfvu1X6js5FG/SiIpKtLIXMuOgAcPhvsfEQDY9vDM3AUufnK90PBJP+Q/FIzxSnkLYhK0aNKZ1uC8IBcChoUWFrwwYOHmAoffPV24HOxL01+pbAfP2ONd642RFn+M5oURko1v9WIOH5tdUuotnwj0AbCDUlii90kHdWFxpOVfowkAhb1voBTx1vFZOtlZw3lreIcWDh5iz9hGzKlbqIYZWfn3SF8ZY4xAFHDxo084NX/RCj5NdmL3PR4tNgxMBDUOhNugfgudmGK3fDsAfAu/iO+xuNDivw+dRIBECWbZRxErg/E0ryabYaaNiQoeGYNTBX8768Ew4Of/8O8cmanTS9MC5w0Lvqe5emsBdVUw/oOVANpQ+PjrMlI3gPYSaHeLnyiaUcBUSzyI5o/UtxFBhT66HK64p7Bm19Q4AKx+gyhNUpy5iyOdOQA4cwBw5gDgzAHAmQOAMwcAZw4AzhwAnDkAOHMAcOYA4MwBwAHAvQIHAGcOAM4cAJw5ADh78Oz/AbtwooLHCkC8AAAAAElFTkSuQmCC"};
var LOGO_TINT=["#33405B","#3C4A3A","#55404E","#4A4535","#2F4A4C","#4E3B36","#3A3F55","#45384A"];
function logoTint(s){var h=0;for(var i=0;i<s.length;i++){h=(h*31+s.charCodeAt(i))>>>0;}return LOGO_TINT[h%LOGO_TINT.length];}
function mountLogo(el,slug,mono){
  var sp=el.querySelector("span.lgmono")||el.querySelector("span");
  if(!sp){sp=document.createElement("span");sp.className="lgmono";el.textContent="";el.appendChild(sp);}
  else if(!sp.className){sp.className="lgmono";}
  if(mono){sp.textContent=mono;}
  sp.style.display="";
  el.style.background=logoTint(slug);
  el.style.color="#fff";
  var old=el.querySelector("img");if(old){old.parentNode.removeChild(old);}
  var img=new Image();
  img.alt="";
  img.onload=function(){sp.style.display="none";el.style.background="#fff";var inner=Math.max(16,el.clientWidth-6);var w=Math.min(img.naturalWidth||inner,inner);img.style.width=w+"px";img.style.height="auto";img.style.left="50%";img.style.top="50%";img.style.transform="translate(-50%,-50%)";img.style.padding="0";el.appendChild(img);};
  img.src=(typeof LOGO_DATA!=="undefined"&&LOGO_DATA[slug])||("logos/"+slug+".svg");
}
function paintLogos(){
  var list=document.querySelectorAll("[data-logo]");
  for(var i=0;i<list.length;i++){
    var el=list[i],v=(el.getAttribute("data-logo")||"").split("|");
    if(!v[0]||el.getAttribute("data-logo-slug")===v[0])continue;
    el.setAttribute("data-logo-slug",v[0]);
    mountLogo(el,v[0],(v[1]||"").toUpperCase());
  }
}

var _rs = document.getElementById("region-sel");
if (_rs) { _rs.addEventListener("change", function(e){ setRegion(e.target.value); }); }
var _mc = document.getElementById("mapcat-sel");
if (_mc) { _mc.addEventListener("change", function(e){ setMapCat(e.target.value); }); }
var _my = document.getElementById("mapyear-sel");
if (_my) { _my.addEventListener("change", function(e){ setMapYear(parseInt(e.target.value, 10)); }); }
initPins();
buildEmpty();
/* แผนที่ดึงข้อมูลจากส่วนตารางอันดับ จึงต้องบูตหลังส่วนนั้นประกาศตัวแปรครบ — เรียก mapBoot() ท้ายสคริปต์ */
function mapBoot(){
  if (typeof rkRows !== "function") { return; }
  buildMapData();
  buildMapCatSelect();
  buildMapYearSelect();
  setRegion('all');
  var list = mapIsos();
  if (list.length) { select(TOP[list.indexOf("AU") >= 0 ? "AU" : list[0]]); }
  closeCard();
  paintLogos();
}
(function(){
  var card = document.getElementById("card");
  if (card && !card.querySelector(".card-close")) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "card-close"; b.innerHTML = "&times;";
    b.setAttribute("aria-label", "ปิดการ์ดโบรกเกอร์");
    b.addEventListener("click", closeCard);
    card.appendChild(b);
  }
  var stage = document.getElementById("map-stage");
  if (stage && !document.getElementById("map-hint")) {
    var h = document.createElement("div");
    h.id = "map-hint"; h.className = "map-hint";
    h.textContent = "คลิกหมุดประเทศเพื่อดูโบรกเกอร์อันดับหนึ่ง";
    stage.appendChild(h);
  }
  closeCard();
  document.addEventListener("keydown", function(e){ if (e.key === "Escape" && cardOpen) { closeCard(); } });
})();

/* ── ช่องค้นหาในการ์ดลอย: ค้นชื่อโบรก หรือเลือกประเภทสินทรัพย์ ── */
var HS_TYPES = [["all","ทั้งหมด"],["fx","Forex / CFD"],["crypto","คริปโต"],["fund","กองทุน"]];
var hsType = "all", hsQ = "";
function hsMembers(t){
  if (t === "all") { return Object.keys(B); }
  var m = (typeof CAT_MEMBERS !== "undefined" && CAT_MEMBERS[t]) ? CAT_MEMBERS[t] : [];
  return Object.keys(B).filter(function(id){ return m.indexOf(B[id].id) >= 0; });
}
function hsRender(){
  document.getElementById("hs-types").innerHTML = HS_TYPES.map(function(t){
    return '<button type="button" class="hs-type" data-hstype="' + t[0] + '" aria-pressed="' + (t[0] === hsType) + '">' + t[1] + '</button>';
  }).join("");
  var q = hsQ.trim().toLowerCase(), active = !!q || hsType !== "all";
  var detail = document.getElementById("card-detail"), res = document.getElementById("card-results");
  detail.hidden = active; res.hidden = !active;
  if (!active) { return; }
  var list = hsMembers(hsType).filter(function(id){ return !q || B[id].n.toLowerCase().indexOf(q) >= 0; });
  list.sort(function(a, b){ return B[b].stars - B[a].stars || B[a].n.localeCompare(B[b].n); });
  if (!list.length) {
    res.innerHTML = '<div class="hs-bar"><span class="hs-count">ไม่พบผลลัพธ์</span>' +
      '<button type="button" class="hs-close" data-hsclose="1">&times; ปิดการค้นหา</button></div>' +
      '<p class="hs-empty">ไม่พบโบรกเกอร์ที่ตรงกับเงื่อนไขนี้ในทะเบียน — การไม่อยู่ในทะเบียนไม่ได้แปลว่าไม่ดี แปลว่าเรายังไม่ได้ตรวจ</p>';
    return;
  }
  res.innerHTML = '<div class="hs-bar"><span class="hs-count">พบ ' + list.length + ' ราย' +
    (hsType === "all" ? "" : " ในหมวด" + HS_TYPES.filter(function(t){ return t[0] === hsType; })[0][1]) + '</span>' +
    '<button type="button" class="hs-close" data-hsclose="1">&times; ปิดการค้นหา</button></div>' +
    list.map(function(id){
      var b = B[id], slug = (typeof LOGO_SLUG !== "undefined" && LOGO_SLUG[b.id]) ? LOGO_SLUG[b.id] : b.id;
      return '<button type="button" class="hs-hit" data-hspick="' + id + '">' +
        '<span data-logo="' + slug + '|' + b.mono + '" style="width:30px;height:30px;border-radius:7px;' +
        'display:inline-flex;align-items:center;justify-content:center;font-family:IBM Plex Sans,sans-serif;' +
        'font-size:11px;font-weight:700;color:#fff;flex-shrink:0;"></span>' +
        '<span><b>' + b.n + '</b><span class="sub">' + b.c + ' · ' + b.reg + '</span></span>' +
        '<span class="stars">' + starHTML(b.stars, 12) + '</span></button>';
    }).join("");
  paintLogos();
}
document.getElementById("hs-q").addEventListener("input", function(e){ hsQ = e.target.value; hsRender();
/* ── ซูมและเลื่อนแผนที่ — หมุดขยับตามพิกัดจริง แต่ขนาดหมุดคงเดิมเสมอ ── */
 });
document.addEventListener("click", function(ev){
  if (ev.target.closest("[data-hsclose]")) {
    hsQ = ""; hsType = "all";
    document.getElementById("hs-q").value = "";
    hsRender();
    return;
  }
  var t = ev.target.closest("[data-hstype]");
  if (t) { hsType = (hsType === t.dataset.hstype && hsType !== "all") ? "all" : t.dataset.hstype; hsRender(); return; }
  var p = ev.target.closest("[data-hspick]");
  if (p) {
    var id = p.dataset.hspick;
    if ((REGION[region] || []).indexOf(B[id].iso) < 0) { setRegion("all"); }
    select(id);
    hsQ = ""; hsType = "all";
    document.getElementById("hs-q").value = "";
    hsRender();
  }
});
document.addEventListener("keydown", function(ev){
  if (ev.key === "Escape" && (hsQ || hsType !== "all")) {
    hsQ = ""; hsType = "all"; document.getElementById("hs-q").value = ""; hsRender();
  }
});
hsRender();

/* ── ตารางอันดับรายประเทศ + เทียบตัวต่อตัว ─────────────────────────
   คะแนนย่อยเป็นข้อมูลสมมติ · คะแนนรวมคำนวณจากค่าเฉลี่ยสี่ด้านเสมอ    */
/* ── ตารางอันดับรายประเทศ + กราฟ + เทียบตัวต่อตัว ────────────────────
   ตัวเลขทุกตัวในส่วนนี้เป็นข้อมูลสมมติที่สร้างขึ้นเพื่อทดสอบการจัดวาง
   สร้างแบบคงที่จากชื่อ (ค่าเดิมทุกครั้งที่เปิด) ไม่ใช่สุ่มใหม่ทุกรอบ   */
var DIMS = [["cost","ต้นทุน"],["platform","แพลตฟอร์ม"],["service","บริการ"],["funding","ฝาก–ถอน"]];
var YEARS3 = [2024, 2025, 2026];
var YEAR_FILL = {2024:"#F7CFCB", 2025:"#E8877F", 2026:"#D92D20"};

var CATS = {
  fx:       {n:"Forex / CFD", metric:"สเปรดเฉลี่ย", unit:"pip", base:0.55, span:1.25,
             parts:["สเปรด","คอมมิชชัน","สวอปข้ามคืน"], costUnit:"USD ต่อ 1 ล็อต",
             note:"ต้นทุนต่อการเทรด 1 ล็อตมาตรฐาน"},
  futures:  {n:"ฟิวเจอร์ส", metric:"ค่าคอมมิชชันต่อสัญญา", unit:"USD", base:0.85, span:3.20,
             parts:["คอมมิชชันโบรกเกอร์","ค่าธรรมเนียมตลาด","ค่าข้อมูลราคา"], costUnit:"USD ต่อ 1 สัญญา ไป-กลับ",
             note:"ต้นทุนต่อการซื้อขาย 1 สัญญาไป-กลับ"},
  stocks:   {n:"หุ้น", metric:"ค่าธรรมเนียมซื้อขาย", unit:"%", base:0.05, span:0.42,
             parts:["ค่าธรรมเนียมโบรกเกอร์","ค่าธรรมเนียมตลาดและหน่วยงานกำกับ","ค่าแปลงสกุลเงิน"],
             costUnit:"USD ต่อการซื้อขาย 10,000 USD", note:"ต้นทุนต่อการซื้อขายมูลค่า 10,000 USD"},
  crypto:   {n:"คริปโต (CFD)", metric:"สเปรดเฉลี่ย", unit:"%", base:0.14, span:0.72,
             parts:["สเปรด","ค่าธรรมเนียมเทรด","ค่าถอน"], costUnit:"USD ต่อการเทรด 1,000 USD",
             note:"ต้นทุนต่อการเทรดมูลค่า 1,000 USD"},
  exchange: {n:"Exchange (ซื้อขายเหรียญจริง)", metric:"ค่าธรรมเนียมฝั่ง Taker", unit:"%", base:0.06, span:0.34,
             parts:["ค่าธรรมเนียม Taker","ค่าธรรมเนียม Maker","ค่าถอนออนเชน"], costUnit:"USD ต่อการเทรด 1,000 USD",
             note:"ต้นทุนต่อการเทรดมูลค่า 1,000 USD"},
  fund:     {n:"กองทุน", metric:"ค่าธรรมเนียมรายปี", unit:"%", base:0.55, span:1.30,
             parts:["ค่าธรรมเนียมจัดการ","ค่าธรรมเนียมแรกเข้า","ค่าธรรมเนียมขายคืน"], costUnit:"% ต่อปี",
             note:"ต้นทุนรวมที่ผู้ถือหน่วยจ่ายจริงต่อปี"}
};
var CAT_ORDER = ["fx","futures","stocks","crypto","exchange","fund"];
/* ชุดตั้งต้นหมวด Forex/CFD — [id, ดาว, ต้นทุน, แพลตฟอร์ม, บริการ, ฝาก–ถอน] (ข้อมูลสมมติ) */
var ROSTER = {
  AU: [["icm",3,9.9,9.8,9.6,9.9],["pep",3,9.7,9.7,9.5,9.5],["axi",1,8.6,8.4,8.3,8.3],["fpm",1,8.4,8.2,8.0,8.2]],
  CY: [["exness",3,9.7,9.4,9.3,9.6],["xm",2,9.1,9.0,9.2,8.7],["tickmill",2,9.0,8.7,8.8,8.7],["hfm",1,8.5,8.2,8.3,8.2]],
  GB: [["tickmill",2,9.5,9.2,9.3,9.2],["ig",2,8.8,9.5,9.2,8.9],["pep",2,9.1,8.9,8.8,8.8],["oanda",1,8.4,8.8,8.7,8.5]],
  SG: [["ig",2,8.9,9.4,9.1,9.0],["icm",2,9.2,8.9,8.7,8.8],["exness",2,8.9,8.6,8.6,8.7],["eig",1,8.3,8.2,8.1,8.2]],
  US: [["oanda",1,8.7,9.1,8.9,8.9],["ig",1,8.3,8.9,8.7,8.5]],
  AE: [["equiti",1,8.6,8.7,8.9,8.6],["exness",1,8.7,8.5,8.4,8.4],["hfm",1,8.3,8.1,8.2,8.2],["xm",1,8.1,8.0,8.0,7.9]],
  ZA: [["hfm",1,8.7,8.5,8.6,8.6],["exness",1,8.6,8.3,8.3,8.4],["xm",1,8.2,8.1,8.0,8.1],["tickmill",1,8.0,7.9,7.8,7.9]]
};
var META = {
  /* ชื่อทั้งหมดเป็นผู้ให้บริการที่มีอยู่จริง แต่ คะแนน/ดาว/ต้นทุนทุกตัวเป็นข้อมูลสมมติ
     หน่วยกำกับที่ระบุคือหน่วยกำกับหลักของแต่ละราย ยังไม่ได้แยกรายประเทศ — ดูเรื่องค้างข้อ 11 ใน STATE.md */
  icm:{n:"IC Markets",mono:"IC",slug:"ic-markets",reg:"ASIC Regulated"},
  pep:{n:"Pepperstone",mono:"PS",slug:"pepperstone",reg:"ASIC Regulated"},
  exness:{n:"Exness",mono:"EX",slug:"exness",reg:"CySEC Regulated"},
  xm:{n:"XM",mono:"XM",slug:"xm",reg:"CySEC Regulated"},
  tickmill:{n:"Tickmill",mono:"TM",slug:"tickmill",reg:"FCA Regulated"},
  ig:{n:"IG",mono:"IG",slug:"ig",reg:"MAS / FCA Regulated"},
  oanda:{n:"OANDA",mono:"OA",slug:"oanda",reg:"NFA / CFTC Regulated"},
  equiti:{n:"Equiti",mono:"EQ",slug:"equiti",reg:"DFSA Regulated"},
  hfm:{n:"HFM",mono:"HF",slug:"hfm",reg:"FSCA Regulated"},
  axi:{n:"Axi",mono:"AX",slug:"axi",reg:"ASIC Regulated"},
  fpm:{n:"FP Markets",mono:"FP",slug:"fp-markets",reg:"ASIC Regulated"},
  eig:{n:"Eightcap",mono:"EC",slug:"eightcap",reg:"ASIC Regulated"},
  saxo:{n:"Saxo Bank",mono:"SX",slug:"saxo-bank",reg:"DFSA (DK) / FCA Regulated"},
  cmc:{n:"CMC Markets",mono:"CM",slug:"cmc-markets",reg:"FCA / ASIC Regulated"},
  fxpro:{n:"FxPro",mono:"FX",slug:"fxpro",reg:"FCA / CySEC Regulated"},
  admirals:{n:"Admirals",mono:"AD",slug:"admirals",reg:"FCA / CySEC Regulated"},
  think:{n:"ThinkMarkets",mono:"TK",slug:"thinkmarkets",reg:"ASIC / FCA Regulated"},
  vantage:{n:"Vantage",mono:"VT",slug:"vantage",reg:"ASIC Regulated"},
  fxtm:{n:"FXTM",mono:"FT",slug:"fxtm",reg:"CySEC / FCA Regulated"},
  capital:{n:"Capital.com",mono:"CP",slug:"capital-com",reg:"FCA / CySEC Regulated"},
  plus500:{n:"Plus500",mono:"P5",slug:"plus500",reg:"FCA / ASIC Regulated"},
  avatrade:{n:"AvaTrade",mono:"AV",slug:"avatrade",reg:"CBI / ASIC Regulated"},
  forexcom:{n:"FOREX.com",mono:"FC",slug:"forex-com",reg:"NFA / CFTC Regulated"},
  blackbull:{n:"BlackBull Markets",mono:"BB",slug:"blackbull-markets",reg:"FMA (NZ) Regulated"},
  fusion:{n:"Fusion Markets",mono:"FM",slug:"fusion-markets",reg:"ASIC Regulated"},
  tastyfx:{n:"tastyfx",mono:"TX",slug:"tastyfx",reg:"NFA / CFTC Regulated"},
  ibkr:{n:"Interactive Brokers",mono:"IB",slug:"interactive-brokers",reg:"SEC / FINRA / NFA Regulated"},
  ninja:{n:"NinjaTrader",mono:"NT",slug:"ninjatrader",reg:"NFA / CFTC Regulated"},
  tradovate:{n:"Tradovate",mono:"TV",slug:"tradovate",reg:"NFA / CFTC Regulated"},
  ampf:{n:"AMP Futures",mono:"AM",slug:"amp-futures",reg:"NFA / CFTC Regulated"},
  optimus:{n:"Optimus Futures",mono:"OF",slug:"optimus-futures",reg:"NFA / CFTC Regulated"},
  tradestation:{n:"TradeStation",mono:"TS",slug:"tradestation",reg:"SEC / FINRA / NFA Regulated"},
  edgeclear:{n:"EdgeClear",mono:"ED",slug:"edgeclear",reg:"NFA / CFTC Regulated"},
  stage5:{n:"Stage 5 Trading",mono:"S5",slug:"stage-5-trading",reg:"NFA / CFTC Regulated"},
  schwab:{n:"Charles Schwab",mono:"CS",slug:"charles-schwab",reg:"SEC / FINRA Regulated"},
  fidelity:{n:"Fidelity",mono:"FD",slug:"fidelity",reg:"SEC / FINRA Regulated"},
  etoro:{n:"eToro",mono:"ET",slug:"etoro",reg:"FCA / CySEC / ASIC Regulated"},
  robinhood:{n:"Robinhood",mono:"RH",slug:"robinhood",reg:"SEC / FINRA Regulated"},
  webull:{n:"Webull",mono:"WB",slug:"webull",reg:"SEC / FINRA Regulated"},
  t212:{n:"Trading 212",mono:"T2",slug:"trading-212",reg:"FCA Regulated"},
  degiro:{n:"DEGIRO",mono:"DG",slug:"degiro",reg:"AFM / BaFin Regulated"},
  tiger:{n:"Tiger Brokers",mono:"TG",slug:"tiger-brokers",reg:"MAS / SEC Regulated"},
  moomoo:{n:"moomoo",mono:"MO",slug:"moomoo",reg:"MAS / SEC Regulated"},
  binance:{n:"Binance",mono:"BN",slug:"binance",reg:"VARA (Dubai) / AMF Registered"},
  coinbase:{n:"Coinbase",mono:"CB",slug:"coinbase",reg:"SEC / FCA Registered"},
  kraken:{n:"Kraken",mono:"KR",slug:"kraken",reg:"FinCEN / FCA Registered"},
  okx:{n:"OKX",mono:"OK",slug:"okx",reg:"VARA (Dubai) Regulated"},
  bybit:{n:"Bybit",mono:"BY",slug:"bybit",reg:"VARA (Dubai) Regulated"},
  kucoin:{n:"KuCoin",mono:"KC",slug:"kucoin",reg:"FinCEN Registered"},
  bitget:{n:"Bitget",mono:"BG",slug:"bitget",reg:"FinCEN Registered"},
  gateio:{n:"Gate.io",mono:"GT",slug:"gate-io",reg:"FinCEN Registered"},
  bitstamp:{n:"Bitstamp",mono:"BS",slug:"bitstamp",reg:"CSSF (LU) Regulated"},
  cryptocom:{n:"Crypto.com",mono:"CR",slug:"crypto-com",reg:"VARA / MAS Regulated"},
  gemini:{n:"Gemini",mono:"GM",slug:"gemini",reg:"NYDFS Regulated"},
  bitfinex:{n:"Bitfinex",mono:"BF",slug:"bitfinex",reg:"FinCEN Registered"},
  vanguard:{n:"Vanguard",mono:"VG",slug:"vanguard",reg:"SEC / FCA Regulated"},
  hl:{n:"Hargreaves Lansdown",mono:"HL",slug:"hargreaves-lansdown",reg:"FCA Regulated"},
  ajbell:{n:"AJ Bell",mono:"AJ",slug:"aj-bell",reg:"FCA Regulated"},
  ii:{n:"interactive investor",mono:"II",slug:"interactive-investor",reg:"FCA Regulated"},
  fineco:{n:"FinecoBank",mono:"FN",slug:"finecobank",reg:"CONSOB / FCA Regulated"},
  allfunds:{n:"Allfunds",mono:"AF",slug:"allfunds",reg:"CNMV Regulated"}
};

/* ค่าตั้งต้นรายเดียวต่อโบรก [ดาว, ต้นทุน, แพลตฟอร์ม, บริการ, ฝาก–ถอน]
   ใช้ตอนที่โบรกนั้นไม่มีแถวที่เขียนไว้ใน ROSTER ของประเทศนั้น — ข้อมูลสมมติทั้งหมด */
var BASE = {
  icm:[3,9.6,9.5,9.3,9.5], pep:[3,9.4,9.3,9.2,9.2], exness:[3,9.3,9.0,8.9,9.1],
  xm:[2,8.7,8.6,8.6,8.4], tickmill:[2,9.0,8.7,8.7,8.7], ig:[2,8.8,9.3,9.0,8.9],
  oanda:[1,8.5,8.9,8.8,8.7], equiti:[1,8.5,8.6,8.7,8.5], hfm:[1,8.4,8.3,8.4,8.4],
  axi:[1,8.5,8.3,8.2,8.2], fpm:[1,8.4,8.2,8.1,8.2], eig:[1,8.3,8.2,8.1,8.2],
  saxo:[3,8.4,9.6,9.2,9.0], cmc:[3,9.0,9.4,9.1,9.0], fxpro:[2,8.8,8.9,8.8,8.7],
  admirals:[2,8.7,8.7,8.8,8.6], think:[2,8.8,8.6,8.5,8.5], vantage:[2,8.9,8.7,8.6,8.6],
  fxtm:[2,8.6,8.5,8.6,8.5], capital:[2,8.7,9.0,8.7,8.7], plus500:[2,8.5,8.9,8.4,8.6],
  avatrade:[2,8.4,8.6,8.5,8.5], forexcom:[1,8.5,8.8,8.6,8.5], blackbull:[1,8.8,8.4,8.3,8.3],
  fusion:[1,9.1,8.2,8.2,8.1], tastyfx:[1,8.4,8.7,8.5,8.4],
  ibkr:[3,9.5,9.4,8.7,9.1], ninja:[2,9.0,9.1,8.6,8.6], tradovate:[2,8.9,8.9,8.5,8.5],
  ampf:[1,9.0,8.4,8.6,8.4], optimus:[1,8.8,8.3,8.7,8.3], tradestation:[2,8.6,9.0,8.5,8.6],
  edgeclear:[1,8.7,8.3,8.6,8.2], stage5:[1,8.6,8.2,8.5,8.2],
  schwab:[3,9.2,9.0,9.1,9.0], fidelity:[3,9.3,8.9,9.2,9.0], etoro:[2,8.6,9.1,8.5,8.6],
  robinhood:[1,9.0,8.8,8.0,8.4], webull:[1,8.9,8.7,8.1,8.3], t212:[2,9.1,8.7,8.3,8.5],
  degiro:[2,8.9,8.4,8.2,8.4], tiger:[1,8.8,8.6,8.3,8.4], moomoo:[1,8.8,8.8,8.3,8.5],
  binance:[2,9.4,9.2,8.4,8.8], coinbase:[3,8.3,9.0,8.9,8.9], kraken:[3,8.9,8.8,8.8,8.7],
  okx:[2,9.2,8.9,8.3,8.6], bybit:[2,9.1,8.8,8.2,8.5], kucoin:[1,8.9,8.5,7.9,8.2],
  bitget:[1,9.0,8.6,8.0,8.3], gateio:[1,8.8,8.4,7.9,8.1], bitstamp:[2,8.4,8.3,8.6,8.5],
  cryptocom:[2,8.7,8.7,8.4,8.6], gemini:[2,8.2,8.5,8.6,8.4], bitfinex:[1,8.8,8.4,7.8,8.0],
  vanguard:[3,9.5,8.5,8.8,8.7], hl:[2,8.2,8.8,9.0,8.7], ajbell:[2,8.8,8.6,8.7,8.6],
  ii:[2,8.6,8.5,8.6,8.5], fineco:[2,8.7,8.6,8.5,8.6], allfunds:[1,8.5,8.4,8.4,8.4]
};

/* รายชื่อที่เปิดให้บริการในแต่ละหมวด — หมวดละอย่างน้อย 13 ราย
   เพื่อให้หยิบมาแสดงประเทศละ 10 รายได้ โดยแต่ละประเทศได้ชุดไม่ซ้ำกัน */
var CAT_MEMBERS = {
  fx:       ["icm","pep","exness","xm","tickmill","ig","oanda","equiti","hfm","axi","fpm","eig",
             "saxo","cmc","fxpro","admirals","think","vantage","fxtm","capital","plus500",
             "avatrade","forexcom","blackbull","fusion","tastyfx"],
  futures:  ["ibkr","ninja","tradovate","ampf","optimus","tradestation","edgeclear","stage5",
             "ig","saxo","cmc","tickmill","plus500","oanda"],
  stocks:   ["ibkr","schwab","fidelity","etoro","robinhood","webull","t212","degiro","tiger",
             "moomoo","saxo","ig","xm","pep","capital"],
  crypto:   ["etoro","plus500","pep","ig","exness","xm","capital","vantage","eig","avatrade",
             "axi","hfm","icm","admirals","fxpro"],
  exchange: ["binance","coinbase","kraken","okx","bybit","kucoin","bitget","gateio","bitstamp",
             "cryptocom","gemini","bitfinex","etoro"],
  fund:     ["vanguard","hl","ajbell","ii","fineco","allfunds","schwab","fidelity","ibkr",
             "saxo","degiro","t212","ig"]
};

function seed(str){
  var h = 2166136261;
  for (var i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619); }
  return (h >>> 0) / 4294967296;
}
function metricOf(cat, iso, id, year){
  var c = CATS[cat];
  var v0 = c.base + seed(cat + iso + id) * c.span;
  var dr = seed(id + cat + "d");
  /* ราวหนึ่งในสี่ของรายชื่อ ต้นทุนแย่ลงตามปี เพื่อให้เห็นทั้งสองสถานะ */
  var drift = (dr > 0.74 ? -0.6 : 1) * (0.04 + dr * 0.16) * c.span;
  var v = v0 - drift * (year - 2024);
  return Math.max(c.base * 0.6, Math.round(v * 100) / 100);
}
function costParts(cat, iso, id){ return costPartsYear(cat, iso, id, 2026); }

/* ปรับคะแนน 4 ด้านตามหมวด โดยยึดชุด Forex เป็นฐาน */
function dimShift(cat, id, iso){
  if (cat === "fx") { return 0; }
  return Math.round((seed(cat + id + iso + "sh") * 1.2 - 0.6) * 10) / 10;
}
/* จำนวนรายชื่อต่อหมวดต่อประเทศ — ตรึงไว้ที่ 10 เพื่อให้เห็นตารางเต็ม */
var ROWS_PER_CAT = 10;
/* สร้างแถวของโบรกที่ไม่ได้เขียนไว้ใน ROSTER ของประเทศนั้น
   ขยับจากค่าตั้งต้นด้วยค่าคงที่หาจากชื่อ เปิดคนละเครื่องจึงเห็นเลขเดิมเสมอ */
function baseRow(id, iso){
  var b = BASE[id] || [1, 8.2, 8.2, 8.2, 8.2];
  var j = function(v, k){
    var d = Math.round((seed(id + iso + k) * 1.6 - 0.8) * 10) / 10;
    return Math.max(6.6, Math.min(9.9, Math.round((v + d) * 10) / 10));
  };
  return [id, b[0], j(b[1], "c"), j(b[2], "p"), j(b[3], "s"), j(b[4], "f")];
}
function rosterFor(cat, iso){
  var members = CAT_MEMBERS[cat] || [];
  var authored = (ROSTER[iso] || []).filter(function(r){ return members.indexOf(r[0]) >= 0; });
  var have = authored.map(function(r){ return r[0]; });
  var rest = members.filter(function(id){ return have.indexOf(id) < 0; })
    .sort(function(a, b){ return seed(cat + iso + a) - seed(cat + iso + b); });
  var out = authored.slice(0, ROWS_PER_CAT);
  for (var i = 0; i < rest.length && out.length < ROWS_PER_CAT; i++) {
    out.push(baseRow(rest[i], iso));
  }
  return out;
}
/* คะแนนรวมย้อนหลัง = ค่าเฉลี่ยของสี่ด้านในปีนั้นจริง ๆ ไม่ได้สร้างแยก */
function scoreSeriesFromDims(dimSer){
  return YEARS3.map(function(y, i){
    var sum = DIMS.reduce(function(a, d){ return a + dimSer[d[0]][i]; }, 0);
    return Math.round(sum / DIMS.length * 10) / 10;
  });
}
function scoreSeriesUnused(cat, iso, id, now){
  var r = seed(id + iso + cat + "sc");
  var dir = r > 0.66 ? -1 : 1;
  var step = 0.05 + r * 0.28;
  /* บีบก้าวไม่ให้ปีเก่าชนเพดาน 10 หรือพื้น 6 จนได้ค่าซ้ำกันสองปี */
  var room = dir < 0 ? (9.9 - now) : (now - 6.2);
  step = Math.max(0.05, Math.min(step, room / 2));
  return YEARS3.map(function(y){
    var v = now - dir * step * (2026 - y);
    return Math.round(Math.max(6.0, Math.min(10, v)) * 10) / 10;
  });
}
/* ส่วนประกอบต้นทุนของปีใดปีหนึ่ง — ส่วนที่ผูกกับสเปรดขยับตามปี ส่วนอื่นคงที่ */
function costPartsYear(cat, iso, id, year){
  var m = metricOf(cat, iso, id, year), r = seed(id + iso + cat + "c"), r2 = seed(id + cat + "c2");
  var R1 = function(v){ return Math.round(v*10)/10; }, R2 = function(v){ return Math.round(v*100)/100; };
  if (cat === "fx")       { return [R1(m*10), R1(3.2 + r*3.6), R1(1.8 + r2*6.4)]; }
  if (cat === "futures")  { return [R1(m), R1(1.1 + r*1.8), R1(0.4 + r2*1.6)]; }
  if (cat === "stocks")   { return [R1(m*100), R1(0.6 + r*1.9), R1(0.5 + r2*2.6)]; }
  if (cat === "crypto")   { return [R1(m*10), R1(0.9 + r*2.9), R1(0.4 + r2*2.4)]; }
  if (cat === "exchange") { return [R1(m*10), R1(m*10*(0.45 + r*0.3)), R1(0.6 + r2*3.2)]; }
  return [m, R2(0.10 + r*0.75), R2(r2*0.45)];
}
function costSeries(cat, iso, id){
  return YEARS3.map(function(y){
    var p = costPartsYear(cat, iso, id, y);
    return Math.round((p[0] + p[1] + p[2]) * 100) / 100;
  });
}
function rkRows(cat, iso, year){
  var yi = YEARS3.indexOf(year || 2026); if (yi < 0) { yi = YEARS3.length - 1; }
  var sh = function(v, d){ return Math.max(6.5, Math.min(10, Math.round((v + d) * 10) / 10)); };
  return rosterFor(cat, iso).map(function(r){
    var d = dimShift(cat, r[0], iso);
    var vals = {cost:sh(r[2],d), platform:sh(r[3],d), service:sh(r[4],d), funding:sh(r[5],d)};
    var total = (vals.cost + vals.platform + vals.service + vals.funding) / 4;
    var stars = cat === "fx" ? r[1] : Math.max(1, r[1] - (seed(cat + r[0] + iso + "st") > 0.62 ? 1 : 0));
    var dimSer = {};
    DIMS.forEach(function(d){ dimSer[d[0]] = dimSeries(cat, iso, r[0], d[0], vals[d[0]]); });
    var scoreSer = scoreSeriesFromDims(dimSer);
    var yr = YEARS3[yi];
    var valsY = {};
    DIMS.forEach(function(d){ valsY[d[0]] = dimSer[d[0]][yi]; });
    var mSer = YEARS3.map(function(y){ return metricOf(cat, iso, r[0], y); });
    var cSer = costSeries(cat, iso, r[0]);
    var cut = function(a){ return a.slice(0, yi + 1); };
    return {id:r[0], stars:stars, vals:valsY, total:scoreSer[yi], year:yr,
            metric:mSer[yi],
            series:cut(mSer),
            dimSer:(function(){ var o = {}; DIMS.forEach(function(d){ o[d[0]] = cut(dimSer[d[0]]); }); return o; })(),
            scoreSeries:cut(scoreSer),
            costSeries:cut(cSer),
            parts:costPartsYear(cat, iso, r[0], yr)};
  }).sort(function(a,b){ return b.total - a.total; });
}
function bestPerDim(rows){
  var best = {};
  DIMS.forEach(function(d){ best[d[0]] = Math.max.apply(null, rows.map(function(r){ return r.vals[d[0]]; })); });
  return best;
}
var rkCat = "fx", rkIso = "AU", cmpA = null, cmpB = null;

var rkYear = 2026, pkYear = 2026;
function yearOptions(sel, cur){
  return YEARS3.slice().reverse().map(function(y){
    return '<option value="' + y + '"' + (y === cur ? " selected" : "") + '>' + y + '</option>';
  }).join("");
}
function buildYearSelects(){
  var a = document.getElementById("rk-year");
  if (a) { a.innerHTML = yearOptions("rk", rkYear); }
}
function rkCatTabs(){
  var sel = document.getElementById("rk-cat-sel");
  sel.innerHTML = CAT_ORDER.map(function(k){
    return '<option value="' + k + '"' + (k === rkCat ? " selected" : "") + '>' + CATS[k].n + '</option>';
  }).join("");
}
function rkTabs(){
  var sel = document.getElementById("rk-iso-sel");
  sel.innerHTML = ["AU","CY","GB","SG","US","AE","ZA"].map(function(iso){
    var n = rosterFor(rkCat, iso).length;
    return '<option value="' + iso + '"' + (iso === rkIso ? " selected" : "") + (n ? "" : " disabled") + '>' +
      CNAME[iso] + (n ? " (" + n + " ราย)" : " — ยังไม่มีในหมวดนี้") + '</option>';
  }).join("");
  var open = ["AU","CY","GB","SG","US","AE","ZA"].filter(function(i){ return rosterFor(rkCat, i).length; }).length;
  document.getElementById("rk-picknote").textContent =
    "หมวด" + CATS[rkCat].n + " เปิดตรวจแล้ว " + open + " ประเทศ จากทั้งหมด 7 ประเทศในทะเบียน";
}
function logoSpan(m, px, fs){
  return '<span data-logo="' + m.slug + '|' + m.mono + '" style="width:' + px + 'px;height:' + px + 'px;' +
    'border-radius:' + Math.round(px/4) + 'px;display:inline-flex;align-items:center;justify-content:center;' +
    'font-family:IBM Plex Sans,sans-serif;font-size:' + fs + 'px;font-weight:700;color:#fff;flex-shrink:0;"></span>';
}

/* ── กราฟแท่งแนวนอน จัดกลุ่มรายปี ── */
function chartSeries(rows, cat){
  if (!rows.length) { return '<p style="font-size:13.5px;color:#667085;margin:0;">ยังไม่มีข้อมูลในหมวดนี้</p>'; }
  var c = CATS[cat], LW = 116, PAD = 8, RW = 400, rowH = 21, gap = 5, blockH = YEARS3.length * rowH + 18;
  var H = rows.length * blockH + 26;
  var max = Math.max.apply(null, rows.map(function(r){ return Math.max.apply(null, r.series); })) * 1.18;
  var g = "";
  for (var t = 0; t <= 4; t++) {
    var x = LW + PAD + (RW * t / 4);
    g += '<line x1="' + x + '" y1="16" x2="' + x + '" y2="' + (H - 10) + '" stroke="#F0F2F5" stroke-width="1"></line>' +
         '<text x="' + x + '" y="10" font-size="9.5" fill="#98A2B3" text-anchor="middle">' +
         (Math.round(max * t / 4 * 100) / 100) + '</text>';
  }
  rows.forEach(function(r, i){
    var top = 26 + i * blockH;
    g += '<text x="' + LW + '" y="' + (top + 13) + '" font-size="12.5" font-weight="600" fill="#101828" text-anchor="end">' +
         META[r.id].n + '</text>';
    r.series.forEach(function(v, j){
      var y = top + j * rowH, w = Math.max(2, RW * v / max);
      g += '<rect x="' + (LW + PAD) + '" y="' + y + '" width="' + w + '" height="' + (rowH - gap) + '" rx="2.5" fill="' + YEAR_FILL[YEARS3[j]] + '"></rect>' +
           '<text x="' + (LW + PAD + w + 7) + '" y="' + (y + rowH - gap - 4) + '" font-size="10.5" fill="#475467">' +
           v.toFixed(2) + '</text>';
    });
  });
  return '<svg viewBox="0 0 ' + (LW + PAD + RW + 46) + ' ' + H + '" role="img" aria-label="กราฟ' + c.metric +
    'ย้อนหลังสามปี">' + g + '</svg>';
}
/* ── กราฟแท่งซ้อน แยกส่วนประกอบต้นทุน ── */
function chartCost(rows, cat){
  if (!rows.length) { return '<p style="font-size:13.5px;color:#667085;margin:0;">ยังไม่มีข้อมูลในหมวดนี้</p>'; }
  var c = CATS[cat], LW = 116, PAD = 8, RW = 380, rowH = 34, barH = 18;
  var H = rows.length * rowH + 22;
  var tot = rows.map(function(r){ return r.parts.reduce(function(a,b){ return a+b; }, 0); });
  var max = Math.max.apply(null, tot) * 1.22;
  var fills = [YEAR_FILL[2026], YEAR_FILL[2025], YEAR_FILL[2024]];
  var g = "";
  rows.forEach(function(r, i){
    var y = 14 + i * rowH, x = LW + PAD, sum = 0;
    g += '<text x="' + LW + '" y="' + (y + barH - 4) + '" font-size="12.5" font-weight="600" fill="#101828" text-anchor="end">' +
         META[r.id].n + '</text>';
    r.parts.forEach(function(v, j){
      var w = Math.max(1.5, RW * v / max);
      g += '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + barH + '" fill="' + fills[j] + '"></rect>';
      x += w; sum += v;
    });
    g += '<text x="' + (x + 8) + '" y="' + (y + barH - 4) + '" font-size="11.5" font-weight="600" fill="#101828">' +
         (Math.round(sum * 100) / 100) + '</text>';
  });
  return '<svg viewBox="0 0 ' + (LW + PAD + RW + 62) + ' ' + H + '" role="img" aria-label="กราฟวิเคราะห์ต้นทุนรวม">' + g + '</svg>';
}

/* กราฟเส้นย่อ 3 ปีในช่องตาราง — เส้นลงหมายถึงต้นทุนลดลง คือดีขึ้น */
function sparkLine(series, w, h){
  if (!series || series.length < 2) {
    return '<svg width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + ' ' + h + '" aria-hidden="true" style="display:block">' +
      '<line x1="' + (w/2 - 6) + '" y1="' + (h/2) + '" x2="' + (w/2 + 6) + '" y2="' + (h/2) + '" stroke="#D0D5DD" stroke-width="1.8" stroke-linecap="round"></line></svg>';
  }
  var min = Math.min.apply(null, series), max = Math.max.apply(null, series);
  var span = (max - min) || 1, pad = 3.5;
  var pts = series.map(function(v, i){
    return [pad + (w - pad*2) * i / (series.length - 1),
            pad + (h - pad*2) * (1 - (v - min) / span)];
  });
  var d = pts.map(function(p, i){ return (i ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1); }).join("");
  var last = pts[pts.length - 1];
  return '<svg width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + ' ' + h + '" aria-hidden="true" style="display:block">' +
    '<path d="' + d + '" fill="none" stroke="#D92D20" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>' +
    '<circle cx="' + last[0].toFixed(1) + '" cy="' + last[1].toFixed(1) + '" r="2.4" fill="#D92D20"></circle></svg>';
}
/* ช่องกราฟย่อ: ค่าปีล่าสุด + เส้นย้อนหลัง + ส่วนต่างจากการตรวจปีแรก
   เครื่องหมายบอกทิศของตัวเลขดิบ ส่วนสีบอกว่าดีขึ้นหรือแย่ลง */
function miniCell(series, opts){
  if (series.length < 2) { series = [series[0], series[0]]; }
  var dp = opts.dp === undefined ? 1 : dp0(opts.dp);
  var first = series[0], last = series[series.length - 1];
  var raw = last - first;
  var gain = opts.lowerBetter ? -raw : raw;
  var eps = Math.pow(10, -dp) / 2;
  var cls = gain > eps ? "down" : (gain < -eps ? "up" : "flat");
  var word = cls === "down" ? "ดีขึ้น" : (cls === "up" ? "แย่ลง" : "เท่าเดิม");
  var txt = cls === "flat" ? "เท่าเดิม" : (raw > 0 ? "+" : "\u2212") + Math.abs(raw).toFixed(dp);
  var label = opts.name + " ปี 2026 เท่ากับ " + last.toFixed(dp) +
              " · ผลตรวจย้อนหลัง " + series.map(function(v){ return v.toFixed(dp); }).join(" ") +
              " · " + word;
  return '<div class="mini' + (opts.best ? " best" : "") + '" role="img" aria-label="' + label + '">' +
    '<span class="top"><span class="v">' + last.toFixed(dp) + '</span>' +
    '<span class="d ' + cls + '">' + txt + '</span></span>' +
    sparkLine(series, 44, 14) + '</div>';
}
function dp0(v){ return v; }
/* คะแนนรายด้านย้อนหลัง — ปี 2026 คือค่าปัจจุบัน */
function dimSeries(cat, iso, id, dim, now){
  var r = seed(id + iso + cat + dim);
  var dir = r > 0.62 ? -1 : 1;
  /* ถ้าค่าปัจจุบันชิดเพดานหรือพื้น ให้กลับทิศ ไม่งั้นปีเก่าจะถูกตัดจนได้เลขซ้ำ */
  if (dir < 0 && (9.9 - now) < 0.3) { dir = 1; }
  if (dir > 0 && (now - 6.2) < 0.3) { dir = -1; }
  var step = 0.05 + r * 0.26;
  var room = dir < 0 ? (9.9 - now) : (now - 6.2);
  step = Math.max(0.05, Math.min(step, room / 2));
  return YEARS3.map(function(y){
    var v = now - dir * step * (2026 - y);
    return Math.round(Math.max(6.0, Math.min(10, v)) * 10) / 10;
  });
}
function trendCell(series, opts){
  if (series.length < 2) { series = [series[0], series[0]]; }
  var dp = opts.dp === undefined ? 2 : opts.dp;
  var first = series[0], last = series[series.length - 1];
  var gain = opts.lowerBetter ? (first - last) : (last - first);
  var eps = Math.pow(10, -dp) / 2;
  var cls = gain > eps ? "down" : (gain < -eps ? "up" : "flat");
  var word = cls === "down" ? "ดีขึ้น " + gain.toFixed(dp)
           : cls === "up"   ? "แย่ลง " + Math.abs(gain).toFixed(dp)
           : "เท่าเดิม";
  var label = opts.name + " ปี 2026 เท่ากับ " + last.toFixed(dp) + (opts.unit ? " " + opts.unit : "") +
              " · ย้อนหลังสามปี " + series.map(function(v){ return v.toFixed(dp); }).join(" ") +
              " · " + word;
  return '<div class="mcell" role="img" aria-label="' + label + '">' +
    '<span class="top"><span class="mval">' + last.toFixed(dp) + '</span>' +
    '<span class="mtrend ' + cls + '">' + word + '</span></span>' +
    sparkLine(series, 58, 16) + '</div>';
}
function rkRender(){
  rkCatTabs(); rkTabs(); buildYearSelects();
  var c = CATS[rkCat];
  if (!rosterFor(rkCat, rkIso).length) {
    var alt = ["AU","CY","GB","SG","US","AE","ZA"].filter(function(i){ return rosterFor(rkCat, i).length; })[0];
    if (alt) { rkIso = alt; rkTabs(); }
  }
  var rows = rkRows(rkCat, rkIso, rkYear), best = bestPerDim(rows);
  var rkQ = (document.getElementById("rk-q") || {}).value || "";
  var qq = rkQ.trim().toLowerCase();
  var shown = qq ? rows.filter(function(r){ return META[r.id].n.toLowerCase().indexOf(qq) >= 0; }) : rows;
  document.getElementById("rk-metric-h").textContent = c.metric + " (" + c.unit + ")";
  if (!shown.length) {
    document.getElementById("rk-body").innerHTML =
      '<tr><td colspan="11" style="padding:34px 16px;text-align:center;color:#667085;font-size:13.5px;">' +
      'ไม่พบ &ldquo;' + rkQ.trim() + '&rdquo; ในหมวด' + c.n + ' ของ' + CNAME[rkIso] +
      ' — ลองเปลี่ยนหมวดหรือประเทศ</td></tr>';
  } else {
  document.getElementById("rk-body").innerHTML = shown.map(function(r, i){
    var m = META[r.id];
    var rk = rows.indexOf(r) + 1;
    return '<tr>' +
      '<td><span class="rk-rank' + (rk === 1 ? " top" : "") + '">' + rk + '</span></td>' +
      '<td><div class="rk-name">' + logoSpan(m, 34, 12) +
        '<span class="t"><b>' + m.n + '</b><span>' + m.reg + '</span></span></div></td>' +
      '<td><div class="rk-stars">' + starHTML(r.stars, 15) + '</div></td>' +
      '<td class="num">' + trendCell(r.scoreSeries, {name:"คะแนนรวม", dp:1}) + '</td>' +
      '<td class="num">' + trendCell(r.series, {name:c.metric, unit:c.unit, lowerBetter:true, dp:2}) + '</td>' +
      '<td class="num">' + trendCell(r.costSeries, {name:"ต้นทุนรวม", unit:c.costUnit, lowerBetter:true, dp:2}) + '</td>' +
      DIMS.map(function(d){
        var v = r.vals[d[0]];
        return '<td class="num">' + miniCell(r.dimSer[d[0]], {name:d[1], dp:1, best:(v === best[d[0]])}) + '</td>';
      }).join("") +
      '<td class="rk-sticky"><span class="rk-cta" data-review="' + m.slug + '" tabindex="0" role="button">อ่านรีวิว &rarr;</span></td>' +
    '</tr>';
  }).join("");
  }
  document.getElementById("rk-note").innerHTML =
    'ทุกช่องคะแนนคือผลหลังการตรวจของแต่ละปี · คะแนนรวมคือค่าเฉลี่ยของสี่ด้านในปีนั้น · ตัวเลขสีแดงคือรายที่ทำได้ดีที่สุดในด้านนั้นของประเทศนี้ · ' +
    'ตัวเลขข้างกราฟย่อคือส่วนต่างจากการตรวจปี 2024 สีเขียวคือดีขึ้น สีส้มคือแย่ลง · ' +
    'กราฟเส้นทุกช่องคือค่าย้อนหลัง 3 ปี ปี 2024 &rarr; 2025 &rarr; 2026 · คะแนนยิ่งสูงยิ่งดี ส่วน' + c.metric + 'และต้นทุนรวมยิ่งต่ำยิ่งดี ' +
    'จึงใช้คำว่าดีขึ้น/แย่ลงกำกับแทนลูกศร<br>' +
    'ตัวเลขทั้งหมดเป็นข้อมูลตัวอย่างสำหรับงานออกแบบ ยังไม่ใช่ผลตรวจจริง';

  document.getElementById("rk-cost-h").textContent = "ต้นทุนรวม (" + c.costUnit + ")";

  paintLogos();
}
/* ── เทียบตัวต่อตัว — มีหมวด/ประเทศ/ปี เป็นของตัวเอง ไม่ผูกกับตารางอันดับ ── */
var cmCat = "fx", cmIso = "AU", cmYear = 2026;
var CM_ISOS = ["AU","CY","GB","SG","US","AE","ZA"];
function cmpRows(){ return rkRows(cmCat, cmIso, cmYear); }
function cmpFixIso(){
  if (rkRows(cmCat, cmIso, cmYear).length) { return; }
  var f = CM_ISOS.filter(function(i){ return rkRows(cmCat, i, cmYear).length; })[0];
  if (f) { cmIso = f; }
}
function cmpControls(){
  var cs = document.getElementById("cmp-cat");
  if (cs) {
    cs.innerHTML = CAT_ORDER.map(function(k){
      return '<option value="' + k + '"' + (k === cmCat ? " selected" : "") + '>' + catShort(k) + '</option>';
    }).join("");
  }
  var is = document.getElementById("cmp-iso");
  if (is) {
    is.innerHTML = CM_ISOS.map(function(iso){
      var m = rkRows(cmCat, iso, cmYear).length;
      return '<option value="' + iso + '"' + (iso === cmIso ? " selected" : "") + (m ? "" : " disabled") + '>' +
        CNAME[iso] + (m ? " (" + m + " \u0e23\u0e32\u0e22)" : " \u2014 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14\u0e19\u0e35\u0e49") + '</option>';
    }).join("");
  }
  var ys = document.getElementById("cmp-year");
  if (ys) { ys.innerHTML = yearOptions("cmp", cmYear); }
}
function cmpSelect(selId, sel, other){
  var el = document.getElementById(selId);
  if (!el) { return; }
  el.innerHTML = cmpRows().map(function(r){
    return '<option value="' + r.id + '"' + (r.id === sel ? " selected" : "") +
      (r.id === other ? " disabled" : "") + '>' + META[r.id].n + ' \u2014 ' +
      r.total.toFixed(1) + '</option>';
  }).join("");
}
function cmpRender(){
  cmpFixIso();
  var rows = cmpRows();
  var ids = rows.map(function(r){ return r.id; });
  if (ids.indexOf(cmpA) < 0) { cmpA = ids[0] || null; }
  if (ids.indexOf(cmpB) < 0 || cmpB === cmpA) { cmpB = ids.filter(function(x){ return x !== cmpA; })[0] || null; }
  cmpControls();
  cmpSelect("cmp-sel-a", cmpA, cmpB);
  cmpSelect("cmp-sel-b", cmpB, cmpA);
  var box = document.getElementById("cmp-body"), c = CATS[cmCat];
  var a = rows.filter(function(r){ return r.id === cmpA; })[0];
  var b = rows.filter(function(r){ return r.id === cmpB; })[0];
  if (!a || !b) {
    box.innerHTML = '<div class="cmp-card"><div style="padding:36px 20px;text-align:center;color:#667085;font-size:13.5px;line-height:1.7;">' +
      '\u0e2b\u0e21\u0e27\u0e14' + CATS[cmCat].n + '\u0e43\u0e19' + CNAME[cmIso] +
      ' \u0e1b\u0e35 ' + cmYear + ' \u0e21\u0e35\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e43\u0e19\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e44\u0e21\u0e48\u0e16\u0e36\u0e07\u0e2a\u0e2d\u0e07\u0e23\u0e32\u0e22 \u0e08\u0e36\u0e07\u0e22\u0e31\u0e07\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49</div></div>';
    var ah = document.getElementById("cmp-ai");
    if (ah) {
      ah.innerHTML = '<div class="ai-head">' + aiMark() +
        '<span><b>RedStar Thinking</b><span>\u0e2a\u0e23\u0e38\u0e1b\u0e08\u0e32\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49</span></span></div>' +
        '<div class="ai-empty">\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e2d\u0e30\u0e44\u0e23\u0e43\u0e2b\u0e49\u0e2a\u0e23\u0e38\u0e1b \u2014 \u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e19\u0e49\u0e2d\u0e22\u0e2a\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e43\u0e19\u0e02\u0e2d\u0e1a\u0e40\u0e02\u0e15\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e16\u0e36\u0e07\u0e08\u0e30\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e19\u0e44\u0e14\u0e49</div>';
    }
    return;
  }
  var ma = META[a.id], mb = META[b.id];
  function head(m){
    return '<div><div class="who">' + logoSpan(m, 30, 11) +
      '<span><b>' + m.n + '</b><span>' + m.reg + '</span></span></div></div>';
  }
  var lines = [{k:"stars", label:"ดาว RedStar", av:a.stars, bv:b.stars, star:true},
               {k:"total", label:"คะแนนรวม", av:a.total, bv:b.total},
               {k:"metric", label:c.metric + " (" + c.unit + ")", av:a.metric, bv:b.metric, lower:true, dp:2}];
  DIMS.forEach(function(d){ lines.push({k:d[0], label:d[1], av:a.vals[d[0]], bv:b.vals[d[0]]}); });
  var winA = 0, winB = 0, tie = 0;
  var body = lines.map(function(l){
    var aw = l.lower ? l.av < l.bv : l.av > l.bv;
    var bw = l.lower ? l.bv < l.av : l.bv > l.av;
    if (aw) { winA++; } else if (bw) { winB++; } else { tie++; }
    function cell(v, win, other){
      var inner = l.star
        ? '<span class="rk-stars">' + starHTML(v, 15) + '</span><span class="cmp-val">' + v + '</span>'
        : '<span class="cmp-val">' + v.toFixed(l.dp || 1) + '</span>';
      var diff = Math.abs(v - other);
      var d = l.star ? String(Math.round(diff)) : diff.toFixed(l.dp || 1);
      var sign = l.lower ? "&minus;" : "+";
      var delta = win ? '<span class="cmp-delta">' + sign + d + '</span>' : '';
      return '<div class="' + (win ? "cmp-win" : "") + '">' + inner + delta + '</div>';
    }
    return '<div class="cmp-row"><div class="cmp-label">' + l.label + '</div>' +
      cell(l.av, aw, l.bv) + cell(l.bv, bw, l.av) + '</div>';
  }).join("");
  box.innerHTML = '<div class="cmp-card">' +
    '<div class="cmp-head"><div style="color:#667085;font-size:11px;letter-spacing:.04em;text-transform:uppercase;' +
    'display:flex;align-items:center;line-height:1.35;">' + catShort(cmCat) + '<br>' + CNAME[cmIso] + ' ' + cmYear + '</div>' +
    head(ma) + head(mb) + '</div>' + body +
    '<div class="cmp-sum">' +
    '<span>' + ma.n + ' \u0e0a\u0e19\u0e30 ' + winA + ' \u00b7 ' + mb.n + ' \u0e0a\u0e19\u0e30 ' + winB + ' \u00b7 \u0e40\u0e2a\u0e21\u0e2d ' + tie + '</span>' +
    '<span class="cmp-tie">\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e44\u0e14\u0e49\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e20\u0e32\u0e22\u0e43\u0e19\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e41\u0e25\u0e30\u0e2b\u0e21\u0e27\u0e14\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e01\u0e25\u0e44\u0e01\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e02\u0e2d\u0e07\u0e41\u0e15\u0e48\u0e25\u0e30\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e44\u0e21\u0e48\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19</span>' +
    '</div></div>';
  aiRender(a, b, ma, mb, c, winA, winB, tie, lines.length);
  paintLogos();
}

/* ── RedStar Thinking — อ่านตัวเลขจากตารางด้านซ้ายแล้วสรุป ไม่สร้างข้อมูลที่ไม่ได้แสดงบนหน้า ── */
function aiMark(){
  return '<span class="ai-mark"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" ' +
    'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    '<path d="M12 3.4l1.7 4.1 4.1 1.7-4.1 1.7L12 15l-1.7-4.1L6.2 9.2l4.1-1.7z"></path>' +
    '<path d="M18.2 15.1l.7 1.7 1.7.7-1.7.7-.7 1.7-.7-1.7-1.7-.7 1.7-.7z"></path></svg></span>';
}
function aiIcon(t){
  var d = t === "up"   ? '<path d="M12 19V5M5 12l7-7 7 7"></path>'
        : t === "down" ? '<path d="M12 5v14M5 12l7 7 7-7"></path>'
        : t === "cost" ? '<circle cx="12" cy="12" r="8.6"></circle><path d="M9.4 9.3h5.2M9.4 12.1h5.2M12 7.9v8.2"></path>'
        : t === "star" ? '<path d="' + STAR_D + '"></path>'
        : '<circle cx="12" cy="12" r="8.6"></circle><path d="M12 11.3v4.9M12 8.2v.1"></path>';
  var col = t === "up" ? "#067647" : t === "down" ? "#B54708" : "#667085";
  return '<svg class="ai-ic" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="' + col +
    '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + d + '</svg>';
}
function aiRender(a, b, ma, mb, c, winA, winB, tie, nLines){
  var host = document.getElementById("cmp-ai");
  if (!host) { return; }
  var nameOf = function(r){ return r === a ? ma.n : mb.n; };
  var dScore = Math.round((a.total - b.total) * 10) / 10;
  var byWins  = winA === winB ? null : (winA > winB ? a : b);
  var byScore = Math.abs(dScore) < 0.05 ? null : (dScore > 0 ? a : b);
  var head, sub;
  if (byWins && byScore && byWins !== byScore) {
    head = '\u0e1c\u0e25\u0e44\u0e21\u0e48\u0e44\u0e1b\u0e17\u0e32\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19';
    sub = '<b>' + nameOf(byWins) + '</b> \u0e0a\u0e19\u0e30\u0e08\u0e33\u0e19\u0e27\u0e19\u0e14\u0e49\u0e32\u0e19\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32 (' +
      Math.max(winA, winB) + ' \u0e08\u0e32\u0e01 ' + nLines + ') \u0e41\u0e15\u0e48 <b>' + nameOf(byScore) +
      '</b> \u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21\u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32 ' + Math.abs(dScore).toFixed(1) +
      ' \u2014 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e0a\u0e19\u0e30\u0e01\u0e31\u0e19\u0e04\u0e19\u0e25\u0e30\u0e14\u0e49\u0e32\u0e19';
  } else if (byWins) {
    head = nameOf(byWins) + ' \u0e14\u0e35\u0e01\u0e27\u0e48\u0e32\u0e43\u0e19\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21';
    sub = '\u0e0a\u0e19\u0e30 ' + Math.max(winA, winB) + ' \u0e08\u0e32\u0e01 ' + nLines + ' \u0e14\u0e49\u0e32\u0e19' +
      (byScore ? ' \u00b7 \u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21\u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32 ' + Math.abs(dScore).toFixed(1)
              : ' \u00b7 \u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21\u0e40\u0e17\u0e48\u0e32\u0e01\u0e31\u0e19');
  } else {
    head = '\u0e2a\u0e39\u0e2a\u0e35';
    sub = '\u0e0a\u0e19\u0e30\u0e01\u0e31\u0e19\u0e04\u0e19\u0e25\u0e30 ' + winA + ' \u0e14\u0e49\u0e32\u0e19' +
      (tie ? ' \u00b7 \u0e40\u0e2a\u0e21\u0e2d ' + tie + ' \u0e14\u0e49\u0e32\u0e19' : '') +
      (byScore ? ' \u00b7 \u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21 <b>' + nameOf(byScore) +
                 '</b> \u0e19\u0e33\u0e2d\u0e22\u0e39\u0e48 ' + Math.abs(dScore).toFixed(1) : '');
  }
  var pts = [];
  var gaps = DIMS.map(function(d){
    return {label:d[1], diff:Math.round((a.vals[d[0]] - b.vals[d[0]]) * 10) / 10};
  });
  var big = gaps.slice().sort(function(x, y){ return Math.abs(y.diff) - Math.abs(x.diff); })[0];
  if (Math.abs(big.diff) >= 0.05) {
    pts.push(["up", '<b>' + (big.diff > 0 ? ma.n : mb.n) + '</b> \u0e17\u0e34\u0e49\u0e07\u0e2b\u0e48\u0e32\u0e07\u0e21\u0e32\u0e01\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e14\u0e49\u0e32\u0e19<b>' +
      big.label + '</b> \u0e2d\u0e22\u0e39\u0e48 ' + Math.abs(big.diff).toFixed(1) + ' \u0e04\u0e30\u0e41\u0e19\u0e19']);
  } else {
    pts.push(["dot", '\u0e04\u0e30\u0e41\u0e19\u0e19\u0e2a\u0e35\u0e48\u0e14\u0e49\u0e32\u0e19\u0e22\u0e48\u0e2d\u0e22\u0e40\u0e01\u0e32\u0e30\u0e01\u0e31\u0e19\u0e41\u0e17\u0e1a\u0e44\u0e21\u0e48\u0e15\u0e48\u0e32\u0e07 \u0e2b\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e44\u0e21\u0e48\u0e16\u0e36\u0e07 0.1 \u0e04\u0e30\u0e41\u0e19\u0e19']);
  }
  var lead = byWins || byScore;
  if (lead) {
    var behind = gaps.filter(function(g){ return (lead === a ? g.diff : -g.diff) < -0.05; })
                     .sort(function(x, y){ return Math.abs(y.diff) - Math.abs(x.diff); });
    pts.push(behind.length
      ? ["down", '<b>' + nameOf(lead) + '</b> \u0e22\u0e31\u0e07\u0e15\u0e32\u0e21\u0e2b\u0e25\u0e31\u0e07\u0e14\u0e49\u0e32\u0e19<b>' + behind[0].label +
          '</b> \u0e2d\u0e22\u0e39\u0e48 ' + Math.abs(behind[0].diff).toFixed(1) + ' \u0e04\u0e30\u0e41\u0e19\u0e19' +
          (behind.length > 1 ? ' \u0e41\u0e25\u0e30\u0e15\u0e32\u0e21\u0e2b\u0e25\u0e31\u0e07\u0e2d\u0e35\u0e01 ' + (behind.length - 1) + ' \u0e14\u0e49\u0e32\u0e19' : '')]
      : ["up", '<b>' + nameOf(lead) + '</b> \u0e19\u0e33\u0e04\u0e23\u0e1a\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e35\u0e48\u0e14\u0e49\u0e32\u0e19\u0e22\u0e48\u0e2d\u0e22 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e14\u0e49\u0e32\u0e19\u0e44\u0e2b\u0e19\u0e15\u0e32\u0e21\u0e2b\u0e25\u0e31\u0e07']);
  }
  var dm = Math.round((a.metric - b.metric) * 100) / 100;
  if (Math.abs(dm) >= 0.005) {
    var lo = dm < 0 ? a : b, hi = dm < 0 ? b : a;
    var save = hi.metric > 0 ? Math.round(Math.abs(dm) / hi.metric * 100) : 0;
    pts.push(["cost", '<b>' + c.metric + '</b> \u0e02\u0e2d\u0e07 <b>' + nameOf(lo) + '</b> \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 ' +
      Math.abs(dm).toFixed(2) + ' ' + c.unit + ' \u2014 \u0e16\u0e39\u0e01\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e27 ' + save + '% (' + c.note + ')']);
  } else {
    pts.push(["cost", '<b>' + c.metric + '</b> \u0e40\u0e17\u0e48\u0e32\u0e01\u0e31\u0e19\u0e17\u0e35\u0e48 ' + a.metric.toFixed(2) + ' ' + c.unit]);
  }
  pts.push(a.stars === b.stars
    ? ["star", '\u0e44\u0e14\u0e49 <b>' + a.stars + ' \u0e14\u0e32\u0e27</b> \u0e40\u0e17\u0e48\u0e32\u0e01\u0e31\u0e19 \u2014 \u0e14\u0e32\u0e27\u0e04\u0e37\u0e2d\u0e1c\u0e48\u0e32\u0e19/\u0e44\u0e21\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c \u0e2a\u0e48\u0e27\u0e19\u0e04\u0e30\u0e41\u0e19\u0e19\u0e44\u0e27\u0e49\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e19\u0e40\u0e2d\u0e07 \u0e14\u0e32\u0e27\u0e40\u0e17\u0e48\u0e32\u0e01\u0e31\u0e19\u0e08\u0e36\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e14\u0e35\u0e40\u0e17\u0e48\u0e32\u0e01\u0e31\u0e19']
    : ["star", '<b>' + (a.stars > b.stars ? ma.n : mb.n) + '</b> \u0e44\u0e14\u0e49 ' + Math.max(a.stars, b.stars) +
        ' \u0e14\u0e32\u0e27 \u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e2d\u0e35\u0e01\u0e23\u0e32\u0e22\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49 ' + Math.min(a.stars, b.stars) +
        ' \u0e14\u0e32\u0e27 \u2014 \u0e14\u0e32\u0e27\u0e21\u0e32\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e04\u0e30\u0e41\u0e19\u0e19']);
  var sa = a.scoreSeries, sb = b.scoreSeries;
  if (sa.length > 1) {
    var ga = Math.round((sa[sa.length - 1] - sa[0]) * 10) / 10;
    var gb = Math.round((sb[sb.length - 1] - sb[0]) * 10) / 10;
    var word = function(g){
      return g > 0.04 ? '\u0e14\u0e35\u0e02\u0e36\u0e49\u0e19 ' + g.toFixed(1)
           : g < -0.04 ? '\u0e41\u0e22\u0e48\u0e25\u0e07 ' + Math.abs(g).toFixed(1) : '\u0e17\u0e23\u0e07\u0e15\u0e31\u0e27';
    };
    pts.push([ga >= gb ? "up" : "down", '\u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48\u0e1b\u0e35 ' + YEARS3[0] + ' \u0e16\u0e36\u0e07 ' + a.year +
      ': <b>' + ma.n + '</b> ' + word(ga) + ' \u00b7 <b>' + mb.n + '</b> ' + word(gb)]);
  }
  host.innerHTML =
    '<div class="ai-head">' + aiMark() +
      '<span><b>RedStar Thinking</b><span>\u0e2a\u0e23\u0e38\u0e1b\u0e08\u0e32\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49</span></span></div>' +
    '<div class="ai-verdict"><span class="ai-v">' + head + '</span><span class="ai-s">' + sub + '</span></div>' +
    '<div class="ai-list">' + pts.map(function(p){
      return '<div class="ai-item">' + aiIcon(p[0]) + '<span>' + p[1] + '</span></div>';
    }).join("") + '</div>' +
    '<div class="ai-foot">\u0e2a\u0e23\u0e38\u0e1b\u0e19\u0e35\u0e49\u0e2d\u0e48\u0e32\u0e19\u0e08\u0e32\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e43\u0e19\u0e15\u0e32\u0e23\u0e32\u0e07\u0e14\u0e49\u0e32\u0e19\u0e0b\u0e49\u0e32\u0e22\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19 \u0e44\u0e21\u0e48\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e2a\u0e14\u0e07\u0e1a\u0e19\u0e2b\u0e19\u0e49\u0e32 \u00b7 <b>\u0e44\u0e21\u0e48\u0e21\u0e35\u0e1c\u0e25\u0e15\u0e48\u0e2d\u0e08\u0e33\u0e19\u0e27\u0e19\u0e14\u0e32\u0e27\u0e41\u0e25\u0e30\u0e04\u0e30\u0e41\u0e19\u0e19</b><br>' +
    '\u0e43\u0e19\u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e08\u0e32\u0e01\u0e01\u0e0e \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e1a\u0e42\u0e21\u0e40\u0e14\u0e25\u0e08\u0e23\u0e34\u0e07</div>';
}
document.addEventListener("click", function(ev){
  var rv = ev.target.closest("[data-review]");
  if (rv) { ev.preventDefault(); }
});
document.getElementById("rk-cat-sel").addEventListener("change", function(e){ rkCat = e.target.value; rkRender(); });
document.getElementById("rk-iso-sel").addEventListener("change", function(e){ rkIso = e.target.value; rkRender(); });
(function(){
  var on = function(id, fn){
    var el = document.getElementById(id);
    if (el) { el.addEventListener("change", function(e){ fn(e.target.value); cmpRender(); }); }
  };
  on("cmp-sel-a", function(v){ cmpA = v; });
  on("cmp-sel-b", function(v){ cmpB = v; });
  on("cmp-cat",  function(v){ cmCat = v; cmpA = cmpB = null; });
  on("cmp-iso",  function(v){ cmIso = v; cmpA = cmpB = null; });
  on("cmp-year", function(v){ cmYear = parseInt(v, 10); });
  cmpRender();
})();
document.addEventListener("keydown", function(ev){
  if (ev.key !== "Enter" && ev.key !== " ") { return; }
  var t = ev.target.closest(".rk-cta");
  if (t) { ev.preventDefault(); t.click(); }
});
var _rq = document.getElementById("rk-q");
if (_rq) { _rq.addEventListener("input", function(){ rkRender(); }); }
rkRender();
/* ── ช่องค้นหาบนแถบดำ: ค้นทั้งทะเบียน แล้วพาไปที่แผนที่ ── */
(function(){
  var inp = document.getElementById("top-search"), box = document.getElementById("top-results");
  if (!inp || !box) { return; }
  function close(){ box.hidden = true; box.innerHTML = ""; }
  function render(){
    var q = inp.value.trim().toLowerCase();
    if (!q) { close(); return; }
    var hits = Object.keys(B).filter(function(id){ return B[id].n.toLowerCase().indexOf(q) >= 0; });
    hits.sort(function(a,b){ return B[b].stars - B[a].stars || B[a].n.localeCompare(B[b].n); });
    box.hidden = false;
    if (!hits.length) {
      box.innerHTML = '<p class="tr-none">ไม่พบ &ldquo;' + inp.value.trim() +
        '&rdquo; ในทะเบียน — การไม่อยู่ในทะเบียนไม่ได้แปลว่าไม่ดี แปลว่าเรายังไม่ได้ตรวจ</p>';
      return;
    }
    box.innerHTML = hits.map(function(id){
      var b = B[id], slug = (typeof LOGO_SLUG !== "undefined" && LOGO_SLUG[b.id]) ? LOGO_SLUG[b.id] : b.id;
      return '<button type="button" class="tr-hit" role="option" data-toppick="' + id + '">' +
        '<span data-logo="' + slug + '|' + b.mono + '" style="width:28px;height:28px;border-radius:7px;' +
        'display:inline-flex;align-items:center;justify-content:center;font-family:IBM Plex Sans,sans-serif;' +
        'font-size:10.5px;font-weight:700;color:#fff;flex-shrink:0;"></span>' +
        '<span><b>' + b.n + '</b><span class="s">' + b.c + ' · ' + b.reg + '</span></span>' +
        '<span class="st">' + starHTML(b.stars, 12) + '</span></button>';
    }).join("");
    paintLogos();
  }
  inp.addEventListener("input", render);
  inp.addEventListener("focus", render);
  document.addEventListener("click", function(ev){
    var p = ev.target.closest("[data-toppick]");
    if (p) {
      var id = p.dataset.toppick;
      if ((REGION[region] || []).indexOf(B[id].iso) < 0) { setRegion("all"); }
      select(id);
      inp.value = ""; close();
      document.getElementById("map-stage").scrollIntoView({behavior:"smooth", block:"center"});
      return;
    }
    if (!ev.target.closest(".mh-search")) { close(); }
  });
  inp.addEventListener("keydown", function(e){ if (e.key === "Escape") { inp.value = ""; close(); } });
})();

/* ── ตัวเลขสถิติใน Hero — นับจากข้อมูลจริงในหน้า ไม่ใช่เลขที่พิมพ์ทิ้งไว้ ── */
(function(){
  var el = document.getElementById("hero-stats");
  if (!el) { return; }
  var isoList = ["AU","CY","GB","SG","US","AE","ZA"];
  var countries = isoList.filter(function(i){ return (ROSTER[i] || []).length; }).length;
  var brokers = Object.keys(META).length;
  var ic = function(d){ return '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#D92D20" ' +
    'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + d + '</svg>'; };
  var rows = [
    ["Countries", countries, ic('<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3c2.6 2.8 2.6 15 0 18M12 3c-2.6 2.8-2.6 15 0 18"></path>')],
    ["Brokers", brokers, ic('<path d="M4 20V9.5L12 4l8 5.5V20"></path><path d="M9.5 20v-5h5v5"></path>')],
    ["Reviewers", 28, ic('<circle cx="9" cy="9" r="3.2"></circle><path d="M3.5 19.5c.7-3 2.9-4.6 5.5-4.6s4.8 1.6 5.5 4.6"></path><path d="M16 6.2a3 3 0 010 5.8M17.6 19.5c-.3-1.6-.9-2.9-1.8-3.8"></path>')],
    ["Evidence", "2,500+", ic('<circle cx="12" cy="12" r="9"></circle><path d="M8.2 12.2l2.6 2.6 5-5.2"></path>')]
  ];
  el.innerHTML = rows.map(function(r){
    return '<div><dt>' + r[2] + r[0] + '</dt><dd>' + r[1] + '</dd></div>';
  }).join("");
  var hc = document.getElementById("hero-countries");
  if (hc) { hc.textContent = countries; }
})();
/* ── 3 อันดับแรกของแต่ละหมวด ── */
var PICK_CATS = [
  {k:"fx",       label:"BEST FOREX",    title:"Forex Broker", bars:["cost","platform"]},
  {k:"stocks",   label:"BEST STOCK",    title:"Stock",        bars:["cost","service"]},
  {k:"exchange", label:"BEST EXCHANGE", title:"Exchange",     bars:["platform","funding"]}
];
var DIM_LABEL = {cost:"Cost", platform:"Platform", service:"Service", funding:"Funding"};
var pkRegion = "all", pkIso = "all";
function pkIsoList(){
  var list = (REGION[pkRegion] || []).filter(function(iso){ return (ROSTER[iso] || []).length; });
  if (pkIso !== "all" && list.indexOf(pkIso) >= 0) { return [pkIso]; }
  return list;
}
function pkScopeLabel(){
  if (pkIso !== "all") { return CNAME[pkIso]; }
  if (pkRegion !== "all") { return REGION_NAME[pkRegion]; }
  return "ทุกประเทศในทะเบียน";
}
function pkControls(){
  var regions = ["all","eu","apac","me","af","na","sa"].map(function(k){
    var n = (REGION[k] || []).filter(function(i){ return (ROSTER[i] || []).length; }).length;
    return '<option value="' + k + '"' + (k === pkRegion ? " selected" : "") + (n ? "" : " disabled") + '>' +
      (k === "all" ? "ทุกภูมิภาค" : REGION_NAME[k]) + (n ? " (" + n + ")" : " — ยังไม่เปิดตรวจ") + '</option>';
  }).join("");
  var inRegion = (REGION[pkRegion] || []).filter(function(i){ return (ROSTER[i] || []).length; });
  var countries = ['<option value="all"' + (pkIso === "all" ? " selected" : "") + '>ทุกประเทศ (' + inRegion.length + ')</option>']
    .concat(inRegion.map(function(iso){
      return '<option value="' + iso + '"' + (iso === pkIso ? " selected" : "") + '>' + CNAME[iso] + '</option>';
    })).join("");
  return '<div class="pk-picks-ctl">' +
    '<label class="rk-pick"><span>ปี</span><select id="pk-year" aria-label="เลือกปีผลตรวจของ 3 อันดับแรก">' +
      YEARS3.slice().reverse().map(function(y){
        return '<option value="' + y + '"' + (y === pkYear ? " selected" : "") + '>' + y + '</option>';
      }).join("") + '</select></label>' +
    '<label class="rk-pick"><span>ภูมิภาค</span><select id="pk-region" aria-label="เลือกภูมิภาคของ 3 อันดับแรก">' + regions + '</select></label>' +
    '<label class="rk-pick"><span>ประเทศ</span><select id="pk-iso" aria-label="เลือกประเทศของ 3 อันดับแรก">' + countries + '</select></label>' +
    '<span class="pk-live"><i></i>Live Ranking</span></div>';
}
function topPicks(cat, n){
  var best = {};
  pkIsoList().forEach(function(iso){
    rkRows(cat, iso, pkYear).forEach(function(r){
      if (!best[r.id] || r.total > best[r.id].r.total) { best[r.id] = {r:r, iso:iso}; }
    });
  });
  return Object.keys(best).map(function(k){ return best[k]; })
    .sort(function(a, b){ return b.r.total - a.r.total || META[a.r.id].n.localeCompare(META[b.r.id].n); })
    .slice(0, n);
}
/* ── ใครอันดับดีขึ้น ใครแย่ลง — เทียบผลตรวจปีที่เลือกกับปีก่อนหน้า ── */
function moverList(){
  var yi = YEARS3.indexOf(mapYear);
  if (yi < 1) { return null; }
  var isos = (typeof mapIsos === "function") ? mapIsos() : (REGION[region] || []);
  var best = {};
  isos.forEach(function(iso){
    rkRows(mapCat, iso, mapYear).forEach(function(r){
      var d = Math.round((r.scoreSeries[yi] - r.scoreSeries[yi - 1]) * 10) / 10;
      var cur = best[r.id];
      if (!cur || Math.abs(d) > Math.abs(cur.d)) { best[r.id] = {r:r, iso:iso, d:d}; }
    });
  });
  return Object.keys(best).map(function(k){ return best[k]; });
}
function moverRows(list, dir){
  return list.filter(function(x){ return dir > 0 ? x.d > 0.04 : x.d < -0.04; })
    .sort(function(a, b){ return dir > 0 ? b.d - a.d : a.d - b.d; })
    .slice(0, 3).map(function(x){
      var m = META[x.r.id], slug = m.slug;
      return '<div class="mv-row">' +
        '<span class="mv-logo" data-logo="' + slug + '|' + m.mono + '"></span>' +
        '<span><span class="mv-name">' + m.n + '</span>' +
        '<span class="mv-loc">' + CNAME[x.iso] + '</span></span>' +
        '<span class="mv-delta"><b>' + (x.d > 0 ? "+" : "\u2212") + Math.abs(x.d).toFixed(1) + '</b>' +
        '<span>' + x.r.scoreSeries[YEARS3.indexOf(mapYear) - 1].toFixed(1) + ' &rarr; ' + x.r.total.toFixed(1) + '</span></span></div>';
    }).join("");
}
function renderMovers(){
  var host = document.getElementById("movers");
  if (!host) { return; }
  if (typeof YEARS3 === "undefined" || typeof ROSTER === "undefined" || typeof mapYear === "undefined") { return; }
  var list = moverList();
  if (!list) {
    host.innerHTML = '<div class="mv-card"><div class="mv-empty">ปี ' + mapYear +
      ' เป็นรอบตรวจแรกของทะเบียน จึงยังไม่มีปีก่อนหน้าให้เทียบ<br>เลือกปีอื่นในตารางอันดับด้านล่างเพื่อดูการเปลี่ยนแปลง</div></div>';
    return;
  }
  var up = moverRows(list, 1), down = moverRows(list, -1);
  var prev = YEARS3[YEARS3.indexOf(mapYear) - 1];
  host.innerHTML =
    '<div class="mv-card up"><div class="mv-head">' +
      '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#067647" stroke-width="2.2" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"></path></svg>' +
      'อันดับดีขึ้น<span class="n">' + prev + ' &rarr; ' + mapYear + '</span></div>' +
      (up || '<div class="mv-empty">ไม่มีรายที่คะแนนดีขึ้นในขอบเขตนี้</div>') + '</div>' +
    '<div class="mv-card down"><div class="mv-head">' +
      '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#B54708" stroke-width="2.2" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M5 12l7 7 7-7"></path></svg>' +
      'อันดับแย่ลง<span class="n">' + prev + ' &rarr; ' + mapYear + '</span></div>' +
      (down || '<div class="mv-empty">ไม่มีรายที่คะแนนแย่ลงในขอบเขตนี้</div>') + '</div>' +
    '<p class="mv-note">แสดงฝั่งละ 3 รายที่ขยับมากที่สุด · เทียบคะแนนรวมหมวด' + (/^[A-Za-z]/.test(CATS[mapCat].n) ? ' ' : '') + CATS[mapCat].n + ' ตามภูมิภาคที่เลือกบนแผนที่ · เปลี่ยนหมวดและปีได้ที่ช่องเหนือแผนที่</p>';
  paintLogos();
}
function renderPicks(){
  var host = document.getElementById("picks");
  if (!host) { return; }
  host.innerHTML = '<div class="sec-rule" aria-hidden="true"></div>' +
    '<div class="pk-head"><div class="pk-title">' +
      awardStar(76) +
      '<span class="pk-titxt"><h2><i class="wm-red">RED</i> STAR</h2>' +
      '<span class="pk-award">รางวัลทรงคุณค่า</span>' +
      '<a class="pk-hof" href="#/awards">' +
        '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
        'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
        '<path d="M7 4h10v5a5 5 0 0 1-10 0z"></path><path d="M7 5.5H4.5V8a3 3 0 0 0 3 3M17 5.5h2.5V8a3 3 0 0 1-3 3"></path>' +
        '<path d="M12 14v3.5M8.5 20h7"></path></svg>Hall of Fame</a>' +
      '</span></div>' +
      pkControls() + '</div>' +
    '<div class="pk-wrap">' + PICK_CATS.map(function(c){
      var rows = topPicks(c.k, 3);
      if (!rows.length) {
        return '<div class="pk-col"><h2>' + c.title + '</h2>' +
          '<div class="pk-empty">ยังไม่มีโบรกเกอร์หมวดนี้ใน' + pkScopeLabel() +
          '<br>เราจะไม่ประกาศอันดับของขอบเขตที่ยังไม่ได้เข้าไปตรวจ</div></div>';
      }
      var one = rows[0], m1 = META[one.r.id];
      var bars = c.bars.map(function(d){
        var v = one.r.vals[d];
        return '<div class="pk-bar"><div class="lb"><span>' + DIM_LABEL[d] + '</span><b>' + v.toFixed(1) + '</b></div>' +
          '<div class="track"><div class="fill" style="width:' + (v * 10).toFixed(1) + '%"></div></div></div>';
      }).join("");
      var big = '<article class="pk-card first" data-stars="' + one.r.stars + '">' +
        '<div class="pk-rank">' + c.label.replace("BEST ", "") + '</div>' +
        '<div class="pk-body">' +
          '<span class="pk-logo" data-logo="' + m1.slug + '|' + m1.mono + '"></span>' +
          '<span class="pk-name">' + m1.n + '</span>' +
          '<span class="pk-loc">' +
            '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#98A2B3" stroke-width="2" aria-hidden="true">' +
            '<path d="M12 21s7-5.6 7-11a7 7 0 10-14 0c0 5.4 7 11 7 11z"></path><circle cx="12" cy="10" r="2.6"></circle></svg>' +
            CNAME[one.iso] + '</span>' +
          '<span class="pk-stars">' + starHTML(one.r.stars, 27) + '</span>' +
          '<span class="pk-score"><span class="pk-scorelbl">Trust Score</span>' +
            '<b>' + one.r.total.toFixed(1) + '</b><span>/10</span></span>' +
          '<div class="pk-bars">' + bars + '</div>' +
        '</div>' +
        '<div class="pk-cta"><a href="/broker/' + m1.slug + '/review" data-review="' + m1.slug + '">View Review</a></div>' +
      '</article>';
      var rest = rows.slice(1).map(function(x, i){
        var m = META[x.r.id];
        return '<article class="pk-mini" data-stars="' + x.r.stars + '">' +
          '<div class="pk-rank">' + c.label.replace("BEST ", "") + '</div>' +
          '<div class="mb">' +
            '<span class="pk-logo" data-logo="' + m.slug + '|' + m.mono + '"></span>' +
            '<span class="nm">' + m.n + '</span>' +
            '<span class="lo">' + CNAME[x.iso] + '</span>' +
            '<span class="st">' + starHTML(x.r.stars, 15) + '</span>' +
            '<span class="sc"><b>' + x.r.total.toFixed(1) + '</b><span>/10</span></span>' +
          '</div>' +
          '<div class="go"><a href="/broker/' + m.slug + '/review" data-review="' + m.slug + '">รีวิว</a></div>' +
        '</article>';
      }).join("");
      return '<div class="pk-col"><h2>' + c.title + '</h2>' + big +
             '<div class="pk-rest">' + rest + '</div></div>';
    }).join("") + '</div>';
  paintLogos();
}

/* ── ตัวเลขสถิติในบล็อกดำ — นับจากข้อมูลจริง ── */
(function(){
  var el = document.getElementById("hd-stats");
  if (!el) { return; }
  var isoList = ["AU","CY","GB","SG","US","AE","ZA"];
  var countries = isoList.filter(function(i){ return (ROSTER[i] || []).length; }).length;
  var brokers = Object.keys(META).length;          /* \u0e19\u0e31\u0e1a\u0e08\u0e32\u0e01\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e08\u0e23\u0e34\u0e07\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32 */
  /* \u0e2a\u0e2d\u0e07\u0e15\u0e31\u0e27\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e21\u0e21\u0e15\u0e34 \u0e08\u0e36\u0e07\u0e40\u0e02\u0e35\u0e22\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e44\u0e27\u0e49\u0e43\u0e15\u0e49\u0e41\u0e16\u0e1a */
  var queued = 148, world = 2600;
  var ic = function(d){ return '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#98A2B3" ' +
    'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + d + '</svg>'; };
  var big = function(n){ return n.toLocaleString ? n.toLocaleString("en-US") : String(n); };
  el.innerHTML =
    '<div>' + ic('<circle cx="12" cy="12" r="9"></circle><path d="M8.2 12.2l2.6 2.6 5-5.2"></path>') +
      '<b>' + brokers + '</b> \u0e15\u0e23\u0e27\u0e08\u0e41\u0e25\u0e49\u0e27</div>' +
    '<div>' + ic('<circle cx="12" cy="12" r="9"></circle><path d="M12 7.4V12l3.2 1.9"></path>') +
      '<b>' + queued + '</b> \u0e23\u0e2d\u0e04\u0e34\u0e27\u0e15\u0e23\u0e27\u0e08</div>' +
    '<div>' + ic('<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3c2.6 2.8 2.6 15 0 18M12 3c-2.6 2.8-2.6 15 0 18"></path>') +
      '<b>' + big(world) + '+</b> \u0e17\u0e31\u0e48\u0e27\u0e42\u0e25\u0e01\u0e17\u0e35\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e23\u0e27\u0e08</div>' +

    '<div>' + ic('<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3c2.6 2.8 2.6 15 0 18M12 3c-2.6 2.8-2.6 15 0 18"></path>') + '<b>' + countries + '</b> ประเทศที่เปิดตรวจ</div>' +
    '<div class="hd-fine">ตัวเลข รอคิวตรวจ และ ทั่วโลกที่ยังไม่ได้ตรวจ เป็นข้อมูลสมมติสำหรับงานออกแบบ</div>';
})();
document.addEventListener("change", function(ev){
  if (ev.target.id === "pk-region") { pkRegion = ev.target.value; pkIso = "all"; renderPicks(); return; }
  if (ev.target.id === "pk-iso") { pkIso = ev.target.value; renderPicks(); return; }
});
document.addEventListener("change", function(ev){
  if (ev.target.id === "rk-year") { rkYear = parseInt(ev.target.value, 10); rkRender(); return; }
  if (ev.target.id === "pk-year") { pkYear = parseInt(ev.target.value, 10); renderPicks(); return; }
});
renderPicks();
renderMovers();
/* ── วอลลุ่มการเทรด ─────────────────────────────────
   เลือกดูได้ว่าจะดูวอลลุ่มของสินทรัพย์ประเภทไหน สีบนแผนที่
   และตารางรายโซนเปลี่ยนตามทั้งคู่
   ทุกตัวเลขคำนวณจาก data-vshare × data-mix ที่ติดอยู่กับประเทศบนแผนที่จริง     */
(function(){
  var svg = document.querySelector(".map-svg");
  var host = document.getElementById("vol-zones");
  if (!svg || !host) { return; }
  var panel = svg.parentNode && svg.parentNode.parentNode && svg.parentNode.parentNode.parentNode;
  if (!panel) { return; }

  var ZN = {na:"North America", eu:"Europe", apac:"Asia Pacific",
            me:"Middle East", af:"Africa", sa:"South America"};
  var COL = {1:"#F7CFCB", 2:"#EDA49D", 3:"#E0655B", 4:"#B42318"};
  var VORDER = ["fx","futures","stocks","crypto","exchange","fund"];
  var nodes = [].slice.call(svg.querySelectorAll("[data-vshare]"));
  var allPaths = svg.querySelectorAll("path").length;
  if (!nodes.length) { return; }
  var volCat = "all", anQ = "";

  function catName(k){
    if (k === "all") { return "\u0e17\u0e38\u0e01\u0e2b\u0e21\u0e27\u0e14\u0e23\u0e27\u0e21\u0e01\u0e31\u0e19"; }
    return (typeof catShort === "function") ? catShort(k) : k;
  }
  function volOf(n, cat){
    var base = +n.dataset.vshare || 0;
    if (cat === "all") { return base; }
    var i = VORDER.indexOf(cat);
    var mix = (n.dataset.mix || "").split(",").map(Number);
    var sum = mix.reduce(function(a, b){ return a + (b || 0); }, 0);
    if (i < 0 || !sum || isNaN(mix[i])) { return base; }
    return base * mix[i] / sum;
  }
  /* ชั้นสีคิดจากส่วนแบ่ง ไม่ใช่อันดับ เพื่อให้สลับหมวดแล้วเห็นการเปลี่ยนจริง */
  function tierOf(p){ return p >= 5 ? 4 : p >= 1.5 ? 3 : p >= 0.4 ? 2 : 1; }

  function render(){
    var vals = nodes.map(function(n){ return volOf(n, volCat); });
    var total = vals.reduce(function(a, b){ return a + b; }, 0);
    if (!total) { return; }
    var pct = function(v){ return v / total * 100; };
    var tiers = {1:0, 2:0, 3:0, 4:0};
    nodes.forEach(function(n, i){
      var p = pct(vals[i]), t = tierOf(p);
      tiers[t]++;
      n.setAttribute("data-vol", t);
      var ttl = n.querySelector("title");
      if (!ttl) {
        ttl = document.createElementNS("http://www.w3.org/2000/svg", "title");
        n.appendChild(ttl);
      }
      ttl.textContent = n.dataset.name + " \u00b7 " + (ZN[n.dataset.zone] || "") + " \u00b7 " +
        catName(volCat) + " " + p.toFixed(1) + "%";
    });

    var key = document.getElementById("vol-key");
    var sw = [1,2,3,4].map(function(v){ return '<b style="background:' + COL[v] + '"></b>'; }).join("");
    key.innerHTML =
      '<span class="t">\u0e27\u0e2d\u0e25\u0e25\u0e38\u0e48\u0e21\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e02\u0e2d\u0e07</span>' +
      '<select id="vol-cat" aria-label="\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e1b\u0e23\u0e30\u0e40\u0e20\u0e17\u0e2a\u0e34\u0e19\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e4c\u0e17\u0e35\u0e48\u0e08\u0e30\u0e14\u0e39\u0e27\u0e2d\u0e25\u0e25\u0e38\u0e48\u0e21">' +
      ["all"].concat(VORDER).map(function(k){
        return '<option value="' + k + '"' + (k === volCat ? " selected" : "") + '>' + catName(k) + '</option>';
      }).join("") + '</select>' +
      '<span class="vol-scale"><span>\u0e15\u0e48\u0e33</span><i>' + sw + '</i><span>\u0e2a\u0e39\u0e07</span></span>' +
      '<span class="vol-na"><b></b>\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 ' + (allPaths - nodes.length) + ' \u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28</span>' +
      '<span>\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 ' + tiers[4] + ' \u00b7 \u0e2a\u0e39\u0e07 ' + tiers[3] + ' \u00b7 \u0e1b\u0e32\u0e19\u0e01\u0e25\u0e32\u0e07 ' + tiers[2] +
      ' \u00b7 \u0e15\u0e48\u0e33 ' + tiers[1] + ' \u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28</span>';
    var sel = document.getElementById("vol-cat");
    if (sel) { sel.addEventListener("change", function(e){ volCat = e.target.value; render(); }); }

    /* \u0e2b\u0e19\u0e49\u0e32 Trade Analytics \u2014 \u0e0a\u0e48\u0e2d\u0e07\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2b\u0e21\u0e27\u0e14\u0e02\u0e2d\u0e07\u0e15\u0e31\u0e27\u0e40\u0e2d\u0e07 + \u0e15\u0e32\u0e23\u0e32\u0e07\u0e23\u0e32\u0e22\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28 */
    var acat = document.getElementById("an-cat");
    if (acat) {
      acat.innerHTML = ["all"].concat(VORDER).map(function(k){
        return '<option value="' + k + '"' + (k === volCat ? " selected" : "") + '>' + catName(k) + '</option>';
      }).join("");
      if (!acat.dataset.wired) {
        acat.dataset.wired = "1";
        acat.addEventListener("change", function(e){ volCat = e.target.value; render(); });
      }
    }
    var aq = document.getElementById("an-q");
    if (aq && !aq.dataset.wired) {
      aq.dataset.wired = "1";
      aq.addEventListener("input", function(e){ anQ = e.target.value; render(); });
    }
    var tbl = document.getElementById("an-table");
    if (tbl) {
      var q = (anQ || "").trim().toLowerCase();
      var rowsIdx = nodes.map(function(n, i){ return i; })
        .filter(function(i){ return !q || nodes[i].dataset.name.toLowerCase().indexOf(q) >= 0; })
        .sort(function(a, b){ return vals[b] - vals[a]; });
      var top = vals.length ? Math.max.apply(null, vals) : 1;
      if (!rowsIdx.length) {
        tbl.innerHTML = '<div class="an-empty">\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e17\u0e35\u0e48\u0e15\u0e23\u0e07\u0e01\u0e31\u0e1a\u0e04\u0e33\u0e04\u0e49\u0e19\u0e19\u0e35\u0e49</div>';
      } else {
        tbl.innerHTML =
          '<div class="an-row hd"><span>\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a</span><span>\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28</span><span>\u0e42\u0e0b\u0e19</span>' +
          '<span>\u0e2a\u0e48\u0e27\u0e19\u0e41\u0e1a\u0e48\u0e07</span><span style="text-align:right">%</span></div>' +
          rowsIdx.map(function(i, k){
            var n = nodes[i], p2 = pct(vals[i]);
            return '<div class="an-row"><span class="an-rank">' + (k + 1) + '</span>' +
              '<span class="an-name"><i class="an-sw" style="background:' + COL[tierOf(p2)] + '"></i>' +
              n.dataset.name + '</span>' +
              '<span class="an-zone">' + (ZN[n.dataset.zone] || "") + '</span>' +
              '<span class="an-bar"><b style="width:' + (vals[i] / top * 100).toFixed(1) + '%"></b></span>' +
              '<span class="an-pct">' + p2.toFixed(2) + '%</span></div>';
          }).join("");
      }
      var an = document.getElementById("an-note");
      if (an) {
        an.innerHTML = '\u0e41\u0e2a\u0e14\u0e07 ' + rowsIdx.length + ' \u0e08\u0e32\u0e01 ' + nodes.length +
          ' \u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e17\u0e35\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 \u00b7 \u0e2b\u0e21\u0e27\u0e14' + catName(volCat) +
          ' \u00b7 \u0e2a\u0e35\u0e2b\u0e19\u0e49\u0e32\u0e0a\u0e37\u0e48\u0e2d\u0e04\u0e37\u0e2d\u0e0a\u0e31\u0e49\u0e19\u0e2a\u0e35\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e17\u0e35\u0e48\u0e23\u0e30\u0e1a\u0e32\u0e22\u0e1a\u0e19\u0e41\u0e1c\u0e19\u0e17\u0e35\u0e48' +
          ' \u00b7 <b>\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e27\u0e2d\u0e25\u0e25\u0e38\u0e48\u0e21\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e21\u0e21\u0e15\u0e34\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a</b>';
      }
    }

    var zones = Object.keys(ZN).map(function(k){
      var idx = [];
      nodes.forEach(function(n, i){ if (n.dataset.zone === k) { idx.push(i); } });
      return {n:ZN[k], cnt:idx.length,
              sum:idx.reduce(function(s, i){ return s + vals[i]; }, 0),
              top:idx.slice().sort(function(a, b){ return vals[b] - vals[a]; }).slice(0, 3)};
    }).filter(function(z){ return z.cnt; }).sort(function(a, b){ return b.sum - a.sum; });
    var max = zones[0].sum || 1;
    host.innerHTML =
      '<div class="vz-head"><h3>\u0e27\u0e2d\u0e25\u0e25\u0e38\u0e48\u0e21\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e23\u0e32\u0e22\u0e42\u0e0b\u0e19</h3>' +
        '<span class="vz-tag">' + catName(volCat) + '</span>' +
        '<span>\u0e44\u0e25\u0e48\u0e08\u0e32\u0e01\u0e42\u0e0b\u0e19\u0e17\u0e35\u0e48\u0e27\u0e2d\u0e25\u0e25\u0e38\u0e48\u0e21\u0e21\u0e32\u0e01\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14 \u00b7 \u0e2a\u0e48\u0e27\u0e19\u0e41\u0e1a\u0e48\u0e07\u0e04\u0e34\u0e14\u0e08\u0e32\u0e01 ' +
        nodes.length + ' \u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e17\u0e35\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1a\u0e19\u0e41\u0e1c\u0e19\u0e17\u0e35\u0e48</span></div>' +
      zones.map(function(z){
        return '<div class="vz-row">' +
          '<span class="vz-name">' + z.n + '<i>' + z.cnt + ' \u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28</i></span>' +
          '<span class="vz-bar"><b style="width:' + (z.sum / max * 100).toFixed(1) + '%"></b></span>' +
          '<span class="vz-pct">' + pct(z.sum).toFixed(1) + '%</span>' +
          '<span class="vz-top">' + z.top.map(function(i){
            return '<span><b>' + nodes[i].dataset.name + '</b> ' + pct(vals[i]).toFixed(1) + '%</span>';
          }).join("") + '</span></div>';
      }).join("") +
      '<p class="vz-note">\u0e0a\u0e48\u0e2d\u0e07\u0e02\u0e27\u0e32\u0e04\u0e37\u0e2d\u0e2a\u0e32\u0e21\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e17\u0e35\u0e48\u0e27\u0e2d\u0e25\u0e25\u0e38\u0e48\u0e21\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e02\u0e2d\u0e07\u0e42\u0e0b\u0e19\u0e19\u0e31\u0e49\u0e19\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14\u0e17\u0e35\u0e48\u0e40\u0e25\u0e37\u0e2d\u0e01 \u00b7 ' +
      '\u0e40\u0e1b\u0e2d\u0e23\u0e4c\u0e40\u0e0b\u0e47\u0e19\u0e15\u0e4c\u0e04\u0e34\u0e14\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e27\u0e2d\u0e25\u0e25\u0e38\u0e48\u0e21\u0e02\u0e2d\u0e07\u0e2b\u0e21\u0e27\u0e14\u0e19\u0e31\u0e49\u0e19\u0e23\u0e27\u0e21\u0e17\u0e38\u0e01\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e17\u0e35\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e17\u0e31\u0e49\u0e07\u0e42\u0e25\u0e01 \u00b7 ' +
      '\u0e0a\u0e35\u0e49\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e1a\u0e19\u0e41\u0e1c\u0e19\u0e17\u0e35\u0e48\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e14\u0e39\u0e2a\u0e48\u0e27\u0e19\u0e41\u0e1a\u0e48\u0e07\u0e23\u0e32\u0e22\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28<br>' +
      '<b>\u0e2a\u0e31\u0e14\u0e2a\u0e48\u0e27\u0e19\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e41\u0e15\u0e48\u0e25\u0e30\u0e2a\u0e34\u0e19\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e4c\u0e41\u0e25\u0e30\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e27\u0e2d\u0e25\u0e25\u0e38\u0e48\u0e21\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e21\u0e21\u0e15\u0e34\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e08\u0e23\u0e34\u0e07</b></p>';
  }

  if (!document.getElementById("vol-key")) {
    var el = document.createElement("div");
    el.id = "vol-key"; el.className = "vol-key";
    panel.appendChild(el);
  }
  render();
})();


/* ── บทความและข่าว ──────────────────────────────
   หัวข้อทั้งหมดเป็นตัวอย่างสำหรับงานออกแบบ ยังไม่มีเนื้อหาจริง จึงเขียนกำกับไว้ท้ายบล็อก
   หมวดใช้ชุดเดียวกับทั้งหน้า (CAT_ORDER)                                     */
var ARTICLES = [
  {c:"fx", d:"2026-06-04", m:7,
   t:"\u0e2a\u0e40\u0e1b\u0e23\u0e14\u0e15\u0e48\u0e33\u0e17\u0e35\u0e48\u0e42\u0e06\u0e29\u0e13\u0e32\u0e01\u0e31\u0e1a\u0e2a\u0e40\u0e1b\u0e23\u0e14\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49\u0e08\u0e23\u0e34\u0e07 \u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e15\u0e23\u0e07\u0e44\u0e2b\u0e19",
   x:"\u0e2a\u0e40\u0e1b\u0e23\u0e14\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e17\u0e35\u0e48\u0e40\u0e23\u0e32\u0e27\u0e31\u0e14\u0e16\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e15\u0e32\u0e21\u0e40\u0e27\u0e25\u0e32 \u0e21\u0e31\u0e01\u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e17\u0e35\u0e48\u0e02\u0e36\u0e49\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e27\u0e47\u0e1a \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e42\u0e06\u0e29\u0e13\u0e32\u0e21\u0e31\u0e01\u0e40\u0e01\u0e47\u0e1a\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e0a\u0e48\u0e27\u0e07\u0e17\u0e35\u0e48\u0e2a\u0e20\u0e32\u0e1e\u0e04\u0e25\u0e48\u0e2d\u0e07\u0e14\u0e35\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14"},
  {c:"fx", d:"2026-05-30", m:6,
   t:"\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e22\u0e49\u0e32\u0e22\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15\u0e1a\u0e48\u0e2d\u0e22 \u0e1a\u0e2d\u0e01\u0e2d\u0e30\u0e44\u0e23\u0e40\u0e23\u0e32\u0e44\u0e14\u0e49\u0e1a\u0e49\u0e32\u0e07",
   x:"\u0e01\u0e32\u0e23\u0e22\u0e49\u0e32\u0e22\u0e40\u0e02\u0e15\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e41\u0e22\u0e48\u0e40\u0e2a\u0e21\u0e2d\u0e44\u0e1b \u0e41\u0e15\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e2d\u0e48\u0e32\u0e19\u0e04\u0e39\u0e48\u0e01\u0e31\u0e1a\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e02\u0e2d\u0e07\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e17\u0e35\u0e48\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e23\u0e34\u0e07"},
  {c:"fx", d:"2026-05-21", m:8,
   t:"\u0e23\u0e35\u0e42\u0e04\u0e27\u0e15\u0e41\u0e25\u0e30\u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08 \u0e27\u0e31\u0e14\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e44\u0e23\u0e43\u0e2b\u0e49\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e19\u0e44\u0e14\u0e49",
   x:"\u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e02\u0e19\u0e32\u0e14\u0e2d\u0e2d\u0e40\u0e14\u0e2d\u0e23\u0e4c \u0e0a\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32 \u0e41\u0e25\u0e30\u0e04\u0e39\u0e48\u0e40\u0e07\u0e34\u0e19\u0e43\u0e2b\u0e49\u0e15\u0e23\u0e07\u0e01\u0e31\u0e19 \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08\u0e08\u0e30\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e40\u0e25\u0e22"},
  {c:"fx", d:"2026-05-12", m:5,
   t:"\u0e2a\u0e27\u0e2d\u0e1b\u0e02\u0e49\u0e32\u0e21\u0e04\u0e37\u0e19 \u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e17\u0e35\u0e48\u0e04\u0e19\u0e16\u0e37\u0e2d\u0e22\u0e32\u0e27\u0e21\u0e31\u0e01\u0e21\u0e2d\u0e07\u0e02\u0e49\u0e32\u0e21",
   x:"\u0e04\u0e34\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e15\u0e48\u0e2d\u0e1b\u0e35\u0e41\u0e25\u0e49\u0e27\u0e2a\u0e27\u0e2d\u0e1b\u0e21\u0e31\u0e01\u0e43\u0e2b\u0e0d\u0e48\u0e01\u0e27\u0e48\u0e32\u0e2a\u0e40\u0e1b\u0e23\u0e14\u0e2b\u0e25\u0e32\u0e22\u0e40\u0e17\u0e48\u0e32 \u0e42\u0e14\u0e22\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e04\u0e39\u0e48\u0e2a\u0e01\u0e38\u0e25\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e01\u0e27\u0e49\u0e32\u0e07"},
  {c:"stocks", d:"2026-06-02", m:6,
   t:"\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e17\u0e35\u0e48\u0e21\u0e2d\u0e07\u0e44\u0e21\u0e48\u0e40\u0e2b\u0e47\u0e19\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e48\u0e32\u0e07\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28 \u0e04\u0e37\u0e2d\u0e04\u0e48\u0e32\u0e41\u0e1b\u0e25\u0e07\u0e2a\u0e01\u0e38\u0e25\u0e40\u0e07\u0e34\u0e19",
   x:"\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e40\u0e1b\u0e47\u0e19\u0e28\u0e39\u0e19\u0e22\u0e4c \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e40\u0e17\u0e23\u0e14\u0e1f\u0e23\u0e35 \u0e25\u0e2d\u0e07\u0e14\u0e39\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07\u0e17\u0e35\u0e48\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e1a\u0e27\u0e01\u0e40\u0e02\u0e49\u0e32\u0e01\u0e31\u0e1a\u0e2d\u0e31\u0e15\u0e23\u0e01\u0e25\u0e32\u0e07"},
  {c:"stocks", d:"2026-05-26", m:7,
   t:"\u0e41\u0e1e\u0e25\u0e15\u0e1f\u0e2d\u0e23\u0e4c\u0e21\u0e2b\u0e38\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e44\u0e21\u0e48\u0e21\u0e35\u0e04\u0e48\u0e32\u0e04\u0e2d\u0e21 \u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e21\u0e32\u0e08\u0e32\u0e01\u0e44\u0e2b\u0e19",
   x:"\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e44\u0e21\u0e48\u0e40\u0e01\u0e47\u0e1a\u0e04\u0e48\u0e32\u0e04\u0e2d\u0e21 \u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e32\u0e08\u0e32\u0e01\u0e17\u0e32\u0e07\u0e2d\u0e37\u0e48\u0e19 \u0e02\u0e49\u0e2d\u0e19\u0e35\u0e49\u0e04\u0e37\u0e2d\u0e2a\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e14\u0e49\u0e32\u0e19\u0e04\u0e27\u0e32\u0e21\u0e42\u0e1b\u0e23\u0e48\u0e07\u0e43\u0e2a\u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32\u0e15\u0e49\u0e2d\u0e07\u0e15\u0e2d\u0e1a\u0e43\u0e2b\u0e49\u0e44\u0e14\u0e49"},
  {c:"stocks", d:"2026-05-15", m:9,
   t:"\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e41\u0e1e\u0e25\u0e15\u0e1f\u0e2d\u0e23\u0e4c\u0e21\u0e2b\u0e38\u0e49\u0e19\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e1e\u0e2d\u0e23\u0e4c\u0e15\u0e2b\u0e25\u0e32\u0e22\u0e2a\u0e01\u0e38\u0e25\u0e40\u0e07\u0e34\u0e19",
   x:"\u0e16\u0e37\u0e2d\u0e2b\u0e25\u0e32\u0e22\u0e2a\u0e01\u0e38\u0e25\u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19 \u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e17\u0e35\u0e48\u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e08\u0e23\u0e34\u0e07 \u0e46 \u0e2d\u0e22\u0e39\u0e48\u0e17\u0e35\u0e48\u0e04\u0e48\u0e32\u0e41\u0e1b\u0e25\u0e07\u0e2a\u0e01\u0e38\u0e25\u0e41\u0e25\u0e30\u0e04\u0e48\u0e32\u0e14\u0e39\u0e41\u0e25\u0e1a\u0e31\u0e0d\u0e0a\u0e35 \u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e15\u0e48\u0e2d\u0e04\u0e23\u0e31\u0e49\u0e07"},
  {c:"exchange", d:"2026-06-03", m:8,
   t:"Proof of Reserves \u0e2d\u0e48\u0e32\u0e19\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e44\u0e23\u0e43\u0e2b\u0e49\u0e44\u0e21\u0e48\u0e16\u0e39\u0e01\u0e2b\u0e25\u0e2d\u0e01",
   x:"\u0e01\u0e32\u0e23\u0e21\u0e35\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e1e\u0e08 Proof of Reserves \u0e44\u0e21\u0e48\u0e40\u0e17\u0e48\u0e32\u0e01\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e2b\u0e19\u0e35\u0e49\u0e2a\u0e34\u0e19 \u0e2a\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e14\u0e39\u0e04\u0e37\u0e2d\u0e02\u0e2d\u0e1a\u0e40\u0e02\u0e15\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08\u0e41\u0e25\u0e30\u0e04\u0e27\u0e32\u0e21\u0e16\u0e35\u0e48"},
  {c:"exchange", d:"2026-05-28", m:5,
   t:"Maker \u0e01\u0e31\u0e1a Taker \u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e15\u0e23\u0e07\u0e44\u0e2b\u0e19 \u0e41\u0e25\u0e30\u0e21\u0e35\u0e1c\u0e25\u0e01\u0e31\u0e1a\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e41\u0e04\u0e48\u0e44\u0e2b\u0e19",
   x:"\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e2a\u0e2d\u0e07\u0e1d\u0e31\u0e48\u0e07\u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e2b\u0e25\u0e32\u0e22\u0e40\u0e17\u0e48\u0e32 \u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e04\u0e19\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e15\u0e25\u0e32\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e2b\u0e25\u0e31\u0e01 \u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07\u0e19\u0e35\u0e49\u0e01\u0e34\u0e19\u0e01\u0e33\u0e44\u0e23\u0e44\u0e14\u0e49\u0e21\u0e32\u0e01"},
  {c:"exchange", d:"2026-05-19", m:6,
   t:"\u0e04\u0e48\u0e32\u0e16\u0e2d\u0e19\u0e2d\u0e2d\u0e19\u0e40\u0e0a\u0e19 \u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e17\u0e35\u0e48\u0e21\u0e31\u0e01\u0e44\u0e21\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e15\u0e32\u0e23\u0e32\u0e07\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e40\u0e17\u0e35\u0e22\u0e1a",
   x:"\u0e40\u0e17\u0e23\u0e14\u0e16\u0e39\u0e01\u0e41\u0e15\u0e48\u0e16\u0e2d\u0e19\u0e41\u0e1e\u0e07 \u0e2a\u0e38\u0e14\u0e17\u0e49\u0e32\u0e22\u0e01\u0e47\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e16\u0e39\u0e01 \u2014 \u0e27\u0e34\u0e18\u0e35\u0e19\u0e31\u0e1a\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21\u0e15\u0e25\u0e2d\u0e14\u0e17\u0e31\u0e49\u0e07\u0e23\u0e2d\u0e1a\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14"},
  {c:"futures", d:"2026-05-24", m:7,
   t:"\u0e04\u0e48\u0e32\u0e04\u0e2d\u0e21\u0e15\u0e48\u0e2d\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14",
   x:"\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e15\u0e25\u0e32\u0e14\u0e41\u0e25\u0e30\u0e04\u0e48\u0e32\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e23\u0e32\u0e04\u0e32\u0e23\u0e27\u0e21\u0e01\u0e31\u0e19\u0e21\u0e31\u0e01\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e04\u0e2d\u0e21\u0e17\u0e35\u0e48\u0e42\u0e06\u0e29\u0e13\u0e32 \u0e42\u0e14\u0e22\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e04\u0e19\u0e40\u0e17\u0e23\u0e14\u0e44\u0e21\u0e48\u0e16\u0e35\u0e48"},
  {c:"crypto", d:"2026-05-17", m:6,
   t:"\u0e04\u0e23\u0e34\u0e1b\u0e42\u0e15 CFD \u0e01\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e16\u0e37\u0e2d\u0e40\u0e2b\u0e23\u0e35\u0e22\u0e0d\u0e08\u0e23\u0e34\u0e07 \u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e17\u0e35\u0e48\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e2d\u0e30\u0e44\u0e23",
   x:"\u0e2a\u0e2d\u0e07\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e19\u0e35\u0e49\u0e2d\u0e22\u0e39\u0e48\u0e04\u0e19\u0e25\u0e30\u0e01\u0e0e\u0e2b\u0e21\u0e32\u0e22 \u0e04\u0e19\u0e25\u0e30\u0e42\u0e04\u0e23\u0e07\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19 \u0e41\u0e25\u0e30\u0e04\u0e19\u0e25\u0e30\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e1c\u0e39\u0e49\u0e43\u0e2b\u0e49\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23\u0e21\u0e35\u0e1b\u0e31\u0e0d\u0e2b\u0e32"},
  {c:"fund", d:"2026-05-31", m:7,
   t:"\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e23\u0e32\u0e22\u0e1b\u0e35\u0e01\u0e34\u0e19\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e44\u0e1b\u0e40\u0e17\u0e48\u0e32\u0e44\u0e23\u0e43\u0e19\u0e2a\u0e34\u0e1a\u0e1b\u0e35",
   x:"\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e2b\u0e25\u0e31\u0e01\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e17\u0e28\u0e19\u0e34\u0e22\u0e21\u0e14\u0e39\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e19\u0e49\u0e2d\u0e22 \u0e41\u0e15\u0e48\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e17\u0e1a\u0e15\u0e49\u0e19\u0e2b\u0e25\u0e32\u0e22\u0e1b\u0e35\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07\u0e08\u0e30\u0e0a\u0e31\u0e14\u0e02\u0e36\u0e49\u0e19\u0e21\u0e32\u0e01"},
  {c:"fund", d:"2026-05-08", m:5,
   t:"\u0e41\u0e1e\u0e25\u0e15\u0e1f\u0e2d\u0e23\u0e4c\u0e21\u0e01\u0e2d\u0e07\u0e17\u0e38\u0e19\u0e04\u0e34\u0e14\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e0b\u0e49\u0e2d\u0e19\u0e01\u0e31\u0e19\u0e01\u0e35\u0e48\u0e0a\u0e31\u0e49\u0e19",
   x:"\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23 \u0e04\u0e48\u0e32\u0e41\u0e23\u0e01\u0e40\u0e02\u0e49\u0e32 \u0e04\u0e48\u0e32\u0e02\u0e32\u0e22\u0e04\u0e37\u0e19 \u0e41\u0e25\u0e30\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e41\u0e1e\u0e25\u0e15\u0e1f\u0e2d\u0e23\u0e4c\u0e21 \u2014 \u0e23\u0e27\u0e21\u0e41\u0e25\u0e49\u0e27\u0e08\u0e48\u0e32\u0e22\u0e08\u0e23\u0e34\u0e07\u0e40\u0e17\u0e48\u0e32\u0e44\u0e23"}
];
/* \u0e20\u0e32\u0e1e\u0e1b\u0e23\u0e30\u0e01\u0e2d\u0e1a\u0e02\u0e48\u0e32\u0e27 \u2014 \u0e27\u0e32\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e27\u0e01\u0e40\u0e15\u0e2d\u0e23\u0e4c\u0e43\u0e19\u0e44\u0e1f\u0e25\u0e4c \u0e44\u0e21\u0e48\u0e42\u0e2b\u0e25\u0e14\u0e08\u0e32\u0e01\u0e20\u0e32\u0e22\u0e19\u0e2d\u0e01 */
var ART_ART = {
  chart:
    '<g stroke="#3B4657" stroke-width="1"><path d="M40 48h320M40 92h320M40 136h320M40 180h320"/></g>' +
    '<g stroke="#98A2B3" stroke-width="2" stroke-linecap="round">' +
      '<path d="M70 60v96M105 78v72M140 52v88M175 92v66"/></g>' +
    '<g stroke="#F97066" stroke-width="2" stroke-linecap="round">' +
      '<path d="M210 70v84M245 100v58M280 62v80M315 84v70"/></g>' +
    '<g fill="#101828" stroke="#98A2B3" stroke-width="2">' +
      '<rect x="62" y="80" width="16" height="46" rx="2"/><rect x="97" y="96" width="16" height="34" rx="2"/>' +
      '<rect x="132" y="70" width="16" height="50" rx="2"/><rect x="167" y="108" width="16" height="34" rx="2"/></g>' +
    '<g fill="#101828" stroke="#F97066" stroke-width="2">' +
      '<rect x="202" y="86" width="16" height="46" rx="2"/><rect x="237" y="112" width="16" height="30" rx="2"/>' +
      '<rect x="272" y="76" width="16" height="52" rx="2"/><rect x="307" y="98" width="16" height="40" rx="2"/></g>' +
    '<rect x="40" y="104" width="320" height="14" fill="#D92D20" opacity="0.28"/>' +
    '<path d="M40 104h320M40 118h320" stroke="#D92D20" stroke-width="1.4" stroke-dasharray="5 5"/>',
  shield:
    '<path d="M200 34l66 25v48c0 42-27 75-66 87-39-12-66-45-66-87V59z" fill="none" stroke="#98A2B3" stroke-width="2.4"/>' +
    '<path d="M174 120l18 18 36-42" fill="none" stroke="#F97066" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>' +
    '<g stroke="#475467" stroke-width="2.2" stroke-linecap="round">' +
      '<path d="M42 74h58M42 98h42M42 122h50M300 74h58M316 98h42M308 122h50"/></g>',
  scatter:
    '<path d="M40 110h320" stroke="#D92D20" stroke-width="1.8" stroke-dasharray="7 6"/>' +
    '<g fill="#98A2B3"><circle cx="72" cy="98" r="5"/><circle cx="110" cy="118" r="5"/>' +
      '<circle cx="148" cy="104" r="5"/><circle cx="186" cy="122" r="5"/><circle cx="224" cy="100" r="5"/></g>' +
    '<g fill="#F97066"><circle cx="262" cy="142" r="7"/><circle cx="300" cy="74" r="7"/><circle cx="336" cy="150" r="7"/></g>' +
    '<g stroke="#3B4657" stroke-width="1.4"><path d="M262 110v32M300 110V74M336 110v40"/></g>',
  calendar:
    '<rect x="108" y="48" width="184" height="132" rx="13" fill="none" stroke="#98A2B3" stroke-width="2.4"/>' +
    '<path d="M108 86h184" stroke="#98A2B3" stroke-width="2.4"/>' +
    '<path d="M148 34v26M252 34v26" stroke="#98A2B3" stroke-width="3.2" stroke-linecap="round"/>' +
    '<g fill="#475467"><circle cx="140" cy="110" r="6"/><circle cx="180" cy="110" r="6"/>' +
      '<circle cx="220" cy="110" r="6"/><circle cx="140" cy="146" r="6"/><circle cx="220" cy="146" r="6"/>' +
      '<circle cx="260" cy="146" r="6"/></g>' +
    '<circle cx="260" cy="110" r="10" fill="#D92D20"/>' +
    '<circle cx="180" cy="146" r="10" fill="#D92D20" opacity="0.5"/>',
  swap:
    '<circle cx="128" cy="110" r="40" fill="none" stroke="#98A2B3" stroke-width="2.4"/>' +
    '<circle cx="272" cy="110" r="40" fill="none" stroke="#F97066" stroke-width="2.4"/>' +
    '<path d="M128 88v44M114 100h28M114 120h28" stroke="#98A2B3" stroke-width="2.4" stroke-linecap="round"/>' +
    '<path d="M272 86v48M258 102h28M258 118h28" stroke="#F97066" stroke-width="2.4" stroke-linecap="round"/>' +
    '<path d="M180 94h44l-10-10M220 128h-44l10 10" fill="none" stroke="#D92D20" stroke-width="2.8" ' +
      'stroke-linecap="round" stroke-linejoin="round"/>',
  flow:
    '<path d="M92 46h216l-58 68v58l-100 34v-92z" fill="none" stroke="#98A2B3" stroke-width="2.4" stroke-linejoin="round"/>' +
    '<g stroke="#475467" stroke-width="2.2" stroke-linecap="round">' +
      '<path d="M36 58h34M36 82h34M36 106h34M330 58h34M330 82h34"/></g>' +
    '<circle cx="200" cy="188" r="8" fill="#D92D20"/>' +
    '<path d="M200 150v22" stroke="#D92D20" stroke-width="2.4" stroke-linecap="round"/>',
  globe:
    '<circle cx="200" cy="106" r="66" fill="none" stroke="#98A2B3" stroke-width="2.4"/>' +
    '<path d="M134 106h132M200 40c27 29 27 104 0 132M200 40c-27 29-27 104 0 132M146 72h108M146 140h108" ' +
      'fill="none" stroke="#3B4657" stroke-width="1.8"/>' +
    '<circle cx="168" cy="82" r="7" fill="#D92D20"/><circle cx="238" cy="126" r="7" fill="#F97066"/>' +
    '<g fill="#475467"><rect x="42" y="150" width="14" height="30" rx="3"/><rect x="64" y="134" width="14" height="46" rx="3"/></g>' +
    '<g fill="#98A2B3"><rect x="322" y="142" width="14" height="38" rx="3"/><rect x="344" y="122" width="14" height="58" rx="3"/></g>',
  vault:
    '<rect x="116" y="42" width="168" height="140" rx="15" fill="none" stroke="#98A2B3" stroke-width="2.4"/>' +
    '<circle cx="200" cy="112" r="40" fill="none" stroke="#98A2B3" stroke-width="2.4"/>' +
    '<circle cx="200" cy="112" r="15" fill="none" stroke="#F97066" stroke-width="2.6"/>' +
    '<path d="M200 72V56M200 168v-16M160 112h-16M256 112h-16" stroke="#475467" stroke-width="2.8" stroke-linecap="round"/>' +
    '<g stroke="#475467" stroke-width="2.2" stroke-linecap="round"><path d="M40 84h50M40 108h34M40 132h44"/></g>' +
    '<path d="M306 128l16 16 32-38" fill="none" stroke="#D92D20" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>',
  ladder:
    '<path d="M200 34v152" stroke="#475467" stroke-width="1.6" stroke-dasharray="5 5"/>' +
    '<g fill="#475467"><rect x="96" y="48" width="96" height="14" rx="3"/><rect x="126" y="70" width="66" height="14" rx="3"/>' +
      '<rect x="66" y="92" width="126" height="14" rx="3"/><rect x="140" y="114" width="52" height="14" rx="3"/>' +
      '<rect x="110" y="136" width="82" height="14" rx="3"/><rect x="150" y="158" width="42" height="14" rx="3"/></g>' +
    '<g fill="#D92D20" opacity="0.85"><rect x="208" y="48" width="58" height="14" rx="3"/>' +
      '<rect x="208" y="70" width="104" height="14" rx="3"/><rect x="208" y="92" width="72" height="14" rx="3"/>' +
      '<rect x="208" y="114" width="128" height="14" rx="3"/><rect x="208" y="136" width="60" height="14" rx="3"/>' +
      '<rect x="208" y="158" width="96" height="14" rx="3"/></g>',
  chain:
    '<g fill="none" stroke="#98A2B3" stroke-width="2.4">' +
      '<rect x="58" y="84" width="56" height="56" rx="12"/><rect x="172" y="84" width="56" height="56" rx="12"/></g>' +
    '<rect x="286" y="84" width="56" height="56" rx="12" fill="none" stroke="#F97066" stroke-width="2.4"/>' +
    '<path d="M114 112h58M228 112h58" stroke="#475467" stroke-width="2.6"/>' +
    '<g stroke="#3B4657" stroke-width="1.8"><path d="M72 100h28M72 112h20M186 100h28M186 112h20M300 100h28M300 112h20"/></g>' +
    '<circle cx="314" cy="62" r="12" fill="#D92D20"/>' +
    '<path d="M310 62h8M314 58v8" stroke="#101828" stroke-width="2.2" stroke-linecap="round"/>',
  stack:
    '<path d="M62 182h276" stroke="#98A2B3" stroke-width="2.2" stroke-linecap="round"/>' +
    '<rect x="84" y="138" width="232" height="30" rx="6" fill="#475467"/>' +
    '<rect x="108" y="100" width="184" height="30" rx="6" fill="#667085"/>' +
    '<rect x="132" y="62" width="136" height="30" rx="6" fill="#D92D20"/>' +
    '<g stroke="#3B4657" stroke-width="1.6" stroke-dasharray="4 4"><path d="M84 130h232M108 92h184"/></g>',
  split:
    '<rect x="46" y="50" width="142" height="118" rx="13" fill="none" stroke="#98A2B3" stroke-width="2.4"/>' +
    '<rect x="212" y="50" width="142" height="118" rx="13" fill="none" stroke="#F97066" stroke-width="2.4"/>' +
    '<path d="M70 138l30-34 24 20 40-46" fill="none" stroke="#98A2B3" stroke-width="2.8" ' +
      'stroke-linecap="round" stroke-linejoin="round"/>' +
    '<circle cx="283" cy="109" r="32" fill="none" stroke="#F97066" stroke-width="2.8"/>' +
    '<path d="M283 88v42M269 99h28M269 119h28" stroke="#F97066" stroke-width="2.4" stroke-linecap="round"/>' +
    '<path d="M200 46v128" stroke="#3B4657" stroke-width="1.6" stroke-dasharray="5 5"/>',
  curve:
    '<path d="M56 178h292M56 178V38" stroke="#98A2B3" stroke-width="2.2" stroke-linecap="round"/>' +
    '<path d="M56 162C132 142 214 96 342 50L342 92C214 122 132 150 56 166Z" fill="#D92D20" opacity="0.22"/>' +
    '<path d="M56 162C132 142 214 96 342 50" fill="none" stroke="#98A2B3" stroke-width="2.8" stroke-linecap="round"/>' +
    '<path d="M56 166C132 150 214 122 342 92" fill="none" stroke="#F97066" stroke-width="2.8" stroke-linecap="round"/>' +
    '<circle cx="342" cy="50" r="6" fill="#98A2B3"/><circle cx="342" cy="92" r="6" fill="#F97066"/>',
  rings:
    '<circle cx="200" cy="108" r="72" fill="none" stroke="#3B4657" stroke-width="12"/>' +
    '<circle cx="200" cy="108" r="54" fill="none" stroke="#475467" stroke-width="12"/>' +
    '<circle cx="200" cy="108" r="36" fill="none" stroke="#D92D20" stroke-width="12"/>' +
    '<circle cx="200" cy="108" r="15" fill="none" stroke="#98A2B3" stroke-width="4"/>' +
    '<g stroke="#667085" stroke-width="1.8" stroke-dasharray="4 5"><path d="M200 108L346 40M200 108L346 176"/></g>'
};
/* \u0e1a\u0e17\u0e17\u0e35\u0e48 i \u0e43\u0e0a\u0e49\u0e20\u0e32\u0e1e\u0e41\u0e1a\u0e1a\u0e44\u0e2b\u0e19 \u2014 \u0e40\u0e23\u0e35\u0e22\u0e07\u0e15\u0e32\u0e21\u0e25\u0e33\u0e14\u0e31\u0e1a\u0e02\u0e2d\u0e07 ARTICLES */
var ART_KIND = ["chart","shield","scatter","calendar","swap","flow","globe",
                "vault","ladder","chain","stack","split","curve","rings"];
function artArt(i){
  var k = ART_KIND[i % ART_KIND.length];
  return '<svg class="art-art" viewBox="0 0 400 220" preserveAspectRatio="xMidYMid slice" ' +
    'fill="none" aria-hidden="true">' + (ART_ART[k] || "") + '</svg>';
}
var TH_MON = ["\u0e21.\u0e04.","\u0e01.\u0e1e.","\u0e21\u0e35.\u0e04.","\u0e40\u0e21.\u0e22.","\u0e1e.\u0e04.","\u0e21\u0e34.\u0e22.",
              "\u0e01.\u0e04.","\u0e2a.\u0e04.","\u0e01.\u0e22.","\u0e15.\u0e04.","\u0e1e.\u0e22.","\u0e18.\u0e04."];
var artCat = "all", artQ = "";
function artDate(s){
  var p = s.split("-");
  return parseInt(p[2], 10) + " " + TH_MON[parseInt(p[1], 10) - 1] + " " + p[0];
}
function artStar(){
  return '<span class="art-star">' + awardStar(21) + '</span>';
}
function artCatName(k){ return k === "all" ? "\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14" : catShort(k); }
function artList(){
  var q = artQ.trim().toLowerCase();
  return ARTICLES.filter(function(a){
    if (artCat !== "all" && a.c !== artCat) { return false; }
    if (!q) { return true; }
    return (a.t + " " + a.x).toLowerCase().indexOf(q) >= 0;
  }).sort(function(a, b){ return a.d < b.d ? 1 : a.d > b.d ? -1 : 0; });
}
function artRender(){
  ["art-cats", "arth-cats"].forEach(function(hostId){
  var cats = document.getElementById(hostId);
  if (cats) {
    cats.innerHTML = ["all"].concat(CAT_ORDER).map(function(k){
      var n = k === "all" ? ARTICLES.length
            : ARTICLES.filter(function(a){ return a.c === k; }).length;
      return '<button type="button" class="art-cat" data-artcat="' + k + '"' +
        ' aria-pressed="' + (k === artCat) + '"' + (n ? "" : " disabled style=\'opacity:.4;cursor:not-allowed\'") +
        '>' + artCatName(k) + '</button>';
    }).join("");
  }
  });
  var list = artList();
  artGridInto("art-grid", list);
  artGridInto("arth-grid", list.slice(0, 5));
  artNoteInto("art-note", list.length, "");
  artNoteInto("arth-note", Math.min(list.length, 5),
    list.length > 5 ? " \u00b7 \u0e14\u0e39\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e17\u0e35\u0e48\u0e2b\u0e19\u0e49\u0e32 News" : "");
}
function artNoteInto(id, shown, extra){
  var note = document.getElementById(id);
  if (!note) { return; }
  note.innerHTML = '\u0e41\u0e2a\u0e14\u0e07 ' + shown + ' \u0e08\u0e32\u0e01 ' + ARTICLES.length + ' \u0e1a\u0e17' +
    (artCat === "all" ? "" : ' \u00b7 \u0e2b\u0e21\u0e27\u0e14' + catShort(artCat)) +
    (artQ.trim() ? ' \u00b7 \u0e04\u0e33\u0e04\u0e49\u0e19 \u201c' + artQ.trim() + '\u201d' : '') + extra +
    ' \u00b7 <b>\u0e1a\u0e17\u0e04\u0e27\u0e32\u0e21\u0e43\u0e19\u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e19\u0e37\u0e49\u0e2d\u0e2b\u0e32\u0e08\u0e23\u0e34\u0e07</b>';
}
function artGridInto(id, list){
  var grid = document.getElementById(id);
  if (!grid) { return; }
  if (!list.length) {
    grid.innerHTML = '<div class="art-empty">\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e1a\u0e17\u0e04\u0e27\u0e32\u0e21\u0e17\u0e35\u0e48\u0e15\u0e23\u0e07\u0e01\u0e31\u0e1a\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e19\u0e35\u0e49<br>' +
      '\u0e25\u0e2d\u0e07\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e2b\u0e21\u0e27\u0e14 \u0e2b\u0e23\u0e37\u0e2d\u0e25\u0e49\u0e32\u0e07\u0e04\u0e33\u0e04\u0e49\u0e19\u0e2b\u0e32</div>';
    return;
  }
  {
    grid.innerHTML = list.map(function(a, i){
      var kind = i > 0 ? "" : (list.length === 1 ? " feat solo" : " feat");
      return '<article class="art-card' + kind + '" role="link" tabindex="0" data-article="' + i + '">' +
        '<div class="art-cover">' + artArt(ARTICLES.indexOf(a)) +
        '<span class="art-badge">' + catShort(a.c) + '</span>' +
        artStar() + '<span class="art-mk">RedStarTrust</span></div>' +
        '<div class="art-body">' +
          '<span class="art-meta">' +
            '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#667085" stroke-width="2" ' +
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
            '<circle cx="12" cy="12" r="8.6"></circle><path d="M12 7.6V12l3 1.8"></path></svg>' +
            artDate(a.d) + ' \u00b7 \u0e2d\u0e48\u0e32\u0e19 ' + a.m + ' \u0e19\u0e32\u0e17\u0e35</span>' +
          '<h3 class="art-title">' + a.t + '</h3>' +
          '<p class="art-ex">' + a.x + '</p>' +
          '<span class="art-more">\u0e2d\u0e48\u0e32\u0e19\u0e1a\u0e17\u0e04\u0e27\u0e32\u0e21' +
            '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" ' +
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
            '<path d="M5 12h13M13 6.5l5.5 5.5L13 17.5"></path></svg></span>' +
        '</div></article>';
    }).join("");
  }
}
document.addEventListener("click", function(ev){
  var c = ev.target.closest("[data-artcat]");
  if (c && !c.disabled) { artCat = c.dataset.artcat; artRender(); return; }
  var a = ev.target.closest("[data-article]");
  if (a) { ev.preventDefault(); }
});
document.addEventListener("keydown", function(ev){
  if (ev.key !== "Enter" && ev.key !== " ") { return; }
  var t = ev.target.closest("[data-article], [data-artcat]");
  if (t) { ev.preventDefault(); t.click(); }
});
(function(){
  var q = document.getElementById("art-q");
  if (q) { q.addEventListener("input", function(e){ artQ = e.target.value; artRender(); }); }
  artRender();
})();

/* BEGIN-MAPZOOM */
(function(){
  var stage = document.getElementById("map-stage"), pan = document.getElementById("map-pan");
  if (!stage || !pan) { return; }
  var W = 752, H = 342, z = 1, tx = 0, ty = 0, MINZ = 1, MAXZ = 6;
  var drag = null;
  function clamp(){
    var maxX = 0, minX = W - W * z, maxY = 0, minY = H - H * z;
    tx = Math.min(maxX, Math.max(minX, tx));
    ty = Math.min(maxY, Math.max(minY, ty));
  }
  function apply(){
    clamp();
    pan.style.transform = "translate(" + tx.toFixed(1) + "px," + ty.toFixed(1) + "px) scale(" + z.toFixed(3) + ")";
    /* หมุดถูกขยายไปพร้อมชั้นแพน จึงหดกลับให้เท่าเดิม แต่ตำแหน่งยังถูกต้อง */
    var pins = pan.querySelectorAll("[data-pin]");
    for (var i = 0; i < pins.length; i++) {
      var p = pins[i], flip = p.hasAttribute("data-flip");
      p.style.transform = "translate(-50%," + (flip ? "0" : "-100%") + ") scale(" + (1 / z).toFixed(3) + ")";
      p.style.transformOrigin = flip ? "50% 0" : "50% 100%";
    }
    document.getElementById("zoom-in").disabled = z >= MAXZ - 0.001;
    document.getElementById("zoom-out").disabled = z <= MINZ + 0.001;
    document.getElementById("zoom-reset").disabled = (z === 1 && tx === 0 && ty === 0);
  }
  function zoomAt(nz, cx, cy){
    nz = Math.min(MAXZ, Math.max(MINZ, nz));
    if (nz === z) { return; }
    tx = cx - (cx - tx) * (nz / z);
    ty = cy - (cy - ty) * (nz / z);
    z = nz; apply();
  }
  document.getElementById("zoom-in").addEventListener("click", function(){ zoomAt(z * 1.6, W/2, H/2); });
  document.getElementById("zoom-out").addEventListener("click", function(){ zoomAt(z / 1.6, W/2, H/2); });
  document.getElementById("zoom-reset").addEventListener("click", function(){ z = 1; tx = 0; ty = 0; apply(); });
  stage.addEventListener("wheel", function(e){
    if (e.ctrlKey) { return; }
    e.preventDefault();
    var r = stage.getBoundingClientRect(), sc = W / r.width;
    zoomAt(z * (e.deltaY < 0 ? 1.18 : 1/1.18), (e.clientX - r.left) * sc, (e.clientY - r.top) * sc);
  }, {passive:false});
  stage.addEventListener("pointerdown", function(e){
    if (e.target.closest(".mapzoom") || e.target.closest("[data-pin]")) { return; }
    drag = {x:e.clientX, y:e.clientY, tx:tx, ty:ty};
    stage.classList.add("dragging");
    stage.setPointerCapture(e.pointerId);
  });
  stage.addEventListener("pointermove", function(e){
    if (!drag) { return; }
    var r = stage.getBoundingClientRect(), sc = W / r.width;
    tx = drag.tx + (e.clientX - drag.x) * sc;
    ty = drag.ty + (e.clientY - drag.y) * sc;
    apply();
  });
  ["pointerup","pointercancel","pointerleave"].forEach(function(ev){
    stage.addEventListener(ev, function(){ drag = null; stage.classList.remove("dragging"); });
  });
  stage.addEventListener("keydown", function(e){
    if (e.key === "+" || e.key === "=") { zoomAt(z * 1.6, W/2, H/2); e.preventDefault(); }
    if (e.key === "-") { zoomAt(z / 1.6, W/2, H/2); e.preventDefault(); }
    if (e.key === "0") { z = 1; tx = 0; ty = 0; apply(); e.preventDefault(); }
  });
  stage.tabIndex = 0;
  stage.setAttribute("aria-label", "แผนที่รางวัล ซูมด้วยปุ่มบวกลบหรือล้อเมาส์ ลากเพื่อเลื่อน");
  window.__mapApply = apply;
  apply();
})();
/* END-MAPZOOM */

mapBoot();

/* ── หน้ารีวิวโบรกเกอร์รวม ────────────────────────
   รวมทุกรายในหมวดที่เลือก โดยใช้ผลของประเทศที่รายนั้นทำคะแนนได้สูงสุด      */
var RV_SORTS = [["score","\u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14"],
                ["stars","\u0e14\u0e32\u0e27\u0e21\u0e32\u0e01\u0e2a\u0e38\u0e14"],
                ["cost","\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14"],
                ["name","\u0e0a\u0e37\u0e48\u0e2d A\u2013Z"]];
var rvCat = "fx", rvQ = "", rvSort = "score";
function rvList(){
  var best = {};
  CM_ISOS.forEach(function(iso){
    rkRows(rvCat, iso, 2026).forEach(function(r){
      if (!best[r.id] || r.total > best[r.id].r.total) { best[r.id] = {r:r, iso:iso}; }
    });
  });
  var out = Object.keys(best).map(function(k){ return best[k]; });
  var q = rvQ.trim().toLowerCase();
  if (q) { out = out.filter(function(x){ return META[x.r.id].n.toLowerCase().indexOf(q) >= 0; }); }
  out.sort(function(a, b){
    if (rvSort === "name") { return META[a.r.id].n.localeCompare(META[b.r.id].n); }
    if (rvSort === "stars") { return b.r.stars - a.r.stars || b.r.total - a.r.total; }
    if (rvSort === "cost") { return a.r.metric - b.r.metric; }
    return b.r.total - a.r.total || META[a.r.id].n.localeCompare(META[b.r.id].n);
  });
  return out;
}
function rvRender(){
  var cats = document.getElementById("rv-cats");
  if (cats) {
    cats.innerHTML = CAT_ORDER.map(function(k){
      return '<button type="button" class="art-cat" data-rvcat="' + k + '" aria-pressed="' +
        (k === rvCat) + '">' + catShort(k) + '</button>';
    }).join("");
  }
  var sel = document.getElementById("rv-sort");
  if (sel && !sel.options.length) {
    sel.innerHTML = RV_SORTS.map(function(s){
      return '<option value="' + s[0] + '"' + (s[0] === rvSort ? " selected" : "") + '>' + s[1] + '</option>';
    }).join("");
  }
  var grid = document.getElementById("rv-grid"), note = document.getElementById("rv-note");
  if (!grid) { return; }
  var list = rvList(), c = CATS[rvCat];
  var total = Object.keys((function(){ var o = {}; CM_ISOS.forEach(function(i){
    rkRows(rvCat, i, 2026).forEach(function(r){ o[r.id] = 1; }); }); return o; })()).length;
  if (!list.length) {
    grid.innerHTML = '<div class="art-empty">\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e17\u0e35\u0e48\u0e15\u0e23\u0e07\u0e01\u0e31\u0e1a\u0e04\u0e33\u0e04\u0e49\u0e19\u0e19\u0e35\u0e49\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14\u0e17\u0e35\u0e48\u0e40\u0e25\u0e37\u0e2d\u0e01<br>' +
      '\u0e01\u0e32\u0e23\u0e44\u0e21\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e44\u0e21\u0e48\u0e14\u0e35 \u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e40\u0e23\u0e32\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e40\u0e02\u0e49\u0e32\u0e44\u0e1b\u0e15\u0e23\u0e27\u0e08</div>';
  } else {
    grid.innerHTML = list.map(function(x){
      var m = META[x.r.id];
      return '<article class="rv-card" data-stars="' + x.r.stars + '">' +
        '<div class="rv-top">' + logoSpan(m, 44, 15) +
          '<span><span class="rv-name">' + m.n + '</span>' +
          '<span class="rv-reg">' + m.reg + '</span></span></div>' +
        '<div class="rv-mid"><span><span class="rv-score">' + x.r.total.toFixed(1) + '</span>' +
          '<span class="rv-of">/10</span>' +
          '<span class="rv-cap">\u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e17\u0e35\u0e48 ' + CNAME[x.iso] + '</span></span>' +
          '<span class="rv-stars"><span class="rk-stars">' + starHTML(x.r.stars, 15) + '</span>' +
          '<span class="n">' + x.r.stars + ' \u0e14\u0e32\u0e27 RedStar</span></span></div>' +
        '<div class="rv-meta"><b>' + c.metric + '</b> ' + x.r.metric.toFixed(2) + ' ' + c.unit +
          ' \u00b7 \u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21 ' + (x.r.parts[0] + x.r.parts[1] + x.r.parts[2]).toFixed(2) +
          ' (' + c.costUnit + ')</div>' +
        '<div class="rv-cta"><a class="rk-cta" href="/broker/' + m.slug + '/review" data-review="' + m.slug + '">' +
          '\u0e2d\u0e48\u0e32\u0e19\u0e23\u0e35\u0e27\u0e34\u0e27\u0e09\u0e1a\u0e31\u0e1a\u0e40\u0e15\u0e47\u0e21 \u2192</a></div>' +
        '</article>';
    }).join("");
    paintLogos();
  }
  if (note) {
    note.innerHTML = '\u0e41\u0e2a\u0e14\u0e07 ' + list.length + ' \u0e08\u0e32\u0e01 ' + total + ' \u0e23\u0e32\u0e22\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14' + CATS[rvCat].n +
      (rvQ.trim() ? ' \u00b7 \u0e04\u0e33\u0e04\u0e49\u0e19 \u201c' + rvQ.trim() + '\u201d' : '') +
      ' \u00b7 \u0e04\u0e30\u0e41\u0e19\u0e19\u0e17\u0e35\u0e48\u0e41\u0e2a\u0e14\u0e07\u0e04\u0e37\u0e2d\u0e1c\u0e25\u0e1b\u0e35 2026 \u0e08\u0e32\u0e01\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e17\u0e35\u0e48\u0e23\u0e32\u0e22\u0e19\u0e31\u0e49\u0e19\u0e17\u0e33\u0e44\u0e14\u0e49\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14' +
      ' \u00b7 <b>\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e21\u0e21\u0e15\u0e34\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a</b>';
  }
}
document.addEventListener("click", function(ev){
  var c = ev.target.closest("[data-rvcat]");
  if (c) { rvCat = c.dataset.rvcat; rvRender(); }
});
(function(){
  var s = document.getElementById("rv-sort");
  if (s) { s.addEventListener("change", function(e){ rvSort = e.target.value; rvRender(); }); }
  var q = document.getElementById("rv-q");
  if (q) { q.addEventListener("input", function(e){ rvQ = e.target.value; rvRender(); }); }
  rvRender();
})();

/* ── ตัวสลับหน้า ────────────────────────────────────
   ต้องรันท้ายสุด เพราะส่วนแผนที่ต้องบูตตอนหน้าแรกยังมองเห็นอยู่       */
/* \u0e1b\u0e38\u0e48\u0e21\u0e20\u0e32\u0e29\u0e32 / Login / \u0e2a\u0e21\u0e31\u0e04\u0e23\u0e2a\u0e21\u0e32\u0e0a\u0e34\u0e01 \u2014 \u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e15\u0e48\u0e2d\u0e23\u0e30\u0e1a\u0e1a\u0e08\u0e23\u0e34\u0e07
   \u0e1b\u0e38\u0e48\u0e21\u0e20\u0e32\u0e29\u0e32\u0e2a\u0e25\u0e31\u0e1a\u0e44\u0e14\u0e49\u0e41\u0e04\u0e48\u0e2a\u0e16\u0e32\u0e19\u0e30\u0e1b\u0e38\u0e48\u0e21 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e40\u0e19\u0e37\u0e49\u0e2d\u0e2b\u0e32 */
document.addEventListener("click", function(ev){
  var l = ev.target.closest("[data-lang]");
  if (l) {
    document.querySelectorAll("[data-lang]").forEach(function(b){
      b.setAttribute("aria-pressed", String(b === l));
    });
    return;
  }
  var a = ev.target.closest("[data-auth]");
  if (a) { ev.preventDefault(); }
});
/* \u0e2b\u0e19\u0e49\u0e32\u0e40\u0e02\u0e49\u0e32\u0e2a\u0e39\u0e48\u0e23\u0e30\u0e1a\u0e1a / \u0e2a\u0e21\u0e31\u0e04\u0e23\u0e2a\u0e21\u0e32\u0e0a\u0e34\u0e01 \u2014 \u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19
   \u0e1f\u0e2d\u0e23\u0e4c\u0e21\u0e44\u0e21\u0e48\u0e2a\u0e48\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e1b\u0e44\u0e2b\u0e19 \u0e01\u0e14\u0e2a\u0e48\u0e07\u0e41\u0e25\u0e49\u0e27\u0e02\u0e36\u0e49\u0e19\u0e04\u0e33\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27 */
(function(){
  var sel = document.getElementById("su-country");
  if (sel && typeof CNAME !== "undefined") {
    var list = ["TH"].concat(Object.keys(CNAME));
    sel.innerHTML = '<option value="">\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28</option>' +
      '<option value="TH">Thailand</option>' +
      Object.keys(CNAME).map(function(k){
        return '<option value="' + k + '">' + CNAME[k] + '</option>';
      }).join("") + '<option value="other">\u0e2d\u0e37\u0e48\u0e19 \u0e46</option>';
  }
})();
document.addEventListener("click", function(ev){
  var eye = ev.target.closest("[data-pw]");
  if (eye) {
    var inp = document.getElementById(eye.dataset.pw);
    if (inp) { inp.type = inp.type === "password" ? "text" : "password"; }
    eye.setAttribute("aria-pressed", String(inp && inp.type === "text"));
  }
});
document.addEventListener("submit", function(ev){
  var f = ev.target.closest("[data-authform]");
  if (!f) { return; }
  ev.preventDefault();
  if (!f.querySelector(".auth-done")) {
    var p = document.createElement("p");
    p.className = "auth-done";
    p.style.cssText = "margin:14px 0 0;padding:11px 14px;background:#F5F7FA;border:1px solid #EAECF0;" +
      "border-radius:10px;font-size:12.5px;line-height:1.6;color:#475467;";
    p.textContent = "\u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e48\u0e2d\u0e23\u0e30\u0e1a\u0e1a\u0e2a\u0e21\u0e32\u0e0a\u0e34\u0e01 \u0e08\u0e36\u0e07\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e2a\u0e48\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e43\u0e14 \u2014 \u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19";
    f.appendChild(p);
  }
});
/* \u2500\u2500 \u0e2b\u0e19\u0e49\u0e32 Broker Alerts \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
   \u0e0a\u0e37\u0e48\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e17\u0e38\u0e01\u0e0a\u0e37\u0e48\u0e2d\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e15\u0e31\u0e49\u0e07\u0e02\u0e36\u0e49\u0e19\u0e40\u0e2d\u0e07 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e17\u0e35\u0e48\u0e21\u0e35\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e23\u0e34\u0e07 \u0e15\u0e32\u0e21\u0e01\u0e0e\u0e02\u0e49\u0e2d 6a */
var AL_STATUS = [["all","\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14"],
                 ["wait","\u0e23\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07"],
                 ["replied","\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e41\u0e25\u0e49\u0e27"],
                 ["closed","\u0e1b\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e41\u0e25\u0e49\u0e27"]];
var ALERTS_D = [
  {s:"hi", st:"wait", b:"Apex Global FX", d:"14 \u0e21\u0e34.\u0e22. 2026",
   t:"\u0e43\u0e2b\u0e49\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23\u0e43\u0e19\u0e40\u0e02\u0e15\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15",
   x:"\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e04\u0e49\u0e19\u0e40\u0e25\u0e02\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e39\u0e49\u0e43\u0e2b\u0e49\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23\u0e41\u0e2a\u0e14\u0e07\u0e44\u0e27\u0e49\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e27\u0e47\u0e1a \u0e41\u0e25\u0e49\u0e27<b>\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e43\u0e19\u0e10\u0e32\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1c\u0e39\u0e49\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15\u0e02\u0e2d\u0e07\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e17\u0e35\u0e48\u0e2d\u0e49\u0e32\u0e07\u0e16\u0e36\u0e07</b> \u0e41\u0e25\u0e30\u0e40\u0e25\u0e02\u0e17\u0e35\u0e48\u0e2d\u0e49\u0e32\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e2d\u0e07\u0e19\u0e34\u0e15\u0e34\u0e1a\u0e38\u0e04\u0e04\u0e25\u0e2d\u0e37\u0e48\u0e19",
   r:null,
   n:"\u0e2a\u0e48\u0e07\u0e2b\u0e19\u0e31\u0e07\u0e2a\u0e37\u0e2d\u0e02\u0e2d\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e44\u0e1b\u0e41\u0e25\u0e49\u0e27 2 \u0e04\u0e23\u0e31\u0e49\u0e07 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e15\u0e2d\u0e1a\u0e01\u0e25\u0e31\u0e1a"},
  {s:"hi", st:"replied", b:"Sterling Wave Capital", d:"6 \u0e21\u0e34.\u0e22. 2026",
   t:"\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e16\u0e2d\u0e19\u0e40\u0e07\u0e34\u0e19\u0e16\u0e39\u0e01\u0e1b\u0e0f\u0e34\u0e40\u0e2a\u0e18\u0e0b\u0e49\u0e33\u0e2b\u0e25\u0e32\u0e22\u0e23\u0e32\u0e22\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27",
   x:"\u0e21\u0e35\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e41\u0e08\u0e49\u0e07\u0e40\u0e02\u0e49\u0e32\u0e21\u0e32 <b>11 \u0e23\u0e32\u0e22\u0e20\u0e32\u0e22\u0e43\u0e19 9 \u0e27\u0e31\u0e19</b> \u0e27\u0e48\u0e32\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e16\u0e2d\u0e19\u0e16\u0e39\u0e01\u0e1b\u0e0f\u0e34\u0e40\u0e2a\u0e18\u0e42\u0e14\u0e22\u0e2d\u0e49\u0e32\u0e07\u0e40\u0e2b\u0e15\u0e38\u0e40\u0e2d\u0e01\u0e2a\u0e32\u0e23\u0e44\u0e21\u0e48\u0e04\u0e23\u0e1a \u0e17\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48\u0e40\u0e04\u0e22\u0e1c\u0e48\u0e32\u0e19\u0e01\u0e32\u0e23\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e15\u0e31\u0e27\u0e15\u0e19\u0e21\u0e32\u0e01\u0e48\u0e2d\u0e19\u0e41\u0e25\u0e49\u0e27",
   r:{d:"9 \u0e21\u0e34.\u0e22. 2026",
      p:"\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e27\u0e48\u0e32\u0e40\u0e01\u0e34\u0e14\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e1c\u0e39\u0e49\u0e43\u0e2b\u0e49\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23\u0e0a\u0e33\u0e23\u0e30\u0e40\u0e07\u0e34\u0e19 \u0e17\u0e33\u0e43\u0e2b\u0e49\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e0a\u0e38\u0e14\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e04\u0e49\u0e32\u0e07\u0e23\u0e30\u0e1a\u0e1a \u0e44\u0e14\u0e49\u0e04\u0e37\u0e19\u0e40\u0e07\u0e34\u0e19\u0e04\u0e23\u0e1a\u0e17\u0e38\u0e01\u0e23\u0e32\u0e22\u0e20\u0e32\u0e22\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 8 \u0e21\u0e34.\u0e22. \u0e41\u0e25\u0e30\u0e22\u0e01\u0e40\u0e25\u0e34\u0e01\u0e01\u0e32\u0e23\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e15\u0e31\u0e27\u0e15\u0e19\u0e0b\u0e49\u0e33\u0e41\u0e25\u0e49\u0e27"},
   n:"\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e02\u0e2d\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e01\u0e32\u0e23\u0e04\u0e37\u0e19\u0e40\u0e07\u0e34\u0e19\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e15\u0e34\u0e21 \u0e41\u0e25\u0e30\u0e08\u0e30\u0e15\u0e34\u0e14\u0e15\u0e32\u0e21\u0e2d\u0e35\u0e01 90 \u0e27\u0e31\u0e19"},
  {s:"md", st:"replied", b:"Orion Trade Group", d:"2 \u0e21\u0e34.\u0e22. 2026",
   t:"\u0e43\u0e0a\u0e49\u0e0a\u0e37\u0e48\u0e2d\u0e41\u0e25\u0e30\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e27\u0e47\u0e1a\u0e04\u0e25\u0e49\u0e32\u0e22\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e21\u0e35\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15",
   x:"\u0e42\u0e14\u0e40\u0e21\u0e19\u0e41\u0e25\u0e30\u0e2b\u0e19\u0e49\u0e32\u0e41\u0e23\u0e01\u0e04\u0e25\u0e49\u0e32\u0e22\u0e01\u0e31\u0e1a\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e21\u0e35\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15\u0e23\u0e32\u0e22\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e08\u0e19\u0e2d\u0e32\u0e08\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e1c\u0e34\u0e14 \u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e2d\u0e17\u0e49\u0e32\u0e22\u0e42\u0e14\u0e40\u0e21\u0e19\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19",
   r:{d:"5 \u0e21\u0e34.\u0e22. 2026",
      p:"\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e41\u0e08\u0e49\u0e07\u0e27\u0e48\u0e32\u0e08\u0e14\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e0a\u0e37\u0e48\u0e2d\u0e19\u0e35\u0e49\u0e21\u0e32\u0e01\u0e48\u0e2d\u0e19 \u0e41\u0e25\u0e30\u0e22\u0e34\u0e19\u0e14\u0e35\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e1a\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e41\u0e23\u0e01\u0e27\u0e48\u0e32\u0e44\u0e21\u0e48\u0e21\u0e35\u0e04\u0e27\u0e32\u0e21\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e02\u0e49\u0e2d\u0e07\u0e01\u0e31\u0e1a\u0e42\u0e1a\u0e23\u0e01\u0e2d\u0e35\u0e01\u0e23\u0e32\u0e22"},
   n:"\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e27\u0e48\u0e32\u0e21\u0e35\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e08\u0e23\u0e34\u0e07 \u0e41\u0e15\u0e48\u0e04\u0e07\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e44\u0e27\u0e49\u0e43\u0e2b\u0e49\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e15\u0e23\u0e27\u0e08\u0e42\u0e14\u0e40\u0e21\u0e19\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e2a\u0e21\u0e2d"},
  {s:"hi", st:"closed", b:"Nova Prime Markets", d:"9 \u0e21\u0e34.\u0e22. 2026",
   t:"\u0e16\u0e39\u0e01\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e40\u0e1e\u0e34\u0e01\u0e16\u0e2d\u0e19\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15",
   x:"\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e40\u0e1e\u0e34\u0e01\u0e16\u0e2d\u0e19\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15\u0e14\u0e49\u0e27\u0e22\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e34\u0e14\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e01\u0e32\u0e23\u0e14\u0e33\u0e23\u0e07\u0e40\u0e07\u0e34\u0e19\u0e01\u0e2d\u0e07\u0e17\u0e38\u0e19\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32 <b>\u0e40\u0e23\u0e32\u0e40\u0e1e\u0e34\u0e01\u0e16\u0e2d\u0e19\u0e14\u0e32\u0e27\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e41\u0e25\u0e49\u0e27 \u0e41\u0e15\u0e48\u0e22\u0e31\u0e07\u0e04\u0e07\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e44\u0e27\u0e49\u0e43\u0e19\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19</b>",
   r:null,
   n:"\u0e1b\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e40\u0e21\u0e37\u0e48\u0e2d 12 \u0e21\u0e34.\u0e22. 2026 \u2014 \u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e27\u0e49\u0e43\u0e19\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e16\u0e32\u0e27\u0e23"},
  {s:"md", st:"wait", b:"Vertex Bridge Markets", d:"21 \u0e1e.\u0e04. 2026",
   t:"\u0e22\u0e49\u0e32\u0e22\u0e40\u0e02\u0e15\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e01\u0e33\u0e01\u0e31\u0e1a 3 \u0e04\u0e23\u0e31\u0e49\u0e07\u0e43\u0e19 12 \u0e40\u0e14\u0e37\u0e2d\u0e19",
   x:"\u0e01\u0e32\u0e23\u0e22\u0e49\u0e32\u0e22\u0e40\u0e02\u0e15\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e44\u0e21\u0e48\u0e1c\u0e34\u0e14\u0e01\u0e0e\u0e2b\u0e21\u0e32\u0e22 \u0e41\u0e15\u0e48\u0e01\u0e32\u0e23\u0e22\u0e49\u0e32\u0e22\u0e16\u0e35\u0e48\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32<b>\u0e40\u0e07\u0e34\u0e19\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e21\u0e37\u0e2d\u0e1c\u0e39\u0e49\u0e14\u0e39\u0e41\u0e25\u0e2b\u0e25\u0e32\u0e22\u0e04\u0e23\u0e31\u0e49\u0e07\u0e43\u0e19\u0e40\u0e27\u0e25\u0e32\u0e2a\u0e31\u0e49\u0e19</b> \u0e0b\u0e36\u0e48\u0e07\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e15\u0e48\u0e2d\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e02\u0e2d\u0e07\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e01\u0e34\u0e14\u0e02\u0e49\u0e2d\u0e1e\u0e34\u0e1e\u0e32\u0e17",
   r:null,
   n:"\u0e2a\u0e48\u0e07\u0e2b\u0e19\u0e31\u0e07\u0e2a\u0e37\u0e2d\u0e02\u0e2d\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e40\u0e21\u0e37\u0e48\u0e2d 23 \u0e1e.\u0e04. 2026 \u0e04\u0e23\u0e1a\u0e01\u0e33\u0e2b\u0e19\u0e14 30 \u0e27\u0e31\u0e19\u0e41\u0e25\u0e49\u0e27"}
];
var EDU = [
  ["\u0e44\u0e21\u0e48\u0e21\u0e35\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15 \u0e2b\u0e23\u0e37\u0e2d\u0e2d\u0e49\u0e32\u0e07\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15\u0e17\u0e35\u0e48\u0e15\u0e23\u0e27\u0e08\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49",
   "\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15\u0e08\u0e23\u0e34\u0e07\u0e15\u0e49\u0e2d\u0e07\u0e04\u0e49\u0e19\u0e40\u0e08\u0e2d\u0e43\u0e19\u0e10\u0e32\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e02\u0e2d\u0e07\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e40\u0e2d\u0e07 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e14\u0e39\u0e08\u0e32\u0e01\u0e42\u0e25\u0e42\u0e01\u0e49\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e25\u0e02\u0e17\u0e35\u0e48\u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e44\u0e27\u0e49\u0e17\u0e49\u0e32\u0e22\u0e40\u0e27\u0e47\u0e1a",
   "Apex Global FX \u0e2d\u0e49\u0e32\u0e07\u0e40\u0e25\u0e02\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e17\u0e35\u0e48\u0e04\u0e49\u0e19\u0e41\u0e25\u0e49\u0e27\u0e44\u0e21\u0e48\u0e1e\u0e1a \u0e41\u0e25\u0e30\u0e40\u0e25\u0e02\u0e17\u0e35\u0e48\u0e2d\u0e49\u0e32\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e2d\u0e07\u0e19\u0e34\u0e15\u0e34\u0e1a\u0e38\u0e04\u0e04\u0e25\u0e2d\u0e37\u0e48\u0e19"],
  ["\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19",
   "\u0e44\u0e21\u0e48\u0e21\u0e35\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e17\u0e35\u0e48\u0e44\u0e2b\u0e19\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15\u0e43\u0e2b\u0e49\u0e42\u0e06\u0e29\u0e13\u0e32\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e21\u0e35\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e2a\u0e21\u0e2d",
   "Zen Peak Securities \u0e42\u0e06\u0e29\u0e13\u0e32\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e02\u0e31\u0e49\u0e19\u0e15\u0e48\u0e33 3% \u0e15\u0e48\u0e2d\u0e40\u0e14\u0e37\u0e2d\u0e19 \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e04\u0e33\u0e27\u0e48\u0e32 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07"],
  ["\u0e16\u0e2d\u0e19\u0e40\u0e07\u0e34\u0e19\u0e22\u0e32\u0e01 \u0e21\u0e35\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e07\u0e2d\u0e01\u0e43\u0e2b\u0e21\u0e48\u0e15\u0e2d\u0e19\u0e08\u0e30\u0e16\u0e2d\u0e19",
   "\u0e1d\u0e32\u0e01\u0e07\u0e48\u0e32\u0e22\u0e41\u0e15\u0e48\u0e16\u0e2d\u0e19\u0e22\u0e32\u0e01 \u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e23\u0e35\u0e22\u0e01\u0e40\u0e01\u0e47\u0e1a\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e40\u0e04\u0e22\u0e41\u0e08\u0e49\u0e07\u0e44\u0e27\u0e49\u0e01\u0e48\u0e2d\u0e19 \u0e40\u0e0a\u0e48\u0e19 \u0e04\u0e48\u0e32\u0e20\u0e32\u0e29\u0e35 \u0e04\u0e48\u0e32\u0e1b\u0e25\u0e14\u0e25\u0e47\u0e2d\u0e01\u0e1a\u0e31\u0e0d\u0e0a\u0e35",
   "Sterling Wave Capital \u0e21\u0e35\u0e04\u0e33\u0e23\u0e49\u0e2d\u0e07 11 \u0e23\u0e32\u0e22\u0e43\u0e19 9 \u0e27\u0e31\u0e19 \u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e16\u0e2d\u0e19\u0e16\u0e39\u0e01\u0e1b\u0e0f\u0e34\u0e40\u0e2a\u0e18"],
  ["\u0e40\u0e27\u0e47\u0e1a\u0e42\u0e04\u0e25\u0e19 \u0e43\u0e0a\u0e49\u0e0a\u0e37\u0e48\u0e2d\u0e04\u0e25\u0e49\u0e32\u0e22\u0e23\u0e32\u0e22\u0e17\u0e35\u0e48\u0e21\u0e35\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15",
   "\u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e41\u0e04\u0e48\u0e42\u0e14\u0e40\u0e21\u0e19\u0e2b\u0e23\u0e37\u0e2d\u0e04\u0e33\u0e15\u0e48\u0e2d\u0e17\u0e49\u0e32\u0e22 \u0e43\u0e2b\u0e49\u0e15\u0e23\u0e27\u0e08\u0e42\u0e14\u0e40\u0e21\u0e19\u0e01\u0e31\u0e1a\u0e40\u0e25\u0e02\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e08\u0e32\u0e01\u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07",
   "Orion Trade Group \u0e43\u0e0a\u0e49\u0e0a\u0e37\u0e48\u0e2d\u0e41\u0e25\u0e30\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e27\u0e47\u0e1a\u0e04\u0e25\u0e49\u0e32\u0e22\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e21\u0e35\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15 \u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e41\u0e04\u0e48\u0e2a\u0e48\u0e27\u0e19\u0e17\u0e49\u0e32\u0e22\u0e42\u0e14\u0e40\u0e21\u0e19"],
  ["\u0e01\u0e14\u0e14\u0e31\u0e19\u0e43\u0e2b\u0e49\u0e1d\u0e32\u0e01\u0e40\u0e1e\u0e34\u0e48\u0e21 \u0e21\u0e35\u0e04\u0e19\u0e42\u0e17\u0e23\u0e15\u0e32\u0e21\u0e15\u0e25\u0e2d\u0e14",
   "\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e14\u0e35\u0e44\u0e21\u0e48\u0e40\u0e23\u0e48\u0e07\u0e43\u0e2b\u0e49\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e43\u0e08\u0e14\u0e49\u0e27\u0e22\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e40\u0e27\u0e25\u0e32 \u0e01\u0e32\u0e23\u0e42\u0e17\u0e23\u0e15\u0e32\u0e21\u0e43\u0e2b\u0e49\u0e1d\u0e32\u0e01\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e04\u0e37\u0e2d\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e2d\u0e31\u0e19\u0e15\u0e23\u0e32\u0e22",
   "\u0e21\u0e35\u0e04\u0e33\u0e23\u0e49\u0e2d\u0e07\u0e27\u0e48\u0e32\u0e16\u0e39\u0e01\u0e42\u0e17\u0e23\u0e0b\u0e49\u0e33\u0e43\u0e2b\u0e49\u0e40\u0e15\u0e34\u0e21\u0e40\u0e07\u0e34\u0e19\u0e20\u0e32\u0e22\u0e43\u0e19 24 \u0e0a\u0e31\u0e48\u0e27\u0e42\u0e21\u0e07 \u0e21\u0e34\u0e09\u0e30\u0e19\u0e31\u0e49\u0e19\u0e08\u0e30\u0e40\u0e2a\u0e35\u0e22\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e4c\u0e42\u0e1b\u0e23\u0e42\u0e21\u0e0a\u0e31\u0e48\u0e19"],
  ["\u0e44\u0e21\u0e48\u0e21\u0e35\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e23\u0e34\u0e07 \u0e2b\u0e23\u0e37\u0e2d\u0e22\u0e49\u0e32\u0e22\u0e40\u0e02\u0e15\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e1a\u0e48\u0e2d\u0e22",
   "\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e14\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e39\u0e49\u0e44\u0e1b\u0e23\u0e29\u0e13\u0e35\u0e22\u0e4c \u0e2b\u0e23\u0e37\u0e2d\u0e22\u0e49\u0e32\u0e22\u0e40\u0e02\u0e15\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e1a\u0e48\u0e2d\u0e22 \u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e15\u0e32\u0e21\u0e40\u0e07\u0e34\u0e19\u0e04\u0e37\u0e19\u0e22\u0e32\u0e01\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e01\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07",
   "Vertex Bridge Markets \u0e22\u0e49\u0e32\u0e22\u0e40\u0e02\u0e15\u0e01\u0e33\u0e01\u0e31\u0e1a 3 \u0e04\u0e23\u0e31\u0e49\u0e07\u0e43\u0e19 12 \u0e40\u0e14\u0e37\u0e2d\u0e19 \u00b7 Halcyon FX Ltd \u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e14\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e15\u0e32\u0e21\u0e17\u0e35\u0e48\u0e41\u0e08\u0e49\u0e07"]
];
var alSt = "all";
function alRender(){
  var cats = document.getElementById("al-cats");
  if (cats) {
    cats.innerHTML = AL_STATUS.map(function(s){
      var n = s[0] === "all" ? ALERTS_D.length
            : ALERTS_D.filter(function(a){ return a.st === s[0]; }).length;
      return '<button type="button" class="art-cat" data-alst="' + s[0] + '" aria-pressed="' +
        (s[0] === alSt) + '"' + (n ? "" : " disabled") + '>' + s[1] + ' (' + n + ')</button>';
    }).join("");
  }
  var host = document.getElementById("al-list");
  if (!host) { return; }
  var list = ALERTS_D.filter(function(a){ return alSt === "all" || a.st === alSt; });
  var pill = {wait:["wait","\u0e23\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07"],
              replied:["replied","\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e41\u0e25\u0e49\u0e27"],
              closed:["closed","\u0e1b\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e41\u0e25\u0e49\u0e27"]};
  if (!list.length) {
    host.innerHTML = '<div class="al-empty">\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e43\u0e19\u0e2a\u0e16\u0e32\u0e19\u0e30\u0e19\u0e35\u0e49</div>';
  } else {
    host.innerHTML = list.map(function(a){
      var p = pill[a.st];
      return '<article class="al-card">' +
        '<div class="al-head"><span class="al-sev ' + a.s + '">' +
          '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="' +
          (a.s === "hi" ? "#D92D20" : "#B54708") + '" stroke-width="2" stroke-linecap="round" ' +
          'stroke-linejoin="round" aria-hidden="true">' +
          '<path d="M10.3 3.6L1.9 18a2 2 0 001.7 3h16.8a2 2 0 001.7-3L13.7 3.6a2 2 0 00-3.4 0z"></path>' +
          '<path d="M12 9v4M12 17v.1"></path></svg></span>' +
          '<span class="al-ttl"><h3>' + a.t + '</h3>' +
          '<span class="al-meta"><b>' + a.b + '</b><span>\u00b7</span><span>\u0e41\u0e08\u0e49\u0e07\u0e40\u0e15\u0e37\u0e2d\u0e19 ' + a.d + '</span></span></span>' +
          '<span class="al-pill ' + p[0] + '">' + p[1] + '</span></div>' +
        '<div class="al-body">' + a.x + '</div>' +
        (a.r ? '<div class="al-reply"><div class="who">' +
          '<span class="tag">\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e08\u0e32\u0e01\u0e1c\u0e39\u0e49\u0e43\u0e2b\u0e49\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23</span>' +
          '<span>' + a.b + ' \u00b7 ' + a.r.d + '</span></div><p>' + a.r.p + '</p></div>' : "") +
        '<div class="al-note"><b>\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e02\u0e2d\u0e07\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08:</b> ' + a.n +
        ' \u00b7 \u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e02\u0e2d\u0e07\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c<b>\u0e44\u0e21\u0e48\u0e21\u0e35\u0e1c\u0e25\u0e15\u0e48\u0e2d\u0e08\u0e33\u0e19\u0e27\u0e19\u0e14\u0e32\u0e27\u0e2b\u0e23\u0e37\u0e2d\u0e04\u0e30\u0e41\u0e19\u0e19</b></div>' +
        '</article>';
    }).join("");
  }
  var note = document.getElementById("al-note");
  if (note) {
    note.innerHTML = '\u0e41\u0e2a\u0e14\u0e07 ' + list.length + ' \u0e08\u0e32\u0e01 ' + ALERTS_D.length + ' \u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07' +
      ' \u00b7 <b>\u0e0a\u0e37\u0e48\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e17\u0e38\u0e01\u0e0a\u0e37\u0e48\u0e2d\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e15\u0e31\u0e49\u0e07\u0e02\u0e36\u0e49\u0e19\u0e40\u0e2d\u0e07\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e17\u0e35\u0e48\u0e21\u0e35\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e23\u0e34\u0e07</b>';
  }
  var edu = document.getElementById("al-edu");
  if (edu && !edu.children.length) {
    edu.innerHTML = EDU.map(function(e, i){
      return '<article class="edu-card"><span class="edu-n">' + (i + 1) + '</span>' +
        '<h4>' + e[0] + '</h4><p>' + e[1] + '</p>' +
        '<div class="edu-eg"><b>\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e17\u0e35\u0e48\u0e15\u0e23\u0e27\u0e08\u0e40\u0e08\u0e2d</b>' + e[2] + '</div></article>';
    }).join("");
    var en = document.getElementById("al-edunote");
    if (en) {
      en.innerHTML = '\u0e2b\u0e01\u0e02\u0e49\u0e2d\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e17\u0e35\u0e48\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e40\u0e08\u0e2d\u0e1a\u0e48\u0e2d\u0e22\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14 ' +
        '\u0e1e\u0e1a\u0e02\u0e49\u0e2d\u0e43\u0e14\u0e02\u0e49\u0e2d\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e40\u0e16\u0e37\u0e48\u0e2d\u0e19\u0e17\u0e31\u0e19\u0e17\u0e35 \u0e41\u0e15\u0e48\u0e04\u0e27\u0e23\u0e15\u0e23\u0e27\u0e08\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e01\u0e48\u0e2d\u0e19\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e43\u0e08 ' +
        '\u00b7 <b>\u0e0a\u0e37\u0e48\u0e2d\u0e43\u0e19\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e15\u0e31\u0e49\u0e07\u0e02\u0e36\u0e49\u0e19\u0e40\u0e2d\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14</b>';
    }
  }
}
document.addEventListener("click", function(ev){
  var b = ev.target.closest("[data-alst]");
  if (b && !b.disabled) { alSt = b.dataset.alst; alRender(); }
});
alRender();

/* \u2500\u2500 \u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07 EA \u2014 \u0e01\u0e14 "\u0e23\u0e31\u0e1a\u0e1f\u0e23\u0e35" \u0e41\u0e25\u0e49\u0e27\u0e40\u0e1b\u0e34\u0e14 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
   \u0e01\u0e23\u0e32\u0e1f\u0e41\u0e17\u0e48\u0e07\u0e40\u0e17\u0e35\u0e22\u0e19\u0e27\u0e32\u0e14\u0e15\u0e32\u0e22\u0e15\u0e31\u0e27 \u0e04\u0e48\u0e32\u0e04\u0e07\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e34\u0e14 \u0e44\u0e21\u0e48\u0e2a\u0e38\u0e48\u0e21\u0e43\u0e2b\u0e21\u0e48\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07 */
var EA_PREV = [
  {sym:"EURUSD, M5", hd:"REDSTAR ANALYTICS",
   rows:[["Spread", "0.9 pip", ""], ["Commission", "$3.50", ""], ["Swap", "-$0.42", "r"],
         ["Cost / lot", "$12.40", ""], ["\u0e23\u0e2d\u0e1a 30 \u0e27\u0e31\u0e19", "$248", ""]],
   cap:"\u0e41\u0e1c\u0e07\u0e08\u0e30\u0e25\u0e2d\u0e22\u0e2d\u0e22\u0e39\u0e48\u0e21\u0e38\u0e21\u0e01\u0e23\u0e32\u0e1f \u0e2d\u0e31\u0e1b\u0e40\u0e14\u0e15\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48\u0e21\u0e35\u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c\u0e1b\u0e34\u0e14",
   get:["\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e23\u0e32\u0e22\u0e40\u0e14\u0e37\u0e2d\u0e19\u0e2a\u0e48\u0e07\u0e40\u0e02\u0e49\u0e32\u0e2d\u0e35\u0e40\u0e21\u0e25",
        "\u0e14\u0e39\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e44\u0e14\u0e49\u0e17\u0e31\u0e49\u0e07\u0e15\u0e32\u0e21\u0e2a\u0e31\u0e0d\u0e25\u0e31\u0e01\u0e29\u0e13\u0e4c\u0e41\u0e25\u0e30\u0e15\u0e32\u0e21\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32",
        "\u0e2a\u0e48\u0e07\u0e2d\u0e2d\u0e01\u0e40\u0e1b\u0e47\u0e19 CSV \u0e44\u0e14\u0e49"]},
  {sym:"EURUSD, H1", hd:"BROKER COMPARE",
   rows:[["\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49", "$2,976", "r"], ["\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14", "$2,208", ""],
         ["Northgate #1", "$1,704", "g"], ["\u0e1b\u0e23\u0e30\u0e2b\u0e22\u0e31\u0e14/\u0e1b\u0e35", "$1,272", "g"]],
   cap:"\u0e04\u0e33\u0e19\u0e27\u0e13\u0e08\u0e32\u0e01\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e08\u0e23\u0e34\u0e07\u0e02\u0e2d\u0e07\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e04\u0e38\u0e13 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e04\u0e48\u0e32\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e01\u0e25\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e15\u0e25\u0e32\u0e14",
   get:["\u0e15\u0e32\u0e23\u0e32\u0e07\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e15\u0e48\u0e2d\u0e1b\u0e35\u0e01\u0e31\u0e1a\u0e42\u0e1a\u0e23\u0e01\u0e2d\u0e37\u0e48\u0e19",
        "\u0e41\u0e22\u0e01\u0e43\u0e2b\u0e49\u0e40\u0e2b\u0e47\u0e19\u0e27\u0e48\u0e32\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07\u0e21\u0e32\u0e08\u0e32\u0e01\u0e2a\u0e40\u0e1b\u0e23\u0e14\u0e2b\u0e23\u0e37\u0e2d\u0e04\u0e2d\u0e21",
        "\u0e01\u0e14\u0e14\u0e39\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e1a\u0e19\u0e40\u0e27\u0e47\u0e1a\u0e15\u0e48\u0e2d\u0e44\u0e14\u0e49"]},
  {sym:"XAUUSD, M1", hd:"HEALTH MONITOR",
   rows:[["Execution", "38 ms", "g"], ["Requotes", "12", "r"], ["Slippage +", "61%", "g"],
         ["Freeze", "0", "g"], ["\u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21", "8.6/10", ""]],
   cap:"\u0e27\u0e31\u0e14\u0e17\u0e38\u0e01\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07 \u0e41\u0e25\u0e49\u0e27\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e17\u0e31\u0e19\u0e17\u0e35\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e04\u0e48\u0e32\u0e40\u0e23\u0e34\u0e48\u0e21\u0e2b\u0e25\u0e38\u0e14\u0e08\u0e32\u0e01\u0e04\u0e48\u0e32\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e02\u0e2d\u0e07\u0e15\u0e31\u0e27\u0e40\u0e2d\u0e07",
   get:["\u0e01\u0e23\u0e32\u0e1f\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e47\u0e27\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e23\u0e32\u0e22\u0e0a\u0e31\u0e48\u0e27\u0e42\u0e21\u0e07",
        "\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e1a\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e08\u0e2d\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e23\u0e35\u0e42\u0e04\u0e27\u0e15\u0e40\u0e01\u0e34\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c",
        "\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e0a\u0e48\u0e27\u0e07\u0e02\u0e48\u0e32\u0e27\u0e01\u0e31\u0e1a\u0e0a\u0e48\u0e27\u0e07\u0e1b\u0e01\u0e15\u0e34"]},
  {sym:"GBPUSD, M5", hd:"COMMUNITY ALERT",
   rows:[["\u0e2a\u0e16\u0e32\u0e19\u0e30", "ALERT", "r"], ["\u0e2a\u0e40\u0e1b\u0e23\u0e14", "+312%", "r"],
         ["\u0e1c\u0e39\u0e49\u0e40\u0e08\u0e2d", "248 \u0e04\u0e19", ""], ["\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32", "30 \u0e19\u0e32\u0e17\u0e35", ""]],
   cap:"\u0e41\u0e08\u0e49\u0e07\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e2b\u0e25\u0e32\u0e22\u0e04\u0e19\u0e40\u0e08\u0e2d\u0e40\u0e2b\u0e15\u0e38\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e43\u0e19\u0e40\u0e27\u0e25\u0e32\u0e43\u0e01\u0e25\u0e49\u0e40\u0e04\u0e35\u0e22\u0e07\u0e01\u0e31\u0e19",
   get:["\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e1a\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e08\u0e2d\u0e41\u0e25\u0e30\u0e17\u0e32\u0e07\u0e2d\u0e35\u0e40\u0e21\u0e25",
        "\u0e1a\u0e2d\u0e01\u0e08\u0e33\u0e19\u0e27\u0e19\u0e04\u0e19\u0e17\u0e35\u0e48\u0e40\u0e08\u0e2d\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19",
        "\u0e14\u0e39\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e44\u0e14\u0e49\u0e27\u0e48\u0e32\u0e40\u0e01\u0e34\u0e14\u0e2d\u0e30\u0e44\u0e23\u0e02\u0e36\u0e49\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e44\u0e2b\u0e19"]},
  {sym:"\u0e2a\u0e21\u0e38\u0e14\u0e01\u0e32\u0e23\u0e16\u0e2d\u0e19", hd:"WITHDRAWAL JOURNAL",
   rows:[["\u0e01\u0e14\u0e16\u0e2d\u0e19", "09:12", ""], ["\u0e2d\u0e19\u0e38\u0e21\u0e31\u0e15\u0e34", "2\u0e0a\u0e21 14\u0e19", ""],
         ["\u0e40\u0e07\u0e34\u0e19\u0e40\u0e02\u0e49\u0e32", "6\u0e0a\u0e21 02\u0e19", ""], ["\u0e23\u0e27\u0e21", "8\u0e0a\u0e21 16\u0e19", "g"]],
   cap:"\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e01\u0e14\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e2a\u0e2d\u0e07\u0e08\u0e38\u0e14 \u0e23\u0e30\u0e1a\u0e1a\u0e04\u0e33\u0e19\u0e27\u0e13\u0e40\u0e27\u0e25\u0e32\u0e08\u0e23\u0e34\u0e07\u0e43\u0e2b\u0e49\u0e40\u0e2d\u0e07",
   get:["\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e01\u0e32\u0e23\u0e16\u0e2d\u0e19\u0e40\u0e07\u0e34\u0e19\u0e02\u0e2d\u0e07\u0e15\u0e31\u0e27\u0e40\u0e2d\u0e07",
        "\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e47\u0e27\u0e01\u0e31\u0e1a\u0e04\u0e48\u0e32\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e02\u0e2d\u0e07\u0e42\u0e1a\u0e23\u0e01\u0e19\u0e31\u0e49\u0e19",
        "\u0e41\u0e22\u0e01\u0e40\u0e27\u0e25\u0e32\u0e2d\u0e19\u0e38\u0e21\u0e31\u0e15\u0e34\u0e01\u0e31\u0e1a\u0e40\u0e27\u0e25\u0e32\u0e42\u0e2d\u0e19"]},
  {sym:"\u0e2a\u0e23\u0e38\u0e1b\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19", hd:"EVIDENCE COLLECTOR",
   rows:[["\u0e2a\u0e48\u0e07\u0e41\u0e25\u0e49\u0e27", "4,812", ""], ["\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19", "4,796", "g"],
         ["\u0e15\u0e01\u0e2b\u0e25\u0e48\u0e19", "16", "r"], ["\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e07\u0e1c\u0e25", "3", ""]],
   cap:"\u0e2a\u0e23\u0e38\u0e1b\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e40\u0e02\u0e49\u0e32\u0e2a\u0e39\u0e15\u0e23\u0e04\u0e30\u0e41\u0e19\u0e19 \u0e15\u0e23\u0e27\u0e08\u0e22\u0e49\u0e2d\u0e19\u0e01\u0e25\u0e31\u0e1a\u0e44\u0e14\u0e49\u0e17\u0e38\u0e01\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23",
   get:["\u0e40\u0e2b\u0e47\u0e19\u0e27\u0e48\u0e32\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e16\u0e39\u0e01\u0e19\u0e31\u0e1a\u0e40\u0e02\u0e49\u0e32\u0e04\u0e30\u0e41\u0e19\u0e19\u0e01\u0e35\u0e48\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23",
        "\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e16\u0e32\u0e19\u0e30\u0e01\u0e32\u0e23\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e44\u0e14\u0e49\u0e40\u0e2d\u0e07",
        "\u0e16\u0e2d\u0e19\u0e01\u0e32\u0e23\u0e2a\u0e48\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e14\u0e49\u0e17\u0e38\u0e01\u0e40\u0e21\u0e37\u0e48\u0e2d"]}
];
/* \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e21\u0e21\u0e15\u0e34 \u0e0a\u0e37\u0e48\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e16\u0e39\u0e01\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e40\u0e1b\u0e47\u0e19\u0e0a\u0e37\u0e48\u0e2d\u0e2a\u0e21\u0e21\u0e15\u0e34 \u0e15\u0e32\u0e21\u0e2b\u0e25\u0e31\u0e01\u0e02\u0e49\u0e2d 6a */
var EA_CMP = [
  {m:"\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21\u0e15\u0e48\u0e2d 1 \u0e25\u0e47\u0e2d\u0e15", hint:"\u0e22\u0e34\u0e48\u0e07\u0e15\u0e48\u0e33\u0e22\u0e34\u0e48\u0e07\u0e14\u0e35", low:true, pre:"$", dec:2,
   me:12.40, med:9.20, best:7.10,
   bn:"Northgate \u2014 \u0e16\u0e39\u0e01\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14",
   wu:"\u0e41\u0e1e\u0e07\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   wd:"\u0e16\u0e39\u0e01\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   rk:17, tt:24,
   note:"\u0e16\u0e49\u0e32\u0e40\u0e17\u0e23\u0e14\u0e40\u0e14\u0e37\u0e2d\u0e19\u0e25\u0e30 20 \u0e25\u0e47\u0e2d\u0e15 \u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07\u0e19\u0e35\u0e49\u0e04\u0e37\u0e2d <b>$1,272 \u0e15\u0e48\u0e2d\u0e1b\u0e35</b>"},

  {m:"\u0e04\u0e48\u0e32\u0e43\u0e0a\u0e49\u0e08\u0e48\u0e32\u0e22\u0e23\u0e27\u0e21 12 \u0e40\u0e14\u0e37\u0e2d\u0e19", hint:"\u0e22\u0e34\u0e48\u0e07\u0e15\u0e48\u0e33\u0e22\u0e34\u0e48\u0e07\u0e14\u0e35", low:true, pre:"$", dec:0,
   me:2976, med:2208, best:1704,
   bn:"Northgate \u2014 \u0e16\u0e39\u0e01\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14",
   wu:"\u0e08\u0e48\u0e32\u0e22\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   wd:"\u0e08\u0e48\u0e32\u0e22\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   rk:19, tt:24,
   note:"\u0e22\u0e49\u0e32\u0e22\u0e44\u0e1b\u0e42\u0e1a\u0e23\u0e01\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a 1 \u0e02\u0e2d\u0e07\u0e2b\u0e21\u0e27\u0e14 \u0e1b\u0e23\u0e30\u0e2b\u0e22\u0e31\u0e14\u0e44\u0e14\u0e49 <b>$1,272 \u0e15\u0e48\u0e2d\u0e1b\u0e35</b> \u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e40\u0e17\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21"},

  {m:"\u0e40\u0e27\u0e25\u0e32\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22", hint:"\u0e22\u0e34\u0e48\u0e07\u0e15\u0e48\u0e33\u0e22\u0e34\u0e48\u0e07\u0e14\u0e35", low:true, suf:" ms", dec:0,
   me:38, med:52, best:24,
   bn:"Kestrel FX \u2014 \u0e40\u0e23\u0e47\u0e27\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14",
   wu:"\u0e0a\u0e49\u0e32\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   wd:"\u0e40\u0e23\u0e47\u0e27\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   rk:6, tt:24,
   note:"\u0e41\u0e15\u0e48\u0e21\u0e35 <b>\u0e23\u0e35\u0e42\u0e04\u0e27\u0e15 12 \u0e04\u0e23\u0e31\u0e49\u0e07/\u0e40\u0e14\u0e37\u0e2d\u0e19</b> \u0e02\u0e13\u0e30\u0e17\u0e35\u0e48\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14\u0e2d\u0e22\u0e39\u0e48\u0e17\u0e35\u0e48 4 \u0e04\u0e23\u0e31\u0e49\u0e07"},

  {m:"\u0e2a\u0e40\u0e1b\u0e23\u0e14\u0e01\u0e27\u0e49\u0e32\u0e07\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34 / \u0e40\u0e14\u0e37\u0e2d\u0e19", hint:"\u0e22\u0e34\u0e48\u0e07\u0e15\u0e48\u0e33\u0e22\u0e34\u0e48\u0e07\u0e14\u0e35", low:true, suf:" \u0e04\u0e23\u0e31\u0e49\u0e07", dec:0,
   me:14, med:6, best:2,
   bn:"Vantabridge \u2014 \u0e19\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14",
   wu:"\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34\u0e1a\u0e48\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   wd:"\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   rk:21, tt:24,
   note:"\u0e21\u0e35 <b>248 \u0e1a\u0e31\u0e0d\u0e0a\u0e35</b> \u0e40\u0e08\u0e2d\u0e40\u0e2b\u0e15\u0e38\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e43\u0e19\u0e19\u0e32\u0e17\u0e35\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19 \u2014 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e40\u0e2b\u0e15\u0e38\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e04\u0e19"},

  {m:"\u0e40\u0e27\u0e25\u0e32\u0e16\u0e2d\u0e19\u0e40\u0e07\u0e34\u0e19\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22", hint:"\u0e22\u0e34\u0e48\u0e07\u0e15\u0e48\u0e33\u0e22\u0e34\u0e48\u0e07\u0e14\u0e35", low:true, kind:"hr", dec:2,
   me:8.27, med:5.67, best:1.20,
   bn:"Northgate \u2014 \u0e40\u0e23\u0e47\u0e27\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14",
   wu:"\u0e0a\u0e49\u0e32\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   wd:"\u0e40\u0e23\u0e47\u0e27\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   rk:15, tt:24,
   note:"\u0e40\u0e27\u0e25\u0e32\u0e17\u0e35\u0e48\u0e2b\u0e32\u0e22\u0e44\u0e1b\u0e2d\u0e22\u0e39\u0e48\u0e0a\u0e48\u0e27\u0e07 <b>\u0e2d\u0e19\u0e38\u0e21\u0e31\u0e15\u0e34\u0e04\u0e33\u0e02\u0e2d</b> \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e0a\u0e48\u0e27\u0e07\u0e18\u0e19\u0e32\u0e04\u0e32\u0e23\u0e42\u0e2d\u0e19"},

  {m:"\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e2a\u0e30\u0e2a\u0e21\u0e15\u0e48\u0e2d\u0e42\u0e1a\u0e23\u0e01", hint:"\u0e22\u0e34\u0e48\u0e07\u0e21\u0e32\u0e01\u0e22\u0e34\u0e48\u0e07\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e16\u0e37\u0e2d\u0e44\u0e14\u0e49", low:false, suf:" \u0e23\u0e32\u0e22\u0e01\u0e32\u0e23", dec:0,
   me:4812, med:2140, best:9650,
   bn:"\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e16\u0e39\u0e01\u0e15\u0e23\u0e27\u0e08\u0e21\u0e32\u0e01\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14",
   wu:"\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   wd:"\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14",
   rk:7, tt:24,
   note:"\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e21\u0e32\u0e01\u0e1e\u0e2d\u0e17\u0e35\u0e48\u0e08\u0e30\u0e2d\u0e2d\u0e01\u0e04\u0e30\u0e41\u0e19\u0e19\u0e44\u0e14\u0e49 \u2014 \u0e40\u0e01\u0e13\u0e11\u0e4c\u0e02\u0e31\u0e49\u0e19\u0e15\u0e48\u0e33\u0e04\u0e37\u0e2d <b>1,000 \u0e23\u0e32\u0e22\u0e01\u0e32\u0e23</b>"}
];
var EA_STEPS = [
  "\u0e2a\u0e21\u0e31\u0e04\u0e23\u0e2a\u0e21\u0e32\u0e0a\u0e34\u0e01 \u0e41\u0e25\u0e49\u0e27\u0e14\u0e32\u0e27\u0e19\u0e4c\u0e42\u0e2b\u0e25\u0e14\u0e44\u0e1f\u0e25\u0e4c EA \u0e08\u0e32\u0e01\u0e2b\u0e19\u0e49\u0e32\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13",
  "\u0e27\u0e32\u0e07\u0e44\u0e1f\u0e25\u0e4c\u0e43\u0e19\u0e42\u0e1f\u0e25\u0e40\u0e14\u0e2d\u0e23\u0e4c MQL4/Experts \u0e2b\u0e23\u0e37\u0e2d MQL5/Experts \u0e41\u0e25\u0e49\u0e27\u0e40\u0e1b\u0e34\u0e14\u0e42\u0e1b\u0e23\u0e41\u0e01\u0e23\u0e21\u0e43\u0e2b\u0e21\u0e48",
  "\u0e25\u0e32\u0e01 EA \u0e25\u0e07\u0e01\u0e23\u0e32\u0e1f\u0e44\u0e2b\u0e19\u0e01\u0e47\u0e44\u0e14\u0e49\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e01\u0e23\u0e32\u0e1f \u0e41\u0e25\u0e49\u0e27\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15 WebRequest \u0e44\u0e1b\u0e17\u0e35\u0e48\u0e42\u0e14\u0e40\u0e21\u0e19\u0e02\u0e2d\u0e07 RedStarTrust"
];
var EA_REQ = ["MetaTrader 4 \u0e2b\u0e23\u0e37\u0e2d 5", "\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e08\u0e23\u0e34\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e17\u0e14\u0e25\u0e2d\u0e07",
              "\u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e43\u0e0a\u0e49 VPS", "\u0e40\u0e1b\u0e34\u0e14\u0e01\u0e23\u0e32\u0e1f\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e47\u0e1e\u0e2d"];
function mtChart(){
  var c = [], x = 16;
  var seed = [58,72,64,86,78,96,88,74,66,80,92,104,96,86,78,90,102,112,104,94];
  for (var i = 0; i < seed.length; i++) {
    var top = 200 - seed[i] - 16, h = 12 + (i % 4) * 5;
    var up = i % 3 !== 1;
    c.push('<line x1="' + (x + 6) + '" y1="' + (top - 9) + '" x2="' + (x + 6) + '" y2="' +
      (top + h + 9) + '" stroke="' + (up ? "#3D9970" : "#C4444A") + '" stroke-width="1.4"/>');
    c.push('<rect x="' + x + '" y="' + top + '" width="12" height="' + h + '" rx="1.5" fill="' +
      (up ? "#2E7D5B" : "#A83B41") + '"/>');
    x += 20;
  }
  return '<svg viewBox="0 0 420 236" preserveAspectRatio="none" aria-hidden="true">' +
    '<g stroke="#1A2433" stroke-width="1">' +
    '<path d="M0 40h420M0 80h420M0 120h420M0 160h420M0 200h420"/></g>' + c.join("") + '</svg>';
}
/* \u0e08\u0e31\u0e07\u0e2b\u0e27\u0e30\u0e02\u0e2d\u0e07\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07: \u0e40\u0e1b\u0e34\u0e14\u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c \u2192 \u0e40\u0e01\u0e47\u0e1a\u0e04\u0e48\u0e32 \u2192 \u0e1b\u0e34\u0e14\u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c \u2192 \u0e40\u0e01\u0e47\u0e1a\u0e04\u0e48\u0e32 \u2192 \u0e2a\u0e48\u0e07\u0e02\u0e36\u0e49\u0e19\u0e23\u0e30\u0e1a\u0e1a
   \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e1a\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e08\u0e23\u0e34\u0e07 */
/* ── ตัวอย่าง EA — แสดงครบทุกก้อนพร้อมกัน ────────
   แต่ละก้อนมีตัวจับเวลาของตัวเอง และเดินเฉพาะก้อนที่อยู่ในสายตา
   เพื่อไม่ให้หกก้อนกะพริบพร้อมกันจนลายตา และไม่กินแรงเครื่องเปล่า ๆ          */
var EA_RUN = [];
function eaPad(n){ return (n < 10 ? "0" : "") + n; }
function eaClock(step){
  var t = 9 * 3600 + 41 * 60 + 2 + step * 47;
  return eaPad(Math.floor(t / 3600) % 24) + ":" + eaPad(Math.floor(t / 60) % 60) + ":" + eaPad(t % 60);
}
function eaFeedRow(i, tag, cls, html){
  var r = EA_RUN[i], box = document.getElementById("mt-rows-" + i);
  if (!r || !box) { return; }
  var el = document.createElement("div");
  el.className = "mt-row";
  el.innerHTML = '<time>' + eaClock(r.step) + '</time><span class="mt-tag ' + cls + '">' + tag +
    '</span><span>' + html + '</span>';
  box.insertBefore(el, box.firstChild);
  while (box.children.length > 4) { box.removeChild(box.lastChild); }
  r.count++;
  var c = document.getElementById("mt-cnt-" + i);
  if (c) { c.textContent = r.count + " \u0e23\u0e32\u0e22\u0e01\u0e32\u0e23"; }
}
function eaTick(i){
  var r = EA_RUN[i];
  if (!r || r.off || !r.seen) { return; }
  var s = r.step, k = s % 5;
  var lot = (0.10 + (s % 4) * 0.05).toFixed(2);
  var px = (1.08400 + (s % 9) * 0.00013).toFixed(5);
  var px2 = (parseFloat(px) + 0.00045).toFixed(5);
  var pnl = (3.6 + (s % 5) * 0.45).toFixed(2);
  var sp = (0.7 + (s % 4) * 0.1).toFixed(1);
  var ms = 32 + (s % 7) * 3;
  if (k === 0) {
    eaFeedRow(i, "OPEN", "open", "BUY <b>" + lot + "</b> EURUSD @ <b>" + px + "</b>");
  } else if (k === 1) {
    eaFeedRow(i, "LOG", "log", "\u0e2a\u0e40\u0e1b\u0e23\u0e14 <b>" + sp + " pip</b> \u00b7 \u0e04\u0e2d\u0e21\u0e21\u0e34\u0e0a\u0e0a\u0e31\u0e19 <b>$3.50</b> \u00b7 \u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07 <b>" + ms + " ms</b>");
  } else if (k === 2) {
    eaFeedRow(i, "CLOSE", "close", "BUY <b>" + lot + "</b> EURUSD @ <b>" + px2 + "</b>");
  } else if (k === 3) {
    eaFeedRow(i, "LOG", "log", "\u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08 <b>-0.2 pip</b> \u00b7 \u0e2a\u0e27\u0e2d\u0e1b <b>$0.00</b> \u00b7 \u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21 <b>$" + pnl + "</b>");
  } else {
    eaFeedRow(i, "SEND", "send", "\u0e2a\u0e48\u0e07\u0e02\u0e36\u0e49\u0e19 RedStar \u2014 <b>\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e25\u0e02\u0e1a\u0e31\u0e0d\u0e0a\u0e35 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e33\u0e44\u0e23\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19</b>");
  }
  var rows = document.querySelectorAll("#mt-panel-" + i + " .rw b");
  var j = s % Math.max(1, rows.length), b = rows[j];
  if (b && EA_PREV[i]) {
    var base = EA_PREV[i].rows[j];
    if (base) {
      var raw = base[1].match(/[0-9][0-9,]*(\.[0-9]+)?/);
      var num = raw ? parseFloat(raw[0].replace(/,/g, "")) : NaN;
      if (!isNaN(num)) {
        var dp = raw[1] ? raw[1].length - 1 : 0;
        var d = ((s % 5) - 2) * (num > 100 ? 3 : (num > 10 ? 0.4 : 0.1));
        var out = Math.max(0, num + d);
        var txt = dp ? out.toFixed(dp) : Math.round(out).toLocaleString("en-US");
        b.textContent = base[1].replace(/[0-9][0-9,]*(\.[0-9]+)?/, txt);
      }
    }
    b.classList.add("tick");
    setTimeout(function(){ b.classList.remove("tick"); }, 380);
  }
  cmpTick(i, s);
  r.step++;
}
function cmpFmt(c, v){
  if (c.kind === "hr") {
    var h = Math.floor(v), mn = Math.round((v - h) * 60);
    if (mn === 60) { h += 1; mn = 0; }
    return h + "\u0e0a\u0e21 " + eaPad(mn) + "\u0e19";
  }
  var t = c.dec ? v.toFixed(c.dec) : Math.round(v).toLocaleString("en-US");
  return (c.pre || "") + t + (c.suf || "");
}
function cmpDelta(c, v){
  var d = (v - c.med) / c.med * 100;
  return {pct: Math.abs(d), up: d >= 0, good: c.low ? (v < c.med) : (v > c.med)};
}
function cmpBar(c, v){ return Math.max(4, Math.min(100, v / c.mx * 100)); }
function eaCmp(i){
  var c = EA_CMP[i];
  c.mx = Math.max(c.me * 1.22, c.med, c.best) ;
  var d = cmpDelta(c, c.me);
  var num = (d.up ? "+" : "\u2212") + d.pct.toFixed(0) + "%";
  function row(cls, name, v){
    return '<div class="mt-cr ' + cls + '"><span>' + name + '</span>' +
      '<span class="mt-ct"><i style="width:' + cmpBar(c, v).toFixed(1) + '%"></i></span>' +
      '<span class="mt-cv">' + cmpFmt(c, v) + '</span></div>';
  }
  return '<div class="mt-cmp">' +
    '<div class="mt-cmph"><b>\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e42\u0e1a\u0e23\u0e01\u0e2d\u0e37\u0e48\u0e19\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19</b>' +
      '<span>' + c.m + ' \u00b7 ' + c.hint + '</span></div>' +
    '<p class="mt-vd"><em class="' + (d.good ? "good" : "bad") + '" id="cmp-num-' + i + '">' + num + '</em>' +
      '<i id="cmp-wd-' + i + '">' + (d.up ? c.wu : c.wd) + '<br>' +
      '\u0e08\u0e32\u0e01\u0e42\u0e1a\u0e23\u0e01 ' + c.tt + ' \u0e23\u0e32\u0e22\u0e17\u0e35\u0e48 EA \u0e40\u0e01\u0e47\u0e1a\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2d\u0e22\u0e39\u0e48</i></p>' +
    '<div class="mt-cr me' + (d.good ? " good" : "") + '" id="cmp-row-' + i + '">' +
      '<span>\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e04\u0e38\u0e13\u0e43\u0e0a\u0e49</span>' +
      '<span class="mt-ct"><i id="cmp-bar-' + i + '" style="width:' + cmpBar(c, c.me).toFixed(1) + '%"></i></span>' +
      '<span class="mt-cv" id="cmp-me-' + i + '">' + cmpFmt(c, c.me) + '</span></div>' +
    row("", "\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e2b\u0e21\u0e27\u0e14", c.med) +
    row("best", c.bn, c.best) +
    '<p class="mt-rank">\u0e2d\u0e22\u0e39\u0e48\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a <b>' + c.rk + ' \u0e08\u0e32\u0e01 ' + c.tt + '</b> \u00b7 ' + c.note + '</p>' +
    '</div>';
}
function cmpTick(i, s){
  var c = EA_CMP[i];
  if (!c) { return; }
  var v = c.me * (1 + (((s % 5) - 2) * 0.02));
  var d = cmpDelta(c, v);
  var n = document.getElementById("cmp-num-" + i);
  var w = document.getElementById("cmp-wd-" + i);
  var b = document.getElementById("cmp-bar-" + i);
  var m = document.getElementById("cmp-me-" + i);
  var rw = document.getElementById("cmp-row-" + i);
  if (n) {
    n.textContent = (d.up ? "+" : "\u2212") + d.pct.toFixed(0) + "%";
    n.className = d.good ? "good" : "bad";
  }
  if (w) { w.innerHTML = (d.up ? c.wu : c.wd) + "<br>\u0e08\u0e32\u0e01\u0e42\u0e1a\u0e23\u0e01 " + c.tt +
    " \u0e23\u0e32\u0e22\u0e17\u0e35\u0e48 EA \u0e40\u0e01\u0e47\u0e1a\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2d\u0e22\u0e39\u0e48"; }
  if (b) { b.style.width = cmpBar(c, v).toFixed(1) + "%"; }
  if (m) { m.textContent = cmpFmt(c, v); }
  if (rw) { rw.className = "mt-cr me" + (d.good ? " good" : ""); }
}
function eaDemo(i){
  var v = EA_PREV[i];
  return '<div class="mt-win"><div class="mt-bar"><i></i><i></i><i></i>' +
      '<span>MetaTrader \u00b7 ' + v.sym + '</span></div>' +
      '<div class="mt-stage">' + mtChart() +
      '<div class="mt-panel" id="mt-panel-' + i + '"><div class="hd">' + v.hd +
      '<span class="live"><i></i>LIVE</span></div>' +
      v.rows.map(function(r){
        return '<div class="rw"><span>' + r[0] + '</span><b class="' + r[2] + '">' + r[1] + '</b></div>';
      }).join("") + '</div></div></div>' +
    eaCmp(i) +
    '<div class="mt-feed"><div class="mt-fhd"><b>\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e17\u0e35\u0e48 EA \u0e40\u0e01\u0e47\u0e1a</b>' +
      '<span class="cnt" id="mt-cnt-' + i + '">0 \u0e23\u0e32\u0e22\u0e01\u0e32\u0e23</span>' +
      '<button type="button" class="mt-fbtn" data-eapause="' + i + '" aria-pressed="false">\u0e2b\u0e22\u0e38\u0e14</button></div>' +
      '<div class="mt-rows" id="mt-rows-' + i + '"></div></div>' +
    '<p class="mt-cap">' + v.cap + '</p>';
}
function eaStart(i){
  EA_RUN[i] = {step: 0, count: 0, off: false, seen: true, t: null};
  eaTick(i); eaTick(i);
  EA_RUN[i].t = setInterval(function(){ eaTick(i); }, 1300 + i * 130);
}
function eaWatch(){
  if (typeof IntersectionObserver === "undefined") { return; }
  var ob = new IntersectionObserver(function(es){
    es.forEach(function(e){
      var i = parseInt(e.target.dataset.eablock, 10);
      if (EA_RUN[i]) { EA_RUN[i].seen = e.isIntersecting; }
    });
  }, {rootMargin: "120px 0px"});
  document.querySelectorAll("[data-eablock]").forEach(function(el){ ob.observe(el); });
}
document.addEventListener("click", function(ev){
  var p = ev.target.closest("[data-eapause]");
  if (!p) { return; }
  var i = parseInt(p.dataset.eapause, 10), r = EA_RUN[i];
  if (!r) { return; }
  r.off = !r.off;
  p.textContent = r.off ? "\u0e40\u0e25\u0e48\u0e19" : "\u0e2b\u0e22\u0e38\u0e14";
  p.setAttribute("aria-pressed", String(r.off));
});

/* \u2500\u2500 RedStar EA Suite \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
   \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e43\u0e19 Dashboard \u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14 \u0e41\u0e25\u0e30\u0e0a\u0e37\u0e48\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e43\u0e19\u0e01\u0e32\u0e23\u0e41\u0e08\u0e49\u0e07\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e15\u0e31\u0e49\u0e07\u0e02\u0e36\u0e49\u0e19\u0e40\u0e2d\u0e07
   \u0e15\u0e32\u0e21\u0e01\u0e0e\u0e02\u0e49\u0e2d 6a \u2014 \u0e2b\u0e49\u0e32\u0e21\u0e0a\u0e35\u0e49\u0e0a\u0e37\u0e48\u0e2d\u0e08\u0e23\u0e34\u0e07\u0e43\u0e19\u0e02\u0e49\u0e2d\u0e01\u0e25\u0e48\u0e32\u0e27\u0e2b\u0e32\u0e17\u0e35\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19       */
var EA_LIST = [
  {ph:"Phase 1", n:"Trade Analytics EA",
   p:"\u0e27\u0e31\u0e14\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e08\u0e23\u0e34\u0e07\u0e02\u0e2d\u0e07\u0e17\u0e38\u0e01\u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c \u2014 \u0e2a\u0e40\u0e1b\u0e23\u0e14 \u0e04\u0e2d\u0e21\u0e21\u0e34\u0e0a\u0e0a\u0e31\u0e19 \u0e2a\u0e27\u0e2d\u0e1b \u0e41\u0e25\u0e30\u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08",
   b:["\u0e40\u0e2b\u0e47\u0e19\u0e27\u0e48\u0e32\u0e40\u0e07\u0e34\u0e19\u0e2b\u0e32\u0e22\u0e44\u0e1b\u0e15\u0e23\u0e07\u0e44\u0e2b\u0e19\u0e02\u0e2d\u0e07\u0e41\u0e15\u0e48\u0e25\u0e30\u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c",
      "\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e23\u0e32\u0e22\u0e40\u0e14\u0e37\u0e2d\u0e19",
      "\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e15\u0e48\u0e2d\u0e25\u0e47\u0e2d\u0e15 \u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e17\u0e35\u0e48\u0e42\u0e06\u0e29\u0e13\u0e32\u0e44\u0e27\u0e49"],
   f:"\u0e04\u0e19\u0e17\u0e35\u0e48\u0e40\u0e17\u0e23\u0e14\u0e16\u0e35\u0e48 \u0e41\u0e25\u0e30\u0e2d\u0e22\u0e32\u0e01\u0e23\u0e39\u0e49\u0e27\u0e48\u0e32\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e08\u0e23\u0e34\u0e07\u0e15\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01\u0e17\u0e35\u0e48\u0e42\u0e06\u0e29\u0e13\u0e32\u0e41\u0e04\u0e48\u0e44\u0e2b\u0e19"},
  {ph:"Phase 2", n:"Broker Compare EA",
   p:"\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49\u0e2d\u0e22\u0e39\u0e48\u0e01\u0e31\u0e1a\u0e23\u0e32\u0e22\u0e2d\u0e37\u0e48\u0e19 \u0e08\u0e32\u0e01\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e08\u0e23\u0e34\u0e07\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e40\u0e2d\u0e07",
   b:["\u0e23\u0e39\u0e49\u0e27\u0e48\u0e32\u0e22\u0e49\u0e32\u0e22\u0e42\u0e1a\u0e23\u0e01\u0e41\u0e25\u0e49\u0e27\u0e1b\u0e23\u0e30\u0e2b\u0e22\u0e31\u0e14\u0e08\u0e23\u0e34\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48",
      "\u0e04\u0e34\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e07\u0e34\u0e19\u0e15\u0e48\u0e2d\u0e1b\u0e35 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e01\u0e25\u0e32\u0e07",
      "\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e1a\u0e19\u0e2a\u0e44\u0e15\u0e25\u0e4c\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e40\u0e2d\u0e07"],
   f:"\u0e04\u0e19\u0e17\u0e35\u0e48\u0e25\u0e31\u0e07\u0e40\u0e25\u0e27\u0e48\u0e32\u0e08\u0e30\u0e22\u0e49\u0e32\u0e22\u0e42\u0e1a\u0e23\u0e01\u0e2b\u0e23\u0e37\u0e2d\u0e2d\u0e22\u0e39\u0e48\u0e17\u0e35\u0e48\u0e40\u0e14\u0e34\u0e21\u0e14\u0e35"},
  {ph:"Phase 3", n:"Broker Health Monitor",
   p:"\u0e27\u0e31\u0e14\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e01\u0e32\u0e23\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e41\u0e1a\u0e1a\u0e40\u0e23\u0e35\u0e22\u0e25\u0e44\u0e17\u0e21\u0e4c",
   b:["\u0e40\u0e2b\u0e47\u0e19\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e47\u0e27\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e21\u0e34\u0e25\u0e25\u0e34\u0e27\u0e34\u0e19\u0e32\u0e17\u0e35",
      "\u0e19\u0e31\u0e1a\u0e23\u0e35\u0e42\u0e04\u0e27\u0e15 \u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08\u0e1a\u0e27\u0e01 \u0e41\u0e25\u0e30\u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08\u0e25\u0e1a",
      "\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e40\u0e23\u0e34\u0e48\u0e21\u0e41\u0e22\u0e48\u0e25\u0e07"],
   f:"\u0e2a\u0e32\u0e22 Scalping \u0e41\u0e25\u0e30\u0e04\u0e19\u0e17\u0e35\u0e48\u0e23\u0e31\u0e19 EA \u0e0b\u0e36\u0e48\u0e07\u0e2d\u0e48\u0e2d\u0e19\u0e44\u0e2b\u0e27\u0e01\u0e31\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e47\u0e27"},
  {ph:"Phase 3", n:"Community Alert EA",
   p:"\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e2b\u0e25\u0e32\u0e22\u0e04\u0e19\u0e40\u0e08\u0e2d\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e43\u0e19\u0e40\u0e27\u0e25\u0e32\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19",
   b:["\u0e19\u0e31\u0e1a\u0e08\u0e32\u0e01\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e08\u0e23\u0e34\u0e07 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e04\u0e32\u0e14\u0e40\u0e14\u0e32",
      "\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e20\u0e32\u0e22\u0e43\u0e19\u0e44\u0e21\u0e48\u0e01\u0e35\u0e48\u0e19\u0e32\u0e17\u0e35",
      "\u0e1a\u0e2d\u0e01\u0e08\u0e33\u0e19\u0e27\u0e19\u0e04\u0e19\u0e17\u0e35\u0e48\u0e40\u0e08\u0e2d\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19"],
   f:"\u0e04\u0e19\u0e40\u0e17\u0e23\u0e14\u0e0a\u0e48\u0e27\u0e07\u0e02\u0e48\u0e32\u0e27 \u0e41\u0e25\u0e30\u0e04\u0e19\u0e17\u0e35\u0e48\u0e16\u0e37\u0e2d\u0e42\u0e1e\u0e0b\u0e34\u0e0a\u0e31\u0e19\u0e02\u0e49\u0e32\u0e21\u0e04\u0e37\u0e19"},
  {ph:"Phase 3", n:"Withdrawal Journal",
   p:"\u0e08\u0e31\u0e1a\u0e40\u0e27\u0e25\u0e32\u0e16\u0e2d\u0e19\u0e40\u0e07\u0e34\u0e19\u0e08\u0e23\u0e34\u0e07 \u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48\u0e01\u0e14\u0e16\u0e2d\u0e19\u0e08\u0e19\u0e40\u0e07\u0e34\u0e19\u0e40\u0e02\u0e49\u0e32\u0e1a\u0e31\u0e0d\u0e0a\u0e35",
   b:["\u0e41\u0e22\u0e01\u0e40\u0e27\u0e25\u0e32\u0e2d\u0e19\u0e38\u0e21\u0e31\u0e15\u0e34\u0e01\u0e31\u0e1a\u0e40\u0e27\u0e25\u0e32\u0e42\u0e2d\u0e19",
      "\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e47\u0e27\u0e16\u0e2d\u0e19\u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07\u0e42\u0e1a\u0e23\u0e01",
      "\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e2a\u0e32\u0e21\u0e02\u0e31\u0e49\u0e19\u0e42\u0e14\u0e22\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e40\u0e2d\u0e07"],
   f:"\u0e04\u0e19\u0e17\u0e35\u0e48\u0e43\u0e2b\u0e49\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e33\u0e04\u0e31\u0e0d\u0e01\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e16\u0e2d\u0e19\u0e40\u0e07\u0e34\u0e19\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e2a\u0e40\u0e1b\u0e23\u0e14"},
  {ph:"Phase 4", n:"Institutional Evidence Collector",
   p:"\u0e23\u0e27\u0e21\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e40\u0e02\u0e49\u0e32\u0e2a\u0e39\u0e15\u0e23\u0e43\u0e2b\u0e49\u0e04\u0e30\u0e41\u0e19\u0e19 RedStar",
   b:["\u0e17\u0e38\u0e01\u0e04\u0e30\u0e41\u0e19\u0e19\u0e22\u0e49\u0e2d\u0e19\u0e01\u0e25\u0e31\u0e1a\u0e44\u0e1b\u0e2b\u0e32\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e44\u0e14\u0e49",
      "\u0e40\u0e1b\u0e34\u0e14\u0e2a\u0e39\u0e15\u0e23\u0e16\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e43\u0e2b\u0e49\u0e40\u0e2b\u0e47\u0e19",
      "\u0e2d\u0e31\u0e1b\u0e40\u0e14\u0e15\u0e15\u0e32\u0e21\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e43\u0e2b\u0e21\u0e48\u0e15\u0e25\u0e2d\u0e14"],
   f:"\u0e17\u0e38\u0e01\u0e04\u0e19\u0e17\u0e35\u0e48\u0e2d\u0e48\u0e32\u0e19\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a\u0e1a\u0e19\u0e40\u0e27\u0e47\u0e1a\u0e19\u0e35\u0e49 \u2014 \u0e40\u0e1b\u0e47\u0e19\u0e40\u0e1a\u0e37\u0e49\u0e2d\u0e07\u0e2b\u0e25\u0e31\u0e07\u0e02\u0e2d\u0e07\u0e04\u0e30\u0e41\u0e19\u0e19"}
];
(function(){
  var d = document.getElementById("ea-dash");
  if (!d) { return; }
  var ic = function(p){ return '<span class="ic"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" ' +
    'stroke="#D92D20" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    p + '</svg></span>'; };
  var TILES = [
    [ic('<rect x="3" y="6" width="18" height="13" rx="2.5"></rect><path d="M16 12h2.5"></path>'),
     "Spread Cost", 126, 92],
    [ic('<path d="M6 3.5h12v17l-3-2-3 2-3-2-3 2z"></path><path d="M9.5 8.5h5M9.5 12.5h5"></path>'),
     "Commission", 70, 62],
    [ic('<path d="M4 7h12l-3-3M20 17H8l3 3"></path>'),
     "Swap", 33, 18],
    [ic('<path d="M3 17l5-6 4 3 4-6 5 4"></path><path d="M17 6h4v4"></path>'),
     "Slippage", 19, 12]
  ];
  d.className = "ea-dash";
  d.innerHTML =
    '<div class="ea-dhead"><h3>Dashboard \u2014 \u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e08\u0e2d\u0e17\u0e35\u0e48\u0e2a\u0e21\u0e32\u0e0a\u0e34\u0e01\u0e08\u0e30\u0e40\u0e2b\u0e47\u0e19</h3>' +
      '<span class="dlive"><i></i>LIVE</span>' +
      '<span>EURUSD \u00b7 812 \u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c \u00b7 \u0e23\u0e2d\u0e1a 30 \u0e27\u0e31\u0e19\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14</span></div>' +
    '<div class="ea-tiles">' + TILES.map(function(t, ix){
      var pc = Math.round((t[2] - t[3]) / t[3] * 100);
      return '<div class="ea-tile">' + t[0] + '<span class="lb">' + t[1] + '</span>' +
        '<span class="vl" id="dk-' + ix + '">$' + t[2] + '</span>' +
        '<span class="sb">\u0e23\u0e2d\u0e1a 30 \u0e27\u0e31\u0e19\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14</span>' +
        '<span class="cmp">\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14 <b>$' + t[3] + '</b><br>' +
        '\u0e42\u0e1a\u0e23\u0e01\u0e04\u0e38\u0e13 <b class="' + (pc >= 0 ? "up" : "dn") + '" id="dp-' + ix + '">' +
        (pc >= 0 ? "+" : "\u2212") + Math.abs(pc) + '%</b></span></div>';
    }).join("") + '</div>' +
    '<div class="ea-panes">' +
      '<div class="ea-pane"><h4>\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e42\u0e1a\u0e23\u0e01\u0e2d\u0e37\u0e48\u0e19' +
        '<span class="pill">24 \u0e42\u0e1a\u0e23\u0e01\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19</span></h4>' +
        '<p class="ea-big"><em id="dg-pc">+35%</em><i>\u0e41\u0e1e\u0e07\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14<br>' +
        '\u0e04\u0e48\u0e32\u0e43\u0e0a\u0e49\u0e08\u0e48\u0e32\u0e22\u0e23\u0e27\u0e21\u0e15\u0e48\u0e2d\u0e1b\u0e35 \u0e17\u0e35\u0e48 240 \u0e25\u0e47\u0e2d\u0e15</i></p>' +
        '<div class="ea-brow me"><span>\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e04\u0e38\u0e13\u0e43\u0e0a\u0e49</span>' +
        '<span class="ea-btube"><i id="dg-b0" style="width:82%"></i></span>' +
        '<span class="ea-bv" id="dg-v0">$2,976</span></div>' +
        '<div class="ea-brow"><span>\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e2b\u0e21\u0e27\u0e14</span>' +
        '<span class="ea-btube"><i style="width:61%"></i></span>' +
        '<span class="ea-bv">$2,208</span></div>' +
        '<div class="ea-brow bs"><span>Northgate \u2014 \u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a 1</span>' +
        '<span class="ea-btube"><i style="width:47%"></i></span>' +
        '<span class="ea-bv">$1,704</span></div>' +
        '<div class="ea-save" style="margin-top:13px"><b>\u0e22\u0e49\u0e32\u0e22\u0e44\u0e1b Northgate Markets</b>' +
        '<span>\u0e1b\u0e23\u0e30\u0e2b\u0e22\u0e31\u0e14\u0e44\u0e14\u0e49\u0e15\u0e48\u0e2d\u0e1b\u0e35\u0e42\u0e14\u0e22\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13</span>' +
        '<em id="dg-sv">$1,272</em></div>' +
        '<p class="mt-rank" style="margin-top:11px">\u0e2d\u0e22\u0e39\u0e48\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a <b>19 \u0e08\u0e32\u0e01 24</b> \u0e14\u0e49\u0e32\u0e19\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19 \u00b7 \u0e40\u0e17\u0e35\u0e22\u0e1a\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e08\u0e23\u0e34\u0e07\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e04\u0e48\u0e32\u0e42\u0e06\u0e29\u0e13\u0e32</p></div>' +
      '<div class="ea-pane"><h4>\u0e2a\u0e38\u0e02\u0e20\u0e32\u0e1e\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c</h4><div class="ea-kv">' +
        '<div class="ea-k"><span class="st ok">\u25cf \u0e14\u0e35\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07</span>' +
        '<span class="nm">Execution \u00b7 \u0e01\u0e25\u0e32\u0e07 52 ms</span>' +
        '<span class="vv" id="dh-0">38 ms</span></div>' +
        '<div class="ea-k"><span class="st warn">\u25cf \u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07</span>' +
        '<span class="nm">Requotes \u00b7 \u0e01\u0e25\u0e32\u0e07 4</span>' +
        '<span class="vv" id="dh-1">12</span></div>' +
        '<div class="ea-k"><span class="st ok">\u25cf \u0e14\u0e35\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07</span>' +
        '<span class="nm">Slippage \u0e1a\u0e27\u0e01 \u00b7 \u0e01\u0e25\u0e32\u0e07 48%</span>' +
        '<span class="vv" id="dh-2">61%</span></div>' +
        '<div class="ea-k"><span class="st ok">\u25cf \u0e14\u0e35\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07</span>' +
        '<span class="nm">Freeze \u00b7 \u0e01\u0e25\u0e32\u0e07 2</span>' +
        '<span class="vv" id="dh-3">0</span></div></div></div>' +
      '<div class="ea-pane"><h4>Live Community Alerts</h4>' +
        '<div class="ea-al hi"><b><i></i>Apex Global FX</b>' +
        '<span>\u0e2a\u0e40\u0e1b\u0e23\u0e14\u0e01\u0e23\u0e30\u0e0a\u0e32\u0e01\u0e40\u0e01\u0e34\u0e19 300% \u00b7 <span class="ct" id="da-0">248</span> \u0e04\u0e19\u0e40\u0e08\u0e2d\u0e43\u0e19 30 \u0e19\u0e32\u0e17\u0e35</span></div>' +
        '<div class="ea-al md"><b><i></i>Vertex Bridge Markets</b>' +
        '<span>\u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08\u0e2a\u0e39\u0e07\u0e0a\u0e48\u0e27\u0e07\u0e02\u0e48\u0e32\u0e27 \u00b7 91 \u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e04\u0e25\u0e49\u0e32\u0e22\u0e01\u0e31\u0e19</span></div></div>' +
    '</div>' +
    '<div class="ea-dnote"><b>\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e43\u0e19 Dashboard \u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a</b> ' +
    '\u00b7 \u0e0a\u0e37\u0e48\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e43\u0e19\u0e2a\u0e48\u0e27\u0e19\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e41\u0e25\u0e30\u0e41\u0e08\u0e49\u0e07\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e15\u0e31\u0e49\u0e07\u0e02\u0e36\u0e49\u0e19\u0e40\u0e2d\u0e07 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e17\u0e35\u0e48\u0e21\u0e35\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e23\u0e34\u0e07</div>';

  var DBASE = TILES.map(function(t){ return {v: t[2], med: t[3]}; });
  var DH = [{v:38, s:" ms", d:0}, {v:12, s:"", d:0}, {v:61, s:"%", d:0}, {v:0, s:"", d:0}];
  var dstep = 0;
  function flash(el){
    if (!el) { return; }
    el.classList.add("tk");
    setTimeout(function(){ el.classList.remove("tk"); }, 420);
  }
  function dashTick(){
    var box = document.getElementById("ea-dash");
    if (!box) { return; }
    var r = box.getBoundingClientRect();
    if (r.bottom < -200 || r.top > (window.innerHeight || 900) + 200) { return; }
    var s = dstep++, tot = 0, med = 0;
    DBASE.forEach(function(b, ix){
      var v = Math.max(1, Math.round(b.v + ((s + ix) % 5 - 2) * (b.v > 60 ? 2 : 1)));
      tot += v; med += b.med;
      var e = document.getElementById("dk-" + ix);
      if (e) { e.textContent = "$" + v; }
      var pc = Math.round((v - b.med) / b.med * 100);
      var p = document.getElementById("dp-" + ix);
      if (p) {
        p.textContent = (pc >= 0 ? "+" : "\u2212") + Math.abs(pc) + "%";
        p.className = pc >= 0 ? "up" : "dn";
      }
      if ((s + ix) % 4 === 0) { flash(e); }
    });
    var yr = tot * 12, ymed = med * 12, best = 1704;
    var gp = Math.round((yr - ymed) / ymed * 100);
    var g = document.getElementById("dg-pc");
    if (g) {
      g.textContent = (gp >= 0 ? "+" : "\u2212") + Math.abs(gp) + "%";
      g.className = gp >= 0 ? "" : "dn";
    }
    var v0 = document.getElementById("dg-v0");
    if (v0) { v0.textContent = "$" + yr.toLocaleString("en-US"); }
    var b0 = document.getElementById("dg-b0");
    if (b0) { b0.style.width = Math.min(100, yr / 3620 * 100).toFixed(1) + "%"; }
    var sv = document.getElementById("dg-sv");
    if (sv) { sv.textContent = "$" + Math.max(0, yr - best).toLocaleString("en-US"); }
    DH.forEach(function(h, ix){
      var v = Math.max(0, h.v + ((s + ix * 2) % 5 - 2) * (h.v > 30 ? 2 : (h.v > 5 ? 1 : 0)));
      var e = document.getElementById("dh-" + ix);
      if (e) { e.textContent = v + h.s; }
      if ((s + ix) % 5 === 0) { flash(e); }
    });
    var a = document.getElementById("da-0");
    if (a) { a.textContent = 248 + (s % 9) * 3; }
  }
  dashTick();
  setInterval(dashTick, 1500);

  var lg = document.getElementById("ea-legend");
  if (lg) {
    var LG = [
      ["\u0e08\u0e2d MetaTrader \u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13",
       "\u0e01\u0e23\u0e32\u0e1f\u0e41\u0e25\u0e30\u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c\u0e17\u0e35\u0e48\u0e04\u0e38\u0e13\u0e40\u0e17\u0e23\u0e14\u0e15\u0e32\u0e21\u0e1b\u0e01\u0e15\u0e34 EA \u0e44\u0e21\u0e48\u0e40\u0e02\u0e49\u0e32\u0e44\u0e1b\u0e22\u0e38\u0e48\u0e07 \u0e44\u0e21\u0e48\u0e40\u0e1b\u0e34\u0e14\u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c\u0e41\u0e17\u0e19",
       "\u0e2d\u0e48\u0e32\u0e19\u0e27\u0e48\u0e32 \u2014 \u0e04\u0e38\u0e13\u0e40\u0e17\u0e23\u0e14\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e40\u0e14\u0e34\u0e21\u0e17\u0e38\u0e01\u0e2d\u0e22\u0e48\u0e32\u0e07"],
      ["\u0e41\u0e1c\u0e07\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48 EA \u0e2d\u0e48\u0e32\u0e19\u0e44\u0e14\u0e49",
       "\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e21\u0e38\u0e21\u0e02\u0e27\u0e32\u0e1a\u0e19\u0e01\u0e23\u0e32\u0e1f \u0e04\u0e37\u0e2d\u0e2a\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48 EA \u0e27\u0e31\u0e14\u0e44\u0e14\u0e49\u0e08\u0e23\u0e34\u0e07\u0e08\u0e32\u0e01\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e04\u0e38\u0e13 \u0e40\u0e0a\u0e48\u0e19 \u0e2a\u0e40\u0e1b\u0e23\u0e14 \u0e04\u0e2d\u0e21\u0e21\u0e34\u0e0a\u0e0a\u0e31\u0e19 \u0e2a\u0e27\u0e2d\u0e1b \u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e47\u0e27\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07",
       "\u0e2d\u0e48\u0e32\u0e19\u0e27\u0e48\u0e32 \u2014 \u0e42\u0e1a\u0e23\u0e01\u0e04\u0e34\u0e14\u0e04\u0e38\u0e13\u0e40\u0e17\u0e48\u0e32\u0e44\u0e2b\u0e23\u0e48"],
      ["\u0e41\u0e16\u0e1a\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e42\u0e1a\u0e23\u0e01\u0e2d\u0e37\u0e48\u0e19",
       "\u0e40\u0e2d\u0e32\u0e04\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e44\u0e1b\u0e27\u0e32\u0e07\u0e02\u0e49\u0e32\u0e07\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e2b\u0e21\u0e27\u0e14 \u0e41\u0e25\u0e30\u0e42\u0e1a\u0e23\u0e01\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a 1 \u0e02\u0e2d\u0e07\u0e2b\u0e21\u0e27\u0e14\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19",
       "\u0e2d\u0e48\u0e32\u0e19\u0e27\u0e48\u0e32 \u2014 \u0e14\u0e35\u0e2b\u0e23\u0e37\u0e2d\u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e17\u0e35\u0e48\u0e2d\u0e37\u0e48\u0e19\u0e40\u0e17\u0e48\u0e32\u0e44\u0e23"],
      ["\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e07\u0e02\u0e36\u0e49\u0e19\u0e23\u0e30\u0e1a\u0e1a",
       "\u0e17\u0e38\u0e01\u0e1a\u0e23\u0e23\u0e17\u0e31\u0e14\u0e04\u0e37\u0e2d\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e07\u0e40\u0e02\u0e49\u0e32 RedStar \u0e08\u0e23\u0e34\u0e07 \u0e04\u0e38\u0e13\u0e40\u0e2b\u0e47\u0e19\u0e44\u0e14\u0e49\u0e04\u0e23\u0e1a\u0e27\u0e48\u0e32\u0e2a\u0e48\u0e07\u0e2d\u0e30\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07",
       "\u0e2d\u0e48\u0e32\u0e19\u0e27\u0e48\u0e32 \u2014 \u0e40\u0e23\u0e32\u0e40\u0e2d\u0e32\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e44\u0e1b\u0e41\u0e04\u0e48\u0e44\u0e2b\u0e19"]
    ];
    lg.className = "ea-lg";
    lg.innerHTML = '<h4>\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e48\u0e32\u0e07\u0e41\u0e2a\u0e14\u0e07\u0e1c\u0e25\u0e1a\u0e2d\u0e01\u0e2d\u0e30\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07</h4>' +
      '<p>\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e02\u0e2d\u0e07 EA \u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e02\u0e49\u0e32\u0e07\u0e25\u0e48\u0e32\u0e07\u0e43\u0e0a\u0e49\u0e42\u0e04\u0e23\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19 4 \u0e2a\u0e48\u0e27\u0e19 \u0e2d\u0e48\u0e32\u0e19\u0e08\u0e32\u0e01\u0e1a\u0e19\u0e25\u0e07\u0e25\u0e48\u0e32\u0e07</p>' +
      '<div class="ea-lgg">' + LG.map(function(g, ix){
        return '<div class="ea-lgi"><span class="no">' + (ix + 1) + '</span>' +
          '<h5>' + g[0] + '</h5><p>' + g[1] + '</p><span class="rd">' + g[2] + '</span></div>';
      }).join("") + '</div>';
  }

  var host = document.getElementById("ea-cards");
  if (host) {
    host.innerHTML = EA_LIST.map(function(e, ix){
      var v = EA_PREV[ix];
      return '<section class="ea-block" data-eablock="' + ix + '">' +
        '<div class="ea-info">' +
          '<div class="ea-top"><span class="ea-ph">' + e.ph + '</span>' + awardStar(26) + '</div>' +
          '<h4 class="ea-h4">' + e.n + '</h4>' +
          '<p class="ea-p">' + e.p + '</p>' +
          '<div class="ea-ul">' + e.b.map(function(x){ return '<span class="ea-li">' + x + '</span>'; }).join("") + '</div>' +
          '<div class="ea-got"><b>\u0e04\u0e38\u0e13\u0e08\u0e30\u0e44\u0e14\u0e49\u0e2d\u0e30\u0e44\u0e23</b>' +
            v.get.map(function(g){ return '<span>' + g + '</span>'; }).join("") + '</div>' +
          '<div class="ea-for"><b>\u0e40\u0e2b\u0e21\u0e32\u0e30\u0e01\u0e31\u0e1a</b>' + e.f + '</div>' +
          '<div class="ea-cta"><a class="ea-get" href="#/signup" data-nav="signup">\u0e23\u0e31\u0e1a\u0e1f\u0e23\u0e35' +
          '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" ' +
          'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
          '<path d="M5 12h13M13 6.5l5.5 5.5L13 17.5"></path></svg></a>' +
          '<span class="ea-mem">\u0e15\u0e49\u0e2d\u0e07\u0e2a\u0e21\u0e31\u0e04\u0e23\u0e2a\u0e21\u0e32\u0e0a\u0e34\u0e01\u0e01\u0e48\u0e2d\u0e19 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e04\u0e48\u0e32\u0e43\u0e0a\u0e49\u0e08\u0e48\u0e32\u0e22</span></div>' +
        '</div>' +
        '<div class="ea-demo">' + eaDemo(ix) + '</div>' +
      '</section>';
    }).join("");
    EA_LIST.forEach(function(_, ix){ eaStart(ix); });
    eaWatch();
  }

  var ins = document.getElementById("ea-install");
  if (ins) {
    ins.innerHTML =
      '<div><h5>\u0e15\u0e34\u0e14\u0e15\u0e31\u0e49\u0e07\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e44\u0e23 \u2014 \u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27</h5>' +
      '<ol class="ea-steps">' + EA_STEPS.map(function(s){ return '<li>' + s + '</li>'; }).join("") + '</ol></div>' +
      '<div><h5>\u0e2a\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35</h5>' +
      '<div class="ea-req">' + EA_REQ.map(function(r){ return '<span>' + r + '</span>'; }).join("") + '</div></div>';
  }


  var pv = document.getElementById("ea-priv");
  if (pv) {
    var chk = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#067647" stroke-width="2.4" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 12.5l5 5 10-11"></path></svg>';
    var xx = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#B42318" stroke-width="2.4" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg>';
    var SEND = ["\u0e2a\u0e40\u0e1b\u0e23\u0e14", "\u0e04\u0e2d\u0e21\u0e21\u0e34\u0e0a\u0e0a\u0e31\u0e19", "\u0e2a\u0e27\u0e2d\u0e1b",
                "\u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08", "\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e47\u0e27\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07",
                "\u0e02\u0e19\u0e32\u0e14\u0e25\u0e47\u0e2d\u0e15 \u00b7 \u0e2a\u0e31\u0e0d\u0e25\u0e31\u0e01\u0e29\u0e13\u0e4c \u00b7 \u0e0a\u0e37\u0e48\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c \u00b7 \u0e40\u0e27\u0e25\u0e32"];
    var NO = ["\u0e40\u0e25\u0e02\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e40\u0e17\u0e23\u0e14", "\u0e23\u0e2b\u0e31\u0e2a\u0e1c\u0e48\u0e32\u0e19\u0e2b\u0e23\u0e37\u0e2d\u0e23\u0e2b\u0e31\u0e2a\u0e19\u0e31\u0e01\u0e25\u0e07\u0e17\u0e38\u0e19",
              "\u0e0a\u0e37\u0e48\u0e2d-\u0e19\u0e32\u0e21\u0e2a\u0e01\u0e38\u0e25 \u0e2d\u0e35\u0e40\u0e21\u0e25 \u0e40\u0e1a\u0e2d\u0e23\u0e4c\u0e42\u0e17\u0e23",
              "\u0e22\u0e2d\u0e14\u0e40\u0e07\u0e34\u0e19\u0e43\u0e19\u0e1a\u0e31\u0e0d\u0e0a\u0e35", "\u0e01\u0e33\u0e44\u0e23\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13",
              "\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e2b\u0e23\u0e37\u0e2d\u0e01\u0e25\u0e22\u0e38\u0e17\u0e18\u0e4c\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14"];
    var W = [["\u0e2a\u0e40\u0e1b\u0e23\u0e14", 25], ["\u0e01\u0e32\u0e23\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07", 25],
             ["\u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08", 20], ["\u0e01\u0e32\u0e23\u0e16\u0e2d\u0e19\u0e40\u0e07\u0e34\u0e19", 15],
             ["\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e0a\u0e38\u0e21\u0e0a\u0e19", 15]];
    pv.className = "ea-priv";
    pv.innerHTML =
      '<h3>\u0e40\u0e23\u0e32\u0e40\u0e01\u0e47\u0e1a\u0e2d\u0e30\u0e44\u0e23 \u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e40\u0e01\u0e47\u0e1a\u0e2d\u0e30\u0e44\u0e23</h3>' +
      '<p>\u0e40\u0e27\u0e47\u0e1a\u0e08\u0e31\u0e14\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a\u0e08\u0e30\u0e19\u0e48\u0e32\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e44\u0e14\u0e49\u0e01\u0e47\u0e15\u0e48\u0e2d\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e1a\u0e2d\u0e01\u0e44\u0e14\u0e49\u0e27\u0e48\u0e32\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e21\u0e32\u0e08\u0e32\u0e01\u0e44\u0e2b\u0e19 ' +
      '\u0e19\u0e35\u0e48\u0e04\u0e37\u0e2d\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e17\u0e35\u0e48 EA \u0e2a\u0e48\u0e07 \u0e41\u0e25\u0e30\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e17\u0e35\u0e48\u0e21\u0e31\u0e19\u0e44\u0e21\u0e48\u0e41\u0e15\u0e30</p>' +
      '<div class="ea-cols">' +
        '<div class="ea-col yes"><h5>\u0e2a\u0e48\u0e07\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e2a\u0e34\u0e48\u0e07\u0e40\u0e2b\u0e25\u0e48\u0e32\u0e19\u0e35\u0e49</h5><ul>' +
          SEND.map(function(x){ return '<li>' + chk + '<span>' + x + '</span></li>'; }).join("") + '</ul></div>' +
        '<div class="ea-col no"><h5>\u0e44\u0e21\u0e48\u0e2a\u0e48\u0e07\u0e40\u0e14\u0e47\u0e14\u0e02\u0e32\u0e14</h5><ul>' +
          NO.map(function(x){ return '<li>' + xx + '<span>' + x + '</span></li>'; }).join("") + '</ul></div>' +
        '<div class="ea-col w"><h5>\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e44\u0e1b\u0e40\u0e1b\u0e47\u0e19\u0e04\u0e30\u0e41\u0e19\u0e19\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e44\u0e23</h5><ul>' +
          W.map(function(w){ return '<li style="display:block"><span class="ea-w">' +
            '<span class="nm">' + w[0] + '</span><span class="bar"><b style="width:' + (w[1] * 4) + '%"></b></span>' +
            '<span class="pc">' + w[1] + '%</span></span></li>'; }).join("") + '</ul></div>' +
      '</div>' +
      '<p class="ea-pnote"><b>\u0e40\u0e23\u0e32\u0e27\u0e31\u0e14\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e27\u0e31\u0e14\u0e1c\u0e25\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13</b> ' +
      '\u00b7 \u0e01\u0e32\u0e23\u0e15\u0e34\u0e14\u0e15\u0e31\u0e49\u0e07 EA \u0e44\u0e21\u0e48\u0e21\u0e35\u0e1c\u0e25\u0e15\u0e48\u0e2d\u0e14\u0e32\u0e27\u0e2b\u0e23\u0e37\u0e2d\u0e04\u0e30\u0e41\u0e19\u0e19\u0e02\u0e2d\u0e07\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e04\u0e38\u0e13\u0e43\u0e0a\u0e49 ' +
      '\u00b7 <b>\u0e2a\u0e48\u0e27\u0e19\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e40\u0e2a\u0e19\u0e2d\u0e02\u0e2d\u0e07 Noting \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e2d\u0e19\u0e38\u0e21\u0e31\u0e15\u0e34</b></p>';
  }
})();

/* \u2500\u2500 \u0e2a\u0e21\u0e31\u0e04\u0e23\u0e43\u0e19\u0e1a\u0e17\u0e1a\u0e32\u0e17\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c \u2500\u2500\u2500\u2500
   \u0e1f\u0e2d\u0e23\u0e4c\u0e21\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e15\u0e48\u0e2d\u0e23\u0e30\u0e1a\u0e1a\u0e08\u0e23\u0e34\u0e07 \u0e40\u0e0a\u0e48\u0e19\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e2b\u0e19\u0e49\u0e32\u0e2a\u0e21\u0e31\u0e04\u0e23\u0e40\u0e14\u0e34\u0e21             */
var BROKER_FLD =
  '<div class="su-bnote">' +
    '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#B54708" stroke-width="2" ' +
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink:0;margin-top:2px">' +
    '<circle cx="12" cy="12" r="9"></circle><path d="M12 7.6V13M12 16.2v.1"></path></svg>' +
    '<span><b>\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e15\u0e49\u0e2d\u0e07\u0e1c\u0e48\u0e32\u0e19\u0e01\u0e32\u0e23\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e15\u0e31\u0e27\u0e15\u0e19\u0e01\u0e48\u0e2d\u0e19</b> ' +
    '\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e08\u0e30\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e0a\u0e37\u0e48\u0e2d\u0e19\u0e34\u0e15\u0e34\u0e1a\u0e38\u0e04\u0e04\u0e25 \u0e40\u0e25\u0e02\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15 ' +
    '\u0e41\u0e25\u0e30\u0e42\u0e14\u0e40\u0e21\u0e19\u0e2d\u0e35\u0e40\u0e21\u0e25\u0e01\u0e31\u0e1a\u0e10\u0e32\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a ' +
    '\u0e43\u0e0a\u0e49\u0e40\u0e27\u0e25\u0e32\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 3\u20135 \u0e27\u0e31\u0e19\u0e17\u0e33\u0e01\u0e32\u0e23 ' +
    '\u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07\u0e23\u0e2d\u0e08\u0e30\u0e22\u0e31\u0e07\u0e15\u0e2d\u0e1a\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49</span></div>' +
  '<label class="fld"><span>\u0e0a\u0e37\u0e48\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e15\u0e32\u0e21\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19</span>' +
    '<input id="su-bname" type="text" placeholder="\u0e0a\u0e37\u0e48\u0e2d\u0e19\u0e34\u0e15\u0e34\u0e1a\u0e38\u0e04\u0e04\u0e25\u0e40\u0e15\u0e47\u0e21" autocomplete="off"></label>' +
  '<div class="fld-2">' +
    '<label class="fld"><span>\u0e40\u0e02\u0e15\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e01\u0e33\u0e01\u0e31\u0e1a</span>' +
      '<select id="su-breg" aria-label="\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e40\u0e02\u0e15\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e01\u0e33\u0e01\u0e31\u0e1a"></select></label>' +
    '<label class="fld"><span>\u0e40\u0e25\u0e02\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15</span>' +
      '<input id="su-blic" type="text" placeholder="\u0e40\u0e0a\u0e48\u0e19 123456" autocomplete="off"></label>' +
  '</div>' +
  '<div class="fld-2">' +
    '<label class="fld"><span>\u0e15\u0e33\u0e41\u0e2b\u0e19\u0e48\u0e07\u0e43\u0e19\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17</span>' +
      '<input id="su-brole" type="text" placeholder="\u0e40\u0e0a\u0e48\u0e19 Compliance Officer" autocomplete="off"></label>' +
    '<label class="fld"><span>\u0e2d\u0e35\u0e40\u0e21\u0e25\u0e42\u0e14\u0e40\u0e21\u0e19\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17</span>' +
      '<input id="su-bmail" type="email" placeholder="you@company.com" autocomplete="off"></label>' +
  '</div>';
var SU_REG = ["FCA (\u0e2a\u0e2b\u0e23\u0e32\u0e0a\u0e2d\u0e32\u0e13\u0e32\u0e08\u0e31\u0e01\u0e23)", "ASIC (\u0e2d\u0e2d\u0e2a\u0e40\u0e15\u0e23\u0e40\u0e25\u0e35\u0e22)",
  "CySEC (\u0e44\u0e0b\u0e1b\u0e23\u0e31\u0e2a)", "FSCA (\u0e41\u0e2d\u0e1f\u0e23\u0e34\u0e01\u0e32\u0e43\u0e15\u0e49)",
  "MAS (\u0e2a\u0e34\u0e07\u0e04\u0e42\u0e1b\u0e23\u0e4c)", "FSA \u0e0d\u0e35\u0e48\u0e1b\u0e38\u0e48\u0e19", "\u0e2d\u0e37\u0e48\u0e19 \u0e46"];
(function(){
  var pick = document.querySelector(".role-pick");
  var slot = document.getElementById("su-broker");
  if (!pick || !slot) { return; }
  slot.innerHTML = BROKER_FLD;
  var sel = document.getElementById("su-breg");
  if (sel) {
    sel.innerHTML = SU_REG.map(function(r){ return '<option>' + r + '</option>'; }).join("");
  }
  var SUB = {
    user: "\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e15\u0e34\u0e14\u0e15\u0e32\u0e21\u0e1c\u0e25\u0e15\u0e23\u0e27\u0e08 \u0e40\u0e01\u0e47\u0e1a\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e40\u0e17\u0e35\u0e22\u0e1a \u0e41\u0e25\u0e30\u0e22\u0e37\u0e48\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e44\u0e14\u0e49",
    broker: "\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e17\u0e35\u0e48\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e41\u0e08\u0e49\u0e07 \u0e41\u0e25\u0e30\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e1c\u0e48\u0e32\u0e19 Broker Dashboard"
  };
  var BTN = {user: "\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e1a\u0e31\u0e0d\u0e0a\u0e35",
             broker: "\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e02\u0e2d\u0e40\u0e1b\u0e34\u0e14\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19"};
  function setRole(r){
    pick.querySelectorAll("[data-role]").forEach(function(b){
      b.setAttribute("aria-checked", String(b.dataset.role === r));
    });
    slot.hidden = r !== "broker";
    var sub = document.getElementById("su-sub");
    if (sub) { sub.textContent = SUB[r]; }
    var peek = document.getElementById("su-peek");
    if (peek) { peek.hidden = r !== "broker"; }
    var btn = document.querySelector('[data-page="signup"] .auth-submit');
    if (btn) { btn.textContent = BTN[r]; }
    var side = document.querySelector('[data-page="signup"] .auth-side');
    if (side) { side.dataset.role = r; }
  }
  pick.addEventListener("click", function(ev){
    var b = ev.target.closest("[data-role]");
    if (b) { setRole(b.dataset.role); }
  });
  setRole("user");
})();

/* \u2500\u2500 Broker Dashboard \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
   \u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e25\u0e47\u0e2d\u0e01\u0e2d\u0e34\u0e19\u0e2d\u0e22\u0e39\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e0a\u0e37\u0e48\u0e2d\u0e2a\u0e21\u0e21\u0e15\u0e34 \u0e41\u0e25\u0e30\u0e40\u0e1b\u0e47\u0e19\u0e23\u0e32\u0e22\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e17\u0e35\u0e48\u0e21\u0e35\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e04\u0e49\u0e32\u0e07\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32 Broker Alerts
   \u0e2a\u0e2d\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e08\u0e36\u0e07\u0e40\u0e25\u0e48\u0e32\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19                                        */
var BD_ME = {n:"Vertex Bridge Markets", mono:"VB", reg:"FSA \u0e0d\u0e35\u0e48\u0e1b\u0e38\u0e48\u0e19 \u00b7 \u0e40\u0e25\u0e02\u0e17\u0e35\u0e48 20-118",
  who:"\u0e2a\u0e38\u0e23\u0e35\u0e22\u0e4c \u0e18\u0e19\u0e30\u0e27\u0e07\u0e28\u0e4c", pos:"Compliance Officer"};
var BD_KPI = [
  ["\u0e23\u0e2d\u0e04\u0e38\u0e13\u0e15\u0e2d\u0e1a", 3, null, "warn"],
  ["\u0e01\u0e33\u0e25\u0e31\u0e07\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a", 1, null, ""],
  ["\u0e1b\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e41\u0e25\u0e49\u0e27\u0e1b\u0e35\u0e19\u0e35\u0e49", 6, null, ""],
  ["\u0e40\u0e27\u0e25\u0e32\u0e15\u0e2d\u0e1a\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22", "9 \u0e27\u0e31\u0e19", 4, ""]
];
var BD_KIND = [
  "\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a \u0e01\u0e33\u0e25\u0e31\u0e07\u0e15\u0e23\u0e27\u0e08\u0e20\u0e32\u0e22\u0e43\u0e19",
  "\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e02\u0e49\u0e2d\u0e40\u0e17\u0e47\u0e08\u0e08\u0e23\u0e34\u0e07",
  "\u0e41\u0e01\u0e49\u0e44\u0e02\u0e40\u0e23\u0e35\u0e22\u0e1a\u0e23\u0e49\u0e2d\u0e22\u0e41\u0e25\u0e49\u0e27",
  "\u0e42\u0e15\u0e49\u0e41\u0e22\u0e49\u0e07\u0e02\u0e49\u0e2d\u0e01\u0e25\u0e48\u0e32\u0e27\u0e2b\u0e32",
  "\u0e02\u0e2d\u0e02\u0e22\u0e32\u0e22\u0e40\u0e27\u0e25\u0e32"
];
var BD_CASES = [
  {id:"RS-2026-0418", s:"md", st:"new", due:2, d:"21 \u0e1e.\u0e04. 2026", src:"\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08 RedStar",
   t:"\u0e22\u0e49\u0e32\u0e22\u0e40\u0e02\u0e15\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e01\u0e33\u0e01\u0e31\u0e1a 3 \u0e04\u0e23\u0e31\u0e49\u0e07\u0e43\u0e19 12 \u0e40\u0e14\u0e37\u0e2d\u0e19",
   x:"\u0e01\u0e32\u0e23\u0e22\u0e49\u0e32\u0e22\u0e40\u0e02\u0e15\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e44\u0e21\u0e48\u0e1c\u0e34\u0e14\u0e01\u0e0e\u0e2b\u0e21\u0e32\u0e22 \u0e41\u0e15\u0e48\u0e01\u0e32\u0e23\u0e22\u0e49\u0e32\u0e22\u0e16\u0e35\u0e48\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32<b>\u0e40\u0e07\u0e34\u0e19\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e21\u0e37\u0e2d\u0e1c\u0e39\u0e49\u0e14\u0e39\u0e41\u0e25\u0e2b\u0e25\u0e32\u0e22\u0e04\u0e23\u0e31\u0e49\u0e07\u0e43\u0e19\u0e40\u0e27\u0e25\u0e32\u0e2a\u0e31\u0e49\u0e19</b> \u0e0b\u0e36\u0e48\u0e07\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e15\u0e48\u0e2d\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e02\u0e2d\u0e07\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e01\u0e34\u0e14\u0e02\u0e49\u0e2d\u0e1e\u0e34\u0e1e\u0e32\u0e17",
   ev:["\u0e2a\u0e33\u0e40\u0e19\u0e32\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19 3 \u0e09\u0e1a\u0e31\u0e1a", "\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e1a\u0e19\u0e40\u0e27\u0e47\u0e1a 2 \u0e2b\u0e19\u0e49\u0e32", "\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e2a\u0e2d\u0e07\u0e09\u0e1a\u0e31\u0e1a"],
   tl:[["\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e40\u0e1b\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07", "21 \u0e1e.\u0e04. 2026 \u00b7 \u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08\u0e23\u0e2d\u0e1a\u0e1b\u0e23\u0e30\u0e08\u0e33\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a", "on"],
       ["\u0e2a\u0e48\u0e07\u0e2b\u0e19\u0e31\u0e07\u0e2a\u0e37\u0e2d\u0e16\u0e36\u0e07\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c", "23 \u0e1e.\u0e04. 2026 \u00b7 \u0e2a\u0e48\u0e07\u0e17\u0e35\u0e48\u0e2d\u0e35\u0e40\u0e21\u0e25\u0e17\u0e35\u0e48\u0e41\u0e08\u0e49\u0e07\u0e44\u0e27\u0e49\u0e01\u0e31\u0e1a\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a", "on"],
       ["\u0e23\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a", "\u0e04\u0e23\u0e1a\u0e01\u0e33\u0e2b\u0e19\u0e14 30 \u0e27\u0e31\u0e19 \u2014 \u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e2d\u0e35\u0e01 2 \u0e27\u0e31\u0e19", "now"],
       ["\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e23\u0e38\u0e1b\u0e41\u0e25\u0e30\u0e40\u0e1c\u0e22\u0e41\u0e1e\u0e23\u0e48", "\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e02\u0e36\u0e49\u0e19\u0e2b\u0e19\u0e49\u0e32 Broker Alerts \u0e04\u0e39\u0e48\u0e01\u0e31\u0e1a\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e40\u0e2a\u0e21\u0e2d", ""]]},

  {id:"RS-2026-0402", s:"hi", st:"new", due:6, d:"17 \u0e1e.\u0e04. 2026", src:"\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e41\u0e08\u0e49\u0e07 24 \u0e23\u0e32\u0e22",
   t:"\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e16\u0e2d\u0e19\u0e40\u0e01\u0e34\u0e19 72 \u0e0a\u0e31\u0e48\u0e27\u0e42\u0e21\u0e07 \u0e0a\u0e48\u0e27\u0e07\u0e2a\u0e34\u0e49\u0e19\u0e40\u0e14\u0e37\u0e2d\u0e19",
   x:"\u0e04\u0e33\u0e23\u0e49\u0e2d\u0e07 24 \u0e23\u0e32\u0e22\u0e43\u0e19 11 \u0e27\u0e31\u0e19 \u0e23\u0e30\u0e1a\u0e38\u0e15\u0e23\u0e07\u0e01\u0e31\u0e19\u0e27\u0e48\u0e32\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e16\u0e2d\u0e19\u0e04\u0e49\u0e32\u0e07\u0e19\u0e32\u0e19\u0e40\u0e01\u0e34\u0e19 72 \u0e0a\u0e31\u0e48\u0e27\u0e42\u0e21\u0e07 \u0e40\u0e09\u0e1e\u0e32\u0e30\u0e0a\u0e48\u0e27\u0e07\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 28\u201331 \u0e02\u0e2d\u0e07\u0e40\u0e14\u0e37\u0e2d\u0e19 \u0e42\u0e14\u0e22<b>\u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e41\u0e08\u0e49\u0e07\u0e25\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e08\u0e32\u0e01\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17</b>",
   ev:["\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e25\u0e02\u0e04\u0e33\u0e02\u0e2d\u0e16\u0e2d\u0e19 24 \u0e23\u0e32\u0e22", "\u0e20\u0e32\u0e1e\u0e08\u0e31\u0e1a\u0e2b\u0e19\u0e49\u0e32\u0e08\u0e2d 18 \u0e44\u0e1f\u0e25\u0e4c", "\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e08\u0e32\u0e01 Withdrawal Journal EA"],
   tl:[["\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e41\u0e08\u0e49\u0e07\u0e40\u0e02\u0e49\u0e32\u0e21\u0e32", "13\u201317 \u0e1e.\u0e04. 2026 \u00b7 24 \u0e23\u0e32\u0e22", "on"],
       ["\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e04\u0e31\u0e14\u0e01\u0e23\u0e2d\u0e07\u0e41\u0e25\u0e49\u0e27\u0e08\u0e31\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27", "17 \u0e1e.\u0e04. 2026 \u00b7 \u0e15\u0e31\u0e14\u0e23\u0e32\u0e22\u0e0b\u0e49\u0e33\u0e2d\u0e2d\u0e01 4 \u0e23\u0e32\u0e22", "on"],
       ["\u0e23\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a", "\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e2d\u0e35\u0e01 6 \u0e27\u0e31\u0e19", "now"],
       ["\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e23\u0e38\u0e1b\u0e41\u0e25\u0e30\u0e40\u0e1c\u0e22\u0e41\u0e1e\u0e23\u0e48", "\u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e15\u0e2d\u0e1a\u0e08\u0e30\u0e02\u0e36\u0e49\u0e19\u0e27\u0e48\u0e32 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e15\u0e2d\u0e1a\u0e01\u0e25\u0e31\u0e1a", ""]]},

  {id:"RS-2026-0377", s:"md", st:"new", due:11, d:"9 \u0e1e.\u0e04. 2026", src:"\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e08\u0e32\u0e01 EA",
   t:"\u0e2a\u0e40\u0e1b\u0e23\u0e14\u0e08\u0e23\u0e34\u0e07\u0e01\u0e27\u0e49\u0e32\u0e07\u0e01\u0e27\u0e48\u0e32\u0e17\u0e35\u0e48\u0e42\u0e06\u0e29\u0e13\u0e32 2.4 \u0e40\u0e17\u0e48\u0e32",
   x:"\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e27\u0e47\u0e1a\u0e42\u0e06\u0e29\u0e13\u0e32\u0e2a\u0e40\u0e1b\u0e23\u0e14 EURUSD \u0e40\u0e23\u0e34\u0e48\u0e21\u0e17\u0e35\u0e48 0.4 pip \u0e41\u0e15\u0e48\u0e04\u0e48\u0e32\u0e21\u0e31\u0e18\u0e22\u0e10\u0e32\u0e19\u0e08\u0e32\u0e01\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e08\u0e23\u0e34\u0e07 <b>412 \u0e1a\u0e31\u0e0d\u0e0a\u0e35</b> \u0e2d\u0e22\u0e39\u0e48\u0e17\u0e35\u0e48 0.96 pip \u0e15\u0e25\u0e2d\u0e14\u0e0a\u0e48\u0e27\u0e07\u0e15\u0e25\u0e32\u0e14\u0e25\u0e2d\u0e19\u0e14\u0e2d\u0e19",
   ev:["\u0e01\u0e25\u0e38\u0e48\u0e21\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07 412 \u0e1a\u0e31\u0e0d\u0e0a\u0e35", "\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e01\u0e47\u0e1a 30 \u0e27\u0e31\u0e19", "\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e2b\u0e19\u0e49\u0e32\u0e42\u0e06\u0e29\u0e13\u0e32\u0e09\u0e1a\u0e31\u0e1a 12 \u0e21\u0e35.\u0e04."],
   tl:[["EA \u0e2a\u0e48\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e40\u0e02\u0e49\u0e32\u0e23\u0e30\u0e1a\u0e1a", "\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07 \u00b7 \u0e44\u0e21\u0e48\u0e23\u0e30\u0e1a\u0e38\u0e15\u0e31\u0e27\u0e15\u0e19\u0e1c\u0e39\u0e49\u0e2a\u0e48\u0e07", "on"],
       ["\u0e23\u0e30\u0e1a\u0e1a\u0e15\u0e31\u0e49\u0e07\u0e18\u0e07\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34", "9 \u0e1e.\u0e04. 2026 \u00b7 \u0e40\u0e01\u0e34\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07 2 \u0e40\u0e17\u0e48\u0e32", "on"],
       ["\u0e23\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a", "\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e2d\u0e35\u0e01 11 \u0e27\u0e31\u0e19", "now"],
       ["\u0e2d\u0e31\u0e1b\u0e40\u0e14\u0e15\u0e2b\u0e19\u0e49\u0e32\u0e42\u0e06\u0e29\u0e13\u0e32\u0e2b\u0e23\u0e37\u0e2d\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07", "\u0e2b\u0e32\u0e01\u0e40\u0e1b\u0e47\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e02\u0e48\u0e32\u0e27\u0e0a\u0e31\u0e48\u0e27\u0e04\u0e23\u0e32\u0e27 \u0e41\u0e19\u0e1a\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e44\u0e14\u0e49", ""]]},

  {id:"RS-2026-0344", s:"md", st:"sent", due:null, d:"28 \u0e21\u0e35.\u0e04. 2026", src:"\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08 RedStar",
   t:"\u0e2b\u0e19\u0e49\u0e32\u0e42\u0e1b\u0e23\u0e42\u0e21\u0e0a\u0e31\u0e48\u0e19\u0e44\u0e21\u0e48\u0e23\u0e30\u0e1a\u0e38\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e01\u0e32\u0e23\u0e16\u0e2d\u0e19",
   x:"\u0e2b\u0e19\u0e49\u0e32\u0e42\u0e1b\u0e23\u0e42\u0e21\u0e0a\u0e31\u0e48\u0e19\u0e42\u0e1a\u0e19\u0e31\u0e2a 30% \u0e44\u0e21\u0e48\u0e23\u0e30\u0e1a\u0e38\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e01\u0e48\u0e2d\u0e19\u0e16\u0e2d\u0e19 \u0e15\u0e49\u0e2d\u0e07\u0e01\u0e14\u0e40\u0e02\u0e49\u0e32\u0e2d\u0e35\u0e01\u0e2a\u0e2d\u0e07\u0e0a\u0e31\u0e49\u0e19\u0e08\u0e36\u0e07\u0e08\u0e30\u0e40\u0e2b\u0e47\u0e19",
   ev:["\u0e20\u0e32\u0e1e\u0e2b\u0e19\u0e49\u0e32\u0e42\u0e1b\u0e23\u0e42\u0e21\u0e0a\u0e31\u0e48\u0e19", "\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e09\u0e1a\u0e31\u0e1a\u0e40\u0e15\u0e47\u0e21"],
   rp:{k:"\u0e41\u0e01\u0e49\u0e44\u0e02\u0e40\u0e23\u0e35\u0e22\u0e1a\u0e23\u0e49\u0e2d\u0e22\u0e41\u0e25\u0e49\u0e27", d:"2 \u0e21\u0e34.\u0e22. 2026",
       p:"\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e22\u0e49\u0e32\u0e22\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e21\u0e32\u0e44\u0e27\u0e49\u0e43\u0e15\u0e49\u0e1b\u0e38\u0e48\u0e21\u0e23\u0e31\u0e1a\u0e42\u0e1a\u0e19\u0e31\u0e2a\u0e42\u0e14\u0e22\u0e15\u0e23\u0e07 \u0e41\u0e25\u0e30\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e44\u0e27\u0e49\u0e43\u0e15\u0e49\u0e1b\u0e38\u0e48\u0e21\u0e41\u0e25\u0e49\u0e27 \u0e21\u0e35\u0e1c\u0e25\u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48 1 \u0e21\u0e34.\u0e22."},
   tl:[["\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e40\u0e1b\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07", "28 \u0e21\u0e35.\u0e04. 2026", "on"],
       ["\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e01\u0e14\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a", "29 \u0e21\u0e35.\u0e04. 2026 \u00b7 \u0e42\u0e14\u0e22 \u0e2a\u0e38\u0e23\u0e35\u0e22\u0e4c \u0e18\u0e19\u0e30\u0e27\u0e07\u0e28\u0e4c", "on"],
       ["\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e41\u0e25\u0e49\u0e27", "2 \u0e21\u0e34.\u0e22. 2026 \u00b7 \u0e41\u0e19\u0e1a\u0e20\u0e32\u0e1e\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e27\u0e47\u0e1a\u0e17\u0e35\u0e48\u0e41\u0e01\u0e49\u0e41\u0e25\u0e49\u0e27 2 \u0e44\u0e1f\u0e25\u0e4c", "on"],
       ["\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e01\u0e33\u0e25\u0e31\u0e07\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a", "\u0e04\u0e32\u0e14\u0e27\u0e48\u0e32\u0e23\u0e39\u0e49\u0e1c\u0e25\u0e20\u0e32\u0e22\u0e43\u0e19 7 \u0e27\u0e31\u0e19", "now"]]},

  {id:"RS-2026-0290", s:"hi", st:"done", due:null, d:"14 \u0e21\u0e35.\u0e04. 2026", src:"\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e41\u0e08\u0e49\u0e07 7 \u0e23\u0e32\u0e22",
   t:"\u0e04\u0e34\u0e14\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e1b\u0e34\u0e14\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e08\u0e49\u0e07\u0e25\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e49\u0e32",
   x:"\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e16\u0e39\u0e01\u0e2b\u0e31\u0e01\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e1b\u0e34\u0e14\u0e1a\u0e31\u0e0d\u0e0a\u0e35 $50 \u0e42\u0e14\u0e22\u0e17\u0e35\u0e48\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e1b\u0e23\u0e32\u0e01\u0e0f\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e32\u0e23\u0e32\u0e07\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21",
   ev:["\u0e2a\u0e33\u0e40\u0e19\u0e32\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e32\u0e23\u0e32\u0e07\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21", "\u0e2a\u0e40\u0e15\u0e15\u0e40\u0e21\u0e19\u0e15\u0e4c\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49 7 \u0e23\u0e32\u0e22"],
   rp:{k:"\u0e41\u0e01\u0e49\u0e44\u0e02\u0e40\u0e23\u0e35\u0e22\u0e1a\u0e23\u0e49\u0e2d\u0e22\u0e41\u0e25\u0e49\u0e27", d:"19 \u0e21\u0e35.\u0e04. 2026",
       p:"\u0e40\u0e1b\u0e47\u0e19\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e17\u0e35\u0e48\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e02\u0e49\u0e32\u0e21\u0e32\u0e42\u0e14\u0e22\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e2d\u0e31\u0e1b\u0e40\u0e14\u0e15\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e32\u0e23\u0e32\u0e07 \u0e04\u0e37\u0e19\u0e40\u0e07\u0e34\u0e19\u0e04\u0e23\u0e1a\u0e17\u0e31\u0e49\u0e07 7 \u0e23\u0e32\u0e22\u0e41\u0e25\u0e49\u0e27 \u0e41\u0e25\u0e30\u0e41\u0e01\u0e49\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e32\u0e23\u0e32\u0e07\u0e40\u0e21\u0e37\u0e48\u0e2d 18 \u0e21\u0e35.\u0e04."},
   tl:[["\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e41\u0e08\u0e49\u0e07\u0e40\u0e02\u0e49\u0e32\u0e21\u0e32", "14 \u0e21\u0e35.\u0e04. 2026", "on"],
       ["\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e01\u0e14\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a", "15 \u0e21\u0e35.\u0e04. 2026", "on"],
       ["\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e41\u0e25\u0e30\u0e04\u0e37\u0e19\u0e40\u0e07\u0e34\u0e19", "19 \u0e21\u0e35.\u0e04. 2026", "on"],
       ["\u0e1b\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07", "24 \u0e21\u0e35.\u0e04. 2026 \u00b7 \u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e27\u0e49\u0e43\u0e19\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e16\u0e32\u0e27\u0e23", "on"]]}
];
var BD_RULES = [
  ["\u0e01\u0e32\u0e23\u0e15\u0e2d\u0e1a\u0e44\u0e21\u0e48\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e14\u0e32\u0e27\u0e2b\u0e23\u0e37\u0e2d\u0e04\u0e30\u0e41\u0e19\u0e19\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19",
   "\u0e14\u0e32\u0e27\u0e21\u0e32\u0e08\u0e32\u0e01\u0e40\u0e01\u0e13\u0e11\u0e4c GCSI \u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19 \u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e17\u0e35\u0e48\u0e14\u0e35\u0e44\u0e21\u0e48\u0e0a\u0e48\u0e27\u0e22\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e14\u0e32\u0e27 \u0e41\u0e25\u0e30\u0e40\u0e23\u0e32\u0e44\u0e21\u0e48\u0e23\u0e31\u0e1a\u0e04\u0e33\u0e02\u0e2d\u0e43\u0e2b\u0e49\u0e25\u0e1a\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07"],
  ["\u0e04\u0e33\u0e15\u0e2d\u0e1a\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e08\u0e30\u0e02\u0e36\u0e49\u0e19\u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e30",
   "\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e07\u0e08\u0e30\u0e41\u0e2a\u0e14\u0e07\u0e04\u0e39\u0e48\u0e01\u0e31\u0e1a\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e1a\u0e19\u0e2b\u0e19\u0e49\u0e32 Broker Alerts \u0e40\u0e2a\u0e21\u0e2d \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e0a\u0e37\u0e48\u0e2d\u0e15\u0e33\u0e41\u0e2b\u0e19\u0e48\u0e07\u0e1c\u0e39\u0e49\u0e15\u0e2d\u0e1a\u0e41\u0e25\u0e30\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48"],
  ["\u0e44\u0e21\u0e48\u0e15\u0e2d\u0e1a\u0e01\u0e47\u0e02\u0e36\u0e49\u0e19\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19",
   "\u0e04\u0e23\u0e1a\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e41\u0e25\u0e49\u0e27\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e08\u0e30\u0e02\u0e36\u0e49\u0e19\u0e2a\u0e16\u0e32\u0e19\u0e30 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e15\u0e2d\u0e1a\u0e01\u0e25\u0e31\u0e1a \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e43\u0e2b\u0e49\u0e04\u0e19\u0e2d\u0e48\u0e32\u0e19\u0e23\u0e39\u0e49\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e34\u0e14\u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e43\u0e2b\u0e49\u0e41\u0e25\u0e49\u0e27"],
  ["\u0e2b\u0e49\u0e32\u0e21\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e1c\u0e39\u0e49\u0e41\u0e08\u0e49\u0e07\u0e42\u0e14\u0e22\u0e15\u0e23\u0e07",
   "\u0e40\u0e23\u0e32\u0e44\u0e21\u0e48\u0e40\u0e1b\u0e34\u0e14\u0e40\u0e1c\u0e22\u0e15\u0e31\u0e27\u0e15\u0e19\u0e1c\u0e39\u0e49\u0e41\u0e08\u0e49\u0e07\u0e43\u0e2b\u0e49\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c \u0e01\u0e32\u0e23\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e17\u0e38\u0e01\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e15\u0e49\u0e2d\u0e07\u0e1c\u0e48\u0e32\u0e19\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08"],
  ["\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e40\u0e17\u0e47\u0e08\u0e21\u0e35\u0e1c\u0e25\u0e15\u0e48\u0e2d\u0e04\u0e30\u0e41\u0e19\u0e19\u0e04\u0e27\u0e32\u0e21\u0e42\u0e1b\u0e23\u0e48\u0e07\u0e43\u0e2a",
   "\u0e16\u0e49\u0e32\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e02\u0e31\u0e14\u0e01\u0e31\u0e1a\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e17\u0e35\u0e48\u0e15\u0e23\u0e27\u0e08\u0e44\u0e14\u0e49 \u0e08\u0e30\u0e16\u0e39\u0e01\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e27\u0e49\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14\u0e04\u0e27\u0e32\u0e21\u0e42\u0e1b\u0e23\u0e48\u0e07\u0e43\u0e2a\u0e02\u0e2d\u0e07 GCSI"],
  ["\u0e17\u0e38\u0e01\u0e01\u0e32\u0e23\u0e01\u0e23\u0e30\u0e17\u0e33\u0e16\u0e39\u0e01\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01",
   "\u0e01\u0e32\u0e23\u0e01\u0e14\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a \u0e01\u0e32\u0e23\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07 \u0e41\u0e25\u0e30\u0e40\u0e27\u0e25\u0e32\u0e17\u0e35\u0e48\u0e17\u0e33 \u0e08\u0e30\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e16\u0e32\u0e27\u0e23 \u0e41\u0e01\u0e49\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49"]
];
var BD_PILL = {new:["new", "\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e01\u0e14\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a"],
  ack:["ack", "\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a\u0e41\u0e25\u0e49\u0e27 \u0e23\u0e2d\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07"],
  sent:["sent", "\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e41\u0e25\u0e49\u0e27"],
  done:["done", "\u0e1b\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e41\u0e25\u0e49\u0e27"]};
function bdSev(s){
  return '<span class="bd-sev ' + s + '"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" ' +
    'stroke="' + (s === "hi" ? "#D92D20" : "#B54708") + '" stroke-width="2" stroke-linecap="round" ' +
    'stroke-linejoin="round" aria-hidden="true"><path d="M12 3.6 21 19.4H3z"></path>' +
    '<path d="M12 10v3.6M12 16.4v.1"></path></svg></span>';
}
function bdCase(c, i){
  var p = BD_PILL[c.st], act = c.st === "new" || c.st === "ack";
  var h = '<article class="bd-case' + (act ? " act" : "") + '" data-bdcase="' + i + '">' +
    '<div class="bd-chead">' + bdSev(c.s) +
      '<span class="bd-ct"><h3>' + c.t + '</h3>' +
      '<span class="bd-cmeta"><code>' + c.id + '</code><span>\u00b7</span><span>' + c.src +
      '</span><span>\u00b7</span><span>\u0e41\u0e08\u0e49\u0e07 ' + c.d + '</span></span></span>' +
      '<span class="bd-pill ' + p[0] + '" id="bd-pill-' + i + '">' + p[1] + '</span></div>' +
    '<div class="bd-cbody">' + c.x +
      '<div class="bd-ev">' + c.ev.map(function(e){
        return '<span>\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19: ' + e + '</span>'; }).join("") + '</div></div>' +
    '<div class="bd-tl" id="bd-tl-' + i + '"><h4>\u0e25\u0e33\u0e14\u0e31\u0e1a\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07</h4>' +
      c.tl.map(function(t){
        return '<div class="bd-step ' + t[2] + '"><b>' + t[0] + '</b><span>' + t[1] + '</span></div>';
      }).join("") + '</div>';
  if (c.rp) {
    h += '<div class="bd-tl" style="padding-top:0"><h4>\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e07\u0e44\u0e1b\u0e41\u0e25\u0e49\u0e27</h4>' +
      '<div class="al-reply" style="margin:0"><div class="who"><b>' + BD_ME.n + '</b>' +
      '<span class="tag">' + c.rp.k + '</span><span>' + c.rp.d + '</span></div>' +
      '<p>' + c.rp.p + '</p></div></div>';
  }
  if (act) {
    h += '<div class="bd-act"><h4>\u0e15\u0e2d\u0e1a\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e19\u0e35\u0e49</h4>' +
      '<div class="bd-kinds" role="group" aria-label="\u0e1b\u0e23\u0e30\u0e40\u0e20\u0e17\u0e01\u0e32\u0e23\u0e15\u0e2d\u0e1a">' +
      BD_KIND.map(function(k, j){
        return '<button type="button" class="bd-kind" data-bdkind="' + i + ':' + j + '" ' +
          'aria-pressed="' + (j === 0 ? "true" : "false") + '">' + k + '</button>';
      }).join("") + '</div>' +
      '<textarea class="bd-ta" id="bd-ta-' + i + '" autocomplete="off" ' +
      'placeholder="\u0e40\u0e02\u0e35\u0e22\u0e19\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e2a\u0e31\u0e49\u0e19 \u0e46 \u0e2d\u0e49\u0e32\u0e07\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e17\u0e35\u0e48\u0e41\u0e19\u0e1a\u0e21\u0e32\u0e14\u0e49\u0e27\u0e22"></textarea>' +
      '<div class="bd-arow">' +
        '<button type="button" class="bd-file" data-bdfile="' + i + '">' +
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
        '<path d="M12 5v14M5 12h14"></path></svg>\u0e41\u0e19\u0e1a\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19 (PDF \u0e2b\u0e23\u0e37\u0e2d\u0e20\u0e32\u0e1e)</button>' +
        '<button type="button" class="bd-ackb" data-bdack="' + i + '"' +
        (c.st === "ack" ? " disabled" : "") + '>' +
        (c.st === "ack" ? "\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a\u0e41\u0e25\u0e49\u0e27" : "\u0e01\u0e14\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e19\u0e35\u0e49") + '</button>' +
        '<button type="button" class="btn-solid bd-send" data-bdsend="' + i + '">' +
        '\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07</button>' +
      '</div>' +
      '<p class="bd-hint"><b>\u0e01\u0e14\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a\u0e01\u0e48\u0e2d\u0e19\u0e44\u0e14\u0e49 \u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e2d\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e1e\u0e23\u0e49\u0e2d\u0e21</b> \u2014 ' +
      '\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a\u0e08\u0e30\u0e02\u0e36\u0e49\u0e19\u0e2a\u0e16\u0e32\u0e19\u0e30\u0e17\u0e31\u0e19\u0e17\u0e35 ' +
      '\u0e41\u0e25\u0e30\u0e19\u0e31\u0e1a\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e27\u0e25\u0e32\u0e15\u0e2d\u0e1a\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13</p></div>';
  }
  return h + '</article>';
}
(function(){
  var top = document.getElementById("bd-top");
  if (!top) { return; }
  top.className = "bd-top";
  top.innerHTML =
    '<span class="bd-logo">' + BD_ME.mono + '</span>' +
    '<span class="bd-id"><h3>' + BD_ME.n + '</h3><span class="row">' +
      '<span class="bd-vf"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#067647" ' +
      'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="M4.5 12.5 10 18 19.5 6.5"></path></svg>\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e15\u0e31\u0e27\u0e15\u0e19\u0e41\u0e25\u0e49\u0e27</span>' +
      '<span>' + BD_ME.reg + '</span></span></span>' +
    '<span class="bd-who">\u0e40\u0e02\u0e49\u0e32\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19\u0e43\u0e19\u0e19\u0e32\u0e21<b>' + BD_ME.who + '</b>' +
      BD_ME.pos + '<br><button type="button" class="bd-out">\u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e23\u0e30\u0e1a\u0e1a</button></span>';

  var due = document.getElementById("bd-due");
  if (due) {
    due.className = "bd-due";
    due.innerHTML =
      '<span class="ic"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#D92D20" ' +
      'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5.4l3.4 2"></path></svg></span>' +
      '<span><b>\u0e21\u0e35 1 \u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e43\u0e01\u0e25\u0e49\u0e04\u0e23\u0e1a\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e15\u0e2d\u0e1a</b>' +
      '<p>' + BD_CASES[0].id + ' \u00b7 ' + BD_CASES[0].t +
      ' \u2014 \u0e16\u0e49\u0e32\u0e40\u0e25\u0e22\u0e01\u0e33\u0e2b\u0e19\u0e14 \u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e08\u0e30\u0e02\u0e36\u0e49\u0e19\u0e2b\u0e19\u0e49\u0e32 Broker Alerts \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e2b\u0e15\u0e38\u0e27\u0e48\u0e32<b> \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e15\u0e2d\u0e1a\u0e01\u0e25\u0e31\u0e1a</b></p></span>' +
      '<span class="cd"><em>2</em><span>\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e40\u0e2b\u0e25\u0e37\u0e2d</span></span>';
  }

  var kpi = document.getElementById("bd-kpi");
  if (kpi) {
    kpi.className = "bd-kpi";
    kpi.innerHTML = BD_KPI.map(function(k){
      var cmp = "";
      if (k[0].indexOf("\u0e40\u0e27\u0e25\u0e32") === 0) {
        cmp = '\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14 <b>4 \u0e27\u0e31\u0e19</b><br>' +
          '\u0e42\u0e1a\u0e23\u0e01\u0e04\u0e38\u0e13 <b class="up">\u0e0a\u0e49\u0e32\u0e01\u0e27\u0e48\u0e32 125%</b>';
      } else if (k[3] === "warn") {
        cmp = '\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e43\u0e01\u0e25\u0e49\u0e04\u0e23\u0e1a\u0e01\u0e33\u0e2b\u0e19\u0e14<br>' +
          '<b class="up">\u0e40\u0e2b\u0e25\u0e37\u0e2d 2 \u0e27\u0e31\u0e19</b>';
      } else if (k[0].indexOf("\u0e1b\u0e34\u0e14") === 0) {
        cmp = '\u0e15\u0e2d\u0e1a\u0e04\u0e23\u0e1a\u0e17\u0e38\u0e01\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07<br><b class="dn">\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e40\u0e01\u0e34\u0e19\u0e01\u0e33\u0e2b\u0e19\u0e14</b>';
      } else {
        cmp = '\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e01\u0e33\u0e25\u0e31\u0e07\u0e2a\u0e2d\u0e1a\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07<br>\u0e20\u0e32\u0e22\u0e43\u0e19 7 \u0e27\u0e31\u0e19';
      }
      return '<div class="bd-k"><span class="lb">' + k[0] + '</span>' +
        '<span class="vl' + (k[3] ? " " + k[3] : "") + '">' + k[1] + '</span>' +
        '<span class="cmp">' + cmp + '</span></div>';
    }).join("");
  }

  var host = document.getElementById("bd-cases");
  if (host) { host.innerHTML = BD_CASES.map(bdCase).join(""); }

  var rl = document.getElementById("bd-rules");
  if (rl) {
    rl.className = "bd-rules";
    rl.innerHTML = '<h4>\u0e01\u0e15\u0e34\u0e01\u0e32\u0e02\u0e2d\u0e07 Broker Dashboard</h4>' +
      '<p>\u0e2d\u0e48\u0e32\u0e19\u0e43\u0e2b\u0e49\u0e04\u0e23\u0e1a\u0e01\u0e48\u0e2d\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 \u2014 \u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e40\u0e2b\u0e25\u0e48\u0e32\u0e19\u0e35\u0e49\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e02\u0e49\u0e2d\u0e15\u0e01\u0e25\u0e07\u0e17\u0e35\u0e48\u0e04\u0e38\u0e13\u0e22\u0e2d\u0e21\u0e23\u0e31\u0e1a\u0e15\u0e2d\u0e19\u0e40\u0e1b\u0e34\u0e14\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19</p>' +
      '<div class="bd-rl">' + BD_RULES.map(function(r){
        return '<div><b>' + r[0] + '</b><span>' + r[1] + '</span></div>';
      }).join("") + '</div>';
  }

  var cta = document.getElementById("al-cta");
  if (cta) {
    cta.className = "al-cta";
    cta.innerHTML =
      '<span class="tx"><b>\u0e04\u0e38\u0e13\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e02\u0e2d\u0e07\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e17\u0e35\u0e48\u0e16\u0e39\u0e01\u0e41\u0e08\u0e49\u0e07\u0e43\u0e0a\u0e48\u0e44\u0e2b\u0e21</b>' +
      '<span>\u0e2a\u0e21\u0e31\u0e04\u0e23\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e41\u0e25\u0e30\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e15\u0e31\u0e27\u0e15\u0e19 \u0e41\u0e25\u0e49\u0e27\u0e15\u0e2d\u0e1a\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e44\u0e14\u0e49\u0e17\u0e35\u0e48 Broker Dashboard ' +
      '\u00b7 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e04\u0e48\u0e32\u0e43\u0e0a\u0e49\u0e08\u0e48\u0e32\u0e22 \u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e21\u0e35\u0e1c\u0e25\u0e15\u0e48\u0e2d\u0e14\u0e32\u0e27\u0e2b\u0e23\u0e37\u0e2d\u0e04\u0e30\u0e41\u0e19\u0e19</span></span>' +
      '<span class="bt"><a class="btn-solid" href="#/brokerdash">\u0e40\u0e02\u0e49\u0e32\u0e2a\u0e39\u0e48 Broker Dashboard</a>' +
      '<a class="btn-ghost" href="#/signup">\u0e2a\u0e21\u0e31\u0e04\u0e23\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19</a></span>';
  }
})();
document.addEventListener("click", function(ev){
  var k = ev.target.closest("[data-bdkind]");
  if (k) {
    var pr = k.dataset.bdkind.split(":")[0];
    document.querySelectorAll('[data-bdkind^="' + pr + ':"]').forEach(function(b){
      b.setAttribute("aria-pressed", String(b === k));
    });
    return;
  }
  var a = ev.target.closest("[data-bdack]");
  if (a) {
    var i = parseInt(a.dataset.bdack, 10), pill = document.getElementById("bd-pill-" + i);
    if (pill) { pill.className = "bd-pill ack"; pill.textContent = BD_PILL.ack[1]; }
    a.disabled = true;
    a.textContent = "\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a\u0e41\u0e25\u0e49\u0e27";
    var tl = document.getElementById("bd-tl-" + i);
    if (tl) {
      var now = tl.querySelector(".bd-step.now");
      if (now) {
        now.className = "bd-step on";
        now.querySelector("span").textContent =
          "\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a\u0e41\u0e25\u0e49\u0e27\u0e42\u0e14\u0e22 " + BD_ME.who +
          " \u00b7 \u0e22\u0e31\u0e07\u0e15\u0e49\u0e2d\u0e07\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e20\u0e32\u0e22\u0e43\u0e19\u0e01\u0e33\u0e2b\u0e19\u0e14";
      }
    }
    return;
  }
  var s = ev.target.closest("[data-bdsend]");
  if (s) {
    alert("\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a " +
      "\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e48\u0e2d\u0e23\u0e30\u0e1a\u0e1a\u0e08\u0e23\u0e34\u0e07 \u2014 " +
      "\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e17\u0e35\u0e48\u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e08\u0e30\u0e44\u0e21\u0e48\u0e16\u0e39\u0e01\u0e2a\u0e48\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e08\u0e31\u0e14\u0e40\u0e01\u0e47\u0e1a\u0e17\u0e35\u0e48\u0e43\u0e14");
    return;
  }
  var f = ev.target.closest("[data-bdfile]");
  if (f) {
    alert("\u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e23\u0e31\u0e1a\u0e44\u0e1f\u0e25\u0e4c \u2014 " +
      "\u0e2a\u0e48\u0e27\u0e19\u0e19\u0e35\u0e49\u0e41\u0e2a\u0e14\u0e07\u0e44\u0e27\u0e49\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e43\u0e2b\u0e49\u0e40\u0e2b\u0e47\u0e19\u0e15\u0e33\u0e41\u0e2b\u0e19\u0e48\u0e07\u0e02\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e41\u0e19\u0e1a\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19");
  }
});

/* \u2550\u2550 RedStar Awards \u2014 \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550
   \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e21\u0e21\u0e15\u0e34 \u0e15\u0e32\u0e21\u0e01\u0e0e\u0e02\u0e49\u0e2d 9 \u0e02\u0e2d\u0e07 CLAUDE.md   */
var AW_YEAR = 2026;
var AW_Q = 2;                       /* \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14\u0e17\u0e35\u0e48\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e1c\u0e25\u0e41\u0e25\u0e49\u0e27 */
var AW_STMAX = 3;                   /* \u0e14\u0e32\u0e27\u0e21\u0e35\u0e41\u0e04\u0e48 3 \u0e14\u0e27\u0e07 \u0e40\u0e17\u0e48\u0e32\u0e01\u0e31\u0e1a\u0e17\u0e31\u0e49\u0e07\u0e40\u0e27\u0e47\u0e1a */
var AW_PERIOD = "Q" + AW_Q + " " + AW_YEAR;
var AW_NEXT = "Q3 2026 \u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28 15 \u0e15.\u0e04. 2026";
var AW_NAME = "RED STAR";
var AW_SUB = "\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e17\u0e23\u0e07\u0e04\u0e38\u0e13\u0e04\u0e48\u0e32";
var AW_CATS = [
  {k:"fx", n:"Forex / CFD",
   d:"\u0e42\u0e1a\u0e23\u0e01\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e41\u0e25\u0e01\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e25\u0e30\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07",
   n2:24, ic:'<path d="M4 17.5 9 11l4 3 7-8.5"></path><path d="M15.5 5.5H20v4.5"></path>'},
  {k:"futures", n:"\u0e1f\u0e34\u0e27\u0e40\u0e08\u0e2d\u0e23\u0e4c\u0e2a",
   d:"\u0e42\u0e1a\u0e23\u0e01\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e25\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e43\u0e19\u0e15\u0e25\u0e32\u0e14\u0e01\u0e25\u0e32\u0e07",
   n2:18, ic:'<path d="M12 3v18M5 7.5 12 3l7 4.5"></path>'},
  {k:"stocks", n:"\u0e2b\u0e38\u0e49\u0e19",
   d:"\u0e42\u0e1a\u0e23\u0e01\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e48\u0e32\u0e07\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28",
   n2:22, ic:'<path d="M4 19V9M9.5 19V5M15 19v-7M20.5 19V8"></path>'},
  {k:"crypto", n:"\u0e04\u0e23\u0e34\u0e1b\u0e42\u0e15 (CFD)",
   d:"\u0e42\u0e1a\u0e23\u0e01\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e04\u0e23\u0e34\u0e1b\u0e42\u0e15",
   n2:16, ic:'<circle cx="12" cy="12" r="8.5"></circle><path d="M9.5 8.5h4.2a2.6 2.6 0 0 1 0 5.2H9.5zM9.5 13.7h4.6a2.6 2.6 0 0 1 0 5.2H9.5zM9.5 8.5v10.4M11.5 6v2.5M14 6v2.5M11.5 18.9v2.4M14 18.9v2.4"></path>'},
  {k:"exchange", n:"Exchange",
   d:"\u0e01\u0e23\u0e30\u0e14\u0e32\u0e19\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e40\u0e2b\u0e23\u0e35\u0e22\u0e0d\u0e08\u0e23\u0e34\u0e07 \u0e16\u0e37\u0e2d\u0e04\u0e23\u0e2d\u0e07\u0e2a\u0e34\u0e19\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e4c\u0e40\u0e2d\u0e07",
   n2:20, ic:'<path d="M4 8h12l-3-3M20 16H8l3 3"></path>'},
  {k:"fund", n:"\u0e01\u0e2d\u0e07\u0e17\u0e38\u0e19",
   d:"\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e02\u0e32\u0e22\u0e41\u0e25\u0e30\u0e41\u0e1e\u0e25\u0e15\u0e1f\u0e2d\u0e23\u0e4c\u0e21\u0e01\u0e2d\u0e07\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21",
   n2:14, ic:'<path d="M3.5 20.5h17M5 20.5V9l7-4.5L19 9v11.5"></path><path d="M9.5 20.5v-5h5v5"></path>'}
];
var AW_WIN = [
  {id:"RS-2026Q2-000128", b:"icm", cat:"fx", st:3, sc:96.4, rg:"apac", lic:"ASIC"},
  {id:"RS-2026Q2-000131", b:"pep", cat:"fx", st:3, sc:95.8, rg:"apac", lic:"ASIC"},
  {id:"RS-2026Q2-000137", b:"ig", cat:"fx", st:3, sc:95.1, rg:"emea", lic:"FCA"},
  {id:"RS-2026Q2-000142", b:"saxo", cat:"stocks", st:3, sc:94.7, rg:"emea", lic:"FSA-DK"},
  {id:"RS-2026Q2-000148", b:"ibkr", cat:"stocks", st:3, sc:94.2, rg:"amer", lic:"SEC"},
  {id:"RS-2026Q2-000155", b:"cmc", cat:"futures", st:2, sc:93.6, rg:"emea", lic:"FCA"},
  {id:"RS-2026Q2-000161", b:"vantage", cat:"fx", st:2, sc:93.1, rg:"apac", lic:"ASIC"},
  {id:"RS-2026Q2-000166", b:"fxpro", cat:"crypto", st:2, sc:92.5, rg:"emea", lic:"CySEC"},
  {id:"RS-2026Q2-000172", b:"exness", cat:"fx", st:2, sc:92.0, rg:"apac", lic:"FSA-SC"},
  {id:"RS-2026Q2-000178", b:"tickmill", cat:"futures", st:2, sc:91.4, rg:"emea", lic:"FCA"},
  {id:"RS-2026Q2-000184", b:"axi", cat:"exchange", st:1, sc:90.8, rg:"apac", lic:"ASIC"},
  {id:"RS-2026Q2-000190", b:"capital", cat:"fund", st:1, sc:90.2, rg:"emea", lic:"CySEC"}
];
var AW_RG = [["all","\u0e17\u0e38\u0e01\u0e20\u0e39\u0e21\u0e34\u0e20\u0e32\u0e04"], ["apac","\u0e40\u0e2d\u0e40\u0e0a\u0e35\u0e22\u2013\u0e41\u0e1b\u0e0b\u0e34\u0e1f\u0e34\u0e01"],
  ["emea","\u0e22\u0e38\u0e42\u0e23\u0e1b\u2013\u0e15\u0e30\u0e27\u0e31\u0e19\u0e2d\u0e2d\u0e01\u0e01\u0e25\u0e32\u0e07\u2013\u0e41\u0e2d\u0e1f\u0e23\u0e34\u0e01\u0e32"], ["amer","\u0e2d\u0e40\u0e21\u0e23\u0e34\u0e01\u0e32"]];
var AW_HOF = [
  {b:"icm", q:9, run:9, cat:"fx", since:"Q2 2024"},
  {b:"ig", q:8, run:8, cat:"fx", since:"Q3 2024"},
  {b:"saxo", q:7, run:7, cat:"stocks", since:"Q4 2024"},
  {b:"pep", q:6, run:6, cat:"fx", since:"Q1 2025"},
  {b:"ibkr", q:6, run:6, cat:"stocks", since:"Q1 2025"}
];
var AW_METH = [
  ["25%", "Execution", "\u0e40\u0e27\u0e25\u0e32\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e41\u0e25\u0e30\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e23\u0e35\u0e42\u0e04\u0e27\u0e15 \u0e08\u0e32\u0e01\u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c\u0e08\u0e23\u0e34\u0e07\u0e17\u0e35\u0e48 EA \u0e40\u0e01\u0e47\u0e1a"],
  ["25%", "Spread & Cost", "\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21\u0e15\u0e48\u0e2d\u0e25\u0e47\u0e2d\u0e15 \u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e2b\u0e21\u0e27\u0e14\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19"],
  ["20%", "Liquidity", "\u0e04\u0e27\u0e32\u0e21\u0e25\u0e36\u0e01\u0e02\u0e2d\u0e07\u0e2a\u0e20\u0e32\u0e1e\u0e04\u0e25\u0e48\u0e2d\u0e07 \u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08 \u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e23\u0e35\u0e42\u0e04\u0e27\u0e15\u0e0a\u0e48\u0e27\u0e07\u0e02\u0e48\u0e32\u0e27"],
  ["15%", "Fund Safety", "\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15 \u0e01\u0e32\u0e23\u0e41\u0e22\u0e01\u0e1a\u0e31\u0e0d\u0e0a\u0e35 \u0e01\u0e2d\u0e07\u0e17\u0e38\u0e19\u0e0a\u0e14\u0e40\u0e0a\u0e22 \u0e2a\u0e16\u0e34\u0e15\u0e34\u0e01\u0e32\u0e23\u0e16\u0e2d\u0e19"],
  ["15%", "Support", "\u0e40\u0e27\u0e25\u0e32\u0e15\u0e2d\u0e1a\u0e08\u0e23\u0e34\u0e07 \u0e2d\u0e31\u0e15\u0e23\u0e32\u0e01\u0e32\u0e23\u0e41\u0e01\u0e49\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e08\u0e19\u0e08\u0e1a \u0e41\u0e25\u0e30\u0e04\u0e27\u0e32\u0e21\u0e1e\u0e36\u0e07\u0e1e\u0e2d\u0e43\u0e08\u0e02\u0e2d\u0e07\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49"]
];
function awCat(k){
  for (var i = 0; i < AW_CATS.length; i++) { if (AW_CATS[i].k === k) { return AW_CATS[i]; } }
  return AW_CATS[0];
}
function awName(id){ return (META[id] || {}).n || id; }
function awMono(id){ return (META[id] || {}).mono || "?"; }
function awReg(id){ return (META[id] || {}).reg || ""; }
function awLogo(id, size, r){
  return '<span class="lg-tile" data-logo="' + ((typeof LOGO_SLUG !== "undefined" && LOGO_SLUG[id]) || id) +
    '|' + awMono(id) + '" style="width:' + size + 'px;height:' + size + 'px;border-radius:' +
    (r || 9) + 'px;flex-shrink:0">' + awMono(id) + '</span>';
}
function awDemo(t){
  return '<div class="aw-demo"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" ' +
    'stroke="#B54708" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ' +
    'aria-hidden="true" style="flex-shrink:0"><circle cx="12" cy="12" r="9"></circle>' +
    '<path d="M12 7.6V13M12 16.2v.1"></path></svg><span>' + t + '</span></div>';
}

function awStarRow(n, size){
  var h = "";
  for (var i = 0; i < AW_STMAX; i++) {
    h += '<span style="opacity:' + (i < n ? 1 : 0.18) + ';line-height:0">' + awardStar(size) + '</span>';
  }
  return '<span class="aw-strow" role="img" aria-label="\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a ' + n +
    ' \u0e14\u0e32\u0e27\u0e08\u0e32\u0e01 ' + AW_STMAX + '">' + h + '</span>';
}
/* \u0e14\u0e32\u0e27\u0e43\u0e19\u0e15\u0e23\u0e32 \u2014 \u0e43\u0e0a\u0e49\u0e40\u0e2a\u0e49\u0e19\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e42\u0e25\u0e42\u0e01\u0e49\u0e40\u0e27\u0e47\u0e1a \u0e22\u0e48\u0e2d\u0e2a\u0e48\u0e27\u0e19\u0e08\u0e32\u0e01 viewBox 64 */
function awBadgeStar(x, y, sc){
  return '<g transform="translate(' + x + ',' + y + ') scale(' + (sc / 64) + ')">' +
    '<path d="' + AW_D + '" fill="#D92D20" stroke="#A81E14" stroke-width="2.4" ' +
    'stroke-linejoin="round" paint-order="stroke"></path>' + AW_FACET +
    '<path d="' + AW_D + '" fill="none" stroke="#A81E14" stroke-width="1.6" ' +
    'stroke-linejoin="round"></path></g>';
}
function awBadge(w, h, opt){
  var o = opt || {}, sq = w === h;
  var cat = o.cat || "Forex / CFD", per = o.per || AW_PERIOD, cid = o.cid || "RS-2026Q2-000128";
  var st = o.st || AW_STMAX;
  var s = w / 320;
  var stars = "";
  if (!sq) {
    for (var i = 0; i < AW_STMAX; i++) {
      stars += awBadgeStar(152 * s + i * 15 * s, h - 27 * s, 12 * s)
        .replace("#D92D20", i < st ? "#D92D20" : "#2C2C2F")
        .replace(/#A81E14/g, i < st ? "#A81E14" : "#242427");
    }
  } else {
    for (var k = 0; k < AW_STMAX; k++) {
      stars += awBadgeStar(194 + k * 44, 352, 34).replace("#D92D20", k < st ? "#D92D20" : "#2C2C2F")
        .replace(/#A81E14/g, k < st ? "#A81E14" : "#242427");
    }
  }
  var sx = sq ? w / 2 - 46 : 22 * s;
  var sy = sq ? 66 : h / 2 - 30 * s;
  var ss = sq ? 92 : 60 * s;
  var tx = sq ? w / 2 : 22 * s + ss + 16 * s;
  var an = sq ? "middle" : "start";
  return '<svg class="bdg" width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + ' ' + h + '" ' +
    'role="img" aria-label="RED STAR \u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e17\u0e23\u0e07\u0e04\u0e38\u0e13\u0e04\u0e48\u0e32 ' +
    cat + ' ' + per + ' \u0e44\u0e14\u0e49 ' + st + ' \u0e14\u0e32\u0e27 \u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e41\u0e25\u0e49\u0e27">' +
    '<rect width="' + w + '" height="' + h + '" rx="' + (sq ? 22 : 8) + '" fill="#0A0A0A"/>' +
    '<rect x="0.75" y="0.75" width="' + (w - 1.5) + '" height="' + (h - 1.5) + '" rx="' +
      (sq ? 21 : 7.3) + '" fill="none" stroke="#A98420" stroke-width="1.5"/>' +
    (sq ? '<rect x="9" y="9" width="' + (w - 18) + '" height="' + (h - 18) + '" rx="15" fill="none" ' +
      'stroke="#A98420" stroke-width="0.8" opacity="0.45"/>' : "") +
    awBadgeStar(sx, sy, ss) + stars +
    '<text x="' + tx + '" y="' + (sq ? 218 : h / 2 - 12 * s) + '" text-anchor="' + an + '" ' +
      'font-family="Inter,sans-serif" font-size="' + (sq ? 40 : 21 * s) + '" font-weight="700" ' +
      'letter-spacing="' + (sq ? 1.5 : 0.4 * s) + '" fill="#FFFFFF">' +
      '<tspan fill="#E8483E">RED</tspan> STAR</text>' +
    '<text x="' + tx + '" y="' + (sq ? 250 : h / 2 + 4 * s) + '" text-anchor="' + an + '" ' +
      'font-family="Inter,sans-serif" font-size="' + (sq ? 17 : 10 * s) + '" font-weight="600" ' +
      'letter-spacing="' + (sq ? 2.6 : 1.1 * s) + '" fill="#A98420">\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e17\u0e23\u0e07\u0e04\u0e38\u0e13\u0e04\u0e48\u0e32</text>' +
    '<text x="' + tx + '" y="' + (sq ? 288 : h / 2 + 20 * s) + '" text-anchor="' + an + '" ' +
      'font-family="Inter,sans-serif" font-size="' + (sq ? 16 : 9.4 * s) + '" font-weight="600" ' +
      'letter-spacing="' + (sq ? 0.8 : 0.3 * s) + '" fill="rgba(255,255,255,0.7)">' +
      cat + '  \u00b7  ' + per + '</text>' +
    (sq ? '<line x1="120" y1="410" x2="392" y2="410" stroke="#A98420" stroke-width="1" opacity="0.5"/>' +
      '<text x="256" y="440" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" ' +
      'font-weight="600" letter-spacing="0.8" fill="rgba(255,255,255,0.5)">VERIFIED \u00b7 ' + cid + '</text>' +
      '<text x="256" y="466" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" ' +
      'font-weight="600" letter-spacing="1.2" fill="#A98420">redstartrust.com/verify</text>'
    : '<text x="' + tx + '" y="' + (h - 17 * s) + '" text-anchor="start" font-family="Inter,sans-serif" ' +
      'font-size="' + (8.4 * s) + '" font-weight="600" letter-spacing="' + (0.5 * s) +
      '" fill="rgba(255,255,255,0.5)">VERIFIED \u00b7 ' + cid + '</text>') +
    '</svg>';
}
/* \u2500\u2500 QR \u2014 \u0e20\u0e32\u0e1e\u0e41\u0e17\u0e19\u0e17\u0e35\u0e48\u0e04\u0e07\u0e17\u0e35\u0e48\u0e15\u0e48\u0e2d\u0e40\u0e25\u0e02\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07 \u2014 \u0e22\u0e31\u0e07\u0e2a\u0e41\u0e01\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 \u2500\u2500 */
function awQR(txt, px){
  var n = 25, c = (px || 150) / n, h = seed(txt), out = "";
  function on(x, y){
    var q = 7;
    if ((x < q && y < q) || (x >= n - q && y < q) || (x < q && y >= n - q)) { return null; }
    h = (h * 1664525 + 1013904223 + x * 37 + y * 131) >>> 0;
    return ((h >>> 13) & 3) !== 0;
  }
  for (var y = 0; y < n; y++) {
    for (var x = 0; x < n; x++) {
      var v = on(x, y);
      if (v) { out += '<rect x="' + (x * c).toFixed(2) + '" y="' + (y * c).toFixed(2) +
        '" width="' + c.toFixed(2) + '" height="' + c.toFixed(2) + '" fill="#0A0A0A"/>'; }
    }
  }
  function eye(cx, cy){
    return '<rect x="' + (cx * c) + '" y="' + (cy * c) + '" width="' + (7 * c) + '" height="' + (7 * c) +
      '" fill="#0A0A0A"/><rect x="' + ((cx + 1) * c) + '" y="' + ((cy + 1) * c) + '" width="' + (5 * c) +
      '" height="' + (5 * c) + '" fill="#FFFFFF"/><rect x="' + ((cx + 2) * c) + '" y="' + ((cy + 2) * c) +
      '" width="' + (3 * c) + '" height="' + (3 * c) + '" fill="#B91C1C"/>';
  }
  return '<svg width="' + (px || 150) + '" height="' + (px || 150) + '" viewBox="0 0 ' + (px || 150) +
    ' ' + (px || 150) + '" role="img" aria-label="\u0e20\u0e32\u0e1e QR \u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e25\u0e34\u0e07\u0e01\u0e4c\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a">' +
    '<rect width="' + (px || 150) + '" height="' + (px || 150) + '" fill="#FFFFFF"/>' + out +
    eye(0, 0) + eye(n - 7, 0) + eye(0, n - 7) + '</svg>';
}

/* \u2500\u2500 PAGE 1 \u2014 /awards \u2500\u2500 */
(function(){
  var h = document.getElementById("aw-hero");
  if (!h) { return; }
  h.innerHTML =
    '<div class="aw-hwm" aria-hidden="true">' + awardStar(560) + '</div>' +
    '<div class="aw-hin">' +
      '<div class="aw-mark" style="margin-bottom:26px">' + awardStar(76) +
      '<span class="tx"><h3><i>RED</i> STAR</h3>' +
      '<span>\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e17\u0e23\u0e07\u0e04\u0e38\u0e13\u0e04\u0e48\u0e32</span></span></div>' +
      '<h1><i>RED</i> STAR<br>' + AW_PERIOD + '</h1>' +
      '<p class="aw-cap" style="color:#A98420;letter-spacing:0.14em;margin:-8px 0 22px">' +
      '\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e17\u0e23\u0e07\u0e04\u0e38\u0e13\u0e04\u0e48\u0e32\u0e02\u0e2d\u0e07 RedStarTrust</p>' +
      '<p><b style="color:#FFFFFF;font-weight:600">\u0e40\u0e23\u0e32\u0e21\u0e35\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e40\u0e14\u0e35\u0e22\u0e27 \u0e04\u0e37\u0e2d \u0e14\u0e32\u0e27\u0e41\u0e14\u0e07</b> \u2014 ' +
      '\u0e17\u0e38\u0e01\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e17\u0e35\u0e48\u0e40\u0e23\u0e32\u0e15\u0e23\u0e27\u0e08\u0e23\u0e27\u0e21\u0e21\u0e32\u0e08\u0e1a\u0e17\u0e35\u0e48\u0e14\u0e32\u0e27\u0e14\u0e27\u0e07\u0e19\u0e35\u0e49 ' +
      '\u0e21\u0e2d\u0e1a\u0e43\u0e2b\u0e49\u0e15\u0e32\u0e21\u0e2b\u0e21\u0e27\u0e14\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c <b style="color:#FFFFFF;font-weight:600">\u0e17\u0e38\u0e01\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a</b> ' +
      '\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e1a\u0e2d\u0e01\u0e14\u0e49\u0e27\u0e22\u0e08\u0e33\u0e19\u0e27\u0e19\u0e14\u0e32\u0e27 1 \u0e16\u0e36\u0e07 3 ' +
      '\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e08\u0e32\u0e01\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e08\u0e23\u0e34\u0e07 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e42\u0e2b\u0e27\u0e15 ' +
      '\u0e44\u0e21\u0e48\u0e21\u0e35\u0e0a\u0e48\u0e2d\u0e07\u0e17\u0e32\u0e07\u0e43\u0e2b\u0e49\u0e0b\u0e37\u0e49\u0e2d \u0e41\u0e25\u0e30\u0e17\u0e38\u0e01\u0e43\u0e1a\u0e15\u0e23\u0e27\u0e08\u0e01\u0e25\u0e31\u0e1a\u0e44\u0e14\u0e49\u0e14\u0e49\u0e27\u0e22\u0e40\u0e25\u0e02\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07</p>' +
      '<p class="aw-cap" style="color:rgba(255,255,255,0.45);margin:-18px 0 26px">\u0e23\u0e2d\u0e1a\u0e16\u0e31\u0e14\u0e44\u0e1b \u00b7 ' + AW_NEXT + '</p>' +
      '<div class="aw-hbt"><a class="aw-btn pri" href="#/awards2026">\u0e14\u0e39\u0e1c\u0e39\u0e49\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e14\u0e32\u0e27 ' + AW_PERIOD + '</a>' +
      '<a class="aw-btn onblk" href="#/verify">\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07</a></div>' +
      '<div class="aw-hst">' +
        '<div><b>12</b><span>\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49\u0e14\u0e32\u0e27\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e19\u0e35\u0e49</span></div>' +
        '<div><b>114</b><span>\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e17\u0e35\u0e48\u0e40\u0e02\u0e49\u0e32\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19</span></div>' +
        '<div><b>4.8\u0e25\u0e49\u0e32\u0e19</b><span>\u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c\u0e08\u0e23\u0e34\u0e07\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49\u0e04\u0e33\u0e19\u0e27\u0e13</span></div>' +
        '<div><b>4</b><span>\u0e23\u0e2d\u0e1a\u0e15\u0e23\u0e27\u0e08\u0e15\u0e48\u0e2d\u0e1b\u0e35 \u00b7 \u0e14\u0e32\u0e27\u0e2b\u0e21\u0e14\u0e2d\u0e32\u0e22\u0e38\u0e17\u0e38\u0e01\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a</span></div>' +
      '</div></div>';

  var c = document.getElementById("aw-cats");
  if (c) {
    c.className = "aw-sec";
    c.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">Award Categories</p>' +
      '<h2 class="aw-h2">\u0e2b\u0e21\u0e27\u0e14\u0e17\u0e35\u0e48\u0e21\u0e2d\u0e1a\u0e14\u0e32\u0e27</h2>' +
      '<p>\u0e14\u0e32\u0e27\u0e14\u0e27\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19 \u0e41\u0e15\u0e48\u0e21\u0e2d\u0e1a\u0e41\u0e22\u0e01\u0e15\u0e32\u0e21\u0e2b\u0e21\u0e27\u0e14 ' +
      '\u0e40\u0e1e\u0e23\u0e32\u0e30\u0e42\u0e1a\u0e23\u0e01\u0e17\u0e35\u0e48\u0e14\u0e35\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07 Forex \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e14\u0e35\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e14\u0e49\u0e27\u0e22 ' +
      '\u0e41\u0e15\u0e48\u0e25\u0e30\u0e2b\u0e21\u0e27\u0e14\u0e08\u0e36\u0e07\u0e15\u0e23\u0e27\u0e08\u0e14\u0e49\u0e27\u0e22\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e02\u0e2d\u0e07\u0e2b\u0e21\u0e27\u0e14\u0e19\u0e31\u0e49\u0e19\u0e40\u0e2d\u0e07</p></div>' +
      '<span class="rt"><a class="aw-btn out" href="#/awards2026">\u0e14\u0e39\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14</a></span></div>' +
      '<div class="aw-grid">' + AW_CATS.map(function(a){
        var w = null;
        for (var i = 0; i < AW_WIN.length; i++) { if (AW_WIN[i].cat === a.k) { w = AW_WIN[i]; break; } }
        return '<a class="aw-card" href="#/verify" data-awcat="' + a.k + '">' +
          '<span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" ' +
          'stroke="#B91C1C" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" ' +
          'aria-hidden="true">' + a.ic + '</svg></span>' +
          '<h3>' + a.n + '</h3><p>' + a.d + '</p>' +
          '<span class="ft">' + (w ? awStarRow(w.st, 13) + '<b>' + awName(w.b) + '</b>' : "") +
          '<span class="go">\u0e14\u0e39\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07 \u2192</span></span></a>';
      }).join("") + '</div>';
  }

  var hf = document.getElementById("aw-hof");
  if (hf) {
    hf.className = "aw-sec";
    hf.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">Hall of Fame</p>' +
      '<h2 class="aw-h2">\u0e1c\u0e39\u0e49\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e17\u0e23\u0e07\u0e04\u0e38\u0e13\u0e04\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32</h2>' +
      '<p>\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a 3,000 \u0e02\u0e49\u0e2d <b style="color:#0A0A0A">\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19\u0e22\u0e32\u0e27\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14</b> \u2014 \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e19\u0e35\u0e49\u0e04\u0e37\u0e2d\u0e2a\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e44\u0e14\u0e49\u0e14\u0e32\u0e27\u0e14\u0e27\u0e07\u0e17\u0e35\u0e48 2 \u0e41\u0e25\u0e30 3 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e44\u0e2b\u0e19\u0e2b\u0e25\u0e38\u0e14\u0e41\u0e21\u0e49\u0e02\u0e49\u0e2d\u0e40\u0e14\u0e35\u0e22\u0e27 \u0e15\u0e31\u0e27\u0e19\u0e31\u0e1a\u0e01\u0e25\u0e31\u0e1a\u0e40\u0e1b\u0e47\u0e19\u0e28\u0e39\u0e19\u0e22\u0e4c\u0e17\u0e31\u0e19\u0e17\u0e35</p></div>' +
      '<span class="rt"><a class="aw-btn out" href="#/brokerawards">\u0e14\u0e39\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e42\u0e1b\u0e23\u0e44\u0e1f\u0e25\u0e4c</a></span></div>' +
      '<div class="aw-hofx">' + AW_HOF.map(function(r){
        var c = awCat(r.cat);
        return '<a class="aw-hx" href="#/brokerawards">' +
          '<span class="aw-hxt">' + awStarRow(AW_STMAX, 15) +
          '<b>' + r.run + '</b><span>\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19</span></span>' +
          '<span class="aw-hxb">' + awLogo(r.b, 42, 10) +
          '<strong>' + awName(r.b) + '</strong><em>' + c.n + '</em></span>' +
          '<span class="aw-hxy"><i>\u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48 ' + r.since + '</i><i>\u0e23\u0e27\u0e21 ' + r.q + ' \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a</i></span></a>';
      }).join("") + '</div>';
  }

  var mt = document.getElementById("aw-meth");
  if (mt) {
    mt.className = "aw-sec";
    mt.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">Methodology</p>' +
      '<h2 class="aw-h2">\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19</h2>' +
      '<p>\u0e04\u0e30\u0e41\u0e19\u0e19\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e21\u0e32\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e27\u0e31\u0e14 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e04\u0e30\u0e41\u0e19\u0e19\u0e08\u0e32\u0e01\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2b\u0e47\u0e19\u0e2b\u0e23\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e42\u0e2b\u0e27\u0e15\u0e02\u0e2d\u0e07\u0e01\u0e23\u0e23\u0e21\u0e01\u0e32\u0e23</p></div>' +
      '<span class="rt"><a class="aw-btn ghost" href="#/criteria">\u0e14\u0e39\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e01\u0e32\u0e23\u0e43\u0e2b\u0e49\u0e14\u0e32\u0e27 \u2192</a></span></div>' +
      '<div class="aw-meth">' + AW_METH.map(function(m){
        return '<div class="aw-mi"><b>' + m[0] + '</b><em>' + m[1] + '</em><span>' + m[2] + '</span></div>';
      }).join("") + '</div>';
  }

  var ct = document.getElementById("aw-cta");
  if (ct) {
    ct.className = "aw-cta";
    ct.innerHTML =
      '<div><h2>\u0e40\u0e2b\u0e47\u0e19\u0e15\u0e23\u0e32 RedStar \u0e1a\u0e19\u0e40\u0e27\u0e47\u0e1a\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c?</h2>' +
      '<p>\u0e15\u0e23\u0e32\u0e17\u0e38\u0e01\u0e43\u0e1a\u0e21\u0e35\u0e40\u0e25\u0e02\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e2d\u0e22\u0e39\u0e48 ' +
      '\u0e01\u0e23\u0e2d\u0e01\u0e40\u0e25\u0e02\u0e19\u0e31\u0e49\u0e19\u0e17\u0e35\u0e48\u0e19\u0e35\u0e48\u0e41\u0e25\u0e49\u0e27\u0e04\u0e38\u0e13\u0e08\u0e30\u0e40\u0e2b\u0e47\u0e19\u0e27\u0e48\u0e32\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e19\u0e31\u0e49\u0e19\u0e21\u0e35\u0e08\u0e23\u0e34\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48 ' +
      '\u0e2d\u0e2d\u0e01\u0e43\u0e2b\u0e49\u0e43\u0e04\u0e23 \u0e1b\u0e35\u0e44\u0e2b\u0e19 \u0e41\u0e25\u0e30\u0e16\u0e39\u0e01\u0e40\u0e1e\u0e34\u0e01\u0e16\u0e2d\u0e19\u0e44\u0e1b\u0e41\u0e25\u0e49\u0e27\u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48</p>' +
      '<a class="aw-btn onblk" href="#/partner">\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c: \u0e40\u0e02\u0e49\u0e32 Partner Dashboard</a></div>' +
      '<div class="aw-vbox"><label for="aw-vq">\u0e40\u0e25\u0e02\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07</label>' +
      '<span class="aw-vin"><input id="aw-vq" class="aw-mono" type="text" value="RS-2026-000128" ' +
      'autocomplete="off" aria-label="\u0e40\u0e25\u0e02\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07">' +
      '<a class="aw-btn pri" href="#/verify">\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a</a></span>' +
      '<p class="aw-vhint">\u0e40\u0e25\u0e02\u0e2d\u0e22\u0e39\u0e48\u0e21\u0e38\u0e21\u0e25\u0e48\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e15\u0e23\u0e32 \u0e2b\u0e23\u0e37\u0e2d\u0e2a\u0e41\u0e01\u0e19 QR \u0e1a\u0e19\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07 \u00b7 \u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07: RS-2026-000128</p></div>';
  }
  paintLogos();
})();

/* \u2500\u2500 PAGE 2 \u2014 /awards/2026 \u2500\u2500 */
var w26 = {rg: "all", cat: "all", lic: "all", q: AW_PERIOD};
var AW_QS = ["Q2 2026", "Q1 2026", "Q4 2025", "Q3 2025"];
function w26Rows(){
  /* \u0e23\u0e2d\u0e1a\u0e01\u0e48\u0e2d\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e40\u0e01\u0e47\u0e1a\u0e44\u0e27\u0e49\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e15\u0e2d\u0e19\u0e19\u0e31\u0e49\u0e19\u0e40\u0e23\u0e32\u0e15\u0e23\u0e27\u0e08\u0e44\u0e14\u0e49\u0e19\u0e49\u0e2d\u0e22\u0e23\u0e32\u0e22\u0e01\u0e27\u0e48\u0e32 */
  var qi = AW_QS.indexOf(w26.q), cap = qi <= 0 ? AW_WIN.length : AW_WIN.length - qi * 2;
  return AW_WIN.slice(0, Math.max(3, cap)).filter(function(w){
    return (w26.rg === "all" || w.rg === w26.rg) &&
           (w26.cat === "all" || w.cat === w26.cat) &&
           (w26.lic === "all" || w.lic === w26.lic);
  });
}
function w26Render(){
  var box = document.getElementById("w26-table");
  if (!box) { return; }
  var rows = w26Rows();
  var cnt = document.getElementById("w26-cnt");
  if (cnt) { cnt.textContent = "\u0e41\u0e2a\u0e14\u0e07 " + rows.length + " \u0e08\u0e32\u0e01 " + AW_WIN.length + " \u0e23\u0e32\u0e22\u0e01\u0e32\u0e23"; }
  box.className = "w26-wrap";
  if (!rows.length) {
    box.innerHTML = '<div style="padding:56px;text-align:center;font-size:13.5px;color:#71717A">' +
      '\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e1c\u0e39\u0e49\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e43\u0e19\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e19\u0e35\u0e49<br>' +
      '\u0e40\u0e23\u0e32\u0e44\u0e21\u0e48\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e02\u0e2d\u0e07\u0e02\u0e2d\u0e1a\u0e40\u0e02\u0e15\u0e17\u0e35\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e40\u0e02\u0e49\u0e32\u0e44\u0e1b\u0e15\u0e23\u0e27\u0e08</div>';
    return;
  }
  box.innerHTML = '<table class="w26"><thead><tr>' +
    '<th>\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a</th><th>\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c</th><th>\u0e2b\u0e21\u0e27\u0e14</th><th>\u0e14\u0e32\u0e27\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49</th><th>\u0e04\u0e30\u0e41\u0e19\u0e19</th><th>\u0e40\u0e25\u0e02\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07</th><th></th>' +
    '</tr></thead><tbody>' + rows.map(function(w, i){
      return '<tr tabindex="0" data-awrow="' + w.b + '">' +
        '<td><span class="w26-rk' + (i === 0 ? " g" : "") + '">' + (i + 1) + '</span></td>' +
        '<td><span class="w26-bk">' + awLogo(w.b, 34, 8) + '<span><b>' + awName(w.b) + '</b>' +
          '<span>' + awReg(w.b) + '</span></span></span></td>' +
        '<td>' + awCat(w.cat).n + '</td>' +
        '<td>' + awStarRow(w.st, 14) + '</td>' +
        '<td><span class="w26-sc">' + w.sc.toFixed(1) + '</span></td>' +
        '<td><span class="w26-id">' + w.id.replace(/2026Q2/, w26.q.replace(/(Q\\d) (\\d+)/, "$2$1")) + '</span></td>' +
        '<td style="text-align:right"><a class="aw-btn out sm" href="#/verify" ' +
          'data-awverify="' + w.id + '">Verify</a></td></tr>';
    }).join("") + '</tbody></table>';
  paintLogos();
}
(function(){
  var c = document.getElementById("w26-ctl");
  if (!c) { return; }
  var CATO = [["all", "\u0e17\u0e38\u0e01\u0e2b\u0e21\u0e27\u0e14"]].concat(AW_CATS.map(function(a){ return [a.k, a.n]; }));
  var LICO = [["all", "\u0e17\u0e38\u0e01\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19"]];
  var QO = AW_QS.map(function(q){ return [q, q]; });
  var seen = {};
  AW_WIN.forEach(function(w){ if (!seen[w.lic]) { seen[w.lic] = 1; LICO.push([w.lic, w.lic]); } });
  function fld(id, lb, opts){
    return '<label class="w26-f"><span>' + lb + '</span><select id="' + id + '">' +
      opts.map(function(o){ return '<option value="' + o[0] + '">' + o[1] + '</option>'; }).join("") +
      '</select></label>';
  }
  c.className = "w26-ctl";
  c.innerHTML = fld("w26-q", "\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a", QO) + fld("w26-rg", "Region", AW_RG) +
    fld("w26-cat", "Category", CATO) + fld("w26-lic", "License", LICO) +
    '<span class="w26-cnt" id="w26-cnt"></span>';
  c.addEventListener("change", function(ev){
    var t = ev.target;
    if (t.id === "w26-q") { w26.q = t.value; }
    else if (t.id === "w26-rg") { w26.rg = t.value; }
    else if (t.id === "w26-cat") { w26.cat = t.value; }
    else if (t.id === "w26-lic") { w26.lic = t.value; }
    w26Render();
  });
  w26Render();
  var n = document.getElementById("w26-note");
  if (n) {
    n.innerHTML = "\u0e04\u0e30\u0e41\u0e19\u0e19\u0e40\u0e15\u0e47\u0e21 100 \u00b7 \u0e04\u0e33\u0e19\u0e27\u0e13\u0e08\u0e32\u0e01 Execution 25% \u00b7 Spread &amp; Cost 25% \u00b7 " +
      "Liquidity 20% \u00b7 Fund Safety 15% \u00b7 Support 15% \u2014 <b>\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e21\u0e21\u0e15\u0e34</b> " +
      "\u0e43\u0e0a\u0e49\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e41\u0e2a\u0e14\u0e07\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19";
  }
})();

/* \u2500\u2500 PAGE 3 \u2014 /verify/RS-2026-000128 \u2500\u2500 */
var VF_DIM = [["Execution", 96.8, "\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 34 ms"],
  ["Spread & Cost", 95.2, "\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21 $7.10 / \u0e25\u0e47\u0e2d\u0e15"],
  ["Liquidity", 97.5, "\u0e2a\u0e25\u0e34\u0e1b\u0e40\u0e1e\u0e08\u0e1a\u0e27\u0e01 63% \u0e02\u0e2d\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07"],
  ["Fund Safety", 96.0, "\u0e41\u0e22\u0e01\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e04\u0e23\u0e1a \u0e16\u0e2d\u0e19\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 1 \u0e0a\u0e21. 12 \u0e19."],
  ["Support", 94.9, "\u0e15\u0e2d\u0e1a\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 3 \u0e19\u0e32\u0e17\u0e35 \u00b7 \u0e44\u0e17\u0e22 24/5"]];
var VF_WHY = [
  ["\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e15\u0e48\u0e33\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14",
   "\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21\u0e15\u0e48\u0e2d\u0e25\u0e47\u0e2d\u0e15\u0e2d\u0e22\u0e39\u0e48\u0e17\u0e35\u0e48 $7.10 \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e2b\u0e21\u0e27\u0e14 23% \u0e41\u0e25\u0e30\u0e19\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19 24 \u0e23\u0e32\u0e22\u0e17\u0e35\u0e48\u0e15\u0e23\u0e27\u0e08",
   "\u0e17\u0e35\u0e48\u0e21\u0e32: Trade Analytics EA \u00b7 1.2 \u0e25\u0e49\u0e32\u0e19\u0e2d\u0e2d\u0e23\u0e4c\u0e40\u0e14\u0e2d\u0e23\u0e4c"],
  ["\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e47\u0e27\u0e2a\u0e21\u0e48\u0e33\u0e40\u0e2a\u0e21\u0e2d\u0e17\u0e31\u0e49\u0e07\u0e1b\u0e35",
   "\u0e40\u0e27\u0e25\u0e32\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 34 ms \u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e14\u0e37\u0e2d\u0e19\u0e44\u0e2b\u0e19\u0e17\u0e35\u0e48\u0e40\u0e01\u0e34\u0e19 45 ms \u0e41\u0e21\u0e49\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e02\u0e48\u0e32\u0e27\u0e41\u0e23\u0e07",
   "\u0e17\u0e35\u0e48\u0e21\u0e32: Broker Health Monitor EA \u00b7 \u0e40\u0e01\u0e47\u0e1a\u0e17\u0e38\u0e01\u0e27\u0e31\u0e19 12 \u0e40\u0e14\u0e37\u0e2d\u0e19"],
  ["\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e02\u0e49\u0e2d\u0e1e\u0e34\u0e1e\u0e32\u0e17\u0e04\u0e49\u0e32\u0e07",
   "\u0e15\u0e25\u0e2d\u0e14\u0e1b\u0e35\u0e21\u0e35\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e41\u0e08\u0e49\u0e07 4 \u0e23\u0e32\u0e22 \u0e15\u0e2d\u0e1a\u0e04\u0e23\u0e1a\u0e17\u0e38\u0e01\u0e23\u0e32\u0e22\u0e20\u0e32\u0e22\u0e43\u0e19 5 \u0e27\u0e31\u0e19 \u0e41\u0e25\u0e30\u0e1b\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e44\u0e14\u0e49\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14",
   "\u0e17\u0e35\u0e48\u0e21\u0e32: \u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e02\u0e49\u0e2d\u0e1e\u0e34\u0e1e\u0e32\u0e17 RedStarTrust"]
];
var VF_TL = [
  {y: "Q2 2026", sr: 3, sc: 96.4, st: "on", id: "RS-2026Q2-000128",
   d: "\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a 3,000 \u0e02\u0e49\u0e2d \u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19\u0e40\u0e1b\u0e47\u0e19\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e17\u0e35\u0e48 9"},
  {y: "Q1 2026", sr: 3, sc: 96.0, st: "gold", id: "RS-2026Q1-000094",
   d: "\u0e04\u0e07\u0e23\u0e30\u0e14\u0e31\u0e1a 3 \u0e14\u0e32\u0e27 \u2014 \u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e15\u0e48\u0e33\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e2b\u0e21\u0e27\u0e14"},
  {y: "Q4 2025", sr: 3, sc: 95.4, st: "gold", id: "RS-2025Q4-000061",
   d: "\u0e04\u0e07\u0e23\u0e30\u0e14\u0e31\u0e1a 3 \u0e14\u0e32\u0e27 \u2014 \u0e40\u0e27\u0e25\u0e32\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e19\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21"},
  {y: "Q3 2025", sr: 3, sc: 94.6, st: "gold", id: "RS-2025Q3-000044",
   d: "\u0e04\u0e23\u0e1a 6 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19 \u2014 \u0e02\u0e36\u0e49\u0e19\u0e40\u0e1b\u0e47\u0e19 3 \u0e14\u0e32\u0e27\u0e40\u0e1b\u0e47\u0e19\u0e23\u0e2d\u0e1a\u0e41\u0e23\u0e01"},
  {y: "Q2 2025", sr: 2, sc: 93.2, st: "gold", id: "RS-2025Q2-000031",
   d: "\u0e1c\u0e48\u0e32\u0e19\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19\u0e40\u0e1b\u0e47\u0e19\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e17\u0e35\u0e48 5 \u2014 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e04\u0e23\u0e1a 6"},
  {y: "Q1 2025", sr: 2, sc: 92.1, st: "gold", id: "RS-2025Q1-000018",
   d: "\u0e1c\u0e48\u0e32\u0e19\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19\u0e40\u0e1b\u0e47\u0e19\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e17\u0e35\u0e48 4"}
];
(function(){
  var h = document.getElementById("vf-hero");
  if (!h) { return; }
  var W = AW_WIN[0], cat = awCat(W.cat);
  h.className = "vf-hero";
  h.innerHTML =
    '<div class="vf-wm" aria-hidden="true">' + awardStar(300) + '</div>' +
    '<div class="vf-l">' +
      '<p class="aw-cap" style="color:#B91C1C;margin-bottom:16px">\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25</p>' +
      '<div class="vf-bk">' + awLogo(W.b, 52, 12) + '<span class="nm"><b>' + awName(W.b) + '</b><br>' +
        '<span>' + awReg(W.b) + '</span></span></div>' +
      '<div class="aw-mark" style="margin-bottom:18px">' + awardStar(64) +
        '<span class="tx"><h3 style="color:#0A0A0A"><i>RED</i> STAR</h3>' +
        '<span style="color:#7A5C11">\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e17\u0e23\u0e07\u0e04\u0e38\u0e13\u0e04\u0e48\u0e32</span></span></div>' +
      '<h2 class="vf-aw" style="font-size:30px">\u0e2b\u0e21\u0e27\u0e14 ' + cat.n + ' \u00b7 ' + AW_PERIOD + '</h2>' +
      '<div style="margin:0 0 18px">' + awStarRow(W.st, 26) + '</div>' +
      '<div class="vf-tags">' +
        '<span class="aw-tag vf"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" ' +
        'stroke="#05603A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" ' +
        'aria-hidden="true"><path d="M4.5 12.5 10 18 19.5 6.5"></path></svg>Verified</span>' +
        '<span class="aw-tag win">\u0e44\u0e14\u0e49\u0e14\u0e32\u0e27 ' + AW_PERIOD + '</span>' +
        '<span class="aw-tag hof">\u0e1c\u0e48\u0e32\u0e19\u0e15\u0e34\u0e14\u0e01\u0e31\u0e19 9 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a</span></div>' +
      '<div class="vf-meta">' +
        '<div><span>Certificate ID</span><b>' + W.id + '</b></div>' +
        '<div><span>\u0e23\u0e2d\u0e1a\u0e17\u0e35\u0e48\u0e15\u0e23\u0e27\u0e08</span><b>' + AW_PERIOD + '</b></div>' +
        '<div><span>\u0e2a\u0e16\u0e32\u0e19\u0e30</span><b style="color:#05603A">\u0e21\u0e35\u0e1c\u0e25 \u00b7 \u0e44\u0e21\u0e48\u0e16\u0e39\u0e01\u0e40\u0e1e\u0e34\u0e01\u0e16\u0e2d\u0e19</b></div>' +
      '</div>' +
    '</div>' +
    '<div class="vf-r"><div class="vf-qr">' + awQR(W.id, 150) + '</div>' +
      '<p class="vf-qc">\u0e2a\u0e41\u0e01\u0e19\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e40\u0e1b\u0e34\u0e14\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49<br>redstartrust.com/verify/' + W.id + '</p>' +
      '<div class="vf-seal"><b>VERIFIED</b><span>RedStarTrust \u00b7 ' + AW_PERIOD + '</span></div></div>';

  var sc = document.getElementById("vf-score");
  if (sc) {
    sc.className = "aw-sec";
    sc.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">Evaluation Score</p>' +
      '<h2 class="aw-h2">\u0e04\u0e30\u0e41\u0e19\u0e19\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19</h2>' +
      '<p>\u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21 <b style="color:#0A0A0A">' + W.sc.toFixed(1) +
      ' / 100</b> \u00b7 \u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e04\u0e33\u0e19\u0e27\u0e13\u0e08\u0e32\u0e01\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e08\u0e23\u0e34\u0e07\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e23\u0e30\u0e1a\u0e38\u0e15\u0e31\u0e27\u0e15\u0e19</p></div></div>' +
      '<div class="vf-bars">' + VF_DIM.map(function(d, i){
        return '<div class="vf-bar"><div class="lb"><span>' + d[0] + '</span><i>' + d[2] + '</i>' +
          '<b>' + d[1].toFixed(1) + '</b></div><div class="vf-tr">' +
          '<i class="' + (d[1] >= 96 ? "gold" : "") + '" data-vfbar="' + d[1] + '"></i></div></div>';
      }).join("") + '</div>';
  }

  var wy = document.getElementById("vf-why");
  if (wy) {
    wy.className = "aw-sec";
    wy.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">Why We Selected This Broker</p>' +
      '<h2 class="aw-h2">\u0e17\u0e33\u0e44\u0e21\u0e42\u0e1a\u0e23\u0e01\u0e19\u0e35\u0e49\u0e08\u0e36\u0e07\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a</h2>' +
      '<p>\u0e17\u0e38\u0e01\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e01\u0e25\u0e31\u0e1a\u0e44\u0e1b\u0e17\u0e35\u0e48\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e15\u0e49\u0e19\u0e17\u0e32\u0e07\u0e44\u0e14\u0e49\u0e17\u0e38\u0e01\u0e02\u0e49\u0e2d</p></div></div>' +
      '<div class="vf-why">' + VF_WHY.map(function(w, i){
        return '<div class="vf-wi"><span class="no">' + (i + 1) + '</span><b>' + w[0] + '</b>' +
          '<p>' + w[1] + '</p><span class="src">' + w[2] + '</span></div>';
      }).join("") + '</div>';
  }

  var tl = document.getElementById("vf-tl");
  if (tl) {
    tl.className = "aw-sec";
    tl.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">Other Awards</p>' +
      '<h2 class="aw-h2">\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e02\u0e2d\u0e07\u0e42\u0e1a\u0e23\u0e01\u0e19\u0e35\u0e49</h2></div>' +
      '<span class="rt"><a class="aw-btn out" href="#/brokerawards">\u0e14\u0e39\u0e2b\u0e19\u0e49\u0e32 Hall of Fame \u0e40\u0e15\u0e47\u0e21</a></span></div>' +
      '<div class="aw-tl">' + VF_TL.slice(0, 3).map(function(t){
        return '<div class="aw-ti ' + t.st + '"><span class="yr">' + t.y + '</span>' +
          '<h4>' + t.n + '</h4>' +
          (t.sr ? '<div style="margin:-2px 0 8px">' + awStarRow(t.sr, 15) + '</div>' : "") +
          '<p>' + t.d + '</p><span class="rw">' +
          (t.sc ? '<span>\u0e04\u0e30\u0e41\u0e19\u0e19 <b>' + t.sc.toFixed(1) + '</b></span>' : "") +
          (t.id ? '<span class="aw-mono">' + t.id + '</span>' : "") + '</span></div>';
      }).join("") + '</div>';
  }

  var mm = document.getElementById("vf-meth");
  if (mm) {
    mm.className = "aw-sec";
    mm.style.paddingBottom = "80px";
    mm.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">Related Methodology</p>' +
      '<h2 class="aw-h2">\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49\u0e01\u0e31\u0e1a\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e19\u0e35\u0e49</h2></div>' +
      '<span class="rt"><a class="aw-btn out" href="#/criteria">\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e01\u0e32\u0e23\u0e43\u0e2b\u0e49\u0e14\u0e32\u0e27\u0e40\u0e15\u0e47\u0e21</a></span></div>' +
      '<div class="aw-meth">' + AW_METH.map(function(m){
        return '<div class="aw-mi"><b>' + m[0] + '</b><em>' + m[1] + '</em><span>' + m[2] + '</span></div>';
      }).join("") + '</div>' +
      '<div style="margin-top:32px">' + awDemo("\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19 <b>\u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e07\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a</b> \u0e40\u0e25\u0e02\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07 \u0e04\u0e30\u0e41\u0e19\u0e19 \u0e41\u0e25\u0e30\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e21\u0e21\u0e15\u0e34 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e2d\u0e2d\u0e01\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e08\u0e23\u0e34\u0e07 \u0e41\u0e25\u0e30 QR \u0e22\u0e31\u0e07\u0e2a\u0e41\u0e01\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49") + '</div>';
  }
  paintLogos();
})();

/* \u2500\u2500 PAGE 4 \u2014 /broker/ic-markets/awards \u2500\u2500 */
(function(){
  var h = document.getElementById("ba-hero");
  if (!h) { return; }
  var B = AW_WIN[0].b;
  h.className = "ba-hero";
  h.innerHTML =
    '<div><div class="ba-id">' + awLogo(B, 68, 15) +
      '<span><h2>' + awName(B) + '</h2><span>' + awReg(B) +
      ' \u00b7 \u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19 RedStarTrust \u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a Q1 2024</span></span></div>' +
      '<div class="ba-st"><div><b>9</b><span>\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49 3 \u0e14\u0e32\u0e27</span></div>' +
      '<div><b>Q1 2024</b><span>\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e41\u0e23\u0e01\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49\u0e14\u0e32\u0e27</span></div>' +
      '<div><b>96.4</b><span>\u0e04\u0e30\u0e41\u0e19\u0e19\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14</span></div></div></div>' +
    '<div class="ba-tro"><div class="ba-trh">' +
      '<div style="display:flex;justify-content:center;margin-bottom:12px">' + awardStar(58) + '</div>' +
      '<p class="aw-cap" style="color:#A98420">\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e17\u0e23\u0e07\u0e04\u0e38\u0e13\u0e04\u0e48\u0e32</p>' +
      '<h4><i style="font-style:normal;color:#E8483E">RED</i> STAR</h4>' +
      '<p style="margin:8px 0 0;font-size:12.5px;color:rgba(255,255,255,0.62)">\u0e2b\u0e21\u0e27\u0e14 Forex / CFD</p></div>' +
      '<div class="ba-trb"><div class="yr" style="font-size:34px">' + AW_PERIOD + '</div>' +
      '<div style="display:flex;justify-content:center;margin:-6px 0 14px">' + awStarRow(AW_STMAX, 22) + '</div>' +
      '<p>\u0e14\u0e32\u0e27\u0e41\u0e14\u0e07\u0e04\u0e23\u0e1a 3 \u0e14\u0e27\u0e07 \u0e2b\u0e21\u0e27\u0e14 Forex / CFD \u2014 '
      + '\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c GCSI \u0e04\u0e23\u0e1a\u0e17\u0e38\u0e01\u0e02\u0e49\u0e2d\u0e43\u0e19\u0e23\u0e2d\u0e1a\u0e15\u0e23\u0e27\u0e08\u0e1b\u0e35 ' + AW_PERIOD + '</p>' +
      '<a class="aw-btn out sm" href="#/verify">\u0e14\u0e39\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07</a></div>' +
      '<div class="ba-trf"><span>Certificate</span><span class="aw-mono">RS-2026-000128</span></div></div>';

  var b = document.getElementById("ba-body");
  if (b) {
    b.className = "ba-body";
    b.innerHTML =
      '<div><div class="aw-shd" style="margin-bottom:32px"><div class="tx">' +
        '<p class="aw-cap">Awards Timeline</p>' +
        '<h2 class="aw-h2">\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07</h2>' +
        '<p>\u0e41\u0e2a\u0e14\u0e07\u0e17\u0e38\u0e01\u0e1b\u0e35\u0e17\u0e35\u0e48\u0e40\u0e23\u0e32\u0e15\u0e23\u0e27\u0e08 \u0e23\u0e27\u0e21\u0e1b\u0e35\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c \u2014 \u0e40\u0e23\u0e32\u0e44\u0e21\u0e48\u0e0b\u0e48\u0e2d\u0e19\u0e1b\u0e35\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49</p></div></div>' +
        '<div class="aw-tl">' + VF_TL.map(function(t){
          return '<div class="aw-ti ' + t.st + '"><span class="yr">' + t.y + '</span>' +
            '<h4>' + t.n + '</h4>' +
            (t.sr ? '<div style="margin:-2px 0 8px">' + awStarRow(t.sr, 15) + '</div>' : "") +
            '<p>' + t.d + '</p><span class="rw">' +
            (t.sc ? '<span>\u0e04\u0e30\u0e41\u0e19\u0e19 <b>' + t.sc.toFixed(1) + '</b></span>' : "") +
            (t.id ? '<span class="aw-mono">' + t.id + '</span>' +
              '<a class="aw-btn ghost sm" href="#/verify">Verify \u2192</a>' :
              '<span class="aw-tag rev">\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25</span>') + '</span></div>';
        }).join("") + '</div></div>' +
      '<div><div class="pt-ch"><h4>\u0e15\u0e23\u0e32\u0e17\u0e35\u0e48\u0e42\u0e1a\u0e23\u0e01\u0e19\u0e35\u0e49\u0e19\u0e33\u0e44\u0e1b\u0e41\u0e2a\u0e14\u0e07\u0e44\u0e14\u0e49</h4>' +
        '<div class="bdg-wrap">' + awBadge(320, 100, {cat: "Forex / CFD", st: AW_STMAX}) + '</div>' +
        '<p class="bdg-lb">320 \u00d7 100 \u00b7 \u0e02\u0e19\u0e32\u0e14\u0e21\u0e32\u0e15\u0e23\u0e10\u0e32\u0e19</p>' +
        '<p style="margin:18px 0 0;font-size:12px;line-height:1.75;color:#71717A">' +
        '\u0e15\u0e23\u0e32\u0e17\u0e38\u0e01\u0e02\u0e19\u0e32\u0e14\u0e25\u0e34\u0e07\u0e01\u0e4c\u0e01\u0e25\u0e31\u0e1a\u0e21\u0e32\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e40\u0e2a\u0e21\u0e2d ' +
        '\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e14\u0e32\u0e27\u0e19\u0e4c\u0e42\u0e2b\u0e25\u0e14\u0e44\u0e14\u0e49\u0e08\u0e32\u0e01 Partner Dashboard</p></div></div>';
  }
  paintLogos();
})();

/* \u2500\u2500 PAGE 5 \u2014 /partner/dashboard \u2500\u2500 */
var PT_NAV = [["ov", "Overview"], ["aw", "My Awards"], ["ct", "Certificates"],
              ["dl", "Downloads"], ["an", "Analytics"]];
var PT_KPI = [["Awards Won", "4", "\u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48\u0e1b\u0e35 2022", ""],
  ["Badge Views", "1,284,910", "+18.4% \u0e08\u0e32\u0e01\u0e40\u0e14\u0e37\u0e2d\u0e19\u0e01\u0e48\u0e2d\u0e19", "up"],
  ["Clicks", "42,617", "+11.2% \u0e08\u0e32\u0e01\u0e40\u0e14\u0e37\u0e2d\u0e19\u0e01\u0e48\u0e2d\u0e19", "up"],
  ["CTR", "3.32%", "\u0e04\u0e48\u0e32\u0e01\u0e25\u0e32\u0e07\u0e1e\u0e32\u0e23\u0e4c\u0e17\u0e40\u0e19\u0e2d\u0e23\u0e4c 2.10%", "up"]];
var PT_AWD = [
  {n: "Forex / CFD", st: 3, y: "Q2 2026", id: "RS-2026Q2-000128"},
  {n: "Forex / CFD", st: 3, y: "Q1 2026", id: "RS-2026Q1-000094"},
  {n: "Forex / CFD", st: 3, y: "Q4 2025", id: "RS-2025Q4-000061"},
  {n: "Forex / CFD", st: 2, y: "Q3 2025", id: "RS-2025Q3-000044"}
];
var PT_DAY = [58, 64, 61, 72, 88, 79, 66, 71, 84, 92, 86, 78, 90, 104, 97, 88, 95, 110, 121, 113,
              102, 116, 128, 119, 108, 122, 134, 127, 118, 131];
var PT_CO = [["\u0e44\u0e17\u0e22", 24.6], ["\u0e21\u0e32\u0e40\u0e25\u0e40\u0e0b\u0e35\u0e22", 18.1],
  ["\u0e40\u0e27\u0e35\u0e22\u0e14\u0e19\u0e32\u0e21", 14.8], ["\u0e2d\u0e34\u0e19\u0e42\u0e14\u0e19\u0e35\u0e40\u0e0b\u0e35\u0e22", 12.3],
  ["\u0e2a\u0e2b\u0e23\u0e32\u0e0a\u0e2d\u0e32\u0e13\u0e32\u0e08\u0e31\u0e01\u0e23", 9.7], ["\u0e2d\u0e37\u0e48\u0e19 \u0e46", 20.5]];
var PT_REF = [["broker-site.com/awards", 38.2], ["broker-site.com (footer)", 27.4],
  ["\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e1b\u0e34\u0e14\u0e1a\u0e31\u0e0d\u0e0a\u0e35", 16.9],
  ["\u0e2d\u0e35\u0e40\u0e21\u0e25\u0e41\u0e04\u0e21\u0e40\u0e1b\u0e0d", 10.1], ["\u0e2d\u0e37\u0e48\u0e19 \u0e46", 7.4]];
var ptTab = "ov";
function ptBars(vals, w, h){
  var mx = Math.max.apply(null, vals), bw = w / vals.length, out = "";
  for (var i = 0; i < vals.length; i++) {
    var bh = Math.max(3, vals[i] / mx * (h - 8));
    out += '<rect x="' + (i * bw + 1.5).toFixed(1) + '" y="' + (h - bh).toFixed(1) +
      '" width="' + (bw - 3).toFixed(1) + '" height="' + bh.toFixed(1) +
      '" rx="2" fill="' + (i >= vals.length - 7 ? "#B91C1C" : "#E4E4E7") + '"/>';
  }
  return '<svg width="100%" height="' + h + '" viewBox="0 0 ' + w + ' ' + h +
    '" preserveAspectRatio="none" role="img" aria-label="\u0e01\u0e23\u0e32\u0e1f\u0e41\u0e17\u0e48\u0e07\u0e23\u0e32\u0e22\u0e27\u0e31\u0e19">' + out + '</svg>';
}
function ptList(rows){
  var mx = rows[0][1];
  return '<ul class="pt-lg">' + rows.map(function(r){
    return '<li><span>' + r[0] + '</span><span class="tr"><i style="width:' +
      (r[1] / mx * 100).toFixed(1) + '%"></i></span><span class="vv">' + r[1].toFixed(1) + '%</span></li>';
  }).join("") + '</ul>';
}
function ptEmbed(a){
  var NL = String.fromCharCode(10);
  return ['&lt;a href="https://redstartrust.com/verify/' + a.id + '"',
    '   target="_blank" rel="noopener"&gt;',
    '  &lt;img src="https://cdn.redstartrust.com/badge/' + a.id + '/320x100.svg"',
    '       width="320" height="100" loading="lazy"',
    '       alt="RED STAR ' + a.n + ' ' + a.y + ' \u2014 Verified"&gt;',
    '&lt;/a&gt;'].join(NL);
}
function ptRender(){
  var m = document.getElementById("pt-main");
  if (!m) { return; }
  var h = "";
  if (ptTab === "ov") {
    h = '<div class="aw-shd" style="margin-bottom:24px"><div class="tx">' +
      '<p class="aw-cap">Overview</p><h2 class="aw-h2">\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21</h2>' +
      '<p>\u0e2a\u0e16\u0e34\u0e15\u0e34\u0e19\u0e31\u0e1a\u0e08\u0e32\u0e01\u0e15\u0e23\u0e32\u0e17\u0e35\u0e48\u0e15\u0e34\u0e14\u0e2d\u0e22\u0e39\u0e48\u0e1a\u0e19\u0e40\u0e27\u0e47\u0e1a\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13 \u0e23\u0e2d\u0e1a 30 \u0e27\u0e31\u0e19\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14</p></div></div>' +
      '<div class="pt-kpi">' + PT_KPI.map(function(k){
        return '<div class="pt-k"><span>' + k[0] + '</span><b>' + k[1] + '</b>' +
          '<i class="' + k[3] + '">' + k[2] + '</i></div>';
      }).join("") + '</div>' +
      '<div class="pt-ch" style="margin-top:16px"><h4>Daily Badge Views \u00b7 30 \u0e27\u0e31\u0e19</h4>' +
        ptBars(PT_DAY, 640, 120) + '</div>' +
      '<div class="pt-2" style="margin-top:16px">' +
        '<div class="pt-ch"><h4>Countries</h4>' + ptList(PT_CO) + '</div>' +
        '<div class="pt-ch"><h4>Top Referrers</h4>' + ptList(PT_REF) + '</div></div>';
  } else if (ptTab === "aw" || ptTab === "ct") {
    h = '<div class="aw-shd" style="margin-bottom:24px"><div class="tx">' +
      '<p class="aw-cap">' + (ptTab === "aw" ? "My Awards" : "Certificates") + '</p>' +
      '<h2 class="aw-h2">' + (ptTab === "aw" ? "\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13" : "\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14") + '</h2>' +
      '<p>\u0e14\u0e32\u0e27\u0e19\u0e4c\u0e42\u0e2b\u0e25\u0e14\u0e15\u0e23\u0e32 \u0e04\u0e31\u0e14\u0e25\u0e2d\u0e01\u0e42\u0e04\u0e49\u0e14\u0e1d\u0e31\u0e07 \u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e1b\u0e34\u0e14\u0e2b\u0e19\u0e49\u0e32\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07\u0e17\u0e35\u0e48\u0e04\u0e19\u0e17\u0e31\u0e48\u0e27\u0e44\u0e1b\u0e40\u0e2b\u0e47\u0e19</p></div></div>' +
      PT_AWD.map(function(a, i){
        return '<div class="pt-awd"><div>' + awBadge(320, 100, {cat: a.n, st: a.st, per: a.y, cid: a.id}) + '</div>' +
          '<div class="pt-at"><h4>RED STAR \u00b7 ' + a.n + ' ' + a.y + '</h4>' +
          '<div style="margin:2px 0 6px">' + awStarRow(a.st, 15) + '</div>' +
          '<span class="aw-mono">' + a.id + '</span>' +
          '<div class="pt-abt">' +
            '<button type="button" class="aw-btn out sm" data-ptdl="PNG">Download PNG</button>' +
            '<button type="button" class="aw-btn out sm" data-ptdl="SVG">Download SVG</button>' +
            '<button type="button" class="aw-btn out sm" data-ptcp="' + i + '">Copy Embed Code</button>' +
            '<a class="aw-btn ghost sm" href="#/verify">View Certificate \u2192</a></div>' +
          '<pre class="pt-emb">' + ptEmbed(a) + '</pre></div></div>';
      }).join("");
  } else if (ptTab === "dl") {
    h = '<div class="aw-shd" style="margin-bottom:24px"><div class="tx">' +
      '<p class="aw-cap">Downloads</p><h2 class="aw-h2">\u0e15\u0e23\u0e32\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25 4 \u0e02\u0e19\u0e32\u0e14</h2>' +
      '<p>\u0e17\u0e38\u0e01\u0e02\u0e19\u0e32\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e27\u0e01\u0e40\u0e15\u0e2d\u0e23\u0e4c \u0e04\u0e21\u0e17\u0e38\u0e01\u0e02\u0e19\u0e32\u0e14 \u0e41\u0e25\u0e30\u0e1d\u0e31\u0e07\u0e40\u0e25\u0e02\u0e43\u0e1a\u0e23\u0e31\u0e1a\u0e23\u0e2d\u0e07\u0e44\u0e27\u0e49\u0e43\u0e19\u0e15\u0e31\u0e27\u0e15\u0e23\u0e32</p></div></div>' +
      '<div class="pt-ch"><h4>Horizontal</h4><div class="bdg-wrap">' +
        '<div>' + awBadge(320, 100, {}) + '<p class="bdg-lb">320 \u00d7 100</p></div>' +
        '<div>' + awBadge(240, 75, {}) + '<p class="bdg-lb">240 \u00d7 75</p></div>' +
        '<div>' + awBadge(180, 56, {}) + '<p class="bdg-lb">180 \u00d7 56</p></div></div></div>' +
      '<div class="pt-ch" style="margin-top:16px"><h4>Square \u00b7 \u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e42\u0e0b\u0e40\u0e0a\u0e35\u0e22\u0e25\u0e41\u0e25\u0e30\u0e2d\u0e35\u0e40\u0e21\u0e25</h4>' +
        '<div class="bdg-wrap"><div style="width:256px">' +
        awBadge(512, 512, {}).replace('width="512" height="512"', 'width="256" height="256"') +
        '<p class="bdg-lb">512 \u00d7 512</p></div>' +
        '<div style="flex:1;min-width:0"><p style="margin:0 0 14px;font-size:12.5px;line-height:1.8;color:#3F3F46">' +
        '<b>\u0e01\u0e0e\u0e01\u0e32\u0e23\u0e43\u0e0a\u0e49\u0e15\u0e23\u0e32</b><br>' +
        '\u2022 \u0e2b\u0e49\u0e32\u0e21\u0e15\u0e31\u0e14\u0e2a\u0e48\u0e27\u0e19 \u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e2a\u0e35 \u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e43\u0e19\u0e15\u0e23\u0e32<br>' +
        '\u2022 \u0e15\u0e49\u0e2d\u0e07\u0e25\u0e34\u0e07\u0e01\u0e4c\u0e01\u0e25\u0e31\u0e1a\u0e21\u0e32\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e40\u0e2a\u0e21\u0e2d<br>' +
        '\u2022 \u0e43\u0e0a\u0e49\u0e44\u0e14\u0e49\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e1b\u0e35\u0e17\u0e35\u0e48\u0e23\u0e30\u0e1a\u0e38\u0e1a\u0e19\u0e15\u0e23\u0e32<br>' +
        '\u2022 \u0e16\u0e49\u0e32\u0e23\u0e32\u0e07\u0e27\u0e31\u0e25\u0e16\u0e39\u0e01\u0e40\u0e1e\u0e34\u0e01\u0e16\u0e2d\u0e19 \u0e15\u0e23\u0e32\u0e08\u0e30\u0e2b\u0e21\u0e14\u0e2d\u0e32\u0e22\u0e38\u0e17\u0e31\u0e19\u0e17\u0e35\u0e41\u0e25\u0e30\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e23\u0e27\u0e08\u0e08\u0e30\u0e02\u0e36\u0e49\u0e19\u0e27\u0e48\u0e32\u0e40\u0e1e\u0e34\u0e01\u0e16\u0e2d\u0e19</p>' +
        '<button type="button" class="aw-btn pri sm" data-ptdl="\u0e0a\u0e38\u0e14\u0e15\u0e23\u0e32\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14 (ZIP)">' +
        '\u0e14\u0e32\u0e27\u0e19\u0e4c\u0e42\u0e2b\u0e25\u0e14\u0e0a\u0e38\u0e14\u0e15\u0e23\u0e32\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14</button></div></div></div>';
  } else {
    h = '<div class="aw-shd" style="margin-bottom:24px"><div class="tx">' +
      '<p class="aw-cap">Analytics</p><h2 class="aw-h2">\u0e2a\u0e16\u0e34\u0e15\u0e34\u0e01\u0e32\u0e23\u0e41\u0e2a\u0e14\u0e07\u0e1c\u0e25</h2>' +
      '<p>\u0e19\u0e31\u0e1a\u0e08\u0e32\u0e01\u0e15\u0e23\u0e32\u0e17\u0e35\u0e48\u0e42\u0e2b\u0e25\u0e14\u0e08\u0e32\u0e01 CDN \u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19 \u0e44\u0e21\u0e48\u0e40\u0e01\u0e47\u0e1a\u0e04\u0e38\u0e01\u0e01\u0e35\u0e49\u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e23\u0e30\u0e1a\u0e38\u0e15\u0e31\u0e27\u0e15\u0e19\u0e1c\u0e39\u0e49\u0e40\u0e02\u0e49\u0e32\u0e0a\u0e21</p></div></div>' +
      '<div class="pt-ch"><h4>Daily Badge Views \u00b7 30 \u0e27\u0e31\u0e19 (\u0e1e\u0e31\u0e19\u0e04\u0e23\u0e31\u0e49\u0e07)</h4>' +
        ptBars(PT_DAY, 640, 150) + '</div>' +
      '<div class="pt-ch" style="margin-top:16px"><h4>Clicks \u00b7 30 \u0e27\u0e31\u0e19</h4>' +
        ptBars(PT_DAY.map(function(v, i){ return Math.round(v * (0.31 + (i % 5) * 0.012)); }), 640, 110) + '</div>' +
      '<div class="pt-2" style="margin-top:16px">' +
        '<div class="pt-ch"><h4>Countries</h4>' + ptList(PT_CO) + '</div>' +
        '<div class="pt-ch"><h4>Top Referrers</h4>' + ptList(PT_REF) + '</div></div>';
  }
  m.innerHTML = h + '<div style="margin-top:26px;padding-bottom:80px">' +
    awDemo("\u0e2a\u0e16\u0e34\u0e15\u0e34\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19 <b>\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e21\u0e21\u0e15\u0e34</b> \u0e1b\u0e38\u0e48\u0e21\u0e14\u0e32\u0e27\u0e19\u0e4c\u0e42\u0e2b\u0e25\u0e14\u0e41\u0e25\u0e30\u0e04\u0e31\u0e14\u0e25\u0e2d\u0e01\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e15\u0e48\u0e2d\u0e23\u0e30\u0e1a\u0e1a\u0e08\u0e23\u0e34\u0e07") +
    '</div>';
}
(function(){
  var s = document.getElementById("pt-side");
  if (!s) { return; }
  s.innerHTML = '<div class="who"><b>' + awName(AW_WIN[0].b) + '</b>' +
    '<span>Partner \u00b7 \u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e15\u0e31\u0e27\u0e15\u0e19\u0e41\u0e25\u0e49\u0e27</span></div>' +
    PT_NAV.map(function(n){
      return '<button type="button" class="pt-nav" data-pttab="' + n[0] + '" aria-current="' +
        (n[0] === ptTab) + '">' + n[1] + '</button>';
    }).join("");
  ptRender();
})();
document.addEventListener("click", function(ev){
  var t = ev.target.closest("[data-pttab]");
  if (t) {
    ptTab = t.dataset.pttab;
    document.querySelectorAll("[data-pttab]").forEach(function(b){
      b.setAttribute("aria-current", String(b === t));
    });
    ptRender();
    return;
  }
  var c = ev.target.closest("[data-ptcp]");
  if (c) {
    var a = PT_AWD[parseInt(c.dataset.ptcp, 10)];
    var txt = ptEmbed(a).replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"');
    if (navigator.clipboard) { navigator.clipboard.writeText(txt).catch(function(){}); }
    c.textContent = "\u0e04\u0e31\u0e14\u0e25\u0e2d\u0e01\u0e41\u0e25\u0e49\u0e27";
    setTimeout(function(){ c.textContent = "Copy Embed Code"; }, 1800);
    awToast("\u0e04\u0e31\u0e14\u0e25\u0e2d\u0e01\u0e42\u0e04\u0e49\u0e14\u0e1d\u0e31\u0e07\u0e41\u0e25\u0e49\u0e27");
    return;
  }
  var d = ev.target.closest("[data-ptdl]");
  if (d) {
    awToast("\u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e22\u0e31\u0e07\u0e14\u0e32\u0e27\u0e19\u0e4c\u0e42\u0e2b\u0e25\u0e14\u0e08\u0e23\u0e34\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 \u2014 \u0e1b\u0e38\u0e48\u0e21 " + d.dataset.ptdl);
    return;
  }
  var v = ev.target.closest("[data-awverify]");
  if (v) { awToast("\u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e21\u0e35\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e40\u0e14\u0e35\u0e22\u0e27 \u2014 " + v.dataset.awverify); return; }
  var r = ev.target.closest("[data-awrow]");
  if (r && !ev.target.closest("a")) { showPage("brokerawards"); }
});
function awToast(msg){
  var t = document.getElementById("aw-toast");
  if (!t) {
    t = document.createElement("div");
    t.id = "aw-toast";
    t.className = "pt-toast";
    t.setAttribute("role", "status");
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.classList.add("on");
  clearTimeout(t._h);
  t._h = setTimeout(function(){ t.classList.remove("on"); }, 2400);
}
/* \u0e2b\u0e25\u0e2d\u0e14\u0e04\u0e30\u0e41\u0e19\u0e19\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32 Verify \u0e27\u0e34\u0e48\u0e07\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e02\u0e49\u0e32\u0e2a\u0e32\u0e22\u0e15\u0e32 */
function awBarsGo(){
  document.querySelectorAll("[data-vfbar]").forEach(function(b){
    b.style.width = "0";
    setTimeout(function(){ b.style.width = b.dataset.vfbar + "%"; }, 60);
  });
}

/* \u2500\u2500 \u0e2b\u0e19\u0e49\u0e32\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e01\u0e32\u0e23\u0e43\u0e2b\u0e49\u0e14\u0e32\u0e27 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
   \u0e02\u0e49\u0e2d\u0e40\u0e2a\u0e19\u0e2d\u0e02\u0e2d\u0e07 Noting \u2014 GCSI \u0e21\u0e35\u0e01\u0e0e\u0e41\u0e25\u0e49\u0e27\u0e27\u0e48\u0e32 "\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a 3,000 \u0e02\u0e49\u0e2d = \u0e44\u0e14\u0e49\u0e14\u0e32\u0e27"
   \u0e41\u0e15\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e19\u0e34\u0e22\u0e32\u0e21\u0e02\u0e2d\u0e07\u0e14\u0e32\u0e27\u0e14\u0e27\u0e07\u0e17\u0e35\u0e48 2 \u0e41\u0e25\u0e30 3 \u0e2a\u0e48\u0e27\u0e19\u0e19\u0e35\u0e49\u0e08\u0e36\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e48\u0e27\u0e19\u0e17\u0e35\u0e48\u0e40\u0e2a\u0e19\u0e2d\u0e40\u0e1e\u0e34\u0e48\u0e21     */
var CR_LV = [
  {n: 1, t: "\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32\u0e15\u0e23\u0e10\u0e32\u0e19", en: "Qualified", need: "\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a 3,000 \u0e02\u0e49\u0e2d \u0e43\u0e19\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e19\u0e35\u0e49",
   lead: "\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c<b>\u0e1c\u0e48\u0e32\u0e19\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08\u0e04\u0e23\u0e1a\u0e17\u0e31\u0e49\u0e07 3,000 \u0e02\u0e49\u0e2d</b>\u0e43\u0e19\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e44\u0e2b\u0e19\u0e44\u0e21\u0e48\u0e1c\u0e48\u0e32\u0e19 \u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e44\u0e2b\u0e19\u0e04\u0e49\u0e32\u0e07\u0e2a\u0e16\u0e32\u0e19\u0e30\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e23\u0e27\u0e08",
   li: [["\u0e1c\u0e48\u0e32\u0e19 <b>3,000 / 3,000 \u0e02\u0e49\u0e2d</b> \u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e22\u0e01\u0e40\u0e27\u0e49\u0e19", 0],
        ["\u0e15\u0e23\u0e27\u0e08\u0e04\u0e23\u0e1a\u0e17\u0e38\u0e01\u0e02\u0e49\u0e2d\u0e08\u0e23\u0e34\u0e07 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e04\u0e49\u0e32\u0e07\u0e2a\u0e16\u0e32\u0e19\u0e30 <b>\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e23\u0e27\u0e08</b>", 0],
        ["\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e17\u0e38\u0e01\u0e02\u0e49\u0e2d\u0e40\u0e01\u0e47\u0e1a\u0e43\u0e19\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e19\u0e35\u0e49 <b>\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e49\u0e02\u0e2d\u0e07\u0e40\u0e01\u0e48\u0e32\u0e02\u0e49\u0e32\u0e21\u0e23\u0e2d\u0e1a</b>", 0]],
   f: "\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e2d\u0e48\u0e32\u0e19\u0e27\u0e48\u0e32", fd: "\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e1a\u0e01\u0e1e\u0e23\u0e48\u0e2d\u0e07\u0e17\u0e35\u0e48\u0e40\u0e23\u0e32\u0e15\u0e23\u0e27\u0e08\u0e40\u0e08\u0e2d\u0e43\u0e19\u0e23\u0e2d\u0e1a\u0e19\u0e35\u0e49"},
  {n: 2, t: "\u0e1c\u0e48\u0e32\u0e19\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07", en: "Consistent", need: "\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19 3 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a",
   lead: "\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a 3,000 \u0e02\u0e49\u0e2d <b>\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19 3 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a</b> \u0e42\u0e14\u0e22\u0e44\u0e21\u0e48\u0e02\u0e32\u0e14\u0e0a\u0e48\u0e27\u0e07 \u2014 \u0e27\u0e31\u0e14\u0e27\u0e48\u0e32\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e1a\u0e31\u0e07\u0e40\u0e2d\u0e34\u0e0d\u0e02\u0e2d\u0e07\u0e23\u0e2d\u0e1a\u0e40\u0e14\u0e35\u0e22\u0e27",
   li: [["\u0e44\u0e14\u0e49\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02 <b>1 \u0e14\u0e32\u0e27</b> \u0e04\u0e23\u0e1a\u0e17\u0e38\u0e01\u0e02\u0e49\u0e2d", 0],
        ["\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19 <b>3 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14</b> \u0e44\u0e21\u0e48\u0e02\u0e32\u0e14\u0e41\u0e21\u0e49\u0e23\u0e2d\u0e1a\u0e40\u0e14\u0e35\u0e22\u0e27", 0],
        ["\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e43\u0e19 Broker Alerts \u0e17\u0e35\u0e48<b>\u0e40\u0e25\u0e22\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e15\u0e2d\u0e1a</b>\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e31\u0e49\u0e19", 1]],
   f: "\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e2d\u0e48\u0e32\u0e19\u0e27\u0e48\u0e32", fd: "\u0e23\u0e31\u0e01\u0e29\u0e32\u0e21\u0e32\u0e15\u0e23\u0e10\u0e32\u0e19\u0e44\u0e14\u0e49\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07\u0e40\u0e01\u0e37\u0e2d\u0e1a\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e1b\u0e35"},
  {n: 3, t: "\u0e17\u0e23\u0e07\u0e04\u0e38\u0e13\u0e04\u0e48\u0e32", en: "Distinguished", need: "\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19 6 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a + \u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e23\u0e30\u0e1e\u0e24\u0e15\u0e34",
   lead: "\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a 3,000 \u0e02\u0e49\u0e2d <b>\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19 6 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a (\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e1b\u0e35\u0e04\u0e23\u0e36\u0e48\u0e07)</b> \u0e41\u0e25\u0e30\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e23\u0e30\u0e1e\u0e24\u0e15\u0e34\u0e17\u0e31\u0e49\u0e07 4 \u0e02\u0e49\u0e2d \u2014 \u0e19\u0e35\u0e48\u0e04\u0e37\u0e2d\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e17\u0e35\u0e48\u0e0b\u0e37\u0e49\u0e2d\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e0b\u0e37\u0e49\u0e2d\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49",
   li: [["\u0e44\u0e14\u0e49\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02 <b>2 \u0e14\u0e32\u0e27</b> \u0e04\u0e23\u0e1a\u0e17\u0e38\u0e01\u0e02\u0e49\u0e2d", 0],
        ["\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19 <b>6 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14</b>", 0],
        ["\u0e1c\u0e48\u0e32\u0e19<b>\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e23\u0e30\u0e1e\u0e24\u0e15\u0e34\u0e04\u0e23\u0e1a\u0e17\u0e31\u0e49\u0e07 4 \u0e02\u0e49\u0e2d</b> (\u0e14\u0e39\u0e15\u0e32\u0e23\u0e32\u0e07\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07)", 1],
        ["<b>\u0e44\u0e21\u0e48\u0e40\u0e04\u0e22\u0e16\u0e39\u0e01\u0e16\u0e2d\u0e19\u0e14\u0e32\u0e27</b>\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07 6 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e19\u0e31\u0e49\u0e19", 1]],
   f: "\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e2d\u0e48\u0e32\u0e19\u0e27\u0e48\u0e32", fd: "\u0e1c\u0e48\u0e32\u0e19\u0e17\u0e38\u0e01\u0e23\u0e2d\u0e1a\u0e21\u0e32\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e1b\u0e35\u0e04\u0e23\u0e36\u0e48\u0e07 \u0e41\u0e25\u0e30\u0e1b\u0e0f\u0e34\u0e1a\u0e31\u0e15\u0e34\u0e15\u0e48\u0e2d\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e14\u0e35\u0e15\u0e25\u0e2d\u0e14\u0e17\u0e32\u0e07"}
];
var CR_PATH = [
  {q: "Q3 2024", st: 1, run: 1, s: "\u0e40\u0e23\u0e34\u0e48\u0e21\u0e2a\u0e15\u0e23\u0e35\u0e04"},
  {q: "Q4 2024", st: 0, run: 0, s: "\u0e2b\u0e25\u0e38\u0e14 \u2014 \u0e2a\u0e15\u0e23\u0e35\u0e04\u0e40\u0e23\u0e34\u0e48\u0e21\u0e19\u0e31\u0e1a\u0e43\u0e2b\u0e21\u0e48"},
  {q: "Q1 2025", st: 1, run: 1, s: "\u0e01\u0e25\u0e31\u0e1a\u0e21\u0e32\u0e1c\u0e48\u0e32\u0e19"},
  {q: "Q2 2025", st: 1, run: 2, s: "\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e04\u0e23\u0e1a 3 \u0e23\u0e2d\u0e1a"},
  {q: "Q3 2025", st: 2, run: 3, s: "\u0e04\u0e23\u0e1a 3 \u0e23\u0e2d\u0e1a \u2192 2 \u0e14\u0e32\u0e27"},
  {q: "Q4 2025", st: 2, run: 4, s: "\u0e04\u0e07\u0e23\u0e30\u0e14\u0e31\u0e1a"},
  {q: "Q1 2026", st: 2, run: 5, s: "\u0e04\u0e07\u0e23\u0e30\u0e14\u0e31\u0e1a"},
  {q: "Q2 2026", st: 3, run: 6, s: "\u0e04\u0e23\u0e1a 6 \u0e23\u0e2d\u0e1a \u2192 3 \u0e14\u0e32\u0e27"}
];
var CR_CONDUCT = [
  ["C1", "\u0e15\u0e2d\u0e1a\u0e17\u0e38\u0e01\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e43\u0e19\u0e01\u0e33\u0e2b\u0e19\u0e14",
   "\u0e17\u0e38\u0e01\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e17\u0e35\u0e48\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e41\u0e08\u0e49\u0e07\u0e43\u0e19 Broker Alerts \u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e01\u0e14\u0e23\u0e31\u0e1a\u0e17\u0e23\u0e32\u0e1a\u0e41\u0e25\u0e30\u0e15\u0e2d\u0e1a\u0e20\u0e32\u0e22\u0e43\u0e19\u0e01\u0e33\u0e2b\u0e19\u0e14 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e43\u0e14\u0e40\u0e25\u0e22\u0e01\u0e33\u0e2b\u0e19\u0e14"],
  ["C2", "\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e1e\u0e34\u0e1e\u0e32\u0e17\u0e17\u0e35\u0e48\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e27\u0e48\u0e32\u0e42\u0e1a\u0e23\u0e01\u0e1c\u0e34\u0e14",
   "\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e1e\u0e34\u0e1e\u0e32\u0e17\u0e17\u0e35\u0e48\u0e1b\u0e34\u0e14\u0e14\u0e49\u0e27\u0e22\u0e02\u0e49\u0e2d\u0e2a\u0e23\u0e38\u0e1b\u0e27\u0e48\u0e32\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e1c\u0e34\u0e14 \u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07 6 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e17\u0e35\u0e48\u0e19\u0e31\u0e1a\u0e2a\u0e15\u0e23\u0e35\u0e04"],
  ["C3", "\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e15\u0e23\u0e07\u0e01\u0e31\u0e1a\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19",
   "\u0e04\u0e33\u0e0a\u0e35\u0e49\u0e41\u0e08\u0e07\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e07\u0e40\u0e02\u0e49\u0e32\u0e21\u0e32\u0e44\u0e21\u0e48\u0e02\u0e31\u0e14\u0e01\u0e31\u0e1a\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e17\u0e35\u0e48\u0e17\u0e35\u0e21\u0e15\u0e23\u0e27\u0e08\u0e16\u0e37\u0e2d\u0e2d\u0e22\u0e39\u0e48 \u0e16\u0e49\u0e32\u0e1e\u0e1a\u0e27\u0e48\u0e32\u0e02\u0e31\u0e14 \u0e08\u0e30\u0e16\u0e37\u0e2d\u0e27\u0e48\u0e32\u0e44\u0e21\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e17\u0e31\u0e19\u0e17\u0e35\u0e41\u0e25\u0e30\u0e2a\u0e15\u0e23\u0e35\u0e04\u0e02\u0e32\u0e14"],
  ["C4", "\u0e44\u0e21\u0e48\u0e1b\u0e23\u0e32\u0e01\u0e0f\u0e43\u0e19 warning list",
   "\u0e44\u0e21\u0e48\u0e1b\u0e23\u0e32\u0e01\u0e0f\u0e43\u0e19\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e02\u0e2d\u0e07\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e01\u0e33\u0e01\u0e31\u0e1a\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e2b\u0e25\u0e31\u0e01\u0e43\u0e14 \u0e46 \u0e15\u0e25\u0e2d\u0e14\u0e0a\u0e48\u0e27\u0e07\u0e17\u0e35\u0e48\u0e19\u0e31\u0e1a\u0e2a\u0e15\u0e23\u0e35\u0e04"]
];
var CR_PIL = [
  ["P01", "\u0e43\u0e1a\u0e2d\u0e19\u0e38\u0e0d\u0e32\u0e15\u0e41\u0e25\u0e30\u0e15\u0e31\u0e27\u0e15\u0e19\u0e19\u0e34\u0e15\u0e34\u0e1a\u0e38\u0e04\u0e04\u0e25", "300 \u0e02\u0e49\u0e2d"],
  ["P02", "\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22\u0e02\u0e2d\u0e07\u0e40\u0e07\u0e34\u0e19\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32", "300 \u0e02\u0e49\u0e2d"],
  ["P03", "\u0e01\u0e32\u0e23\u0e1d\u0e32\u0e01\u2013\u0e16\u0e2d\u0e19\u0e40\u0e07\u0e34\u0e19\u0e08\u0e23\u0e34\u0e07", "300 \u0e02\u0e49\u0e2d"],
  ["P04", "\u0e04\u0e27\u0e32\u0e21\u0e42\u0e1b\u0e23\u0e48\u0e07\u0e43\u0e2a\u0e02\u0e2d\u0e07\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19", "300 \u0e02\u0e49\u0e2d"],
  ["P05", "\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e01\u0e32\u0e23\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07", "300 \u0e02\u0e49\u0e2d"],
  ["P06", "\u0e41\u0e1e\u0e25\u0e15\u0e1f\u0e2d\u0e23\u0e4c\u0e21\u0e41\u0e25\u0e30\u0e40\u0e2a\u0e16\u0e35\u0e22\u0e23\u0e20\u0e32\u0e1e", "300 \u0e02\u0e49\u0e2d"],
  ["P07", "\u0e04\u0e27\u0e32\u0e21\u0e40\u0e1b\u0e47\u0e19\u0e18\u0e23\u0e23\u0e21\u0e02\u0e2d\u0e07\u0e2a\u0e31\u0e0d\u0e0d\u0e32", "300 \u0e02\u0e49\u0e2d"],
  ["P08", "\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e41\u0e25\u0e30\u0e02\u0e49\u0e2d\u0e23\u0e49\u0e2d\u0e07\u0e40\u0e23\u0e35\u0e22\u0e19", "300 \u0e02\u0e49\u0e2d"],
  ["P09", "\u0e01\u0e32\u0e23\u0e15\u0e25\u0e32\u0e14\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e34\u0e14\u0e40\u0e1c\u0e22\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07", "300 \u0e02\u0e49\u0e2d"],
  ["P10", "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e48\u0e27\u0e19\u0e1a\u0e38\u0e04\u0e04\u0e25\u0e41\u0e25\u0e30\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22", "300 \u0e02\u0e49\u0e2d"]
];
var CR_REVOKE = [
  ["1", "\u0e44\u0e21\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e41\u0e21\u0e49\u0e02\u0e49\u0e2d\u0e40\u0e14\u0e35\u0e22\u0e27\u0e43\u0e19\u0e23\u0e2d\u0e1a\u0e43\u0e2b\u0e21\u0e48",
   "<b>\u0e14\u0e32\u0e27\u0e2b\u0e32\u0e22\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e17\u0e31\u0e19\u0e17\u0e35</b> \u0e01\u0e25\u0e31\u0e1a\u0e44\u0e1b\u0e40\u0e1b\u0e47\u0e19 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e14\u0e32\u0e27 \u0e41\u0e25\u0e30\u0e2a\u0e15\u0e23\u0e35\u0e04\u0e40\u0e23\u0e34\u0e48\u0e21\u0e19\u0e31\u0e1a\u0e43\u0e2b\u0e21\u0e48\u0e08\u0e32\u0e01\u0e28\u0e39\u0e19\u0e22\u0e4c \u2014 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e25\u0e14\u0e17\u0e35\u0e25\u0e30\u0e14\u0e27\u0e07"],
  ["2", "\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a\u0e41\u0e15\u0e48\u0e2a\u0e15\u0e23\u0e35\u0e04\u0e02\u0e32\u0e14\u0e44\u0e1b\u0e01\u0e48\u0e2d\u0e19\u0e2b\u0e19\u0e49\u0e32",
   "\u0e44\u0e14\u0e49 <b>1 \u0e14\u0e32\u0e27</b> \u0e15\u0e32\u0e21\u0e23\u0e2d\u0e1a\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19 \u0e41\u0e25\u0e49\u0e27\u0e44\u0e15\u0e48\u0e02\u0e36\u0e49\u0e19\u0e43\u0e2b\u0e21\u0e48\u0e15\u0e32\u0e21\u0e08\u0e33\u0e19\u0e27\u0e19\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e15\u0e34\u0e14\u0e01\u0e31\u0e19"],
  ["3", "\u0e1c\u0e34\u0e14\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e23\u0e30\u0e1e\u0e24\u0e15\u0e34\u0e02\u0e49\u0e2d\u0e43\u0e14\u0e02\u0e49\u0e2d\u0e2b\u0e19\u0e36\u0e48\u0e07",
   "\u0e25\u0e14\u0e08\u0e32\u0e01 3 \u0e14\u0e32\u0e27\u0e40\u0e2b\u0e25\u0e37\u0e2d <b>2 \u0e14\u0e32\u0e27</b> \u0e17\u0e31\u0e19\u0e17\u0e35 \u0e41\u0e25\u0e30\u0e01\u0e25\u0e31\u0e1a\u0e02\u0e36\u0e49\u0e19 3 \u0e14\u0e32\u0e27\u0e44\u0e14\u0e49\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e04\u0e23\u0e1a\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07"],
  ["4", "\u0e15\u0e23\u0e27\u0e08\u0e44\u0e21\u0e48\u0e04\u0e23\u0e1a\u0e43\u0e19\u0e23\u0e2d\u0e1a\u0e43\u0e2b\u0e21\u0e48",
   "\u0e41\u0e2a\u0e14\u0e07 <b>\u0e2d\u0e22\u0e39\u0e48\u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07\u0e15\u0e23\u0e27\u0e08</b> \u0e41\u0e25\u0e30\u0e22\u0e31\u0e07\u0e04\u0e07\u0e41\u0e2a\u0e14\u0e07\u0e14\u0e32\u0e27\u0e02\u0e2d\u0e07\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e01\u0e48\u0e2d\u0e19\u0e44\u0e27\u0e49\u0e08\u0e19\u0e01\u0e27\u0e48\u0e32\u0e1c\u0e25\u0e43\u0e2b\u0e21\u0e48\u0e08\u0e30\u0e2d\u0e2d\u0e01"]
];
function crTick(gold){
  return '<span class="tick"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" ' +
    'stroke="' + (gold ? "#7A5C11" : "#B91C1C") + '" stroke-width="3.4" stroke-linecap="round" ' +
    'stroke-linejoin="round" aria-hidden="true"><path d="M4.5 12.5 10 18 19.5 6.5"></path></svg></span>';
}
(function(){
  var r = document.getElementById("cr-rule");
  if (!r) { return; }
  r.className = "cr-rule";
  r.innerHTML =
    '<span class="st">' + awardStar(56) + '</span>' +
    '<div><h2>\u0e14\u0e32\u0e27\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e21\u0e32\u0e08\u0e32\u0e01\u0e04\u0e30\u0e41\u0e19\u0e19 \u0e41\u0e15\u0e48\u0e21\u0e32\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a\u0e17\u0e38\u0e01\u0e02\u0e49\u0e2d</h2>' +
    '<p>GCSI \u0e44\u0e21\u0e48\u0e21\u0e35\u0e23\u0e30\u0e1a\u0e1a\u0e16\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e40\u0e1b\u0e2d\u0e23\u0e4c\u0e40\u0e0b\u0e47\u0e19\u0e15\u0e4c \u0e17\u0e38\u0e01\u0e02\u0e49\u0e2d\u0e43\u0e19\u0e0a\u0e38\u0e14 <b>3,000 \u0e02\u0e49\u0e2d</b> ' +
    '\u0e21\u0e35\u0e2a\u0e16\u0e32\u0e19\u0e30\u0e1a\u0e31\u0e07\u0e04\u0e31\u0e1a\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e17\u0e48\u0e32\u0e01\u0e31\u0e19\u0e2b\u0e21\u0e14 <span class="hl">\u0e44\u0e21\u0e48\u0e1c\u0e48\u0e32\u0e19 1 \u0e02\u0e49\u0e2d = \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e14\u0e32\u0e27</span> ' +
    '\u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e16\u0e31\u0e27\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e22\u0e01\u0e40\u0e27\u0e49\u0e19</p>' +
    '<p>\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a\u0e41\u0e25\u0e49\u0e27 <b>\u0e14\u0e32\u0e27\u0e14\u0e27\u0e07\u0e17\u0e35\u0e48 2 \u0e41\u0e25\u0e30 3 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e21\u0e32\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32\u0e01\u0e02\u0e36\u0e49\u0e19</b> ' +
    '\u2014 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a\u0e41\u0e25\u0e49\u0e27\u0e01\u0e47\u0e04\u0e37\u0e2d\u0e04\u0e23\u0e1a \u0e44\u0e21\u0e48\u0e21\u0e35\u0e2d\u0e30\u0e44\u0e23\u0e43\u0e2b\u0e49\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19 ' +
    '\u0e14\u0e32\u0e27\u0e14\u0e27\u0e07\u0e16\u0e31\u0e14\u0e44\u0e1b\u0e08\u0e36\u0e07\u0e27\u0e31\u0e14<b>\u0e23\u0e30\u0e22\u0e30\u0e40\u0e27\u0e25\u0e32\u0e17\u0e35\u0e48\u0e23\u0e31\u0e01\u0e29\u0e32\u0e21\u0e32\u0e15\u0e23\u0e10\u0e32\u0e19\u0e44\u0e27\u0e49\u0e44\u0e14\u0e49</b> \u0e41\u0e25\u0e30<b>\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e23\u0e30\u0e1e\u0e24\u0e15\u0e34\u0e15\u0e48\u0e2d\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32</b>\u0e41\u0e17\u0e19</p>' +
    '<p>\u0e1c\u0e25\u0e04\u0e37\u0e2d\u0e14\u0e32\u0e27\u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48<b>\u0e0b\u0e37\u0e49\u0e2d\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49</b> \u2014 \u0e40\u0e07\u0e34\u0e19\u0e0b\u0e37\u0e49\u0e2d\u0e1c\u0e25\u0e15\u0e23\u0e27\u0e08\u0e23\u0e2d\u0e1a\u0e40\u0e14\u0e35\u0e22\u0e27\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e2d\u0e22\u0e39\u0e48\u0e41\u0e25\u0e49\u0e27 ' +
    '\u0e41\u0e25\u0e30\u0e0b\u0e37\u0e49\u0e2d\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e2b\u0e01\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e22\u0e34\u0e48\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49</p></div>';

  var lv = document.getElementById("cr-levels");
  if (lv) {
    lv.className = "aw-sec";
    lv.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">Star Levels</p>' +
      '<h2 class="aw-h2">\u0e14\u0e32\u0e27\u0e41\u0e15\u0e48\u0e25\u0e30\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e15\u0e49\u0e2d\u0e07\u0e1c\u0e48\u0e32\u0e19\u0e2d\u0e30\u0e44\u0e23</h2>' +
      '<p>\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e2a\u0e30\u0e2a\u0e21\u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b \u2014 \u0e14\u0e32\u0e27\u0e14\u0e27\u0e07\u0e17\u0e35\u0e48\u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32\u0e15\u0e49\u0e2d\u0e07\u0e44\u0e14\u0e49\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e02\u0e2d\u0e07\u0e14\u0e27\u0e07\u0e17\u0e35\u0e48\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e04\u0e23\u0e1a\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e2a\u0e21\u0e2d</p></div></div>' +
      '<div class="cr-lv">' + CR_LV.map(function(c){
        return '<div class="cr-c' + (c.n === 3 ? " top" : "") + '">' +
          '<div class="cr-ch">' + awStarRow(c.n, 22) +
            '<h3>' + c.t + '</h3><span>' + c.en + '</span></div>' +
          '<div class="cr-cb"><p class="lead">' + c.lead + '</p>' +
            c.li.map(function(x){
              return '<div class="cr-li' + (x[1] ? " plus" : "") + '">' + crTick(x[1]) +
                '<span>' + x[0] + '</span></div>';
            }).join("") + '</div>' +
          '<div class="cr-cf"><b>' + c.f + '</b>' + c.fd + '</div></div>';
      }).join("") + '</div>';
  }

  var pt = document.getElementById("cr-path");
  if (pt) {
    pt.className = "aw-sec";
    var mx = 3;
    pt.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">How It Builds</p>' +
      '<h2 class="aw-h2">\u0e14\u0e32\u0e27\u0e44\u0e15\u0e48\u0e02\u0e36\u0e49\u0e19\u0e41\u0e25\u0e30\u0e2b\u0e25\u0e38\u0e14\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e44\u0e23</h2>' +
      '<p>\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e40\u0e2a\u0e49\u0e19\u0e17\u0e32\u0e07\u0e08\u0e23\u0e34\u0e07\u0e02\u0e2d\u0e07\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e23\u0e32\u0e22\u0e2b\u0e19\u0e36\u0e48\u0e07 8 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u2014 \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e2a\u0e21\u0e21\u0e15\u0e34</p></div></div>' +
      '<div class="cr-path"><div class="cr-track">' + CR_PATH.map(function(p){
        var h = p.st ? (p.st / mx * 96) : 22;
        return '<div class="cr-q' + (p.st ? "" : " fail") + '">' +
          '<div class="cr-qd">' + (p.st ? awStarRow(p.st, 13) : "") +
          '<div class="cr-bar' + (p.st === 3 ? " g" : (p.st ? "" : " x")) + '" style="height:' +
          h.toFixed(0) + 'px"></div></div>' +
          '<div class="ql">' + p.q + '</div>' +
          '<span class="qs">' + p.s + '</span></div>';
      }).join("") + '</div>' +
      '<p class="cr-note"><b>\u0e2d\u0e48\u0e32\u0e19\u0e01\u0e23\u0e32\u0e1f\u0e19\u0e35\u0e49\u0e22\u0e31\u0e07\u0e44\u0e07 \u2014</b> Q4 2024 \u0e44\u0e21\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e02\u0e49\u0e2d \u0e14\u0e32\u0e27\u0e2b\u0e32\u0e22\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e41\u0e25\u0e30\u0e2a\u0e15\u0e23\u0e35\u0e04\u0e01\u0e25\u0e31\u0e1a\u0e40\u0e1b\u0e47\u0e19\u0e28\u0e39\u0e19\u0e22\u0e4c ' +
      '\u0e08\u0e32\u0e01\u0e19\u0e31\u0e49\u0e19\u0e15\u0e49\u0e2d\u0e07\u0e1c\u0e48\u0e32\u0e19\u0e43\u0e2b\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e23\u0e2d\u0e1a\u0e08\u0e36\u0e07\u0e44\u0e14\u0e49\u0e14\u0e32\u0e27\u0e17\u0e35\u0e48\u0e2a\u0e2d\u0e07 \u0e41\u0e25\u0e30\u0e2d\u0e35\u0e01\u0e2a\u0e32\u0e21\u0e23\u0e2d\u0e1a\u0e08\u0e36\u0e07\u0e44\u0e14\u0e49\u0e14\u0e32\u0e27\u0e17\u0e35\u0e48\u0e2a\u0e32\u0e21 ' +
      '\u0e23\u0e27\u0e21\u0e40\u0e27\u0e25\u0e32\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e43\u0e0a\u0e49\u0e01\u0e25\u0e31\u0e1a\u0e21\u0e32\u0e17\u0e35\u0e48 3 \u0e14\u0e32\u0e27\u0e04\u0e37\u0e2d <b>\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e1b\u0e35\u0e04\u0e23\u0e36\u0e48\u0e07</b> \u2014 \u0e23\u0e32\u0e04\u0e32\u0e02\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e1e\u0e25\u0e32\u0e14\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e02\u0e49\u0e2d\u0e08\u0e36\u0e07\u0e41\u0e1e\u0e07\u0e21\u0e32\u0e01\u0e42\u0e14\u0e22\u0e15\u0e31\u0e49\u0e07\u0e43\u0e08</p></div>';
  }

  var cd = document.getElementById("cr-conduct");
  if (cd) {
    cd.className = "aw-sec";
    cd.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">Conduct Conditions</p>' +
      '<h2 class="aw-h2">\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e23\u0e30\u0e1e\u0e24\u0e15\u0e34 4 \u0e02\u0e49\u0e2d (\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e14\u0e32\u0e27\u0e17\u0e35\u0e48 3)</h2>' +
      '<p>\u0e2a\u0e48\u0e27\u0e19\u0e19\u0e35\u0e49\u0e27\u0e31\u0e14\u0e2a\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e0a\u0e38\u0e14\u0e15\u0e23\u0e27\u0e08 3,000 \u0e02\u0e49\u0e2d\u0e27\u0e31\u0e14\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 \u2014 \u0e04\u0e37\u0e2d\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e1b\u0e0f\u0e34\u0e1a\u0e31\u0e15\u0e34\u0e15\u0e48\u0e2d\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e41\u0e25\u0e30\u0e15\u0e48\u0e2d\u0e40\u0e23\u0e32\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e44\u0e23\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e01\u0e34\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07</p></div></div>' +
      '<table class="cr-tb"><thead><tr><th>\u0e23\u0e2b\u0e31\u0e2a</th><th>\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02</th><th>\u0e23\u0e32\u0e22\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14</th></tr></thead><tbody>' +
      CR_CONDUCT.map(function(c){
        return '<tr><td class="no">' + c[0] + '</td><td><b>' + c[1] + '</b></td><td>' + c[2] + '</td></tr>';
      }).join("") + '</tbody></table>';
  }

  var pl = document.getElementById("cr-pillars");
  if (pl) {
    pl.className = "aw-sec";
    pl.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">The 3,000 Items</p>' +
      '<h2 class="aw-h2">3,000 \u0e02\u0e49\u0e2d\u0e21\u0e32\u0e08\u0e32\u0e01\u0e44\u0e2b\u0e19</h2>' +
      '<p>\u0e2a\u0e34\u0e1a\u0e40\u0e2a\u0e32 \u0e40\u0e2a\u0e32\u0e25\u0e30 300 \u0e02\u0e49\u0e2d\u0e40\u0e17\u0e48\u0e32\u0e01\u0e31\u0e19\u0e17\u0e38\u0e01\u0e40\u0e2a\u0e32 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e2a\u0e32\u0e44\u0e2b\u0e19\u0e2a\u0e33\u0e04\u0e31\u0e0d\u0e01\u0e27\u0e48\u0e32\u0e40\u0e2a\u0e32\u0e44\u0e2b\u0e19</p></div>' +
      '<span class="rt"><a class="aw-btn out" href="#/awards">\u0e01\u0e25\u0e31\u0e1a\u0e2b\u0e19\u0e49\u0e32 RED STAR</a></span></div>' +
      '<div class="cr-pil">' + CR_PIL.map(function(p){
        return '<div class="cr-p"><span class="cd">' + p[0] + '</span><b>' + p[1] + '</b>' +
          '<span>' + p[2] + '</span></div>';
      }).join("") + '</div>';
  }

  var rv = document.getElementById("cr-revoke");
  if (rv) {
    rv.className = "aw-sec";
    rv.innerHTML = '<div class="aw-shd"><div class="tx"><p class="aw-cap">Losing Stars</p>' +
      '<h2 class="aw-h2">\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e44\u0e2b\u0e23\u0e48\u0e14\u0e32\u0e27\u0e16\u0e39\u0e01\u0e16\u0e2d\u0e19</h2>' +
      '<p>\u0e17\u0e38\u0e01\u0e01\u0e23\u0e13\u0e35\u0e21\u0e35\u0e1c\u0e25\u0e17\u0e31\u0e19\u0e17\u0e35\u0e17\u0e35\u0e48\u0e1c\u0e25\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e43\u0e2b\u0e21\u0e48\u0e2d\u0e2d\u0e01 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e0a\u0e48\u0e27\u0e07\u0e1c\u0e48\u0e2d\u0e19\u0e1c\u0e31\u0e19</p></div></div>' +
      '<table class="cr-tb"><thead><tr><th>\u0e01\u0e23\u0e13\u0e35</th><th>\u0e40\u0e01\u0e34\u0e14\u0e2d\u0e30\u0e44\u0e23\u0e02\u0e36\u0e49\u0e19</th><th>\u0e1c\u0e25\u0e01\u0e31\u0e1a\u0e14\u0e32\u0e27</th></tr></thead><tbody>' +
      CR_REVOKE.map(function(c){
        return '<tr><td class="no">' + c[0] + '</td><td><b>' + c[1] + '</b></td><td>' + c[2] + '</td></tr>';
      }).join("") + '</tbody></table>';
  }

  var nt = document.getElementById("cr-note");
  if (nt) {
    nt.className = "cr-warn";
    nt.style.marginBottom = "80px";
    nt.innerHTML =
      '<span class="ic"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B54708" ' +
      'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<circle cx="12" cy="12" r="9"></circle><path d="M12 7.6V13M12 16.2v.1"></path></svg></span>' +
      '<div><b>\u0e2a\u0e16\u0e32\u0e19\u0e30\u0e02\u0e2d\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49 \u2014 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e17\u0e35\u0e48\u0e2d\u0e19\u0e38\u0e21\u0e31\u0e15\u0e34\u0e41\u0e25\u0e49\u0e27</b>' +
      '<p><b>\u0e2a\u0e48\u0e27\u0e19\u0e17\u0e35\u0e48\u0e2d\u0e19\u0e38\u0e21\u0e31\u0e15\u0e34\u0e41\u0e25\u0e49\u0e27\u0e08\u0e23\u0e34\u0e07</b> \u0e04\u0e37\u0e2d\u0e01\u0e0e\u0e17\u0e35\u0e48\u0e27\u0e48\u0e32 <code>\u0e1c\u0e48\u0e32\u0e19\u0e04\u0e23\u0e1a 3,000/3,000 \u0e02\u0e49\u0e2d = \u0e44\u0e14\u0e49\u0e14\u0e32\u0e27</code> ' +
      '\u0e41\u0e25\u0e30\u0e23\u0e2d\u0e1a\u0e15\u0e23\u0e27\u0e08\u0e43\u0e2b\u0e21\u0e48\u0e17\u0e38\u0e01\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a (GCSI \u0e09\u0e1a\u0e31\u0e1a 15 \u0e2a.\u0e04. 2569)</p>' +
      '<p><b>\u0e2a\u0e48\u0e27\u0e19\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e40\u0e2a\u0e19\u0e2d\u0e02\u0e2d\u0e07 Noting \u0e41\u0e25\u0e30\u0e22\u0e31\u0e07\u0e23\u0e2d Boss \u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19</b> \u0e04\u0e37\u0e2d\u0e19\u0e34\u0e22\u0e32\u0e21\u0e02\u0e2d\u0e07\u0e14\u0e32\u0e27\u0e14\u0e27\u0e07\u0e17\u0e35\u0e48 2 \u0e41\u0e25\u0e30 3 \u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14 ' +
      '\u2014 \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02 <code>3 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a</code> \u0e41\u0e25\u0e30 <code>6 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a</code> \u0e23\u0e27\u0e21\u0e16\u0e36\u0e07\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e23\u0e30\u0e1e\u0e24\u0e15\u0e34 C1\u2013C4 ' +
      '\u0e1c\u0e21\u0e15\u0e31\u0e49\u0e07\u0e02\u0e36\u0e49\u0e19\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e43\u0e2b\u0e49\u0e40\u0e2b\u0e47\u0e19\u0e20\u0e32\u0e1e \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e1c\u0e25\u0e43\u0e14 \u0e46</p>' +
      '<p>\u0e15\u0e32\u0e21\u0e01\u0e0e\u0e42\u0e1b\u0e23\u0e40\u0e08\u0e47\u0e04 <b>\u0e15\u0e49\u0e2d\u0e07\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e01\u0e48\u0e2d\u0e19\u0e15\u0e23\u0e27\u0e08\u0e42\u0e1a\u0e23\u0e01\u0e23\u0e32\u0e22\u0e41\u0e23\u0e01 \u0e2b\u0e49\u0e32\u0e21\u0e15\u0e31\u0e49\u0e07\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e2b\u0e25\u0e31\u0e07\u0e40\u0e2b\u0e47\u0e19\u0e1c\u0e25</b> ' +
      '\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e17\u0e35\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e40\u0e04\u0e32\u0e30\u0e2d\u0e35\u0e01 1,447 \u0e08\u0e38\u0e14\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19 <code>gcsi/PENDING-CRITERIA.md</code></p></div>';
  }
})();

var PAGE_IDS = ["home", "rating", "review", "news", "analytics", "alerts", "login", "signup",
  "brokerdash", "awards", "awards2026", "verify", "brokerawards", "partner", "criteria"];
/* \u0e2b\u0e19\u0e49\u0e32\u0e22\u0e48\u0e2d\u0e22 \u2014 \u0e40\u0e21\u0e19\u0e39\u0e2b\u0e25\u0e31\u0e01\u0e22\u0e31\u0e07\u0e15\u0e49\u0e2d\u0e07\u0e04\u0e49\u0e32\u0e07\u0e2d\u0e22\u0e39\u0e48\u0e17\u0e35\u0e48\u0e2b\u0e19\u0e49\u0e32\u0e41\u0e21\u0e48 */
var SUB_OF = {brokerdash: "alerts", awards2026: "awards", verify: "awards",
  brokerawards: "awards", partner: "awards", criteria: "awards"};
function showPage(p){
  if (PAGE_IDS.indexOf(p) < 0) { p = "home"; }
  /* ตารางอันดับ + เทียบตัวต่อตัว มีบล็อกเดียว ย้ายไปหน้าที่กำลังแสดง
     ถ้าทำสองชุด id จะซ้ำกัน แล้วสคริปต์จะวาดลงได้ที่เดียว */
  var vz = document.getElementById("vol-zones");
  if (vz) {
    var vslot = document.querySelector('[data-page="' + p + '"] [data-slot="vol"]');
    if (vslot && vz.parentNode !== vslot) { vslot.appendChild(vz); }
    vz.style.marginTop = (p === "analytics") ? "0" : "40px";
  }
  var sec = document.getElementById("rank-section");
  if (sec) {
    var slot = document.querySelector('[data-page="' + p + '"] [data-slot="rank"]');
    if (slot && sec.parentNode !== slot) { slot.appendChild(sec); }
    var head = document.getElementById("rank-head");
    if (head) { head.hidden = (p === "rating"); }
    sec.style.paddingTop = (p === "rating") ? "52px" : "96px";
  }
  document.querySelectorAll("[data-page]").forEach(function(el){ el.hidden = el.dataset.page !== p; });
  document.querySelectorAll("[data-hero]").forEach(function(el){ el.hidden = el.dataset.hero !== p; });
  var navOn = SUB_OF[p] || p;
  document.querySelectorAll(".mh-nav a[data-nav]").forEach(function(a){
    if (a.dataset.nav === navOn) { a.setAttribute("aria-current", "page"); }
    else { a.removeAttribute("aria-current"); }
  });
  if (p === "verify") { awBarsGo(); }
  window.scrollTo(0, 0);
}
function routeFromHash(){
  showPage((location.hash || "").replace(/^#\/?/, "") || "home");
}
/* ลิงก์ภายในหน้าใช้เลื่อนแทน ไม่ให้ไปชนกับตัวสลับหน้า */
document.addEventListener("click", function(ev){
  var a = ev.target.closest('a[href^="#"]');
  if (!a) { return; }
  var h = a.getAttribute("href");
  ev.preventDefault();
  if (h.indexOf("#/") === 0) {
    /* \u0e2a\u0e31\u0e48\u0e07\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e23\u0e07 \u0e46 \u0e41\u0e25\u0e49\u0e27\u0e04\u0e48\u0e2d\u0e22\u0e1e\u0e22\u0e32\u0e22\u0e32\u0e21\u0e2d\u0e31\u0e1b\u0e40\u0e14\u0e15 URL \u2014
       \u0e1a\u0e32\u0e07\u0e2a\u0e20\u0e32\u0e1e\u0e41\u0e27\u0e14\u0e25\u0e49\u0e2d\u0e21 (data: URL) \u0e40\u0e02\u0e35\u0e22\u0e19 location.hash \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 \u0e40\u0e21\u0e19\u0e39\u0e15\u0e49\u0e2d\u0e07\u0e17\u0e33\u0e07\u0e32\u0e19\u0e44\u0e14\u0e49\u0e2d\u0e22\u0e39\u0e48\u0e14\u0e35 */
    showPage(h.replace(/^#\/?/, "") || "home");
    try { if (location.hash !== h) { location.hash = h; } } catch (e) {}
    return;
  }
  if (h === "#") { return; }
  var t = document.getElementById(h.slice(1));
  if (t) { t.scrollIntoView({behavior: "smooth", block: "start"}); }
});
window.addEventListener("hashchange", routeFromHash);
routeFromHash();

</script>"""

io.open(OUT, "w", encoding="utf-8").write(HEAD + "\n\n" + PAGE + "\n")
print("wrote", OUT)
print("KB:", round(os.path.getsize(OUT) / 1024, 1))
