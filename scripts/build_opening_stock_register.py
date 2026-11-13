
"""Build the NURA Beauty Opening Stock Register (XLSX).

Run: python scripts/build_opening_stock_register.py
Needs: xlsxwriter, Pillow. Logo: assets/NURA_Beauty_Compact_Logo_Flat_Full_Colour_3000px.png
Formulas are written with cached results so phone/preview apps show the figures too.
"""
import os, sys
from PIL import Image
import xlsxwriter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(ROOT, "assets", "NURA_Beauty_Compact_Logo_Flat_Full_Colour_3000px.png")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "data", "NURA-Beauty-Opening-Stock-Register-2026-11-13.xlsx")
TMP = os.path.join(ROOT, "assets")

DOC_NO, VERSION, AS_AT = "NURA-STK-OS-2026-001", "4.1", "2026-11-13"

# product line code -> product name
NAMES = {
    "LWF": "Loose Wave Frontal", "LW44": "Loose Wave 4x4 Closure", "BSHF": "Bone Straight High Fibre",
    "BW": "Body Wave", "BOBA": "Bob Amanda", "EMP": "Empress",
    "WF": "Wonderful Frontal (new trial)", "NEG22": "2x2 Negatron Closure (new trial)",
}
# Actual cost of making each product line (KES), owner 2026-11-13: wigs made from scratch
# (bundles, ventilation, wig cap, labour). Main batch + additional costs.
COST_PARTS = {
    "LWF":   [("Main batch", 26100), ("Extra bundles", 1210), ("Colour 30 (additional)", 3210), ("Another frontal (additional)", 2300)],
    "LW44":  [("Main batch", 9615)],
    "BSHF":  [("Main batch", 11800), ("Additional", 3100)],
    "BW":    [("Main batch", 14700)],
    "BOBA":  [("Main batch", 7340)],
    "EMP":   [("Main batch", 4100)],
    "WF":    [("Additional", 1000)],
    "NEG22": [("Additional", 700)],
}
# KES 200 transport for the wig maker to collect materials for the main batch (owner, 2026-11-14).
# Shared cost of the whole batch (IAS 2 cost of purchase), allocated to the main-batch lines
# in proportion to their main-batch cost; rounding difference goes to the largest line.
TRANSPORT = 200
_main = {k: sum(a for n, a in v if n in ("Main batch", "Extra bundles")) for k, v in COST_PARTS.items()}
_mt = sum(_main.values())
_alloc = {k: round(TRANSPORT * m / _mt, 2) for k, m in _main.items() if m}
_alloc[max(_main, key=_main.get)] = round(_alloc[max(_main, key=_main.get)] + TRANSPORT - sum(_alloc.values()), 2)
for k, a in _alloc.items():
    COST_PARTS[k].append(("Transport share", a))
LINE_TOTAL = {k: round(sum(a for _, a in v), 2) for k, v in COST_PARTS.items()}
# line, colour, colour code, ordered, received, remark
ITEMS = [
    ("LWF", "Black (colour 2)", "2", 3, 3, ""),
    ("LWF", "Black (colour 1)", "1", 2, 2, ""),
    ("LWF", "Burgundy", "BUR", 3, 2, "Ordered 3, received 2; balance of 1 due from supplier."),
    ("LWF", "Colour 33", "33", 3, 4, "Ordered 3, received 4; 1 piece over-delivered."),
    ("LWF", "Red Wine", "RW", 2, 2, ""),
    ("LWF", "Colour 2/30", "2-30", 1, 1, ""),
    ("LWF", "Colour 30", "30", 2, 1, "Ordered 2, received 1; balance of 1 due from supplier."),
    ("LW44", "Colour 99J", "99J", 2, 2, ""),
    ("LW44", "Black (colour 1)", "1", 2, 2, ""),
    ("LW44", "Colour 33", "33", 2, 2, ""),
    ("BSHF", "Colour 613 (blonde)", "613", 2, 2, ""),
    ("BSHF", "Piano Dark", "PD", 2, 2, ""),
    ("BSHF", "Black", "BLK", 2, 2, ""),
    ("BW", "Piano Dark", "PD", 2, 2, ""),
    ("BW", "Colour 613 (blonde)", "613", 2, 2, ""),
    ("BW", "Black", "BLK", 2, 2, ""),
    ("BOBA", "Black", "BLK", 1, 1, ""),
    ("BOBA", "Colour 99J", "99J", 1, 1, ""),
    ("BOBA", "Colour 33", "33", 1, 1, ""),
    ("BOBA", "Colour 30", "30", 1, 1, ""),
    ("EMP", "Colour 1B", "1B", 1, 1, ""),
    ("EMP", "Colour 1/33", "1-33", 1, 1, ""),
    ("WF", "Black", "BLK", 1, 1, "New trial line."),
    ("NEG22", "Colour 1/30", "1-30", 1, 1, "New trial line."),
]

