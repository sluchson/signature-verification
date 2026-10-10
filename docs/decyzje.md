# Dziennik decyzji

Wpisy z sierpnia dopisane później, daty przybliżone.

## Sierpień 2026 — Zbiór danych: CEDAR
- trenuję i testuję na CEDAR
- 55 osób, każda ma 24 prawdziwe podpisy i 24 podrobione, razem 2640 obrazów
- często używany w artykułach, więc mogę porównać wyniki z innymi
- pobrany z Kaggle „shreelakshmigp/cedardataset”, bo oficjalna strona cedar.buffalo.edu często nie działa
- Brazilian PUC-PR odpadł: trzeba pisać maila do autorów, tylko 60 ze 168 osób ma fałszerstwa, format plików nieopisany, w nowszych pracach prawie nieużywany
- BHSig260 łatwo pobrać z Kaggle, może na końcu jako drugi zbiór do sprawdzenia modelu, jeśli starczy czasu

## Sierpień 2026 — Rodzaje fałszerstw
- fałszerstwa wykwalifikowane (skilled): są w CEDAR, ktoś ćwiczył podrabianie podpisu
- fałszerstwa losowe (random): robię sam, łącząc w parę podpis jednej osoby z podpisem innej
- tak samo robili Bromley i in. (1993), przypis 1 na str. 741
- nie testuję fałszerstw prostych, bo ani CEDAR, ani BHSig260 ich nie mają
- opisać to w rozdz. 3 jako ograniczenie pracy

## Sierpień 2026 — Podział danych niezależny od autora (writer-independent)
- każda osoba jest tylko w jednym zbiorze: treningowym, walidacyjnym albo testowym
- model nie widzi w treningu żadnego podpisu osób testowych
- tylko wtedy wynik na teście pokazuje, jak model działa dla nowych osób
- w niektórych artykułach EER na CEDAR jest bliski 0%, podejrzewam, że czasem przez te same osoby w treningu i teście
- to na razie przypuszczenie, przed rozdz. 5 znaleźć artykuł, który to potwierdza

## Sierpień 2026 — Model: sieć syjamska z contrastive loss
- dwie takie same podsieci CNN ze wspólnymi wagami
- trening funkcją straty kontrastowej (contrastive loss)
- wejście: obrazy podpisów
- sieć syjamską do podpisów zaproponowali Bromley i in. (1993)
- contrastive loss pochodzi od Hadsell i in. (2006)
- SigNet (Dey i in., 2017) robi podobnie na CEDAR, więc mam z czym porównać wyniki

## Sierpień 2026 — Narzędzia i ocena
- Python, OpenCV, PyTorch
- środowisko działa: Python 3.13.15, PyTorch 2.11.0+cu128, RTX 4070 Laptop
- miary: FAR, FRR, EER
- próg decyzyjny wybieram na zbiorze walidacyjnym, nie testowym

## Sierpień 2026 — Dobór hiperparametrów
- ablation study: zmieniam jeden parametr naraz, reszta bez zmian
- zawsze ten sam seed, wyniki zapisuję do CSV
- do sprawdzenia: margines w contrastive loss, rozmiar embeddingu, liczba warstw
- każdą wartość w pracy chcę uzasadnić wynikiem eksperymentu

## Sierpień 2026 — GUI (do ustalenia)
- opcje: Tkinter / PyQt (aplikacja okienkowa) albo Streamlit / Gradio (przeglądarka, szybciej się robi)
- zapytać promotora, co jest akceptowane, zanim zacznę

## Wrzesień 2026 — Skala szarości i jeden rozmiar
- każdy obraz przy wczytywaniu: `convert("L")` i zmiana rozmiaru na stały
- w `full_org` 1095 różnych rozmiarów na 1320 plików
- w `full_forg` 1006 różnych rozmiarów na 1320 plików
- różne tryby kolorów: `full_org` RGBA i L, `full_forg` P i RGBA
- sieć potrzebuje tego samego rozmiaru i tej samej liczby kanałów
- kolor nic nie mówi o kształcie podpisu, jeden kanał wystarczy
- żaden obraz nie ma przezroczystości (kanał alfa pełny), więc zamiana na L nic nie gubi
- notebook `01_eksploracja_danych.ipynb`

