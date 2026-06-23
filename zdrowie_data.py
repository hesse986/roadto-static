# -*- coding: utf-8 -*-
"""
RoadTo — treść strony „Zdrowie".

Szczepienia = rozwijane sekcje (akordeon). Treść medyczna odtworzona 1:1
z Framera (opisy szczepień były w zwiniętych komponentach, nie zgrały się
przy imporcie). Edytujesz tu, potem `python3 build_site.py`.

Bloki w opisie szczepienia:
  ("h", "Nagłówek pytania")
  ("p", "akapit z **pogrubieniem**")
  ("ul", ["punkt", ...])
  ("check", ["punkt z zielonym ✓", ...])
  ("cols", [("Nagłówek kolumny", [bloki...]), ...])   # 3 kolumny obok siebie
  ("table", "podpis|None", [nagłówki bez 1. kolumny], [wiersze])
"""

ZDROWIE_INTRO = (
    "Przygotowując się do wejścia na Kilimandżaro nie można zapominać o kwestiach "
    "zdrowotnych. Afryka Wschodnia to inny klimat, inne zagrożenia i inne warunki niż "
    "te, do których jesteśmy przyzwyczajeni w Europie. Odpowiednie szczepienia, "
    "profilaktyka przeciwmalaryczna i dobrze skompletowana apteczka to nie tylko "
    "formalność, ale realna ochrona zdrowia i komfortu w trakcie wyprawy. W tym "
    "rozdziale znajdziesz praktyczne informacje, które pomogą Ci zadbać o "
    "bezpieczeństwo i przygotować organizm na spotkanie z Afryką i górami."
)

SZCZEPIENIA_INTRO = (
    "Zanim ruszysz w stronę Kilimandżaro warto zadbać o zdrowie jeszcze na etapie "
    "przygotowań. My również przed pierwszym wyjazdem do Tanzanii spędziliśmy trochę "
    "czasu w punktach szczepień – to po prostu część wyprawy. Dzięki temu czuliśmy się "
    "spokojniej i bezpieczniej, wiedząc że chronimy się przed chorobami, z którymi w "
    "Europie nie mamy do czynienia. Poniżej znajdziesz listę szczepień, które warto "
    "rozważyć, oraz informacje, gdzie najlepiej je wykonać."
)