DELIVERY = [
    ("LW44", "1", 2, "4x4 closure wig, colour one"),
    ("LW44", "33", 2, "4x4 closure wig, colour 33"),
    ("LW44", "99J", 2, "4x4 closure wig, burgundy (99J in stock book)"),
    ("LWF", "RW", 2, "Red wine frontal"),
    ("LWF", "2-30", 1, "Colour 2/30 frontal"),
    ("BSHF", "BLK", 2, "Bone straight, black"),
    ("LWF", "30", 1, "Loose wave, colour 30"),
    ("LWF", "33", 4, "Loose wave frontal, colour 33"),
    ("LWF", "BUR", 2, "Loose wave frontal, burgundy"),
    ("LWF", "2", 3, "Loose wave frontal, colour two"),
    ("LWF", "1", 2, "Loose wave frontal, colour one"),
    ("BOBA", "BLK", 1, "Bob, black"),
    ("BOBA", "33", 1, "Bob, colour 33"),
    ("NEG22", "1-30", 1, "Negatron 2x2"),
]
DELIVERED = {(lc, cc): q for lc, cc, q, _ in DELIVERY}
# Weighted average cost per piece = line total / pieces in the stock book (ordered + any over-delivery)
BOOK_QTY = {lc: sum(max(o, DELIVERED.get((l2, cc), 0)) for l2, _, cc, o, _, _ in ITEMS if l2 == lc) for lc in NAMES}
LINES = {lc: (NAMES[lc], LINE_TOTAL[lc] / BOOK_QTY[lc]) for lc in NAMES}

GOLD, BLACK, INK, CREAM, ZEBRA, LINE, MUTED = "#C9972C", "#0E0E0E", "#1F1F1F", "#FBF6EA", "#FAFAFA", "#D9D9D9", "#6B6B6B"
FONT = "Calibri"

# ---------- logo: exact pixel sizes at 96 dpi so Excel never rescales it
def logo(h):
    im = Image.open(LOGO).convert("RGBA")
    im = im.crop(im.getbbox())
    w = round(im.width * h / im.height)
    p = os.path.join(TMP, f"_logo_{h}.png")
    im.resize((w, h), Image.LANCZOS).save(p, dpi=(96, 96))
    return p, w

wb = xlsxwriter.Workbook(OUT)
wb.set_properties({"title": "NURA Beauty - Opening Stock Register " + AS_AT, "author": "NURA Beauty",
                   "company": "NURA CROWN & BEAUTY", "subject": "Opening stock and valuation",
                   "keywords": "inventory, IAS 2, opening stock", "comments": DOC_NO + " v" + VERSION})
wb.set_calc_mode("auto")

def f(**k):
    base = {"font_name": FONT, "font_size": 10, "font_color": INK, "valign": "vcenter"}
    base.update(k)
    return wb.add_format(base)

band = f(bg_color=BLACK)
band_title = f(bg_color=BLACK, font_color=GOLD, bold=True, font_size=18)
band_sub = f(bg_color=BLACK, font_color="#FFFFFF", font_size=10)
band_meta = f(bg_color=BLACK, font_color="#D8C08A", font_size=9)
gold_rule = f(top=5, top_color=GOLD)
hdr = f(bold=True, font_color="#FFFFFF", bg_color=INK, align="center", text_wrap=True, border=1, border_color="#3A3A3A")
sec = f(bold=True, font_size=12, bottom=2, bottom_color=GOLD)
lab = f(bold=True, font_color=MUTED)
txt = f()
wrap = f(text_wrap=True, valign="top")
note = f(italic=True, font_size=9, font_color=MUTED)

def cell(z, **k):
    d = dict(border=1, border_color=LINE)
    if z: d["bg_color"] = ZEBRA
    d.update(k)
    return f(**d)

def header_band(ws, ncols, title, sub, logo_h, rows_pt, col_px):
    """Black band in two parts: a logo block on its own rows, then the title rows below it.
    Nothing is written beside the logo, and the logo is sized to fit its rows even if a
    viewer ignores custom row heights (default 20 px rows), so it can never cover the sheet."""
    logo_rows = 5 if logo_h > 70 else 4
    logo_h = min(logo_h, logo_rows * 20 - 12)          # fits at default row height too
    text_rows = [26, 18, 16]
    rows = [20] * logo_rows + text_rows
    for r, h in enumerate(rows):
        ws.set_row(r, h, band)
        for c in range(ncols):
            ws.write_blank(r, c, None, band)
    p, w = logo(logo_h)
    ws.insert_image(0, 0, p, {"x_offset": 12, "y_offset": 8, "object_position": 3,
                              "description": "NURA Beauty logo", "decorative": False})
    t = 0 if col_px[0] >= 40 else 1
    ws.write(logo_rows, t, title, band_title)
    ws.write(logo_rows + 1, t, sub, band_sub)
    ws.write(logo_rows + 2, t, f"Document {DOC_NO}  |  Version {VERSION}  |  As at {AS_AT}  |  Currency KES  |  UoM PCS", band_meta)
    r = len(rows)
    ws.set_row(r, 6)
    for c in range(ncols):
        ws.write_blank(r, c, None, gold_rule)
    return r + 2

def px(chars):  # Excel column width (chars) -> pixels
    return int(chars * 7 + 5)

def setup_print(ws, landscape=True, repeat=None):
    ws.set_paper(9)
    ws.set_landscape() if landscape else ws.set_portrait()
    ws.fit_to_pages(1, 0)
    ws.center_horizontally()
    ws.set_margins(left=0.4, right=0.4, top=0.7, bottom=0.6)
    ws.set_header("&R&8&K6B6B6BNURA Beauty - Opening Stock Register")
    ws.set_footer("&L&8&K6B6B6B" + DOC_NO + " v" + VERSION + " - Confidential&R&8&K6B6B6BPage &P of &N")
    if repeat is not None:
        ws.repeat_rows(*repeat)
    ws.hide_gridlines(2)

