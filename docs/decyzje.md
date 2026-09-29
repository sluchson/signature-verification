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
- różne tryby kolorów: `full_org` RGBA i L, `full_forg` P i RGBA
- sieć potrzebuje tego samego rozmiaru i tej samej liczby kanałów
- kolor nic nie mówi o kształcie podpisu, jeden kanał wystarczy
- notebook `01_eksploracja_danych.ipynb`

## Wrzesień 2026 — Proporcje wejścia sieci
- wejście ma być prostokątem szerszym niż wyższym, nie kwadratem
- mediana rozmiaru 576×349 px, proporcja ok. 1,65:1, tak samo w `full_org` i `full_forg`
- szerokości od 264 do 888 px, więc trochę zniekształcenia i tak będzie
- np. ok. 220×140 zamiast 128×128, dokładny rozmiar w rozdz. 4
- SigNet skaluje wszystkie obrazy do 155×220 (wys. × szer.), proporcja ok. 1,42:1, czyli też prostokąt
- notebook `01_eksploracja_danych.ipynb`

## Wrzesień 2026 — Przycinanie do samego podpisu
- przed zmianą rozmiaru przycinam obraz do prostokąta z samym podpisem (bounding box)
- podpis zajmuje średnio ok. 60% obrazu (60,1% w `full_org`, 58,6% w `full_forg`), reszta to tło
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
- prosty test: obrazy 128×128, korelacja pikseli
- prawdziwy–prawdziwy: 0,146, prawdziwy–podrobiony: 0,146, prawdziwy–inna osoba: 0,081
- taka metoda nie odróżnia dobrego fałszerstwa od oryginału, więc potrzebne jest uczenie głębokie
- pliki sprawdzone (MD5 + `PIL.Image.verify()`): brak uszkodzeń i duplikatów
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

---

## Wrzesień 2026 — Tło zdradza, co jest fałszerstwem
- mediana jasności tła: `full_org` 234–245 (średnio 239,8), `full_forg` 249–255 (średnio 253,5)
- zakresy się nie nakładają, 513 z 1320 fałszerstw ma tło idealnie białe, prawdziwe żadne
- jeden próg (ok. 247) oddziela wszystkie prawdziwe podpisy od fałszerstw bez patrzenia na podpis
- bez poprawki sieć mogłaby rozpoznawać fałszerstwa wykwalifikowane po tle, a nie po kształcie
- nie binaryzuję, więc różnica w tle trafiłaby do sieci
- decyzja: usunięcie tła metodą Otsu, tło = 255, atrament zostaje w skali szarości (jak Hafemann i in. 2017, rozdz. 3.3)
- po przetworzeniu powtórzyć test `background_level` i sprawdzić, czy różnica zniknęła
- notebook `01_eksploracja_danych.ipynb`