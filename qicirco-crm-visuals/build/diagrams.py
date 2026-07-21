# -*- coding: utf-8 -*-
"""Architecture / process diagrams 2-4 (mirrored for Microsoft & Salesforce)."""
import math
from kit import *


# icon dispatch for system/channel nodes
ICONS = dict(phone=ic_phone, whatsapp=ic_whatsapp, mail=ic_mail, web=ic_web,
             portal=ic_portal, card=ic_card, core=ic_core, walkin=ic_walkin)


def node(x, y, w, h, title, sub, iconfn, prim, edge, icon_c=None, boundary=False):
    s = [rrect(x, y, w, h, r=12, fill="#fff",
               stroke=(QIC["gold"] if boundary else edge), sw=(2.4 if boundary else 1.4))]
    s.append(f'<g filter="url(#dsSoft)">' + rrect(x, y, w, h, r=12, fill="none") + '</g>')
    s.append(rrect(x, y, w, 4, r=2, fill=(QIC["gold"] if boundary else prim)))
    s.append(iconfn(x + 14, y + h/2 - 15, 1.25, c=icon_c or prim))
    s.append(txt(x + 52, y + h/2 - 4, title, size=12.2, color=QIC["ink"], weight="800"))
    s.append(txt(x + 52, y + h/2 + 13, sub, size=9.4, color=QIC["sub"], weight="500"))
    if boundary:
        s.append(chip(x + w - 96, y + 8, 88, 16, "CONSUME ONLY", QIC["gold"],
                      text_color="#3a2a06", size=7.6, r=8, weight="800"))
    return "".join(s)


