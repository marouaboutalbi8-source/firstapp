# -*- coding: utf-8 -*-
"""
Realistic application-UI mockup kit for the QICIRCO requirement-realization cards.

Each card shows how a real Microsoft Dynamics 365 or Salesforce screen satisfies a
specific RFP/BRD/proposal requirement, with numbered callouts tying UI to the
requirement. Chrome is an evocative (not pixel-exact) rendering of each product.
"""
from kit import (W, H, HEADER_H, FOOTER_H, MARGIN, QIC, MS, SF, FONT, esc, txt,
                 wraptext, rrect, line, path, chip, defs, header, footer,
                 canvas_open, canvas_close, save, _mini, ms_logo, sf_cloud,
                 platform_glyph)

# ------------------------------------------------------------------ palette
UI = dict(
    page_ms="#F1F3F7", page_sf="#F3F3F3",
    card="#FFFFFF", cardline="#E3E8EE",
    ink="#1B2733", sub="#5A6B7B", faint="#94A3B2",
    ms_topbar="#0B1F3A", ms_cmd="#FBFCFD",
    sf_hdr="#FFFFFF", sf_navblue="#0176D3", sf_hdrline="#E5E5E5",
    field="#F6F8FA", green="#1E9E5A", amber="#E8A33D", red="#C0392B",
    ok="#0B875B",
)

GOLD = QIC["gold"]


# ------------------------------------------------------------------ small ui primitives
def dot(cx, cy, r, c):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>'


def waffle(x, y, c="#ffffff", s=3.0, gap=2.4):
    out = []
    for r in range(3):
        for col in range(3):
            out.append(f'<rect x="{x+col*(s+gap):.1f}" y="{y+r*(s+gap):.1f}" '
                       f'width="{s}" height="{s}" rx="0.6" fill="{c}"/>')
    return "".join(out)


def badge_pill(x, y, text, fill, tc="#fff", size=10.5, pad=10, h=19, weight="700"):
    w = len(text) * size * 0.6 + pad * 2
    return rrect(x, y, w, h, r=h/2, fill=fill) + txt(x + w/2, y + h/2 + size*0.35, text,
        size=size, color=tc, weight=weight, anchor="middle"), w


def field(x, y, w, label, value, vcolor=None, lh=15, vsize=12.5, strong=False):
    vcolor = vcolor or UI["ink"]
    s = [txt(x, y, label.upper(), size=9, color=UI["faint"], weight="700", spacing="0.6")]
    s.append(txt(x, y + 18, value, size=vsize, color=vcolor,
                 weight="700" if strong else "600"))
    return "".join(s)


def field_box(x, y, w, label, value, vcolor=None, h=44):
    vcolor = vcolor or UI["ink"]
    s = [rrect(x, y, w, h, r=6, fill=UI["field"], stroke=UI["cardline"], sw=1)]
    s.append(txt(x + 12, y + 17, label.upper(), size=8.6, color=UI["faint"],
                 weight="700", spacing="0.5"))
    s.append(txt(x + 12, y + 34, value, size=12, color=vcolor, weight="600"))
    return "".join(s)


def card(x, y, w, h, title=None, icon=None, icon_c=None, pf=None, actions=None,
         head_c=None):
    s = [rrect(x, y, w, h, r=9, fill=UI["card"], stroke=UI["cardline"], sw=1.2)]
    s.append(f'<g filter="url(#dsSoft)">' + rrect(x, y, w, h, r=9, fill="none") + '</g>')
    if title:
        hc = head_c or (pf["primary"] if pf else UI["ink"])
        if icon:
            s.append(mini_chip(icon, icon_c or hc, x + 12, y + 12, 22))
            s.append(txt(x + 42, y + 27, title, size=12.5, color=UI["ink"], weight="800"))
        else:
            s.append(txt(x + 14, y + 27, title, size=12.5, color=UI["ink"], weight="800"))
        s.append(line(x + 12, y + 40, x + w - 12, y + 40, color=UI["cardline"], w=1))
    return "".join(s)


