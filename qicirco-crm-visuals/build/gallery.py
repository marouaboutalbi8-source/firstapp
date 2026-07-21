# -*- coding: utf-8 -*-
"""Generate index.html gallery + README.md from the card/diagram metadata."""
from cards import CARDS

DIAGRAMS = [
    ("01-architecture", "Enterprise Solution Architecture",
     "Layered reference architecture — engagement channels, CRM engagement layer, integration, systems of record, with security and analytics rails."),
    ("02-integration", "Integration & Data Flow",
     "API-led hub-and-spoke across the nine enterprise interfaces; the CRM consumes the governed customer master, never creates it."),
    ("03-process", "Case Lifecycle · SLA & Escalation",
     "Omnichannel capture to audited resolution: classify, route, SLA timers, multi-level escalation and automation scenarios."),
    ("04-capability-map", "Functional Capability Map",
     "Five capability domains mapped to product components, serving six operational departments."),
]

HEAD = """<header>
  <div class="brand">
    <div class="mark"></div>
    <div>
      <h1>QICIRCO — Enterprise CRM</h1>
      <p>Qatar General Insurance &amp; Reinsurance Company · Technical Proposal · Solution Visuals</p>
    </div>
  </div>
  <p class="intro">Two independently engineered CRM solutions, mapped to every requirement of the RFP,
  BRD and Technical Proposal. Each requirement is shown as a realistic <b>Microsoft Dynamics 365</b> and
  <b>Salesforce</b> screen, annotated to show how the product delivers it. Click any image to open full resolution.
  Prepared by Trion Technology &times; Volge.</p>
</header>"""


def card_block(slug, title, sub, extra=""):
    return f"""<section class="row">
  <div class="rhead"><h2>{title}</h2><p>{sub}</p>{extra}</div>
  <div class="pair">
    <figure><a href="png/ms-{slug}.png" target="_blank"><img src="png/ms-{slug}.png" loading="lazy"></a><figcaption>Microsoft Dynamics 365</figcaption></figure>
    <figure><a href="png/sf-{slug}.png" target="_blank"><img src="png/sf-{slug}.png" loading="lazy"></a><figcaption>Salesforce</figcaption></figure>
  </div>
</section>"""


