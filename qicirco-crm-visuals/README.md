# QICIRCO Enterprise CRM — Solution Visuals

Professional, enterprise-grade architecture and requirement-realization visuals for the
QICIRCO (Qatar General Insurance & Reinsurance Company) CRM implementation technical proposal,
covering two independently engineered options: **Microsoft Dynamics 365** and **Salesforce**.

Every visual is tailored to the QICIRCO RFP, BRD and Technical Proposal — not generic CRM art.
Each requirement is shown as a realistic product screen (with QICIRCO insurance data: QID,
policy numbers, Azentio, WhatsApp/WABA, SkipCash, 3CX, Insursa portals) annotated to show how
the platform delivers it.

> Note: the client brief refers to the company as **QICIRCO**; the source documents name it
> **QGIRCO (Qatar General Insurance & Reinsurance Company)**. Visuals use QICIRCO per the brief.

## How to view

Open `index.html` in a browser for the side-by-side gallery, or browse `png/` (high-res, 3520×2200)
and `svg/` (vector, editable) directly. Regenerate with `python3 build/cards.py all &&
python3 build/diagrams.py all && python3 build/render.py`.

## Architecture & process diagrams

| # | Diagram | Microsoft | Salesforce |
|---|---------|-----------|------------|
| — | Enterprise Solution Architecture | `png/ms-01-architecture.png` | `png/sf-01-architecture.png` |
| — | Integration & Data Flow | `png/ms-02-integration.png` | `png/sf-02-integration.png` |
| — | Case Lifecycle · SLA & Escalation | `png/ms-03-process.png` | `png/sf-03-process.png` |
| — | Functional Capability Map | `png/ms-04-capability-map.png` | `png/sf-04-capability-map.png` |
| — | Implementation Roadmap & Phasing | `png/ms-05-roadmap.png` | `png/sf-05-roadmap.png` |

## Requirement → realized in product

| Ref | Requirement | Sources | Microsoft | Salesforce |
|-----|-------------|---------|-----------|------------|
| FR-1 | Customer 360 & Unified Customer Search | RFP §5.1; BRD §7.1 / §10.1; Proposal FR-1 | `png/ms-r1-customer360.png` | `png/sf-r1-customer360.png` |
| FR-2 | Structured Interaction Logging & Audit Trail | RFP §5.1; BRD §7.2 / §11.7; Proposal FR-2 | `png/ms-r2-interaction-log.png` | `png/sf-r2-interaction-log.png` |
| FR-3 | Ticket & Incident Case Management | RFP §5.2; BRD §7.3 / §11.1; Proposal FR-3 | `png/ms-r3-ticket-incident.png` | `png/sf-r3-ticket-incident.png` |
| FR-5 | SLA Timers, Reminders & Multi-level Escalation | RFP §5.3 / §10.3; BRD §11.3 / §13; Proposal FR-5 | `png/ms-r4-sla-escalation.png` | `png/sf-r4-sla-escalation.png` |
| FR-6 | Omnichannel Engagement — One Agent Workspace | RFP §5.4; BRD §7.6 / §9.4; Proposal FR-6 | `png/ms-r5-omnichannel.png` | `png/sf-r5-omnichannel.png` |
| FR-4 | Departmental Routing, Queues & Ownership | RFP §5.2 / §10.1; BRD §11.2 / §11.5; Proposal FR-4 | `png/ms-r6-routing-queues.png` | `png/sf-r6-routing-queues.png` |
| FR-7 | Sales — Lead, Opportunity & Account Management | RFP §5.5; BRD §7.5 / §3.5; Proposal FR-7 | `png/ms-r7-sales-pipeline.png` | `png/sf-r7-sales-pipeline.png` |
| FR-8 | Real-time Dashboards, KPIs & Management Reporting | RFP §5.6 / §10.2; BRD §12 / §13; Proposal FR-8 | `png/ms-r8-dashboards-kpi.png` | `png/sf-r8-dashboards-kpi.png` |
| FR-9 | Enterprise Integration — API-led, Monitored | RFP §7; BRD §9 / §16.3; Proposal FR-9 | `png/ms-r9-integration.png` | `png/sf-r9-integration.png` |
| NFR-3 | Security, RBAC, Encryption & Compliance | RFP §6; BRD §8.2 / §14 / §15; Proposal NFR-3/4 | `png/ms-r10-security-rbac.png` | `png/sf-r10-security-rbac.png` |
| FR-Cfg | Configuration & Low-code Workflow | RFP §6; BRD §4.1 / §11.2; Proposal — configuration over code | `png/ms-r11-config-lowcode.png` | `png/sf-r11-config-lowcode.png` |
| AI | Governed AI Assistance for Service & Sales | RFP §17 (future); BRD §13.5 / §16.5; Proposal §04 AI | `png/ms-r12-ai-assist.png` | `png/sf-r12-ai-assist.png` |
| FR-Ntf | Notifications & Follow-up Management | RFP §5.3; BRD §11.6 / §7.7; Proposal — automation | `png/ms-r13-notifications.png` | `png/sf-r13-notifications.png` |
| NFR-Usab | Responsive Web & Mobile Access | RFP §6; BRD §8.3 / §17.3; Proposal NFR — usability | `png/ms-r14-mobile.png` | `png/sf-r14-mobile.png` |
| FR-KB | Knowledge Management & Self-service Deflection | RFP §5.2; BRD §17.2 / §3.1; Proposal — knowledge & FCR | `png/ms-r15-knowledge.png` | `png/sf-r15-knowledge.png` |
| FR-Cmp | Complaints Management & Regulatory Handling | RFP §5.2 / §15; BRD §11.5 / §2.3; Proposal — Complaints dept. | `png/ms-r16-complaints.png` | `png/sf-r16-complaints.png` |
| FR-Exec | Executive & Management Reporting | RFP §10.2; BRD §12.2 / §13.3; Proposal — management visibility | `png/ms-r17-executive.png` | `png/sf-r17-executive.png` |

## Layout

- `build/` — Python generators (`kit.py`, `appkit.py`, `cards.py`, `diagrams.py`, `render.py`, `gallery.py`)
- `svg/` — editable vector source (36 files)
- `png/` — high-resolution renders for direct proposal inclusion (36 files)
- `index.html` — side-by-side review gallery