## Wrzesień 2026 — Proporcje wejścia sieci
- wejście ma być prostokątem szerszym niż wyższym, nie kwadratem
- mediana rozmiaru: `full_org` 577×349 px, `full_forg` 576×336 px, proporcja ok. 1,65–1,7:1
- szerokości od 264 do 888 px, więc trochę zniekształcenia i tak będzie
- np. ok. 220×140 zamiast 128×128, dokładny rozmiar w rozdz. 4
- SigNet skaluje wszystkie obrazy do 155×220 (wys. × szer.), proporcja ok. 1,42:1, czyli też prostokąt
- notebook `01_eksploracja_danych.ipynb`

## Wrzesień 2026 — Przycinanie do samego podpisu
- przed zmianą rozmiaru przycinam obraz do prostokąta z samym podpisem (bounding box)
- prostokąt wokół podpisu zajmuje średnio ok. 60% obrazu (60,1% w `full_org`, 58,6% w `full_forg`), reszta to tło
- bez przycięcia duża część małego wejścia sieci to byłoby puste tło
- SigNet nie przycina, skaluje cały obraz do 155×220 (rozdz. 2.1)
- Hafemann i in. 2017 też nie przycinają: wyśrodkowują podpis na dużym tle według środka masy i dopiero skalują (rozdz. 3.3)
- czyli przycinanie to mój własny wybór, w rozdz. 4 porównać wyniki z przycinaniem i bez
- oba artykuły odwracają kolory (tło = 0, podpis jasny), rozważyć to samo
- notebook `01_eksploracja_danych.ipynb`

## Wrzesień 2026 — Rozmiar obrazu zdradza autora, prosty test porównawczy
- 85,4% rozmiarów w `full_org` i 78,1% w `full_forg` występuje tylko u jednej osoby
- po samym rozmiarze obrazu prawie zawsze da się zgadnąć, kto się podpisał
- dlatego ujednolicenie rozmiaru jest potrzebne też po to, żeby sieć nie uczyła się tego skrótu
- pliki sprawdzone (MD5 + `PIL.Image.verify()`): brak uszkodzeń i duplikatów
- test korelacji pikseli (128×128) na wszystkich 5280 parach:
  prawdziwy–prawdziwy 0,158 ± 0,090, prawdziwy–fałszerstwo 0,104 ± 0,069, różne osoby 0,083 ± 0,061
- EER: 38,0% dla fałszerstw wykwalifikowanych, 32,3% dla różnych osób, czyli metoda myli się w ok. 1/3 przypadków
- wcześniejszy test na 10 parach (0,146 = 0,146) dawał mylący wniosek, że metoda w ogóle nie odróżnia fałszerstw
- to będzie metoda bazowa do porównania z siecią w rozdz. 5
- powtórzyć test po usunięciu tła (Otsu), żeby sprawdzić, ile z wyniku dla fałszerstw wynika z tła
- notebook `01_eksploracja_danych.ipynb`

## Wrzesień 2026 — Podział osób i pary losowe
- 55 osób: 35 trening, 10 walidacja, 10 test
- losowanie z seedem 42, zapis w `data/writer_split.json`
- pary losowe: każdy z 24 prawdziwych podpisów osoby + losowy prawdziwy podpis innej osoby z tej samej grupy
- seed 123, 24 pary na osobę, razem 1320, zapis w `data/random_forgery_pairs.csv`
- pary losowe tylko w obrębie tej samej grupy, żeby nie przemycić osób testowych do treningu
- 24 pary losowe na osobę, bo tyle samo jest par z fałszerstwami wykwalifikowanymi
- stałe seedy, więc za każdym razem wychodzi to samo
- notebook `01_eksploracja_danych.ipynb`