def build_html():
    parts = []
    parts.append("<h3 class='grp'>Solution architecture &amp; process</h3>")
    for slug, title, sub in DIAGRAMS:
        parts.append(card_block(slug, title, sub))
    parts.append("<h3 class='grp'>Requirement &rarr; realized in product</h3>")
    for slug, req, _ in CARDS:
        srcs = " · ".join(req["sources"])
        extra = f"<div class='tags'><span class='id'>{req['id']}</span><span class='src'>{srcs}</span></div>"
        parts.append(card_block(slug, req["headline"], req["text"][0], extra))
    body = "\n".join(parts)
    css = """
    :root{--maroon:#8A1538;--slate:#16283A;--gold:#C9A24B;--ink:#1B2733;--sub:#5A6B7B;--line:#E2E8EF;--bg:#EEF2F6}
    *{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',Arial,sans-serif;background:var(--bg);color:var(--ink)}
    header{background:linear-gradient(100deg,var(--slate),var(--maroon));color:#fff;padding:34px 48px 30px;border-bottom:4px solid var(--gold)}
    .brand{display:flex;align-items:center;gap:16px}
    .mark{width:46px;height:46px;border-radius:50%;background:#fff2;border:2px solid var(--gold);position:relative}
    .mark:after{content:"";position:absolute;inset:11px;background:var(--maroon);clip-path:polygon(50% 0,100% 30%,100% 75%,50% 100%,0 75%,0 30%)}
    header h1{margin:0;font-size:26px;letter-spacing:1px}header p{margin:2px 0 0;color:#E7D6C4;font-size:13px}
    .intro{max-width:1000px;margin:16px 0 0;color:#EAD9C6;font-size:13.5px;line-height:1.6}
    .grp{margin:34px 48px 4px;font-size:13px;letter-spacing:2px;text-transform:uppercase;color:var(--maroon);border-bottom:2px solid var(--line);padding-bottom:8px}
    .row{margin:24px 48px}
    .rhead h2{margin:0;font-size:19px;color:var(--slate)}
    .rhead p{margin:4px 0 0;color:var(--sub);font-size:13px;max-width:1100px;line-height:1.5}
    .tags{margin-top:8px;display:flex;gap:10px;align-items:center}
    .tags .id{background:var(--slate);color:#fff;font-weight:700;font-size:11px;padding:3px 10px;border-radius:6px}
    .tags .src{color:var(--sub);font-size:11.5px;font-weight:600}
    .pair{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:14px}
    figure{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;box-shadow:0 2px 10px #1b283a1a}
    figure img{display:block;width:100%;height:auto}
    figcaption{padding:9px 14px;font-size:12.5px;font-weight:700;color:var(--slate);border-top:1px solid var(--line);background:#fafbfc}
    @media(max-width:1100px){.pair{grid-template-columns:1fr}.row,.grp{margin-left:20px;margin-right:20px}header{padding:24px}}
    footer{margin:40px 48px;padding:18px 0;border-top:1px solid var(--line);color:var(--sub);font-size:12px}
    """
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>QICIRCO CRM — Solution Visuals</title><style>{css}</style></head>
<body>{HEAD}
{body}
<footer>QICIRCO Enterprise CRM Implementation · Technical Proposal · Microsoft Dynamics 365 and Salesforce solution visuals · Trion Technology &times; Volge.
Company reference &ldquo;QICIRCO&rdquo; per client brief (source documents: QGIRCO).</footer>
</body></html>"""


def build_readme():
    lines = ["# QICIRCO Enterprise CRM — Solution Visuals", "",
             "Professional, enterprise-grade architecture and requirement-realization visuals for the",
             "QICIRCO (Qatar General Insurance & Reinsurance Company) CRM implementation technical proposal,",
             "covering two independently engineered options: **Microsoft Dynamics 365** and **Salesforce**.",
             "",
             "Every visual is tailored to the QICIRCO RFP, BRD and Technical Proposal — not generic CRM art.",
             "Each requirement is shown as a realistic product screen (with QICIRCO insurance data: QID,",
             "policy numbers, Azentio, WhatsApp/WABA, SkipCash, 3CX, Insursa portals) annotated to show how",
             "the platform delivers it.",
             "",
             "> Note: the client brief refers to the company as **QICIRCO**; the source documents name it",
             "> **QGIRCO (Qatar General Insurance & Reinsurance Company)**. Visuals use QICIRCO per the brief.",
             "",
             "## How to view", "",
             "Open `index.html` in a browser for the side-by-side gallery, or browse `png/` (high-res, 3520×2200)",
             "and `svg/` (vector, editable) directly. Regenerate with `python3 build/cards.py all &&",
             "python3 build/diagrams.py all && python3 build/render.py`.",
             "",
             "## Architecture & process diagrams", ""]
    lines.append("| # | Diagram | Microsoft | Salesforce |")
    lines.append("|---|---------|-----------|------------|")
    for slug, title, _ in DIAGRAMS:
        lines.append(f"| — | {title} | `png/ms-{slug}.png` | `png/sf-{slug}.png` |")
    lines += ["", "## Requirement → realized in product", "",
              "| Ref | Requirement | Sources | Microsoft | Salesforce |",
              "|-----|-------------|---------|-----------|------------|"]
    for slug, req, _ in CARDS:
        srcs = "; ".join(req["sources"])
        lines.append(f"| {req['id']} | {req['headline']} | {srcs} | `png/ms-{slug}.png` | `png/sf-{slug}.png` |")
    lines += ["", "## Layout", "",
              "- `build/` — Python generators (`kit.py`, `appkit.py`, `cards.py`, `diagrams.py`, `render.py`, `gallery.py`)",
              "- `svg/` — editable vector source (36 files)",
              "- `png/` — high-resolution renders for direct proposal inclusion (36 files)",
              "- `index.html` — side-by-side review gallery", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    with open("../index.html", "w", encoding="utf-8") as f:
        f.write(build_html())
    with open("../README.md", "w", encoding="utf-8") as f:
        f.write(build_readme())
    print("wrote index.html and README.md")