# ---------- computed values (used as cached formula results)
rows = []
for i, (lc, col, cc, o, r, rem) in enumerate(ITEMS):
    name, cost = LINES[lc]
    r = DELIVERED.get((lc, cc), 0)   # only the 2026-11-13 delivery is on the shelf
    if r == 0:
        rem = "Not yet received from supplier."
    pend, over = max(o - r, 0), max(r - o, 0)
    status = "Awaiting delivery" if r == 0 else "Part-received" if pend else ("Over-delivered" if over else "Received in full")
    rows.append(dict(n=i + 1, sku=f"NURA-{lc}-{cc}", lc=lc, name=name, col=col, cc=cc, o=o, r=r, pend=pend,
                     over=over, oh=r, cost=cost, val=r * cost, status=status, rem=rem))
T = {k: sum(x[k] for x in rows) for k in ("o", "r", "pend", "over", "oh", "val")}
T["pend_val"] = sum(x["pend"] * x["cost"] for x in rows)

# =====================================================================  STOCK REGISTER
reg = wb.add_worksheet("Stock Register")
cols = [("No.", 5), ("Item code (SKU)", 17), ("Product", 29), ("Colour", 20), ("Colour code", 9),
        ("Qty ordered", 9), ("Qty received", 9), ("Pending delivery", 9), ("Over-delivered", 9),
        ("Stock on hand", 9), ("UoM", 6), ("Unit cost (KES)", 12), ("Stock value (KES)", 14),
        ("Status", 15), ("Remarks", 44)]
for i, (_, w) in enumerate(cols):
    reg.set_column(i, i, w)
HR = header_band(reg, len(cols), "OPENING STOCK REGISTER",
                 "NURA CROWN & BEAUTY (BN-MJS7ALRV), trading as NURA Beauty  |  Stanbank House, 2nd Floor, Room 20, Nairobi CBD, Kenya",
                 64, [18, 24, 18, 18], [px(w) for _, w in cols])
reg.set_row(HR, 34)
for i, (h, _) in enumerate(cols):
    reg.write(HR, i, h, hdr)
R0 = HR + 1
for k, x in enumerate(rows):
    r = R0 + k; e = r + 1; z = k % 2
    c_ctr = cell(z, align="center"); c_l = cell(z); c_num = cell(z, align="center", num_format="#,##0")
    c_in = cell(False, bg_color="#FFF6D6", align="right", num_format="#,##0.00", locked=False)
    c_money = cell(z, align="right", num_format="#,##0.00")
    c_rem = cell(z, text_wrap=True, font_size=9)
    reg.set_row(r, 30 if x["rem"] and len(x["rem"]) > 40 else 18)
    reg.write_number(r, 0, x["n"], c_ctr)
    reg.write(r, 1, x["sku"], c_l)
    reg.write(r, 2, x["name"], c_l)
    reg.write(r, 3, x["col"], c_l)
    reg.write_string(r, 4, x["cc"], c_ctr)
    reg.write_number(r, 5, x["o"], cell(False, bg_color="#FFF6D6", align="center", num_format="#,##0", locked=False))
    reg.write_number(r, 6, x["r"], cell(False, bg_color="#FFF6D6", align="center", num_format="#,##0", locked=False))
    reg.write_formula(r, 7, f"=MAX(F{e}-G{e},0)", c_num, x["pend"])
    reg.write_formula(r, 8, f"=MAX(G{e}-F{e},0)", c_num, x["over"])
    reg.write_formula(r, 9, f"=G{e}", c_num, x["oh"])
    reg.write(r, 10, "PCS", c_ctr)
    reg.write_number(r, 11, x["cost"], c_in)
    reg.write_formula(r, 12, f"=J{e}*L{e}", c_money, x["val"])
    reg.write_formula(r, 13, f'=IF(G{e}=0,"Awaiting delivery",IF(H{e}>0,"Part-received",IF(I{e}>0,"Over-delivered","Received in full")))', c_ctr, x["status"])
    reg.write(r, 14, x["rem"], c_rem)
LAST = R0 + len(rows) - 1; TR = LAST + 1; a, b = R0 + 1, LAST + 1
tot = f(bold=True, bg_color=CREAM, top=2, top_color=GOLD, bottom=6, bottom_color=GOLD, align="center", num_format="#,##0")
tot_m = f(bold=True, bg_color=CREAM, top=2, top_color=GOLD, bottom=6, bottom_color=GOLD, align="right", num_format="#,##0.00")
tot_l = f(bold=True, bg_color=CREAM, top=2, top_color=GOLD, bottom=6, bottom_color=GOLD)
reg.set_row(TR, 22)
for c in range(len(cols)):
    reg.write_blank(TR, c, None, tot_l)
reg.write(TR, 2, "TOTAL", tot_l)
for c, key in ((5, "o"), (6, "r"), (7, "pend"), (8, "over"), (9, "oh")):
    L = chr(65 + c)
    reg.write_formula(TR, c, f"=SUBTOTAL(109,{L}{a}:{L}{b})", tot, T[key])