## Wrzesień 2026 — Pliki z parami do treningu
- trzy pliki CSV: `genuine_pairs.csv`, `skilled_forgery_pairs.csv`, `random_forgery_pairs.csv`
- te same kolumny wszędzie: `split`, `writer_a`, `file_a`, `writer_b`, `file_b`, `label`
- 2640 par „ta sama osoba” i 2640 par „nie ta sama osoba” (1320 wykwalifikowanych + 1320 losowych)
- klasy po równo 1:1
- kolumna `split` pilnuje podziału na trening / walidację / test
- w rozdz. 4 łączę je i wczytuję do `Dataset` w PyTorch
- notebook `01_eksploracja_danych.ipynb`

## Wrzesień 2026 — Tło zdradza, co jest fałszerstwem
- mediana jasności tła: `full_org` 234–245 (średnio 239,8), `full_forg` 249–255 (średnio 253,5)
- zakresy się nie nakładają, 513 z 1320 fałszerstw ma tło idealnie białe, prawdziwe żadne
- jeden próg (ok. 247) oddziela wszystkie prawdziwe podpisy od fałszerstw bez patrzenia na podpis
- bez poprawki sieć mogłaby rozpoznawać fałszerstwa wykwalifikowane po tle, a nie po kształcie
- nie binaryzuję, więc różnica w tle trafiłaby do sieci
- decyzja: usunięcie tła metodą Otsu, tło = 255, atrament zostaje w skali szarości (jak Hafemann i in. 2017, rozdz. 3.3)
- po przetworzeniu powtórzyć test `background_level` i sprawdzić, czy różnica zniknęła
- wg Kalera i in. (str. 1341) oryginał był w 8-bitowej skali szarości, a w kopii z Kaggle są też RGBA i P, czyli kopia była konwertowana
- nie wiadomo, czy różnica tła pochodzi z oryginalnego skanowania, czy z tej konwersji, poprawka Otsu działa w obu przypadkach
- notebook `01_eksploracja_danych.ipynb`

## Październik 2026 — Błąd w wybieraniu plików osoby (naprawiony)
- funkcja `get_files_for_writer` szukała wzorcem `*{id}_*`, więc dla osób 1–9 łapała też pliki osób 11, 21, 31 itd.
- w starych plikach par: 359 par „ta sama osoba” z dwóch różnych osób, 173 złe pary z fałszerstwami, 6 par losowych z tą samą osobą
- część par zawierała pliki osób z innego zbioru (np. testowego w treningowym), czyli łamała podział writer-independent
- poprawka: wzorzec `*_{id}_*` + `assert`, że każda osoba ma dokładnie 24 pliki
- pary wygenerowane ponownie (te same seedy), dodana komórka sprawdzająca każdą parę: 0 błędów
- test korelacji pikseli policzony ponownie
- notebook `01_eksploracja_danych.ipynb`

## Październik 2026 — Przygotowanie obrazów (`src/preprocessing.py`)
- kolejność: skala szarości → usunięcie tła metodą Otsu (tło = 255, atrament w skali szarości) → przycięcie do podpisu → ujednolicenie ciemności atramentu → dopasowanie do 128×256 bez rozciągania (białe dopełnienie)
- po Otsu mediana obrazu = 255 we wszystkich 2640 obrazach, różnica tła zniknęła
- progi Otsu: prawdziwe 170–210, fałszerstwa 174–226, nakładają się
- proporcja po przycięciu: mediana ok. 2,1; skrajne 0,63 (osoba 27) i 10,57 (osoba 52) to prawdziwe kształty podpisów, dlatego bez rozciągania
- rozmiar 128×256, bo proporcja 2:1 jest blisko mediany 2,1
- notebook `02_przygotowanie_obrazow.ipynb`