VACCINES = [
    {"title": "Żółta Febra (Yellow fever)", "blocks": [
        ("h", "Czym jest i jak się objawia?"),
        ("p", "Żółta Febra to wirusowa choroba przenoszona przez ukąszenia zakażonych komarów (Aedes, Haemagogus)."),
        ("p", "**Objawy:** u większości zakażonych przebieg choroby jest łagodny (gorączka, bóle mięśni, nudności), ale u części rozwija się ciężka postać z żółtaczką, niewydolnością wątroby i nerek, krwawieniami, a nawet śmiercią."),
        ("p", "Okres inkubacji zwykle wynosi 3–6 dni."),
        ("h", "Czy szczepienie jest obowiązkowe?"),
        ("p", "Tanzania wymaga dowodu szczepienia przeciw żółtej febrze (odnotowanego w Międzynarodowym Świadectwie Szczepień — ICVP, tzw. „żółta książeczka”) jeśli podróżujesz z kraju endemicznego dla żółtej febry albo byłeś w takim kraju w trakcie podróży — obejmuje to także dłuższe tranzyty/międzylądowania (np. przesiadka ≥12 godzin w kraju endemicznym). Dla podróżnych przybywających bezpośrednio z krajów niezagrożonych (np. Polska) zazwyczaj nie wymaga się szczepienia, ale reguły mogą się różnić w zależności od kraju odlotu i aktualnych ognisk. **Na chwilę obecną przy lotach z Polski nawet z przesiadką (nie dłuższą niż 12h) w Nairobi czy Addis Abeba szczepienie nie jest obligatoryjne.**"),
        ("h", "Kiedy się zaszczepić / schemat:"),
        ("p", "Jedna dawka szczepionki YF (żywa, atenuowana) — podaje się co najmniej 10 dni przed podróżą, by ochrona była uznawana przy wjeździe. Od 2016 r. IHR uznaje certyfikat za ważny całe życie po szczepieniu."),
        ("h", "Przeciwwskazania / uwagi bezpieczeństwa:"),
        ("p", "Szczepionka żółtej febry jest szczepionką żywą — niezalecana dla osób ciężko immunoniekompetentnych, pacjentów z zaawansowaną chorobą immunologiczną, u kobiet w intensywnej immunosupresji. Powikłania (rzadkie) obejmują ciężkie reakcje neurologiczne lub żółtej febry-odwzorowanej reakcji poszczepiennej u osób starszych. O szczepieniu decyduje lekarz podróżny."),
        ("h", "Gdzie się szczepić i dokumentacja:"),
        ("p", "Żółta książeczka (ICVP) musi być wypełniona i podpisana/ostemplowana przez uprawnione centrum / ośrodek szczepień przeciw żółtej febrze. W Polsce i w wielu krajach są oficjalne ośrodki szczepień żółtej febry — szczepienia w takich punktach uprawniają do wydania ICVP. W Tanzanii dowód jest wymagany przy wjeździe tylko w opisanych wyżej sytuacjach — miej dokument przy sobie (oryginał) i kopię cyfrową."),
        ("h", "Przykładowe wyspecjalizowane placówki:"),
        ("ul", [
            "Vaccine Centre – Krakowski Szpital Specjalistyczny im. św. Jana Pawła II (Kraków)",
            "Centrum Medycyny Podróży OpenMed (Warszawa i Płock) – oferują szeroki zakres szczepień",
            "POLMED – sieć placówek w miastach: Gdańsk, Gdynia, Katowice, Kraków, Olsztyn, Poznań, Słupsk, Sosnowiec, Starogard Gdański, Tczew, Warszawa, Wrocław",
        ]),
    ]},

    {"title": "Dur Brzuszny (Typhoid fever)", "blocks": [
        ("h", "Czym jest i jak się objawia?"),
        ("p", "Dur brzuszny to poważna choroba bakteryjna wywoływana przez Salmonella enterica serotyp Typhi (rzadziej Paratyphi A, B, C – tzw. dur rzekomy). Do zakażenia dochodzi głównie przez spożycie wody lub żywności zanieczyszczonej kałem osoby chorej lub nosiciela. Występuje endemicznie w wielu krajach o niższym standardzie sanitarnym, w tym w części Afryki, Azji i Ameryki Południowej."),
        ("p", "Okres inkubacji wynosi zwykle 6–30 dni."),
        ("p", "**Objawy to:**"),
        ("ul", [
            "wysoka, narastająca gorączka (często >39°C)",
            "bóle głowy i brzucha",
            "ogólne osłabienie",
            "zaparcia lub biegunka",
            "charakterystyczna wysypka plamisto-grudkowa („różyczka durowa”)",
            "w ciężkich przypadkach możliwe są perforacje jelit, krwawienia, sepsa i zgon.",
        ]),
        ("p", "Bez leczenia dur brzuszny może prowadzić do poważnych powikłań, dlatego profilaktyka — w tym szczepienie — ma istotne znaczenie."),
        ("h", "Czy szczepienie jest obowiązkowe?"),
        ("p", "Nie — Tanzania nie wymaga dowodu szczepienia przeciw durowi brzusznemu przy wjeździe. Szczepienie jest jednak silnie zalecane dla podróżujących w rejony o podwyższonym ryzyku, szczególnie jeśli:"),
        ("ul", [
            "planujesz jeść poza hotelami, w lokalnych barach ulicznych",
            "odwiedzasz małe miejscowości lub wioski",
            "podróżujesz poza utartymi szlakami turystycznymi",
            "przebywasz w Tanzanii dłużej niż 2–3 tygodnie",
        ]),
        ("h", "Kiedy się zaszczepić / schemat:"),
        ("p", "Dostępne są dwa główne rodzaje szczepionek:"),
        ("p", "**1. Inaktywowane, podawane domięśniowo (ViCPS)** – jedna dawka co najmniej 2 tygodnie przed wyjazdem."),
        ("ul", ["Ochrona utrzymuje się przez ok. 2–3 lata (zaleca się dawkę przypominającą co 3 lata przy utrzymującym się ryzyku)."]),
        ("p", "**2. Szczepionki doustne (żywe atenuowane, Ty21a)** – 3 kapsułki przyjmowane w odstępach co 2 dni, zakończenie cyklu co najmniej 1 tydzień przed wyjazdem."),
        ("ul", ["Ochrona ok. 5 lat (w Polsce dostęp ograniczony, częściej stosuje się formę iniekcyjną)."]),
        ("h", "Przeciwwskazania / uwagi bezpieczeństwa:"),
        ("p", "Szczepionkę inaktywowaną można stosować u osób od 2. roku życia, u kobiet w ciąży po indywidualnej ocenie lekarza. Szczepionka doustna — przeciwwskazana w immunosupresji, ciąży. Działania niepożądane są zwykle łagodne: ból w miejscu wkłucia, gorączka, przejściowe dolegliwości żołądkowo-jelitowe."),
        ("h", "Gdzie się szczepić i dokumentacja:"),
        ("p", "Szczepienie przeciw durowi brzusznemu wykonują punkty medycyny podróży, poradnie chorób zakaźnych oraz wybrane stacje sanitarno-epidemiologiczne w Polsce. Nie ma międzynarodowego certyfikatu (ICVP) dla tego szczepienia, ale warto mieć w książeczce szczepień wpis potwierdzający datę i rodzaj szczepionki."),
    ]},

    {"title": "Wirusowe zapalenie wątroby typu A (WZW A, Hepatitis A)", "blocks": [
        ("h", "Czym jest i jak się objawia?"),
        ("p", "Hepatitis A to wirusowa choroba przenoszona głównie przez skażoną żywność/wodę lub kontakt bezpośredni."),
        ("p", "**Objawy:** gorączka, złe samopoczucie, nudności, bóle brzucha, potem żółtaczka. U dzieci często bezobjawowo; u dorosłych może przebiegać ciężej, ale rzadko przechodzi w postać przewlekłą (zwykle samoograniczająca się)."),
        ("h", "Czy szczepienie jest obowiązkowe?"),
        ("p", "Nie jest obowiązkowe przy wjeździe do Tanzanii, ale jest zdecydowanie zalecane dla większości podróżnych, ponieważ ryzyko zakażenia przez zanieczyszczoną żywność/wodę w Tanzanii jest realne."),
        ("h", "Kiedy się szczepić / schemat:"),
        ("p", "Standardowy schemat: 2 dawki single-antigen w odstępie 6–12 miesięcy (pierwsza dawka daje znaczną ochronę już po ~2–4 tygodniach). Dla szybkiej ochrony można podać jedną dawkę przed wyjazdem (jeśli brakuje czasu — pierwsza dawka zabezpiecza częściowo), ale kompletna ochrona długoterminowa wymaga drugiej dawki. Dzieci ≥1 roku: szczepienie zalecane."),
        ("h", "Przeciwwskazania / efekty uboczne:"),
        ("p", "Szczepionka inaktywowana — bezpieczna. Możliwe miejscowe reakcje w miejscu wkłucia, ból, gorączka. Rzadkie reakcje alergiczne — warto omówić historię alergii z lekarzem przed szczepieniem."),
        ("h", "Gdzie się szczepić:"),
        ("p", "W gabinetach medycyny podróży, dużych przychodniach i niektórych centrach zdrowia. Warto zrobić to min. 2–4 tygodnie przed wyjazdem (dla pełniejszej odpowiedzi immunologicznej), a komplet serii przed dłuższym pobytem planować wcześniej."),
    ]},

    {"title": "Wirusowe zapalenie wątroby typu B (WZW B, Hepatitis B)", "blocks": [
        ("h", "Czym jest i jak się objawia?"),
        ("p", "Hepatitis B przenosi się przez kontakt z krwią, kontakty seksualne, użycie niesterylnych igieł lub przez zabiegi medyczne."),
        ("p", "**Objawy:** może przebiegać od bezobjawowego zakażenia do ostrej żółtaczki; u części zakażonych rozwija się przewlekłe zakażenie wątroby, prowadzące do marskości i raka wątroby."),
        ("h", "Czy szczepienie jest obowiązkowe?"),
        ("p", "Nie jest obowiązkowe do wjazdu do Tanzanii. Jest zalecane dla podróżnych, którzy mogą mieć ryzykowne kontakty (np. kontakt seksualny z nowymi partnerami, tatuaże, zabiegi medyczne, kontakty z krwią)."),
        ("h", "Kiedy się szczepić / schemat:"),
        ("p", "Standardowy schemat: 3 dawki (0, 1, 6 miesięcy) lub przyspieszony schemat w specjalnych sytuacjach (np. 0, 1, 2 miesiące + booster w 12 miesiącu). Istnieje też schemat 2-dawkowy dla niektórych preparatów (w zależności od produktu). Jeśli masz mało czasu, porozmawiaj z lekarzem o schemacie przyspieszonym."),
        ("h", "Przeciwwskazania / efekty uboczne:"),
        ("p", "Preparaty rekombinowane — bezpieczne; miejscowe reakcje i przejściowe objawy ogólne możliwe. Osoby z ciężkimi reakcjami alergicznymi na składniki powinny unikać – warto omówić wcześniej alergie z lekarzem."),
        ("h", "Gdzie się szczepić:"),
        ("p", "Gabinety szczepień, przychodnie medycyny podróży, kliniki medycyny rodzinnej. Warto planować z wyprzedzeniem (kompletna seria = ochrona długoterminowa)."),
    ]},

    {"title": "Tężec, błonica (Tetanus, Diphtheria) — szczepienia przeciw Tdap/Td", "blocks": [
        ("h", "Czym są i jak się objawiają?"),
        ("p", "**Tężec:** toksyna bakteryjna powodująca bolesne skurcze mięśni, sztywność, trudności w oddychaniu; przenoszony przez zakażenie ran."),
        ("p", "**Błonica:** zakażenie gardła/niosące toksynę; może prowadzić do trudności w oddychaniu, porażenia."),
        ("h", "Czy szczepienie jest obowiązkowe?"),
        ("p", "Nie jest obowiązkowe przy wjeździe do Tanzanii. Jednak aktualność szczepień rutynowych (Tdap/Td) jest standardową rekomendacją przed podróżą (szczególnie przy wyjazdach outdoorowych i ryzyku zranień). Rekomendowana jest dawka przypominająca co 10 lat."),
        ("h", "Kiedy się szczepić / schemat:"),
        ("p", "Jeśli nie masz dawki Tdap w dorosłym życiu — zrób ją przed wyjazdem. Jeśli Twoje ostatnie szczepienie tężcowe było >10 lat temu — przypomnienie (Td lub Tdap) jest wskazane."),
        ("h", "Przeciwwskazania / efekty uboczne:"),
        ("p", "Zwykle łagodne: ból, obrzęk w miejscu wkłucia, gorączka. Rzadkie poważne odczyny alergiczne. Porozmawiaj z lekarzem jeśli miałaś wcześniejsze poważne reakcje."),
        ("h", "Gdzie się szczepić:"),
        ("p", "Przychodnie podstawowej opieki, centra medycyny podróży. Zrób przypomnienie co najmniej kilka dni przed wyjazdem."),
    ]},

    {"title": "Polio (choroba Heinego-Medina, poliomyelitis)", "blocks": [
        ("h", "Czym jest i jak się objawia?"),
        ("p", "Polio to wirusowe zakażenie układu nerwowego, które może prowadzić do trwałego porażenia i zaburzeń motorycznych; przenoszone fekalno-oralnie, rzadziej przez kontakt. Nieleczone u niektórych osób może prowadzić do trwałego inwalidztwa."),
        ("h", "Czy szczepienie jest obowiązkowe?"),
        ("p", "Zwykle nie jest wymagane przy wjeździe do Tanzanii. Jednak sytuacja z polio jest dynamiczna — WHO i niektóre rządy mogą wymagać dowodu szczepienia (ICVP) od podróżnych przybywających z krajów z ryzykiem transmisji polio lub od osób opuszczających kraj, w którym występuje ryzyko eksportu poliowirusa."),
        ("h", "Kiedy się szczepić / schemat:"),
        ("p", "Dorośli, którzy ukończyli standardowe szczepienie w dzieciństwie, zwykle nie potrzebują dodatkowej dawki. Jednak jeśli wybierasz się do obszaru z ryzykiem polio, może być wymagany jednorazowy booster IPV podany 4 tygodnie do 12 miesięcy przed opuszczeniem kraju."),
        ("h", "Przeciwwskazania / efekty uboczne:"),
        ("p", "IPV (inaktywowana szczepionka) jest bezpieczna; możliwe miejscowe reakcje."),
        ("h", "Gdzie się szczepić i dokumentacja:"),
        ("p", "Jeśli wymagany jest certyfikat: szczepienia dokumentowane są w Międzynarodowym Świadectwie Szczepień (ICVP)."),
    ]},

    {"title": "Malaria", "blocks": [
        ("h", "Malaria w Tanzanii – co musisz wiedzieć przed wyjazdem!"),
        ("p", "Tanzania to kraj o niezwykłym bogactwie przyrodniczym – z dzikimi sawannami Serengeti, rajskimi plażami Zanzibaru i majestatycznym Kilimandżaro. Niestety, tropikalny klimat niesie ze sobą również zagrożenie chorobami przenoszonymi przez komary, a jedną z najpoważniejszych z nich jest malaria."),
        ("h", "Czym jest malaria?"),
        ("p", "Malaria to choroba pasożytnicza wywoływana przez pierwotniaki z rodzaju Plasmodium, przenoszone przez ukąszenia komarów z rodzaju Anopheles. Objawia się gorączką, dreszczami, bólami głowy i mięśni, a nieleczona może prowadzić do powikłań, a nawet śmierci. W Tanzanii występuje przede wszystkim malaria tropikalna (Plasmodium falciparum) – najgroźniejsza forma tej choroby."),
        ("h", "Ryzyko malarii w różnych regionach Tanzanii"),
        ("p", "Ryzyko zakażenia malarią w Tanzanii jest zróżnicowane geograficznie i sezonowo. Oto podział ryzyka w zależności od regionu:"),
        ("cols", [
            ("Wysokie ryzyko", [
                ("p", "**Nizinne rejony kontynentalnej Tanzanii**, szczególnie:"),
                ("ul", ["okolice jeziora Wiktorii", "Park Narodowy Serengeti", "rejon Ngorongoro", "Bagamoyo, Tanga, wybrzeże Oceanu Indyjskiego"]),
                ("p", "**Zanzibar i Pemba** – choć w ostatnich latach notuje się tam znaczny spadek zachorowań, wciąż istnieje ryzyko transmisji."),
            ]),
            ("Umiarkowane ryzyko", [
                ("p", "**Arusha i rejony wokół Kilimandżaro na niższych wysokościach (poniżej 1 800 m n.p.m.)**"),
            ]),
            ("Niskie ryzyko / praktycznie brak ryzyka", [
                ("p", "**Strefa górska Kilimandżaro (powyżej 2 000 m n.p.m.)** – ze względu na wysokość, temperatury i warunki środowiskowe komary nie występują w tej strefie."),
                ("p", "Podczas **samej akcji górskiej na Kilimandżaro** ryzyko zarażenia malarią jest **praktycznie zerowe**."),
            ]),
        ]),
        ("h", "Czy trzeba brać leki przeciwmalaryczne?"),
        ("p", "Decyzja o profilaktyce lekowej powinna być skonsultowana z lekarzem medycyny tropikalnej lub chorób zakaźnych, najlepiej 4–6 tygodni przed wyprawą. Ostateczna decyzja o braniu leków jednak zawsze będzie należała do Ciebie."),
        ("h", "Najczęściej stosowane leki profilaktyczne to:"),
        ("ul", [
            "**Malarone (atowakwon + proguanil)** – dobrze tolerowany, stosowany codziennie, również w krótkich wyjazdach.",
            "**Doxycyklina** – alternatywa, ale może powodować uczulenie na słońce.",
            "**Lariam (meflochina)** – stosowany rzadziej ze względu na możliwe działania uboczne o charakterze neuropsychiatrycznym.",
        ]),
        ("p", "Jeśli planujesz jedynie wejście na Kilimandżaro oraz krótki pobyt w Moshi lub Arushy, niektórzy lekarze mogą uznać, że ryzyko zakażenia malarią jest na tyle niskie, że nie wymaga pełnej profilaktyki lekowej. Ostateczna decyzja powinna jednak zawsze zostać podjęta indywidualnie, po konsultacji ze specjalistą."),
        ("h", "Ochrona przed komarami – kluczowa niezależnie od profilaktyki"),
        ("p", "Leki nie dają nigdy 100% ochrony, dlatego **mechaniczna ochrona przed ukąszeniami** pozostaje podstawą zapobiegania:"),
        ("check", [
            "Stosuj środki odstraszające komary (DEET minimum 50%, ikarydyna, PMD)",
            "Noś ubrania z długimi rękawami i nogawkami, najlepiej jasne",
            "Śpij pod moskitierą – szczególnie w niższych partiach Tanzanii",
            "Unikaj przebywania na zewnątrz o świcie i o zmierzchu – wtedy komary są najbardziej aktywne",
        ]),
        ("table", "Ryzyko malarii i rekomendacje wg etapu podróży", ["Ryzyko malarii", "Rekomendacja"], [
            ["Przylot (Arusha / Moshi)", "Niskie do umiarkowanego", "Repelenty + ewentualnie leki"],
            ["Noclegi przed wyprawą", "Niskie", "Moskitiera, repelenty"],
            ["Wyprawa górska (powyżej 2 000 m)", "Brak ryzyka", "Profilaktyka niepotrzebna"],
            ["Safari / Zanzibar po wyprawie", "Wysokie", "Profilaktyka lekowa + pełna ochrona"],
        ]),
        ("p", "Malaria może rozwinąć się nawet kilka tygodni po powrocie, a nieleczona – zwłaszcza malaria tropikalna (Plasmodium falciparum) – może prowadzić do powikłań, a nawet śmierci. Uwaga: objawy przypominają grypę lub zatrucie pokarmowe, co utrudnia szybkie rozpoznanie."),
        ("h", "Typowy przebieg malarii – fazy i objawy"),
        ("p", "**Faza początkowa** (7–14 dni po ukąszeniu):"),
        ("ul", [
            "Gorączka (często bardzo wysoka, powyżej 39°C)",
            "Dreszcze i silne poty",
            "Bóle głowy",
            "Bóle mięśni i stawów",
            "Osłabienie, zmęczenie",
            "Nudności, wymioty, biegunka (często mylone z zatruciem)",
        ]),
        ("p", "**Faza zaawansowana / powikłania** (szczególnie w malarii tropikalnej):"),
        ("ul", [
            "Zaburzenia świadomości, splątanie",
            "Drgawki",
            "Duszność",
            "Przyspieszone tętno",
            "Powiększenie śledziony lub wątroby",
            "Żółtaczka (objaw uszkodzenia wątroby lub rozpadu krwinek)",
            "Skąpomocz lub bezmocz (uszkodzenie nerek)",
            "Zapaść krążeniowa",
        ]),
        ("h", "Kiedy natychmiast zgłosić się do lekarza?"),
        ("ul", [
            "Jeśli po powrocie z Tanzanii (lub innego regionu tropikalnego) pojawi się gorączka lub inne objawy grypopodobne",
            "Jeśli objawy pojawią się nawet kilka tygodni po powrocie",
            "Jeśli stosowano leki przeciwmalaryczne, ale mimo to wystąpiły objawy – lekooporna malaria też się zdarza",
        ]),
        ("h", "Co zrobić w razie podejrzenia malarii?"),
        ("ul", [
            "Zgłoś lekarzowi, że byłeś w strefie malarycznej (to kluczowe!)",
            "Wykonaj test diagnostyczny (szybki test + badanie krwi – rozmaz cienki i gruby)",
            "Leczenie malarii musi być wdrożone jak najszybciej",
        ]),
        ("p", "Bez paniki, ale z rozwagą – malaria jest realnym zagrożeniem, ale dzięki odpowiedniej wiedzy i przygotowaniu można jej skutecznie zapobiec. Zadbaj o zdrowie przed podróżą, by w pełni cieszyć się przygodą życia!"),
    ]},
]

