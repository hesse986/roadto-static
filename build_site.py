#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RoadTo static-site builder.

Rebuilds the Kilimandżaro section into one consistent, branded system:
  * sticky nav with logo  * full-bleed hero per section
  * cleaned, structured content (de-duplicated, numbered accordions / bullets)
  * image cards on hub pages  * map switcher on Trasy
  * shared footer (photo strip + contact)

Content is recovered from the existing generated pages in site/ (which hold
the full text extracted from Framer). The script de-duplicates the doubled
lines, drops footer/nav boilerplate, and re-renders with the new template.
"""

import re
import html as html_mod
from pathlib import Path

from sprzet_data import INTRO as SPRZET_INTRO, CHECKLIST_PDF, SPRZET_SECTIONS
from safari_data import SAFARI_INTRO, SAFARI_ATTRACTIONS
from zdrowie_data import (ZDROWIE_INTRO, SZCZEPIENIA_INTRO, VACCINES, PRAKTYCZNE,
                          APTECZKA_INTRO, PORADNIK_INTRO, APTECZKA_PDF, PORADNIK_PDF)
from trasy_data import ROUTES as TRASY_CONTENT

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
SRC = ROOT / "src_pages"          # pristine originals (decoupled from output)
IMG = "/assets/images/framer"

# --------------------------------------------------------------------------- #
#  Configuration
# --------------------------------------------------------------------------- #

# main sections, in nav + landing order
SECTIONS = [
    ("trasy",           "Trasy",             f"{IMG}/N8r3L6juAZsihso94JAF3tsgkuY.jpg",
        "Warianty wejścia: Machame, Marangu, Lemosho i pozostałe trasy."),
    ("trening",         "Trening",           f"{IMG}/ptt1MbUgNPHImTFg0hHE1hSa1eA.jpg",
        "Wydolność, siła i regeneracja — jak przygotować ciało do wyprawy."),
    ("dieta",           "Dieta",             f"{IMG}/H0PBmA3u828lCjParlI7uB0qzdc.jpg",
        "Energia, nawodnienie i elektrolity przed wyjazdem i w górach."),
    ("zdrowie",         "Zdrowie",           f"{IMG}/R1LUoxtFgShPAKFDTJXbUYAUk.jpg",
        "Wysokość, aklimatyzacja i bezpieczeństwo na szlaku."),
    ("oddychanie",      "Oddychanie",        f"{IMG}/6uTG5GAXs3pYhPjUayKYtk1OqX8.jpg",
        "Techniki oddechowe na szlak — i na co dzień."),
    ("sprzet",          "Sprzęt",            f"{IMG}/fytbLmLZUxa0J5Ki5kxiopTog.jpg",
        "Co spakować i jak przygotować ekwipunek na Kilimandżaro."),
    ("safari-atrakcje", "Safari i atrakcje", f"{IMG}/JaRO5dK2imchTtLi1gO4U6411o.jpg",
        "Co zobaczyć w Tanzanii po zejściu z góry."),
    # „Logistyka" ukryta z nawigacji/landingu na życzenie (strona pusta).
    # URL /kilimandzaro/logistyka/ nadal się generuje (gdyby prowadził do niego kod QR).
]

HOME_HERO = f"{IMG}/U1TVwvGpfYQZaWxhY1aL5ZumEg.jpg"
KILI_HERO = f"{IMG}/ql6eidHyNj0Dirq3cHNYkDZIsC8.jpg"

# Logistyka — strona UKRYTA z nav/stopki/kafelków (poza SECTIONS), ale żywa pod URL
# (np. dla kodu QR). Ma własny przycisk PDF (checklista). Edytuj link tutaj.
LOGISTYKA_PDF = "https://drive.google.com/file/d/1fAYKOABLi14s1Ha8yBfh7focra7c-1ic/view"
LOGISTYKA_INTRO = (
    "Każda wyprawa zaczyna się dużo wcześniej niż na szlaku. To godziny planowania, "
    "kompletowania sprzętu, załatwiania formalności i dbania o szczegóły, które później "
    "pozwalają w pełni cieszyć się drogą na szczyt. Z doświadczenia wiemy, że im lepiej "
    "przygotowana logistyka, tym mniej stresu w ostatnich dniach przed wyjazdem. Dlatego "
    "stworzyliśmy checklistę – prostą listę kroków do odhaczenia, która pomoże Ci upewnić "
    "się, że masz wszystko pod kontrolą. Pobierz ją i potraktuj jako swojego asystenta w "
    "drodze do mistrzowskiego przygotowania."
)

# title / hero / description / source for each page; "kind" = leaf | hub
PAGES = {
    "kilimandzaro/dieta":      dict(title="Dieta", hero=f"{IMG}/H0PBmA3u828lCjParlI7uB0qzdc.jpg", kind="leaf", parent=("Kilimandżaro", "/kilimandzaro/")),
    "kilimandzaro/zdrowie":    dict(title="Zdrowie", hero=f"{IMG}/R1LUoxtFgShPAKFDTJXbUYAUk.jpg", kind="leaf", parent=("Kilimandżaro", "/kilimandzaro/")),
    "kilimandzaro/oddychanie": dict(title="Oddychanie", hero=f"{IMG}/6uTG5GAXs3pYhPjUayKYtk1OqX8.jpg", kind="leaf", parent=("Kilimandżaro", "/kilimandzaro/")),
    "kilimandzaro/sprzet":     dict(title="Sprzęt", hero=f"{IMG}/fytbLmLZUxa0J5Ki5kxiopTog.jpg", kind="leaf", parent=("Kilimandżaro", "/kilimandzaro/")),
    "kilimandzaro/logistyka":  dict(title="Logistyka", hero=f"{IMG}/fAOAXfHCeMpDiLn9f2Aqhivwc.jpg", kind="leaf", parent=("Kilimandżaro", "/kilimandzaro/")),
    "kilimandzaro/safari-atrakcje": dict(title="Safari i atrakcje", hero=f"{IMG}/JaRO5dK2imchTtLi1gO4U6411o.jpg", kind="leaf", parent=("Kilimandżaro", "/kilimandzaro/")),

    "kilimandzaro/trening": dict(
        title="Trening", hero=f"{IMG}/ptt1MbUgNPHImTFg0hHE1hSa1eA.jpg", kind="hub",
        parent=("Kilimandżaro", "/kilimandzaro/"),
        children=[
            ("Trening wydolnościowy", "/kilimandzaro/trening/wydolnosciowy/", "Serce, płuca i baza tlenowa.", f"{IMG}/WZ6tlnrd8xNMH2I5zl26dv1xRg.jpg"),
            ("Trening oporowy",       "/kilimandzaro/trening/oporowy/",       "Siła nóg, pleców i tułowia.", f"{IMG}/luNxOWwpbFhvfKuIy3kkUVInMY.jpg"),
            ("Regeneracja",           "/kilimandzaro/trening/regeneracja/",   "Odpoczynek, który buduje formę.", f"{IMG}/fytbLmLZUxa0J5Ki5kxiopTog.jpg"),
        ]),
    "kilimandzaro/trening/regeneracja": dict(title="Regeneracja", hero=f"{IMG}/fytbLmLZUxa0J5Ki5kxiopTog.jpg", kind="leaf", parent=("Trening", "/kilimandzaro/trening/")),

    "kilimandzaro/trening/wydolnosciowy": dict(
        title="Trening wydolnościowy", hero=f"{IMG}/WZ6tlnrd8xNMH2I5zl26dv1xRg.jpg", kind="hub",
        parent=("Trening", "/kilimandzaro/trening/"),
        children=[
            ("Strefy tętna",                "/kilimandzaro/trening/wydolnosciowy/strefy-tetna/",        "Jak czytać i trenować w strefach.", f"{IMG}/ptt1MbUgNPHImTFg0hHE1hSa1eA.jpg"),
            ("Czynniki wpływające",         "/kilimandzaro/trening/wydolnosciowy/czynniki-wplywajace/", "Co realnie podnosi wydolność.", f"{IMG}/WZ6tlnrd8xNMH2I5zl26dv1xRg.jpg"),
        ]),
    "kilimandzaro/trening/wydolnosciowy/strefy-tetna":        dict(title="Strefy tętna", hero=f"{IMG}/ptt1MbUgNPHImTFg0hHE1hSa1eA.jpg", kind="leaf", parent=("Trening wydolnościowy", "/kilimandzaro/trening/wydolnosciowy/")),
    "kilimandzaro/trening/wydolnosciowy/czynniki-wplywajace": dict(title="Czynniki wpływające na wydolność", hero=f"{IMG}/WZ6tlnrd8xNMH2I5zl26dv1xRg.jpg", kind="leaf", parent=("Trening wydolnościowy", "/kilimandzaro/trening/wydolnosciowy/")),

    "kilimandzaro/trening/oporowy": dict(
        title="Trening oporowy", hero=f"{IMG}/luNxOWwpbFhvfKuIy3kkUVInMY.jpg", kind="hub",
        parent=("Trening", "/kilimandzaro/trening/"),
        # Przycisk PDF (link Google Drive). Etykietę zmień tutaj, jeśli w oryginale była inna.
        pdf=("Plan treningu oporowego do pobrania",
             "https://drive.google.com/file/d/1W4VATzz3GqzsiDaGhqxJ2HZplA3OrYB0/view"),
        children=[
            ("Core",            "/kilimandzaro/trening/oporowy/core/",          "Brzuch i stabilny tułów.", f"{IMG}/ptt1MbUgNPHImTFg0hHE1hSa1eA.jpg"),
            ("Nogi i pośladki", "/kilimandzaro/trening/oporowy/nogi-posladki/", "Motor podejść i zejść.", f"{IMG}/WZ6tlnrd8xNMH2I5zl26dv1xRg.jpg"),
            ("Plecy i barki",   "/kilimandzaro/trening/oporowy/plecy-barki/",   "Nośność pod plecakiem.", f"{IMG}/luNxOWwpbFhvfKuIy3kkUVInMY.jpg"),
            ("Stabilizacja",    "/kilimandzaro/trening/oporowy/stabilizacja/",  "Kontrola i równowaga.", f"{IMG}/fytbLmLZUxa0J5Ki5kxiopTog.jpg"),
        ]),
    "kilimandzaro/trening/oporowy/core":          dict(title="Core", hero=f"{IMG}/ptt1MbUgNPHImTFg0hHE1hSa1eA.jpg", kind="leaf", parent=("Trening oporowy", "/kilimandzaro/trening/oporowy/")),
    "kilimandzaro/trening/oporowy/nogi-posladki": dict(title="Nogi i pośladki", hero=f"{IMG}/WZ6tlnrd8xNMH2I5zl26dv1xRg.jpg", kind="leaf", parent=("Trening oporowy", "/kilimandzaro/trening/oporowy/")),
    "kilimandzaro/trening/oporowy/plecy-barki":   dict(title="Plecy i barki", hero=f"{IMG}/luNxOWwpbFhvfKuIy3kkUVInMY.jpg", kind="leaf", parent=("Trening oporowy", "/kilimandzaro/trening/oporowy/")),
    "kilimandzaro/trening/oporowy/stabilizacja":  dict(title="Stabilizacja", hero=f"{IMG}/fytbLmLZUxa0J5Ki5kxiopTog.jpg", kind="leaf", parent=("Trening oporowy", "/kilimandzaro/trening/oporowy/")),
}

# footer photo strip
GALLERY = [
    "MBWb0PBM0bBPV0K2zcCZ0Efk.webp", "ATMgLLEDmsKumMryHPX4Az1uRE.jpg",
    "3JsqVojLMZvjjHN4RdxnfDyOk.jpg", "wvOkb9IWYynqK8AHtxtJlFG5iE.jpg",
    "fAOAXfHCeMpDiLn9f2Aqhivwc.jpg", "mQa2fWmZlSW5KGFFrjWH6DwkZr4.jpg",
    "iAvOqWBB1x9zr56DMQdud18VfI.jpg", "Z1AfcFhS4QQCDkcqjA2Zi6UoBc8.jpg",
    "JaRO5dK2imchTtLi1gO4U6411o.jpg", "4BF4YITDaUJIgSuGEiqvxx6el4.jpg",
    "1oH7wrwEGEAMmqAOlgrHIhCgZms.jpg", "ozZMW0JD5KZWeVRSLsmupXzICk.jpg",
]

LOGO = f"{IMG}/1QZodsXygocZljYBuQ3tYv94OA.svg"
INSTAGRAM = "https://www.instagram.com/roadto_7c/"
EMAIL = "7c.road@gmail.com"

# --------------------------------------------------------------------------- #
#  Content extraction
# --------------------------------------------------------------------------- #

FOOTER_MARKERS = (
    "masz pytania dotyczące naszych podróży",
    "śmiało napisz do nas",
    "copyright",
)
DROP_EXACT = {
    "wyślij", "instagram", "facebook", "road_to", EMAIL,
    "trasy", "safari, atrakcje", "trening", "oddech", "sprzęt",
    "zdrowie", "logistyka", "dieta", "kilimandżaro",
}


def extract_items(page_path: Path):
    """Return cleaned, ordered (tag, text) list from a generated page."""
    raw = page_path.read_text(encoding="utf-8", errors="ignore")
    raw = re.sub(r"<style>.*?</style>", "", raw, flags=re.DOTALL)
    m = re.search(r"<main\b[^>]*>(.*?)</main>", raw, flags=re.DOTALL)
    body = m.group(1) if m else raw

    pairs = re.findall(r"<(h1|h2|h3|h4|p)\b[^>]*>(.*?)</\1>", body, flags=re.DOTALL)
    items = []
    for tag, txt in pairs:
        t = html_mod.unescape(re.sub(r"<[^>]+>", "", txt))
        t = t.replace("\xa0", " ").strip()
        if not t:
            continue
        items.append((tag, t))

    # cut footer/contact tail
    cut = len(items)
    for i, (_, t) in enumerate(items):
        low = t.lower()
        if any(mk in low for mk in FOOTER_MARKERS):
            cut = i
            break
    items = items[:cut]

    cleaned = []
    for tag, t in items:
        low = t.lower()
        if low in DROP_EXACT:
            continue
        if "| ro" in low and len(t) > 30:        # leaked <title> meta
            continue
        if "@gmail.com" in low:
            continue
        if cleaned and cleaned[-1][1] == t:      # collapse Framer double-render
            continue
        cleaned.append((tag, t))
    # drop a leading h1 (it repeats the page title we set ourselves)
    if cleaned and cleaned[0][0] == "h1":
        cleaned = cleaned[1:]
    return cleaned


NUM_INLINE = re.compile(r"^(\d{1,2})[.)]\s+(.{3,})$")


def is_standalone_number(t: str) -> bool:
    return t.isdigit() and 1 <= int(t) <= 29


def parse_structure(items):
    """Split items into lead paragraphs + a list of chapters.
    Each chapter: dict(num, title, blocks=[(tag,text)...])."""
    lead, chapters, cur, pending_num = [], [], None, None
    for tag, t in items:
        if is_standalone_number(t):
            pending_num = int(t)
            continue
        if pending_num is not None:
            cur = dict(num=pending_num, title=t, blocks=[])
            chapters.append(cur)
            pending_num = None
            continue
        mi = NUM_INLINE.match(t) if tag in ("h2", "h3") else None
        if mi:
            cur = dict(num=int(mi.group(1)), title=mi.group(2).strip(), blocks=[])
            chapters.append(cur)
            continue
        if tag == "h2":
            cur = dict(num=None, title=t, blocks=[])
            chapters.append(cur)
            continue
        if cur is None:
            lead.append(t)
        else:
            cur["blocks"].append((tag, t))
    return lead, chapters


def render_flow(items):
    """Lossless flowing-article render: h2 -> section head, h3 -> sub-head,
    paragraphs -> text with short consecutive lines grouped into bullets."""
    out, bul = [], []

    def flush():
        nonlocal bul
        if not bul:
            return
        if len(bul) >= 2:
            out.append("<ul>" + "".join(f"<li>{esc(x)}</li>" for x in bul) + "</ul>")
        else:
            out.append(f"<p>{esc(bul[0])}</p>")
        bul = []

    for tag, t in items:
        if tag == "h2":
            flush()
            out.append(f'<h2 class="flow-h2">{esc(t)}</h2>')
        elif tag in ("h3", "h4"):
            flush()
            out.append(f"<h3>{esc(t)}</h3>")
        else:
            if t.endswith(":") and len(t) <= 170:
                flush()
                out.append(f'<p class="list-label">{esc(t)}</p>')
            elif len(t) <= 160:
                bul.append(t)
            else:
                flush()
                out.append(f"<p>{esc(t)}</p>")
    flush()
    return "\n".join(out)


def render_blocks(blocks):
    """Render a chapter body: h3 sub-heads + paragraphs, grouping short
    consecutive lines into bullet lists."""
    out, bul = [], []

    def flush():
        nonlocal bul
        if not bul:
            return
        if len(bul) >= 2:
            lis = "".join(f"<li>{esc(x)}</li>" for x in bul)
            out.append(f"<ul>{lis}</ul>")
        else:
            out.append(f"<p>{esc(bul[0])}</p>")
        bul = []

    for tag, t in blocks:
        if tag in ("h3", "h4"):
            flush()
            out.append(f"<h3>{esc(t)}</h3>")
            continue
        # paragraph
        if t.endswith(":") and len(t) <= 170:
            flush()
            out.append(f'<p class="list-label">{esc(t)}</p>')
            continue
        if len(t) <= 160:
            bul.append(t)
        else:
            flush()
            out.append(f"<p>{esc(t)}</p>")
    flush()
    return "\n".join(out)


# --------------------------------------------------------------------------- #
#  HTML templates
# --------------------------------------------------------------------------- #

def esc(s: str) -> str:
    return html_mod.escape(s, quote=False)


def head(title, desc, body_class=""):
    bc = f' class="{body_class}"' if body_class else ""
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — RoadTo Kilimandżaro</title>
<meta name="description" content="{esc(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body{bc}>
"""