reg.write_formula(TR, 12, f"=SUBTOTAL(109,M{a}:M{b})", tot_m, T["val"])
reg.autofilter(HR, 0, LAST, len(cols) - 1)
reg.freeze_panes(R0, 3)
reg.conditional_format(R0, 13, LAST, 13, {"type": "formula", "criteria": f"=$H{a}>0", "format": wb.add_format({"bg_color": "#FDE7D3", "font_color": "#9C4A00", "bold": True})})
reg.conditional_format(R0, 13, LAST, 13, {"type": "formula", "criteria": f"=$I{a}>0", "format": wb.add_format({"bg_color": "#E3EEF9", "font_color": "#1F4E79", "bold": True})})
reg.conditional_format(R0, 13, LAST, 13, {"type": "formula", "criteria": f"=AND($H{a}=0,$I{a}=0)", "format": wb.add_format({"bg_color": "#E6F2E6", "font_color": "#1E6B2E"})})
reg.data_validation(R0, 5, LAST, 6, {"validate": "integer", "criteria": ">=", "value": 0, "error_title": "Quantity", "error_message": "Whole pieces only (0 or more)."})
reg.data_validation(R0, 11, LAST, 11, {"validate": "decimal", "criteria": ">=", "value": 0, "input_title": "Unit cost (KES)", "input_message": "Landed buying price per piece (IAS 2).", "error_message": "Enter 0 or more."})
n = TR + 2
reg.write(n, 0, "Light-yellow cells are inputs. Pending, over-delivered, stock on hand, value and status are calculated. Definitions and basis of preparation: see Notes.", note)
reg.write(n + 2, 0, "Counted by: ______________________", txt)
reg.write(n + 2, 4, "Checked by: ______________________", txt)
reg.write(n + 2, 11, "Approved by: ______________________", txt)
reg.write(n + 3, 0, "Date: ____________", txt); reg.write(n + 3, 4, "Date: ____________", txt); reg.write(n + 3, 11, "Date: ____________", txt)
setup_print(reg, True, (HR, HR))
reg.print_area(0, 0, n + 3, len(cols) - 1)
REG = "'Stock Register'!"

# =====================================================================  SUMMARY
s = wb.add_worksheet("Summary")
scol = [3, 30, 15, 15, 15, 15, 17, 3]
for i, w in enumerate(scol):
    s.set_column(i, i, w)
top = header_band(s, len(scol), "OPENING STOCK", "Stock-take summary and valuation", 84, [18, 30, 22, 22, 20], [px(w) for w in scol])
r = top
for k, (l, v) in enumerate([("Entity", "NURA CROWN & BEAUTY (BN-MJS7ALRV), trading as NURA Beauty"),
                            ("Location", "NURA Studio, Stanbank House, 2nd Floor, Room 20, Nairobi CBD, Kenya"),
                            ("Count date", AS_AT + " (physical count: only the 26 pieces delivered today are on the shelf)"),
                            ("Measurement basis", "Lower of cost and net realisable value (IAS 2 / IFRS for SMEs s.13); cost = landed buying price")]):
    s.write(r + k, 1, l, lab); s.write(r + k, 2, v, txt)
r += 5
kl = f(bold=True, font_size=9, font_color=MUTED, bg_color=CREAM, align="center", text_wrap=True, top=5, top_color=GOLD)
kv = f(bold=True, font_size=18, font_color=INK, bg_color=CREAM, align="center", num_format="#,##0")
kvg = f(bold=True, font_size=18, font_color=GOLD, bg_color=CREAM, align="center", num_format="#,##0")
s.set_row(r, 26); s.set_row(r + 1, 36)
kpis = [("Stock value at cost (KES)", f"={REG}M{TR+1}", T["val"], kvg),
        ("Stock on hand (pcs)", f"={REG}J{TR+1}", T["oh"], kv),
        ("Stock book total (pcs)", f"={REG}J{TR+1}+{REG}H{TR+1}", T["oh"] + T["pend"], kv),
        ("Pending delivery (pcs)", f"={REG}H{TR+1}", T["pend"], kv),
        ("Over-delivered (pcs)", f"={REG}I{TR+1}", T["over"], kv)]
for i, (l, fx, v, fm) in enumerate(kpis):
    s.write(r, 1 + i, l, kl); s.write_formula(r + 1, 1 + i, fx, fm, v)
r += 3
s.merge_range(r, 1, r, 6, "VALUATION BY PRODUCT LINE", sec); r += 1
h2 = ["Product line", "Unit cost (KES)", "Colours", "Pieces on hand", "Pending (pcs)", "Stock value (KES)"]
s.set_row(r, 30)
for i, h in enumerate(h2):
    s.write(r, 1 + i, h, hdr)
r += 1; p0 = r
for k, (lc, (name, cost)) in enumerate(LINES.items()):
    z = k % 2; rr = r + k; e = rr + 1
    its = [x for x in rows if x["lc"] == lc]
    rng = lambda L: f"{REG}${L}${a}:${L}${b}"
    s.write(rr, 1, name, cell(z))
    s.write_number(rr, 2, cost, cell(z, align="right", num_format="#,##0.00"))
    s.write_formula(rr, 3, f'=COUNTIF({rng("C")},B{e})', cell(z, align="center"), len(its))
    s.write_formula(rr, 4, f'=SUMIF({rng("C")},B{e},{rng("J")})', cell(z, align="center", num_format="#,##0"), sum(x["oh"] for x in its))
    s.write_formula(rr, 5, f'=SUMIF({rng("C")},B{e},{rng("H")})', cell(z, align="center", num_format="#,##0"), sum(x["pend"] for x in its))
    s.write_formula(rr, 6, f'=SUMIF({rng("C")},B{e},{rng("M")})', cell(z, align="right", num_format="#,##0.00"), sum(x["val"] for x in its))
