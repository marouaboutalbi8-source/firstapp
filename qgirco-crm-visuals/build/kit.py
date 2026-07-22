# -*- coding: utf-8 -*-
"""
Shared SVG layout engine + brand/icon library for the QGIRCO CRM solution visuals.

Every diagram is drawn on an identical canvas with identical chrome (header, footer,
legend rail) so the Microsoft Dynamics 365 set and the Salesforce set are visually
consistent. Only the platform palette and the product components differ.

Company: QGIRCO — Qatar General Insurance & Reinsurance Company
"""

from html import escape as _esc

# ----------------------------------------------------------------------------
# Canvas
# ----------------------------------------------------------------------------
W, H = 1760, 1100
HEADER_H = 104
FOOTER_H = 46
MARGIN = 40

# ----------------------------------------------------------------------------
# QGIRCO customer brand chrome  (corporate deep blue + gold)
# NOTE: palette approximates the QGIRCO corporate identity (deep blue + gold);
# swap the hex values below if exact brand colours are provided.
# ----------------------------------------------------------------------------
QIC = dict(
    maroon="#0B3D91",       # QGIRCO corporate blue — customer primary
    maroon_dk="#082C6B",
    slate="#0E2647",        # deep navy
    slate2="#1C3A63",
    gold="#C79A3B",         # QGIRCO gold accent
    ink="#1B2733",
    sub="#5A6B7B",
    line="#D5DEE7",
    panel="#FFFFFF",
    bg="#EEF2F6",
    band="#F6F8FB",
)

# ----------------------------------------------------------------------------
# Platform palettes
# ----------------------------------------------------------------------------
MS = dict(
    key="microsoft",
    name="Microsoft Dynamics 365",
    tagline="Customer Engagement · Power Platform · Azure",
    primary="#0F6CBD",       # Fluent communication blue
    primary_dk="#0A4C86",
    deep="#052B4E",
    accent="#50E6FF",        # azure cyan accent
    tile="#FFFFFF",
    tile_edge="#BBD3E8",
    tile_head="#0F6CBD",
    chip_bg="#E8F1FB",
    integ="Azure Integration Services",
    integ_short="APIM · Logic Apps · Service Bus",
    automation="Power Automate",
    analytics="Power BI",
    ai="Copilot",
    identity="Microsoft Entra ID",
)

SF = dict(
    key="salesforce",
    name="Salesforce",
    tagline="Sales Cloud · Service Cloud · Platform",
    primary="#0D9DDA",       # Salesforce cloud blue
    primary_dk="#0B5CAB",
    deep="#032D60",          # Salesforce navy
    accent="#FE9339",        # Salesforce warm accent (Astro)
    tile="#FFFFFF",
    tile_edge="#AED9F0",
    tile_head="#0D9DDA",
    chip_bg="#E3F3FC",
    integ="MuleSoft Anypoint Platform",
    integ_short="API-led · reusable assets",
    automation="Flow",
    analytics="CRM Analytics",
    ai="Einstein",
    identity="Salesforce Identity",
)

# ----------------------------------------------------------------------------
# low-level helpers
# ----------------------------------------------------------------------------
FONT = "'Segoe UI','Helvetica Neue',Arial,'Liberation Sans',sans-serif"


def esc(s):
    return _esc(str(s), quote=True)


def txt(x, y, s, size=15, color="#1B2733", weight="400", anchor="start",
        spacing=None, italic=False, family=FONT, opacity=None):
    extra = ""
    if spacing is not None:
        extra += f' letter-spacing="{spacing}"'
    if italic:
        extra += ' font-style="italic"'
    if opacity is not None:
        extra += f' opacity="{opacity}"'
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" '
            f'font-size="{size}" font-weight="{weight}" fill="{color}" '
            f'text-anchor="{anchor}"{extra}>{esc(s)}</text>')


def wraptext(x, y, s, size, color, weight="400", anchor="middle",
             max_chars=22, lh=None, family=FONT):
    """Simple word-wrap into tspans."""
    lh = lh or (size + 4)
    words = str(s).split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if len(t) > max_chars and cur:
            lines.append(cur)
            cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    out = [f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
           f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}">']
    for i, ln in enumerate(lines):
        dy = 0 if i == 0 else lh
        out.append(f'<tspan x="{x:.1f}" dy="{dy}">{esc(ln)}</tspan>')
    out.append('</text>')
    return "".join(out), len(lines)


def rrect(x, y, w, h, r=12, fill="#fff", stroke=None, sw=1.5, opacity=None,
          dash=None):
    a = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    if dash:
        a += f' stroke-dasharray="{dash}"'
    if opacity is not None:
        a += f' opacity="{opacity}"'
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'rx="{r}" ry="{r}" fill="{fill}"{a}/>')


