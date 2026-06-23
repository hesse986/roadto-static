# HANDOFF — roadto.pl (migracja z Framera na stronę statyczną)

> Wklej ten dokument na początku NOWEJ rozmowy. **Najpierw wgraj też najnowszą paczkę
> `roadto-tresc.zip`** (albo swój katalog repo) — bez tego nowy asystent nie ma plików,
> bo środowisko robocze zeruje się między rozmowami.

---

## 1. Co to za projekt
Strona **roadto.pl** — poradnik wejścia na Kilimandżaro (po polsku). Migrujemy ją z
Framera na **statyczną stronę generowaną Pythonem**, odporną na regenerację. Właściciel
jest nietechniczny, pracuje lokalnie w `~/roadto-backup`, publikuje przez `git push` na
Cloudflare (Cloudflare serwuje folder `/site`, **bez** kroku budowania po stronie serwera).

**Problem przewodni:** przy zgrywaniu z Framera część treści (zwinięte akordeony,
tabele, komponenty) nie pobrała się jako tekst — strony wyszły „cienkie". Schemat
naprawy: użytkownik przysyła screeny rozwiniętej treści → przepisujemy ją 1:1 do modułu
danych w Pythonie → dodajemy dedykowaną funkcję w generatorze, żeby treść przetrwała
regenerację (tak jak `build_trasy`/`build_home`).

## 2. Jak działa generator
- `build_site.py` — generator. Uruchomienie: `python3 build_site.py` (z katalogu projektu).
  Wypisuje „Built 21 pages:". Tworzy folder `site/` (gotowy output).
- `src_pages/` — oryginalny, surowy zrzut HTML z Framera (źródło tekstu; tylko do odczytu w sensie logicznym).
- `site/assets/css/site.css` — style.
- Moduły danych (treść odzyskana ze screenów): `sprzet_data.py`, `safari_data.py`, `zdrowie_data.py`.
- W `build_site.py`: `SECTIONS` = kafelki nav/landing/stopka; `PAGES` = wszystkie strony.
  Helpery: `head() nav() hero() crumbs() footer() write() esc() extract_items() _gear_table() _rich() _zd_block()`.
  Akordeony: `<details class="chapter">` z `<summary>`. `main()` rozdziela slugi do dedykowanych funkcji.

## 3. Co jest ZROBIONE (w aktualnej paczce roadto-tresc.zip)
- **Sprzęt** (`/kilimandzaro/sprzet/`): pełny przewodnik, 7 sekcji, 31 tabel, 113 produktów
  (`sprzet_data.py`, renderer `build_sprzet` + `_gear_table`). Brak linku PDF (checklist) — placeholder.
- **Safari i atrakcje** (`/kilimandzaro/safari-atrakcje/`): 8 atrakcji jako akordeony
  (`safari_data.py`, `build_safari`). Zdjęcia atrakcji: były w Framerze, nie potwierdzone w repo (tekst-only).
- **Logistyka**: UKRYTA z nav/stopki/kafelków (usunięta z `SECTIONS`). URL
  `/kilimandzaro/logistyka/` nadal się generuje (żywy dla ew. kodu QR). Przywrócenie: odkomentuj wpis w `SECTIONS`.
- **Trening — strony ćwiczeń** (4 podstrony oporowego): `nogi-posladki` (10 ćwiczeń),
  `core` (6), `plecy-barki` (4), `stabilizacja` (3). Każde ćwiczenie = jeden akordeon z
  sekcjami Pozycja startowa (✓) / Ruch (→) / Najczęstsze błędy (✕) / Warianty + „Wskazówka
  trenera" w żółtym dymku. Renderer `build_training_exercise` parsuje istniejący `src_pages`
  (NIC nie przepisywano). Funkcje: `_parse_exercises`, `_split_title`, `_ex_norm`, stała `BULB`.
- **Zdrowie** (`/kilimandzaro/zdrowie/`): cała strona przebudowana. 7 szczepień jako
  rozwijane sekcje (zielony ✓ w nagłówku) z opisem w środku. Malaria: 3-kolumnowa tabela
  ryzyka (`vax-cols`), tabela etapów podróży (`_gear_table`), lista ochrony przed komarami
  (`vax-check`), fazy/objawy. „Praktyczne szczegóły" = numerowane kroki (`vax-steps`).
  Apteczka + Mini-poradnik = sekcje z przyciskiem PDF (placeholder). Treść w `zdrowie_data.py`,
  renderer `build_zdrowie` + helpery `_rich`, `_zd_block`.

