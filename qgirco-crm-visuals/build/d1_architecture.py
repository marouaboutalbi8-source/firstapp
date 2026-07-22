# -*- coding: utf-8 -*-
"""Diagram 1 — Enterprise Solution Architecture (layered)."""
from kit import *


def band(x, y, w, h, tag, tag_color, fill, edge):
    s = [rrect(x, y, w, h, r=16, fill=fill, stroke=edge, sw=1.5)]
    # left vertical tag tab
    s.append(rrect(x, y, 30, h, r=16, fill=tag_color))
    s.append(rrect(x + 15, y, 15, h, fill=tag_color))
    tfs = 11.5 if h > 150 else 10.5
    tsp = 2.5 if h > 150 else 1.2
    s.append(f'<text x="{x+20}" y="{y+h/2}" font-family="{FONT}" font-size="{tfs}" '
             f'font-weight="800" fill="#ffffff" letter-spacing="{tsp}" text-anchor="middle" '
             f'transform="rotate(-90 {x+20} {y+h/2})">{esc(tag)}</text>')
    return "".join(s)


def vrail(x, y, w, h, title, sub, color, items, pf):
    s = [rrect(x, y, w, h, r=16, fill="#ffffff", stroke=color, sw=1.6)]
    s.append(f'<g filter="url(#dsSoft)">' + rrect(x, y, w, h, r=16, fill="none") + '</g>')
    hh = 56
    s.append(rrect(x, y, w, hh, r=16, fill=color))
    s.append(rrect(x, y + 26, w, hh - 26, fill=color))
    tline1, tline2 = title
    s.append(txt(x + w/2, y + 22, tline1, size=12.5, color="#fff", weight="800",
                 anchor="middle", spacing="1"))
    s.append(txt(x + w/2, y + 38, tline2, size=12.5, color="#fff", weight="800",
                 anchor="middle", spacing="1"))
    s.append(txt(x + w/2, y + 51, sub, size=9, color="#ffffff", weight="500",
                 anchor="middle", opacity=0.9))
    iy = y + hh + 12
    ih = (h - hh - 22) / len(items)
    for glyph, gc, t1, t2 in items:
        s.append(rrect(x + 12, iy, w - 24, ih - 10, r=9, fill="#F5F8FB",
                       stroke=QIC["line"], sw=1))
        s.append(_icon_chip_small(glyph, gc, x + 20, iy + (ih-10)/2 - 12))
        s.append(txt(x + 50, iy + (ih-10)/2 - 1, t1, size=10.6, color=QIC["ink"], weight="700"))
        s.append(txt(x + 50, iy + (ih-10)/2 + 14, t2, size=9.3, color=QIC["sub"], weight="500"))
        iy += ih
    return "".join(s)


def _icon_chip_small(glyph, color, x, y, sz=24):
    from kit import _mini
    mini = _mini(glyph, color)
    sc = sz / 24.0
    s = [rrect(x, y, sz, sz, r=6, fill="#ffffff", stroke=QIC["line"], sw=1)]
    if mini:
        s.append(f'<g transform="translate({x+sz*0.13},{y+sz*0.13}) scale({sc*0.74})">{mini}</g>')
    return "".join(s)