def line(x1, y1, x2, y2, color="#9fb0c0", w=2, dash=None, cap="round",
         marker=None, opacity=None):
    a = f' stroke-dasharray="{dash}"' if dash else ""
    if marker:
        a += f' marker-end="url(#{marker})"'
    if opacity is not None:
        a += f' opacity="{opacity}"'
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{w}" stroke-linecap="{cap}"{a}/>')


def path(d, fill="none", stroke=None, sw=2, dash=None, cap="round",
         marker=None, opacity=None):
    a = ""
    if stroke:
        a += f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}" stroke-linejoin="round"'
    if dash:
        a += f' stroke-dasharray="{dash}"'
    if marker:
        a += f' marker-end="url(#{marker})"'
    if opacity is not None:
        a += f' opacity="{opacity}"'
    return f'<path d="{d}" fill="{fill}"{a}/>'


def chip(x, y, w, h, label, fill, text_color="#fff", size=12, r=None,
         weight="600", edge=None):
    r = r if r is not None else h / 2
    s = [rrect(x, y, w, h, r=r, fill=fill, stroke=edge, sw=1)]
    s.append(txt(x + w / 2, y + h / 2 + size * 0.35, label, size=size,
                 color=text_color, weight=weight, anchor="middle"))
    return "".join(s)


# ----------------------------------------------------------------------------
# defs: gradients, shadow, arrowheads
# ----------------------------------------------------------------------------
def defs(pf):
    return f'''<defs>
  <linearGradient id="qicHead" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{QIC['slate']}"/>
    <stop offset="0.62" stop-color="{QIC['maroon_dk']}"/>
    <stop offset="1" stop-color="{QIC['maroon']}"/>
  </linearGradient>
  <linearGradient id="pfBadge" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{pf['primary']}"/>
    <stop offset="1" stop-color="{pf['primary_dk']}"/>
  </linearGradient>
  <linearGradient id="pfBand" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{pf['primary']}"/>
    <stop offset="1" stop-color="{pf['deep']}"/>
  </linearGradient>
  <linearGradient id="aiGrad" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#8E5BE8"/>
    <stop offset="1" stop-color="{pf['primary']}"/>
  </linearGradient>
  <filter id="ds" x="-8%" y="-8%" width="116%" height="120%">
    <feDropShadow dx="0" dy="2.5" stdDeviation="4.5" flood-color="#1b283a" flood-opacity="0.16"/>
  </filter>
  <filter id="dsSoft" x="-20%" y="-20%" width="140%" height="150%">
    <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#1b283a" flood-opacity="0.13"/>
  </filter>
  <marker id="arr" markerWidth="11" markerHeight="11" refX="8.5" refY="5.5" orient="auto">
    <path d="M1,1 L9.5,5.5 L1,10" fill="none" stroke="{QIC['sub']}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="arrP" markerWidth="11" markerHeight="11" refX="8.5" refY="5.5" orient="auto">
    <path d="M1,1 L9.5,5.5 L1,10" fill="none" stroke="{pf['primary_dk']}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="arrG" markerWidth="11" markerHeight="11" refX="8.5" refY="5.5" orient="auto">
    <path d="M1,1 L9.5,5.5 L1,10" fill="none" stroke="{QIC['gold']}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="dot" markerWidth="8" markerHeight="8" refX="4" refY="4">
    <circle cx="4" cy="4" r="3" fill="{pf['primary']}"/>
  </marker>
</defs>'''


# ----------------------------------------------------------------------------
# QGIRCO logo mark
# ----------------------------------------------------------------------------
def qic_logo(cx, cy, r=26):
    """Abstract shield/pearl mark for QGIRCO on the maroon header."""
    s = []
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" opacity="0.10"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r-4}" fill="none" stroke="{QIC["gold"]}" stroke-width="2"/>')
    # stylised 'Q' with insurance shield
    s.append(f'<path d="M{cx} {cy-14} L{cx+13} {cy-6} L{cx+13} {cy+7} '
             f'Q{cx+13} {cy+13} {cx} {cy+16} Q{cx-13} {cy+13} {cx-13} {cy+7} '
             f'L{cx-13} {cy-6} Z" fill="#ffffff"/>')
    s.append(f'<path d="M{cx} {cy-8} L{cx+7} {cy-3.5} L{cx+7} {cy+4} '
             f'Q{cx+7} {cy+7.5} {cx} {cy+9.5} Q{cx-7} {cy+7.5} {cx-7} {cy+4} '
             f'L{cx-7} {cy-3.5} Z" fill="{QIC["maroon"]}"/>')
    return "".join(s)