# „Praktyczne szczegóły" — kroki (pogrubiony początek + reszta)
PRAKTYCZNE = [
    ("Zrób wizytę w poradni medycyny podróży", " na 6–8 tygodni przed wyjazdem (jeśli to możliwe). Pozwala to na: ocenę Twojego statusu szczepień, rozpoczęcie serii dawek wymagających czasu (Hep B, Hep A), i wydanie wymaganych dokumentów (ICVP). Jeśli masz mniej czasu, rozpocznij jak najszybciej — niektóre szczepienia mają przyspieszone schematy."),
    ("Zabierz ze sobą", ": kartę szczepień, dowód szczepień żółtej febry (jeśli dotyczy), kopie dokumentów, listę przyjmowanych leków i schorzeń (ważne przy przeciwwskazaniach do żywych szczepionek)."),
    ("Gdzie się zaszczepić:", " centra medycyny podróży, duże przychodnie, sanepid, autoryzowane ośrodki szczepień żółtej febry (dla ICVP). W Polsce i Europie listy punktów znajdziesz na stronach krajowych instytucji zdrowia (lub przez lokalne przychodnie)."),
    ("Dowód i ważność:", " po szczepieniu żółtej febry otrzymasz ICVP z datą — minimalny czas od szczepienia do podróży to 10 dni (dla uznania ochrony). Dla polio — niektóre kraje wymagają wpisu do ICVP dla osób opuszczających kraj z potwierdzonym ryzykiem — więc sprawdź status kraju przed wylotem i przy planie tranzytów."),
    ("Grupy ryzyka:", " kobiety w ciąży, kobiety karmiące, dzieci, osoby immunosupresyjne — wymagają odniesienia do lekarza; szczepionki żywe (np. żółta febra) mają szczególne ograniczenia."),
]

