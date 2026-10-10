# Literatura

PDF-y w folderze `literatura_pdf/` (nie trafiają do gita).
Strony podane wg numeracji w PDF-ie, jeśli nie zaznaczono inaczej.

## Weryfikacja podpisu (rozdz. 1, 2)

### Hafemann, Sabourin, Oliveira 2017 — Offline Handwritten Signature Verification: Literature Review
- plik: hafemann2017review.pdf (arXiv v4, 8 stron)
- przeczytany abstrakt i rozdz. II
- IPTA 2017, DOI 10.1109/IPTA.2017.8310112, strony w wersji IPTA do sprawdzenia
- abstrakt, 1. zdanie: dziedzina badana od dekad, nadal problem otwarty, cytowane we Wstępie
- abstrakt, 4. zdanie: uczenie głębokie uczy się cech z obrazów podpisów, cytowane we Wstępie
- rozdz. I: rodzaje fałszerstw (losowe, proste, wykwalifikowane), cytowane w 3.4
- rozdz. II (str. 2): writer-dependent i writer-independent, cytowane w 3.3
- rozdz. II.A (str. 2): duża zmienność podpisów jednej osoby, mało próbek na osobę
- tab. I (str. 3): CEDAR wśród najczęściej używanych zbiorów
- rozdz. IV (str. 3): nawet prawdziwe podpisy jednej osoby różnią się grubością pióra, skalą i obrotem, do uzasadnienia augmentacji w rozdz. 4
- rozdz. VI.E (str. 6): augmentacja w podpisach (Huang i Yan: obrót, skalowanie, pochylenie)
- rozdz. VI.F (str. 6): definicje FRR, FAR, EER
- tab. IV (str. 6): wyniki innych metod na CEDAR, najlepszy EER 4,63% (Hafemann 2017 features), do rozdz. 5

### Jain, Ross, Prabhakar 2004 — An Introduction to Biometric Recognition
- plik: jain2004.pdf
- nieprzeczytane, miejsca sprawdzone
- IEEE Trans. on Circuits and Systems for Video Technology, vol. 14, nr 1, str. 4–20
- strony wg czasopisma (str. 1 w PDF = str. 4)
- rozdz. II (str. 4–5): tryb weryfikacji (1:1) i identyfikacji (1:N)
- rozdz. III (str. 6–7, rys. 2): FMR i FNMR zależą od progu, kompromis między nimi
- rozdz. IV (str. 10): podpis jako biometria behawioralna, zmienia się w czasie, u niektórych osób kolejne podpisy wyraźnie się różnią
- nazwy FMR/FNMR zamiast FAR/FRR, nie ma EER, te definicje brać z Hafemanna

## Sieci syjamskie i funkcja straty (rozdz. 2, 4)

### Bromley i in. 1993 — Signature Verification using a "Siamese" Time Delay Neural Network
- plik: bromley1993.pdf
- przeczytane
- NIPS 6 (1993), str. 737–744
- abstrakt: definicja sieci syjamskiej, cytowane we Wstępie
- rozdz. 4: współdzielone wagi, proporcje par 50/40/10
- przypis 1 (str. 741): fałszerstwa losowe to oryginały innych osób, do rozdz. 3.4
- rozdz. 2: fałszerstwa wykwalifikowane są najtrudniejsze
- podpisy z tabletu (online), nie obrazy

### Hadsell, Chopra, LeCun 2006 — Dimensionality Reduction by Learning an Invariant Mapping
- plik: hadsell2006.pdf (wersja przed publikacją, 8 stron)
- nieprzeczytane, miejsca sprawdzone
- CVPR 2006, str. 1735–1742, DOI 10.1109/CVPR.2006.100
- strony poniżej wg PDF-u, w wersji CVPR mogą być inne
- rozdz. 2.1 (str. 2–3): contrastive loss, oryginalne źródło straty, której używam
- wzór (1) (str. 3): odległość euklidesowa między wyjściami sieci
- wzór (4) (str. 3): pełna funkcja straty z marginesem m
- Y=0 oznacza parę podobną (u mnie i w Li 2022 odwrotnie)
- we wzorze jest ½ przed oboma składnikami, u mnie nie ma (strata razy 2, to samo minimum)
- str. 3: bez składnika dla par niepodobnych sieć mogłaby wszystko mapować w jeden punkt (rozwiązanie „zapadnięte”)

