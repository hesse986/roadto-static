# -*- coding: utf-8 -*-
"""
RoadTo — treść strony „Safari i atrakcje".

Każda atrakcja = rozwijana sekcja (akordeon). Edytujesz tu, potem
`python3 build_site.py`. Wbudowane w generator, więc nie znika przy regeneracji.

Struktura:
  SAFARI_ATTRACTIONS = [ {title, intro:[akapity], tip, info:[(etykieta, tekst)...]} ]
"""

SAFARI_INTRO = (
    "Kilimandżaro to dopiero początek. Wokół Moshi i Arushy — a także nieco dalej, "
    "nad oceanem — czeka cała Tanzania: wodospady, gorące źródła, dziki wulkan i "
    "rajskie plaże. Poniżej kilka miejsc, które warto połączyć z wyprawą na dach Afryki."
)

SAFARI_ATTRACTIONS = [
    {
        "title": "Mount Meru — mniej znana siostra Kilimandżaro",
        "intro": [
            "W cieniu swojego słynnego sąsiada stoi góra, którą wielu nazywa „cichą siostrą Kilimandżaro”. Mount Meru ma 4566 metrów i jest jednym z najpiękniejszych wulkanów w Afryce.",
            "Trasa na szczyt prowadzi przez Arusha National Park — zaczynasz w tropikalnym lesie, gdzie spotkasz pawiany i żyrafy, a kończysz w surowym, skalistym krajobrazie z widokiem na chmury. To wspinaczka, która daje wszystko: przyrodę, wyzwanie i emocję.",
            "Pierwszy nocleg w Miriakamba Hut to spotkanie z ciszą. Drugiego dnia wspinasz się do Saddle Hut, skąd o północy rusza atak szczytowy. Droga jest stroma, ale każdy krok wynagradza wschód słońca nad Kilimandżaro — to moment, który trudno opisać słowami.",
        ],
        "tip": "Nawet jeśli byłeś już na Kilimandżaro, Meru zaskoczy Cię dzikością i spokojem.",
        "info": [
            ("Jak się dostać", "Wejście przez Momella Gate w Arusha NP. 1 godz. z miasta."),
            ("Koszt", "Trekking 3–4 dni: 350–500 USD (z agencją). Park fee: 50 USD/dzień."),
            ("Warto wiedzieć", "Wymagany przewodnik i ranger. Idealny trening przed Kilimandżaro."),
        ],
    },
    {
        "title": "Zanzibar — przyprawy, słońce i oddech oceanu",
        "intro": [
            "Po tygodniach wędrówki po górach i sawannach przychodzi czas na nagrodę. Zanzibar to inny świat — pachnący cynamonem, goździkami i oceanem. Tu wszystko toczy się wolniej, jakby czas przestał gonić.",
            "Białe plaże Nungwi i Kendwa przypominają pocztówki. Ocean zmienia kolor od mlecznego błękitu po turkus. Na południu, w Paje, surferzy łapią wiatr, a miejscowi łowią ośmiornice w przyboju.",
            "W sercu wyspy leży Stone Town — labirynt wąskich uliczek, arabskich drzwi i zapachu przypraw. Tu można zgubić się z przyjemnością.",
            "Nie zapomnij odwiedzić farm przypraw — pieprz, wanilia, kardamon, goździki. Każdy liść, każda gałązka pachnie inaczej. Zanzibar naprawdę smakuje powietrzem.",
            "A wieczorem? Zachód słońca nad plażą i grill z owocami morza — proste, piękne życie.",
        ],
        "tip": "To najlepsze miejsce, by dać ciału odpocząć po górach. Zasłużyłeś.",
        "info": [
            ("Jak się dostać", "Lot z Arusha lub Moshi (1 godz.) albo prom z Dar es Salaam (ok. 2 godz.)."),
            ("Koszt", "Lot 100–150 USD. Prom 35 USD. Taxi z lotniska: 10–30 USD."),
            ("Warto wiedzieć", "Waluta – szyling tanzański. Napiwki: 5–10%. Warto odwiedzić rezerwat Jozani (małpy red colobus) i wyspę Prison Island."),
        ],
    },
    {
        "title": "Wodospad Materuni — kawa, chłód i widok na Kilimandżaro",
        "intro": [
            "Kiedy schodzisz z Kilimandżaro, w głowie ciągle dudni rytm górskiego oddechu. A potem trafiasz tu – do Materuni, maleńkiej wioski ukrytej pośród zielonych wzgórz. Powietrze jest ciężkie od zapachu kawy i wilgoci, a z oddali słychać grzmot wody spadającej z wysokości siedemdziesięciu metrów. To właśnie tu natura uczy cię, że cisza może mieć własny głos.",
            "Ścieżka do wodospadu prowadzi przez pola bananowców i kawowce, które wyglądają jak zielone płuca gór. Dzieci machają z drogi, kobiety suszą ziarna na matach, a z małych domków słychać śmiech i muzykę. Po kilkunastu minutach marszu las zaczyna gęstnieć, powietrze staje się chłodniejsze, a ziemia miękka od mchu.",
            "Nagle ścieżka kończy się – i stajesz przed ścianą wody, która spada z krateru wulkanu niczym srebrny welon. Krople unoszą się w powietrzu jak mgła, a tęcza, która tańczy w słońcu, wygląda jak znak błogosławieństwa od samego Kili.",
            "W okolicy wodospadu działa niewielka społeczność Chagga, która z pokolenia na pokolenie przekazuje tradycję uprawy kawy. To nie jest komercyjny pokaz – to szczere, radosne spotkanie z ludźmi, którzy autentycznie kochają to, co robią. Wypalisz tu swoje własne ziarna, utłuczesz je w drewnianym moździerzu i zaparzysz filiżankę czarnego złota.",
            "Według lokalnej legendy, duch przodka strzeże tego miejsca. Mówi się, że jeśli wejdziesz do wody z czystym sercem, twoje zmęczenie zostanie „zmyte” i wrócisz z nową siłą. Czy to prawda? Trudno powiedzieć — ale wielu turystów twierdzi, że właśnie po kąpieli w Materuni odzyskali energię po wspinaczce.",
            "To też idealne miejsce na spokój i refleksję — nie znajdziesz tu tłumów jak w parkach safari. Tylko szum wody, zieleń i uczucie, że przez chwilę jesteś częścią czegoś starszego niż człowiek.",
        ],
        "tip": "Jeśli masz szczęście, trafisz tu, gdy chmury odsłaniają Kilimandżaro. Widok szczytu zza wodospadu to obraz, którego nie zapomnisz.",
        "info": [
            ("Jak się dostać", "Z Moshi ok. 15 km, 40–50 minut drogi. Można dojechać boda-bodą (motocyklem, ok. 10–15 USD w obie strony) lub w ramach jednodniowej wycieczki z agencją (np. 4Challenge)."),
            ("Koszt", "Wstęp + lokalny przewodnik: ok. 10–15 USD. Warsztaty kawowe dodatkowo 5–10 USD."),
            ("Warto wiedzieć", "Zabierz gotówkę (brak terminali). W weekendy bywa tłoczno, ale w tygodniu można mieć wodospad prawie dla siebie. Nie zapomnij ręcznika i lekkiej kurtki — w dolinie jest chłodniej niż w Moshi."),
        ],
    },
    {
        "title": "Gorące źródła Kikuletwa — naturalne spa w sercu sawanny",
        "intro": [
            "Między Moshi a Arusha ciągnie się pas suchej sawanny, poprzecinany korytami wyschniętych rzek. Trudno uwierzyć, że w tym krajobrazie kryje się jedno z najbardziej rajskich miejsc Tanzanii — Kikuletwa Hot Springs, znane też jako Chemka.",
            "Z oddali widać tylko drzewa i kurz. A potem, jak fatamorgana, pojawia się oaza – woda krystaliczna jak szkło, przezroczysta na kilka metrów w głąb, mieniąca się turkusem. Dookoła palmy, figowce, konary zwisające nad wodą, z których odważni skaczą jak Tarzan.",
            "Po trekkingu na Kilimandżaro to miejsce działa jak restart całego ciała. Zanurzasz się, zamykasz oczy i słyszysz tylko szum liści. Woda ma około 27°C – idealna temperatura, by odpocząć i rozluźnić mięśnie. To najlepsze „spa” w Tanzanii – bez murów, bez muzyki relaksacyjnej, za to z naturą w roli głównej.",
            "Miejsce jest popularne zarówno wśród turystów, jak i lokalnych rodzin. W weekendy słychać śmiech, rozmowy i muzykę z głośników — Tanzania w najczystszej postaci. W tygodniu natomiast możesz mieć całą oazę dla siebie.",
            "Masajowie wierzą, że duch ziemi ukrył tu źródło siły dla tych, którzy wracają z gór. Mówią, że kto zanurzy się w Kikuletwa, odzyska witalność i spokój ducha. Legenda czy nie – wielu przysięga, że to działa.",
            "Warto zostać tu dłużej – zabrać lunch, rozłożyć ręcznik i po prostu cieszyć się ciszą. Gdy słońce prześwituje przez gałęzie, a woda odbija światło jak lustro, trudno uwierzyć, że to miejsce istnieje naprawdę.",
        ],
        "tip": "Weź maskę do snorkelingu – w czystej wodzie widać maleńkie rybki, które lubią „podgryzać” palce u nóg.",
        "info": [
            ("Jak się dostać", "Z Moshi ok. 1 godzina jazdy (35 km). Do Boma Ng’ombe można dojechać dala-dalą, a stamtąd boda-bodą (ok. 5–10 USD). Agencje często łączą wizytę w Kikuletwa z Materuni."),
            ("Koszt", "Wstęp: ok. 10 USD. Parking i toalety dostępne. Na miejscu bar z napojami i przekąskami."),
            ("Warto wiedzieć", "Brak przebieralni – duży ręcznik to must have. Woda głęboka (2–6 m). Najlepiej przyjechać rano, gdy słońce jest łagodne, a tłumów jeszcze nie ma."),
        ],
    },
]