def mini_chip(glyph, color, x, y, sz=24, bg="#F3F7FB", cloud=False):
    m = _mini(glyph, color)
    sc = sz / 24.0
    if cloud:
        s = [sf_cloud(x + sz/2, y + sz/2, sz*0.6, c=color)]
        if m:
            s.append(f'<g transform="translate({x+sz*0.26},{y+sz*0.24}) scale({sc*0.5})">{m}</g>')
        return "".join(s)
    s = [rrect(x, y, sz, sz, r=5, fill=bg, stroke=UI["cardline"], sw=1)]
    if m:
        s.append(f'<g transform="translate({x+sz*0.14},{y+sz*0.14}) scale({sc*0.72})">{m}</g>')
    return "".join(s)


def avatar(cx, cy, r, initials, c):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>'
            + txt(cx, cy + r*0.34, initials, size=r*0.82, color="#fff",
                  weight="700", anchor="middle"))


def list_row(x, y, w, h, avinit, avc, title, sub, right=None, active=False, score=None):
    s = []
    if active:
        s.append(rrect(x, y, w, h, r=6, fill="#EAF2FB"))
        s.append(rrect(x, y, 3.5, h, fill="#0F6CBD"))
    s.append(avatar(x + 20, y + h/2, 13, avinit, avc))
    s.append(txt(x + 40, y + h/2 - 3, title, size=11.6, color=UI["ink"], weight="700"))
    s.append(txt(x + 40, y + h/2 + 13, sub, size=9.8, color=UI["sub"], weight="500"))
    if score is not None:
        s.append(txt(x + w - 16, y + h/2 + 5, str(score), size=15, color="#0F6CBD",
                     weight="800", anchor="end"))
    elif right:
        s.append(txt(x + w - 14, y + h/2 + 4, right, size=9.6, color=UI["faint"],
                     weight="600", anchor="end"))
    return "".join(s)


def timeline_item(x, y, w, icon, ic_c, title, sub, when, tag=None, tag_c=None):
    s = [dot(x + 8, y + 12, 4, ic_c)]
    s.append(f'<line x1="{x+8}" y1="{y+18}" x2="{x+8}" y2="{y+48}" stroke="{UI["cardline"]}" stroke-width="1.4"/>')
    s.append(mini_chip(icon, ic_c, x + 22, y + 2, 20))
    s.append(txt(x + 50, y + 12, title, size=11, color=UI["ink"], weight="700"))
    s.append(txt(x + 50, y + 28, sub, size=9.6, color=UI["sub"], weight="500"))
    s.append(txt(x + w - 6, y + 12, when, size=9, color=UI["faint"], weight="500", anchor="end"))
    if tag:
        s.append(chip(x + 50, y + 34, 66, 15, tag, tag_c or "#EAF3EA",
                      text_color="#0B875B", size=8.6, r=7))
    return "".join(s)


def stat_tile(x, y, w, h, value, label, color, sub=None, glyph=None):
    s = [rrect(x, y, w, h, r=8, fill="#fff", stroke=UI["cardline"], sw=1.1)]
    s.append(rrect(x, y, w, 3.5, r=2, fill=color))
    if glyph:
        s.append(mini_chip(glyph, color, x + 12, y + 12, 20))
    s.append(txt(x + w - 12, y + 34, value, size=23, color=color, weight="800", anchor="end"))
    s.append(txt(x + 12, y + h - 22, label, size=10, color=UI["ink"], weight="700"))
    if sub:
        s.append(txt(x + 12, y + h - 8, sub, size=8.8, color=UI["sub"], weight="500"))
    return "".join(s)


def bars(x, y, w, h, values, color, labels=None, maxv=None):
    maxv = maxv or max(values)
    n = len(values)
    bw = w / n * 0.6
    gap = w / n
    s = []
    for i, v in enumerate(values):
        bh = (v / maxv) * h
        bx = x + i * gap + (gap - bw) / 2
        s.append(rrect(bx, y + h - bh, bw, bh, r=2, fill=color))
        if labels:
            s.append(txt(bx + bw/2, y + h + 12, labels[i], size=8.2, color=UI["faint"],
                         weight="600", anchor="middle"))
    return "".join(s)


def donut(cx, cy, r, segments, inner=0.62):
    """segments: list of (value, color). Draws a donut."""
    import math
    total = sum(v for v, _ in segments)
    a0 = -90
    s = []
    for v, c in segments:
        a1 = a0 + 360 * v / total
        large = 1 if (a1 - a0) > 180 else 0
        x0 = cx + r * math.cos(math.radians(a0))
        y0 = cy + r * math.sin(math.radians(a0))
        x1 = cx + r * math.cos(math.radians(a1))
        y1 = cy + r * math.sin(math.radians(a1))
        s.append(f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f} Z" fill="{c}"/>')
        a0 = a1
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r*inner}" fill="#fff"/>')
    return "".join(s)