pl = r + len(LINES); s.set_row(pl, 22)
s.write(pl, 1, "TOTAL", tot_l); s.write_blank(pl, 2, None, tot_l)
s.write_formula(pl, 3, f"=SUM(D{p0+1}:D{pl})", tot, len(rows))
s.write_formula(pl, 4, f"=SUM(E{p0+1}:E{pl})", tot, T["oh"])
s.write_formula(pl, 5, f"=SUM(F{p0+1}:F{pl})", tot, T["pend"])
s.write_formula(pl, 6, f"=SUM(G{p0+1}:G{pl})", tot_m, T["val"])
s.write_formula(pl + 1, 6, f"=G{pl+1}-{REG}M{TR+1}", f(font_size=8, font_color=MUTED, align="right", num_format='"Check: "#,##0.00;"Check: "-#,##0.00;"Check: OK"'), 0)
s.write(pl + 2, 1, "Stock on order (pending delivery) at cost, not included above:", lab)
s.write_formula(pl + 2, 6, f"=SUMPRODUCT({REG}H{a}:H{b},{REG}L{a}:L{b})", f(bold=True, align="right", num_format="#,##0.00"), T["pend_val"])
s.write(pl + 4, 1, "All figures on this sheet are linked to the Stock Register sheet.", note)
setup_print(s, False)

# =====================================================================  SUPPLIER VARIANCES
v = wb.add_worksheet("Supplier Variances")
vcol = [3, 17, 29, 20, 10, 10, 10, 14, 42]
for i, w in enumerate(vcol):
    v.set_column(i, i, w)
vr = header_band(v, len(vcol), "SUPPLIER DELIVERY VARIANCES", "Deliveries that did not match the order quantity", 64, [18, 24, 18, 18], [px(w) for w in vcol])
vh = ["Item code (SKU)", "Product", "Colour", "Ordered", "Received", "Variance (pcs)", "Variance at cost (KES)", "Action"]
v.set_row(vr, 30)
for i, h in enumerate(vh):
    v.write(vr, 1 + i, h, hdr)
var = [(k, x) for k, x in enumerate(rows) if x["o"] != x["r"]]
for j, (k, x) in enumerate(var):
    rr = vr + 1 + j; src = R0 + k + 1; e = rr + 1; z = j % 2
    v.set_row(rr, 30)
    v.write_formula(rr, 1, f"={REG}B{src}", cell(z), x["sku"])
    v.write_formula(rr, 2, f"={REG}C{src}", cell(z), x["name"])
    v.write_formula(rr, 3, f"={REG}D{src}", cell(z), x["col"])
    v.write_formula(rr, 4, f"={REG}F{src}", cell(z, align="center"), x["o"])
    v.write_formula(rr, 5, f"={REG}G{src}", cell(z, align="center"), x["r"])
    v.write_formula(rr, 6, f"=F{e}-E{e}", cell(z, align="center", num_format="+#,##0;-#,##0;0", bold=True, font_color="#9C4A00" if x["r"] < x["o"] else "#1F4E79"), x["r"] - x["o"])
    v.write_formula(rr, 7, f"=G{e}*{REG}L{src}", cell(z, align="right", num_format="+#,##0.00;-#,##0.00;0.00"), (x["r"] - x["o"]) * x["cost"])
    v.write(rr, 8, ("Follow up with supplier: nothing received yet." if x["r"] == 0 else "Follow up with supplier for the balance due.") if x["r"] < x["o"] else "Agree with supplier: keep and pay for the extra piece, or return it.", cell(z, text_wrap=True))
v.write(vr + 2 + len(var), 1, "Variance = received minus ordered. Negative = still due from supplier (not in stock); positive = over-delivered (in stock).", note)
setup_print(v, True, (vr, vr))


# =====================================================================  GOODS RECEIVED
g = wb.add_worksheet("Goods Received")
gcol = [3, 6, 17, 27, 18, 34, 9, 9, 10, 12, 14]
for i, w in enumerate(gcol):
    g.set_column(i, i, w)
gr = header_band(g, len(gcol), "GOODS RECEIVED NOTE", "Supplier delivery received at the studio on " + AS_AT + " (owner's list)", 64, [18, 24, 18, 18], [px(w) for w in gcol])
gh = ["No.", "Item code (SKU)", "Product", "Colour", "As written on delivery list", "Qty ordered", "Qty received", "Variance (pcs)", "Unit cost (KES)", "Value received (KES)"]
g.set_row(gr, 30)
for i, h in enumerate(gh):
    g.write(gr, 1 + i, h, hdr)