### Chopra, Hadsell, LeCun 2005 — Learning a Similarity Metric Discriminatively, with Application to Face Verification
- nie pobrane
- CVPR 2005, vol. 1, str. 539–546 (wg bibliografii Hadsella, poz. [5])
- PDF: http://yann.lecun.com/exdb/publis/pdf/chopra-05.pdf
- wcześniejsza wersja pomysłu contrastive loss
- SigNet cytuje contrastive loss właśnie z tej pracy (poz. [15])

### Koch, Zemel, Salakhutdinov 2015 — Siamese Neural Networks for One-shot Image Recognition
- nie pobrane
- ICML Deep Learning Workshop 2015
- PDF: https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf
- abstrakt: sieć działa też dla zupełnie nowych klas
- rozdz. 3.2: strata cross-entropy zamiast contrastive
- zbiór Omniglot (znaki pisma), nie podpisy

### Li, Chen, Zhang 2022 — A Survey on Siamese Network: Methodologies, Applications, and Opportunities
- plik: li2022.pdf
- przeczytany abstrakt i wstęp
- IEEE Trans. on Artificial Intelligence, vol. 3, nr 6, str. 994–1014, DOI 10.1109/TAI.2022.3207112
- str. 994: sieć syjamską jako pierwszy zaproponował Bromley
- str. 996, rys. 2: schemat sieci syjamskiej
- str. 996, wzór (5): contrastive loss, tutaj Y=1 oznacza parę podobną
- przydatny do szukania innych źródeł w bibliografii

## Sieci dla podpisów w postaci obrazów (rozdz. 2, 5)

### Dey i in. 2017 — SigNet: Convolutional Siamese Network for Writer Independent Offline Signature Verification
- plik: dey2017.pdf (arXiv v2)
- przeczytany abstrakt i wstęp, wyniki sprawdzone
- arXiv:1707.02131, 2017
- rozdz. 1: czym jest writer-independent i dlaczego nie trzeba przetrenowywać modelu, cytowane we Wstępie
- rozdz. 2.1 (str. 2): obrazy skalowane do 155×220, odwrócone kolory
- rozdz. 2.2 (str. 2–3): contrastive loss, margines m = 1 (tak samo jak u mnie)
- str. 4, tab. 2: RMSprop, lr 1e-4, 20 epok, batch 128
- rozdz. 3.1.1 (str. 4): opis CEDAR, każdy fałszerz podrabiał 3 osoby po 8 razy
- rozdz. 3.3 i tab. 3 (str. 5): CEDAR losowo podzielony raz, 50 osób trening / 5 test (u mnie 35/10/10)
- rozdz. 3.2, wzór (2) (str. 5): dokładność = najlepszy wynik po sprawdzeniu wszystkich progów na zbiorze testowym, czyli próg dobrany na teście
- tab. 4 (str. 6): na CEDAR 100% dokładności, FAR 0, FRR 0 (tak samo Dutta i in.)
- rys. 3 (str. 6): model uczony na CEDAR na innych zbiorach tylko 54–64%; model uczony na GPDS300 na CEDAR 94,82%
- najbardziej podobna praca do mojej (sieć syjamska, CNN, contrastive loss, CEDAR)
- cytowane w 3.1 (CEDAR często używany) i 3.3 (writer-independent, podział 50/5)
- do rozdz. 5: 100% przy progu z testu i 5 osobach testowych, porównać z moim protokołem

### Hafemann, Sabourin, Oliveira 2017 — Learning Features for Offline Handwritten Signature Verification using Deep CNNs
- plik: hafemann2017features.pdf (arXiv v1, 35 stron)
- nieprzeczytane, miejsca sprawdzone
- Pattern Recognition, vol. 70, str. 163–176, DOI 10.1016/j.patcog.2017.05.012
- strony poniżej wg arXiv, w czasopiśmie inne
- abstrakt: na obrazie podpisu nie ma informacji o ruchu pióra
- inne podejście niż sieć syjamska (uczenie cech przez CNN), do rozdz. 2
- rozdz. 3.3 (str. 13): środek masy na dużym tle, Otsu (tło = 255, atrament w skali szarości), odwrócenie kolorów, zmiana rozmiaru
- tab. 3 (str. 16): CEDAR wśród używanych zbiorów (55 osób, 24 + 24), cytowane w 3.1
- str. 18: na CEDAR klasyfikator dla każdej osoby uczony tylko na prawdziwych podpisach (negatywy to podpisy innych osób), bez fałszerstw wykwalifikowanych
- tab. 9 (str. 27): CEDAR EER 4,63% (SigNet-F, 12 podpisów wzorcowych)
- ich sieć też nazywa się „SigNet”, ale to inna sieć niż Dey i in.

