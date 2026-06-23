# -*- coding: utf-8 -*-
"""
RoadTo — treść strony „Sprzęt".

Odtworzona 1:1 z oryginału (Framer). Dane są tu, a nie w `site/`, żeby
przetrwały regenerację (generator nie czyta tabel z HTML). Edytujesz tu,
potem uruchamiasz `python3 build_site.py`.

Struktura:
  SPRZET_SECTIONS = [ (numer, "Tytuł sekcji", [ blok, blok, ... ]) ]
  blok = ("group", "Podtytuł")                      -> nagłówek pod-grupy
       | ("table", "Pasek/None", [kolumny], [wiersze])
  wiersz = ["Nazwa produktu", komórka1, komórka2, ...]   (kolumny bez nazwy)
"""

INTRO = (
    "Sprzęt to Twój najlepszy towarzysz w drodze na szczyt – od wygodnych butów "
    "po ciepły śpiwór, który zapewni spokojny sen na dużej wysokości. W książce "
    "znajdziesz wszystkie praktyczne porady, na co zwrócić uwagę przy wyborze "
    "i zakupie ekwipunku, aby nic Cię nie zaskoczyło. Tutaj natomiast "
    "przygotowaliśmy listę przykładowych modeli ubrań i sprzętu, które naszym "
    "zdaniem warto rozważyć – sprawdzonych, wygodnych i godnych polecenia. Dzięki "
    "temu łatwiej znajdziesz rozwiązania dopasowane do własnych potrzeb i budżetu."
)

# Link do PDF-a „Ekwipunek niezbędny na wyprawę" (Google Drive).
# TODO: wklej tu właściwy link; "#" = placeholder.
CHECKLIST_PDF = "https://drive.google.com/file/d/14-ut4ORqLyJEfPICnr1vh-QnoNWwJcIA/view"

WAC = ["Waga", "Atuty", "Cena"]
MAC = ["Materiał", "Atuty", "Cena"]
SAC = ["Skład", "Atuty", "Cena"]
PAC = ["Pojemność", "Atuty", "Cena"]
AC  = ["Atuty", "Cena"]
MEM = ["Membrana / parametry", "Atuty", "Cena"]

