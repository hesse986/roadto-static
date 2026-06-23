# -*- coding: utf-8 -*-
"""
RoadTo — treść strony „Safari i atrakcje".

Każda atrakcja = rozwijana sekcja (akordeon). Edytujesz tu, potem
`python3 build_site.py`. Wbudowane w generator, więc nie znika przy regeneracji.

Struktura:
  SAFARI_ATTRACTIONS = [ {title, intro:[akapity], tip, info:[(etykieta, tekst)...]} ]
Kolejność jak w oryginale (Framer).
"""

SAFARI_INTRO = (
    "Kilimandżaro to dopiero początek. Wokół Moshi i Arushy — a także nieco dalej, "
    "nad oceanem — czeka cała Tanzania: wulkany, jeziora w kraterach, gorące źródła, "
    "parki pełne zwierząt i rajskie plaże. Poniżej miejsca, które warto połączyć "
    "z wyprawą na dach Afryki."
)

SAFARI_ATTRACTIONS = [
    {
        "title": "Jezioro Chala — błękitne oko wulkanu na granicy dwóch światów",
        "intro": [
            "Na wschodnim krańcu Tanzanii, tuż przy granicy z Kenią, leży jezioro, które wygląda jak klejnot ukryty w kraterze — Jezioro Chala. To wulkaniczne cudo ma kolor, który trudno opisać jednym słowem: czasem turkus, czasem szafir, a czasem zielone szkło. Zmienia się jak nastroje pogody.",
            "Gdy stoisz na krawędzi krateru i patrzysz w dół, czujesz, jak ziemia oddycha. Powietrze pachnie pyłem i suchą trawą, a echo niesie odgłos ptaków. W oddali widać sylwetkę Kilimandżaro, a w dole taflę wody tak spokojną, że wydaje się, jakby czas naprawdę się zatrzymał.",
            "To miejsce ma w sobie spokój i tajemnicę. Woda jeziora pochodzi z podziemnych źródeł Kilimandżaro i jest tak czysta, że odbija wszystko jak lustro. Wokół krateru wije się ścieżka, którą można zejść aż nad brzeg — strome zejście, ale nagroda warta wysiłku.",
            "Lokalne plemię Chagga wierzy, że w jeziorze mieszka duch kobiety, która z rozpaczy po utraconej miłości rzuciła się w jego wody. Mówią, że dlatego jezioro ma kolor jej oczu. I faktycznie — gdy słońce zachodzi, powierzchnia nabiera barwy turkusu z nutą melancholii.",
            "Na brzegu działa niewielki Chala Safari Camp — miejsce, gdzie można napić się zimnego piwa, obserwując pawiany i małpy colobus, które grasują po okolicy. Nocą słychać tu świerszcze i wiatr, a nad wodą pojawia się tysiąc gwiazd.",
            "To idealne miejsce na jednodniowy wypad po Kilimandżaro albo na spokojny weekend z dala od tłumów. Nie ma tu zasięgu, nie ma pośpiechu — tylko natura i cisza, która koi.",
        ],
        "tip": "Zabierz lornetkę — ptaki w Chala to uczta dla każdego, kto lubi obserwacje przyrody.",
        "info": [
            ("Jak się dostać", "Z Moshi ok. 1,5 godziny (ok. 55 km). Dojazd boda-bodą lub samochodem 4x4 (droga częściowo szutrowa). Możliwy transport z agencji."),
            ("Koszt", "Wstęp ok. 10 USD. Kemping i nocleg w Chala Safari Camp od 30 USD/noc."),
            ("Warto wiedzieć", "Nie kąp się daleko od brzegu – dno gwałtownie opada. Weź wodę i przekąski – w okolicy brak sklepów."),
        ],
    },
    {
        "title": "Ol Doinyo Lengai & Jezioro Natron — kraina ognia, popiołu i soli",
        "intro": [
            "Tam, gdzie kończą się asfaltowe drogi, a ziemia staje się czerwona jak ogień, zaczyna się inny świat. Ol Doinyo Lengai, „Góra Boga” Masajów, góruje nad horyzontem niczym strażnik czasu. To jedyny aktywny wulkan w Tanzanii i zarazem najbardziej niezwykły – jego lawa jest zimna w dotyku i ma kolor popiołu.",
            "U stóp góry rozlewa się Jezioro Natron — różowe, błyszczące i nierealne. Woda jest tak zasadowa, że przypomina płynną sól. W jej pobliżu nie ma drzew, nie ma cienia — tylko cisza, która dudni w uszach. To królestwo flamingów, które właśnie tu zakładają największe kolonie lęgowe w Afryce.",
            "Trekking na Ol Doinyo Lengai to przygoda dla odważnych. Start o północy, wejście po ciemku przy świetle latarek. Szlak stromy, kamienisty, wymagający, ale nagroda? Wschód słońca nad Jezioro Natron – morze chmur, różowa tafla jeziora i widok, który zostaje w głowie na zawsze.",
            "Masajowie wierzą, że szczyt jest miejscem, gdzie bóg Eng’ai zsyła błogosławieństwo. Czasem, gdy wulkan „kicha” popiołem, mówią, że to jego śmiech. Wspinaczka tutaj to nie tylko wyzwanie fizyczne, ale też duchowe.",
            "W dolinie Natron warto odwiedzić wodospady Engare Sero – ukryte między skałami, dają wytchnienie po piekielnym upale. Woda jest tu chłodna, a kąpiel po wspinaczce – jak chrzest dla ciała.",
        ],
        "tip": "Zabierz okulary przeciwsłoneczne, chustę i mnóstwo wody. To jedno z najbardziej surowych miejsc w Tanzanii, ale też jedno z najbardziej magicznych.",
        "info": [
            ("Jak się dostać", "Z Mto wa Mbu do Lake Natron ok. 5 godzin jazdy 4x4. Z Arusha ok. 7 godzin. Najłatwiej zorganizować wyprawę z agencją (transport, nocleg, przewodnik)."),
            ("Koszt", "Wstęp do rejonu Natron ok. 10 USD, przewodnik Masaj – 10–20 USD. Trekking na Lengai – 100–150 USD (z nocnym wejściem)."),
            ("Warto wiedzieć", "Koniecznie buty trekkingowe i zapas wody. Weź powerbank – brak prądu i zasięgu. Najlepszy czas: czerwiec–październik (pora sucha)."),
        ],
    },
    {
        "title": "Arusha National Park — Tanzania w miniaturze",
        "intro": [
            "Zaledwie godzinę drogi od miasta Arusha leży park, który potrafi zaskoczyć. Arusha National Park to mały, ale różnorodny mikrokosmos Tanzanii: od sawanny, przez jeziora, po las deszczowy i górskie szczyty.",
            "Gdy wjedziesz przez bramę Momella, krajobraz zmienia się z każdą minutą. Z lewej strony migoczą jeziora Momella, w których odbijają się chmury i flamingi, z prawej wznosi się majestatyczne Mount Meru, a w środku — las, gdzie żyją żyrafy, bawoły i colobusy z czarno-białym futrem.",
            "Nie zobaczysz tu lwów, ale za to możesz przeżyć coś wyjątkowego: safari piesze. Uzbrojony ranger prowadzi cię ścieżką, po której przed chwilą przeszła żyrafa. Słyszysz każdy szelest, każdy śpiew ptaka — to nie przejazd w jeepie, to wejście do świata przyrody bez filtra.",
            "Park jest też bramą na Mount Meru — dla wielu wspinaczy to pierwszy etap przed Kilimandżaro. Ale nawet bez trekkingu, samo spojrzenie na górę z punktu widokowego Ngurdoto Crater potrafi przyprawić o dreszcz.",
            "Woda w jeziorach mieni się różnymi kolorami — od niebieskiego po zielony, w zależności od minerałów i światła. To miejsce, które zmienia się z każdą godziną dnia.",
        ],
        "tip": "Zabierz aparat i cierpliwość – tu nie chodzi o ilość zwierząt, tylko o bliskość natury.",
        "info": [
            ("Jak się dostać", "Z Arusha ok. 45 min jazdy. Dojazd możliwy prywatnie lub z agencją."),
            ("Koszt", "Wstęp: 50 USD. Safari piesze: ok. 30 USD z rangerem."),
            ("Warto wiedzieć", "Park czynny cały rok. W porze deszczowej (marzec–maj) las jest soczyście zielony. Napiwki dla rangersów: 10 USD/dzień."),
        ],
    },
    {
        "title": "Lake Manyara — las, jezioro i lwy na drzewach",
        "intro": [
            "Witaj w świecie, w którym sawanna spotyka wodę. Lake Manyara National Park to miejsce pełne kontrastów: z jednej strony gęsty las figowców, z drugiej bezkresne jezioro, w którym odbija się niebo.",
            "Kiedy wjeżdżasz do parku, pierwsze co czujesz to zapach — mieszanka wilgoci, błota i kwiatów. Potem widzisz żyrafy, które przemykają między drzewami jak duchy. Dalej — słonie brodzące w błocie, stada bawołów i hipopotamy, które chrapią w wodzie jakby śniły o spokojnym świecie.",
            "Ale Manyara słynie z jednego: lwów, które wspinają się na drzewa. To rzadki widok — ogromne koty leżące na gałęziach akacji, zwisające łapami jak kot domowy na parapecie. To obraz, którego nie da się zapomnieć.",
            "Warto zatrzymać się też przy gorących źródłach Maji Moto, gdzie woda bąbelkuje w ziemi. A jeśli lubisz obserwować ptaki — tu znajdziesz ich setki: pelikany, ibisy, bociany i tysiące flamingów. Park jest mały, ale pełen życia.",
            "W ciągu jednego dnia zobaczysz więcej niż w niejednym dużym parku.",
        ],
        "tip": "Najlepsze światło do zdjęć jest po południu, gdy słońce odbija się w jeziorze.",
        "info": [
            ("Jak się dostać", "Z Arusha ok. 2 godziny jazdy (125 km). Agencje oferują safari 1-dniowe."),
            ("Koszt", "Wstęp: 50 USD. Safari z przewodnikiem – 150–180 USD."),
            ("Warto wiedzieć", "Pora sucha (czerwiec–październik) to najlepszy czas na lwy. Napiwki: 10–15 USD/dzień."),
        ],
    },
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