# ----------------------------------------------------------------------------
# header / footer
# ----------------------------------------------------------------------------
def header(pf, section, title, subtitle):
    s = [f'<rect x="0" y="0" width="{W}" height="{HEADER_H}" fill="url(#qicHead)"/>']
    s.append(f'<rect x="0" y="{HEADER_H-4}" width="{W}" height="4" fill="{QIC["gold"]}"/>')
    s.append(qic_logo(MARGIN + 30, HEADER_H / 2))
    lx = MARGIN + 74
    s.append(txt(lx, 40, "QGIRCO", size=27, color="#ffffff", weight="800", spacing="2"))
    s.append(txt(lx, 63, "Qatar General Insurance & Reinsurance Company",
                 size=13.5, color="#EBD9C2", weight="500"))
    s.append(txt(lx, 84, section, size=11.5, color=QIC["gold"], weight="700", spacing="2.5"))
    # centre title
    s.append(txt(W/2 + 60, 52, title, size=22, color="#ffffff", weight="700", anchor="middle"))
    s.append(txt(W/2 + 60, 76, subtitle, size=13, color="#D9C3AD", weight="400",
                 anchor="middle", italic=True))
    # platform badge (right)
    bw, bh = 268, 52
    bx, by = W - MARGIN - bw, (HEADER_H - bh) / 2
    s.append(rrect(bx, by, bw, bh, r=10, fill="#ffffff", opacity=0.97))
    s.append(platform_glyph(pf, bx + 26, by + bh/2, 15))
    s.append(txt(bx + 50, by + 23, pf["name"], size=15.5, color=pf["deep"], weight="800"))
    s.append(txt(bx + 50, by + 40, pf["tagline"], size=9.6, color=pf["primary_dk"], weight="600"))
    return "".join(s)


def footer(pf, idx):
    y = H - FOOTER_H
    s = [f'<rect x="0" y="{y}" width="{W}" height="{FOOTER_H}" fill="{QIC["slate"]}"/>']
    s.append(f'<rect x="0" y="{y}" width="{W}" height="2.5" fill="{QIC["gold"]}"/>')
    s.append(txt(MARGIN, y + 28, "QGIRCO Enterprise CRM Implementation  ·  Technical Proposal",
                 size=12, color="#CBD6E1", weight="600"))
    s.append(txt(W/2, y + 28,
                 f"Solution option: {pf['name']}", size=11.5, color=QIC["gold"],
                 weight="700", anchor="middle"))
    s.append(txt(W - MARGIN, y + 28,
                 f"Trion Technology  ×  Volge   ·   {idx}",
                 size=11.5, color="#CBD6E1", weight="500", anchor="end"))
    return "".join(s)


def canvas_open(pf):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" font-family="{FONT}">'
            + defs(pf)
            + f'<rect width="{W}" height="{H}" fill="{QIC["bg"]}"/>')


def canvas_close():
    return '</svg>'


def section_label(x, y, text, color, w=None):
    """Small vertical-free section tag used on the left of layer bands."""
    return txt(x, y, text, size=11.5, color=color, weight="800", spacing="2")


# ----------------------------------------------------------------------------
# generic pictograms (channels, systems)  -- 0..1 space scaled into box
# ----------------------------------------------------------------------------
def _g(x, y, sc, body):
    return f'<g transform="translate({x},{y}) scale({sc})">{body}</g>'


def ic_phone(x, y, sc=1, c="#2A7DE1"):
    b = (f'<path d="M6 4 Q4 4 4 6 Q4 20 18 20 Q20 20 20 18 L20 15 L15 13 L13 15 '
         f'Q9 13 9 9 L11 7 L9 2 L6 4 Z" fill="{c}"/>')
    return _g(x, y, sc, b)


def ic_whatsapp(x, y, sc=1, c="#25D366"):
    b = (f'<circle cx="12" cy="12" r="11" fill="{c}"/>'
         f'<path d="M8.5 7.5 Q7 7.5 7 9.2 Q7 15 13 17 Q15 17.4 16 16 L16.4 15 L13.6 13.6 '
         f'L12.7 14.6 Q10 13.4 9.6 10.8 L10.6 9.9 L9.4 7.5 Z" fill="#fff"/>')
    return _g(x, y, sc, b)


def ic_mail(x, y, sc=1, c="#2A7DE1"):
    b = (f'<rect x="2" y="5" width="20" height="14" rx="2.4" fill="{c}"/>'
         f'<path d="M3 6.5 L12 13 L21 6.5" fill="none" stroke="#fff" stroke-width="1.8"/>')
    return _g(x, y, sc, b)


def ic_web(x, y, sc=1, c="#2A7DE1"):
    b = (f'<circle cx="12" cy="12" r="10" fill="{c}"/>'
         f'<ellipse cx="12" cy="12" rx="4.2" ry="10" fill="none" stroke="#fff" stroke-width="1.4"/>'
         f'<line x1="2" y1="12" x2="22" y2="12" stroke="#fff" stroke-width="1.4"/>'
         f'<line x1="4" y1="7" x2="20" y2="7" stroke="#fff" stroke-width="1.1"/>'
         f'<line x1="4" y1="17" x2="20" y2="17" stroke="#fff" stroke-width="1.1"/>')
    return _g(x, y, sc, b)


