from pathlib import Path
from html import escape
import shutil
from datetime import datetime

ROOT = Path.cwd()
TEXT_DIR = ROOT / "extracted-text"
SITE_DIR = ROOT / "site"

if not TEXT_DIR.exists():
    raise SystemExit("Brak katalogu extracted-text. Uruchom skrypt z ~/roadto-backup")

if not SITE_DIR.exists():
    raise SystemExit("Brak katalogu site. Uruchom skrypt z ~/roadto-backup")

pages = {
    "trening__regeneracja.txt": {
        "title": "Regeneracja",
        "path": "kilimandzaro/trening/regeneracja/index.html",
        "description": "Regeneracja w przygotowaniach do Kilimandżaro."
    },
    "trening__wydolnosciowy.txt": {
        "title": "Trening wydolnościowy",
        "path": "kilimandzaro/trening/wydolnosciowy/index.html",
        "description": "Trening wydolnościowy przed wejściem na Kilimandżaro."
    },
    "trening__wydolnosciowy__strefy-tetna.txt": {
        "title": "Strefy tętna",
        "path": "kilimandzaro/trening/wydolnosciowy/strefy-tetna/index.html",
        "description": "Strefy tętna w treningu wydolnościowym."
    },
    "trening__wydolnosciowy__czynniki-wplywajace.txt": {
        "title": "Czynniki wpływające na wydolność",
        "path": "kilimandzaro/trening/wydolnosciowy/czynniki-wplywajace/index.html",
        "description": "Czynniki wpływające na wydolność w przygotowaniach."
    },
    "trening__oporowy.txt": {
        "title": "Trening oporowy",
        "path": "kilimandzaro/trening/oporowy/index.html",
        "description": "Trening siłowy i oporowy przed Kilimandżaro."
    },
    "trening__oporowy__core.txt": {
        "title": "Core",
        "path": "kilimandzaro/trening/oporowy/core/index.html",
        "description": "Ćwiczenia core w przygotowaniach do trekkingu."
    },
    "trening__oporowy__nogi-posladki.txt": {
        "title": "Nogi i pośladki",
        "path": "kilimandzaro/trening/oporowy/nogi-posladki/index.html",
        "description": "Ćwiczenia na nogi i pośladki przed trekkingiem."
    },
    "trening__oporowy__plecy-barki.txt": {
        "title": "Plecy i barki",
        "path": "kilimandzaro/trening/oporowy/plecy-barki/index.html",
        "description": "Ćwiczenia na plecy i barki przed Kilimandżaro."
    },
    "trening__oporowy__stabilizacja.txt": {
        "title": "Stabilizacja",
        "path": "kilimandzaro/trening/oporowy/stabilizacja/index.html",
        "description": "Stabilizacja i kontrola ruchu w przygotowaniach."
    },
}

training_links = [
    ("/kilimandzaro/trening/", "Trening"),
    ("/kilimandzaro/trening/regeneracja/", "Regeneracja"),
    ("/kilimandzaro/trening/wydolnosciowy/", "Trening wydolnościowy"),
    ("/kilimandzaro/trening/wydolnosciowy/strefy-tetna/", "Strefy tętna"),
    ("/kilimandzaro/trening/wydolnosciowy/czynniki-wplywajace/", "Czynniki wpływające"),
    ("/kilimandzaro/trening/oporowy/", "Trening oporowy"),
    ("/kilimandzaro/trening/oporowy/core/", "Core"),
    ("/kilimandzaro/trening/oporowy/nogi-posladki/", "Nogi i pośladki"),
    ("/kilimandzaro/trening/oporowy/plecy-barki/", "Plecy i barki"),
    ("/kilimandzaro/trening/oporowy/stabilizacja/", "Stabilizacja"),
]

main_links = [
    ("/kilimandzaro/trasy/", "Trasy"),
    ("/kilimandzaro/dieta/", "Dieta"),
    ("/kilimandzaro/logistyka/", "Logistyka"),
    ("/kilimandzaro/zdrowie/", "Zdrowie"),
    ("/kilimandzaro/oddychanie/", "Oddychanie"),
    ("/kilimandzaro/safari-atrakcje/", "Safari i atrakcje"),
    ("/kilimandzaro/trening/", "Trening"),
]

def clean_lines(text):
    lines = []
    seen_consecutive = None

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue

        # Usuwamy typowe śmieci z eksportu/nawigacji, ale nie agresywnie.
        if line in {"ROADTO", "roadto.pl", "www.roadto.pl"}:
            continue

        if line == seen_consecutive:
            continue

        seen_consecutive = line
        lines.append(line)

    return lines

def line_to_html(line, index):
    safe = escape(line)

    # Krótkie linie wyglądające jak nagłówki robimy jako h2.
    if index > 0 and len(line) <= 80 and not line.endswith((".", ",", ";", ":")):
        return f"<h2>{safe}</h2>"

    return f"<p>{safe}</p>"

def render_page(title, description, lines):
    body = "\n".join(line_to_html(line, i) for i, line in enumerate(lines))

    main_nav = "\n".join(
        f'<a href="{href}">{escape(label)}</a>'
        for href, label in main_links
    )

    training_nav = "\n".join(
        f'<a href="{href}">{escape(label)}</a>'
        for href, label in training_links
    )

    return f"""<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} — ROADTO Kilimandżaro</title>
  <meta name="description" content="{escape(description)}">
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

    .section-nav {{
      margin-top: 34px;
      padding-top: 24px;
      border-top: 1px solid var(--border);
    }}

    .section-nav h2 {{
      margin-top: 0;
      font-size: 22px;
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
        {main_nav}
      </nav>
    </div>
  </header>

  <main>
    <div class="wrap">
      <article>
        <div class="breadcrumb">
          <a href="/kilimandzaro/trening/">Trening</a> / {escape(title)}
        </div>

        <h1>{escape(title)}</h1>
        <div class="lead">{escape(description)}</div>

        {body}

        <div class="section-nav">
          <h2>Podstrony treningowe</h2>
          <nav aria-label="Podstrony treningowe">
            {training_nav}
          </nav>
        </div>
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

backup_root = ROOT / "backups" / f"training-subpages-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
written = []

for filename, info in pages.items():
    source = TEXT_DIR / filename
    target = SITE_DIR / info["path"]

    if not source.exists():
        print(f"UWAGA: brak pliku tekstowego: {source}")
        continue

    text = source.read_text(encoding="utf-8", errors="ignore")
    lines = clean_lines(text)

    if not lines:
        print(f"UWAGA: pusty plik tekstowy: {source}")
        continue

    if target.exists():
        backup = backup_root / info["path"]
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(target, backup)

    target.parent.mkdir(parents=True, exist_ok=True)
    html = render_page(info["title"], info["description"], lines)
    target.write_text(html, encoding="utf-8")
    written.append(target)

print("")
print("Gotowe. Wygenerowano strony:")
for path in written:
    print("-", path.relative_to(ROOT))

if backup_root.exists():
    print("")
    print("Backup nadpisanych plików:")
    print("-", backup_root.relative_to(ROOT))
