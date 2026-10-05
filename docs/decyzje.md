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
- EER: 38,0% dla fałszerstw wykwalifikowanych, 32,3% dla różnych osób, czyli metoda myli się w ponad 1/3 przypadków
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