def ic_portal(x, y, sc=1, c="#2A7DE1"):
    b = (f'<rect x="2.5" y="3.5" width="19" height="17" rx="2.2" fill="{c}"/>'
         f'<rect x="2.5" y="3.5" width="19" height="4.5" rx="2.2" fill="#ffffff" opacity="0.85"/>'
         f'<circle cx="5.4" cy="5.8" r="0.9" fill="{c}"/>'
         f'<rect x="5" y="11" width="6" height="6" rx="1" fill="#fff"/>'
         f'<rect x="13" y="11" width="6" height="2" rx="1" fill="#fff"/>'
         f'<rect x="13" y="15" width="6" height="2" rx="1" fill="#fff"/>')
    return _g(x, y, sc, b)


def ic_walkin(x, y, sc=1, c="#2A7DE1"):
    b = (f'<circle cx="12" cy="6.5" r="3.3" fill="{c}"/>'
         f'<path d="M6 21 Q6 13 12 13 Q18 13 18 21 Z" fill="{c}"/>')
    return _g(x, y, sc, b)


def ic_card(x, y, sc=1, c="#F2A93B"):
    b = (f'<rect x="2" y="5" width="20" height="14" rx="2.4" fill="{c}"/>'
         f'<rect x="2" y="8.4" width="20" height="3" fill="#7a4d10"/>'
         f'<rect x="5" y="14" width="7" height="2.2" rx="1" fill="#fff"/>')
    return _g(x, y, sc, b)


def ic_db(x, y, sc=1, c="#4C6B8A", check=False, lock=False):
    b = (f'<ellipse cx="12" cy="5" rx="9" ry="3.2" fill="{c}"/>'
         f'<path d="M3 5 V19 Q3 22 12 22 Q21 22 21 19 V5" fill="{c}"/>'
         f'<ellipse cx="12" cy="5" rx="9" ry="3.2" fill="#ffffff" opacity="0.22"/>'
         f'<path d="M3 12 Q3 15 12 15 Q21 15 21 12" fill="none" stroke="#ffffff" stroke-width="1.2" opacity="0.6"/>')
    if check:
        b += ('<circle cx="18" cy="19" r="5" fill="#1E9E5A"/>'
              '<path d="M15.5 19 L17.4 20.8 L20.6 17" fill="none" stroke="#fff" stroke-width="1.8"/>')
    if lock:
        b += ('<rect x="14.5" y="16.5" width="7" height="6" rx="1.2" fill="#C9A24B"/>'
              '<path d="M15.8 16.5 V15 Q15.8 12.8 18 12.8 Q20.2 12.8 20.2 15 V16.5" fill="none" stroke="#C9A24B" stroke-width="1.4"/>')
    return _g(x, y, sc, b)


def ic_core(x, y, sc=1, c="#3F5D7A"):
    """Azentio core insurance — gear + doc."""
    b = (f'<rect x="3" y="3" width="14" height="18" rx="2" fill="{c}"/>'
         f'<rect x="5.5" y="6" width="9" height="1.6" rx="0.8" fill="#fff" opacity="0.8"/>'
         f'<rect x="5.5" y="9" width="9" height="1.6" rx="0.8" fill="#fff" opacity="0.8"/>'
         f'<rect x="5.5" y="12" width="6" height="1.6" rx="0.8" fill="#fff" opacity="0.8"/>'
         f'<circle cx="17.5" cy="17.5" r="5.2" fill="{c}"/>'
         f'<circle cx="17.5" cy="17.5" r="2" fill="#fff"/>'
         f'<g fill="#fff">'
         f'<rect x="16.7" y="10.8" width="1.6" height="2.6"/>'
         f'<rect x="16.7" y="21.6" width="1.6" height="2.6"/>'
         f'<rect x="11.1" y="16.7" width="2.6" height="1.6"/>'
         f'<rect x="21.3" y="16.7" width="2.6" height="1.6"/></g>')
    return _g(x, y, sc, b)


def ic_shield(x, y, sc=1, c="#0F6CBD"):
    b = (f'<path d="M12 2 L21 5.5 V12 Q21 19 12 22.5 Q3 19 3 12 V5.5 Z" fill="{c}"/>'
         f'<path d="M8 12 L11 15 L16.5 8.5" fill="none" stroke="#fff" stroke-width="2"/>')
    return _g(x, y, sc, b)