idx = {(x["lc"], x["cc"]): k for k, x in enumerate(rows)}
gv = 0
for j, (lc, cc, q, said) in enumerate(DELIVERY):
    k = idx[(lc, cc)]; x = rows[k]; rr = gr + 1 + j; e = rr + 1; src = R0 + k + 1; z = j % 2
    g.write_number(rr, 1, j + 1, cell(z, align="center"))
    g.write_formula(rr, 2, f"={REG}B{src}", cell(z), x["sku"])
    g.write_formula(rr, 3, f"={REG}C{src}", cell(z), x["name"])
    g.write_formula(rr, 4, f"={REG}D{src}", cell(z), x["col"])
    g.write(rr, 5, said, cell(z, font_size=9, italic=True))
    g.write_formula(rr, 6, f"={REG}F{src}", cell(z, align="center"), x["o"])
    g.write_number(rr, 7, q, cell(False, bg_color="#FFF6D6", align="center", num_format="#,##0"))
    g.write_formula(rr, 8, f"=H{e}-G{e}", cell(z, align="center", num_format="+#,##0;-#,##0;0"), q - x["o"])
    g.write_formula(rr, 9, f"={REG}L{src}", cell(z, align="right", num_format="#,##0.00"), x["cost"])
    g.write_formula(rr, 10, f"=H{e}*J{e}", cell(z, align="right", num_format="#,##0.00"), q * x["cost"])
    gv += q * x["cost"]
gl = gr + 1 + len(DELIVERY); ga, gb = gr + 2, gl
g.set_row(gl, 22)
for c in range(1, 11):
    g.write_blank(gl, c, None, tot_l)
g.write(gl, 3, "TOTAL RECEIVED", tot_l)
g.write_formula(gl, 6, f"=SUM(G{ga}:G{gb})", tot, sum(rows[idx[(a, b)]]["o"] for a, b, _, _ in DELIVERY))
g.write_formula(gl, 7, f"=SUM(H{ga}:H{gb})", tot, sum(q for _, _, q, _ in DELIVERY))
g.write_formula(gl, 10, f"=SUM(K{ga}:K{gb})", tot_m, gv)
g.write(gl + 2, 1, "Reconciliation to opening stock", lab)
recon = [("Received in this delivery (pcs)", f"=H{gl+1}", sum(q for _, _, q, _ in DELIVERY)),
         ("Not yet received from supplier (pcs)", f"={REG}H{TR+1}", T["pend"]),
         ("Total per stock book (pcs)", f"=H{gl+4}+H{gl+5}", T["oh"] + T["pend"])]
for i, (l, fx, val) in enumerate(recon):
    g.write(gl + 3 + i, 2, l, f(bold=(i == 2)))
    g.write_formula(gl + 3 + i, 7, fx, f(bold=(i == 2), align="center", num_format="#,##0", top=(2 if i == 2 else 0), top_color=GOLD), val)
g.write(gl + 7, 1, "Only this delivery is on the shelf: opening stock on hand = 26 pieces. Variance = received minus ordered.", note)
g.write(gl + 9, 1, "Received by: ______________________", txt); g.write(gl + 9, 5, "Checked by: ______________________", txt); g.write(gl + 9, 9, "Date: ____________", txt)
setup_print(g, True, (gr, gr))


# =====================================================================  DASHBOARD (charts)
d = wb.add_worksheet("Dashboard")
for i, w in enumerate([3, 30, 12, 12, 12, 16, 16, 3, 12, 12, 12, 12, 12, 12, 3]):
    d.set_column(i, i, w)
dr = header_band(d, 15, "STOCK DASHBOARD", "Charts of the opening stock position at cost (KES) and in pieces", 64, [18, 24, 18, 18], [px(w) for w in [3, 30, 12]])
PAL = ["#C9972C", "#0E0E0E", "#8C6A1F", "#6B6B6B", "#E0C27A", "#3D2E0E", "#A8A8A8", "#D9B860"]
# chart data table (linked to the Stock Register)
d.merge_range(dr, 1, dr, 6, "CHART DATA (linked to the Stock Register)", sec)
dh = ["Product line", "Ordered", "On shelf", "Awaiting vendor", "Value on shelf (KES)", "Value awaiting (KES)"]
d.set_row(dr + 1, 30)
for i, h in enumerate(dh):
    d.write(dr + 1, 1 + i, h, hdr)
rng = lambda L: f"{REG}${L}${a}:${L}${b}"
d0 = dr + 2
for k, (lc, (name, cost)) in enumerate(LINES.items()):
    its = [x for x in rows if x["lc"] == lc]; rr = d0 + k; e = rr + 1; z = k % 2
    d.write(rr, 1, name, cell(z))
    d.write_formula(rr, 2, f'=SUMIF({rng("C")},B{e},{rng("F")})', cell(z, align="center", num_format="#,##0"), sum(x["o"] for x in its))
    d.write_formula(rr, 3, f'=SUMIF({rng("C")},B{e},{rng("J")})', cell(z, align="center", num_format="#,##0"), sum(x["oh"] for x in its))
    d.write_formula(rr, 4, f'=SUMIF({rng("C")},B{e},{rng("H")})', cell(z, align="center", num_format="#,##0"), sum(x["pend"] for x in its))
    d.write_formula(rr, 5, f'=SUMIF({rng("C")},B{e},{rng("M")})', cell(z, align="right", num_format="#,##0"), sum(x["val"] for x in its))
    d.write_formula(rr, 6, f'=E{e}*{cost}', cell(z, align="right", num_format="#,##0"), sum(x["pend"] for x in its) * cost)