# ==================================================================== D2
def d2(pf):
    prim, deep = pf["primary"], pf["deep"]
    s = [canvas_open(pf)]
    s.append(header(pf, "INTEGRATION ARCHITECTURE",
                    "Enterprise Integration & Data Flow",
                    f"API-led connectivity · {pf['integ']} · the CRM consumes the customer master, never creates it"))
    cx0, cy0 = W/2, 588
    # integration ring
    ring_w, ring_h = 520, 250
    rx, ry = cx0 - ring_w/2, cy0 - ring_h/2
    s.append(rrect(rx, ry, ring_w, ring_h, r=24, fill=pf["chip_bg"], stroke=prim, sw=2, dash="8 5"))
    s.append(txt(cx0, ry + 24, f"INTEGRATION & API LAYER · {pf['integ'].upper()}",
                 size=12, color=pf["primary_dk"], weight="800", anchor="middle", spacing="1"))
    # integration capability chips inside ring (top)
    caps = ({"microsoft": ["API Management", "Logic Apps", "Service Bus", "Key Vault"],
             "salesforce": ["Anypoint API Mgr", "API assets", "Connectors", "Policies"]})[pf["key"]]
    cw = (ring_w - 40 - 3*10) / 4
    for i, c in enumerate(caps):
        s.append(rrect(rx + 20 + i*(cw+10), ry + 36, cw, 26, r=7, fill="#fff", stroke=prim, sw=1))
        s.append(txt(rx + 20 + i*(cw+10) + cw/2, ry + 53, c, size=8.8, color=pf["primary_dk"], weight="700", anchor="middle"))
    # CRM hub (center)
    hb_w, hb_h = 340, 120
    hx, hy = cx0 - hb_w/2, cy0 - hb_h/2 + 18
    s.append(rrect(hx, hy, hb_w, hb_h, r=16, fill="url(#pfBand)"))
    s.append(f'<g filter="url(#ds)">' + rrect(hx, hy, hb_w, hb_h, r=16, fill="none") + '</g>')
    s.append(platform_glyph(pf, hx + 40, hy + 44, 18))
    s.append(txt(hx + 74, hy + 40, "QICIRCO CRM", size=17, color="#fff", weight="800"))
    s.append(txt(hx + 74, hy + 60, pf["name"] + " · engagement layer", size=10.5, color="#DCE8F5", weight="500"))
    s.append(txt(hx + hb_w/2, hy + 92, "Interactions · cases · workflow · SLA · comms  (system of engagement)",
                 size=9.4, color="#EAF2FB", weight="500", anchor="middle"))

    # top channel nodes
    top_nodes = [
        ("3CX Telephony", "call log · screen-pop", "phone", "Events"),
        ("WhatsApp · WABA", "two-way messaging", "whatsapp", "Two-way", "#25D366"),
        ("Microsoft 365 / Outlook", "email · follow-up", "mail", "Two-way"),
        ("Shared mailboxes", "dept. comms", "mail", "Inbound"),
        ("Website & web forms", "enquiry capture", "web", "Inbound"),
        ("Insursa B2B/B2C portals", "servicing · visibility", "portal", "Two-way"),
    ]
    nw, nh = 232, 74
    ny = 168
    gapx = (W - 2*40 - 3*nw) / 2
    xs = [40, 40 + nw + gapx, 40 + 2*(nw + gapx)]
    # arrange 6 nodes: 3 on upper row, 3 slightly lower to avoid crowding -> actually 3 columns x 2 rows
    positions = []
    for r in range(2):
        for c in range(3):
            positions.append((xs[c], ny + r*92))
    for i, tn in enumerate(top_nodes):
        title, sub, ic, pat = tn[0], tn[1], tn[2], tn[3]
        icc = tn[4] if len(tn) > 4 else prim
        px, py = positions[i]
        s.append(node(px, py, nw, nh, title, sub, ICONS[ic], prim, pf["tile_edge"], icon_c=icc))
        # connector to ring top
        sx = px + nw/2
        sy = py + nh
        tx_ = cx0 + (px - cx0) * 0.12
        s.append(path(f"M{sx} {sy} C {sx} {sy+40}, {tx_} {ry-40}, {tx_} {ry}",
                      stroke=prim, sw=1.8, marker="arrP", opacity=0.8))
        s.append(chip(sx - 30, (sy + ry)/2 - 8, 60, 16, pat, "#fff", text_color=pf["primary_dk"],
                      size=8, r=8, edge=pf["tile_edge"]))

    # bottom systems of record
    bot_nodes = [
        ("Customer Master DB", "governed identity · 360", "core", "RT + Batch", True, "#4C6B8A"),
        ("Azentio Core Insurance", "policy · claims reference", "core", "RT + Batch", False, "#3F5D7A"),
        ("SkipCash Gateway", "payment notifications", "card", "Events", False, "#E08A2B"),
    ]
    bnw = 300
    bny = 900
    bxs = [cx0 - bnw*1.6, cx0 - bnw/2, cx0 + bnw*0.6]
    for i, (title, sub, ic, pat, boundary, icc) in enumerate(bot_nodes):
        px = bxs[i]
        s.append(node(px, bny, bnw, 78, title, sub, ICONS[ic], prim, pf["tile_edge"], icon_c=icc, boundary=boundary))
        sx = px + bnw/2
        # up to ring bottom
        col = QIC["gold"] if boundary else prim
        mk = "arrG" if boundary else "arrP"
        s.append(path(f"M{sx} {bny} C {sx} {bny-40}, {cx0 + (px-cx0)*0.1} {ry+ring_h+40}, {cx0 + (px-cx0)*0.1} {ry+ring_h}",
                      stroke=col, sw=2, marker=mk, opacity=0.85))
        s.append(chip(sx - 34, (bny + ry+ring_h)/2 - 8, 68, 16, pat, "#fff",
                      text_color=(QIC["maroon_dk"] if boundary else pf["primary_dk"]), size=7.8, r=8, edge=pf["tile_edge"]))
        if boundary:
            s.append(txt(sx, bny - 30, "read-only", size=9, color=QIC["gold"], weight="800", anchor="middle"))

    # left legend
    s.append(legend(40, 902, [
        ("line", prim, "Real-time / event API"),
        ("dash", prim, "Batch synchronization"),
        ("line", QIC["gold"], "Governed read-only (master)"),
    ], title="INTEGRATION PATTERNS", w=250))
    # right ownership panel
    ow = 300
    ox = W - 40 - ow
    s.append(rrect(ox, 902, ow, 150, r=12, fill="#fff", stroke=QIC["line"], sw=1.3))
    s.append(txt(ox + 16, 926, "DATA OWNERSHIP", size=11.5, color=QIC["ink"], weight="800", spacing="1"))
    own = [("Customer master", "Customer Master DB"), ("Policy & claims", "Azentio"),
           ("Interactions · cases · SLA", "CRM platform"), ("Payment references", "Gateway")]
    oy = 946
    for a, b in own:
        s.append(txt(ox + 16, oy + 12, a, size=9.6, color=QIC["ink"], weight="600"))
        s.append(txt(ox + ow - 16, oy + 12, b, size=9.6, color=prim, weight="700", anchor="end"))
        s.append(line(ox + 16, oy + 20, ox + ow - 16, oy + 20, color=QIC["line"], w=0.8))
        oy += 26
    s.append(footer(pf, "Integration & Data Flow · 2 of 5"))
    s.append(canvas_close())
    return "".join(s)