def ic_gear(x, y, sc=1, c="#5A6B7B"):
    b = (f'<circle cx="12" cy="12" r="5" fill="{c}"/><circle cx="12" cy="12" r="2.1" fill="#fff"/>'
         f'<g fill="{c}">'
         f'<rect x="11" y="1.5" width="2" height="4"/><rect x="11" y="18.5" width="2" height="4"/>'
         f'<rect x="1.5" y="11" width="4" height="2"/><rect x="18.5" y="11" width="4" height="2"/>'
         f'<rect x="4" y="4" width="2" height="4" transform="rotate(45 5 6)"/>'
         f'<rect x="18" y="16" width="2" height="4" transform="rotate(45 19 18)"/>'
         f'<rect x="18" y="4" width="2" height="4" transform="rotate(-45 19 6)"/>'
         f'<rect x="4" y="16" width="2" height="4" transform="rotate(-45 5 18)"/></g>')
    return _g(x, y, sc, b)


def ic_chart(x, y, sc=1, c="#F2C811"):
    b = (f'<rect x="3" y="12" width="4" height="9" rx="1" fill="{c}"/>'
         f'<rect x="10" y="7" width="4" height="14" rx="1" fill="{c}"/>'
         f'<rect x="17" y="3" width="4" height="18" rx="1" fill="{c}"/>')
    return _g(x, y, sc, b)


def ic_flow(x, y, sc=1, c="#0B53CE"):
    b = (f'<circle cx="5" cy="6" r="3" fill="{c}"/>'
         f'<circle cx="19" cy="6" r="3" fill="{c}"/>'
         f'<circle cx="12" cy="18" r="3" fill="{c}"/>'
         f'<path d="M5 9 V12 Q5 15 12 15 M19 9 V12 Q19 15 12 15" fill="none" stroke="{c}" stroke-width="1.8"/>')
    return _g(x, y, sc, b)


def ic_route(x, y, sc=1, c="#0F6CBD"):
    b = (f'<circle cx="5" cy="5" r="2.6" fill="{c}"/>'
         f'<circle cx="5" cy="19" r="2.6" fill="{c}"/>'
         f'<circle cx="19" cy="12" r="2.6" fill="{c}"/>'
         f'<path d="M5 7.6 V16.4 M7 5 Q19 5 19 12 M7 19 Q19 19 19 12" fill="none" stroke="{c}" stroke-width="1.7"/>')
    return _g(x, y, sc, b)


def ic_clock(x, y, sc=1, c="#C0392B"):
    b = (f'<circle cx="12" cy="12" r="10" fill="{c}"/>'
         f'<circle cx="12" cy="12" r="10" fill="none" stroke="#fff" stroke-width="1" opacity="0.4"/>'
         f'<path d="M12 6 V12 L16 14" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>')
    return _g(x, y, sc, b)


def ic_people(x, y, sc=1, c="#0F6CBD"):
    b = (f'<circle cx="8" cy="8" r="3.2" fill="{c}"/>'
         f'<circle cx="16.5" cy="8.5" r="2.7" fill="{c}" opacity="0.75"/>'
         f'<path d="M2.5 20 Q2.5 12.5 8 12.5 Q13.5 12.5 13.5 20 Z" fill="{c}"/>'
         f'<path d="M13.5 20 Q13.5 13.5 16.5 13.5 Q21.5 13.5 21.5 20 Z" fill="{c}" opacity="0.75"/>')
    return _g(x, y, sc, b)


def ic_user360(x, y, sc=1, c="#0F6CBD"):
    b = (f'<circle cx="12" cy="12" r="10.5" fill="none" stroke="{c}" stroke-width="1.6" stroke-dasharray="3 2.6"/>'
         f'<circle cx="12" cy="10" r="3.4" fill="{c}"/>'
         f'<path d="M5.5 19 Q5.5 13.5 12 13.5 Q18.5 13.5 18.5 19 Z" fill="{c}"/>')
    return _g(x, y, sc, b)


def ic_case(x, y, sc=1, c="#0F6CBD"):
    b = (f'<rect x="3" y="6.5" width="18" height="13" rx="2.2" fill="{c}"/>'
         f'<path d="M9 6.5 V5 Q9 3.5 10.5 3.5 H13.5 Q15 3.5 15 5 V6.5" fill="none" stroke="{c}" stroke-width="1.8"/>'
         f'<rect x="6" y="10" width="12" height="1.7" rx="0.8" fill="#fff" opacity="0.85"/>'
         f'<rect x="6" y="13.5" width="8" height="1.7" rx="0.8" fill="#fff" opacity="0.85"/>')
    return _g(x, y, sc, b)


def ic_bolt(x, y, sc=1, c="#F2A93B"):
    b = f'<path d="M13 2 L4 13 H11 L9 22 L20 10 H12 Z" fill="{c}"/>'
    return _g(x, y, sc, b)