def nav(current=""):
    links = ""
    for slug, label, _, _ in SECTIONS:
        cur = " is-current" if slug == current else ""
        links += f'<a class="{cur.strip()}" href="/kilimandzaro/{slug}/">{esc(label)}</a>'
    return f"""<header class="nav">
  <div class="nav__inner">
    <a class="brand" href="/kilimandzaro/">
      <img class="brand__mark" src="{LOGO}" alt="">
      <span class="brand__name">Road<b>To</b></span>
    </a>
    <nav class="nav__links" aria-label="Sekcje Kilimandżaro">
      {links}
    </nav>
  </div>
</header>
"""


CHEV = ('<svg class="chapter__chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="m6 9 6 6 6-6"/></svg>')
ARROW = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')


def hero(title, desc, hero_img, crumbs_html="", extra="", cls=""):
    return f"""<section class="hero {cls}">
  <div class="hero__media"><img src="{hero_img}" alt=""></div>
  <div class="hero__inner">
    {crumbs_html}
    <p class="eyebrow">RoadTo · Kilimandżaro</p>
    <h1>{esc(title)}</h1>
    {f'<p class="hero__lead">{esc(desc)}</p>' if desc else ''}
    {extra}
  </div>
</section>
"""


def crumbs(parent):
    if not parent:
        return ""
    label, href = parent
    return (f'<p class="crumbs"><a href="/kilimandzaro/">Kilimandżaro</a>'
            f'{"" if href == "/kilimandzaro/" else f" / <a href=\"{href}\">{esc(label)}</a>"}'
            f'</p>')