def line_chart(x, y, w, h, pts, color, fill_op=0.12):
    n = len(pts)
    mx = max(pts)
    coords = [(x + i * (w/(n-1)), y + h - (v/mx)*h) for i, v in enumerate(pts)]
    d = "M" + " L".join(f"{px:.1f} {py:.1f}" for px, py in coords)
    area = d + f" L{coords[-1][0]:.1f} {y+h:.1f} L{coords[0][0]:.1f} {y+h:.1f} Z"
    s = [path(area, fill=color, opacity=fill_op)]
    s.append(path(d, stroke=color, sw=2.4))
    return "".join(s)


def table(x, y, w, cols, rows, colw, rowh=26, head_c="#F4F6F9"):
    s = [rrect(x, y, w, rowh, r=4, fill=head_c)]
    cx = x + 12
    for i, c in enumerate(cols):
        s.append(txt(cx, y + rowh/2 + 4, c, size=9.4, color=UI["sub"], weight="800"))
        cx += colw[i]
    yy = y + rowh
    for r in rows:
        cx = x + 12
        for i, cell in enumerate(r):
            col = UI["ink"]
            val = cell
            if isinstance(cell, tuple):
                val, col = cell
            s.append(txt(cx, yy + rowh/2 + 4, val, size=9.6, color=col, weight="600"))
            cx += colw[i]
        s.append(line(x + 8, yy + rowh, x + w - 8, yy + rowh, color=UI["cardline"], w=0.8))
        yy += rowh
    return "".join(s)


# ------------------------------------------------------------------ product chrome
def app_window(pf, x, y, w, h, breadcrumb, record_title):
    """Outer window + product chrome. Returns (svg, content_x, content_y, content_w, content_h)."""
    s = [rrect(x, y, w, h, r=10, fill="#fff", stroke="#C7D2DE", sw=1.4)]
    s.append(f'<g filter="url(#ds)">' + rrect(x, y, w, h, r=10, fill="none") + '</g>')
    # window title bar (browser-like)
    tb = 26
    s.append(rrect(x, y, w, tb, r=10, fill="#E7ECF2"))
    s.append(rrect(x, y + tb - 10, w, 10, fill="#E7ECF2"))
    for i, c in enumerate(["#F25F5C", "#FFB84D", "#2ECC71"]):
        s.append(dot(x + 16 + i*15, y + tb/2, 4.2, c))
    # url pill
    s.append(rrect(x + 70, y + 6, w - 140, tb - 12, r=7, fill="#FFFFFF", stroke="#D4DCE5", sw=1))
    dom = "org.crm.dynamics.com" if pf["key"] == "microsoft" else "qicirco.lightning.force.com"
    s.append(f'<circle cx="{x+84}" cy="{y+tb/2}" r="3.4" fill="{UI["green"]}"/>')
    s.append(txt(x + 94, y + tb/2 + 3.4, dom, size=9.4, color=UI["sub"], weight="500"))
    cy = y + tb
    if pf["key"] == "microsoft":
        s2, cont = _chrome_ms(pf, x, cy, w, y + h - cy, breadcrumb, record_title)
    else:
        s2, cont = _chrome_sf(pf, x, cy, w, y + h - cy, breadcrumb, record_title)
    s.append(s2)
    return "".join(s), cont