def build(pf):
    s = [canvas_open(pf)]
    s.append(header(pf, "SOLUTION ARCHITECTURE",
                    "Enterprise CRM — Solution Architecture",
                    "Layered reference architecture · engagement, integration, and systems of record"))

    LX, RX = 40, W - 40
    railW = 176
    top = 126
    bottom = 902
    midX = LX + railW + 16          # 232
    midR = RX - railW - 16          # 1528
    midW = midR - midX              # ~1296

    prim = pf["primary"]
    deep = pf["deep"]

    # ---- left rail: security & governance ----
    sec_items = [
        ("entra", prim, "Identity · SSO · MFA", pf["identity"]),
        ("dv" if pf["key"] == "microsoft" else "shield", prim, "Role-based access",
         "Dataverse roles + BU" if pf["key"] == "microsoft" else "Profiles + perm sets"),
        ("defender", "#107C41", "Encryption", "In transit & at rest"),
        ("purview", "#8657C7", "Audit & monitoring",
         "Purview" if pf["key"] == "microsoft" else "Shield Event Monitoring"),
        ("defender", prim, "Threat protection",
         "Microsoft Defender" if pf["key"] == "microsoft" else "Salesforce Shield"),
        ("purview", QIC["maroon"], "Compliance", "QCB · PDPPL · GDPR"),
    ]
    s.append(vrail(LX, top, railW, bottom - top, ("SECURITY &", "GOVERNANCE"),
                   "Zero-Trust · every layer", QIC["slate"], sec_items, pf))

    # ---- right rail: analytics & AI ----
    an_items = [
        ("pbi", "#F2B707", "Operational dashboards", "Volumes · SLA · aging"),
        ("pbi", prim, "Management reporting", pf["analytics"]),
        ("pbi", "#107C41", "KPI monitoring", "SLA % · FCR · workload"),
        ("copilot", "#8657C7", "AI assistance", pf["ai"] + " · governed"),
        ("pbi", QIC["gold"], "Future intelligence", "Predict · segment"),
    ]
    s.append(vrail(midR + 16, top, railW, bottom - top, ("ANALYTICS", "& AI"),
                   "Insight foundation", deep, an_items, pf))

    # ================= BAND A — engagement channels =================
    ay, ah = top, 132
    s.append(band(midX, ay, midW, ah, "CHANNELS", prim, "#FFFFFF", pf["tile_edge"]))
    s.append(txt(midX + 44, ay + 26, "Engagement Channels",
                 size=15, color=deep, weight="800"))
    s.append(txt(midX + 232, ay + 26, "— omnichannel customer contact unified to one engagement surface",
                 size=11, color=QIC["sub"], weight="500", italic=True))
    chans = [
        ("Voice", "3CX telephony", ic_phone),
        ("WhatsApp", "WABA business", ic_whatsapp),
        ("Email", "M365 / Outlook", ic_mail),
        ("Shared mailboxes", "departmental", ic_mail),
        ("Web & forms", "website capture", ic_web),
        ("Portals", "Insursa B2B/B2C", ic_portal),
        ("Walk-in", "branch counter", ic_walkin),
    ]
    n = len(chans)
    pad = 44
    gap = 12
    cw = (midW - pad - 16 - (n - 1) * gap) / n
    cx = midX + pad
    cyt = ay + 42
    chy = ah - 54
    for name, sub, icon in chans:
        s.append(rrect(cx, cyt, cw, chy, r=10, fill="#F5F8FB", stroke=pf["tile_edge"], sw=1.2))
        s.append(rrect(cx, cyt, cw, 4, r=2, fill=prim))
        s.append(icon(cx + cw/2 - 15, cyt + 12, 1.25,
                      c=prim if name not in ("WhatsApp",) else "#25D366"))
        s.append(txt(cx + cw/2, cyt + chy - 24, name, size=11.6, color=QIC["ink"],
                     weight="700", anchor="middle"))
        s.append(txt(cx + cw/2, cyt + chy - 9, sub, size=9.3, color=QIC["sub"],
                     weight="500", anchor="middle"))
        cx += cw + gap

    # ================= BAND B — CRM engagement layer =================
    by, bh = ay + ah + 20, 316
    bandfill = "#F2F7FC" if pf["key"] == "microsoft" else "#EFF8FD"
    s.append(band(midX, by, midW, bh, "CRM ENGAGEMENT LAYER", prim, bandfill, pf["tile_edge"]))
    apps = ("Dynamics 365 Customer Service · Sales · Contact Center"
            if pf["key"] == "microsoft"
            else "Service Cloud · Sales Cloud · Digital Engagement")
    s.append(txt(midX + 44, by + 26, "CRM Engagement Layer",
                 size=15, color=deep, weight="800"))
    s.append(txt(midX + 240, by + 26, f"— system of engagement · {apps}",
                 size=11, color=QIC["sub"], weight="500", italic=True))

    modules = [
        ("Customer 360 & Search", "QID·policy·mobile·email·enterprise ID", "user360"),
        ("Interaction Management", "structured logging · notes · audit trail", "case"),
        ("Case Management", "tickets · incidents · workflow history", "case"),
        ("SLA & Escalation Engine", "timers · reminders · multi-level", "clock"),
        ("Omnichannel Routing & Queues", "skill · capacity · priority", "route"),
        ("Sales, Leads & Accounts", "pipeline · corporate servicing · visits", "sales"),
        ("Dashboards & Reporting", "real-time · role-based · export", "pbi"),
        ("Configuration & Workflow", "dynamic forms · rules · notifications", "flow"),
    ]
    # product mapping subtitle differs per platform
    mapping = {
        "microsoft": ["Dataverse search", "Activities & timeline", "Cases + process flows",
                      "SLAs + entitlements", "Unified routing", "Dynamics 365 Sales",
                      "Power BI", "Power Apps + Power Automate"],
        "salesforce": ["Global search", "Case feed", "Case record types",
                       "Entitlements + milestones", "Omni-Channel", "Sales Cloud",
                       "CRM Analytics", "Lightning + Flow"],
    }[pf["key"]]
    glyphmap = {
        "user360": ("user360", ic_user360), "case": ("case", ic_case),
        "clock": ("clock", ic_clock), "route": ("route", ic_route),
        "sales": ("people", ic_people), "pbi": ("pbi", ic_chart), "flow": ("flow", ic_flow),
    }
    cols = 4
    ipad = 22
    igap = 15
    tw = (midW - 44 - ipad - cols * igap) / cols
    th = 108
    startx = midX + 44
    rowy = [by + 42, by + 42 + th + 14]
    for i, (name, sub, gk) in enumerate(modules):
        r_i = i // cols
        c_i = i % cols
        tx = startx + c_i * (tw + igap)
        ty = rowy[r_i]
        s.append(rrect(tx, ty, tw, th, r=11, fill="#ffffff", stroke=pf["tile_edge"], sw=1.4))
        s.append(f'<g filter="url(#dsSoft)">' + rrect(tx, ty, tw, th, r=11, fill="none") + '</g>')
        s.append(rrect(tx, ty, tw, 5, r=2.5, fill=prim))
        gkey, _ = glyphmap[gk]
        s.append(_icon_chip_small(gkey, prim, tx + 14, ty + 16, sz=32))
        s.append(txt(tx + 56, ty + 30, name, size=12.4, color=deep, weight="700"))
        wt, _ = wraptext(tx + 56, ty + 47, sub, 9.6, QIC["sub"], weight="500",
                         anchor="start", max_chars=30, lh=12)
        s.append(wt)
        # platform chip
        s.append(chip(tx + 14, ty + th - 26, tw - 28, 18, mapping[i], pf["chip_bg"],
                      text_color=pf["primary_dk"], size=9.6, r=9))
    # data foundation substrate label
    fnd = "Microsoft Dataverse — managed data platform & security model" if pf["key"] == "microsoft" \
        else "Salesforce Platform — data model, sharing & extensibility"
    s.append(rrect(startx, by + bh - 30, midW - 88, 20, r=10, fill=deep))
    s.append(txt(midX + midW/2, by + bh - 16, fnd, size=10.6, color="#fff",
                 weight="700", anchor="middle", spacing="0.5"))

    # ================= BAND C — integration & API =================
    cy, ch = by + bh + 20, 98
    s.append(band(midX, cy, midW, ch, "INTEGRATION", deep, "#FFFFFF", pf["tile_edge"]))
    s.append(txt(midX + 44, cy + 24, "Integration & API Layer",
                 size=15, color=deep, weight="800"))
    s.append(txt(midX + 250, cy + 24, f"— {pf['integ']} · API-led · real-time + batch · secured & monitored",
                 size=11, color=QIC["sub"], weight="500", italic=True))
    integ_chips = ({
        "microsoft": ["API Management", "Logic Apps", "Service Bus", "Key Vault", "Monitoring & retry"],
        "salesforce": ["Anypoint API Manager", "Reusable API assets", "Runtime & connectors",
                       "Secrets & policies", "Monitoring & retry"],
    })[pf["key"]]
    ncc = len(integ_chips)
    ccw = (midW - 60 - (ncc - 1) * 14) / ncc
    ccx = midX + 44
    for c in integ_chips:
        s.append(rrect(ccx, cy + 42, ccw, 38, r=9, fill=pf["chip_bg"], stroke=prim, sw=1.3))
        s.append(txt(ccx + ccw/2, cy + 65, c, size=11, color=pf["primary_dk"],
                     weight="700", anchor="middle"))
        ccx += ccw + 14

    # ================= BAND D — systems of record =================
    dy, dh = cy + ch + 20, bottom - (cy + ch + 20)
    s.append(band(midX, dy, midW, dh, "SYSTEMS", QIC["maroon"], "#F1F6FC", "#C7D8EC"))
    s.append(txt(midX + 44, dy + 26, "Systems of Record",
                 size=15, color=QIC["maroon_dk"], weight="800"))
    s.append(txt(midX + 214, dy + 26, "— authoritative sources · the CRM reads, and never becomes a second master",
                 size=11, color=QIC["sub"], weight="500", italic=True))
    sysrec = [
        ("Customer Master Database", "Enterprise single source of truth", "governed customer identity · read-only lookup",
         lambda x, y: ic_db(x, y, 1.7, c="#4C6B8A", check=True, lock=True), True),
        ("Azentio Core Insurance", "Policy & claims system of record", "policy · claims · customer reference",
         lambda x, y: ic_core(x, y, 1.7, c="#3F5D7A"), False),
        ("Payment Gateway — SkipCash", "Payment transaction references", "notifications · collections-ready",
         lambda x, y: ic_card(x, y, 1.7, c="#E08A2B"), False),
    ]
    npad = 44
    sgap = 22
    sw_ = (midW - npad - 22 - (len(sysrec) - 1) * sgap) / len(sysrec)
    sx = midX + npad
    for name, role, detail, icon, boundary in sysrec:
        sh = dh - 52
        sty = dy + 42
        s.append(rrect(sx, sty, sw_, sh, r=12, fill="#ffffff",
                       stroke=("#C79A3B" if boundary else "#C7D8EC"),
                       sw=(2.2 if boundary else 1.4)))
        s.append(f'<g filter="url(#dsSoft)">' + rrect(sx, sty, sw_, sh, r=12, fill="none") + '</g>')
        s.append(icon(sx + 20, sty + sh/2 - 22))
        s.append(txt(sx + 74, sty + 30, name, size=13.2, color=QIC["maroon_dk"], weight="800"))
        s.append(txt(sx + 74, sty + 49, role, size=10.4, color=QIC["ink"], weight="600"))
        s.append(txt(sx + 74, sty + 66, detail, size=9.6, color=QIC["sub"], weight="500"))
        if boundary:
            s.append(chip(sx + sw_ - 132, sty + 10, 120, 20, "CONSUME · NOT CREATE",
                          QIC["gold"], text_color="#3a2a06", size=9, r=10, weight="800"))
        sx += sw_ + sgap

    # ---- vertical flow arrows between bands ----
    ax1 = midX + midW * 0.5
    # channels -> CRM
    s.append(line(ax1, ay + ah, ax1, by, color=prim, w=3, marker="arrP"))
    # CRM <-> integration (down)
    s.append(line(ax1 - 60, by + bh, ax1 - 60, cy, color=prim, w=3, marker="arrP"))
    # integration -> systems (down)  and reads back (up)
    s.append(line(ax1 - 60, cy + ch, ax1 - 60, dy, color=prim, w=3, marker="arrP"))
    s.append(line(ax1 + 60, dy, ax1 + 60, cy + ch, color=QIC["gold"], w=3, marker="arrG"))
    s.append(line(ax1 + 60, cy, ax1 + 60, by + bh, color=QIC["gold"], w=3, marker="arrG"))
    s.append(txt(ax1 + 74, (cy + ch + dy)/2 + 4, "reads", size=9.5, color=QIC["gold"],
                 weight="700"))
    s.append(txt(ax1 - 46, (by + bh + cy)/2 + 4, "requests", size=9.5, color=pf["primary_dk"],
                 weight="700"))

    # ================= bottom strip: legend + NFR chips =================
    ly = bottom + 16
    s.append(legend(LX, ly, [
        ("box", prim, "Platform component (configured)"),
        ("line", prim, "Request / data to systems of record"),
        ("line", QIC["gold"], "Governed read-back to the CRM"),
    ], title="LEGEND", w=306))

    # NFR compliance chips
    nfrx = LX + 326
    s.append(rrect(nfrx, ly, RX - nfrx, 106, r=12, fill="#ffffff", stroke=QIC["line"], sw=1.3))
    s.append(txt(nfrx + 18, ly + 24, "NON-FUNCTIONAL COMPLIANCE — both options engineered to exceed",
                 size=12, color=QIC["ink"], weight="800", spacing="0.5"))
    nfrs = ["300+ concurrent users", "≤ 3s page response", "99.5% availability",
            "RPO ≤ 24h · RTO ≤ 4h", "Encryption · MFA · RBAC", "Full audit trail",
            "QCB · PDPPL · GDPR", "Regional data residency"]
    ncx = nfrx + 18
    ncy = ly + 40
    cwn = (RX - nfrx - 36 - 3 * 12) / 4
    for i, t in enumerate(nfrs):
        col = i % 4
        row = i // 4
        px = nfrx + 18 + col * (cwn + 12)
        py = ly + 40 + row * 30
        s.append(rrect(px, py, cwn, 24, r=6, fill=pf["chip_bg"], stroke=prim, sw=1))
        s.append(f'<circle cx="{px+13}" cy="{py+12}" r="6" fill="#1E9E5A"/>')
        s.append(txt(px + 13, py + 15.5, "✓", size=9, color="#fff", weight="900", anchor="middle"))
        s.append(txt(px + 24, py + 16, t, size=10, color=QIC["ink"], weight="600"))

    s.append(footer(pf, "Solution Architecture · 1 of 5"))
    s.append(canvas_close())
    return "".join(s)


if __name__ == "__main__":
    import sys
    pf = MS if sys.argv[1] == "ms" else SF
    save(build(pf), sys.argv[2])
    print("wrote", sys.argv[2])