def footer():
    gal = "".join(
        f'<a href="{INSTAGRAM}" target="_blank" rel="noopener"><img src="{IMG}/{f}" alt="" loading="lazy"></a>'
        for f in GALLERY
    )
    sec_links = "".join(
        f'<a href="/kilimandzaro/{slug}/">{esc(label)}</a>' for slug, label, _, _ in SECTIONS
    )
    return f"""<footer class="footer">
  <div class="footer__top">
    <div>
      <h2>Masz pytania o wyprawę?</h2>
      <p>Planujesz wejście na Kilimandżaro albo masz pomysł na wspólny projekt? Śmiało napisz do nas.</p>
      <div class="footer__contacts">
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram — @roadto_7c</a>
      </div>
      <a class="btn btn--gold" href="mailto:{EMAIL}">Napisz do nas {ARROW}</a>
    </div>
    <div class="footer__gallery">{gal}</div>
  </div>
  <div class="footer__bar">
    <span>© 2025 RoadTo · Kilimandżaro</span>
    <nav>{sec_links}</nav>
  </div>
</footer>
</body>
</html>
"""


# --------------------------------------------------------------------------- #
#  Page builders
# --------------------------------------------------------------------------- #

def write(rel_path: str, html: str):
    out = SITE / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return rel_path