def _chrome_ms(pf, x, y, w, h, breadcrumb, record_title):
    s = []
    # ---- top app bar (dark navy — Unified Interface) ----
    hb = 42
    appname = _ms_appname(breadcrumb)
    s.append(rrect(x, y, w, hb, fill=UI["ms_topbar"]))
    s.append(waffle(x + 16, y + hb/2 - 5, c="#ffffff", s=2.9, gap=2.3))
    s.append(txt(x + 42, y + hb/2 + 4, "Dynamics 365", size=12.6, color="#fff", weight="700"))
    s.append(line(x + 148, y + 10, x + 148, y + hb - 10, color="#3a5170", w=1))
    s.append(txt(x + 162, y + hb/2 + 4, appname, size=11.4, color="#DCE8F5", weight="600"))
    # center search
    sw_ = 380
    s.append(rrect(x + w/2 - sw_/2, y + 8, sw_, hb - 16, r=4, fill="#12324f", stroke="#284a6e", sw=1))
    s.append(txt(x + w/2 - sw_/2 + 14, y + hb/2 + 4, "⌕  Search", size=10.4, color="#8AA2BC", weight="500"))
    # right icons
    rx = x + w - 20
    for lbl in ["➕", "⚙", "?", "▣", "◔"]:
        s.append(txt(rx, y + hb/2 + 4.5, lbl, size=11.5, color="#B9CBDD", anchor="end"))
        rx -= 25
    s.append(avatar(x + w - 22, y + hb/2, 11, "SA", "#C9A24B"))
    # ---- command bar (light) ----
    y2 = y + hb
    cb = 36
    s.append(rrect(x, y2, w, cb, fill=UI["ms_cmd"], stroke=UI["cardline"], sw=1))
    s.append(txt(x + 16, y2 + cb/2 + 4.5, "←", size=13, color=pf["primary"], weight="700"))
    cx = x + 40
    cmds = [("➕", "New"), ("\U0001F4BE", "Save"), ("✓", "Save & Close"),
            ("↻", "Refresh"), ("⚑", "Flow"), ("⋯", "More")]
    for ic, lb in cmds:
        s.append(txt(cx, y2 + cb/2 + 4.5, ic, size=10.5, color=pf["primary"], weight="700"))
        s.append(txt(cx + 15, y2 + cb/2 + 4.5, lb, size=10.4, color=UI["ink"], weight="600"))
        cx += 22 + len(lb) * 6.2 + 14
    # right side: view selector
    s.append(rrect(x + w - 196, y2 + 6, 184, cb - 12, r=4, fill="#fff", stroke=UI["cardline"], sw=1))
    s.append(txt(x + w - 186, y2 + cb/2 + 4, "Active records  ▾", size=9.6, color=UI["sub"], weight="600"))
    # ---- left sitemap rail ----
    y3 = y2 + cb
    rail = 158
    s.append(rrect(x, y3, rail, y + h - y3, fill="#FAFBFC", stroke=UI["cardline"], sw=1))
    s.append(txt(x + 14, y3 + 22, appname.upper(), size=9, color=UI["faint"], weight="800", spacing="0.5"))
    s.append(line(x + 12, y3 + 30, x + rail - 12, y3 + 30, color=UI["cardline"], w=1))
    nav = [("search", "Search", False), ("user360", "Customers", True), ("case", "Cases", False),
           ("clock", "SLA / Queues", False), ("people", "Accounts", False),
           ("pbi", "Dashboards", False), ("flow", "Workflows", False)]
    ny = y3 + 42
    for g, lb, act in nav:
        if act:
            s.append(rrect(x, ny - 4, rail, 30, fill="#EAF2FB"))
            s.append(rrect(x, ny - 4, 3, 30, fill=pf["primary"]))
        s.append(mini_chip(g, pf["primary"], x + 14, ny, 18))
        s.append(txt(x + 40, ny + 13, lb, size=10.4,
                     color=UI["ink"] if act else UI["sub"], weight="700" if act else "600"))
        ny += 32
    # area switcher (bottom)
    s.append(line(x + 12, y + h - 40, x + rail - 12, y + h - 40, color=UI["cardline"], w=1))
    s.append(txt(x + 14, y + h - 20, "Customer Service  ▴", size=9.6, color=pf["primary"], weight="700"))
    cont = (x + rail, y3, w - rail, y + h - y3)
    s.append(rrect(cont[0], cont[1], cont[2], cont[3], fill=UI["page_ms"]))
    return "".join(s), cont


def _ms_appname(breadcrumb):
    b = breadcrumb.lower()
    if "sales" in b or "opportun" in b or "pipeline" in b:
        return "Sales Hub"
    if "dashboard" in b or "analytics" in b:
        return "Customer Service"
    if "setup" in b or "security" in b or "maker" in b or "integration" in b:
        return "Power Platform admin"
    return "Customer Service"