def ic_bell(x, y, sc=1, c="#0F6CBD"):
    b = (f'<path d="M12 3 Q17 3 17 9 V13 L19 16 H5 L7 13 V9 Q7 3 12 3 Z" fill="{c}"/>'
         f'<circle cx="12" cy="18.5" r="2" fill="{c}"/>')
    return _g(x, y, sc, b)


# ----------------------------------------------------------------------------
# platform product glyphs  (simplified, brand-recognisable, always labelled)
# ----------------------------------------------------------------------------
def platform_glyph(pf, cx, cy, r):
    if pf["key"] == "microsoft":
        return ms_logo(cx, cy, r)
    return sf_cloud(cx, cy, r)


def ms_logo(cx, cy, r):
    """Microsoft four-square."""
    g = r * 0.92
    o = g * 0.06
    s = [
        f'<rect x="{cx-g}" y="{cy-g}" width="{g-o}" height="{g-o}" fill="#F25022"/>',
        f'<rect x="{cx+o}" y="{cy-g}" width="{g-o}" height="{g-o}" fill="#7FBA00"/>',
        f'<rect x="{cx-g}" y="{cy+o}" width="{g-o}" height="{g-o}" fill="#00A4EF"/>',
        f'<rect x="{cx+o}" y="{cy+o}" width="{g-o}" height="{g-o}" fill="#FFB900"/>',
    ]
    return "".join(s)


def sf_cloud(cx, cy, r, c="#00A1E0"):
    """Salesforce puffy-cloud mark."""
    sc = r / 15.0
    b = (f'<path d="M6 20 Q1.5 20 1.5 15.5 Q1.5 11.5 5.6 11 Q6 6.5 10.5 6.5 '
         f'Q13.6 6.5 15 9 Q16.4 7.7 18.4 7.7 Q22.5 7.7 22.5 12 '
         f'Q26 12.3 26 16 Q26 20 21.5 20 Z" fill="{c}"/>')
    return f'<g transform="translate({cx-13.7*sc},{cy-13.2*sc}) scale({sc})">{b}</g>'