def build_leaf(slug, cfg):
    src = SRC / slug / "index.html"
    items = extract_items(src) if src.exists() else []
    lead, chapters = parse_structure(items)

    # Pages without a clear chapter structure -> lossless flowing article.
    if len([c for c in chapters if render_blocks(c["blocks"]).strip()]) < 2:
        flow = render_flow(items)
        if not flow.strip():
            flow = f'<p>{esc(cfg.get("desc") or "Treść w przygotowaniu.")}</p>'
        desc = cfg.get("desc") or (lead[0][:155] if lead else cfg["title"])
        html = (
            head(cfg["title"], desc)
            + nav(cfg.get("nav_current", ""))
            + hero(cfg["title"], "", cfg["hero"], crumbs_html=crumbs(cfg.get("parent")))
            + f'<main class="content"><div class="content__col">'
              f'<div class="section-body prose-card">{flow}</div></div></main>'
            + footer()
        )
        return write(slug + "/index.html", html)

    # lead block
    lead_html = ""
    if lead:
        ps = "".join(f"<p>{esc(p)}</p>" for p in lead[:5])
        lead_html = f'<div class="lead-block">{ps}</div>'

    # merge consecutive chapters that share a title (drop the empty header dup)
    merged = []
    for c in chapters:
        if merged and merged[-1]["title"] == c["title"]:
            merged[-1]["blocks"].extend(c["blocks"])
            if merged[-1]["num"] is None:
                merged[-1]["num"] = c["num"]
            continue
        merged.append(c)
    chapters = merged

    # chapters: empty ones become section dividers, the rest accordions
    body_parts, first_open_used = [], False
    for c in chapters:
        inner = render_blocks(c["blocks"])
        if not inner.strip():
            body_parts.append(f'<h2 class="divider">{esc(c["title"])}</h2>')
            continue
        if c["num"] is not None:
            badge = f'<span class="chapter__num">{c["num"]}</span>'
        else:
            badge = '<span class="chapter__num chapter__num--glyph">▲</span>'
        open_attr = "" if first_open_used else " open"
        first_open_used = True
        body_parts.append(
            f'<details class="chapter"{open_attr}>'
            f'<summary>{badge}'
            f'<span class="chapter__title">{esc(c["title"])}</span>{CHEV}</summary>'
            f'<div class="chapter__body">{inner}</div></details>'
        )
    chapters_html = "\n".join(body_parts)
    if not chapters_html and not lead_html:
        chapters_html = f'<div class="lead-block"><p>{esc(cfg["desc"]) if cfg.get("desc") else "Treść w przygotowaniu."}</p></div>'

    desc = cfg.get("desc") or (lead[0][:155] if lead else f'{cfg["title"]} — RoadTo Kilimandżaro.')
    html = (
        head(cfg["title"], desc)
        + nav(cfg.get("nav_current", ""))
        + hero(cfg["title"], "", cfg["hero"], crumbs_html=crumbs(cfg.get("parent")))
        + f'<main class="content"><div class="content__col">{lead_html}{chapters_html}</div></main>'
        + footer()
    )
    return write(slug + "/index.html", html)


def build_hub(slug, cfg):
    src = SRC / slug / "index.html"
    items = extract_items(src) if src.exists() else []
    lead, _ = parse_structure(items)
    intro = "".join(f"<p>{esc(p)}</p>" for p in lead[:3]) if lead else ""

    cards = ""
    for label, href, blurb, img in cfg["children"]:
        cards += f"""<a class="card-link" href="{href}">
      <div class="card-link__media"><img src="{img}" alt="" loading="lazy"></div>
      <div class="card-link__body">
        <h3>{esc(label)}</h3>
        <p>{esc(blurb)}</p>
        <span class="card-link__more">Zobacz {ARROW}</span>
      </div>
    </a>"""

    desc = cfg.get("desc") or (lead[0][:155] if lead else cfg["title"])
    intro_html = f'<section class="section-intro">{intro}</section>' if intro else ""

    pdf_html = ""
    pdf = cfg.get("pdf")
    if pdf and pdf[1] and pdf[1] != "#":
        label, link = pdf
        pdf_html = (f'<div class="lead-block" style="text-align:center">'
                    f'<a class="btn btn--gold" href="{link}" target="_blank" '
                    f'rel="noopener">{esc(label)} (PDF) {ARROW}</a></div>')

    html = (
        head(cfg["title"], desc)
        + nav(cfg.get("nav_current", ""))
        + hero(cfg["title"], cfg.get("desc", ""), cfg["hero"], crumbs_html=crumbs(cfg.get("parent")))
        + f'<main class="wrap">{intro_html}<div class="cards">{cards}</div>{pdf_html}</main>'
        + footer()
    )
    return write(slug + "/index.html", html)