## Październik 2026 — Atrament zdradza fałszerstwo
- przed poprawką: EER po samej jasności atramentu 21,1% (mediana różnicy w parze: 3 prawdziwy–prawdziwy, 18 prawdziwy–fałszerstwo)
- przyczyna: prawdziwe podpisy jednej osoby tym samym długopisem i w jednej sesji, fałszerstwa innym długopisem
- poprawka: ciemność kresek przeskalowana tak, żeby jej mediana była taka sama w każdym obrazie (bez binaryzacji)
- po poprawce EER 35,9%: dużo słabiej, ale nie 50%; przypuszczalnie zostaje grubość kresek (inny długopis)
- opisać jako ograniczenie; po treningu ewentualnie porównać z wariantem ze zbinaryzowanymi kreskami
- metoda bazowa na przetworzonych obrazach: 42,1% dla fałszerstw (było 38,0%), 31,6% dla różnych osób (było 32,3%)
- czyli część starego wyniku dla fałszerstw pochodziła z tła i atramentu, a nie z kształtu

## Październik 2026 — Plan eksperymentów
- najpierw jeden trening na obecnym procesie, jako punkt odniesienia
- potem zawsze jedna zmiana naraz, ten sam seed, wyniki do CSV
- kolejność eksperymentów:
  - bez usuwania tła i bez normalizacji atramentu (ile zawyżają sztuczne wskazówki)
  - przycinanie vs cały obraz (SigNet) vs środek masy na dużym tle (Hafemann)
  - nowe pary w każdej epoce (teraz w treningu jest tylko część fałszerstw)
  - augmentacja (obrót, przesunięcie, skala, grubość kresek)
  - trening bez fałszerstw wykwalifikowanych, test na nich
  - rozmiar wejścia (64×128, 128×256, 256×512)
- na końcu walidacja krzyżowa po osobach (np. 5 × 11 osób) dla najlepszego wariantu, wynik jako średnia ± odchylenie
- do `preprocess()` dodać parametry do włączania i wyłączania kroków

## Październik 2026 — Pierwszy trening (punkt odniesienia)
- sieć: 4 bloki splotowe (32-64-128-128), uśrednianie do siatki 2×4, dropout 0,3, wektor cech 128 znormalizowany
- strata kontrastowa, margines 1,0, etykieta 1 = ta sama osoba (u Hadsella odwrotnie)
- Adam, lr 1e-3, weight decay 1e-4, batch 32, 30 epok, seed 42
- najlepsza epoka 9 (EER walidacja 20,2%); strata walidacyjna najniższa w epoce 4, potem rośnie, czyli przeuczenie
- EER walidacji skacze między epokami (20–32%), bo walidacja to tylko 10 osób; wybór najlepszej epoki jest przez to trochę zawyżony
- test, fałszerstwa wykwalifikowane: EER 28,7% (metoda bazowa 45,7%)
- test, fałszerstwa losowe: EER 15,4% (metoda bazowa 30,8%)
- próg z walidacji na wszystkich parach (odległość 0,515): wykwalifikowane FAR 40,0% / FRR 15,6%, losowe FAR 15,0% / FRR 15,6%
- próg ustalony na mieszance par jest za łagodny dla fałszerstw wykwalifikowanych, dlatego od teraz próg wybieram na walidacji z samymi fałszerstwami wykwalifikowanymi
- notebook `03_trening.ipynb`

## Październik 2026 — Eksperyment: stałe pary vs nowe pary co epokę
- `src/train.py`: funkcja `run_experiment`, wyniki zapisywane do `results/experiments.csv`
- każdy wariant 3 razy (seed 1, 2, 3), próg wybierany na walidacji z fałszerstwami wykwalifikowanymi
- stałe pary: EER wykwalifikowane 23,7% ± 3,8, losowe 16,5% ± 2,8
- nowe pary: EER wykwalifikowane 24,6% ± 3,0, losowe 16,1% ± 1,4
- różnica mniejsza niż rozrzut między seedami, więc nowe pary nie dają pewnej poprawy
- wcześniejsza „poprawa” o 3,3 pkt z jednego treningu była przypadkiem, dlatego każdy wariant trenuję na kilku seedach
- rozrzut między seedami duży (wykwalifikowane od 18,8% do 28,6%)
- najlepsze epoki od 2 do 11, 30 epok to za dużo; 6 treningów = 33 min
- notebook `04_eksperymenty.ipynb`