SPRZET_SECTIONS = [
    (1, "Warstwa bazowa (bielizna termoaktywna)", [
        ("group", "Koszulki termiczne z długim rękawem"),
        ("table", "Wełna merino", WAC, [
            ["Icebreaker – 200 Oasis / 260 Tech", "ok 230 g",
             "naturalna regulacja temperatury, neutralizacja zapachów, komfort termiczny", "250–450 zł"],
            ["Smartwool – Merino 250", "ok 250 g",
             "ciepła, trwała, dobry balans między oddychalnością a izolacją", "350–470 zł"],
            ["Ortovox – 185 Rock'n'Wool", "ok 200 g",
             "miękka struktura, szybkie schnięcie, dobry wybór na warstwę bazową", "330–500 zł"],
            ["Forclaz – MT500", "ok 220 g",
             "dobry stosunek jakości do ceny, rozsądna izolacja", "130–230 zł"],
            ["Aclima – LightWool / WarmWool", "LightWool ok 200 g, WarmWool ok 260 g",
             "wydajne termicznie, lekkość i komfort noszenia", "300–450 zł"],
        ]),
        ("table", "Materiały syntetyczne", WAC, [
            ["Under Armour – HeatGear", "ok 200 g",
             "szybkie odprowadzanie wilgoci, elastyczność, dobre dopasowanie, szybkie schnięcie", "100–200 zł"],
            ["X-Bionic Under Energy Accumulator", "ok 220 g",
             "strefy wentylacyjne, systemy chłodzenia / magazynowania energii, dobry balans między izolacją a oddychalnością", "500–600 zł"],
            ["Brubeck Dry lub Thermo", "ok 170–250 g",
             "dobra relacja jakości do ceny, elastyczność, szybkie odprowadzanie potu", "120–250 zł"],
        ]),
        ("table", "Mieszanki merino z syntetykiem", WAC, [
            ["Icebreaker – Sphere LS", "ok. 180–200 g",
             "bardzo lekka i oddychająca, świetnie reguluje wilgoć, szybciej schnie niż 100% merino, przyjemna w dotyku", "300–400 zł"],
            ["Ortovox 120 Cool Tec Fast Upward", "ok. 110–120 g",
             "ekstremalnie lekka, przewiewna i szybkoschnąca, przyjemnie chłodzi dzięki domieszce włókien Cool-Tec, bardzo dobrze sprawdza się w intensywnym wysiłku", "300–400 zł"],
        ]),
        ("group", "Kalesony termoaktywne"),
        ("table", "Wełna merino", WAC, [
            ["Icebreaker – 260 Tech Leggings / Base Layer Bottom", "ok 250 g",
             "naturalna regulacja temperatury, komfort termiczny, dobre odprowadzanie wilgoci, lekkie i elastyczne", "350–520 zł"],
            ["Smartwool Classic Thermal Merino Base Layer Bottom", "ok 250 g",
             "dobra izolacja przy umiarkowanych temperaturach, miękkość materiału, komfort noszenia", "350–400 zł"],
            ["Ortovox Rock'n'Wool Long Pants", "ok 150–200 g",
             "miękki materiał, szybkie schnięcie, komfortowa warstwa bazowa", "300–400 zł"],
        ]),
        ("table", "Materiały syntetyczne", WAC, [
            ["Brubeck – Thermo / Dry Pants", "ok. 225 g",
             "bardzo dobre odprowadzanie wilgoci, elastyczność, dobra izolacja w stosunku do wagi, przyjemne w noszeniu", "150–200 zł"],
            ["Under Armour ColdGear Base Layer", "ok. 200 g",
             "miękki, szczotkowany materiał wewnętrzny, świetna elastyczność 4-way stretch, szybkie odprowadzanie wilgoci, komfort noszenia", "150–250 zł"],
            ["X-Bionic Apani 4.0 Merino Pants", "230–260 g",
             "strefy wentylacyjne i izolacyjne (technologia 3D Bionic Sphere®), precyzyjne rozmieszczenie funkcji dzięki Retina® Ultra HD, naturalna termika merino połączona z trwałością i elastycznością", "450–600 zł"],
        ]),
        ("table", "Mieszanki merino z syntetykiem", WAC, [
            ["Rab Syncrino Leggings", "ok 125 g",
             "elastyczna mieszanka merino + syntetyk, dobra oddychalność, komfort przy aktywności ruchowej", "200–300 zł"],
            ["Smartwool Intraknit Thermal Merino Bottoms", "ok 280 g",
             "zaawansowana konstrukcja, panele wentylacyjne + mieszanka merino/syntetyk, szybkie schnięcie", "450–600 zł"],
        ]),
    ]),

    (2, "Warstwa środkowa (izolacyjna)", [
        ("table", "Polar lub techniczna bluza", MAC, [
            ["Patagonia R1 Pullover Hoody", "Polartec® Power Grid® 93% poliester z recyklingu / 7% spandex",
             "elastyczny, oddychający, lekki, dobrze odprowadza wilgoć", "480–700 zł"],
            ["Rab Nexus Hoody", "Thermic™ G (178 g/m²) — poliester z recyklingu 94%, elastan 6%",
             "kaptur, elastyczność, dobry balans między izolacją a oddychalnością", "290–450 zł"],
            ["Montane Protium Hoodie", "drapany polar THERMO GRID o kostkowej strukturze, 93% poliester (z recyklingu), 7% elastan",
             "pakowność, elastyczność, komfort przy ruchu", "300–450 zł"],
            ["Montane Protium Pull-on", "polar THERMO Grid, 93% poliester (recyklowany), 7% elastan",
             "prostota kroju, dobra izolacja, komfort noszenia", "250–350 zł"],
            ["The North Face Glacier Fleece Jacket", "100% poliester",
             "miękki materiał, szybkie schnięcie, dobry stosunek ciepła do wagi, elastyczne wykończenia i kieszenie boczne", "280–360 zł"],
        ]),
        ("table", "Lekka kurtka puchowa (lub syntetyczna o podobnych właściwościach)", MAC, [
            ["Decathlon / Forclaz – Trek 100", "syntetyk",
             "dobra izolacja w stosunku do ceny, kompaktowość, szybkie schnięcie, łatwość w konserwacji", "200–300 zł"],
            ["Patagonia – Down Sweater Hoody (800 cuin)", "puch",
             "wysoka sprężystość puchu (800 cuin), doskonała izolacja przy niskiej wadze, trwałość, stylowy krój", "1200–1500 zł"],
            ["Patagonia – Micro Puff Hoody", "syntetyk",
             "bardzo lekka i pakowna, świetna izolacja nawet po zamoczeniu, oddychająca, wygodna w noszeniu", "1100–1400 zł"],
            ["The North Face – ThermoBall Eco Hoodie", "syntetyk",
             "syntetyczne wypełnienie ThermoBall Eco (z recyklingu), izoluje nawet na mokro, solidna konstrukcja, dobra cena jak na tę klasę", "800–1000 zł"],
            ["Rab – Microlight Alpine Down Jacket (700 cuin)", "puch",
             "puch 700 cuin, bardzo dobry stosunek ciepła do wagi, techniczny krój, niezawodna marka outdoorowa", "1100–1300 zł"],
        ]),
    ]),

    (3, "Warstwa zewnętrzna (ochrona przed wiatrem i deszczem)", [
        ("table", "Kurtka przeciwdeszczowa i przeciwwiatrowa", MEM, [
            ["Arc'teryx – Beta AR Jacket", "GORE-TEX® Pro; wodoodporność ≥ 20 000 mm H₂O; wysoka oddychalność",
             "wyjątkowa trwałość i odporność na przetarcia; minimalistyczny krój; kaptur kompatybilny z kaskiem; świetna na wyprawy wysokogórskie i skitury", "2500–3000 zł"],
            ["Mammut – Nordwand Advanced HS Hooded Jacket", "GORE-TEX® Pro; 28 000 mm H₂O; ekstremalna wytrzymałość",
             "techniczny, dopasowany krój; panele wzmacniające; idealna na alpinizm i trudne warunki; znakomita wentylacja", "1900–2800 zł"],
            ["Millet – Trilogy V Icon Dual GTX Pro Jacket", "GORE-TEX® Pro; ≥ 20 000 mm H₂O",
             "nowoczesny design; solidna konstrukcja; dobra ochrona w zmiennych warunkach; kaptur z regulacją 3D", "2000–3200 zł"],
            ["The North Face – Kandersteg Jacket", "GORE-TEX® Pro; 28 000 mm H₂O",
             "nowoczesny design; solidna konstrukcja TNF; dobra ochrona w zmiennych warunkach; kaptur z regulacją 3D", "1500–2600 zł"],
        ]),
        ("table", "Spodnie wodoodporne (hardshell)", MEM, [
            ["Rab – Firewall Pants", "Pertex® Shield, 3-warstwowy hardshell",
             "lekkie (~328 g, rozmiar M), w pełni rozpinane od talii, bardzo pakowne; idealne jako spodnie przeciwdeszczowe na trekkingi i wyprawy wysokogórskie", "600–850 zł"],
            ["Marmot – PreCip Full-Zip Pants", "NanoPro® (Marmot), 2,5-warstwowy laminat",
             "pełne boczne zamki ułatwiające zakładanie na buty, dobra oddychalność, odporne na deszcz, lekkie i kompaktowe", "300–600 zł"],
            ["The North Face – Venture 2 Half-Zip Rain Pants", "DryVent™ 2.5L hardshell",
             "lekka konstrukcja, zamki do kolan (knee-high zips), regulacja w pasie i nogawkach, dobra ochrona przed deszczem i wiatrem", "250–300 zł"],
            ["Montane – Solution Waterproof Pants", "Pertex Shield Revolve (2.5L, materiał z recyklingu)",
             "trwała tkanina, YKK ¾ long side zips, komfortowy krój, swoboda ruchu, przyjazne środowisku wykonanie", "600–750 zł"],
        ]),
    ]),

    (4, "Akcesoria odzieżowe", [
        ("group", "Rękawiczki"),
        ("table", "Cienkie rękawiczki trekkingowe", AC, [
            ["The North Face – Etip™ Glove", "kompatybilne z ekranami dotykowymi, lekkie i elastyczne, dobre dopasowanie", "120–180 zł"],
            ["Black Diamond – Lightweight Softshell", "obsługa ekranów dotykowych, bardzo pakowne, minimalna waga", "70–130 zł"],
            ["Black Diamond – Midweight Softshell", "touchscreen, zwiększona trwałość dzięki wzmocnieniom, komfort cieplny", "100–180 zł"],
            ["Rab – Power Stretch Contact Grip Glove", "touchscreen, świetny chwyt, oddychające i elastyczne", "150–200 zł"],
            ["Montane – Power Stretch Pro Glove", "touchscreen, minimalna waga, dobre dopasowanie i oddychalność", "160–200 zł"],
        ]),
        ("table", "Grube rękawiczki (warstwa zewnętrzna)", SAC, [
            ["Black Diamond – Soloist Gloves", "BD.dry™, skóra kozia, wykończenie GTT Empel DWR, izolacja PrimaLoft Gold",
             "wodoodporne, bardzo dobra izolacja, skórzane wzmocnienia dłoni, wszechstronność dzięki wyjmowanej wkładce", "400–600 zł"],
            ["Mountain Equipment – Guide Glove", "100% poliamid; podszewka: 100% poliester oraz 71% poliester / 29% akryl",
             "odporne na wiatr i wilgoć, trwałe, zapewniają precyzję chwytu", "290–450 zł"],
            ["Rab – Guide 2 GTX Glove", "skóra Pittards®; membrana Gore-Tex®; izolacja Primaloft® Gold",
             "pełna wodoodporność, wysoka izolacja, skórzane wzmocnienia dłoni, świetny balans między ciepłem a funkcjonalnością", "460–800 zł"],
            ["Rab – Endurance Down Mitts", "puch kaczki europejskiej 650 cuin z hydrofobowym wykończeniem Nikwax bez fluoru",
             "ekstremalnie ciepłe przy niskiej wadze, szybkoschnące, świetna pakowność", "400–620 zł"],
            ["Black Diamond – Mercury Mitts", "PrimaLoft Gold 340 g, nylon (Pertex Shield®)",
             "wyjątkowo ciepłe, trwałe, dobrze izolują nawet przy dużym mrozie, wszechstronne dzięki wyjmowanej wyściółce", "380–550 zł"],
        ]),
        ("group", "Nakrycia głowy i ochrona"),
        ("table", "Czapka", SAC, [
            ["Buff – Thermal Wool Beanie", "100% wełna merino",
             "lekka, termiczna, komfort użytkowania nawet do −20 °C, elastyczny i dobrze dopasowany krój", "100–170 zł"],
            ["Woolona – Icewall Merino", "100% wełna merino",
             "naturalna izolacja termiczna, świetnie zakrywa uszy, oddychająca, zapewnia ciepło nawet w ekstremalnych warunkach", "100–130 zł"],
        ]),
        ("table", "Chusta wielofunkcyjna (Buff®)", SAC, [
            ["Buff Original Ecostretch", "95% poliester z recyklingu, 5% elastan",
             "wszechstronność, szybkoschnąca tkanina, wygoda noszenia na wiele sposobów", "70–100 zł"],
            ["Merino Wool Buff", "100% wełna merynosa",
             "świetna termoizolacja, brak zapachu, wysoki komfort noszenia", "130–150 zł"],
            ["ThermoNet Buff", "96% poliester, 4% elastan",
             "izolacja cieplna, ochrona przed wiatrem, szybkie schnięcie", "90–120 zł"],
            ["Coolnet UV Buff", "95% poliester, 5% elastan",
             "maksymalna oddychalność, UPF 50+, ochrona przed słońcem", "70–100 zł"],
        ]),
        ("table", "Kapelusz lub czapka z daszkiem", AC, [
            ["Patagonia Duckbill Cap", "przewiewna, szybkoschnąca, stylowa konstrukcja", "90–180 zł"],
            ["Outdoor Research Sun Runner Cap", "ochrona karku przed słońcem, przewiewny materiał, regulacja", "150–220 zł"],
            # UWAGA: w oryginale opis tej pozycji był pusty (powielał nazwę) — do uzupełnienia.
            ["Sunday Afternoons Ultra Adventure Kapelusz", "—", "190–230 zł"],
        ]),
    ]),

    (5, "Obuwie", [
        ("table", "Lekkie buty obozowe", AC, [
            ["Crocs All-Terrain Atlas Clog", "bardzo lekki, łatwy do założenia i zdjęcia, dobra wentylacja, nadaje się jako obuwie „po” dniu wspinaczki — idealne do obozu", "350–400 zł"],
            ["The North Face ThermoBall Traction Mule V", "świetnie izoluje termicznie stopy, komfortowe w obozie, dobra ochrona przy krótkich przejściach wokół miejsca obozowego", "200–300 zł"],
            ["Bedrock Sandals Mountain Clog", "bardzo lekki model, zaprojektowany typowo jako obozowe obuwie dla backpackerów, dobra przyczepność", "750–800 zł"],
        ]),
        ("table", "Wysokie buty trekkingowe", AC, [
            ["Meindl – Bhutan MFS GTX", "bardzo dobre trzymanie stopy dzięki MFS, solidna impregnacja, klasyczny krój górski", "1300–1500 zł"],
            ["Lowa – Renegade GTX Mid", "dobra elastyczność, komfort na długich trasach, niezła oddychalność przy umiarkowanym obciążeniu", "650–1100 zł"],
            ["Hanwag – Tatra II GTX", "dobra elastyczność, komfort na długich trasach, niezła oddychalność przy umiarkowanym obciążeniu", "1000–1500 zł"],
            ["Salewa – MTN Trainer 2 Mid GTX", "dobra wentylacja, elastyczny i lekki materiał, dobra trakcja na zróżnicowanym terenie", "950–1300 zł"],
            ["La Sportiva – TX Hike Mid GTX", "dobra oddychalność, zwarta konstrukcja, dobre trzymanie w trudnych warunkach", "700–800 zł"],
        ]),
        ("table", "Skarpety trekkingowe", SAC, [
            ["Smartwool – Mountaineering Extra Heavy Crew", "74% wełny merino, 25% nylonu, 1% elastanu",
             "ekstremalnie ciepłe, bardzo trwałe, świetne na zimowe wyprawy wysokogórskie", "80–140 zł"],
            ["Bridgedale – Explorer Heavy", "poliamid",
             "miękkie, świetnie izolują, wzmocnione w strefach narażonych na przetarcia", "ok 100 zł"],
            ["Darn Tough – Mountaineering OTC Heavyweight Full Cushion", "74% wełna merino, 24% nylon, 2% Lycra Spandex",
             "wyjątkowa wytrzymałość, świetna izolacja i komfort termiczny", "200–220 zł"],
            ["Icebreaker – Hike+ Heavy Crew", "66% wełna merino, 32% nylon, 2% elastan",
             "miękkie, ciepłe, anatomiczny krój poprawia komfort i dopasowanie", "90–140 zł"],
        ]),
    ]),

    (6, "Sprzęt trekkingowy", [
        ("table", "Plecak podręczny 30–35 l", PAC, [
            ["Deuter – Futura 30", "30 l", "świetna wentylacja pleców, bardzo wygodny stelaż, dobre rozłożenie ciężaru", "500–750 zł"],
            ["Osprey – Talon 33", "31–33 l", "świetnie przylega do pleców, lekki, kompatybilny z bukłakiem", "500–600 zł"],
            ["Gregory – Zulu 30", "30 l", "rewelacyjne dopasowanie, bardzo wygodny system nośny, dużo kieszeni i przegród", "500–850 zł"],
            ["Salewa – Alp Trainer 33", "33 l", "solidny i bardzo trwały materiał, przystosowany do cięższych ładunków", "500–770 zł"],
        ]),
        ("table", "Torba transportowa (duffel bag 70–90 l)", ["Waga / pojemność", "Atuty", "Cena"], [
            ["The North Face – Base Camp Duffel", "ok 1,8 kg / 95 l", "kultowa trwałość, grube PVC odporne na przetarcia i wilgoć, wygodne szelki naramienne", "500–700 zł"],
            ["Rab Expedition Kitbag II", "ok 1 kg / 80 l", "wyjątkowo mocny materiał balistyczny, wyściełane pasy naramienne do noszenia jak plecak, odporność na trudne warunki", "400–600 zł"],
            ["Patagonia – Black Hole Duffel (70 / 100 l)", "ok 1,4 kg / 70 l", "wodoodporny materiał TPU, możliwość spakowania torby w jej własną kieszeń, nowoczesny design", "580–860 zł"],
            ["Forclaz Duffel 900 Extend", "ok 2,2 kg / 80–120 l", "solidna konstrukcja w przystępnej cenie, odpinane szelki do noszenia jak plecak, wodoodporna", "400–500 zł"],
        ]),
        ("table", "Kijki trekkingowe", AC, [
            ["Black Diamond – Trail / Trail Pro", "niezawodny system blokady FlickLock, duża trwałość, komfortowe uchwyty, niska waga", "400–580 zł"],
            ["LEKI – Khumbu", "świetnie wyprofilowane rączki z przedłużonym gripem, opcja amortyzacji redukująca obciążenie stawów", "300–400 zł"],
            ["Fizan – Compact / Trek", "jedne z najlżejszych kijów aluminiowych na rynku, atrakcyjna cena, składane do kompaktowych rozmiarów", "220–320 zł"],
            ["Komperdell – Explorer Contour", "ergonomiczne uchwyty, trwały system amortyzacji, solidna konstrukcja do trudnych warunków", "400–520 zł"],
        ]),
        ("table", "Czołówka", ["Lumeny", "Atuty", "Cena"], [
            ["Petzl – Actik Core", "do 600 lm", "moc 600 lm, lekka konstrukcja i hybrydowe zasilanie (akumulator Core lub baterie AAA) — elastyczność i wygoda w każdych warunkach", "200–300 zł"],
            ["Petzl Swift RL", "do 1100 lm", "jasny, kompaktowy tryb mieszany (rozproszony + skupiony), automatyczne sterowanie jasnością, ładowanie USB-C, ruchome mocowanie, funkcja blokady, dioda stanu baterii", "350–500 zł"],
            ["Ledlenser MH7", "do 600 lm", "moc 600 lm i zasięg do 200 m, podwójny system zasilania (akumulator lub baterie AA), niezawodność w trudnych warunkach i przy długich nocnych aktywnościach", "200–260 zł"],
            ["Decathlon – Forclaz HL900 USB", "do 600 lm", "bardzo atrakcyjna cena, wodoodporność, dobry stosunek ceny do funkcji", "130–200 zł"],
        ]),
        ("table", "Śpiwór", ["Waga / wkład", "Komfort / limit", "Atuty", "Cena"], [
            ["Pajak – Core 950", "1,4 kg, puch kaczy", "−10 / −18 °C", "wysoka klasa puchu, doskonała izolacja nawet w ekstremalnych warunkach", "ok 2500 zł"],
            ["Cumulus – Panyam 600", "ok 1 kg, puch gęsi", "−6 / −13 °C", "dobry balans między wagą a izolacją, elastyczność użycia w różne sezony", "1600–1800 zł"],
            ["Cumulus – Teneqa 700", "ok 1,3 kg, puch gęsi", "−15 / −23 °C", "bardzo wysoka izolacja, nadaje się także na chłodniejsze noce", "2100–2300 zł"],
            ["Mammut – Perform Fiber Bag", "ok 1,2 kg, syntetyk", "−4 / −11 °C", "syntetyczne ocieplenie HL-ElixR™ ECO działa dobrze nawet w wilgotnych warunkach; zamek pełnej długości + wentylacja oraz kieszonka wewnętrzna", "ok 850 zł"],
        ]),
        ("table", "Mata samopompująca", WAC, [
            ["Therm-a-Rest ProLite Plus", "ok 450 g", "bardzo kompaktowa, dobra izolacja na 3 sezony, przyjemny komfort snu", "380–600 zł"],
            ["Sea to Summit Comfort Light SI", "ok. 790 g", "komfort wyższy niż w standardowych matach samopompujących, lekka i kompaktowa", "480–700 zł"],
            ["Robens PrimaCore 60", "ok 650 g", "lepsza izolacja niż w klasycznych matach samopompujących, komfort cieplny w chłodniejsze noce", "420–780 zł"],
        ]),
        ("table", "Karimata z pianki EVA", WAC, [
            ["Easy Camp – Wave EVA Mat", "ok 320 g", "bardzo wytrzymała, prosta konstrukcja, nie wymaga pompowania, odporna na uszkodzenia", "90–120 zł"],
            ["Mil-Tec – BW EVA Mat", "ok 610 g", "minimalistyczna, tania opcja, dobra jako mata zapasowa, łatwa do czyszczenia", "100–110 zł"],
        ]),
    ]),

    (7, "Nawodnienie i ochrona", [
        ("table", "Bukłak z rurką — główne źródło", PAC, [
            ["Hydrapak Hydrasleeve Reservoir 3L", "3 l", "izolowany rękaw chroni zawartość przed nagrzewaniem / wychłodzeniem, szeroki otwór do napełniania, zawór typu Plug-N-Play", "200–330 zł"],
            ["Source Widepac / Tactical Reservoir", "2–3 l", "smukły kształt (ułatwiający dopasowanie do plecaka), kompatybilność z systemami taktycznymi, szybkie napełnianie", "130–200 zł"],
            ["Osprey Hydraulics LT Reservoir", "1,5 l", "konstrukcja z dwoma przegrodami (dual baffles) dla stabilności, złącze Slide-Seal™, system magnetyczny na rurce, zawór z przyciskiem on/off, łatwe napełnianie i obsługa jedną ręką", "130–160 zł"],
        ]),
        ("table", "Bidony — rezerwa i „plan B”", PAC, [
            ["Nalgene Wide Mouth 1 L", "1 l (ok 145 g)", "szeroka szyjka ułatwia dolewanie i czyszczenie, materiał BPA-free, trwały", "50–80 zł"],
            ["Hydrapak Stash", "1 l (ok 100 g)", "kompaktowy, lekki, idealny jako zapasowy pojemnik, gdy oryginalny bukłak się zepsuje", "100–140 zł"],
            ["Quechua 500 Ecozen 0,8 l", "0,8 l (ok 130 g)", "bardzo dobry stosunek cena / funkcja, łatwo dostępny w Decathlon", "ok 25 zł"],
        ]),
        ("table", "Termos", PAC, [
            ["Stanley – Classic Legendary", "ok 500–600 g (wersja 1 l)", "ekstremalnie trwały, utrzymuje temperaturę przez wiele godzin, kultowy design", "200–250 zł"],
            ["Primus TrailBreak EX Vacuum Bottle", "ok. 630 g (wersja 0,75 l)", "łatwy korek z wygodnym uchwytem, antypoślizgowa powierzchnia, dobre utrzymywanie ciepła", "140–210 zł"],
            ["Esbit – Majoris Vacuum Flask", "ok. 510 g (wersja 0,75 l)", "solidna konstrukcja, dobre właściwości izolacyjne, kompaktowy rozmiar", "150–200 zł"],
            ["Thermos – Light & Compact", "ok. 260–300 g (wersja 0,75 l)", "kompaktowy design, dobra izolacja cieplna, solidna stal nierdzewna", "120–200 zł"],
        ]),
        ("table", "Okulary przeciwsłoneczne", ["Kategoria", "Atuty", "Cena"], [
            ["Julbo Camino (Spectron Cat 3)", "3", "dobra ochrona UV, stabilność na twarzy, klasyczny design", "300–400 zł"],
            ["Uvex MTN Classic CV", "3", "boczne osłony, wysoka ochrona kat. 3, świetny kontrast dzięki soczewkom ColorVision", "450–750 zł"],
            ["Julbo Shield", "3", "zdejmowane boczne osłony chroniące przed światłem bocznym, system Air Flow zapobiegający parowaniu szkieł, elastyczne, antypoślizgowe zauszniki (Grip Tech) i nos (Nose Grip)", "400–550 zł"],
            ["GOG – Manaslu (Matt Black / Purple)", "2–4", "soczewki fotochromowe (kat. 2–4), lekka i elastyczna konstrukcja TR90, pełna ochrona UV400 z powłoką lustrzaną, boczne osłony z regulowanym sznurkiem, hydrofobowa powłoka zapobiegająca parowaniu", "320–500 zł"],
        ]),
        ("table", "Kremy SPF 50+", PAC, [
            ["Piz Buin – Mountain Suncream SPF50", "tubka 50 ml", "wysoka ochrona UVA/UVB, formuła chroniąca skórę w zimnie i wietrze, poręczny format", "70–100 zł"],
            ["Lifesystems – Mountain SPF50+", "tubka 100 ml", "bardzo wysoka odporność na promieniowanie UV, formuła odporna na pot i zimno, stworzony do dużych wysokości", "55–100 zł"],
            ["Alpen – Glacier Cream SPF 50", "40 g", "bardzo wysoka ochrona SPF 50, poręczne opakowanie idealne do plecaka, formuła dostosowana do ekspozycji na słońce, wiatr i niskie temperatury", "55–80 zł"],
            ["Aptonia SPF 50+", "tubka 50 ml", "przystępna cena, wodoodporny, praktyczny w podróży", "25–40 zł"],
        ]),
        ("table", "Balsamy do ust z filtrem SPF", PAC, [
            ["Blistex SPF 50", "4,25 g", "wysoka ochrona, nawilżenie, łatwa aplikacja", "11–25 zł"],
            ["Bielenda — ochronny balsam do ust SPF50", "10 g", "łatwa aplikacja, dobra ochrona przeciwsłoneczna", "30–50 zł"],
            ["Bondi Sands Lip Balm SPF50+", "10 g", "mocna ochrona, lekka formuła, marka znana z produktów do opalania", "18–35 zł"],
        ]),
    ]),
]