def build_landing():
    cards = ""
    for slug, label, img, blurb in SECTIONS:
        cards += f"""<a class="card-link" href="/kilimandzaro/{slug}/">
      <div class="card-link__media"><img src="{img}" alt="" loading="lazy"></div>
      <div class="card-link__body">
        <span class="card-link__kicker">Przewodnik</span>
        <h3>{esc(label)}</h3>
        <p>{esc(blurb)}</p>
      </div>
    </a>"""
    intro = ('<section class="section-intro">'
             '<p>Wszystko, czego potrzebujesz, żeby dobrze przygotować się do wejścia na '
             'Kilimandżaro — w jednym miejscu. Wybierz dział i czytaj we własnym tempie.</p>'
             '<p>Materiały rozszerzają treści z książki <em>Road to Kilimandżaro</em> '
             'i są stale aktualizowane.</p></section>')
    html = (
        head("Kilimandżaro", "Kompletny przewodnik po Kilimandżaro: trasy, trening, dieta, sprzęt, zdrowie, logistyka i safari.", "page-kili")
        + nav("")
        + hero("Kilimandżaro", "Przewodnik po przygotowaniu do wejścia — krok po kroku.", KILI_HERO)
        + f'<main class="wrap">{intro}<div class="cards">{cards}</div></main>'
        + footer()
    )
    return write("kilimandzaro/index.html", html)


def _trasy_versions_table(content):
    """Render the 'Różnice między wersją…' comparison table (full header row)."""
    t = content.get("table")
    if not t:
        note = content.get("table_note")
        if note:
            return f'<p class="route-todo">{esc(note)}</p>'
        return ""
    cols = t["cols"]
    head_cells = "".join(f'<th scope="col">{esc(c)}</th>' for c in cols)
    body = ""
    for r in t["rows"]:
        first, rest = r[0], r[1:]
        tds = "".join(
            f'<td data-label="{esc(cols[i+1])}">{esc(v)}</td>' for i, v in enumerate(rest)
        )
        body += (f'<tr><th scope="row" data-label="{esc(cols[0])}">{esc(first)}</th>{tds}</tr>')
    cap = f'<caption>{esc(t.get("title", ""))}</caption>' if t.get("title") else ""
    return (f'<div class="gear-table-wrap route-table"><table class="gear-table">{cap}'
            f'<thead><tr>{head_cells}</tr></thead><tbody>{body}</tbody></table></div>')


def _trasy_day(day):
    stats = "".join(
        f'<div class="route-day__stat"><span class="route-day__k">{esc(k)}</span>'
        f'<span class="route-day__v">{esc(v)}</span></div>'
        for k, v in day.get("stats", [])
    )
    note = (f'<p class="route-day__note">{esc(day["note"])}</p>'
            if day.get("note") else "")
    return (
        f'<article class="route-day">'
        f'<h4 class="route-day__title">{esc(day["title"])}</h4>'
        f'<div class="route-day__stats">{stats}</div>'
        f'<p class="route-day__desc">{esc(day["desc"])}</p>'
        f'{note}</article>'
    )


def _trasy_panel(name, content, active):
    if not content:
        return ""
    meta = f'<p class="route-meta">{esc(content["meta"])}</p>' if content.get("meta") else ""
    bullets = "".join(f"<li>{esc(b)}</li>" for b in content.get("good_if", []))
    good = ""
    if bullets:
        gt = content.get("good_if_title", "Sprawdzi się, jeśli:")
        good = (f'<div class="route-goodif"><h3>{esc(gt)}</h3>'
                f'<ul class="route-goodif__list">{bullets}</ul></div>')
    partial = (f'<p class="route-todo">{esc(content["partial_note"])}</p>'
               if content.get("partial_note") else "")
    days = "".join(_trasy_day(d) for d in content.get("days", []))
    table = _trasy_versions_table(content)
    hidden = "" if active else " hidden"
    return (
        f'<section class="route-panel" data-panel="{esc(name)}"{hidden}>'
        f'<h2 class="route-panel__title">{esc(content["title"])}</h2>'
        f'{meta}{good}{partial}'
        f'<div class="route-days">{days}</div>'
        f'{table}</section>'
    )


def build_trasy():
    routes = [
        ("Machame", "Machame Route", "H1uV71HmHwcSbf2lI3IXbTOqzo.png"),
        ("Marangu", "Marangu Route", "Tj1bIDbhxHmtpFetxXPtByFRlM.png"),
        ("Lemosho", "Lemosho Route", "jaCVCkNeYXVCnHLKCkL1ggvNo.png"),
        ("Rongai", "Rongai Route", "ymoD2RIoGh4EZfvAcPibQDKUU.png"),
        ("Northern Circuit", "Northern Circuit Route", "qBLGlEWF4YERkNapDrKid0rRk.png"),
        ("Shira", "Shira Route", "zRRqdMgdrnY3UXU60b7g1LMgmI.png"),
        ("Umbwe", "Umbwe Route", "UVSTsnVy5MAQlMlGWrw1cZy9OFA.png"),
        ("Western Breach", "Western Breach Route", "we3HbvznYRvwn6ix2pJbzc1ZLA.png"),
    ]
    tabs = "".join(
        f'<button type="button" class="routes__tab{" is-active" if i == 0 else ""}" data-i="{i}">{esc(n)}</button>'
        for i, (n, _, _) in enumerate(routes)
    )
    data = ",".join(f'["{n}","{lab}","{IMG}/{f}"]' for n, lab, f in routes)
    panels = "".join(
        _trasy_panel(n, TRASY_CONTENT.get(n), i == 0) for i, (n, _, _) in enumerate(routes)
    )
    intro = ('<section class="section-intro">'
             '<p>Na Kilimandżaro prowadzi kilka tras, które różnią się długością, krajobrazem '
             'i tempem aklimatyzacji. Wybierz trasę, by zobaczyć jej przebieg na mapie i pełny opis '
             'dzień po dniu.</p></section>')
    body = f"""<main>
  {intro}
  <div class="routes">
    <div class="routes__tabs" role="tablist" aria-label="Wybór trasy">{tabs}</div>
    <figure class="routes__map">
      <img id="routeMap" src="{IMG}/{routes[0][2]}" alt="Mapa trasy Machame na Kilimandżaro">
      <figcaption class="routes__cap"><b id="routeName">Machame Route</b><span>Mapa trasy — RoadTo</span></figcaption>
    </figure>
  </div>
  <div class="content__col route-content">
    {panels}
  </div>
</main>
<script>
  const R=[{data}];
  const img=document.getElementById('routeMap'),nm=document.getElementById('routeName');
  const panels=document.querySelectorAll('.route-panel');
  document.querySelectorAll('.routes__tab').forEach(b=>b.addEventListener('click',()=>{{
    const r=R[+b.dataset.i];
    img.src=r[2]; img.alt='Mapa trasy '+r[0]+' na Kilimandżaro'; nm.textContent=r[1];
    document.querySelectorAll('.routes__tab').forEach(x=>x.classList.remove('is-active'));
    b.classList.add('is-active');
    panels.forEach(p=>{{ p.hidden = (p.dataset.panel !== r[0]); }});
  }}));
</script>
"""
    html = (
        head("Trasy", "Mapy i opisy tras wejściowych na Kilimandżaro: Machame, Marangu, Lemosho, Rongai i inne.", "page-trasy")
        + nav("trasy")
        + hero("Trasy", "Warianty wejścia na dach Afryki.", f"{IMG}/N8r3L6juAZsihso94JAF3tsgkuY.jpg",
               crumbs_html=crumbs(("Kilimandżaro", "/kilimandzaro/")))
        + body
        + footer()
    )
    return write("kilimandzaro/trasy/index.html", html)