## Październik 2026 — Eksperyment: augmentacja
- augmentacja tylko na zbiorze treningowym, walidacja i test bez zmian
- geometria: obrót do ±5°, przesunięcie do 5%, zmniejszenie do 85–100%
- powiększania nie ma, bo ucinało końce podpisu
- grubość: z prawdopodobieństwem 50% kreski pogrubione o 1 px (`max_pool2d` 3×3)
- pocieniania nie ma, bo cienkie kreski znikały
- każdy wariant 3 razy (seed 1, 2, 3), porównanie z „nowe pary” (te same ustawienia, tylko bez augmentacji)
- bez augmentacji: EER wykwalifikowane 24,6% ± 3,0, losowe 16,1% ± 1,4
- geometria: EER wykwalifikowane 20,3% ± 1,9, losowe 11,1% ± 0,6
- geometria + grubość: EER wykwalifikowane 23,0% ± 2,0, losowe 13,5% ± 1,4
- geometria lepsza przy każdym seedzie, nie tylko średnio (wykwalifikowane 17,9 / 20,4 / 22,5 zamiast 21,4 / 28,7 / 23,7)
- mniejszy rozrzut między seedami, EER walidacji 14,2% ± 0,8 zamiast 19,3% ± 2,2
- najlepsza epoka średnio 11 zamiast 6, czyli sieć przeucza się później
- pogrubianie kresek pogarsza wynik przy każdym seedzie
- przypuszczenie: grubość kreski pomaga odróżnić fałszerstwo (po wyrównaniu atramentu zostawała grubość, patrz wpis „Atrament zdradza fałszerstwo”)
- nie wiem, czy to prawdziwa cecha (fałszerz pisze wolniej i mocniej przyciska), czy kolejna różnica ze sposobu zbierania danych, opisać w rozdz. 5
- decyzja: od teraz augmentacja geometryczna domyślnie włączona, bez pogrubiania
- próg z walidacji dalej źle pasuje do osób testowych: FAR 26,8%, FRR 14,5% (wykwalifikowane), kolejny argument za walidacją krzyżową
- tylko 3 seedy i jeden podział osób, więc wynik spójny, ale nie dowód statystyczny
- 6 treningów = 43 min
- notebook `04_eksperymenty.ipynb`

## Październik 2026 — Eksperyment: wycieki (bez wyrównania atramentu, bez usuwania tła)
- do `preprocess()` dodane przełączniki `background` i `ink`, domyślnie oba włączone (wynik taki sam jak wcześniej)
- prostokąt do przycięcia zawsze liczony na obrazie po Otsu, więc we wszystkich wariantach wycinany jest ten sam fragment
- wariantu „bez tła, z wyrównaniem atramentu” nie ma: bez usuwania tła wyrównanie potraktowałoby szare tło jak atrament
- wszystkie warianty z augmentacją geometryczną, 3 seedy, porównanie z `aug_geom`
- przewidywanie przed treningiem: bez poprawek EER dla fałszerstw wykwalifikowanych mocno spadnie, dla losowych prawie się nie zmieni
- pełne przygotowanie: EER wykwalifikowane 20,3% ± 1,9, losowe 11,1% ± 0,6
- bez wyrównania atramentu: EER wykwalifikowane 20,0% ± 1,6, losowe 12,6% ± 1,3
- bez usuwania tła: EER wykwalifikowane 1,8% ± 0,7 (0,8 / 2,5 / 2,1), losowe 14,1% ± 1,3
- tło: wyciek potwierdzony, sieć prawie bezbłędnie „wykrywa” fałszerstwa po jaśniejszym tle
- przy progu z walidacji model bez usuwania tła akceptuje 42,6% par dwóch różnych osób (pełne przygotowanie: 8,2%)
- czyli sieć nauczyła się porównywać tło, a nie rozpoznawać osobę; na fałszerstwach wygląda świetnie, w prawdziwym zadaniu jest gorsza
- to skrót (shortcut) w rozumieniu Geirhos i in. 2020
- SigNet ma na CEDAR 100% (Dey i in., tab. 4), próg dobierany na teście, bez usuwania tła; mój wynik 1,8% pokazuje, skąd taki wynik może się brać
- atrament: przewidywanie się nie sprawdziło, wynik bez zmian
- możliwe powody: sieć nie korzysta z ciemności, bierze tę samą informację z grubości kresek albo ciemność nic nie dokłada do kształtu
- wyrównanie atramentu zostaje, bo nie szkodzi, a dla fałszerstw losowych wynik trochę lepszy
- najlepsze epoki w nowych wariantach późno (19–27 z 30), modele mogły się jeszcze poprawiać, ważne przed zmniejszaniem liczby epok
- 6 treningów = 41 min
- notebook `04_eksperymenty.ipynb`