dl = d0 + len(LINES)
d.write(dl, 1, "TOTAL", tot_l)
for c, key in ((2, "o"), (3, "oh"), (4, "pend")):
    L = chr(65 + c); d.write_formula(dl, c, f"=SUM({L}{d0+1}:{L}{dl})", tot, T[key])
d.write_formula(dl, 5, f"=SUM(F{d0+1}:F{dl})", tot_m, T["val"])
d.write_formula(dl, 6, f"=SUM(G{d0+1}:G{dl})", tot_m, T["pend_val"])
# pie data: only lines with stock on shelf (zero slices clutter a pie)
pie_rows = [k for k, lc in enumerate(LINES) if sum(x["val"] for x in rows if x["lc"] == lc) > 0]
pr0 = dl + 2
d.write(pr0, 1, "Pie data: product lines with stock on shelf", lab)
for j, k in enumerate(pie_rows):
    src = d0 + k + 1
    d.write_formula(pr0 + 1 + j, 1, f"=B{src}", cell(j % 2), list(LINES.values())[k][0])
    d.write_formula(pr0 + 1 + j, 2, f"=F{src}", cell(j % 2, align="right", num_format="#,##0"), sum(x["val"] for x in rows if x["lc"] == list(LINES)[k]))
pe = pr0 + len(pie_rows)
d.write(pe + 2, 2, "Status", lab); d.write(pe + 2, 3, "Pieces", lab)
d.write(pe + 3, 2, "On shelf", cell(False)); d.write_formula(pe + 3, 3, f"=D{dl+1}", cell(False, align="center"), T["oh"])
d.write(pe + 4, 2, "Awaiting vendor", cell(True)); d.write_formula(pe + 4, 3, f"=E{dl+1}", cell(True, align="center"), T["pend"])
SH = "Dashboard"
def style(ch, title):
    ch.set_title({"name": title, "name_font": {"name": FONT, "size": 12, "bold": True, "color": INK}})
    ch.set_chartarea({"border": {"color": LINE}, "fill": {"color": "#FFFFFF"}})
    ch.set_legend({"position": "bottom", "font": {"name": FONT, "size": 9}})
    return ch
# 1. Pie: value on shelf by product line
c1 = style(wb.add_chart({"type": "pie"}), "Stock value on shelf by product line (KES)")
c1.add_series({"name": "Value on shelf", "categories": [SH, pr0 + 1, 1, pe, 1], "values": [SH, pr0 + 1, 2, pe, 2],
               "points": [{"fill": {"color": PAL[i % len(PAL)]}, "border": {"color": "#FFFFFF"}} for i in range(len(pie_rows))],
               "data_labels": {"percentage": True, "leader_lines": True, "position": "best_fit", "font": {"name": FONT, "size": 9, "bold": True}}})
# 2. Doughnut: on shelf vs awaiting
c2 = style(wb.add_chart({"type": "doughnut"}), "Stock book: on shelf vs awaiting vendor (pcs)")
c2.add_series({"name": "Pieces", "categories": [SH, pe + 3, 2, pe + 4, 2], "values": [SH, pe + 3, 3, pe + 4, 3],
               "points": [{"fill": {"color": GOLD}}, {"fill": {"color": "#BFBFBF"}}],
               "data_labels": {"value": True, "percentage": True, "separator": "\n", "font": {"name": FONT, "size": 10, "bold": True}}})
c2.set_hole_size(55)
# 3. Clustered bar: ordered vs on shelf vs awaiting
c3 = style(wb.add_chart({"type": "bar"}), "Pieces by product line: ordered, on shelf, awaiting")
for col, nm, colr in ((2, "Ordered", "#6B6B6B"), (3, "On shelf", GOLD), (4, "Awaiting vendor", "#0E0E0E")):
    c3.add_series({"name": nm, "categories": [SH, d0, 1, dl - 1, 1], "values": [SH, d0, col, dl - 1, col],
                   "fill": {"color": colr}, "gap": 60, "data_labels": {"value": True, "font": {"name": FONT, "size": 8}}})
c3.set_x_axis({"name": "Pieces", "major_gridlines": {"visible": True, "line": {"color": "#EEEEEE"}}, "num_font": {"name": FONT, "size": 9}})
c3.set_y_axis({"reverse": True, "num_font": {"name": FONT, "size": 9}})
# 4. Stacked column: value on shelf + awaiting (KES)
c4 = style(wb.add_chart({"type": "column", "subtype": "stacked"}), "Value at cost by product line: on shelf and awaiting (KES)")
for col, nm, colr in ((5, "Value on shelf", GOLD), (6, "Value awaiting vendor", "#0E0E0E")):
    c4.add_series({"name": nm, "categories": [SH, d0, 1, dl - 1, 1], "values": [SH, d0, col, dl - 1, col], "fill": {"color": colr}, "gap": 70})
c4.set_y_axis({"num_format": "#,##0", "major_gridlines": {"visible": True, "line": {"color": "#EEEEEE"}}, "num_font": {"name": FONT, "size": 9}})
c4.set_x_axis({"num_font": {"name": FONT, "size": 8, "rotation": -30}})
# place charts in a 2 x 2 grid to the right of the data
for ch, (rw, cl) in ((c1, (dr, 8)), (c2, (dr, 11 + 0)), (c3, (dr + 20, 8)), (c4, (dr + 20, 11))):
    pass