def build_home():
    extra = """<div class="home-cta">
      <a class="btn btn--gold" href="/kilimandzaro/">Przewodnik Kilimandżaro %s</a>
      <a class="btn btn--ghost" href="/kilimandzaro/trasy/">Zobacz trasy</a>
    </div>""" % ARROW
    stats = """<section class="home-stats">
      <div class="stat"><b>420+</b><span>stron w książce</span></div>
      <div class="stat"><b>170+</b><span>zdjęć i grafik</span></div>
      <div class="stat"><b>28</b><span>kodów QR i map</span></div>
    </section>"""
    html = (
        head("RoadTo", "RoadTo — przewodnik po przygotowaniu do wejścia na Kilimandżaro.", "page-home")
        + nav("")
        + hero("Road to Kilimandżaro", "Przygotuj się do dachu Afryki — trasy, trening, dieta, sprzęt i zdrowie w jednym miejscu.",
               HOME_HERO, extra=extra, cls="home-hero")
        + stats
        + footer()
    )
    return write("index.html", html)


def build_404():
    btns = ('<div class="home-cta">'
            f'<a class="btn btn--gold" href="/kilimandzaro/">Przewodnik Kilimandżaro</a>'
            f'<a class="btn btn--ghost" href="/kilimandzaro/trasy/">Trasy</a></div>')
    html = (
        head("Nie znaleziono strony", "Ten adres nie istnieje.")
        + nav("")
        + f'<main class="notfound"><div><h1>404</h1><p>Ten adres nie istnieje albo został przeniesiony. Wróć do przewodnika.</p>{btns}</div></main>'
        + footer()
    )
    return write("404.html", html)


def build_sprzet_redirect():
    # physical /kilimandzaro/sprzęt/ -> canonical /kilimandzaro/sprzet/
    html = ("""<!doctype html><html lang="pl"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=/kilimandzaro/sprzet/">
<link rel="canonical" href="/kilimandzaro/sprzet/">
<title>Sprzęt — RoadTo</title></head>
<body><p>Przekierowanie do <a href="/kilimandzaro/sprzet/">/kilimandzaro/sprzet/</a></p></body></html>""")
    return write("kilimandzaro/sprzęt/index.html", html)


# --------------------------------------------------------------------------- #
#  Sprzęt — data-driven tables (recovered 1:1 from Framer)
# --------------------------------------------------------------------------- #

def _gear_table(caption, cols, rows):
    head_cells = "<th scope=\"col\"></th>" + "".join(
        f'<th scope="col">{esc(c)}</th>' for c in cols)
    body = ""
    for r in rows:
        name, cells = r[0], r[1:]
        tds = ""
        for col, val in zip(cols, cells):
            cls = ' class="gear-price"' if col.lower().startswith("cena") else ""
            tds += f'<td data-label="{esc(col)}"{cls}>{esc(val)}</td>'
        body += (f'<tr><th scope="row" data-label="Model">{esc(name)}</th>'
                 f'{tds}</tr>')
    cap = f"<caption>{esc(caption)}</caption>" if caption else ""
    return (f'<div class="gear-table-wrap"><table class="gear-table">{cap}'
            f'<thead><tr>{head_cells}</tr></thead><tbody>{body}</tbody>'
            f'</table></div>')


def build_logistyka(cfg):
    # Strona ukryta w menu (nie ma jej w SECTIONS), ale generowana pod URL.
    pdf_btn = ""
    if LOGISTYKA_PDF and LOGISTYKA_PDF != "#":
        pdf_btn = (f'<a class="btn btn--gold" href="{LOGISTYKA_PDF}" target="_blank" '
                   f'rel="noopener">Checklista do pobrania (PDF) {ARROW}</a>')
    lead = f'<div class="lead-block"><p>{esc(LOGISTYKA_INTRO)}</p>{pdf_btn}</div>'
    html = (
        head(cfg["title"], "Logistyka wyprawy na Kilimandżaro — checklista przygotowań do pobrania.")
        + nav(cfg.get("nav_current", ""))
        + hero(cfg["title"], "mistrzowskie przygotowanie", cfg["hero"], crumbs_html=crumbs(cfg.get("parent")))
        + f'<main class="content"><div class="content__col">{lead}</div></main>'
        + footer()
    )
    return write("kilimandzaro/logistyka/index.html", html)