## 4. Co ZOSTAŁO do zrobienia (PENDING)
1. **Filmy w Treningu** — nagrania „TAKE YOUR PLAN" przy ćwiczeniach NIE zgrały się
   (tylko tekst). Gdy użytkownik poda linki (YouTube/Vimeo), dodać slot na film w
   `build_training_exercise` (np. prawa kolumna obok sekcji; CSS już przewiduje układ).
2. **PDF-y** — UWAGA: w oryginale roadto.pl były **4** przyciski pobierania, nie 3
   (4. to checklista na stronie Logistyka, która jest ukryta — dlatego umykała w rachunku).
   ZROBIONE (linki Google Drive podpięte, przyciski aktywne):
   - `CHECKLIST_PDF` w `sprzet_data.py` — „Ekwipunek niezbędny na wyprawę" ✓
   - `APTECZKA_PDF` w `zdrowie_data.py` — „Apteczka do pobrania" ✓
   - `PORADNIK_PDF` w `zdrowie_data.py` — „Poradnik do pobrania" ✓
   PENDING — **Logistyka (checklista)**: właściciel ma uruchomić link, ALE strona Logistyka
   ma POZOSTAĆ ukryta z nav/stopki/kafelków. Gdy poda link: dodać stałą (np. `LOGISTYKA_PDF`)
   i podpiąć przycisk w renderze logistyki — strona dalej niewidoczna w menu, ale żywa pod URL.
3. **Literówka medyczna** — ZROBIONE: Żółta Febra „immunokompetentnych" → „immunoniekompetentnych"
   (`zdrowie_data.py`, VACCINES[0]).
4. **Zdjęcia atrakcji Safari** — pliki nieobecne w repo; strony tekstowe.
5. **Sprzęt — czapka „Sunday Afternoons"** — atut był pusty, renderuje się „—".

Strony treningu, które NIE są ćwiczeniami (zostawione jako artykuły, render `build_leaf`):
`trening/wydolnosciowy/strefy-tetna`, `…/czynniki-wplywajace`, `trening/regeneracja`.
Huby (`trening`, `…/oporowy`, `…/wydolnosciowy`) działają (kafelki-linki). Te małe zdjęcia
na screenach Framera to kafelki linkujące do podstron — w generatorze to `card-link`.

## 5. Jak kontynuować w nowej rozmowie
1. Wgraj najnowszą `roadto-tresc.zip`. Asystent rozpakuje do `/home/claude/roadto/`,
   uruchomi `python3 build_site.py` i pracuje dalej tym samym schematem (drop-in zip).
2. Nowa treść do odzyskania → screeny → przepis 1:1 do modułu `*_data.py` → funkcja w generatorze.
3. Deliverable zawsze jako `/mnt/user-data/outputs/roadto-tresc.zip` (kumulatywny drop-in)
   + zaktualizować `CO-ZROBIONO.md`.

## 6. Podgląd i publikacja (komendy dla właściciela)
**Podgląd** (paczka w `~/Downloads`):
```
cd ~/roadto-backup
unzip -o ~/Downloads/roadto-tresc.zip -d ~/roadto-backup
cd ~/roadto-backup/site && python3 -m http.server 8000     # Ctrl+C aby zatrzymać
```
Sprawdź m.in.: `/kilimandzaro/zdrowie/`, `/kilimandzaro/trening/oporowy/nogi-posladki/`.

**Publikacja** (uwaga na pliki danych — `zdrowie_data.py` jest nowy):
```
cd ~/roadto-backup
git add site build_site.py sprzet_data.py safari_data.py zdrowie_data.py src_pages CO-ZROBIONO.md
git commit -m "Zdrowie: szczepienia rozwijane; Trening; Logistyka ukryta"
git push origin main
```

## 7. Pliki w paczce
- `build_site.py` — generator (zawiera build_sprzet / build_safari / build_zdrowie / build_training_exercise).
- `sprzet_data.py`, `safari_data.py`, `zdrowie_data.py` — treść (edytuj tu, potem rebuild).
- `site/` — gotowy output (21 stron) — to publikujesz.
- `src_pages/` — surowe źródło z Framera (źródło tekstu dla parserów).
- `CO-ZROBIONO.md` — changelog. `HANDOFF.md` — ten dokument.