d.insert_chart(dr, 8, c1, {"x_scale": 0.95, "y_scale": 1.25, "object_position": 3})
d.insert_chart(dr + 19, 8, c2, {"x_scale": 0.95, "y_scale": 1.0, "object_position": 3})
d.insert_chart(pe + 7, 1, c3, {"x_scale": 1.45, "y_scale": 1.3, "object_position": 3})
d.insert_chart(pe + 7 + 22, 1, c4, {"x_scale": 1.45, "y_scale": 1.3, "object_position": 3})
setup_print(d, True)

# =====================================================================  NOTES
nt = wb.add_worksheet("Notes")
nt.set_column(0, 0, 3); nt.set_column(1, 1, 28); nt.set_column(2, 2, 100)
nr = header_band(nt, 3, "NOTES AND BASIS OF PREPARATION", "Definitions, policies and document control", 64, [18, 24, 18, 18], [px(3), px(28), px(100)])
notes = [
    ("Purpose", "Records the physical opening stock of NURA Beauty at the studio. It is the starting balance for NURA Stocks (stock control in NURA Desk) and supports the inventory figure in the accounts."),
    ("Count", "Physical count on " + AS_AT + ", recorded in the stock book and confirmed line by line by the owner. Dates follow ISO 8601 (YYYY-MM-DD)."),
    ("Unit of measure", "PCS = one wig / unit. Quantities are whole pieces."),
    ("Qty ordered / received", "Ordered = quantity on the supplier order. Received = pieces physically counted. Where no difference was noted, the order was received in full."),
    ("Pending delivery", "Ordered but not yet received. Not owned stock, so not included in stock on hand or stock value; shown separately as stock on order."),
    ("Over-delivered", "Received above the quantity ordered. Included in stock on hand and value; settle the extra piece with the supplier."),
    ("Measurement (IAS 2)", "Inventories are measured at the lower of cost and net realisable value (IAS 2 Inventories; IFRS for SMEs Section 13). Cost of conversion = materials (bundles, wig cap), ventilation and labour. Cost formula: weighted average cost per product line."),
    ("Cost of making", "All wigs are made from scratch: bundles, ventilation, wig cap and labour. Actual cost per product line (KES, owner, " + AS_AT + "): " + "; ".join(NAMES[k] + " " + f"{LINE_TOTAL[k]:,.2f}" + (" (" + " + ".join(f"{n.lower()} {a:,.2f}" for n, a in v) + ")" if len(v) > 1 else "") for k, v in COST_PARTS.items()) + ". Total " + f"{sum(LINE_TOTAL.values()):,.2f}" + ", including KES 200 transport for the wig maker to collect materials, shared across the main batch in proportion to cost."),
    ("Unit costs used", "Weighted average cost per piece = product line total / pieces in the stock book for that line: " + "; ".join(f"{NAMES[k]} {LINE_TOTAL[k]:,.2f} / {BOOK_QTY[k]} = {LINES[k][1]:,.2f}" for k in NAMES) + "."),
    ("Currency", "Kenya Shilling (KES), ISO 4217. Amounts to 2 decimal places."),
    ("Item codes (SKU)", "NURA-<product line>-<colour code>, e.g. NURA-LWF-33 = Loose Wave Frontal, colour 33. A slash in a colour code is written as a hyphen (1/33 = 1-33)."),
    ("Colour codes", "1 = jet black, 1B = off black, 2 = darkest brown, 30 / 33 = auburn tones, 99J = burgundy-plum, 613 = blonde, x/y = two-tone (ombre), BUR = burgundy, RW = red wine, PD = piano dark, BLK = black."),
    ("Controls", "Light-yellow cells are inputs; all other figures are formulas. The Summary carries a check that the product-line total equals the register total."),
    ("Goods received", "26 pieces were delivered on " + AS_AT + " and are the only stock on the shelf. The stock book lists 43 pieces in total; the other 17 have not yet been received from the supplier and are not counted as stock."),
    ("Document control", DOC_NO + " v" + VERSION + " (" + AS_AT + "): Dashboard with charts added. v3.0: stock on hand corrected to the 26 pieces received; 17 awaiting delivery. v2.2: logo moved to its own header block (no overlap). v2.1: Goods Received note added. v2.0: unit costs and valuation. v1.0: quantities only."),
    ("Next step", "Match each SKU to its WooCommerce product and colour option and load these counts and buying prices as the NURA Desk stock-take."),
]
for i, (l, t) in enumerate(notes):
    rr = nr + i
    nt.set_row(rr, max(20, 15 * (len(t) // 110 + 1) + 6))
    nt.write(rr, 1, l, f(bold=True, valign="top", bottom=1, bottom_color=LINE))
    nt.write(rr, 2, t, f(text_wrap=True, valign="top", bottom=1, bottom_color=LINE))
setup_print(nt, True)

for ws, c in ((s, GOLD), (reg, BLACK), (v, GOLD), (g, BLACK), (d, GOLD), (nt, MUTED)):
    ws.set_tab_color(c)
wb.worksheets_objs.sort(key=lambda w: ["Summary", "Dashboard", "Stock Register", "Goods Received", "Supplier Variances", "Notes"].index(w.name))
s.activate(); s.set_first_sheet()
wb.close()
for fn in os.listdir(TMP):
    if fn.startswith("_logo_"): os.remove(os.path.join(TMP, fn))
print("saved", OUT, T)