def build_sprzet(cfg):
    pdf_btn = ""
    if CHECKLIST_PDF and CHECKLIST_PDF != "#":
        pdf_btn = (f'<a class="btn btn--gold" href="{CHECKLIST_PDF}" target="_blank" '
                   f'rel="noopener">Ekwipunek niezbędny na wyprawę (PDF) {ARROW}</a>')
    lead = (f'<div class="lead-block"><p>{esc(SPRZET_INTRO)}</p>{pdf_btn}</div>')

    sections_html = []
    first_open = True
    for num, title, blocks in SPRZET_SECTIONS:
        inner = []
        for blk in blocks:
            if blk[0] == "group":
                inner.append(f'<h3 class="gear-group">{esc(blk[1])}</h3>')
            else:  # table
                _, caption, cols, rows = blk
                inner.append(_gear_table(caption, cols, rows))
        open_attr = " open" if first_open else ""
        first_open = False
        sections_html.append(
            f'<details class="chapter"{open_attr}>'
            f'<summary><span class="chapter__num">{num}</span>'
            f'<span class="chapter__title">{esc(title)}</span>{CHEV}</summary>'
            f'<div class="chapter__body">{"".join(inner)}</div></details>'
        )

    html = (
        head(cfg["title"], cfg.get("desc", "Sprzęt na Kilimandżaro — sprawdzona lista ekwipunku."), "page-sprzet")
        + nav(cfg.get("nav_current", "sprzet"))
        + hero(cfg["title"], cfg.get("desc", ""), cfg["hero"], crumbs_html=crumbs(cfg.get("parent")))
        + f'<main class="content"><div class="gear">{lead}{"".join(sections_html)}</div></main>'
        + footer()
    )
    return write("kilimandzaro/sprzet/index.html", html)


# --------------------------------------------------------------------------- #
#  Safari i atrakcje — data-driven accordions (recovered 1:1 from Framer)
# --------------------------------------------------------------------------- #

def build_safari(cfg):
    intro = f'<div class="lead-block"><p>{esc(SAFARI_INTRO)}</p></div>'

    blocks, first_open = [], True
    for a in SAFARI_ATTRACTIONS:
        paras = "".join(f"<p>{esc(p)}</p>" for p in a["intro"])
        tip = (f'<div class="safari-tip"><b>Tip:</b> {esc(a["tip"])}</div>'
               if a.get("tip") else "")
        rows = "".join(f"<dt>{esc(lab)}</dt><dd>{esc(txt)}</dd>" for lab, txt in a.get("info", []))
        info = (f'<div class="safari-info"><h4>Informacje praktyczne</h4>'
                f'<dl>{rows}</dl></div>') if rows else ""
        open_attr = " open" if first_open else ""
        first_open = False
        blocks.append(
            f'<details class="chapter"{open_attr}>'
            f'<summary><span class="chapter__num chapter__num--glyph">▲</span>'
            f'<span class="chapter__title">{esc(a["title"])}</span>{CHEV}</summary>'
            f'<div class="chapter__body">{paras}{tip}{info}</div></details>'
        )

    html = (
        head(cfg["title"], cfg.get("desc", "Co zobaczyć w Tanzanii po zejściu z Kilimandżaro."), "page-safari")
        + nav(cfg.get("nav_current", "safari-atrakcje"))
        + hero(cfg["title"], cfg.get("desc", ""), cfg["hero"], crumbs_html=crumbs(cfg.get("parent")))
        + f'<main class="content"><div class="safari">{intro}{"".join(blocks)}</div></main>'
        + footer()
    )
    return write("kilimandzaro/safari-atrakcje/index.html", html)


# --------------------------------------------------------------------------- #
#  Trening — exercise pages (parsed from existing scraped content)
# --------------------------------------------------------------------------- #

BULB = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1h6c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2Z"/></svg>')

_EX_LABELS = {
    "pozycja startowa": ("Pozycja startowa", "check"),
    "ruch": ("Ruch", "arrow"),
    "najczęstsze błędy": ("Najczęstsze błędy", "x"),
    "warianty": ("Warianty", "arrow"),
}


def _ex_norm(t):
    return t.strip().lower().rstrip(":").strip()


def _split_title(pending):
    """pending = list of lines before a 'Pozycja startowa:'.
    title = last line not starting with '('; rest-after = subtitle; before = intro."""
    if not pending:
        return ("Ćwiczenie", "", [])
    title_idx = 0
    for i, x in enumerate(pending):
        if not x.strip().startswith("("):
            title_idx = i
    title = pending[title_idx]
    subtitle = " ".join(pending[title_idx + 1:]).strip()
    intro = pending[:title_idx]
    return (title, subtitle, intro)


def _parse_exercises(items):
    exercises, intro = [], []
    cur, section, pending, expect_tip = None, None, [], False
    for _, t in items:
        n = _ex_norm(t)
        if n == "pozycja startowa":
            title, subtitle, leftover = _split_title(pending)
            if not exercises:
                intro.extend(leftover)
            pending = []
            cur = dict(title=title, subtitle=subtitle, secs=[], tip="")
            exercises.append(cur)
            cur["secs"].append(["Pozycja startowa", "check", []])
            section = cur["secs"][-1][2]
            expect_tip = False
            continue
        if n in ("ruch", "najczęstsze błędy", "warianty") and cur is not None:
            label, icon = _EX_LABELS[n]
            cur["secs"].append([label, icon, []])
            section = cur["secs"][-1][2]
            expect_tip = False
            continue
        if n == "wskazówka trenera":
            expect_tip = True
            section = None
            continue
        # content line
        if expect_tip:
            if cur is not None and not cur["tip"]:
                cur["tip"] = t
            else:
                pending.append(t)
                expect_tip = False
            continue
        if section is not None:
            section.append(t)
        else:
            pending.append(t)
    return intro, exercises


def build_training_exercise(slug, cfg):
    src = SRC / slug / "index.html"
    items = extract_items(src) if src.exists() else []
    intro, exercises = _parse_exercises(items)

    lead = ""
    intro = [p for p in intro if not p.lower().startswith("ćwiczenia na")]
    if intro:
        lead = '<div class="ex-lead">' + "".join(f"<p>{esc(p)}</p>" for p in intro) + "</div>"

    blocks, first_open = [], True
    for ex in exercises:
        body = ""
        for label, icon, bullets in ex["secs"]:
            if not bullets:
                continue
            lis = "".join(f"<li>{esc(b)}</li>" for b in bullets)
            body += (f'<p class="ex-label">{esc(label)}</p>'
                     f'<ul class="ex-list ex-list--{icon}">{lis}</ul>')
        sub = f'<p class="ex-sub">{esc(ex["subtitle"])}</p>' if ex["subtitle"] else ""
        tip = ""
        if ex["tip"]:
            tip = (f'<div class="ex-tip"><p class="ex-tip__h">{BULB}'
                   f'Wskazówka trenera</p><p>{esc(ex["tip"])}</p></div>')
        open_attr = " open" if first_open else ""
        first_open = False
        blocks.append(
            f'<details class="chapter"{open_attr}>'
            f'<summary><span class="chapter__num chapter__num--glyph">▲</span>'
            f'<span class="chapter__title">{esc(ex["title"])}</span>{CHEV}</summary>'
            f'<div class="chapter__body">{sub}<div class="ex-body">{body}</div>{tip}</div>'
            f'</details>'
        )

    html = (
        head(cfg["title"], cfg.get("desc", f'{cfg["title"]} — ćwiczenia przygotowujące na Kilimandżaro.'), "page-trening")
        + nav(cfg.get("nav_current", "trening"))
        + hero(cfg["title"], cfg.get("desc", ""), cfg["hero"], crumbs_html=crumbs(cfg.get("parent")))
        + f'<main class="content"><div class="content__col">{lead}{"".join(blocks)}</div></main>'
        + footer()
    )
    return write(slug + "/index.html", html)