## Październik 2026 — Eksperyment: trening bez fałszerstw wykwalifikowanych
- dwa nowe przełączniki w `train.py`: `skilled_train` (fałszerstwa w treningu) i `skilled_val` (fałszerstwa przy wyborze epoki i progu)
- bez fałszerstw w treningu 48 par „ta sama osoba” i 48 par losowych na osobę, żeby klasy były po równo
- poprawka w `resample`: przy 48 parach losowych każdy podpis osoby użyty 2 razy; dla 24 par wynik taki sam jak wcześniej (sprawdzone)
- komórka kontrolna: 3360 par, 1680/1680, 0 fałszerstw, 0 par losowych z tą samą osobą
- 3 seedy, porównanie z `aug_geom`
- aug_geom: EER wykwalifikowane 20,3% ± 1,9, losowe 11,1% ± 0,6
- bez fałszerstw w treningu: EER wykwalifikowane 26,4% ± 2,3, losowe 9,2% ± 1,2
- bez fałszerstw w ogóle (także wybór epoki i progu): EER wykwalifikowane 27,8% ± 0,5, losowe 10,5% ± 0,6
- fałszerstwa w treningu dają ok. 6 pkt, przy każdym seedzie; nie wiem, czy to prawdziwe cechy fałszerstw, czy resztka wycieku (np. grubość kresek)
- bez fałszerstw sieć i tak dużo lepsza niż metoda bazowa (45,7% na teście), czyli uczy się głównie kształtu podpisu
- pary losowe lepiej bez fałszerstw, bo w treningu jest ich dwa razy więcej
- wybór epoki na fałszerstwach daje niewiele (26,4% vs 27,8%)
- próg z par losowych za łagodny na fałszerstwa: FAR 64,4%, FRR 3,9%; bez przykładów fałszerstw nie da się dobrze ustawić progu, do rozdz. 5
- SigNet na GPDS: bez fałszerstw w treningu też gorzej (Dey i in., tab. 4)
- decyzja: w głównym modelu zostają fałszerstwa w treningu i walidacji, ten eksperyment opisać jako wariant realistyczny
- 6 treningów, notebook `04_eksperymenty.ipynb`