# product icon chips: return a small square/cloud badge with mini-glyph
def _mini(name, c):
    m = {
        "dyn": f'<circle cx="12" cy="12" r="9" fill="{c}"/><path d="M8 8 H14 Q17 8 17 12 Q17 16 14 16 H8 Z M11 11 V13 H13 Q14 13 14 12 Q14 11 13 11 Z" fill="#fff"/>',
        "pa": f'<path d="M13 2 L4 13 H11 L9 22 L20 10 H12 Z" fill="{c}"/>',
        "papps": f'<path d="M12 2 L22 12 L12 22 L2 12 Z" fill="{c}"/><path d="M12 7 L17 12 L12 17 L7 12 Z" fill="#fff" opacity="0.85"/>',
        "pbi": f'<rect x="3" y="12" width="4" height="9" fill="{c}"/><rect x="10" y="7" width="4" height="14" fill="{c}"/><rect x="17" y="3" width="4" height="18" fill="{c}"/>',
        "ppages": f'<rect x="3" y="4" width="18" height="16" rx="2" fill="{c}"/><rect x="3" y="4" width="18" height="4" rx="2" fill="#fff" opacity="0.7"/><rect x="6" y="11" width="12" height="1.6" fill="#fff"/><rect x="6" y="14.5" width="8" height="1.6" fill="#fff"/>',
        "dv": f'<ellipse cx="12" cy="5" rx="8" ry="2.6" fill="{c}"/><path d="M4 5 V19 Q4 21.6 12 21.6 Q20 21.6 20 19 V5" fill="{c}"/><path d="M4 12 Q4 14.6 12 14.6 Q20 14.6 20 12" fill="none" stroke="#fff" stroke-width="1.2"/>',
        "azure": f'<path d="M9 3 L15 3 L22 20 L14 20 L11.5 13 L14 13 L12 8 L6 20 L2 20 Z" fill="{c}"/>',
        "entra": f'<circle cx="12" cy="12" r="9" fill="none" stroke="{c}" stroke-width="2.4"/><circle cx="12" cy="12" r="3.4" fill="{c}"/>',
        "purview": f'<path d="M12 2 L21 6 V12 Q21 19 12 22 Q3 19 3 12 V6 Z" fill="{c}"/><circle cx="12" cy="11" r="3.4" fill="#fff"/>',
        "defender": f'<path d="M12 2 L21 5.5 V12 Q21 19 12 22.5 Q3 19 3 12 V5.5 Z" fill="{c}"/><path d="M8 12 L11 15 L16.5 8.5" fill="none" stroke="#fff" stroke-width="2"/>',
        "teams": f'<circle cx="12" cy="12" r="9" fill="{c}"/><rect x="6" y="8" width="12" height="2.4" fill="#fff"/><rect x="10.8" y="8" width="2.4" height="9" fill="#fff"/>',
        "copilot": f'<path d="M6 12 Q6 6 12 6 Q18 6 18 12 Q18 18 12 18 Q9 18 8 15" fill="none" stroke="url(#aiGrad)" stroke-width="3" stroke-linecap="round"/><circle cx="18.5" cy="6" r="2.4" fill="#8E5BE8"/>',
        "shield": f'<path d="M12 2 L21 5.5 V12 Q21 19 12 22.5 Q3 19 3 12 V5.5 Z" fill="{c}"/><path d="M8 12 L11 15 L16.5 8.5" fill="none" stroke="#fff" stroke-width="2"/>',
        "lock": f'<rect x="4" y="10" width="16" height="12" rx="2" fill="{c}"/><path d="M6.5 10 V7 Q6.5 2.5 12 2.5 Q17.5 2.5 17.5 7 V10" fill="none" stroke="{c}" stroke-width="2.4"/><circle cx="12" cy="15" r="2" fill="#fff"/>',
        "user360": f'<circle cx="12" cy="12" r="10.5" fill="none" stroke="{c}" stroke-width="1.8" stroke-dasharray="3 2.6"/><circle cx="12" cy="10" r="3.4" fill="{c}"/><path d="M5.5 19 Q5.5 13.5 12 13.5 Q18.5 13.5 18.5 19 Z" fill="{c}"/>',
        "case": f'<rect x="3" y="6.5" width="18" height="13" rx="2.2" fill="{c}"/><path d="M9 6.5 V5 Q9 3.5 10.5 3.5 H13.5 Q15 3.5 15 5 V6.5" fill="none" stroke="{c}" stroke-width="1.8"/><rect x="6" y="10" width="12" height="1.7" rx="0.8" fill="#fff"/><rect x="6" y="13.5" width="8" height="1.7" rx="0.8" fill="#fff"/>',
        "clock": f'<circle cx="12" cy="12" r="10" fill="{c}"/><path d="M12 6 V12 L16 14" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>',
        "route": f'<circle cx="5" cy="5" r="2.6" fill="{c}"/><circle cx="5" cy="19" r="2.6" fill="{c}"/><circle cx="19" cy="12" r="2.6" fill="{c}"/><path d="M5 7.6 V16.4 M7 5 Q19 5 19 12 M7 19 Q19 19 19 12" fill="none" stroke="{c}" stroke-width="1.7"/>',
        "people": f'<circle cx="8" cy="8" r="3.2" fill="{c}"/><circle cx="16.5" cy="8.5" r="2.7" fill="{c}" opacity="0.75"/><path d="M2.5 20 Q2.5 12.5 8 12.5 Q13.5 12.5 13.5 20 Z" fill="{c}"/><path d="M13.5 20 Q13.5 13.5 16.5 13.5 Q21.5 13.5 21.5 20 Z" fill="{c}" opacity="0.75"/>',
        "flow": f'<circle cx="5" cy="6" r="3" fill="{c}"/><circle cx="19" cy="6" r="3" fill="{c}"/><circle cx="12" cy="18" r="3" fill="{c}"/><path d="M5 9 V11 Q5 15 12 15 M19 9 V11 Q19 15 12 15" fill="none" stroke="{c}" stroke-width="1.8"/>',
        "bolt": f'<path d="M13 2 L4 13 H11 L9 22 L20 10 H12 Z" fill="{c}"/>',
        "bell": f'<path d="M12 3 Q17 3 17 9 V13 L19 16 H5 L7 13 V9 Q7 3 12 3 Z" fill="{c}"/><circle cx="12" cy="18.5" r="2" fill="{c}"/>',
        "search": f'<circle cx="10" cy="10" r="6.5" fill="none" stroke="{c}" stroke-width="2.4"/><line x1="14.8" y1="14.8" x2="21" y2="21" stroke="{c}" stroke-width="2.6" stroke-linecap="round"/>',
        "gauge": f'<path d="M3 18 A9 9 0 0 1 21 18" fill="none" stroke="{c}" stroke-width="2.4"/><line x1="12" y1="18" x2="16" y2="12" stroke="{c}" stroke-width="2.2" stroke-linecap="round"/><circle cx="12" cy="18" r="2" fill="{c}"/>',
    }
    return m.get(name)