def _chrome_sf(pf, x, y, w, h, breadcrumb, record_title):
    s = []
    appname, appcolor, tabs, active_tab = _sf_app(breadcrumb)
    # ---- global header (dark blue Lightning bar) ----
    hb = 40
    s.append(rrect(x, y, w, hb, fill="#16325C"))
    s.append(waffle(x + 18, y + hb/2 - 5, c="#ffffff", s=3.0, gap=2.4))
    s.append(txt(x + 42, y + hb/2 + 4, "⋮⋮⋮", size=6, color="#fff", weight="400"))
    # search (big, center-left)
    s.append(rrect(x + 150, y + 8, w - 340, hb - 16, r=6, fill="#0b264a"))
    s.append(txt(x + 166, y + hb/2 + 3.6, "⌕   Search Salesforce", size=10, color="#9DB4CE", weight="500"))
    rx = x + w - 20
    for lbl in ["✦", "?", "⚙", "🔔", "▦"]:
        s.append(txt(rx, y + hb/2 + 4.5, lbl, size=11, color="#C8D6E6", anchor="end"))
        rx -= 24
    s.append(avatar(x + w - 22, y + hb/2, 11, "SA", "#C9A24B"))
    # ---- app nav bar (white) ----
    y2 = y + hb
    nb = 42
    s.append(rrect(x, y2, w, nb, fill="#FFFFFF", stroke=UI["sf_hdrline"], sw=1))
    s.append(rrect(x + 14, y2 + 9, 26, 24, r=6, fill=appcolor))
    s.append(sf_cloud(x + 27, y2 + 21, 8, c="#fff"))
    s.append(txt(x + 48, y2 + nb/2 + 4, appname, size=12.5, color="#080707", weight="800"))
    s.append(txt(x + 48 + len(appname) * 7.4 + 6, y2 + nb/2 + 4, "▾", size=9, color=UI["sub"]))
    tx = x + 60 + len(appname) * 7.6 + 26
    for i, t in enumerate(tabs):
        act = (i == active_tab)
        s.append(txt(tx, y2 + nb/2 + 4, t, size=10.6,
                     color="#080707" if act else "#3E3E3C", weight="700" if act else "500"))
        twd = len(t) * 6.8 + 26
        if act:
            s.append(rrect(tx - 3, y2 + nb - 3, twd - 18, 3, fill=UI["sf_navblue"]))
        tx += twd
    y3 = y2 + nb
    # ---- utility bar (bottom, dark) — Service Console signature ----
    ub = 30
    uby = y + h - ub
    s.append(rrect(x, uby, w, ub, fill="#032D60"))
    utils = [("🎧", "Omni-Channel"), ("●", "Available"), ("☎", "Phone"),
             ("🕘", "History"), ("📝", "Notes"), ("⚡", "Macros")]
    ux = x + 16
    for i, (ic, lb) in enumerate(utils):
        col = "#4BCA81" if lb == "Available" else "#C8D6E6"
        s.append(txt(ux, uby + ub/2 + 4, ic, size=10, color=col))
        s.append(txt(ux + 16, uby + ub/2 + 4, lb, size=9.4, color="#DCE8F5", weight="600"))
        ux += 22 + len(lb) * 6.2 + 20
        if i == 1:
            ux += 6
    s.append(txt(x + w - 16, uby + ub/2 + 4, "QICIRCO · Lightning Experience", size=8.8,
                 color="#7f9ab8", weight="500", anchor="end"))
    cont = (x, y3, w, uby - y3)
    s.append(rrect(cont[0], cont[1], cont[2], cont[3], fill=UI["page_sf"]))
    return "".join(s), cont


def _sf_app(breadcrumb):
    b = breadcrumb.lower()
    if "sales" in b or "opportun" in b or "pipeline" in b:
        return "Sales", "#0D9DDA", ["Home", "Leads", "Opportunities", "Accounts", "Contacts", "Reports", "More ▾"], 2
    if "dashboard" in b or "analytics" in b:
        return "Analytics", "#E8762D", ["Home", "Dashboards", "Reports", "Cases", "Accounts", "More ▾"], 1
    if "setup" in b or "security" in b:
        return "Setup", "#706E6B", ["Home", "Users", "Profiles", "Permission Sets", "Security", "More ▾"], 4
    if "maker" in b or "flow" in b:
        return "Platform", "#032D60", ["Home", "Flows", "Objects", "Apps", "More ▾"], 1
    if "integration" in b or "mulesoft" in b:
        return "Integration", "#00A0DF", ["Home", "APIs", "Runtimes", "Monitoring", "More ▾"], 3
    return "Service", "#1B96FF", ["Home", "Cases", "Accounts", "Contacts", "Knowledge", "Reports", "More ▾"], 1