## Październik 2026 — Eksperyment: sposób przycinania
- do `preprocess()` dodany przełącznik `crop`: `bbox` (przycięcie do podpisu), `none` (cały obraz po usunięciu tła), `center` (podpis na tle 730×1460 wg środka masy, jak Hafemann i in. 2017, rozdz. 3.3)
- tło 730×1460, bo najwyższy przycięty podpis ma 729 px; to fałszerstwa osoby 7 (zbiór testowy), pisane ukośnie przez całą kartkę, przycinanie działa poprawnie
- 3 seedy, augmentacja geometryczna, porównanie z `aug_geom` (= `bbox`)
- przewidywanie przed treningiem: `bbox` najlepszy lub podobny, `center` gorszy
- bbox: EER wykwalifikowane 20,3% ± 1,9, losowe 11,1% ± 0,6, walidacja 14,2% ± 0,8
- none: EER wykwalifikowane 17,2% ± 0,5, losowe 12,5% ± 1,2, walidacja 13,5% ± 0,9
- center: EER wykwalifikowane 26,2% ± 0,7, losowe 17,3% ± 3,1, walidacja 18,7% ± 0,7
- center gorszy, bo typowy podpis zajmuje na wejściu tylko ok. 38×91 px
- none lepszy na fałszerstwach przy każdym seedzie, ale trochę gorszy na losowych; przewidywanie się nie sprawdziło
- sprawdzenie wycieku przez kadr (EER z samej różnicy cechy w parze): środek y 49,3%, środek x 47,0%, wysokość 45,5%, wypełnienie 43,8%, szerokość 42,1%
- położenie podpisu nic nie zdradza, rozmiar względem kartki tylko słabo; prostego wycieku brak
- możliwe wyjaśnienie: przy `none` zostaje względny rozmiar podpisu i grubość kresek (przy `bbox` każdy podpis skalowany inaczej), nie sprawdzone
- powtórzony trening (crop_none, seed 1) dał identyczny wynik co do cyfry, czyli trening jest w pełni powtarzalny
- decyzja: od teraz `crop="none"` domyślnie, bo lepszy na walidacji, stabilniejszy i prostszy (jak SigNet)
- wcześniejsze eksperymenty zostają ważne, bo porównywały warianty przy tym samym przycinaniu
- do zrobienia: przerobić akapit o przycinaniu w rozdz. 4.1
- metoda bazowa przy `none`: 38,0% (wykwalifikowane), 32,0% (losowe); atrament po wyrównaniu 36,7%
- wniosek z wpisu „Atrament zdradza fałszerstwo” (42,1% → część wyniku z tła i atramentu) nieaktualny: wzrost do 42,1% powodowało przycinanie
- ten wpis zastępuje decyzje z wpisów „Przycinanie do samego podpisu” i „Przygotowanie obrazów” (kolejność kroków, uzasadnienie 128×256)
- usunięty zdublowany wiersz crop_none seed 1 z CSV
- notebooki `02_przygotowanie_obrazow.ipynb` (kadr), `04_eksperymenty.ipynb` (trening)

## Październik 2026 — Eksperyment: rozmiar wejścia
- do `train.py` dodane ustawienie `size` (domyślnie 128×256), przekazywane do `preprocess()`
- sieć działa dla każdego rozmiaru bez zmian, bo `AdaptiveAvgPool2d((2, 4))` zawsze daje siatkę 2×4 przed warstwą liniową
- warianty: 64×128, 128×216 (proporcja ok. 1,7 jak całe obrazy, bez białych pasów), 256×512; porównanie z `crop_none` (128×256)
- przewidywanie przed treningiem: 64×128 gorszy, 128×216 podobny, 256×512 może trochę lepszy
- 128×256: walidacja 13,5% ± 0,9, wykwalifikowane 17,2% ± 0,5, losowe 12,5% ± 1,2 (ok. 9 min na trening)
- 64×128: walidacja 16,9% ± 1,1, wykwalifikowane 16,9% ± 1,9, losowe 13,7% ± 1,3 (ok. 3 min)
- 128×216: walidacja 14,1% ± 0,4, wykwalifikowane 16,6% ± 1,8, losowe 15,2% ± 1,3 (ok. 7 min)
- 256×512: walidacja 11,7% ± 0,6, wykwalifikowane 19,2% ± 1,8, losowe 12,9% ± 1,6 (ok. 70 min, najlepsze epoki 19–28)
- na fałszerstwach rozmiar prawie nic nie zmienia, mały obraz wystarcza; przewidywanie dla 64×128 się nie sprawdziło
- 64×128 i 128×216 gorsze na walidacji; 128×216 gorszy na losowych o 2,7 pkt, powód nieznany (może nierówny podział mapy cech o szerokości 13 w `AdaptiveAvgPool2d`, nie sprawdzone)
- 256×512 najlepszy na walidacji przy każdym seedzie, ale na teście gorszy na fałszerstwach o 2 pkt
- walidacja i test wskazują co innego, czyli 10 osób w walidacji to za mało do wyboru między wariantami różniącymi się o 1–2 pkt; kolejny argument za walidacją krzyżową
- decyzja: zostaje 128×256, mimo lepszej walidacji 256×512, bo przewaga nie potwierdziła się na teście, a trening jest ponad 8 razy dłuższy (walidacja krzyżowa: ok. 17 h zamiast ok. 2,5 h)
- białe pasy po bokach całych obrazów nie szkodzą
- notebook `04_eksperymenty.ipynb`