# --------------------------------------------------------------------------- #
#  Zdrowie — szczepienia jako rozwijane sekcje (treść odzyskana z Framera)
# --------------------------------------------------------------------------- #

def _rich(s):
    """Escape + zamień **pogrubienie** na <strong>."""
    out = ""
    for i, part in enumerate(esc(s).split("**")):
        out += f"<strong>{part}</strong>" if i % 2 == 1 else part
    return out


def _zd_block(b):
    kind = b[0]
    if kind == "h":
        return f'<h4 class="vax-q">{esc(b[1])}</h4>'
    if kind == "p":
        return f'<p>{_rich(b[1])}</p>'
    if kind == "ul":
        return "<ul>" + "".join(f"<li>{_rich(x)}</li>" for x in b[1]) + "</ul>"
    if kind == "check":
        return ('<ul class="vax-check">'
                + "".join(f"<li>{_rich(x)}</li>" for x in b[1]) + "</ul>")
    if kind == "cols":
        cards = ""
        for header, blocks in b[1]:
            inner = "".join(_zd_block(x) for x in blocks)
            cards += (f'<div class="vax-col"><div class="vax-col__h">{esc(header)}</div>'
                      f'<div class="vax-col__b">{inner}</div></div>')
        return f'<div class="vax-cols">{cards}</div>'
    if kind == "table":
        _, cap, cols, rows = b
        return _gear_table(cap, cols, rows)
    return ""


def build_zdrowie(cfg):
    lead = f'<div class="lead-block"><p>{esc(ZDROWIE_INTRO)}</p></div>'

    # Sekcja: Szczepienia
    sez = (f'<h2 class="divider">Szczepienia</h2>'
           f'<p class="section-intro">{esc(SZCZEPIENIA_INTRO)}</p>'
           f'<h3 class="vax-h3">Zalecane szczepienia</h3>')

    accordions, first_open = [], True
    for v in VACCINES:
        body = "".join(_zd_block(b) for b in v["blocks"])
        open_attr = " open" if first_open else ""
        first_open = False
        accordions.append(
            f'<details class="chapter"{open_attr}>'
            f'<summary><span class="chapter__num chapter__num--glyph chapter__num--check">✓</span>'
            f'<span class="chapter__title">{esc(v["title"])}</span>{CHEV}</summary>'
            f'<div class="chapter__body">{body}</div></details>'
        )

    # Praktyczne szczegóły
    steps = "".join(f'<li><strong>{esc(lead_)}</strong>{esc(rest)}</li>'
                    for lead_, rest in PRAKTYCZNE)
    praktyczne = (f'<h2 class="divider">Praktyczne szczegóły — jak planować szczepienia</h2>'
                  f'<ol class="vax-steps">{steps}</ol>')

    # Apteczka + poradnik (przyciski PDF, jeśli link podpięty)
    def pdf_section(title, intro, link, label):
        if link and link != "#":
            btn = (f'<a class="btn btn--gold" href="{link}" target="_blank" '
                   f'rel="noopener">{label} (PDF) {ARROW}</a>')
        else:
            btn = '<p class="pdf-todo">Plik PDF do podpięcia (link z Google Drive).</p>'
        return (f'<h2 class="divider">{esc(title)}</h2>'
                f'<div class="lead-block"><p>{esc(intro)}</p>{btn}</div>')

    apteczka = pdf_section("Apteczka wyprawowa", APTECZKA_INTRO, APTECZKA_PDF,
                           "Apteczka do pobrania")
    poradnik = pdf_section("Mini-poradnik pierwszej pomocy", PORADNIK_INTRO, PORADNIK_PDF,
                           "Poradnik do pobrania")

    html = (
        head(cfg["title"], cfg.get("desc", "Zdrowie przed wyprawą na Kilimandżaro — szczepienia, malaria, apteczka."), "page-zdrowie")
        + nav(cfg.get("nav_current", "zdrowie"))
        + hero(cfg["title"], cfg.get("desc", ""), cfg["hero"], crumbs_html=crumbs(cfg.get("parent")))
        + f'<main class="content"><div class="content__col">'
          f'{lead}{sez}{"".join(accordions)}{praktyczne}{apteczka}{poradnik}</div></main>'
        + footer()
    )
    return write("kilimandzaro/zdrowie/index.html", html)


# --------------------------------------------------------------------------- #
def main():
    built = []
    built.append(build_home())
    built.append(build_landing())
    built.append(build_trasy())
    built.append(build_404())
    built.append(build_sprzet_redirect())

    for slug, cfg in PAGES.items():
        cfg = dict(cfg)
        cfg["nav_current"] = slug.split("/")[1] if slug.startswith("kilimandzaro/") else ""
        if slug == "kilimandzaro/sprzet":
            built.append(build_sprzet(cfg))
        elif slug == "kilimandzaro/safari-atrakcje":
            built.append(build_safari(cfg))
        elif slug == "kilimandzaro/zdrowie":
            built.append(build_zdrowie(cfg))
        elif slug == "kilimandzaro/logistyka":
            built.append(build_logistyka(cfg))
        elif slug in (
            "kilimandzaro/trening/oporowy/nogi-posladki",
            "kilimandzaro/trening/oporowy/core",
            "kilimandzaro/trening/oporowy/plecy-barki",
            "kilimandzaro/trening/oporowy/stabilizacja",
        ):
            built.append(build_training_exercise(slug, cfg))
        elif cfg["kind"] == "hub":
            built.append(build_hub(slug, cfg))
        else:
            built.append(build_leaf(slug, cfg))

    print(f"Built {len(built)} pages:")
    for b in built:
        print("  ", b)


if __name__ == "__main__":
    main()