# ------------------------------------------------------------------ callouts + requirement rail
def chevrons(x, y, w, h, stages, active, color, done_color=None):
    """Business-process-flow chevron bar."""
    done_color = done_color or color
    n = len(stages)
    sw_ = w / n
    tip = 12
    s = []
    for i, st in enumerate(stages):
        sx = x + i * sw_
        if i < active:
            fc, tc = done_color, "#fff"
        elif i == active:
            fc, tc = color, "#fff"
        else:
            fc, tc = "#EEF2F6", UI["sub"]
        if i == 0:
            d = f"M{sx} {y} L{sx+sw_-tip} {y} L{sx+sw_} {y+h/2} L{sx+sw_-tip} {y+h} L{sx} {y+h} Z"
        else:
            d = (f"M{sx} {y} L{sx+sw_-tip} {y} L{sx+sw_} {y+h/2} L{sx+sw_-tip} {y+h} "
                 f"L{sx} {y+h} L{sx+tip} {y+h/2} Z")
        s.append(path(d, fill=fc))
        s.append(txt(sx + sw_/2 + tip/2, y + h/2 + 4, st, size=10.2, color=tc,
                     weight="700", anchor="middle"))
    return "".join(s)


def sect(x, y, text, color=None):
    return txt(x, y, text.upper(), size=9.6, color=color or UI["faint"],
               weight="800", spacing="1")


def inbox_row(x, y, w, h, glyph, gc, title, sub, meta, active=False, tag=None, tag_c=None):
    s = []
    if active:
        s.append(rrect(x, y, w, h, r=6, fill="#EAF2FB"))
        s.append(rrect(x, y, 3.5, h, fill=gc))
    s.append(mini_chip(glyph, gc, x + 12, y + h/2 - 11, 22))
    s.append(txt(x + 44, y + h/2 - 4, title, size=11.2, color=UI["ink"], weight="700"))
    s.append(txt(x + 44, y + h/2 + 12, sub, size=9.4, color=UI["sub"], weight="500"))
    s.append(txt(x + w - 12, y + h/2 - 4, meta, size=8.8, color=UI["faint"],
                 weight="600", anchor="end"))
    if tag:
        s.append(chip(x + w - 78, y + h/2 + 3, 64, 15, tag, tag_c or "#EAF3EA",
                      text_color="#0B875B", size=8.2, r=7))
    return "".join(s)


def gauge_ring(cx, cy, r, pct, color, label, value):
    import math
    s = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#E7ECF2" stroke-width="8"/>']
    a = -90 + 360 * pct
    large = 1 if pct > 0.5 else 0
    x1 = cx + r * math.cos(math.radians(a))
    y1 = cy + r * math.sin(math.radians(a))
    x0 = cx
    y0 = cy - r
    s.append(f'<path d="M{x0} {y0} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}" fill="none" '
             f'stroke="{color}" stroke-width="8" stroke-linecap="round"/>')
    s.append(txt(cx, cy + 2, value, size=r*0.55, color=color, weight="800", anchor="middle"))
    s.append(txt(cx, cy + r + 18, label, size=9.5, color=UI["sub"], weight="600", anchor="middle"))
    return "".join(s)


