# -*- coding: utf-8 -*-
"""Per-requirement platform-UI mockup cards for QICIRCO."""
from appkit import *
from kit import MS, SF, save


# ====================================================================== R1
R1 = dict(
    id="FR-1",
    headline="Customer 360 & Unified Customer Search",
    title="Customer 360 & Unified Search",
    sources=["RFP §5.1", "BRD §7.1 / §10.1", "Proposal FR-1"],
    text=[
        "Search customer records by QID, policy number, mobile, email and enterprise customer identifier.",
        "Present a governed 360° view: profile, policy references, claims status, servicing and follow-ups on one record.",
        "Consume the governed Customer Master Database — never create a second master.",
    ],
    addressed=[
        "Unified search bar resolves a customer across all five identifiers in one query.",
        "Profile is read live from the Customer Master DB — a badge marks it governed, read-only.",
        "Policy & claims context is surfaced inline from Azentio integration on the same record.",
        "Complete, auditable interaction history across every channel sits on the timeline.",
    ],
)


def c_r1(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    win, (cx, cy, cw, ch) = app_window(
        pf, ax, ay, aw, ah,
        "Customers  ›  Customer 360",
        "Ahmed Al-Kuwari")
    s = [win]
    pad = 16
    ix = cx + pad
    iw = cw - pad * 2
    # ---- search bar (callout 1) ----
    sby = cy + 12
    s.append(rrect(ix, sby, iw, 38, r=8, fill="#fff", stroke=prim, sw=1.6))
    s.append(mini_chip("search", prim, ix + 8, sby + 8, 22, cloud=(pf["key"] == "salesforce")))
    s.append(txt(ix + 40, sby + 24, "288**********   ·   search by  QID · Policy no. · Mobile · Email · Enterprise ID",
                 size=11.5, color=UI["ink"], weight="600"))
    s.append(rrect(ix + iw - 96, sby + 6, 88, 26, r=6, fill=prim))
    s.append(txt(ix + iw - 52, sby + 23, "Search", size=11, color="#fff", weight="700", anchor="middle"))
    s.append(callout(1, ix + iw - 110, sby + 19))

    # ---- record header ----
    ry = sby + 50
    rh = 74
    s.append(rrect(ix, ry, iw, rh, r=8, fill="#fff", stroke=UI["cardline"], sw=1.1))
    s.append(rrect(ix, ry, 4, rh, r=2, fill=prim))
    s.append(avatar(ix + 40, ry + rh/2, 22, "AK", deep))
    s.append(txt(ix + 74, ry + 28, "Ahmed Nasser Al-Kuwari", size=16, color=UI["ink"], weight="800"))
    s.append(txt(ix + 74, ry + 48, "Enterprise ID  QIC-CUST-004182", size=10.6, color=UI["sub"], weight="600"))
    # badges
    bx = ix + 74
    for lbl, fc, tc in [("Active customer", "#E4F5EC", "#0B875B"),
                        ("Corporate · Motor & Medical", "#EAF2FB", prim),
                        ("VIP tier", "#FBF1DA", "#8A6D1E")]:
        bw = len(lbl) * 6.0 + 20
        s.append(rrect(bx, ry + 54, bw, 16, r=8, fill=fc))
        s.append(txt(bx + bw/2, ry + 65.5, lbl, size=8.8, color=tc, weight="700", anchor="middle"))
        bx += bw + 6
    # governed badge (callout 2)
    gbw = 176
    s.append(rrect(ix + iw - gbw - 12, ry + 14, gbw, 30, r=8, fill="#FBF4F6", stroke=GOLD, sw=1.4))
    s.append(mini_chip("lock", GOLD, ix + iw - gbw - 2, ry + 18, 20))
    s.append(txt(ix + iw - gbw + 22, ry + 27, "Governed by Customer", size=9.6, color=QIC["maroon_dk"], weight="700"))
    s.append(txt(ix + iw - gbw + 22, ry + 39, "Master DB · read-only", size=9.6, color=QIC["maroon_dk"], weight="700"))
    s.append(callout(2, ix + iw - gbw - 12, ry + 14))

    # ---- three columns ----
    colY = ry + rh + 12
    band_h = 150
    colH = cy + ch - colY - 14 - band_h - 12
    gap = 12
    c1w = iw * 0.30
    c2w = iw * 0.36
    c3w = iw - c1w - c2w - gap * 2
    x1 = ix
    x2 = ix + c1w + gap
    x3 = x2 + c2w + gap

    # col1 profile
    s.append(card(x1, colY, c1w, colH, "Profile", "user360", prim, pf=pf))
    fy = colY + 54
    for lb, vv in [("QID / National ID", "288 74 06 12345"),
                   ("Mobile", "+974 5512 8890"),
                   ("Email", "a.alkuwari@qatar.example"),
                   ("Date of birth", "14 Mar 1979"),
                   ("Nationality", "Qatari"),
                   ("Address", "West Bay, Doha"),
                   ("Preferred channel", "WhatsApp · Arabic"),
                   ("Relationship owner", "N. Al-Sadi (Corp.)"),
                   ("Segment / tier", "Corporate · VIP"),
                   ("KYC status", "Verified · 2025"),
                   ("Marketing consent", "Granted · WhatsApp")]:
        vc = UI["green"] if lb == "KYC status" else UI["ink"]
        s.append(field(x1 + 14, fy, c1w - 28, lb, vv, vcolor=vc))
        fy += 40

    # col2 policies + claims (callout 3)
    s.append(card(x2, colY, c2w, colH, "Policies & Claims", "case", prim, pf=pf))
    s.append(chip(x2 + c2w - 118, colY + 12, 106, 18, "via Azentio", "#EAF2FB",
                  text_color=prim, size=8.8, r=9))
    s.append(callout(3, x2 + c2w - 12, colY + 12))
    # premium summary tiles
    tw = (c2w - 24 - 12) / 2
    s.append(stat_tile(x2 + 12, colY + 50, tw, 54, "QAR 48,600", "Annual premium", prim, sub="3 active policies"))
    s.append(stat_tile(x2 + 24 + tw, colY + 50, tw, 54, "12 Aug", "Next renewal", UI["amber"], sub="Motor · P-MOT-2291"))
    py = colY + 116
    pol = [("P-MOT-2291", "Motor · Comprehensive", "QAR 6,200 · renews 12 Aug", "Active", UI["green"]),
           ("P-MED-1188", "Medical · Family floater", "QAR 31,400 · renews 03 Nov", "Active", UI["green"]),
           ("P-GRP-3390", "Group life · corporate", "QAR 11,000 · renews 01 Jan", "Active", UI["green"]),
           ("P-PRP-0774", "Property · Home", "QAR 2,050 · lapsed 30 Jun", "Lapsed", UI["amber"])]
    for no, ln, prem, st, stc in pol:
        s.append(rrect(x2 + 12, py, c2w - 24, 46, r=6, fill=UI["field"], stroke=UI["cardline"], sw=1))
        s.append(txt(x2 + 22, py + 17, no, size=11, color=UI["ink"], weight="800"))
        s.append(txt(x2 + 22, py + 32, ln, size=9.2, color=UI["sub"], weight="500"))
        s.append(txt(x2 + 22, py + 43, prem, size=8.4, color=UI["faint"], weight="500"))
        s.append(chip(x2 + c2w - 84, py + 13, 60, 17, st, "#fff", text_color=stc, size=9, r=8))
        s.append(f'<circle cx="{x2+c2w-90}" cy="{py+21.5}" r="3.5" fill="{stc}"/>')
        py += 52
    # claim
    s.append(line(x2 + 12, py + 2, x2 + c2w - 12, py + 2, color=UI["cardline"], w=1))
    s.append(txt(x2 + 22, py + 22, "OPEN CLAIM", size=9, color=UI["faint"], weight="700", spacing="0.5"))
    s.append(txt(x2 + 22, py + 39, "CLM-4471 · Motor · own-damage", size=11, color=UI["ink"], weight="700"))
    s.append(chip(x2 + c2w - 108, py + 25, 92, 17, "In assessment", "#FBF1DA",
                  text_color="#8A6D1E", size=8.8, r=8))

    # col3 interaction timeline (callout 4)
    s.append(card(x3, colY, c3w, colH, "Interaction history", "clock", prim, pf=pf))
    s.append(callout(4, x3 + c3w - 12, colY + 12))
    ty = colY + 52
    tl = [("whatsapp", "#25D366", "WhatsApp — renewal query", "Handled by S. Kamal", "2h", "Resolved"),
          ("phone", prim, "Inbound call · 3CX", "Motor policy change request", "1d", "Logged"),
          ("mail", prim, "Email — medical card reissue", "Follow-up scheduled", "3d", "Follow-up"),
          ("case", prim, "Case #INC-2043 opened", "Property lapse review", "5d", "In progress"),
          ("whatsapp", "#25D366", "WhatsApp — payment link sent", "SkipCash · QAR 6,200", "6d", "Delivered"),
          ("people", prim, "Branch visit — Doha West Bay", "Corporate servicing review", "1w", "Closed"),
          ("mail", prim, "Email — welcome / group life", "Onboarding pack", "2w", "Sent")]
    for g, gc, tt, sub, wn, tg in tl:
        s.append(timeline_item(x3 + 12, ty, c3w - 24, g, gc, tt, sub, wn, tag=tg))
        ty += 50
    # quick log bar
    qy = colY + colH - 42
    s.append(rrect(x3 + 12, qy, c3w - 24, 30, r=6, fill=pf["chip_bg"], stroke=prim, sw=1.2))
    s.append(txt(x3 + 24, qy + 19, "+  Log interaction", size=10.5, color=pf["primary_dk"], weight="700"))
    s.append(txt(x3 + c3w - 24, qy + 19, "auto: date · user · channel", size=8.8,
                 color=UI["sub"], weight="500", anchor="end"))

    # ---- bottom band: one customer, five identifiers + governed provenance ----
    byy = colY + colH + 12
    half = (iw - 12) / 2
    # left: five identifiers -> one record
    s.append(card(ix, byy, half, band_h, "One customer · five identifiers", "search", prim, pf=pf))
    ids = ["QID / National ID", "Policy number", "Mobile", "Email", "Enterprise ID"]
    cyy = byy + 56
    for i, idl in enumerate(ids):
        s.append(rrect(ix + 16, cyy + i * 17.5, 150, 15, r=7, fill=UI["field"], stroke=prim, sw=1))
        s.append(txt(ix + 22, cyy + i * 17.5 + 11, idl, size=8.8, color=UI["ink"], weight="600"))
        s.append(line(ix + 168, cyy + i * 17.5 + 7.5, ix + 210, byy + band_h/2 + 6,
                      color=prim, w=1.2, marker="arrP", opacity=0.55))
    s.append(rrect(ix + 214, byy + band_h/2 - 12, half - 232, 46, r=8, fill=prim))
    s.append(txt(ix + 214 + (half - 232)/2, byy + band_h/2 + 3, "Single golden",
                 size=11.5, color="#fff", weight="800", anchor="middle"))
    s.append(txt(ix + 214 + (half - 232)/2, byy + band_h/2 + 20, "customer record",
                 size=11.5, color="#fff", weight="800", anchor="middle"))
    # right: governed provenance
    px2 = ix + half + 12
    s.append(card(px2, byy, half, band_h, "Governed 360 — assembled from", "lock", GOLD, pf=pf))
    prov = [("Customer Master DB", "identity · profile · segment", "#4C6B8A", "read-only"),
            ("Azentio Core Insurance", "policies · claims references", "#3F5D7A", "read-only"),
            ("CRM engagement layer", "interactions · cases · follow-ups", prim, "owned by CRM")]
    pvy = byy + 52
    for nm, ds, cc, tg in prov:
        s.append(rrect(px2 + 16, pvy, half - 32, 26, r=6, fill=UI["field"], stroke=UI["cardline"], sw=1))
        s.append(f'<circle cx="{px2+30}" cy="{pvy+13}" r="5" fill="{cc}"/>')
        s.append(txt(px2 + 44, pvy + 11, nm, size=10, color=UI["ink"], weight="700"))
        s.append(txt(px2 + 44, pvy + 21, ds, size=8.4, color=UI["sub"], weight="500"))
        tgc = GOLD if tg != "owned by CRM" else prim
        s.append(chip(px2 + half - 108, pvy + 5, 92, 16, tg,
                      "#FBF4F6" if tg != "owned by CRM" else pf["chip_bg"],
                      text_color=QIC["maroon_dk"] if tg != "owned by CRM" else pf["primary_dk"],
                      size=8.2, r=8))
        pvy += 30

    return "".join(s)


def _content(pf, ax, ay, aw, ah, breadcrumb, record):
    win, box = app_window(pf, ax, ay, aw, ah, breadcrumb, record)
    return win, box


# ====================================================================== R2
R2 = dict(
    id="FR-2", headline="Structured Interaction Logging & Audit Trail",
    title="Interaction Logging & Audit",
    sources=["RFP §5.1", "BRD §7.2 / §11.7", "Proposal FR-2"],
    text=["Structured logging with date/time, channel, category, reason, outcome, follow-up, notes and attachments.",
          "Mandatory-field validation, timestamps and user stamps on every interaction.",
          "Complete, immutable audit trail for interactions, workflow and access."],
    addressed=["Guided form enforces mandatory fields before an interaction can be saved.",
               "Date, time and handling user are stamped automatically — the agent records only what can't be inferred.",
               "Notes and attachments are captured on the same record.",
               "Every create, edit and status change is written to an immutable audit trail."],
)


def c_r2(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, "Interactions  ›  New interaction", "New interaction")
    s = [win]
    ix, iw = cx + 16, cw - 32
    gap = 14
    mw = iw * 0.6
    rw = iw - mw - gap
    top = cy + 14
    mh = cy + ch - top - 14
    # form
    s.append(card(ix, top, mw, mh, "Log interaction", "case", prim, pf=pf))
    s.append(chip(ix + mw - 96, top + 12, 84, 18, "Unsaved", "#FBF1DA", text_color="#8A6D1E", size=9, r=9))
    fx, fy = ix + 16, top + 54
    fw = (mw - 32 - 12) / 2
    fields = [("Channel *", "WhatsApp (WABA)", True), ("Direction *", "Inbound", True),
              ("Category *", "Policy servicing", True), ("Reason *", "Renewal enquiry", True),
              ("Related customer *", "Ahmed Al-Kuwari", True), ("Related policy", "P-MOT-2291", False),
              ("Assigned user", "S. Kamal (auto)", False), ("Outcome *", "Resolved – FCR", True)]
    for i, (lb, vv, mand) in enumerate(fields):
        col = i % 2
        row = i // 2
        bx = fx + col * (fw + 12)
        by = fy + row * 52
        s.append(field_box(bx, by, fw, lb, vv, vcolor=deep if mand else UI["ink"]))
    # notes
    ny = fy + 4 * 52 + 4
    s.append(rrect(fx, ny, mw - 32, 74, r=6, fill=UI["field"], stroke=UI["cardline"], sw=1))
    s.append(txt(fx + 12, ny + 17, "NOTES", size=8.6, color=UI["faint"], weight="700"))
    s.append(txt(fx + 12, ny + 36, "Customer requested motor renewal quote; payment link", size=10.4, color=UI["ink"], weight="500"))
    s.append(txt(fx + 12, ny + 51, "sent via SkipCash. Follow-up if unpaid in 48h.", size=10.4, color=UI["ink"], weight="500"))
    # attachments + follow-up
    ay2 = ny + 84
    s.append(rrect(fx, ay2, fw, 30, r=6, fill="#fff", stroke=UI["cardline"], sw=1))
    s.append(txt(fx + 12, ay2 + 19, "📎  renewal-quote.pdf", size=9.6, color=prim, weight="600"))
    s.append(callout(3, fx + fw - 8, ay2 + 4))
    s.append(rrect(fx + fw + 12, ay2, fw, 30, r=6, fill="#fff", stroke=UI["cardline"], sw=1))
    s.append(txt(fx + fw + 24, ay2 + 19, "Follow-up: 12 Aug ✓", size=9.6, color=UI["ink"], weight="600"))
    # validation banner + save (callout 1)
    vb = ay2 + 40
    s.append(rrect(fx, vb, mw - 32, 28, r=6, fill="#FDECEC", stroke="#E7B4B4", sw=1))
    s.append(txt(fx + 12, vb + 18, "!  4 mandatory fields required before save", size=9.8, color="#B4342B", weight="700"))
    s.append(callout(1, fx + 6, vb + 14))
    s.append(rrect(ix + mw - 108, vb - 2, 92, 30, r=6, fill=prim))
    s.append(txt(ix + mw - 62, vb + 17, "Save & log", size=10.5, color="#fff", weight="700", anchor="middle"))
    # auto-stamp chip (callout 2)
    s.append(rrect(fx, top + mh - 40, mw - 32, 26, r=6, fill=pf["chip_bg"]))
    s.append(txt(fx + 12, top + mh - 23, "Auto-captured:  21 Jul 2026 · 10:42 · S. Kamal · WhatsApp", size=9.6, color=pf["primary_dk"], weight="600"))
    s.append(callout(2, fx + 6, top + mh - 40))
    # audit trail (callout 4)
    axr = ix + mw + gap
    s.append(card(axr, top, rw, mh, "Audit trail", "lock", GOLD, pf=pf))
    s.append(callout(4, axr + rw - 12, top + 12))
    aty = top + 52
    aud = [("case", prim, "Interaction created", "S. Kamal · WhatsApp", "10:42"),
           ("flow", prim, "Field 'Outcome' set", "Resolved – FCR", "10:44"),
           ("bell", prim, "Follow-up task created", "Due 12 Aug", "10:44"),
           ("mail", prim, "Payment link sent", "SkipCash · QAR 6,200", "10:45"),
           ("lock", GOLD, "Record locked & hashed", "immutable entry", "10:45"),
           ("people", prim, "Viewed by supervisor", "N. Al-Sadi", "11:10")]
    for g, gc, tt, sub, wn in aud:
        s.append(timeline_item(axr + 12, aty, rw - 24, g, gc, tt, sub, wn))
        aty += 50
    return "".join(s)


# ====================================================================== R3
R3 = dict(
    id="FR-3", headline="Ticket & Incident Case Management",
    title="Ticket vs Incident + Workflow",
    sources=["RFP §5.2", "BRD §7.3 / §11.1", "Proposal FR-3"],
    text=["Classify interactions into tickets (first-contact resolution) and incidents (escalation / follow-up).",
          "Configurable workflow stages, status transitions, department routing and follow-up ownership.",
          "Workflow history, reassignment visibility and complete audit trail."],
    addressed=["A case is classified as ticket or incident; the process flow drives the stages.",
               "Configurable stage bar enforces status transitions and required steps.",
               "When a ticket can't be resolved it escalates to an incident, carrying full history forward.",
               "Every reassignment and status change is recorded on the workflow history."],
)


def c_r3(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    plat = "Business process flow" if pf["key"] == "microsoft" else "Path"
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, "Cases  ›  INC-2043", "INC-2043")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    # record header
    s.append(rrect(ix, top, iw, 56, r=8, fill="#fff", stroke=UI["cardline"], sw=1.1))
    s.append(rrect(ix, top, 4, 56, r=2, fill=prim))
    s.append(mini_chip("case", prim, ix + 14, top + 14, 28, cloud=(pf["key"] == "salesforce")))
    s.append(txt(ix + 54, top + 24, "INC-2043 · Property lapse review", size=15, color=UI["ink"], weight="800"))
    s.append(txt(ix + 54, top + 43, "Ahmed Al-Kuwari · Complaints Management · opened 5d ago", size=10, color=UI["sub"], weight="500"))
    s.append(chip(ix + iw - 210, top + 18, 92, 20, "Incident", "#FDECEC", text_color="#B4342B", size=10, r=10))
    s.append(chip(ix + iw - 110, top + 18, 96, 20, "Priority: High", "#FBF1DA", text_color="#8A6D1E", size=9.4, r=10))
    # chevrons (callout 2)
    chy = top + 66
    s.append(sect(ix, chy - 4, plat))
    s.append(chevrons(ix, chy + 4, iw, 34, ["Logged", "Ticket (FCR)", "Incident", "In progress", "Resolved", "Closed"], 3, prim, done_color="#3E7CB1"))
    s.append(callout(2, ix + iw * 0.42, chy + 4))
    # body: left detail, right workflow history
    by = chy + 52
    bh = cy + ch - by - 14
    gap = 14
    mw = iw * 0.56
    rw = iw - mw - gap
    # classification card (callout 1)
    s.append(card(ix, by, mw, bh, "Case detail & classification", "route", prim, pf=pf))
    s.append(callout(1, ix + mw - 12, by + 12))
    fx = ix + 16
    fw = (mw - 32 - 12) / 2
    dets = [("Type", "Incident"), ("Origin", "Ticket TKT-1990"), ("Department", "Complaints"),
            ("Owner / queue", "M. Haddad"), ("Channel", "WhatsApp"), ("SLA", "1 business day"),
            ("Category", "Policy lapse"), ("Sub-reason", "Auto-renew failed")]
    for i, (lb, vv) in enumerate(dets):
        col = i % 2; row = i // 2
        s.append(field_box(fx + col * (fw + 12), by + 52 + row * 50, fw, lb, vv))
    # ticket/incident toggle
    tgy = by + 52 + 4 * 50 + 2
    s.append(rrect(fx, tgy, mw - 32, 34, r=8, fill=UI["field"], stroke=UI["cardline"], sw=1))
    s.append(rrect(fx + 3, tgy + 3, (mw - 38) / 2, 28, r=6, fill="#fff", stroke=UI["cardline"], sw=1))
    s.append(txt(fx + 3 + (mw - 38) / 4, tgy + 22, "Ticket · FCR", size=10, color=UI["sub"], weight="600", anchor="middle"))
    s.append(rrect(fx + 3 + (mw - 38) / 2, tgy + 3, (mw - 38) / 2, 28, r=6, fill=prim))
    s.append(txt(fx + 3 + (mw - 38) * 0.75, tgy + 22, "Incident · escalated", size=10, color="#fff", weight="700", anchor="middle"))
    # escalation note (callout 3)
    eny = tgy + 44
    s.append(rrect(fx, eny, mw - 32, 30, r=6, fill="#FBF4F6", stroke=GOLD, sw=1.2))
    s.append(txt(fx + 12, eny + 19, "Escalated from ticket TKT-1990 — history carried forward", size=9.8, color=QIC["maroon_dk"], weight="700"))
    s.append(callout(3, fx + 6, eny + 15))
    # workflow history (callout 4)
    axr = ix + mw + gap
    s.append(card(axr, by, rw, bh, "Workflow & audit history", "clock", prim, pf=pf))
    s.append(callout(4, axr + rw - 12, by + 12))
    hy = by + 52
    hist = [("case", "#3E7CB1", "Ticket TKT-1990 raised", "Call · agent L. Fahad", "5d"),
            ("bolt", GOLD, "Escalated → Incident", "FCR not achieved", "5d"),
            ("route", prim, "Routed to Complaints", "rule: lapse > 30d", "5d"),
            ("people", prim, "Assigned to M. Haddad", "by supervisor", "4d"),
            ("flow", prim, "Status → In progress", "SLA timer started", "4d"),
            ("people", prim, "Reassigned", "M. Haddad → team", "2d"),
            ("mail", prim, "Customer update sent", "WhatsApp", "1d")]
    for g, gc, tt, sub, wn in hist:
        s.append(timeline_item(axr + 12, hy, rw - 24, g, gc, tt, sub, wn))
        hy += 50
    return "".join(s)


# ====================================================================== R4
R4 = dict(
    id="FR-5", headline="SLA Timers, Reminders & Multi-level Escalation",
    title="SLA & Escalation Management",
    sources=["RFP §5.3 / §10.3", "BRD §11.3 / §13", "Proposal FR-5"],
    text=["Configure SLA by department, case type, priority, channel and interaction category.",
          "Live timers, reminders as thresholds approach and automated breach alerts.",
          "Automated multi-level escalation with supervisor and management visibility."],
    addressed=["Each case carries a live SLA timer for response and resolution targets.",
               "Reminders fire automatically as thresholds approach, reducing avoidable breaches.",
               "On breach, escalation climbs automatically through a configured multi-level path.",
               "SLA rules are defined by department, priority, channel and case type."],
)


def c_r4(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, "Cases  ›  INC-2051 · SLA", "INC-2051")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    gap = 14
    lw = iw * 0.33
    mwd = iw * 0.34
    rw = iw - lw - mwd - gap * 2
    bh = 328
    # left: SLA timers (callout 1/2)
    s.append(card(ix, top, lw, bh, "Live SLA timers", "clock", prim, pf=pf))
    s.append(callout(1, ix + lw - 12, top + 12))
    s.append(gauge_ring(ix + lw/2, top + 104, 48, 0.72, "#C0392B", "Resolution SLA · High", "01:07"))
    s.append(txt(ix + lw/2, top + 186, "of 1 business day target", size=9.4, color=UI["sub"], weight="600", anchor="middle"))
    s.append(rrect(ix + 16, top + 200, lw - 32, 44, r=6, fill="#E4F5EC"))
    s.append(txt(ix + 28, top + 218, "✓ First response met", size=9.8, color="#0B875B", weight="700"))
    s.append(txt(ix + 28, top + 233, "22 min · target 30 min", size=8.8, color="#0B875B", weight="500"))
    s.append(rrect(ix + 16, top + 250, lw - 32, 44, r=6, fill="#FBF1DA"))
    s.append(txt(ix + 28, top + 268, "⏰ Reminder sent · 75% threshold", size=9.6, color="#8A6D1E", weight="700"))
    s.append(txt(ix + 28, top + 283, "escalation arms automatically", size=8.8, color="#8A6D1E", weight="500"))
    s.append(callout(2, ix + 10, top + 250))
    # middle: escalation ladder (callout 3)
    s.append(card(ix + lw + gap, top, mwd, bh, "Escalation path", "bolt", prim, pf=pf))
    s.append(callout(3, ix + lw + gap + mwd - 12, top + 12))
    lvls = [("L1 · Case owner", "M. Haddad · on assignment", "#3E7CB1", True),
            ("L2 · Supervisor", "N. Al-Sadi · at 75% / reassign", prim, True),
            ("L3 · Dept. manager", "Complaints mgr · on breach", "#E8A33D", True),
            ("L4 · Management / board", "Ops committee · critical breach", "#C0392B", False)]
    ely = top + 56
    exm = ix + lw + gap + 30
    for i, (lv, who, cc, done) in enumerate(lvls):
        s.append(f'<circle cx="{exm}" cy="{ely+14}" r="10" fill="{cc if done else "#fff"}" stroke="{cc}" stroke-width="2.4"/>')
        if done:
            s.append(txt(exm, ely + 18, "✓", size=11, color="#fff", weight="900", anchor="middle"))
        if i < 3:
            s.append(line(exm, ely + 26, exm, ely + 56, color=cc, w=2.4, dash="3 3"))
        s.append(txt(exm + 22, ely + 11, lv, size=11, color=UI["ink"], weight="800"))
        s.append(txt(exm + 22, ely + 27, who, size=9.2, color=UI["sub"], weight="500"))
        ely += 66
    # right: notifications (callout)
    rxr = ix + lw + mwd + gap * 2
    s.append(card(rxr, top, rw, bh, "Automated alerts", "bell", prim, pf=pf))
    ny = top + 56
    alerts = [("bell", prim, "Reminder → owner", "75% of SLA elapsed", "now"),
              ("mail", prim, "Breach warning → supervisor", "email + in-app", "12m"),
              ("whatsapp", "#25D366", "Customer update", "WhatsApp WABA", "15m"),
              ("bolt", "#C0392B", "Escalation → manager", "auto multi-level", "—")]
    for g, gc, tt, sub, wn in alerts:
        s.append(timeline_item(rxr + 12, ny, rw - 24, g, gc, tt, sub, wn))
        ny += 62
    # bottom: SLA matrix (callout 4)
    my = top + bh + 14
    mh = cy + ch - my - 14
    s.append(card(ix, my, iw, mh, "Configurable SLA matrix — by department · priority · channel · case type", "clock", prim, pf=pf))
    s.append(callout(4, ix + iw - 12, my + 12))
    cols = ["Case type", "Dept.", "Priority", "Channel", "Response", "Resolution", "Escalation"]
    colw = [iw*0.18, iw*0.15, iw*0.11, iw*0.16, iw*0.12, iw*0.14, iw*0.12]
    rows = [["Complaint", "Complaints", ("High", "#C0392B"), "Any", "30 min", "1 business day", "L1→L4"],
            ["Claims servicing query", "Claims", ("High", "#C0392B"), "Voice / WhatsApp", "1 hour", "1 business day", "L1→L3"],
            ["Service request", "Customer Service", ("Medium", "#E8A33D"), "Any", "2 hours", "2 business days", "L1→L2"],
            ["Underwriting query", "Underwriting", ("Medium", "#E8A33D"), "Email / portal", "2 hours", "2 business days", "L1→L2"],
            ["General enquiry", "Customer Service", ("Low", "#0B875B"), "Any", "4 hours", "3 business days", "L1"]]
    s.append(table(ix + 12, my + 48, iw - 24, cols, rows, colw, rowh=(mh-60)/6))
    return "".join(s)


# ====================================================================== R5
R5 = dict(
    id="FR-6", headline="Omnichannel Engagement — One Agent Workspace",
    title="Omnichannel Engagement",
    sources=["RFP §5.4", "BRD §7.6 / §9.4", "Proposal FR-6"],
    text=["Voice (3CX), WhatsApp (WABA), email, shared mailboxes, web forms, portals and walk-ins on one desk.",
          "Unified interaction visibility across channels, linked to the customer record.",
          "Extensible for future digital communication channels."],
    addressed=["All channels feed one prioritized agent worklist and routing model.",
               "WhatsApp Business API supports two-way messaging threaded to the customer.",
               "Every conversation is linked to the customer record and case automatically.",
               "Customer context travels with the conversation across channels."],
)


def c_r5(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    tool = "Contact Center" if pf["key"] == "microsoft" else "Omni-Channel"
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, f"{tool}  ›  Agent workspace", "Workspace")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    gap = 14
    lw = iw * 0.28
    mwd = iw * 0.42
    rw = iw - lw - mwd - gap * 2
    bh = cy + ch - top - 14
    # left: unified worklist (callout 1)
    s.append(card(ix, top, lw, bh, f"My work · {tool}", "route", prim, pf=pf))
    s.append(callout(1, ix + lw - 12, top + 12))
    convs = [("whatsapp", "#25D366", "Ahmed Al-Kuwari", "WhatsApp · renewal", "0:12", True, "Active", None),
             ("phone", prim, "Fatima Al-Ansari", "Voice · 3CX", "wait", False, "Ringing", "#FBF1DA"),
             ("mail", prim, "Group HR — Ooredoo", "Email · medical", "5m", False, "Open", None),
             ("web", prim, "Web form #WF-882", "Motor quote", "8m", False, "New", None),
             ("portal", prim, "Insursa portal", "Claim status", "12m", False, "Open", None),
             ("whatsapp", "#25D366", "K. Rahman", "WhatsApp · complaint", "20m", False, "Queued", None)]
    wy = top + 50
    for g, gc, nm, sub, meta, act, tag, tc in convs:
        s.append(inbox_row(ix + 8, wy, lw - 16, 46, g, gc, nm, sub, meta, active=act, tag=tag,
                           tag_c=tc or ("#EAF3EA")))
        wy += 48
    s.append(rrect(ix + 8, wy + 6, lw - 16, 26, r=6, fill=pf["chip_bg"]))
    s.append(txt(ix + lw/2, wy + 23, "6 channels · 1 unified queue", size=9.4, color=pf["primary_dk"], weight="700", anchor="middle"))
    # middle: WhatsApp conversation (callout 2)
    mxr = ix + lw + gap
    s.append(card(mxr, top, mwd, bh, "WhatsApp · Ahmed Al-Kuwari (WABA)", "whatsapp", "#25D366", pf=pf))
    s.append(callout(2, mxr + mwd - 12, top + 12))
    bubbles = [(False, "Hello, I'd like to renew my motor policy P-MOT-2291.", "10:38"),
               (True, "Certainly. Your renewal premium is QAR 6,200, valid to 12 Aug.", "10:39"),
               (False, "Can you send a payment link?", "10:40"),
               (True, "Here is your secure SkipCash link. Anything else?", "10:41"),
               (False, "That's all, thank you!", "10:42")]
    byb = top + 54
    for mine, tx_, wn in bubbles:
        bw = min(mwd - 90, 26 + len(tx_) * 5.0)
        bxb = mxr + mwd - 24 - bw if mine else mxr + 20
        fc = "#DCF8C6" if mine else "#F1F3F5"
        s.append(rrect(bxb, byb, bw, 34, r=9, fill=fc))
        s.append(txt(bxb + 12, byb + 16, tx_[:52], size=9.3, color=UI["ink"], weight="500"))
        s.append(txt(bxb + bw - 10, byb + 29, wn, size=7.6, color=UI["faint"], weight="500", anchor="end"))
        byb += 42
    # composer
    s.append(rrect(mxr + 16, top + bh - 40, mwd - 32, 28, r=14, fill="#fff", stroke=UI["cardline"], sw=1))
    s.append(txt(mxr + 32, top + bh - 22, "Type a reply…  (templates · quick replies)", size=9.4, color=UI["faint"], weight="500"))
    s.append(f'<circle cx="{mxr+mwd-30}" cy="{top+bh-26}" r="11" fill="#25D366"/>')
    # right: customer context (callout 3/4)
    rxr = ix + lw + mwd + gap * 2
    s.append(card(rxr, top, rw, bh, "Linked customer & case", "user360", prim, pf=pf))
    s.append(callout(3, rxr + rw - 12, top + 12))
    s.append(avatar(rxr + 30, top + 66, 18, "AK", deep))
    s.append(txt(rxr + 58, top + 60, "Ahmed Al-Kuwari", size=12.5, color=UI["ink"], weight="800"))
    s.append(txt(rxr + 58, top + 76, "QIC-CUST-004182 · VIP", size=9.4, color=UI["sub"], weight="500"))
    cy2 = top + 100
    for lb, vv in [("Active policies", "3 · Motor, Medical, Group"),
                   ("Open case", "INC-2043 · in progress"),
                   ("Preferred channel", "WhatsApp · Arabic"),
                   ("Last contact", "Today · 10:42")]:
        s.append(field(rxr + 16, cy2, rw - 32, lb, vv))
        cy2 += 42
    s.append(rrect(rxr + 16, cy2 + 2, rw - 32, 30, r=6, fill="#FBF4F6", stroke=GOLD, sw=1.2))
    s.append(txt(rxr + 26, cy2 + 21, "Context follows across channels", size=9.4, color=QIC["maroon_dk"], weight="700"))
    s.append(callout(4, rxr + 10, cy2 + 2))
    s.append(rrect(rxr + 16, cy2 + 40, rw - 32, 28, r=6, fill=pf["chip_bg"]))
    s.append(txt(rxr + rw/2, cy2 + 58, "+ Create case from chat", size=9.8, color=pf["primary_dk"], weight="700", anchor="middle"))
    return "".join(s)


# ====================================================================== R6
R6 = dict(
    id="FR-4", headline="Departmental Routing, Queues & Ownership",
    title="Routing & Queue Management",
    sources=["RFP §5.2 / §10.1", "BRD §11.2 / §11.5", "Proposal FR-4"],
    text=["Department-based routing, queue assignment and follow-up ownership.",
          "Configurable routing rules aligned to approved SOPs.",
          "Queue management, workload distribution and reassignment visibility."],
    addressed=["Each department has its own queues, stages, SLA rules and views.",
               "Classification rules route every case to the correct queue without manual triage.",
               "Work is assigned by skill and capacity; ownership is always explicit.",
               "Supervisors balance workload and reassign from a single console."],
)


def c_r6(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, "Queues  ›  Supervisor console", "Queues")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    gap = 14
    lw = iw * 0.24
    mwd = iw * 0.44
    rw = iw - lw - mwd - gap * 2
    bh = cy + ch - top - 14
    # left: department queues (callout 1)
    s.append(card(ix, top, lw, bh, "Department queues", "route", prim, pf=pf))
    s.append(callout(1, ix + lw - 12, top + 12))
    qs = [("Customer Service", 24, prim, True), ("Claims", 12, "#3E7CB1", False),
          ("Underwriting", 40, "#7A5CC0", False), ("Complaints", 7, "#C0392B", False),
          ("Sales & BD", 15, "#0B875B", False), ("Corporate Servicing", 9, "#E8A33D", False)]
    qy = top + 52
    for nm, cnt, cc, act in qs:
        if act:
            s.append(rrect(ix + 8, qy, lw - 16, 40, r=6, fill="#EAF2FB"))
            s.append(rrect(ix + 8, qy, 3, 40, fill=prim))
        s.append(f'<circle cx="{ix+22}" cy="{qy+20}" r="5" fill="{cc}"/>')
        s.append(txt(ix + 34, qy + 17, nm, size=10, color=UI["ink"], weight="700"))
        s.append(txt(ix + 34, qy + 31, "open work items", size=8.2, color=UI["sub"], weight="500"))
        s.append(txt(ix + lw - 16, qy + 26, str(cnt), size=15, color=cc, weight="800", anchor="end"))
        qy += 46
    # middle: work items table (callout 2)
    mxr = ix + lw + gap
    s.append(card(mxr, top, mwd, bh, "Customer Service queue — work items", "case", prim, pf=pf))
    s.append(callout(2, mxr + mwd - 12, top + 12))
    cols = ["Case", "Subject", "Pri.", "SLA", "Owner"]
    colw = [mwd*0.16, mwd*0.36, mwd*0.13, mwd*0.16, mwd*0.19]
    rows = [["INC-2043", "Property lapse review", ("High", "#C0392B"), ("01:07", "#C0392B"), "M. Haddad"],
            ["TKT-3120", "Motor renewal query", ("Med", "#E8A33D"), "03:40", "S. Kamal"],
            ["TKT-3126", "Medical card reissue", ("Low", "#0B875B"), "2d", "Unassigned"],
            ["INC-2051", "Complaint — billing", ("High", "#C0392B"), ("00:34", "#C0392B"), "L. Fahad"],
            ["TKT-3130", "Address change", ("Low", "#0B875B"), "2d", "A. Nabil"],
            ["TKT-3134", "Portal access", ("Med", "#E8A33D"), "05:10", "S. Kamal"],
            ["INC-2055", "Claims status escalation", ("High", "#C0392B"), ("01:55", "#C0392B"), "M. Haddad"]]
    s.append(table(mxr + 12, top + 50, mwd - 24, cols, rows, colw, rowh=(bh-64)/8))
    # right: routing rules + capacity (callout 3/4)
    rxr = ix + lw + mwd + gap * 2
    s.append(card(rxr, top, rw, bh * 0.5 - 7, "Routing rules", "flow", prim, pf=pf))
    s.append(callout(3, rxr + rw - 12, top + 12))
    ry2 = top + 50
    for cond, q in [("Lapse > 30d", "→ Complaints"), ("Claims keyword", "→ Claims"),
                    ("Underwriting cat.", "→ Underwriting"), ("Default", "→ Customer Service")]:
        s.append(rrect(rxr + 12, ry2, rw - 24, 26, r=6, fill=UI["field"], stroke=UI["cardline"], sw=1))
        s.append(txt(rxr + 22, ry2 + 17, cond, size=9.4, color=UI["ink"], weight="700"))
        s.append(txt(rxr + rw - 22, ry2 + 17, q, size=9.2, color=prim, weight="700", anchor="end"))
        ry2 += 30
    cap_y = top + bh * 0.5 + 7
    s.append(card(rxr, cap_y, rw, bh * 0.5 - 7, "Agent capacity", "people", prim, pf=pf))
    s.append(callout(4, rxr + rw - 12, cap_y + 12))
    ay3 = cap_y + 50
    for nm, load, cap in [("S. Kamal", 4, 6), ("M. Haddad", 6, 6), ("L. Fahad", 3, 6), ("A. Nabil", 2, 6)]:
        s.append(txt(rxr + 16, ay3 + 10, nm, size=9.6, color=UI["ink"], weight="700"))
        s.append(txt(rxr + rw - 16, ay3 + 10, f"{load}/{cap}", size=9, color=UI["sub"], weight="600", anchor="end"))
        s.append(rrect(rxr + 16, ay3 + 16, rw - 32, 8, r=4, fill="#E7ECF2"))
        col = "#C0392B" if load >= cap else prim
        s.append(rrect(rxr + 16, ay3 + 16, (rw - 32) * load / cap, 8, r=4, fill=col))
        ay3 += 34
    return "".join(s)


# ====================================================================== R7
R7 = dict(
    id="FR-7", headline="Sales — Lead, Opportunity & Account Management",
    title="Sales & Corporate Accounts",
    sources=["RFP §5.5", "BRD §7.5 / §3.5", "Proposal FR-7"],
    text=["Lead capture and qualification, opportunity pipeline and account ownership.",
          "Corporate account servicing, relationship tracking, visit and activity logging.",
          "Pipeline visibility and readiness for cross-sell and retention."],
    addressed=["Leads are captured and qualified; low-intent leads recycle to nurture.",
               "The pipeline board tracks value and stage from lead to won customer.",
               "Corporate accounts are owned and serviced with visits and activities logged.",
               "Pipeline value and forecast are visible for management."],
)


def c_r7(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    app = "Dynamics 365 Sales" if pf["key"] == "microsoft" else "Sales Cloud"
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, f"{app}  ›  Pipeline", "Opportunities")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    # stat row
    tiles = [("QAR 4.8M", "Open pipeline", prim), ("18", "Open opportunities", "#3E7CB1"),
             ("32%", "Win rate (QTD)", "#0B875B"), ("QAR 920K", "Weighted forecast", "#E8A33D")]
    tw = (iw - 3 * 12) / 4
    for i, (v, l, c) in enumerate(tiles):
        s.append(stat_tile(ix + i * (tw + 12), top, tw, 58, v, l, c))
    # kanban (callout 1/2/4)
    ky = top + 72
    kh = (cy + ch - ky - 14) * 0.6
    stages = [("New lead", 5, "#94A3B2"), ("Qualified", 4, "#3E7CB1"), ("Proposal", 3, prim),
              ("Negotiation", 3, "#E8A33D"), ("Won", 3, "#0B875B")]
    kw = (iw - 4 * 10) / 5
    deals = {0: [("Al Meera Group", "Medical · QAR 480K"), ("Woqod fleet", "Motor · QAR 220K")],
             1: [("Ooredoo staff", "Medical · QAR 900K"), ("Katara Hosp.", "Property · QAR 150K")],
             2: [("Qatar Steel", "Group life · QAR 640K")],
             3: [("Doha Bank", "Motor fleet · QAR 380K")],
             4: [("Mannai Corp.", "Won · QAR 520K"), ("QNB branch", "Won · QAR 210K")]}
    for i, (nm, cnt, cc) in enumerate(stages):
        kx = ix + i * (kw + 10)
        s.append(rrect(kx, ky, kw, kh, r=8, fill="#F4F6F9", stroke=UI["cardline"], sw=1))
        s.append(rrect(kx, ky, kw, 4, r=2, fill=cc))
        s.append(txt(kx + 12, ky + 22, nm, size=10.4, color=UI["ink"], weight="800"))
        s.append(txt(kx + kw - 12, ky + 22, str(cnt), size=10, color=cc, weight="800", anchor="end"))
        dy = ky + 34
        for dn, dv in deals.get(i, []):
            s.append(rrect(kx + 8, dy, kw - 16, 48, r=6, fill="#fff", stroke=UI["cardline"], sw=1))
            s.append(rrect(kx + 8, dy, 3, 48, fill=cc))
            s.append(txt(kx + 18, dy + 18, dn, size=9.6, color=UI["ink"], weight="700"))
            s.append(txt(kx + 18, dy + 33, dv, size=8.6, color=UI["sub"], weight="500"))
            dy += 54
    s.append(callout(1, ix + kw * 0.5, ky))
    s.append(callout(2, ix + kw * 2.5 + 20, ky))
    s.append(callout(4, ix + kw * 4.5 + 40, ky))
    # bottom: account + activities (callout 3)
    by = ky + kh + 14
    bh2 = cy + ch - by - 14
    half = (iw - 12) / 2
    s.append(card(ix, by, half, bh2, "Corporate account — Ooredoo Q.S.C.", "people", prim, pf=pf))
    s.append(callout(3, ix + half - 12, by + 12))
    for i, (lb, vv) in enumerate([("Account owner", "N. Al-Sadi"), ("Segment", "Corporate · Strategic"),
                                   ("Active policies", "6 · QAR 3.1M premium"), ("Next renewal", "03 Nov 2026")]):
        col = i % 2; row = i // 2
        s.append(field_box(ix + 16 + col * (half/2 - 12), by + 50 + row * 48, half/2 - 28, lb, vv))
    s.append(card(ix + half + 12, by, half, bh2, "Activities & visits", "clock", prim, pf=pf))
    ay4 = by + 50
    for g, gc, tt, sub, wn in [("people", prim, "Site visit — West Bay HQ", "Renewal review", "2d"),
                                ("phone", prim, "Call — benefits manager", "Cross-sell life", "4d"),
                                ("mail", prim, "Proposal sent", "Medical top-up", "1w")]:
        s.append(timeline_item(ix + half + 24, ay4, half - 48, g, gc, tt, sub, wn))
        ay4 += 48
    return "".join(s)


# ====================================================================== R8
R8 = dict(
    id="FR-8", headline="Real-time Dashboards, KPIs & Management Reporting",
    title="Dashboards & KPI Reporting",
    sources=["RFP §5.6 / §10.2", "BRD §12 / §13", "Proposal FR-8"],
    text=["Real-time dashboards: interaction volumes, open/closed cases, SLA, escalations, aging, workload.",
          "Management reporting for departmental performance and service trends.",
          "Role-based visibility, configurable widgets and export to Excel/PDF/CSV."],
    addressed=["Operational tiles and charts refresh in real time across channels and departments.",
               "SLA compliance and breach trends are tracked against target.",
               "Case aging and workload distribution are visible at a glance.",
               "Dashboards are role-based, filterable and exportable."],
)


def c_r8(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    tool = "Power BI" if pf["key"] == "microsoft" else "CRM Analytics"
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, f"Dashboards  ›  Operations ({tool})", "Operations")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    # stat tiles (callout 1)
    tiles = [("312", "Open cases", prim, "▲ 4%"), ("94.6%", "SLA compliance", "#0B875B", "▲ 1.2%"),
             ("00:41", "Avg first response", "#3E7CB1", "▼ 6m"), ("28", "Escalations (wk)", "#C0392B", "▲ 3")]
    tw = (iw - 3 * 12) / 4
    for i, (v, l, c, d) in enumerate(tiles):
        s.append(stat_tile(ix + i * (tw + 12), top, tw, 62, v, l, c, sub=d))
    s.append(callout(1, ix + tw - 6, top))
    # row of charts
    ry = top + 76
    rh = (cy + ch - ry - 14) * 0.52
    gap = 12
    c1 = iw * 0.3
    c2 = iw * 0.36
    c3 = iw - c1 - c2 - gap * 2
    # donut by channel (callout with 1)
    s.append(card(ix, ry, c1, rh, "Interactions by channel", "pbi", prim, pf=pf))
    segs = [(38, "#25D366"), (24, prim), (18, "#3E7CB1"), (12, "#E8A33D"), (8, "#7A5CC0")]
    s.append(donut(ix + c1*0.36, ry + rh*0.56, min(rh*0.3, 58), segs))
    leg = ["WhatsApp 38%", "Voice 24%", "Email 18%", "Web 12%", "Portal 8%"]
    ly = ry + 52
    for i, (lbl) in enumerate(leg):
        s.append(f'<rect x="{ix+c1*0.62}" y="{ly-8}" width="10" height="10" rx="2" fill="{segs[i][1]}"/>')
        s.append(txt(ix + c1*0.62 + 16, ly, lbl, size=9, color=UI["ink"], weight="600"))
        ly += 20
    # bars by dept (callout 3)
    s.append(card(ix + c1 + gap, ry, c2, rh, "Open cases by department", "pbi", prim, pf=pf))
    s.append(callout(3, ix + c1 + gap + c2 - 12, ry + 12))
    s.append(bars(ix + c1 + gap + 20, ry + 54, c2 - 44, rh - 90, [96, 62, 48, 40, 34, 32], prim,
                  labels=["U/W", "CS", "Clm", "Cmp", "Sal", "Corp"]))
    # SLA line trend (callout 2)
    s.append(card(ix + c1 + c2 + gap*2, ry, c3, rh, "SLA compliance trend", "gauge", prim, pf=pf))
    s.append(callout(2, ix + c1 + c2 + gap*2 + c3 - 12, ry + 12))
    s.append(line_chart(ix + c1 + c2 + gap*2 + 16, ry + 54, c3 - 32, rh - 84, [88, 90, 89, 92, 93, 94, 95], "#0B875B"))
    s.append(txt(ix + c1 + c2 + gap*2 + 16, ry + rh - 12, "target 90% · trending up", size=8.8, color=UI["sub"], weight="600"))
    # bottom table (callout 4)
    by = ry + rh + 14
    bh2 = cy + ch - by - 14
    s.append(card(ix, by, iw, bh2, "Departmental performance — this week (role-based · exportable)", "pbi", prim, pf=pf))
    s.append(chip(ix + iw - 200, by + 12, 60, 18, "Excel", pf["chip_bg"], text_color=pf["primary_dk"], size=8.6, r=9))
    s.append(chip(ix + iw - 136, by + 12, 52, 18, "PDF", pf["chip_bg"], text_color=pf["primary_dk"], size=8.6, r=9))
    s.append(chip(ix + iw - 80, by + 12, 60, 18, "Schedule", pf["chip_bg"], text_color=pf["primary_dk"], size=8.6, r=9))
    s.append(callout(4, ix + iw - 12, by + 12))
    cols = ["Department", "Open", "Closed (wk)", "SLA %", "Avg resolution", "Escalations", "Aging >3d"]
    colw = [iw*0.2, iw*0.1, iw*0.14, iw*0.12, iw*0.18, iw*0.15, iw*0.11]
    rows = [["Customer Service", "62", "418", ("96%", "#0B875B"), "3.2h", "4", "6"],
            ["Underwriting", "96", "210", ("93%", "#0B875B"), "6.1h", "3", "14"],
            ["Claims", "48", "156", ("91%", "#0B875B"), "5.4h", "7", "9"],
            ["Complaints", "40", "88", ("89%", "#E8A33D"), "8.0h", "11", "12"],
            ["Sales & BD", "34", "72", ("95%", "#0B875B"), "2.6h", "1", "3"]]
    s.append(table(ix + 12, by + 42, iw - 24, cols, rows, colw, rowh=(bh2-54)/6))
    return "".join(s)


# ====================================================================== R9
R9 = dict(
    id="FR-9", headline="Enterprise Integration — API-led, Monitored",
    title="Integration Architecture (9 systems)",
    sources=["RFP §7", "BRD §9 / §16.3", "Proposal FR-9"],
    text=["Secure API-led integration with nine enterprise systems and channels.",
          "Real-time and batch patterns with error handling, retry and monitoring.",
          "The CRM consumes the customer master and never creates it."],
    addressed=["A managed integration platform exposes governed APIs for all nine interfaces.",
               "Each interface uses the right pattern — real-time events or scheduled batch.",
               "Every interface is secured, logged, monitored and retried on failure.",
               "The customer master is consumed read-only; the CRM is never a second master."],
)


def c_r9(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    plat = "Azure API Management" if pf["key"] == "microsoft" else "MuleSoft Anypoint"
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, f"Integration  ›  {plat}", "Interfaces")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    gap = 14
    lw = iw * 0.62
    rw = iw - lw - gap
    bh = cy + ch - top - 14
    # left: interface inventory (callout 1/2/4)
    s.append(card(ix, top, lw, bh, f"Interface inventory · {plat}", "flow", prim, pf=pf))
    s.append(callout(1, ix + lw - 12, top + 12))
    cols = ["#", "System / channel", "Purpose", "Pattern", "Status"]
    colw = [lw*0.06, lw*0.28, lw*0.36, lw*0.18, lw*0.12]
    rt = "Real-time"; bt = "Batch"; tw = "Two-way"
    rows = [["1", "Customer Master DB", "Identity · governed 360", (rt+" + "+bt, prim), ("● Live", "#0B875B")],
            ["2", "Azentio Core Insurance", "Policy · claims reference", (rt+" + "+bt, prim), ("● Live", "#0B875B")],
            ["3", "WhatsApp Business API", "Messaging · notifications", (tw, prim), ("● Live", "#0B875B")],
            ["4", "Microsoft 365 / Outlook", "Email · follow-up", (tw, prim), ("● Live", "#0B875B")],
            ["5", "Shared mailboxes", "Dept. communications", ("Inbound", prim), ("● Live", "#0B875B")],
            ["6", "3CX Telephony", "Call log · screen-pop", ("Events", prim), ("● Live", "#0B875B")],
            ["7", "Website & web forms", "Enquiry capture", ("Inbound", prim), ("● Live", "#0B875B")],
            ["8", "SkipCash gateway", "Payment notifications", ("Events", prim), ("● Live", "#0B875B")],
            ["9", "Insursa B2B/B2C portals", "Servicing · visibility", (tw, prim), ("● Live", "#0B875B")]]
    s.append(table(ix + 12, top + 50, lw - 24, cols, rows, colw, rowh=(bh-64)/10))
    s.append(callout(4, ix + lw*0.5, top + 66))
    # right: monitoring + master boundary (callout 2/3)
    rxr = ix + lw + gap
    s.append(card(rxr, top, rw, bh*0.52 - 7, "Runtime monitoring", "gauge", prim, pf=pf))
    s.append(callout(2, rxr + rw - 12, top + 12))
    s.append(gauge_ring(rxr + rw/2, top + 100, 46, 0.998, "#0B875B", "Interface success (24h)", "99.8%"))
    my = top + 150
    for lb, vv in [("Msgs today", "48,210"), ("Avg latency", "180 ms"), ("Retries", "12 · auto-recovered")]:
        s.append(txt(rxr + 16, my + 12, lb, size=9.4, color=UI["sub"], weight="600"))
        s.append(txt(rxr + rw - 16, my + 12, vv, size=9.8, color=UI["ink"], weight="700", anchor="end"))
        my += 22
    # master boundary
    mb = top + bh*0.52 + 7
    s.append(card(rxr, mb, rw, bh*0.48 - 7, "Master-data boundary", "lock", GOLD, pf=pf))
    s.append(callout(3, rxr + rw - 12, mb + 12))
    s.append(rrect(rxr + 16, mb + 50, rw - 32, 46, r=8, fill="#FBF4F6", stroke=GOLD, sw=1.4))
    s.append(mini_chip("db", "#4C6B8A", rxr + 26, mb + 60, 26))
    s.append(txt(rxr + 60, mb + 68, "Customer Master DB", size=10.4, color=QIC["maroon_dk"], weight="800"))
    s.append(txt(rxr + 60, mb + 84, "read-only lookup · never written", size=9, color=QIC["maroon_dk"], weight="600"))
    s.append(line(rxr + rw/2, mb + 96, rxr + rw/2, mb + 116, color=GOLD, w=2, marker="arrG"))
    s.append(rrect(rxr + 16, mb + 118, rw - 32, 40, r=8, fill=pf["chip_bg"]))
    s.append(txt(rxr + rw/2, mb + 137, "CRM engagement layer", size=10, color=pf["primary_dk"], weight="800", anchor="middle"))
    s.append(txt(rxr + rw/2, mb + 151, "consumes · owns interactions only", size=8.6, color=pf["primary_dk"], weight="600", anchor="middle"))
    return "".join(s)


# ====================================================================== R10
R10 = dict(
    id="NFR-3", headline="Security, RBAC, Encryption & Compliance",
    title="Security & Access Control",
    sources=["RFP §6", "BRD §8.2 / §14 / §15", "Proposal NFR-3/4"],
    text=["Role-based access control with department segregation and least privilege.",
          "Encryption in transit and at rest, SSO and multi-factor authentication.",
          "Complete audit trails; QCB, Qatari PDPPL and GDPR alignment."],
    addressed=["Roles and permissions grant least-privilege access by department and responsibility.",
               "SSO and MFA authenticate every user; sessions are controlled.",
               "Data is encrypted in transit and at rest with managed keys.",
               "Full audit and compliance controls align to QCB, PDPPL and GDPR."],
)


def c_r10(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    idp = "Microsoft Entra ID" if pf["key"] == "microsoft" else "Salesforce Identity"
    model = "Security roles & business units" if pf["key"] == "microsoft" else "Profiles, permission sets & sharing"
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, "Setup  ›  Security & access", "Security")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    gap = 14
    lw = iw * 0.6
    rw = iw - lw - gap
    bh = cy + ch - top - 14
    # left: role matrix (callout 1)
    s.append(card(ix, top, lw, bh, f"Role-based access matrix · {model}", "shield", prim, pf=pf))
    s.append(callout(1, ix + lw - 12, top + 12))
    cols = ["Role", "View", "Edit", "Assign", "Escalate", "Config", "Data scope"]
    colw = [lw*0.24, lw*0.1, lw*0.1, lw*0.12, lw*0.13, lw*0.11, lw*0.2]
    Y = ("✓", "#0B875B"); N = ("—", "#C7CFD8")
    rows = [["CS / Call-center agent", Y, Y, N, N, N, "Own + team"],
            ["Underwriter", Y, Y, N, N, N, "Department"],
            ["Claims user", Y, Y, N, Y, N, "Department"],
            ["Sales / BDM", Y, Y, Y, N, N, "Own accounts"],
            ["Supervisor / lead", Y, Y, Y, Y, N, "Department"],
            ["CRM administrator", Y, Y, Y, Y, Y, "Enterprise"],
            ["Management", Y, N, N, N, N, "Enterprise (read)"]]
    s.append(table(ix + 12, top + 50, lw - 24, cols, rows, colw, rowh=(bh-64)/8))
    # right: controls (callout 2/3/4)
    rxr = ix + lw + gap
    s.append(card(rxr, top, rw, bh, "Security controls", "lock", prim, pf=pf))
    ctrls = [("entra", prim, "Identity · SSO · MFA", idp, 2),
             ("lock", "#0B875B", "Encryption", "In transit (TLS) & at rest", 3),
             ("defender", prim, "Threat protection", "Defender" if pf["key"]=="microsoft" else "Shield", None),
             ("purview", "#7A5CC0", "Audit & monitoring", "Purview" if pf["key"]=="microsoft" else "Shield Event Monitoring", 4)]
    ry2 = top + 52
    for g, gc, tt, sub, co in ctrls:
        s.append(rrect(rxr + 12, ry2, rw - 24, 44, r=8, fill=UI["field"], stroke=UI["cardline"], sw=1))
        s.append(mini_chip(g, gc, rxr + 22, ry2 + 11, 24, cloud=(pf["key"]=="salesforce")))
        s.append(txt(rxr + 56, ry2 + 20, tt, size=10.4, color=UI["ink"], weight="800"))
        s.append(txt(rxr + 56, ry2 + 35, sub, size=8.8, color=UI["sub"], weight="500"))
        if co:
            s.append(callout(co, rxr + 12, ry2 + 6))
        ry2 += 52
    # compliance chips
    s.append(sect(rxr + 14, ry2 + 8, "REGULATORY ALIGNMENT"))
    cy3 = ry2 + 18
    for i, cmp in enumerate(["QCB guidelines", "Qatari PDPPL", "GDPR principles", "Data residency (Qatar/region)"]):
        s.append(rrect(rxr + 12, cy3, rw - 24, 26, r=6, fill="#E4F5EC"))
        s.append(txt(rxr + 24, cy3 + 17, "✓  " + cmp, size=9.8, color="#0B875B", weight="700"))
        cy3 += 30
    return "".join(s)


# ====================================================================== R11
R11 = dict(
    id="FR-Cfg", headline="Configuration & Low-code Workflow",
    title="Configuration & Automation",
    sources=["RFP §6", "BRD §4.1 / §11.2", "Proposal — configuration over code"],
    text=["Dynamic forms, configurable workflows, queue rules and notification/reminder configuration.",
          "Delivered by configuration on a single extensible platform — minimal custom code.",
          "Phase 2–4 roadmap absorbed without re-platforming."],
    addressed=["Forms are configured with drag-and-drop fields and validation — no code.",
               "Workflows and routing are built declaratively on the automation designer.",
               "Business rules, SLAs and notifications are configuration, not development.",
               "The same platform extends to later phases without re-platforming."],
)


def c_r11(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    former = "Power Apps form designer" if pf["key"] == "microsoft" else "Lightning App Builder"
    flowt = "Power Automate" if pf["key"] == "microsoft" else "Flow Builder"
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, f"Maker  ›  {former}", "Designer")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    gap = 14
    lw = iw * 0.44
    rw = iw - lw - gap
    bh = cy + ch - top - 14
    # left: form designer (callout 1/3)
    s.append(card(ix, top, lw, bh, f"{former} — dynamic form", "papps" if pf["key"]=="microsoft" else "case", prim, pf=pf))
    s.append(callout(1, ix + lw - 12, top + 12))
    # palette
    palx = ix + 12
    s.append(rrect(palx, top + 50, 108, bh - 64, r=6, fill="#F4F6F9", stroke=UI["cardline"], sw=1))
    s.append(sect(palx + 10, top + 68, "FIELDS"))
    for i, fld in enumerate(["Text", "Choice", "Lookup", "Date", "Number", "Toggle", "Sub-grid", "Section"]):
        s.append(rrect(palx + 8, top + 78 + i * 30, 92, 24, r=5, fill="#fff", stroke=UI["cardline"], sw=1))
        s.append(txt(palx + 18, top + 94 + i * 30, "⋮⋮ " + fld, size=9.2, color=UI["ink"], weight="600"))
    # canvas
    canx = palx + 118
    canw = lw - 12 - 118 - 12
    s.append(rrect(canx, top + 50, canw, bh - 64, r=6, fill="#fff", stroke=prim, sw=1.4, dash="5 4"))
    fy = top + 64
    for lb, mand in [("Channel", True), ("Category", True), ("Reason", True), ("Assigned user", False),
                     ("Outcome", True), ("Follow-up date", False)]:
        s.append(rrect(canx + 12, fy, canw - 24, 34, r=5, fill=UI["field"], stroke=UI["cardline"], sw=1))
        s.append(txt(canx + 22, fy + 14, lb + (" *" if mand else ""), size=8.6, color=UI["faint"], weight="700"))
        s.append(txt(canx + 22, fy + 28, "—", size=9, color=UI["sub"], weight="500"))
        fy += 40
    s.append(callout(3, canx + canw - 8, top + 56))
    # right: flow designer (callout 2/4)
    rxr = ix + lw + gap
    s.append(card(rxr, top, rw, bh, f"{flowt} — case automation", "flow", "#0B53CE" if pf["key"]=="microsoft" else prim, pf=pf))
    s.append(callout(2, rxr + rw - 12, top + 12))
    nodes = [("⚡ When a case is created", "Trigger", "#0B875B"),
             ("◈ Condition: priority = High", "Control", "#7A5CC0"),
             ("→ Assign to department queue", "Action", prim),
             ("⏱ Start SLA timer", "Action", prim),
             ("✉ Send acknowledgement (WhatsApp/email)", "Action", prim),
             ("⤴ If breach → escalate (multi-level)", "Action", "#C0392B")]
    ny = top + 58
    nx = rxr + 24
    nw = rw - 48
    for i, (tt, kind, cc) in enumerate(nodes):
        s.append(rrect(nx, ny, nw, 42, r=8, fill="#fff", stroke=cc, sw=1.4))
        s.append(rrect(nx, ny, 5, 42, r=2, fill=cc))
        s.append(txt(nx + 18, ny + 19, tt, size=10, color=UI["ink"], weight="700"))
        s.append(txt(nx + 18, ny + 34, kind + " · no code", size=8.4, color=UI["sub"], weight="500"))
        if i < len(nodes) - 1:
            s.append(line(nx + nw/2, ny + 42, nx + nw/2, ny + 50, color=UI["faint"], w=1.8, marker="arr"))
        ny += 50
    s.append(callout(4, nx + nw - 8, top + 54))
    return "".join(s)


# ====================================================================== R12
R12 = dict(
    id="AI", headline="Governed AI Assistance for Service & Sales",
    title="AI Assistance (Copilot / Einstein)",
    sources=["RFP §17 (future)", "BRD §13.5 / §16.5", "Proposal §04 AI"],
    text=["AI assistance for case summarization, drafted responses and knowledge suggestions.",
          "Phased, governed adoption with human review for customer-facing output.",
          "Foundation for predictive insight, segmentation and retention analytics."],
    addressed=["AI summarizes the case and conversation so agents ramp instantly.",
               "It drafts a reply the agent reviews and edits before sending.",
               "Relevant knowledge and next-best-action are surfaced in context.",
               "AI is governed: human review is retained for customer-facing output."],
)


def c_r12(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    ai = "Copilot" if pf["key"] == "microsoft" else "Einstein"
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, f"Cases  ›  INC-2043 · {ai}", "INC-2043")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    gap = 14
    lw = iw * 0.52
    rw = iw - lw - gap
    bh = cy + ch - top - 14
    # left: case context
    s.append(card(ix, top, lw, bh, "Case context", "case", prim, pf=pf))
    s.append(txt(ix + 16, top + 62, "INC-2043 · Property lapse review", size=13, color=UI["ink"], weight="800"))
    s.append(txt(ix + 16, top + 80, "Ahmed Al-Kuwari · Complaints · High priority", size=9.6, color=UI["sub"], weight="500"))
    thy = top + 100
    for g, gc, tt, sub, wn in [("whatsapp", "#25D366", "Customer: policy lapsed unexpectedly", "auto-renew failed", "5d"),
                                ("mail", prim, "Agent: requested payment proof", "", "4d"),
                                ("case", prim, "Escalated to Complaints", "SLA High", "4d"),
                                ("phone", prim, "Call: reinstatement options discussed", "", "2d")]:
        s.append(timeline_item(ix + 16, thy, lw - 32, g, gc, tt, sub, wn))
        thy += 50
    # knowledge
    s.append(sect(ix + 16, thy + 12, "SUGGESTED KNOWLEDGE (AI)"))
    ky = thy + 22
    for art in ["KB-118 · Policy reinstatement after lapse", "KB-204 · Auto-renewal failure handling", "KB-090 · Goodwill & waiver policy"]:
        s.append(rrect(ix + 16, ky, lw - 32, 28, r=6, fill=pf["chip_bg"]))
        s.append(txt(ix + 26, ky + 18, "📄  " + art, size=9.4, color=pf["primary_dk"], weight="600"))
        ky += 32
    # right: AI panel (callouts)
    rxr = ix + lw + gap
    s.append(rrect(rxr, top, rw, bh, r=9, fill="#fff", stroke="#C9B8E8", sw=1.5))
    s.append(rrect(rxr, top, rw, 40, r=9, fill="url(#aiGrad)"))
    s.append(rrect(rxr, top + 24, rw, 16, fill="none"))
    s.append(mini_chip("copilot", "#fff", rxr + 12, top + 9, 22))
    s.append(txt(rxr + 44, top + 26, f"{ai} for Service", size=13, color="#fff", weight="800"))
    s.append(chip(rxr + rw - 96, top + 11, 84, 18, "Governed", "#ffffff", text_color="#6D28D9", size=9, r=9))
    # summary (callout 1)
    sy = top + 52
    s.append(rrect(rxr + 12, sy, rw - 24, 76, r=8, fill="#F7F3FE", stroke="#E4D8F7", sw=1))
    s.append(txt(rxr + 22, sy + 18, "CASE SUMMARY", size=8.6, color="#6D28D9", weight="800"))
    for i, ln in enumerate(["Customer's property policy lapsed after an auto-renewal",
                            "payment failure. Escalated as a High-priority complaint;",
                            "reinstatement options discussed. Awaiting proof of payment."]):
        s.append(txt(rxr + 22, sy + 36 + i * 15, ln, size=9.2, color=UI["ink"], weight="500"))
    s.append(callout(1, rxr + 12, sy))
    # drafted reply (callout 2)
    dy = sy + 88
    s.append(rrect(rxr + 12, dy, rw - 24, 92, r=8, fill="#F7F3FE", stroke="#E4D8F7", sw=1))
    s.append(txt(rxr + 22, dy + 18, "DRAFTED REPLY  ·  review before send", size=8.6, color="#6D28D9", weight="800"))
    for i, ln in enumerate(["Dear Mr Al-Kuwari, thank you for your patience. We can",
                            "reinstate policy P-PRP-0774 today on receipt of the QAR",
                            "2,050 premium. A secure SkipCash link follows shortly."]):
        s.append(txt(rxr + 22, dy + 36 + i * 15, ln, size=9.2, color=UI["ink"], weight="500"))
    s.append(rrect(rxr + rw - 190, dy + 62, 84, 22, r=6, fill="#fff", stroke="#C9B8E8", sw=1))
    s.append(txt(rxr + rw - 148, dy + 77, "Edit", size=9.4, color="#6D28D9", weight="700", anchor="middle"))
    s.append(rrect(rxr + rw - 100, dy + 62, 88, 22, r=6, fill=prim))
    s.append(txt(rxr + rw - 56, dy + 77, "Review & send", size=9, color="#fff", weight="700", anchor="middle"))
    s.append(callout(2, rxr + 12, dy))
    # next best action (callout 3) + governance (callout 4)
    ny = dy + 104
    s.append(rrect(rxr + 12, ny, rw - 24, 40, r=8, fill="#F7F3FE", stroke="#E4D8F7", sw=1))
    s.append(txt(rxr + 22, ny + 17, "NEXT BEST ACTION", size=8.6, color="#6D28D9", weight="800"))
    s.append(txt(rxr + 22, ny + 32, "Offer reinstatement + cross-sell motor top-up", size=9.4, color=UI["ink"], weight="600"))
    s.append(callout(3, rxr + 12, ny))
    gy = ny + 52
    s.append(rrect(rxr + 12, gy, rw - 24, 34, r=8, fill="#FBF4F6", stroke=GOLD, sw=1.2))
    extra = " · Arabic-capable" if pf["key"] == "microsoft" else ""
    s.append(txt(rxr + 22, gy + 21, "Human-in-the-loop · no auto-send to customer" + extra, size=9.2, color=QIC["maroon_dk"], weight="700"))
    s.append(callout(4, rxr + 12, gy))
    return "".join(s)


# ====================================================================== R13
R13 = dict(
    id="FR-Ntf", headline="Notifications & Follow-up Management",
    title="Notifications & Follow-ups",
    sources=["RFP §5.3", "BRD §11.6 / §7.7", "Proposal — automation"],
    text=["Automated notifications for assignments, follow-ups, SLA breaches and workflow updates.",
          "Delivered in-CRM, by email and by WhatsApp where applicable.",
          "Follow-up requirements generate scheduled tasks so nothing is missed."],
    addressed=["A notification centre alerts each user to the events that concern them.",
               "SLA reminders and breach alerts fire automatically to owners and supervisors.",
               "Follow-up requirements auto-create scheduled tasks with due dates.",
               "Notifications route across in-app, email and WhatsApp channels."],
)


def c_r13(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, "Home  ›  Notifications & tasks", "My day")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    gap = 14
    lw = iw * 0.5
    rw = iw - lw - gap
    bh = cy + ch - top - 14
    # left: notification center (callout 1/2)
    s.append(card(ix, top, lw, bh, "Notification centre", "bell", prim, pf=pf))
    s.append(callout(1, ix + lw - 12, top + 12))
    notes = [("bolt", "#C0392B", "SLA breach — INC-2051", "Complaint · billing · escalate now", "2m", "Breach", "#FDECEC", "#B4342B"),
             ("clock", "#E8A33D", "SLA at 75% — TKT-3134", "Portal access · respond soon", "10m", "Warning", "#FBF1DA", "#8A6D1E"),
             ("case", prim, "Case assigned to you", "INC-2055 · claims escalation", "18m", "New", "#EAF2FB", prim),
             ("bell", prim, "Follow-up due today", "Ahmed Al-Kuwari · renewal", "1h", "Due", "#EAF2FB", prim),
             ("flow", prim, "Workflow update", "TKT-3120 moved to In progress", "2h", None, None, None),
             ("mail", prim, "Customer replied", "Group HR — Ooredoo (email)", "3h", None, None, None)]
    ny = top + 50
    for g, gc, tt, sub, meta, tag, tc, ttc in notes:
        s.append(inbox_row(ix + 8, ny, lw - 16, 50, g, gc, tt, sub, meta, tag=tag, tag_c=tc))
        if tag:
            pass
        ny += 52
    # right top: follow-up tasks (callout 3)
    rxr = ix + lw + gap
    th = bh * 0.58
    s.append(card(rxr, top, rw, th, "Follow-up tasks", "case", prim, pf=pf))
    s.append(callout(3, rxr + rw - 12, top + 12))
    ty = top + 50
    tasks = [("Send renewal proof reminder", "Ahmed Al-Kuwari", "Today", "#C0392B"),
             ("Confirm medical card reissue", "F. Al-Ansari", "Today", "#E8A33D"),
             ("Corporate visit follow-up", "Ooredoo", "Tomorrow", prim),
             ("Reinstatement paperwork", "INC-2043", "23 Jul", prim),
             ("Payment confirmation check", "SkipCash", "24 Jul", prim)]
    for tt, who, due, cc in tasks:
        s.append(rrect(rxr + 12, ty, rw - 24, 34, r=6, fill=UI["field"], stroke=UI["cardline"], sw=1))
        s.append(f'<rect x="{rxr+22}" y="{ty+11}" width="12" height="12" rx="3" fill="#fff" stroke="{cc}" stroke-width="1.6"/>')
        s.append(txt(rxr + 44, ty + 16, tt, size=9.8, color=UI["ink"], weight="700"))
        s.append(txt(rxr + 44, ty + 28, who, size=8.4, color=UI["sub"], weight="500"))
        s.append(chip(rxr + rw - 84, ty + 9, 68, 17, due, "#fff", text_color=cc, size=8.6, r=8))
        ty += 40
    # right bottom: channels (callout 4)
    chy = top + th + 12
    s.append(card(rxr, chy, rw, bh - th - 12, "Delivery channels", "route", prim, pf=pf))
    s.append(callout(4, rxr + rw - 12, chy + 12))
    cwn = (rw - 24 - 2 * 10) / 3
    for i, (g, gc, lb) in enumerate([("bell", prim, "In-app"), ("mail", prim, "Email"), ("whatsapp", "#25D366", "WhatsApp")]):
        px = rxr + 12 + i * (cwn + 10)
        s.append(rrect(px, chy + 48, cwn, 50, r=8, fill=pf["chip_bg"]))
        s.append(mini_chip(g, gc, px + cwn/2 - 12, chy + 56, 24, cloud=False))
        s.append(txt(px + cwn/2, chy + 92, lb, size=9.4, color=pf["primary_dk"], weight="700", anchor="middle"))
    return "".join(s)


# ====================================================================== R14
R14 = dict(
    id="NFR-Usab", headline="Responsive Web & Mobile Access",
    title="Mobile & Responsive Access",
    sources=["RFP §6", "BRD §8.3 / §17.3", "Proposal NFR — usability"],
    text=["Responsive web interface for desktop, tablet and mobile.",
          "Mobile access for field sales and servicing teams; validation, dropdowns, auto-save.",
          "Foundation for future voice-to-text and geo-tagging."],
    addressed=["The same solution renders responsively on desktop, tablet and phone.",
               "Field sellers manage accounts, visits and activities on the mobile app.",
               "Agents service cases on the go with guided, validated forms.",
               "Roadmap-ready for voice-to-text capture and geo-tagged visits."],
)


def c_r14(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    app = "Dynamics 365 mobile" if pf["key"] == "microsoft" else "Salesforce mobile"
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, f"{app}  ·  responsive", "Mobile")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 22
    bh = cy + ch - top - 16
    # three phones
    phw = 224
    php = 330
    gapp = (iw - 3 * phw) / 4 if iw > 3 * phw + 60 else 30
    labels = [("Field sales · account", 1), ("Case servicing", 2), ("Dashboards on the go", None)]

    def phone(px, title, callout_n, kind):
        fr, (bx, by, bw, bhh) = phone_frame(px, top, phw, php, pf)
        o = [fr]
        # status bar
        o.append(rrect(bx, by, bw, 26, r=4, fill=deep))
        o.append(mini_chip("case", "#fff", bx + 8, by + 4, 18, cloud=(pf["key"]=="salesforce")))
        o.append(txt(bx + 32, by + 17, title, size=9, color="#fff", weight="700"))
        yy = by + 34
        if kind == "sales":
            o.append(rrect(bx + 8, yy, bw - 16, 44, r=6, fill=UI["field"]))
            o.append(avatar(bx + 26, yy + 22, 13, "OO", prim))
            o.append(txt(bx + 46, yy + 18, "Ooredoo Q.S.C.", size=9.6, color=UI["ink"], weight="800"))
            o.append(txt(bx + 46, yy + 32, "Corporate · QAR 3.1M", size=8, color=UI["sub"], weight="500"))
            yy += 52
            for lb, vv in [("Next renewal", "03 Nov"), ("Open opps", "2 · QAR 1.4M"), ("Owner", "N. Al-Sadi")]:
                o.append(rrect(bx + 8, yy, bw - 16, 30, r=5, fill="#fff", stroke=UI["cardline"], sw=1))
                o.append(txt(bx + 16, yy + 12, lb.upper(), size=6.8, color=UI["faint"], weight="700"))
                o.append(txt(bx + 16, yy + 25, vv, size=9, color=UI["ink"], weight="700"))
                yy += 34
            o.append(rrect(bx + 8, yy + 4, bw - 16, 34, r=8, fill=pf["chip_bg"], stroke=prim, sw=1.2))
            o.append(txt(bx + bw/2, yy + 20, "🎤  Log visit · voice-to-text", size=8.6, color=pf["primary_dk"], weight="700", anchor="middle"))
            o.append(txt(bx + bw/2, yy + 31, "📍 geo-tagged  ·  roadmap", size=7.2, color=UI["sub"], weight="500", anchor="middle"))
        elif kind == "case":
            o.append(rrect(bx + 8, yy, bw - 16, 30, r=5, fill="#FDECEC"))
            o.append(txt(bx + 16, yy + 13, "INC-2043 · High", size=9, color="#B4342B", weight="800"))
            o.append(txt(bx + 16, yy + 25, "SLA 01:07 remaining", size=7.6, color="#B4342B", weight="600"))
            yy += 38
            for lb, vv in [("Customer", "Ahmed Al-Kuwari"), ("Subject", "Property lapse"), ("Owner", "M. Haddad")]:
                o.append(rrect(bx + 8, yy, bw - 16, 30, r=5, fill="#fff", stroke=UI["cardline"], sw=1))
                o.append(txt(bx + 16, yy + 12, lb.upper(), size=6.8, color=UI["faint"], weight="700"))
                o.append(txt(bx + 16, yy + 25, vv, size=9, color=UI["ink"], weight="700"))
                yy += 34
            o.append(rrect(bx + 8, yy + 2, bw - 16, 26, r=5, fill=UI["field"]))
            o.append(txt(bx + 16, yy + 18, "Outcome ▾  (validated)", size=8.4, color=UI["sub"], weight="600"))
            yy += 32
            o.append(rrect(bx + 8, yy, bw - 16, 30, r=8, fill=prim))
            o.append(txt(bx + bw/2, yy + 19, "Update & save", size=9, color="#fff", weight="700", anchor="middle"))
        else:
            for v, l, c in [("312", "Open cases", prim), ("94.6%", "SLA", "#0B875B")]:
                pass
            o.append(rrect(bx + 8, yy, (bw-20)/2, 44, r=6, fill="#fff", stroke=UI["cardline"], sw=1))
            o.append(txt(bx + 8 + (bw-20)/4, yy + 24, "312", size=15, color=prim, weight="800", anchor="middle"))
            o.append(txt(bx + 8 + (bw-20)/4, yy + 37, "Open", size=7.6, color=UI["sub"], weight="600", anchor="middle"))
            o.append(rrect(bx + 12 + (bw-20)/2, yy, (bw-20)/2, 44, r=6, fill="#fff", stroke=UI["cardline"], sw=1))
            o.append(txt(bx + 12 + (bw-20)*0.75, yy + 24, "94.6%", size=14, color="#0B875B", weight="800", anchor="middle"))
            o.append(txt(bx + 12 + (bw-20)*0.75, yy + 37, "SLA", size=7.6, color=UI["sub"], weight="600", anchor="middle"))
            yy += 52
            o.append(bars(bx + 14, yy + 6, bw - 28, 70, [96, 62, 48, 40, 34], prim,
                          labels=["UW", "CS", "Cl", "Cm", "Sa"]))
            yy += 92
            o.append(donut(bx + bw/2, yy + 34, 28, [(38, "#25D366"), (24, prim), (18, "#3E7CB1"), (20, "#E8A33D")]))
            o.append(txt(bx + bw/2, yy + 78, "by channel", size=7.6, color=UI["sub"], weight="600", anchor="middle"))
        if callout_n:
            o.append(callout(callout_n, px + phw - 6, top + 6))
        return "".join(o)

    xs = ix + gapp
    kinds = ["sales", "case", "dash"]
    for i, (title, co) in enumerate(labels):
        s.append(phone(xs, title, co, kinds[i]))
        xs += phw + gapp
    # responsive note strip
    ny = top + php + 16
    sh = cy + ch - ny - 12
    s.append(rrect(ix, ny, iw, sh, r=10, fill="#fff", stroke=UI["cardline"], sw=1.2))
    s.append(mini_chip("gauge", prim, ix + 16, ny + 18, 24, cloud=(pf["key"] == "salesforce")))
    s.append(txt(ix + 50, ny + 26, "One responsive solution — desktop · tablet · phone",
                 size=13.5, color=deep, weight="800"))
    s.append(txt(ix + 50, ny + 45, "The same configuration renders across every form factor; field teams work online with validated, auto-saving forms.",
                 size=9.8, color=UI["sub"], weight="500"))
    s.append(callout(4, ix + 10, ny + 14))
    # usability chips (full width, one row)
    chips_ = ["Responsive web & mobile", "Field servicing access", "Mandatory-field validation",
              "Dropdowns & auto-save", "Voice-to-text · roadmap", "Geo-tagged visits · roadmap"]
    cwn = (iw - 40 - 5 * 10) / 6
    cyy = ny + 62
    for i, cptn in enumerate(chips_):
        px = ix + 20 + i * (cwn + 10)
        s.append(rrect(px, cyy, cwn, 28, r=6, fill=pf["chip_bg"]))
        s.append(txt(px + cwn / 2, cyy + 18, cptn, size=8.4, color=pf["primary_dk"],
                     weight="700", anchor="middle"))
    # NFR stat tiles (fill lower half)
    stiles = [("300+", "Concurrent users", prim), ("≤ 3s", "Page response", "#0B875B"),
              ("99.5%", "Availability", "#3E7CB1"), ("Auto-save", "No lost work", "#E8A33D"),
              ("Offline-ready", "Field resilience", "#7A5CC0")]
    stw = (iw - 40 - 4 * 12) / 5
    sty = ny + 106
    sthh = min(sh - 106 - 34, 76)
    for i, (v, l, c) in enumerate(stiles):
        s.append(stat_tile(ix + 20 + i * (stw + 12), sty, stw, sthh, v, l, c))
    s.append(txt(ix + 20, ny + sh - 14,
                 "Non-functional targets verified on web and mobile — responsive Unified Interface / Lightning across desktop, tablet and phone.",
                 size=9.4, color=UI["sub"], weight="500"))
    return "".join(s)


# ====================================================================== R15
R15 = dict(
    id="FR-KB", headline="Knowledge Management & Self-service Deflection",
    title="Knowledge & Self-service",
    sources=["RFP §5.2", "BRD §17.2 / §3.1", "Proposal — knowledge & FCR"],
    text=["Knowledge articles support first-contact resolution across departments.",
          "Agents surface relevant knowledge in context; customers self-serve on the portal.",
          "Multilingual content (including Arabic) for the Qatar market."],
    addressed=["A searchable knowledge base backs every service interaction.",
               "Relevant articles are surfaced on the case for first-contact resolution.",
               "The same articles power self-service deflection on the Insursa portal.",
               "Articles are versioned, approved and available in English and Arabic."],
)


def c_r15(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, "Knowledge  ›  KB-118", "KB-118")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    gap = 14
    lw = iw * 0.26
    mw = iw * 0.44
    rw = iw - lw - mw - gap * 2
    bh = cy + ch - top - 14
    # left: article list (callout 1)
    s.append(card(ix, top, lw, bh, "Knowledge base", "case", prim, pf=pf))
    s.append(callout(1, ix + lw - 12, top + 12))
    arts = [("KB-118 Policy reinstatement", "Motor · Property", "1.2k", True),
            ("KB-204 Auto-renewal failure", "Billing", "980", False),
            ("KB-090 Goodwill & waiver", "Complaints", "640", False),
            ("KB-152 Medical card reissue", "Medical", "1.5k", False),
            ("KB-061 Claim status FAQ", "Claims", "2.1k", False),
            ("KB-133 WhatsApp opt-in", "Channels", "410", False)]
    ay2 = top + 48
    for t, cat, views, act in arts:
        if act:
            s.append(rrect(ix + 8, ay2, lw - 16, 44, r=6, fill="#EAF2FB"))
            s.append(rrect(ix + 8, ay2, 3, 44, fill=prim))
        s.append(txt(ix + 18, ay2 + 18, t, size=9.8, color=UI["ink"], weight="700"))
        s.append(txt(ix + 18, ay2 + 33, f"{cat} · {views} views", size=8.4, color=UI["sub"], weight="500"))
        ay2 += 48
    # middle: article view (callout 2/4)
    mxr = ix + lw + gap
    s.append(card(mxr, top, mw, bh, "KB-118 · Policy reinstatement after lapse", "case", prim, pf=pf))
    s.append(callout(2, mxr + mw - 12, top + 12))
    s.append(chip(mxr + 16, top + 48, 74, 18, "Published", "#E4F5EC", text_color="#0B875B", size=8.6, r=9))
    s.append(chip(mxr + 96, top + 48, 90, 18, "EN · العربية", pf["chip_bg"], text_color=pf["primary_dk"], size=8.6, r=9))
    s.append(chip(mxr + 192, top + 48, 70, 18, "v3 · 2026", QIC["band"], text_color=QIC["slate2"], size=8.6, r=9))
    s.append(callout(4, mxr + 96, top + 44))
    lines = ["Summary", "When a policy lapses after an auto-renewal payment failure, it can be",
             "reinstated within the grace window on receipt of the outstanding premium.",
             "", "Steps", "1. Confirm the customer identity against the Customer Master.",
             "2. Verify the lapsed policy and outstanding premium from Azentio.",
             "3. Issue a secure SkipCash payment link for the premium due.",
             "4. On payment confirmation, request reinstatement in the core system.",
             "5. Log the interaction and close the case with the reinstatement outcome.",
             "", "Related: KB-204 (auto-renewal failure) · KB-090 (goodwill & waiver)"]
    tyy = top + 78
    for ln in lines:
        b = ln in ("Summary", "Steps")
        s.append(txt(mxr + 18, tyy, ln, size=(10.4 if b else 9.6),
                     color=(deep if b else UI["ink"]), weight=("800" if b else "500")))
        tyy += 16 if ln else 9
    # right: deflection + related (callout 3)
    rxr = ix + lw + mw + gap * 2
    s.append(card(rxr, top, rw, bh * 0.5 - 7, "Self-service deflection", "gauge", prim, pf=pf))
    s.append(callout(3, rxr + rw - 12, top + 12))
    s.append(gauge_ring(rxr + rw/2, top + 96, 42, 0.63, "#0B875B", "Portal deflection rate", "63%"))
    s.append(txt(rxr + rw/2, top + 150, "cases avoided via Insursa self-service", size=8.6, color=UI["sub"], weight="500", anchor="middle"))
    ry2 = top + bh*0.5 + 7
    s.append(card(rxr, ry2, rw, bh*0.5 - 7, "Used on cases", "case", prim, pf=pf))
    ky = ry2 + 48
    for cs, st in [("INC-2043", "linked"), ("TKT-3120", "resolved FCR"), ("CMP-3021", "referenced")]:
        s.append(rrect(rxr + 12, ky, rw - 24, 30, r=6, fill=UI["field"], stroke=UI["cardline"], sw=1))
        s.append(txt(rxr + 22, ky + 19, cs, size=10, color=UI["ink"], weight="700"))
        s.append(txt(rxr + rw - 22, ky + 19, st, size=8.8, color=prim, weight="600", anchor="end"))
        ky += 36
    return "".join(s)


# ====================================================================== R16
R16 = dict(
    id="FR-Cmp", headline="Complaints Management & Regulatory Handling",
    title="Complaints & Regulatory (QCB)",
    sources=["RFP §5.2 / §15", "BRD §11.5 / §2.3", "Proposal — Complaints dept."],
    text=["Standardized complaint handling for the Complaints Management department.",
          "Regulatory tracking aligned to QCB and Qatari data-protection obligations.",
          "Root-cause, redress, resolution and full audit for regulatory reporting."],
    addressed=["Complaints are a dedicated case type with a High-priority SLA (30 min / 1 day).",
               "Regulatory fields capture QCB-reportability, category and redress.",
               "Multi-level escalation reaches management for high-impact complaints.",
               "Every action is audited and reportable for compliance review."],
)


def c_r16(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, "Cases  ›  CMP-3021 · Complaint", "CMP-3021")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    # header
    s.append(rrect(ix, top, iw, 56, r=8, fill="#fff", stroke=UI["cardline"], sw=1.1))
    s.append(rrect(ix, top, 4, 56, r=2, fill="#C0392B"))
    s.append(mini_chip("case", "#C0392B", ix + 14, top + 14, 28, cloud=(pf["key"]=="salesforce")))
    s.append(txt(ix + 54, top + 24, "CMP-3021 · Billing complaint — duplicate premium charge", size=14, color=UI["ink"], weight="800"))
    s.append(txt(ix + 54, top + 43, "Fatima Al-Ansari · Complaints Management · opened 6h ago", size=10, color=UI["sub"], weight="500"))
    s.append(chip(ix + iw - 214, top + 18, 92, 20, "Complaint", "#FDECEC", text_color="#B4342B", size=10, r=10))
    s.append(chip(ix + iw - 114, top + 18, 100, 20, "QCB reportable", "#FBF1DA", text_color="#8A6D1E", size=9, r=10))
    # chevrons
    chy = top + 64
    s.append(chevrons(ix, chy, iw, 32, ["Logged", "Acknowledged", "Investigation", "Redress", "Resolved", "Closed"], 2, "#C0392B", done_color="#B4342B"))
    by = chy + 48
    bh = cy + ch - by - 14
    gap = 14
    mw = iw * 0.56
    rw = iw - mw - gap
    # left: complaint + regulatory (callout 1/2/3)
    s.append(card(ix, by, mw, bh, "Complaint detail & regulatory tracking", "shield", "#C0392B", pf=pf))
    s.append(callout(1, ix + mw*0.5, by + 12))
    fx = ix + 16
    fw = (mw - 32 - 12) / 2
    dets = [("Complaint category", "Billing · duplicate charge"), ("Channel", "WhatsApp → phone"),
            ("Priority / SLA", "High · 30 min / 1 day"), ("Owner", "M. Haddad (Complaints)"),
            ("QCB reportable", "Yes · logged 21 Jul"), ("Data-protection flag", "None"),
            ("Root cause", "Auto-renewal double-run"), ("Redress", "Refund QAR 6,200 + apology")]
    for i, (lb, vv) in enumerate(dets):
        col = i % 2; row = i // 2
        reg = lb in ("QCB reportable", "Data-protection flag", "Root cause", "Redress")
        s.append(field_box(fx + col*(fw+12), by + 52 + row*54, fw, lb, vv,
                           vcolor=("#8A6D1E" if lb == "QCB reportable" else UI["ink"])))
    s.append(callout(2, fx + fw*2 + 6, by + 52 + 2*54))
    s.append(callout(3, fx + fw*2 + 6, by + 52 + 3*54))
    # right: SLA + escalation + audit (callout 4)
    rxr = ix + mw + gap
    s.append(card(rxr, by, rw, bh, "SLA · escalation · audit", "clock", prim, pf=pf))
    s.append(callout(4, rxr + rw - 12, by + 12))
    s.append(rrect(rxr + 12, by + 48, rw - 24, 40, r=8, fill="#FDECEC"))
    s.append(txt(rxr + 22, by + 66, "Resolution SLA", size=9, color="#B4342B", weight="700"))
    s.append(txt(rxr + rw - 22, by + 66, "00:22 left", size=13, color="#B4342B", weight="800", anchor="end"))
    s.append(txt(rxr + 22, by + 80, "High priority · 1 business day", size=8.4, color="#B4342B", weight="500"))
    hy = by + 100
    for g, gc, tt, sub, wn in [("case", "#C0392B", "Complaint logged", "WhatsApp · agent L. Fahad", "6h"),
                                ("people", prim, "Acknowledged to customer", "SLA ack 30 min", "6h"),
                                ("bolt", "#E8A33D", "Escalated → manager", "QCB reportable", "5h"),
                                ("flow", prim, "Root cause identified", "billing system", "3h"),
                                ("mail", prim, "Redress approved", "refund + apology", "1h"),
                                ("lock", GOLD, "Audit entry · reportable", "compliance pack", "1h")]:
        s.append(timeline_item(rxr + 12, hy, rw - 24, g, gc, tt, sub, wn))
        hy += 48
    return "".join(s)


# ====================================================================== R17
R17 = dict(
    id="FR-Exec", headline="Executive & Management Reporting",
    title="Executive Management Dashboard",
    sources=["RFP §10.2", "BRD §12.2 / §13.3", "Proposal — management visibility"],
    text=["Management and executive reporting for departmental performance and service trends.",
          "KPI monitoring: SLA, resolution, escalation analysis, customer-servicing trends.",
          "Real-time oversight with drill-down and export."],
    addressed=["Executive KPI tiles give management real-time operational oversight.",
               "Service and satisfaction trends are tracked over time.",
               "A departmental league table ranks performance against SLA.",
               "Escalation analysis and export support governance review."],
)


def c_r17(pf, ax, ay, aw, ah, req):
    prim, deep = pf["primary"], pf["deep"]
    tool = "Power BI" if pf["key"] == "microsoft" else "CRM Analytics"
    win, (cx, cy, cw, ch) = _content(pf, ax, ay, aw, ah, f"Dashboards  ›  Executive ({tool})", "Executive")
    s = [win]
    ix, iw = cx + 16, cw - 32
    top = cy + 14
    # KPI tiles (callout 1)
    tiles = [("92.4%", "CSAT (30d)", "#0B875B", "▲ 1.8"), ("94.6%", "SLA compliance", prim, "▲ 1.2"),
             ("4.6h", "Avg resolution", "#3E7CB1", "▼ 0.4h"), ("1,204", "Cases MTD", "#E8A33D", "▲ 6%"),
             ("88%", "Retention (YTD)", "#7A5CC0", "▲ 2%")]
    tw = (iw - 4*12) / 5
    for i, (v, l, c, d) in enumerate(tiles):
        s.append(stat_tile(ix + i*(tw+12), top, tw, 64, v, l, c, sub=d))
    s.append(callout(1, ix + tw - 6, top))
    # charts row
    ry = top + 78
    rh = (cy + ch - ry - 14) * 0.5
    gap = 12
    c1 = iw * 0.42
    c2 = iw * 0.3
    c3 = iw - c1 - c2 - gap*2
    # trend (callout 2)
    s.append(card(ix, ry, c1, rh, "Service & satisfaction trend (6 months)", "gauge", prim, pf=pf))
    s.append(callout(2, ix + c1 - 12, ry + 12))
    s.append(line_chart(ix + 16, ry + 54, c1 - 32, rh - 96, [86, 88, 87, 90, 91, 92], "#0B875B"))
    s.append(line_chart(ix + 16, ry + 54, c1 - 32, rh - 96, [78, 80, 83, 82, 85, 87], prim))
    s.append(txt(ix + 20, ry + rh - 22, "— CSAT   — SLA compliance", size=9, color=UI["sub"], weight="600"))
    # escalation donut (callout 4)
    s.append(card(ix + c1 + gap, ry, c2, rh, "Escalations by level", "pbi", prim, pf=pf))
    s.append(callout(4, ix + c1 + gap + c2 - 12, ry + 12))
    s.append(donut(ix + c1 + gap + c2*0.34, ry + rh*0.56, min(rh*0.28, 52),
                   [(52, prim), (28, "#E8A33D"), (14, "#C0392B"), (6, "#7A5CC0")]))
    ly = ry + 54
    for lbl, cc in [("L1 52%", prim), ("L2 28%", "#E8A33D"), ("L3 14%", "#C0392B"), ("L4 6%", "#7A5CC0")]:
        s.append(f'<rect x="{ix+c1+gap+c2*0.6}" y="{ly-8}" width="10" height="10" rx="2" fill="{cc}"/>')
        s.append(txt(ix + c1 + gap + c2*0.6 + 15, ly, lbl, size=9, color=UI["ink"], weight="600"))
        ly += 19
    # gauges (callout)
    s.append(card(ix + c1 + c2 + gap*2, ry, c3, rh, "This month", "gauge", prim, pf=pf))
    s.append(gauge_ring(ix + c1 + c2 + gap*2 + c3/2, ry + rh*0.55, min(rh*0.3, 50), 0.946, "#0B875B", "SLA vs 90% target", "94.6%"))
    # league table (callout 3)
    by = ry + rh + 14
    bh2 = cy + ch - by - 14
    s.append(card(ix, by, iw, bh2, "Departmental performance league — ranked by SLA (drill-down · export)", "pbi", prim, pf=pf))
    s.append(chip(ix + iw - 132, by + 12, 56, 18, "Export", pf["chip_bg"], text_color=pf["primary_dk"], size=8.6, r=9))
    s.append(chip(ix + iw - 72, by + 12, 56, 18, "Subscribe", pf["chip_bg"], text_color=pf["primary_dk"], size=8.4, r=9))
    s.append(callout(3, ix + iw - 12, by + 12))
    cols = ["Rank", "Department", "CSAT", "SLA %", "Avg resolution", "Escalations", "Trend"]
    colw = [iw*0.08, iw*0.24, iw*0.12, iw*0.13, iw*0.18, iw*0.14, iw*0.11]
    rows = [["1", "Sales & BD", ("95%", "#0B875B"), ("95%", "#0B875B"), "2.6h", "1", ("▲", "#0B875B")],
            ["2", "Customer Service", ("93%", "#0B875B"), ("96%", "#0B875B"), "3.2h", "4", ("▲", "#0B875B")],
            ["3", "Underwriting", ("90%", "#0B875B"), ("93%", "#0B875B"), "6.1h", "3", ("▬", "#E8A33D")],
            ["4", "Claims", ("89%", "#E8A33D"), ("91%", "#0B875B"), "5.4h", "7", ("▲", "#0B875B")],
            ["5", "Complaints", ("84%", "#E8A33D"), ("89%", "#E8A33D"), "8.0h", "11", ("▼", "#C0392B")]]
    s.append(table(ix + 12, by + 42, iw - 24, cols, rows, colw, rowh=(bh2-54)/6))
    return "".join(s)


CARDS = [
    ("r1-customer360", R1, c_r1),
    ("r2-interaction-log", R2, c_r2),
    ("r3-ticket-incident", R3, c_r3),
    ("r4-sla-escalation", R4, c_r4),
    ("r5-omnichannel", R5, c_r5),
    ("r6-routing-queues", R6, c_r6),
    ("r7-sales-pipeline", R7, c_r7),
    ("r8-dashboards-kpi", R8, c_r8),
    ("r9-integration", R9, c_r9),
    ("r10-security-rbac", R10, c_r10),
    ("r11-config-lowcode", R11, c_r11),
    ("r12-ai-assist", R12, c_r12),
    ("r13-notifications", R13, c_r13),
    ("r14-mobile", R14, c_r14),
    ("r15-knowledge", R15, c_r15),
    ("r16-complaints", R16, c_r16),
    ("r17-executive", R17, c_r17),
]


if __name__ == "__main__":
    import sys
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for slug, req, fn in CARDS:
        if which not in ("all", slug):
            continue
        for pf, pk in [(MS, "ms"), (SF, "sf")]:
            svg = build_card(pf, req, fn, f"{req['id']} · {req['title']}")
            out = f"../svg/{pk}-{slug}.svg"
            save(svg, out)
            print("wrote", out)