# ==================================================================== D3
def d3(pf):
    prim, deep = pf["primary"], pf["deep"]
    auto = pf["automation"]
    s = [canvas_open(pf)]
    s.append(header(pf, "BUSINESS PROCESS",
                    "Case Lifecycle · SLA & Escalation Workflow",
                    f"Omnichannel capture to audited resolution · automated with {auto}"))
    LX = 40
    RX = W - 40
    # top: omnichannel capture band
    cby = 132
    s.append(rrect(LX, cby, RX-LX, 66, r=12, fill=pf["chip_bg"], stroke=pf["tile_edge"], sw=1.3))
    s.append(txt(LX + 16, cby + 27, "OMNICHANNEL CAPTURE", size=11, color=pf["primary_dk"], weight="800", spacing="1"))
    chans = [("Voice · 3CX", ic_phone, prim), ("WhatsApp", ic_whatsapp, "#25D366"),
             ("Email · M365", ic_mail, prim), ("Web forms", ic_web, prim),
             ("Portals", ic_portal, prim), ("Walk-in", ic_walkin, prim)]
    cwn = (RX - LX - 230 - 5*12) / 6
    for i, (nm, icf, icc) in enumerate(chans):
        px = LX + 220 + i*(cwn+12)
        s.append(rrect(px, cby + 36, cwn, 22, r=7, fill="#fff", stroke=pf["tile_edge"], sw=1))
        s.append(icf(px + 6, cby + 39, 0.7, c=icc))
        s.append(txt(px + 24, cby + 51, nm, size=8.8, color=QIC["ink"], weight="600"))

    # main flow stages (row 1)
    fy = 236
    stages = [
        ("Identify customer", "match against\nCustomer Master DB", "user360"),
        ("Log interaction", "auto date · user ·\nchannel · audit", "case"),
        ("Classify", "Ticket (FCR)\nor Incident", "route"),
        ("Route to dept.", "rule-based\nqueue assignment", "route"),
        ("Work under SLA", "live timer ·\nreminders", "clock"),
        ("Resolve & close", "outcome ·\nsatisfaction check", "case"),
    ]
    n = len(stages)
    sw_ = (RX - LX - (n-1)*54) / n
    sh = 116
    def picto(key, x, y, c):
        m = {"user360": ic_user360, "case": ic_case, "route": ic_route, "clock": ic_clock}[key]
        return m(x, y, 1.5, c=c)
    xpos = []
    for i, (t, sub, ic) in enumerate(stages):
        px = LX + i*(sw_ + 54)
        xpos.append(px)
        boxc = prim
        s.append(rrect(px, fy, sw_, sh, r=12, fill="#fff", stroke=pf["tile_edge"], sw=1.5))
        s.append(f'<g filter="url(#dsSoft)">' + rrect(px, fy, sw_, sh, r=12, fill="none") + '</g>')
        s.append(rrect(px, fy, sw_, 5, r=2, fill=boxc))
        s.append(f'<circle cx="{px+26}" cy="{fy+30}" r="15" fill="{pf["chip_bg"]}"/>')
        s.append(picto(ic, px + 14, fy + 18, prim))
        s.append(f'<circle cx="{px+sw_-20}" cy="{fy+26}" r="12" fill="{deep}"/>')
        s.append(txt(px + sw_-20, fy + 30, str(i+1), size=12, color="#fff", weight="800", anchor="middle"))
        s.append(txt(px + 12, fy + 62, t, size=12.5, color=deep, weight="800"))
        for j, ln in enumerate(sub.split("\n")):
            s.append(txt(px + 12, fy + 80 + j*14, ln, size=9.4, color=QIC["sub"], weight="500"))
        if i < n-1:
            ax0 = px + sw_
            s.append(line(ax0, fy + sh/2, ax0 + 54, fy + sh/2, color=prim, w=2.4, marker="arrP"))
    # decision annotation on Classify (stage 3 index2)
    s.append(chip(xpos[2], fy - 22, 92, 18, "decision point", QIC["band"], text_color=deep, size=8.6, r=9, edge=QIC["line"]))
    # connector capture -> first stage
    s.append(line((LX+RX)/2, cby+66, (LX+RX)/2, fy-8, color=prim, w=2, marker="arrP", opacity=0.6))

    # departmental routing fan (below Route stage)
    dry = fy + sh + 40
    s.append(txt(LX, dry - 6, "DEPARTMENTAL ROUTING & OWNERSHIP", size=11, color=deep, weight="800", spacing="1"))
    depts = [("Customer Service", "agent → supervisor"), ("Sales & BD", "salesperson → BDM"),
             ("Underwriting", "underwriter → lead"), ("Claims", "claims → supervisor"),
             ("Complaints", "owner → management"), ("Corporate Servicing", "account → cross-dept")]
    dwn = (RX - LX - 5*14) / 6
    for i, (nm, own) in enumerate(depts):
        px = LX + i*(dwn+14)
        s.append(rrect(px, dry + 4, dwn, 60, r=10, fill="#fff", stroke=pf["tile_edge"], sw=1.3))
        s.append(rrect(px, dry + 4, 4, 60, r=2, fill=deep))
        s.append(txt(px + 14, dry + 28, nm, size=10.6, color=QIC["ink"], weight="800"))
        s.append(txt(px + 14, dry + 46, own, size=8.8, color=QIC["sub"], weight="500"))
        # connector from route stage (index3) down
        s.append(line(xpos[3] + sw_/2, fy + sh, px + dwn/2, dry + 4, color=deep, w=1, opacity=0.28))

    # SLA & escalation band (bottom)
    ey = dry + 84
    eh = 214
    half = (RX - LX - 16) / 2
    # SLA timers panel
    s.append(rrect(LX, ey, half, eh, r=12, fill="#fff", stroke=pf["tile_edge"], sw=1.4))
    s.append(rrect(LX, ey, 5, eh, r=2, fill=prim))
    s.append(txt(LX + 18, ey + 26, "SLA GOVERNANCE", size=11.5, color=deep, weight="800", spacing="1"))
    s.append(txt(LX + 18, ey + 46, "Timers by department · case type · priority · channel · category",
                 size=9.8, color=QIC["sub"], weight="500"))
    slas = [("Complaint · High", "30 min", "1 business day", "#C0392B"),
            ("Claims query · High", "1 hour", "1 business day", "#C0392B"),
            ("Service request · Med", "2 hours", "2 business days", "#E8A33D"),
            ("General enquiry · Low", "4 hours", "3 business days", "#0B875B")]
    syy = ey + 58
    for nm, resp, res, cc in slas:
        s.append(rrect(LX + 18, syy, half - 36, 30, r=6, fill=QIC["band"]))
        s.append(f'<circle cx="{LX+34}" cy="{syy+15}" r="5" fill="{cc}"/>')
        s.append(txt(LX + 48, syy + 19, nm, size=9.8, color=QIC["ink"], weight="700"))
        s.append(txt(LX + half - 36, syy + 19, f"{resp}  ·  {res}", size=9.4, color=prim, weight="700", anchor="end"))
        syy += 36
    # escalation ladder
    ex = LX + half + 16
    s.append(rrect(ex, ey, half, eh, r=12, fill="#fff", stroke=pf["tile_edge"], sw=1.4))
    s.append(rrect(ex, ey, 5, eh, r=2, fill=QIC["maroon"]))
    s.append(txt(ex + 18, ey + 26, "MULTI-LEVEL ESCALATION", size=11.5, color=QIC["maroon_dk"], weight="800", spacing="1"))
    s.append(txt(ex + 18, ey + 46, f"Automated by {auto} on threshold, breach or aging",
                 size=9.8, color=QIC["sub"], weight="500"))
    lvls = [("L1", "Case owner", prim), ("L2", "Supervisor", "#3E7CB1"),
            ("L3", "Dept. manager", "#E8A33D"), ("L4", "Management / board", "#C0392B")]
    lw2 = (half - 36 - 3*30) / 4
    lxx = ex + 18
    for i, (lv, who, cc) in enumerate(lvls):
        s.append(rrect(lxx, ey + 62, lw2, 60, r=10, fill="#fff", stroke=cc, sw=1.8))
        s.append(f'<circle cx="{lxx+lw2/2}" cy="{ey+82}" r="13" fill="{cc}"/>')
        s.append(txt(lxx + lw2/2, ey + 87, lv, size=12, color="#fff", weight="800", anchor="middle"))
        s.append(txt(lxx + lw2/2, ey + 112, who, size=8.6, color=QIC["ink"], weight="700", anchor="middle"))
        if i < 3:
            s.append(line(lxx + lw2, ey + 92, lxx + lw2 + 30, ey + 92, color=cc, w=2.4, marker="arr"))
        lxx += lw2 + 30
    s.append(txt(ex + 18, ey + eh - 14, "Notifications delivered in-CRM · email · WhatsApp · every action audited",
                 size=9.4, color=QIC["sub"], weight="500"))
    # automation scenarios band
    auy = ey + eh + 16
    auh = (H - FOOTER_H - 14) - auy
    s.append(rrect(LX, auy, RX-LX, auh, r=12, fill="url(#pfBand)"))
    s.append(txt(LX + 20, auy + 30, f"AUTOMATION SCENARIOS — configured with {auto}, no custom code",
                 size=12, color="#fff", weight="800", spacing="0.5"))
    autos = [("Auto case creation", "email · web · WhatsApp → case"),
             ("Duplicate prevention", "check vs customer master"),
             ("Rule-based routing", "→ correct department queue"),
             ("SLA timers", "start on create · track targets"),
             ("Reminders", "fire as thresholds approach"),
             ("Multi-level escalation", "breach / aging auto-climbs"),
             ("Notifications", "in-CRM · email · WhatsApp"),
             ("Follow-up tasks", "scheduled · nothing missed")]
    awn = (RX - LX - 40 - 3*12) / 4
    for i, (t, d) in enumerate(autos):
        col = i % 4; row = i // 4
        px = LX + 20 + col*(awn+12)
        py = auy + 44 + row*((auh-56)/2)
        s.append(rrect(px, py, awn, (auh-56)/2 - 8, r=8, fill="#ffffff", opacity=0.14))
        s.append(f'<circle cx="{px+16}" cy="{py+18}" r="7" fill="{QIC["gold"]}"/>')
        s.append(txt(px+16, py+21.5, str(i+1), size=9, color="#3a2a06", weight="900", anchor="middle"))
        s.append(txt(px + 30, py + 22, t, size=10.2, color="#fff", weight="800"))
        s.append(txt(px + 30, py + 38, d, size=8.6, color="#DCE8F5", weight="500"))
    s.append(footer(pf, "Case & SLA Process · 3 of 5"))
    s.append(canvas_close())
    return "".join(s)