def list_view(pf, x, y, w, h, view_name, count, cols, colw, rows, buttons,
              rowh=34, chart=None):
    """Authentic CRM list/grid landing view (D365 entity grid / SF list view)."""
    prim = pf["primary"]
    s = []
    # toolbar
    tbh = 40
    s.append(rrect(x, y, w, tbh, fill="#fff", stroke=UI["cardline"], sw=1))
    if pf["key"] == "microsoft":
        s.append(txt(x + 16, y + tbh/2 + 5, view_name + "  ▾", size=14, color=UI["ink"], weight="800"))
    else:
        s.append(mini_chip("case", prim, x + 14, y + 9, 22, cloud=True))
        s.append(txt(x + 44, y + tbh/2 - 1, view_name, size=13, color="#080707", weight="800"))
        s.append(txt(x + 44, y + tbh/2 + 13, f"{count} items · sorted by modified", size=8.6, color=UI["sub"], weight="500"))
    # right buttons
    bx = x + w - 12
    for lb in reversed(buttons):
        bw = len(lb) * 6.6 + 22
        bx -= bw
        primary_btn = (lb == buttons[-1])
        s.append(rrect(bx, y + 7, bw, tbh - 14, r=5,
                       fill=(prim if primary_btn else "#fff"),
                       stroke=(prim if not primary_btn else None), sw=1.2))
        s.append(txt(bx + bw/2, y + tbh/2 + 4, lb, size=9.6,
                     color=("#fff" if primary_btn else prim), weight="700", anchor="middle"))
        bx -= 8
    # search (ms shows count on right; sf search left of buttons)
    if pf["key"] == "microsoft":
        s.append(rrect(x + w - 470, y + 8, 190, tbh - 16, r=5, fill=UI["field"], stroke=UI["cardline"], sw=1))
        s.append(txt(x + w - 458, y + tbh/2 + 3.5, "⌕ Filter by keyword", size=9, color=UI["faint"], weight="500"))
    gy = y + tbh + 8
    gw = w - (chart[0] if chart else 0)
    # grid header
    s.append(rrect(x, gy, gw, h - tbh - 8, r=8, fill="#fff", stroke=UI["cardline"], sw=1))
    hh = 30
    s.append(rrect(x, gy, gw, hh, r=8, fill="#F4F6F9"))
    s.append(rrect(x, gy + hh - 8, gw, 8, fill="#F4F6F9"))
    # checkbox col
    s.append(f'<rect x="{x+14}" y="{gy+hh/2-6}" width="12" height="12" rx="2.5" fill="#fff" stroke="{UI["faint"]}" stroke-width="1.4"/>')
    cxp = x + 40
    for i, c in enumerate(cols):
        s.append(txt(cxp, gy + hh/2 + 4, c + (" ▾" if i == 0 else ""), size=9.4, color=UI["sub"], weight="800"))
        cxp += colw[i]
    ry = gy + hh
    for ri, row in enumerate(rows):
        if ri % 2 == 1:
            s.append(rrect(x + 2, ry, gw - 4, rowh, fill="#FAFBFC"))
        s.append(f'<rect x="{x+14}" y="{ry+rowh/2-6}" width="12" height="12" rx="2.5" fill="#fff" stroke="{UI["faint"]}" stroke-width="1.4"/>')
        cxp = x + 40
        for ci, cell in enumerate(row):
            if isinstance(cell, tuple) and cell and cell[0] == "pill":
                _, lbl, bg, fg = cell
                s.append(chip(cxp, ry + rowh/2 - 8, len(lbl)*6.2 + 18, 16, lbl, bg, text_color=fg, size=8.6, r=8))
            elif isinstance(cell, tuple):
                val, col = cell
                s.append(txt(cxp, ry + rowh/2 + 4, val, size=9.6, color=col,
                             weight="700" if ci == 0 else "600"))
            else:
                s.append(txt(cxp, ry + rowh/2 + 4, cell, size=9.6,
                             color=(prim if ci == 0 else UI["ink"]),
                             weight="700" if ci == 0 else "500"))
            cxp += colw[ci]
        s.append(line(x + 10, ry + rowh, x + gw - 10, ry + rowh, color=UI["cardline"], w=0.7))
        ry += rowh
    # footer count (ms)
    if pf["key"] == "microsoft":
        s.append(txt(x + 16, gy + h - tbh - 8 - 12, f"1 - {len(rows)} of {count}", size=9, color=UI["sub"], weight="600"))
        s.append(txt(x + gw - 16, gy + h - tbh - 8 - 12, "◀  Page 1  ▶", size=9, color=UI["sub"], weight="600", anchor="end"))
    return "".join(s), (x + gw + 12, gy, (chart[0] - 12) if chart else 0, h - tbh - 8)


