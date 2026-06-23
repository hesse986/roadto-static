from pathlib import Path

SITE = Path("site")
CSS_LINK = '<link rel="stylesheet" href="/assets/css/roadto-brand.css">'

changed = []

for file in SITE.rglob("*.html"):
    text = file.read_text(encoding="utf-8", errors="ignore")

    if CSS_LINK in text:
        continue

    if "</head>" not in text:
        print("Pominięto bez </head>:", file)
        continue

    text = text.replace("</head>", f"  {CSS_LINK}\n</head>")
    file.write_text(text, encoding="utf-8")
    changed.append(file)

print("Podłączono CSS do:")
for file in changed:
    print("-", file)
