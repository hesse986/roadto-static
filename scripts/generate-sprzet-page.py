from pathlib import Path
from html import escape
from datetime import datetime
import shutil

ROOT = Path.cwd()
TEXT_FILE = ROOT / "extracted-text" / "sprzet.txt"
TARGET = ROOT / "site" / "kilimandzaro" / "sprzet" / "index.html"

if not TEXT_FILE.exists():
    raise SystemExit("Brak pliku extracted-text/sprzet.txt")

main_links = [
    ("/kilimandzaro/trasy/", "Trasy"),
    ("/kilimandzaro/sprzet/", "Sprzęt"),
    ("/kilimandzaro/dieta/", "Dieta"),
    ("/kilimandzaro/logistyka/", "Logistyka"),
    ("/kilimandzaro/zdrowie/", "Zdrowie"),
    ("/kilimandzaro/oddychanie/", "Oddychanie"),
    ("/kilimandzaro/safari-atrakcje/", "Safari i atrakcje"),
    ("/kilimandzaro/trening/", "Trening"),
]

def clean_lines(text):
    lines = []
    previous = None

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue

        if line in {"ROADTO", "roadto.pl", "www.roadto.pl"}:
            continue

        if line == previous:
            continue

        previous = line
        lines.append(line)

    return lines

def line_to_html(line, index):
    safe = escape(line)

    if index > 0 and len(line) <= 90 and not line.endswith((".", ",", ";", ":")):
        return f"<h2>{safe}</h2>"

    return f"<p>{safe}</p>"

def render(lines):
    nav = "\n".join(
        f'<a href="{href}">{escape(label)}</a>'
        for href, label in main_links
    )

    body = "\n".join(line_to_html(line, i) for i, line in enumerate(lines))

    return f"""<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sprzęt — ROADTO Kilimandżaro</title>
  <meta name="description" content="Sprzęt i pakowanie na Kilimandżaro.">
  <style>
    :root {{
      --bg: #f5f1e8;
      --card: #ffffff;
      --text: #1f1f1f;
      --muted: #68645c;
      --border: #ded6c7;
      --accent: #2f5d50;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.65;
    }}

    header {{
      padding: 28px 20px 18px;
      border-bottom: 1px solid var(--border);
      background: #fffaf0;
    }}

    .wrap {{
      max-width: 980px;
      margin: 0 auto;
    }}

    .brand {{
      font-weight: 800;
      letter-spacing: .04em;
      margin-bottom: 18px;
    }}

    nav {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}

    nav a {{
      color: var(--accent);
      text-decoration: none;
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 7px 12px;
      background: white;
      font-size: 14px;
    }}

    main {{
      padding: 34px 20px 60px;
    }}

    article {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 30px;
      box-shadow: 0 12px 40px rgba(0,0,0,.04);
    }}

    .breadcrumb {{
      margin-bottom: 20px;
      color: var(--muted);
      font-size: 14px;
    }}

    .breadcrumb a {{
      color: var(--accent);
      text-decoration: none;
    }}

    h1 {{
      margin: 0 0 14px;
      font-size: clamp(34px, 6vw, 58px);
      line-height: 1.05;
      letter-spacing: -0.04em;
    }}

    .lead {{
      color: var(--muted);
      font-size: 18px;
      margin-bottom: 30px;
    }}

    h2 {{
      margin-top: 34px;
      margin-bottom: 10px;
      font-size: 26px;
      line-height: 1.2;
      letter-spacing: -0.02em;
    }}

    p {{
      margin: 0 0 16px;
      font-size: 17px;
    }}

    footer {{
      padding: 30px 20px;
      border-top: 1px solid var(--border);
      color: var(--muted);
      font-size: 14px;
    }}

    @media (max-width: 640px) {{
      article {{
        padding: 22px;
        border-radius: 18px;
      }}

      nav a {{
        font-size: 13px;
      }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <div class="brand">ROADTO.PL</div>
      <nav aria-label="Główna nawigacja">
        {nav}
      </nav>
    </div>
  </header>

  <main>
    <div class="wrap">
      <article>
        <div class="breadcrumb">
          <a href="/kilimandzaro/trasy/">Kilimandżaro</a> / Sprzęt
        </div>

        <h1>Sprzęt</h1>
        <div class="lead">Sprzęt i pakowanie na Kilimandżaro.</div>

        {body}
      </article>
    </div>
  </main>

  <footer>
    <div class="wrap">
      ROADTO.PL — Kilimandżaro
    </div>
  </footer>
</body>
</html>
"""

text = TEXT_FILE.read_text(encoding="utf-8", errors="ignore")
lines = clean_lines(text)

if not lines:
    raise SystemExit("Plik extracted-text/sprzet.txt jest pusty po oczyszczeniu")

if TARGET.exists():
    backup = ROOT / "backups" / f"sprzet-{datetime.now().strftime('%Y%m%d-%H%M%S')}" / "index.html"
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(TARGET, backup)
    print("Zrobiono backup istniejącej strony:", backup)

TARGET.parent.mkdir(parents=True, exist_ok=True)
TARGET.write_text(render(lines), encoding="utf-8")

print("Gotowe:")
print("-", TARGET.relative_to(ROOT))