def phone_frame(x, y, w, h, pf):
    """A phone device frame; returns (svg, inner box)."""
    s = [rrect(x, y, w, h, r=22, fill="#1B2733")]
    s.append(rrect(x + 5, y + 5, w - 10, h - 10, r=18, fill="#fff"))
    s.append(rrect(x + w/2 - 26, y + 10, 52, 5, r=2.5, fill="#1B2733"))
    return "".join(s), (x + 8, y + 22, w - 16, h - 30)


def callout(n, x, y, r=15):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{GOLD}" stroke="#fff" stroke-width="2"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{QIC["maroon_dk"]}" stroke-width="1" opacity="0.5"/>'
            + txt(x, y + r*0.36, str(n), size=r*0.95, color="#3a2a06", weight="900", anchor="middle"))


def highlight(x, y, w, h, r=6):
    return rrect(x, y, w, h, r=r, fill="none", stroke=GOLD, sw=2.2, dash="6 4")


def req_rail(pf, x, y, w, h, req):
    prim = pf["primary"]
    deep = pf["deep"]
    s = [rrect(x, y, w, h, r=12, fill="#fff", stroke=QIC["line"], sw=1.4)]
    s.append(f'<g filter="url(#dsSoft)">' + rrect(x, y, w, h, r=12, fill="none") + '</g>')
    s.append(rrect(x, y, w, 6, r=3, fill=QIC["maroon"]))
    pad = 18
    s.append(txt(x + pad, y + 30, "REQUIREMENT", size=11, color=QIC["maroon"],
                 weight="800", spacing="2"))
    # id
    s.append(rrect(x + w - pad - 54, y + 16, 54, 20, r=6, fill=QIC["slate"]))
    s.append(txt(x + w - pad - 27, y + 30, req["id"], size=11, color="#fff",
                 weight="800", anchor="middle"))
    # title
    wt, nl = wraptext(x + pad, y + 54, req["title"], 15.5, deep, weight="800",
                      anchor="start", max_chars=30, lh=19)
    s.append(wt)
    yy = y + 54 + nl * 19 + 6
    # source chips
    cx = x + pad
    for src in req["sources"]:
        cw = len(src) * 5.6 + 18
        s.append(rrect(cx, yy, cw, 17, r=8, fill=QIC["band"], stroke=QIC["line"], sw=1))
        s.append(txt(cx + cw/2, yy + 12, src, size=8.8, color=QIC["slate2"],
                     weight="700", anchor="middle"))
        cx += cw + 6
    yy += 30
    # requirement text bullets
    for b in req["text"]:
        s.append(f'<circle cx="{x+pad+3}" cy="{yy-3}" r="2.4" fill="{prim}"/>')
        wt, nl = wraptext(x + pad + 14, yy, b, 10.6, UI["ink"], weight="500",
                          anchor="start", max_chars=42, lh=14)
        s.append(wt)
        yy += nl * 14 + 8
    yy += 4
    s.append(line(x + pad, yy, x + w - pad, yy, color=QIC["line"], w=1))
    yy += 22
    s.append(mini_chip("copilot" if False else "gauge", prim, x + pad, yy - 15, 20))
    s.append(txt(x + pad + 28, yy, f"HOW {pf['name'].upper()} DELIVERS IT",
                 size=10.5, color=deep, weight="800", spacing="0.5"))
    yy += 16
    for i, a in enumerate(req["addressed"], 1):
        s.append(callout(i, x + pad + 10, yy + 4, r=11))
        wt, nl = wraptext(x + pad + 28, yy, a, 10.4, UI["ink"], weight="500",
                          anchor="start", max_chars=40, lh=13.5)
        s.append(wt)
        yy += max(nl * 13.5, 22) + 7
    return "".join(s)


# ------------------------------------------------------------------ full card wrapper
def build_card(pf, req, content_fn, idx_label):
    s = [canvas_open(pf)]
    s.append(header(pf, "REQUIREMENT → REALIZED IN PRODUCT",
                    req["headline"],
                    f"How the {pf['name']} solution addresses this QICIRCO requirement"))
    railW = 372
    top = 124
    bot = H - FOOTER_H - 14
    s.append(req_rail(pf, MARGIN, top, railW, bot - top, req))
    ax = MARGIN + railW + 16
    aw = W - MARGIN - ax
    aiy = top
    aih = bot - top
    s.append(content_fn(pf, ax, aiy, aw, aih, req))
    s.append(footer(pf, idx_label))
    s.append(canvas_close())
    return "".join(s)
