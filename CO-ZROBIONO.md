# RoadTo — aktualizacja treści: Sprzęt + Safari (23.06.2026)

## Co się zmieniło
Dwie „chude" strony dostały pełną treść z Framera:

- **/kilimandzaro/sprzet/** — 7 sekcji, 31 tabel, 113 produktów (warstwy odzieży,
  akcesoria, obuwie, sprzęt trekkingowy, nawodnienie i ochrona).
- **/kilimandzaro/safari-atrakcje/** — wszystkie 8 atrakcji jako rozwijane sekcje
  (Jezioro Chala, Ol Doinyo Lengai & Natron, Arusha NP, Lake Manyara, Mount Meru,
  Zanzibar, Wodospad Materuni, Gorące źródła Kikuletwa). Każda z opisem, „Tipem"
  i blokiem Jak się dostać / Koszt / Warto wiedzieć.

Nowe / zmienione pliki:
- `sprzet_data.py`  — treść tabel Sprzętu (edytujesz tu)
- `safari_data.py`  — treść atrakcji Safari (edytujesz tu)
- `build_site.py`   — generatory tabel (Sprzęt) i atrakcji (Safari)
- `site/assets/css/site.css` — style tabel i sekcji Safari
- `site/kilimandzaro/sprzet/index.html`, `site/kilimandzaro/safari-atrakcje/index.html`

## Jak wgrać (paczka w ~/Downloads)
```
cd ~/roadto-backup
unzip -o ~/Downloads/roadto-tresc.zip -d ~/roadto-backup
cd ~/roadto-backup/site
python3 -m http.server 8000
# otwórz: http://localhost:8000/kilimandzaro/sprzet/
#         http://localhost:8000/kilimandzaro/safari-atrakcje/
# zatrzymanie: Ctrl + C
```

Publikacja (UWAGA: doszły NOWE pliki sprzet_data.py i safari_data.py):
```
cd ~/roadto-backup
git add site build_site.py sprzet_data.py safari_data.py src_pages
git commit -m "Sprzet i Safari: pelna tresc z Framera"
git push origin main
```

## Do uzupełnienia
1. **PDF Sprzętu** — w `sprzet_data.py` zmień `CHECKLIST_PDF = "#"` na link Google Drive.
2. **Kapelusz „Sunday Afternoons"** w Sprzęcie — opis był pusty w oryginale (`—`).
3. **Zdjęcia przy atrakcjach Safari** — w Framerze każda atrakcja miała zdjęcie.
   Te pliki trzeba dograć do repo, żeby je pokazać. Na razie strony są tekstowe.
4. **Logistyka** — ostatnia chuda strona (głównie „checklista do pobrania" + PDF).

## Edycja treści w przyszłości
Treść Sprzętu → `sprzet_data.py`, Safari → `safari_data.py`. Zmień → zapisz →
`python3 build_site.py`. Wszystko wbudowane w generator, więc nie znika.

## Zmiana 23.06 (wieczór)
- **Logistyka ukryta** — usunięta z menu, stopki i kafelków na stronie Kilimandżaro.
  Strona /kilimandzaro/logistyka/ nadal się generuje (URL żywy dla ewentualnego QR),
  ale nigdzie nie ma do niej linku. Aby przywrócić: odkomentuj wpis w `build_site.py` (SECTIONS).
- **Trening** — treść ćwiczeń JEST (zgrana z Framera). Do poprawy zostało formatowanie
  (ćwiczenie + „Wskazówka trenera" w jednym boksie) oraz filmy (brak linków w zgranym tekście).

## Zmiana 23.06 — Trening (formatowanie ćwiczeń)
- 4 strony oporowego (nogi i pośladki, core, plecy i barki, stabilizacja) przebudowane:
  każde ćwiczenie = jeden rozwijany blok z sekcjami Pozycja startowa / Ruch /
  Najczęstsze błędy / Warianty (listy ✓ → ✕) + „Wskazówka trenera" w żółtym dymku.
  Wcześniej ćwiczenie i wskazówka były osobnymi boksami (wyglądało na poszatkowane).
- Renderer czyta istniejącą treść z `src_pages` (nic nie przepisywano), więc poprawka
  jest w generatorze (`build_site.py`, funkcja build_training_exercise) i przetrwa regenerację.
- DO ZROBIENIA: filmy „TAKE YOUR PLAN" — w zgranym tekście nie ma linków. Gdy podasz
  linki (YouTube/Vimeo), dorobię osadzenie filmu przy każdym ćwiczeniu.

## Zmiana 23.06 — Zdrowie (szczepienia rozwijane)
- Cała strona „Zdrowie" przebudowana. 7 szczepień (Żółta Febra, Dur Brzuszny, WZW A,
  WZW B, Tężec/błonica, Polio, Malaria) jako rozwijane sekcje z opisem w środku.
- Opisy szczepień NIE zgrały się przy imporcie (zwinięte akordeony Framera) —
  odzyskane 1:1 ze screenów i zapisane w `zdrowie_data.py`.
- Malaria: 3-kolumnowa tabela ryzyka wg regionu, tabela ryzyka wg etapu podróży,
  lista ochrony przed komarami (zielone ✓), fazy/objawy, kiedy do lekarza.
- „Praktyczne szczegóły" = numerowane kroki. Apteczka + Mini-poradnik = sekcje
  z przyciskiem PDF (na razie placeholder — brak linków Google Drive).
- UWAGA do sprawdzenia: w opisie Żółtej Febry jest fraza „osób ciężko
  immunokompetentnych" — odtworzona 1:1 z oryginału, ale wygląda na literówkę
  (prawdopodobnie miało być „immunoNIEkompetentnych”). Nie zmieniałem — zweryfikuj.

## Aktualizacja (sesja 23.06, część „Zdrowie / PDF-y")
- Podpięto 3 linki PDF (Google Drive), przyciski aktywne:
  Sprzęt → „Ekwipunek niezbędny na wyprawę", Zdrowie → „Apteczka do pobrania" + „Poradnik do pobrania".
- Poprawiono literówkę medyczną: Żółta Febra „immunokompetentnych" → „immunoniekompetentnych".
- Ustalono: w oryginale były 4 przyciski pobierania (4. = checklista na ukrytej stronie Logistyka).
  PENDING: link do Logistyki — strona ma pozostać ukryta w menu.

## Aktualizacja (sesja 23.06, część „Logistyka PDF")
- Podpięto 4. (ostatni) plik PDF: checklista na stronie Logistyka (link Google Drive).
- Dodano dedykowany renderer `build_logistyka` (hero + wstęp 1:1 + przycisk „Checklista do pobrania").
- Logistyka POZOSTAJE ukryta w menu/stopce/kafelkach (0 linków w serwisie) — dostępna tylko pod URL.
- Komplet: wszystkie 4 przyciski pobierania aktywne (Ekwipunek, Apteczka, Poradnik, Checklista).

## Aktualizacja (sesja 23.06, część „Trasy")
- Sekcja Trasy: 8 tras (Marangu, Machame, Lemosho, Rongai, Shira, Umbwe, Northern Circuit, Western Breach)
  jako panele pod przełącznikiem map — każda: główka (Długość/Czas/Trudność/Przewyższenie),
  lista „sprawdzi się, jeśli", dni w szarych kartach (stats + opis), tabela wersji (gdy jest).
- NAPRAWA: trasy_data.py nie kompilował się — polskie cudzysłowy „tekst" miały zamykający znak jako
  zwykły ASCII " (rozrywał stringi). Naprawiono 18 par (zamykające → ”). Build znów przechodzi (21 stron).
- DO WERYFIKACJI (nie zmyślam treści): brak tabeli „różnice wersji" w danych dla Machame, Rongai, Umbwe;
  Western Breach ma dni 3–7 (1–2 brak — prawdopodobnie celowo, bo dojście zależy od trasy: Machame/Lemosho/Umbwe).

## Aktualizacja (sesja 23.06, część „PDF Treningu oporowego")
- Podpięto 5. plik PDF: na hubie /kilimandzaro/trening/oporowy (link Google Drive).
- build_hub obsługuje teraz opcjonalny przycisk PDF (pole `pdf=(label, link)` w PAGES).
- Etykieta przycisku ustawiona jako „Plan treningu oporowego do pobrania" — do potwierdzenia/zmiany,
  bo oryginalna nazwa nie zgrała się ze schowanego komponentu (edycja: pole `pdf` w PAGES["kilimandzaro/trening/oporowy"]).

## Aktualizacja (sesja 23.06, część „Trasy — tabele Machame/Rongai/Umbwe")
- Dodano tabelę „Różnice między wersją 7- a 8-dniową" do Machame, Rongai, Umbwe (były placeholdery table=None).
  Dni tych tras zgadzały się 1:1 ze screenami — brakowało tylko tabeli. Treść tabeli 1:1 ze strony.
- Wszystkie 8 tras ma teraz tabelę wersji (Marangu: 5–6; pozostałe: 7–8).
- Pozostałe flagi do ewentualnej weryfikacji (notatki w trasy_data.py, nie blokują):
  Shira i Northern Circuit mają tabelę „7/8 dni" mimo innej liczby dni trasy; Western Breach bez dni 1–2 (dojście).