def prod_tile(pf, x, y, w, h, title, subtitle=None, glyph=None, glyph_color=None,
              accent=None, small=False):
    """A branded product component tile.
       Microsoft -> square Fluent tile with colored icon chip.
       Salesforce -> cloud-badge tile.
    """
    accent = accent or pf["primary"]
    s = [rrect(x, y, w, h, r=12, fill=pf["tile"], stroke=pf["tile_edge"], sw=1.4)]
    s.append(f'<g filter="url(#dsSoft)">' + rrect(x, y, w, h, r=12, fill="none") + '</g>')
    # accent header strip
    s.append(f'<path d="M{x+12} {y} H{x+w-12} Q{x+w} {y} {x+w} {y+12} V{y+6} '
             f'Q{x+w} {y} {x+w-12} {y} Z" fill="none"/>')
    s.append(rrect(x, y, 5, h, r=2.5, fill=accent))
    # icon chip
    chip_s = 34 if not small else 27
    cxp, cyp = x + 16, y + h/2 - chip_s/2
    s.append(_icon_chip(pf, cxp, cyp, chip_s, glyph, glyph_color or accent))
    tx = x + 16 + chip_s + 12
    if subtitle:
        s.append(txt(tx, y + h/2 - 4, title, size=13.5 if not small else 12.5,
                     color=pf["deep"], weight="700"))
        w2, _ = wraptext(0, 0, "", 1, "#000")  # noop
        s.append(txt(tx, y + h/2 + 14, subtitle, size=10.6 if not small else 10,
                     color=QIC["sub"], weight="500"))
    else:
        s.append(txt(tx, y + h/2 + 5, title, size=13.5 if not small else 12.5,
                     color=pf["deep"], weight="700"))
    return "".join(s)


def _icon_chip(pf, x, y, sz, glyph, color):
    """Render a small product icon inside a rounded (MS) or cloud (SF) chip."""
    sc = sz / 24.0
    mini = _mini(glyph, color) if glyph else None
    if pf["key"] == "salesforce":
        # cloud-shaped chip
        s = [f'<g filter="url(#dsSoft)">' + sf_cloud(x + sz/2, y + sz/2, sz*0.62, c=color) + '</g>']
        if mini:
            s.append(f'<g transform="translate({x+sz*0.28},{y+sz*0.26}) scale({sc*0.52})">{mini}</g>')
        else:
            s.append(sf_cloud(x + sz/2, y + sz/2, sz*0.34, c="#ffffff"))
        return "".join(s)
    else:
        s = [rrect(x, y, sz, sz, r=7, fill="#F3F7FB", stroke=pf["tile_edge"], sw=1)]
        if mini:
            s.append(f'<g transform="translate({x+sz*0.12},{y+sz*0.12}) scale({sc*0.76})">{mini}</g>')
        return "".join(s)


def legend(x, y, items, title="Legend", w=250):
    """items: list of (swatch_kind, color, label). swatch_kind: 'box','line','dash','dot'"""
    rowh = 23
    h = 40 + rowh * len(items)
    s = [rrect(x, y, w, h, r=12, fill="#ffffff", stroke=QIC["line"], sw=1.3)]
    s.append(f'<g filter="url(#dsSoft)">' + rrect(x, y, w, h, r=12, fill="none") + '</g>')
    s.append(txt(x + 16, y + 25, title, size=12.5, color=QIC["ink"], weight="800", spacing="1.5"))
    s.append(line(x + 16, y + 33, x + w - 16, y + 33, color=QIC["line"], w=1))
    cy = y + 33 + 20
    for kind, color, label in items:
        sx = x + 18
        if kind == "box":
            s.append(rrect(sx, cy - 9, 20, 14, r=3, fill=color))
        elif kind == "line":
            s.append(line(sx, cy - 2, sx + 20, cy - 2, color=color, w=3, marker="arr"))
        elif kind == "dash":
            s.append(line(sx, cy - 2, sx + 20, cy - 2, color=color, w=2.4, dash="5 4"))
        elif kind == "dot":
            s.append(f'<circle cx="{sx+10}" cy="{cy-2}" r="6" fill="{color}"/>')
        s.append(txt(sx + 30, cy + 3, label, size=11.3, color=QIC["ink"], weight="500"))
        cy += rowh
    return "".join(s)


def note_ribbon(x, y, w, text, color=None):
    color = color or QIC["gold"]
    h = 30
    s = [rrect(x, y, w, h, r=8, fill="#FFF9EE", stroke=color, sw=1.3)]
    s.append(f'<circle cx="{x+16}" cy="{y+h/2}" r="6.5" fill="{color}"/>')
    s.append(txt(x + 16, y + h/2 + 3.4, "!", size=11, color="#fff", weight="900", anchor="middle"))
    s.append(txt(x + 30, y + h/2 + 4, text, size=11, color=QIC["maroon_dk"], weight="600"))
    return "".join(s)


def title_pill(x, y, text, color, tw=None):
    tw = tw or (len(text) * 8 + 34)
    h = 30
    s = [rrect(x, y, tw, h, r=15, fill=color)]
    s.append(txt(x + tw/2, y + h/2 + 4, text, size=12.5, color="#fff", weight="800",
                 anchor="middle", spacing="1"))
    return "".join(s), tw


def save(svg, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