## Zbiór danych (rozdz. 3)

### Kalera, Srihari, Xu 2004 — Offline Signature Verification and Identification Using Distance Statistics
- plik: kalera2004.pdf
- do przeczytania rozdz. 1–2 (ok. 3 strony)
- Int. Journal of Pattern Recognition and Artificial Intelligence, vol. 18, nr 7 (listopad 2004), str. 1339–1360, DOI 10.1142/S0218001404003630
- źródło zbioru CEDAR
- str. 1339 (wstęp): obrazy offline bez informacji o ruchu, fałszerstwa wykwalifikowane trudne, cytowane we Wstępie
- str. 1341 (rozdz. 2.1): opis zbioru, cytowane w 3.1 i 3.2 (8-bit skala szarości)
- str. 1342 (tab. 1): podsumowanie zbioru
- str. 1349 (rozdz. 3.1.1): podział podpisów 16/8, te same osoby w treningu i teście, cytowane w 3.3
- metoda: cechy GSC na obrazach zbinaryzowanych, 78% dokładności weryfikacji (abstrakt)

## Przygotowanie obrazów (rozdz. 4)

### Otsu 1979 — A Threshold Selection Method from Gray-Level Histograms
- plik: otsu1979.pdf
- nieprzeczytane, miejsca sprawdzone
- IEEE Trans. on Systems, Man, and Cybernetics, vol. SMC-9, nr 1, str. 62–66, DOI 10.1109/TSMC.1979.4310076
- w PDF-ie na str. 62 jest też koniec innego artykułu, Otsu zaczyna się w prawej kolumnie
- abstrakt (str. 62): automatyczny wybór progu tylko z histogramu, bez nadzoru
- rozdz. I (str. 62): dwa szczyty histogramu (obiekt i tło), próg trudno znaleźć, gdy dolina między nimi jest płaska
- rozdz. II (str. 63): piksele dzielone progiem k na dwie klasy (tło i obiekt)
- wzory (18)–(19) (str. 63): wybierany próg, przy którym wariancja między klasami jest największa
- do opisu usuwania tła w rozdz. 4 (obiecane w 3.2)

## Trening sieci (rozdz. 2, 4)

### Kingma, Ba 2015 — Adam: A Method for Stochastic Optimization
- plik: kingma2015.pdf (arXiv v9)
- nieprzeczytane, miejsca sprawdzone
- ICLR 2015, arXiv:1412.6980
- rozdz. 1 (str. 1): osobny, dopasowywany krok uczenia dla każdego parametru, na podstawie średniej gradientów i średniej ich kwadratów; nazwa od „adaptive moment estimation”
- algorytm 1 (str. 2): cały algorytm, domyślnie α = 0,001 (u mnie lr 1e-3, czyli domyślna wartość)
- rozdz. 3 (str. 3): poprawka na początkowe zerowe średnie (bias correction)

### Ioffe, Szegedy 2015 — Batch Normalization
- plik: ioffe2015.pdf (arXiv v3)
- nieprzeczytane, miejsca sprawdzone
- ICML 2015, PMLR vol. 37, str. 448–456
- abstrakt: pozwala na większy krok uczenia, działa też jak regularyzacja
- algorytm 1 (str. 3): normalizacja średnią i wariancją z mini-batcha, potem skalowanie γ i przesunięcie β
- rozdz. 3.1, algorytm 2 (str. 4): przy ocenie zamiast mini-batcha używane są średnie z całego treningu (dlatego `model.eval()`)
- rozdz. 3.2 (str. 4–5): wersja dla warstw splotowych (jedna para γ, β na kanał)
- rozdz. 3.4 (str. 5): BatchNorm częściowo zastępuje Dropout