## Walidacja krzyżowa

- po co: w eksperymencie z rozmiarem wejścia walidacja i test pokazywały co innego, a test to tylko 10 osób, więc nie wiadomo było, ile wynik zależy od tego, kto trafił do testu
- jak: 55 osób podzielone na 5 części po 11 (seed 42, plik data/cv_folds.json); każda część raz jest testem, 10 osób walidacja, 34 trening
- pary walidacyjne i testowe losowane raz (seed 123), treningowe co epokę jak wcześniej
- ustawienia: aktualne DEFAULTS (crop none, 128x256, augmentacja geometryczna, usuwanie tła, wyrównanie atramentu)
- 5 części x 3 seedy = 15 treningów, ok. 141 min
- wynik (średnia ± odchylenie z 15 treningów):
  - EER wykwalifikowane 20,4% ± 3,1 (od 15,5 do 25,8)
  - EER losowe 13,6% ± 2,4 (od 9,5 do 17,8)
  - EER walidacja 12,1% ± 1,6
- średnie części (wykw. / losowe): 23,1/14,5, 16,5/16,7, 22,7/10,0, 18,9/13,9, 20,9/12,9
- na starym podziale było 17,2 ± 0,5, czyli stary podział był łatwiejszy niż przeciętny
- wybór osób do testu zmienia wynik bardziej niż seed (ok. 2,4 pkt vs ok. 1,4 pkt), ale seed w niektórych częściach też dużo zmienia (część 2: 17,7–25,8)
- część 4 to prawie stary test, a wychodzi 20,9 zamiast 17,2 (inna liczba osób w teście, inne osoby w walidacji, losowane pary zamiast CSV)
- najlepsze epoki głównie 18–30, czasem ostatnia, więc 30 epok może być trochę za mało
- FAR wykwalifikowane od 9,8 do 37,1%, czyli próg wybrany na walidacji (10 osób) słabo przenosi się na test
- decyzja: w rozdziale 5 jako główny wynik sieci podaję wynik z walidacji krzyżowej (20,4 ± 3,1 / 13,6 ± 2,4), a wyniki z jednego podziału zostają do porównywania wariantów między sobą

## Metoda bazowa na częściach walidacji krzyżowej

- po co: porównać sieć i metodę bazową na dokładnie tych samych parach testowych
- jak: korelacja pikseli po pełnym przygotowaniu (tło, atrament, crop none, 128x256), te same pary co w walidacji krzyżowej (seed 123), próg z walidacji (prawdziwe + wykwalifikowane)
- przewidywanie: wykwalifikowane 35–40%, losowe 30–33%
- wynik (średnia ± odchylenie z 5 części):
  - EER wykwalifikowane 39,0% ± 3,1 (od 34,8 do 43,2)
  - EER losowe 32,7% ± 3,0 (od 29,9 do 37,9)
- zgadza się z notebookiem 02 (38,0 / 32,0 na wszystkich parach)
- sieć wygrywa w każdej części: 20,4 vs 39,0 (wykwalifikowane), 13,6 vs 32,7 (losowe), czyli EER mniej więcej o połowę niższy
- najgorszy trening sieci (25,8%) lepszy niż najlepsza część metody bazowej (34,8%)
- trudne części są inne dla sieci i dla korelacji (część 1: sieć 16,5, korelacja 41,3; część 2: sieć 22,7, korelacja 34,8)
- próg z walidacji tu też słabo się przenosi (FRR 42,6% vs FAR 34,4%, FRR od 24,6 do 54,7)
- w pracy: odchylenie bazowej z 5 wartości, sieci z 15 (5 części x 3 seedy)