# ==================================================================== D4
def d4(pf):
    prim, deep = pf["primary"], pf["deep"]
    s = [canvas_open(pf)]
    s.append(header(pf, "FUNCTIONAL CAPABILITY MAP",
                    "CRM Functional Capability Map",
                    f"Five capability domains · delivered by configuration on {pf['name']}"))
    LX, RX = 40, W - 40
    top = 132
    domains = [
        ("ENGAGEMENT", prim, [
            ("Customer 360 & search", "QID·policy·mobile·email·ID"),
            ("Interaction management", "structured logging · audit"),
            ("Omnichannel desk", "voice·WhatsApp·email·web"),
            ("Notifications", "in-app · email · WhatsApp")],
         "Contact Center + M365" if pf["key"]=="microsoft" else "Digital Engagement"),
        ("SERVICE & CASES", "#3E7CB1", [
            ("Ticket & incident", "classification · stages"),
            ("Routing & queues", "skill · capacity · dept."),
            ("SLA & escalation", "timers · multi-level"),
            ("Knowledge & FCR", "articles · first contact")],
         "Customer Service" if pf["key"]=="microsoft" else "Service Cloud"),
        ("SALES & ACCOUNTS", "#0B875B", [
            ("Leads & qualification", "capture · nurture"),
            ("Opportunity pipeline", "stages · value · forecast"),
            ("Corporate accounts", "ownership · servicing"),
            ("Visits & activities", "logging · follow-up")],
         "Dynamics 365 Sales" if pf["key"]=="microsoft" else "Sales Cloud"),
        ("INSIGHT & OPERATIONS", "#E8A33D", [
            ("Operational dashboards", "volumes · SLA · aging"),
            ("Management reporting", "performance · trends"),
            ("KPI monitoring", "FCR · resolution · workload"),
            ("AI assistance", pf["ai"] + " · governed")],
         pf["analytics"]),
        ("PLATFORM & GOVERNANCE", "#7A5CC0", [
            ("Config & low-code", "forms · flows · rules"),
            ("Security & RBAC", "roles · least privilege"),
            ("Audit & compliance", "QCB · PDPPL · GDPR"),
            ("Integration & API", pf["integ_short"])],
         "Power Platform" if pf["key"]=="microsoft" else "Salesforce Platform"),
    ]
    n = len(domains)
    gap = 16
    cw = (RX - LX - (n-1)*gap) / n
    ch_ = 686
    th = (ch_ - 68 - 44 - 3*10) / 4
    for i, (dname, dc, caps, prod) in enumerate(domains):
        x = LX + i*(cw + gap)
        s.append(rrect(x, top, cw, ch_, r=14, fill="#fff", stroke=QIC["line"], sw=1.4))
        s.append(f'<g filter="url(#dsSoft)">' + rrect(x, top, cw, ch_, r=14, fill="none") + '</g>')
        s.append(rrect(x, top, cw, 52, r=14, fill=dc))
        s.append(rrect(x, top + 30, cw, 22, fill=dc))
        s.append(txt(x + cw/2, top + 32, dname, size=12, color="#fff", weight="800", anchor="middle", spacing="0.5"))
        cyc = top + 68
        for cap, sub in caps:
            s.append(rrect(x + 12, cyc, cw - 24, th, r=10, fill=QIC["band"], stroke=QIC["line"], sw=1))
            s.append(rrect(x + 12, cyc, 4, th, r=2, fill=dc))
            wt, nl = wraptext(x + cw/2, cyc + th/2 - 8, cap, 12, deep, weight="800", anchor="middle", max_chars=18, lh=15)
            s.append(wt)
            wt2, _ = wraptext(x + cw/2, cyc + th/2 - 8 + nl*15 + 4, sub, 9.2, QIC["sub"], weight="500", anchor="middle", max_chars=24, lh=12)
            s.append(wt2)
            cyc += th + 10
        # product footer
        s.append(rrect(x + 12, top + ch_ - 40, cw - 24, 28, r=8, fill=pf["chip_bg"]))
        s.append(txt(x + cw/2, top + ch_ - 22, prod, size=9.6, color=pf["primary_dk"], weight="800", anchor="middle"))

    # bottom band: departments + foundation
    by = top + ch_ + 14
    bh = (H - FOOTER_H - 14) - by
    s.append(rrect(LX, by, RX-LX, bh, r=14, fill="url(#pfBand)"))
    s.append(txt(LX + 20, by + 30, "SERVING SIX OPERATIONAL DEPARTMENTS", size=12, color="#fff", weight="800", spacing="1"))
    deps = ["Customer Service", "Sales & Business Dev.", "Underwriting", "Claims", "Complaints", "Corporate Servicing"]
    dwn = (RX - LX - 40 - 5*10) / 6
    for i, d in enumerate(deps):
        px = LX + 20 + i*(dwn+10)
        s.append(rrect(px, by + 44, dwn, 30, r=8, fill="#ffffff", opacity=0.16))
        s.append(txt(px + dwn/2, by + 63, d, size=9.6, color="#fff", weight="700", anchor="middle"))
    sec = "Entra ID · Defender · Purview" if pf["key"] == "microsoft" else "Shield · Identity · Hyperforce"
    s.append(txt(LX + 20, by + bh - 16,
                 f"One governed platform · consumes the Customer Master DB · reads Azentio · {pf['integ']} · {sec} security · scales beyond 300 concurrent users",
                 size=9.6, color="#DCE8F5", weight="500"))
    s.append(footer(pf, "Functional Capability Map · 4 of 5"))
    s.append(canvas_close())
    return "".join(s)


if __name__ == "__main__":
    import sys
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    fns = {"d2": (d2, "02-integration"), "d3": (d3, "03-process"), "d4": (d4, "04-capability-map")}
    for key, (fn, slug) in fns.items():
        if which not in ("all", key):
            continue
        for pf, pk in [(MS, "ms"), (SF, "sf")]:
            save(fn(pf), f"../svg/{pk}-{slug}.svg")
            print("wrote", f"../svg/{pk}-{slug}.svg")