### Srivastava i in. 2014 — Dropout: A Simple Way to Prevent Neural Networks from Overfitting
- plik: srivastava2014.pdf
- nieprzeczytane, miejsca sprawdzone
- JMLR vol. 15, str. 1929–1958
- strony wg czasopisma (str. 1 w PDF = str. 1929)
- abstrakt (str. 1929): przeuczenie to poważny problem dużych sieci, dropout losowo wyłącza neurony w treningu
- rys. 1 (str. 1930): sieć bez dropoutu i z dropoutem
- rys. 2 (str. 1931): przy teście wszystkie neurony włączone, wagi skalowane przez p
- rozdz. 4 (str. 1933–1934): opis modelu
- u nich p = prawdopodobieństwo, że neuron zostaje; w PyTorch p = prawdopodobieństwo wyłączenia (moje 0,3 w PyTorch = p 0,7 u nich)

### Shorten, Khoshgoftaar 2019 — A survey on Image Data Augmentation for Deep Learning
- plik: shorten2019.pdf
- nieprzeczytane, miejsca sprawdzone
- Journal of Big Data 6, 60, DOI 10.1186/s40537-019-0197-0
- abstrakt (str. 1): definicja przeuczenia, augmentacja jako sposób na mało danych
- str. 7: „bezpieczeństwo” augmentacji, czyli czy po przekształceniu etykieta zostaje prawdziwa
- str. 8: obrót (tylko małe kąty są bezpieczne), przesunięcie (dopełnienie stałą wartością)
- do rozdz. 4 (dlaczego małe obroty) i 5 (pogrubianie kresek mogło nie być „bezpieczne”, bo grubość niesie informację)

### Goodfellow, Bengio, Courville 2016 — Deep Learning
- bez PDF-a, tylko strona: https://www.deeplearningbook.org
- MIT Press, 2016
- rozdz. 6: sieci jednokierunkowe (podstawy)
- rozdz. 7.4: augmentacja danych
- rozdz. 7.8: wczesne zatrzymanie (u mnie wybór najlepszej epoki)
- rozdz. 7.12: dropout
- rozdz. 8.5.3: Adam
- rozdz. 8.7.1: BatchNorm
- rozdz. 9: sieci konwolucyjne

### LeCun, Bottou, Bengio, Haffner 1998 — Gradient-Based Learning Applied to Document Recognition
- nie pobrane
- Proceedings of the IEEE, vol. 86, nr 11, str. 2278–2324
- klasyczne źródło CNN (LeNet), tylko gdyby był potrzebny cytat historyczny

## Wyniki i dyskusja (rozdz. 5)

### Geirhos i in. 2020 — Shortcut Learning in Deep Neural Networks
- plik: geirhos2020.pdf (arXiv v5)
- nieprzeczytane, miejsca sprawdzone
- Nature Machine Intelligence, vol. 2, nr 11, str. 665–673, DOI 10.1038/s42256-020-00257-z
- strony poniżej wg arXiv
- abstrakt: „shortcut” to reguła, która działa na typowym teście, ale nie w trudniejszych warunkach
- rys. 1 i str. 2–3: sieć rozpoznawała zapalenie płuc po znaczniku szpitala na zdjęciu RTG, nie po chorobie (podobnie jak tło w CEDAR)
- rozdz. 4.1 (str. 7): tło jako skrót (krowa na trawie), skróty biorą się ze zbioru danych
- rozdz. 6.1 (str. 11): wynik na zbiorze danych jest wart tyle, ile ten zbiór mierzy to, co chcemy mierzyć
- do dyskusji o tle, atramencie i grubości kresek w CEDAR

## Nie pobrane (opcjonalne)
- Pal i in. 2016, zbiór BHSig260, tylko jeśli użyję drugiego zbioru
- Paszke i in. 2019, PyTorch, arXiv:1912.01703, tylko jeśli promotor każe cytować narzędzia

## Do znalezienia
- artykuł o tym, że złe dzielenie osób daje zawyżone wyniki na CEDAR, do rozdz. 5
- czy ktoś w literaturze opisał różnicę tła między prawdziwymi podpisami a fałszerstwami w CEDAR