APTECZKA_INTRO = (
    "Na wyprawach nauczyliśmy się, że to właśnie apteczka potrafi uratować dzień – "
    "a czasem i całą przygodę. Z pozoru drobiazgi, takie jak ból głowy, obtarte stopy "
    "czy problemy żołądkowe, w górach mogą zamienić się w spore wyzwanie. Dlatego "
    "przygotowaliśmy listę leków i podstawowych środków medycznych, które sami "
    "zabieramy na Kilimandżaro i które polecamy każdemu uczestnikowi wyprawy. Możesz "
    "ją pobrać i sprawdzić, czy Twoja apteczka jest gotowa."
)
PORADNIK_INTRO = (
    "Ten poradnik stworzyliśmy z myślą o osobach, które – tak jak my – ruszają w góry "
    "z ekscytacją, ale też ze świadomością, że nie wszystko da się przewidzieć. Podczas "
    "trekkingu mogą zdarzyć się drobne urazy, osłabienie czy pierwsze objawy choroby "
    "wysokościowej. W takich chwilach liczy się szybka reakcja i spokój. Zebraliśmy "
    "tutaj najprostsze i najpraktyczniejsze wskazówki, które pomogą Ci poradzić sobie w "
    "trudniejszych momentach, zanim dotrzesz do profesjonalnej pomocy. To nie jest "
    "podręcznik medycyny, ale coś w rodzaju „ściągi” w plecaku."
)

# Linki do PDF (Google Drive) — "#" = jeszcze nie podpięte.
APTECZKA_PDF = "https://drive.google.com/file/d/1Ko1rsI6lLInJTXVvYoUGMfkEgsj0mTON/view"
PORADNIK_PDF = "https://drive.google.com/file/d/1b_fHNb2OdpTX_1fflIdodpjmDxHWLQlz/view"
