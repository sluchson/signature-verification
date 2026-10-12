# Weryfikacja autentyczności podpisu siecią syjamską

Kod i praca inżynierska „Zastosowanie algorytmów sztucznej inteligencji do rozpoznawania autentyczności podpisu” (Politechnika Rzeszowska, WEII, promotor dr inż. Paweł Górka).

Sieć syjamska (splotowa sieć neuronowa trenowana funkcją straty kontrastowej) porównuje dwa zeskanowane podpisy i sprawdza, czy należą do tej samej osoby. Weryfikacja jest niezależna od autora: osoby testowe nie występują w treningu. Dane: zbiór CEDAR (55 osób, po 24 podpisy prawdziwe i 24 fałszerstwa wykwalifikowane).

Wynik końcowy (walidacja krzyżowa, 5 części × 3 ziarna, 50 epok): EER 19,4% ± 3,5 dla fałszerstw wykwalifikowanych i 12,0% ± 1,8 dla fałszerstw losowych (metoda porównawcza – korelacja pikseli: 39,0% i 32,7%).

## Struktura

```
data/          podział osób (writer_split.json), części walidacji krzyżowej (cv_folds.json), pary podpisów (*_pairs.csv)
data/signatures/   obrazy CEDAR (poza gitem, trzeba pobrać)
src/           kod: przygotowanie obrazów, zbiór danych, sieć, metryki, trening
notebooks/     01 analiza danych, 02 przygotowanie obrazów, 03 pierwszy trening (historyczny), 04 eksperymenty
results/       wyniki wszystkich treningów (experiments.csv) i przebiegi treningu (*_historia.json)
models/        zapisane wagi sieci (poza gitem)
docs/          dziennik decyzji, notatki o literaturze, zasady formatowania
praca/         tekst pracy w LaTeX (szablon WEII) i rysunki
```

## Instalacja

Wymagany Python 3.13 i karta graficzna NVIDIA (trening działa też na procesorze, ale dużo wolniej).

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` zawiera adres repozytorium PyTorch z obsługą CUDA 12.8.

## Dane

1. Pobrać zbiór „CEDAR Signature Dataset” z Kaggle: https://www.kaggle.com/datasets/shreelakshmigp/cedardataset
2. Rozpakować tak, żeby obrazy były w `data/signatures/full_org/` (podpisy prawdziwe, `original_<osoba>_<nr>.png`) i `data/signatures/full_forg/` (fałszerstwa, `forgeries_<osoba>_<nr>.png`).

Podział osób, części walidacji krzyżowej i pary podpisów są już w repozytorium. Notebook 01 tworzy je od nowa, ale przy tych samych ziarnach wychodzą identyczne pliki.

## Uruchamianie

Notebooki uruchamia się z folderu `notebooks/` (ścieżki są względne).

- `01_eksploracja_danych.ipynb` – sprawdzenie zbioru, różnica jasności tła, podział osób, pary, metoda porównawcza.
- `02_przygotowanie_obrazow.ipynb` – usuwanie tła, wyrównanie atramentu, wybór obszaru obrazu, rysunek do pracy.
- `03_trening.ipynb` – zapis pierwszego treningu, nie uruchamiać ponownie (starsza wersja kodu).
- `04_eksperymenty.ipynb` – wszystkie eksperymenty, walidacja krzyżowa i rysunek krzywej uczenia.

W notebooku 04 treningi są wyłączone przełącznikiem `RUN_TRAINING = False` w pierwszej komórce, żeby przypadkowe „Run All” nie uruchomiło wielu godzin obliczeń. Komórki z podsumowaniami czytają gotowe wyniki z `results/`.

Pojedynczy trening z kodu:

```python
from src.train import run_experiment
result, history = run_experiment("nazwa", seed=1, fold=0, epochs=50)
```

Każdy trening dopisuje wiersz do `results/experiments.csv` i zapisuje najlepszy model w `models/`. Trening z tym samym ziarnem daje identyczny wynik.

## Praca

Tekst jest w `praca/weiiszablon.tex` (szablon WEII PRz). Kompilacja pdfLaTeX, np. rozszerzeniem LaTeX Workshop w VS Code. Rysunki w `praca/figures/` generują notebooki 01, 02 i 04.

## Aplikacja

Interfejs graficzny do porównywania dwóch podpisów – w przygotowaniu.
