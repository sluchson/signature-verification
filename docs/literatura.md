# Literatura

PDF-y w folderze `literatura_pdf/` (nie trafiają do gita).
Strony podane wg numeracji w PDF-ie, jeśli nie zaznaczono inaczej.
„Cytowane w” = podrozdziały pracy, w których jest `\cite` (stan na październik 2026).
Wszystkie cytaty w pracy sprawdzone ze źródłami w październiku 2026 (tabela zdań i stron: rozdz. 2 w pliku z czatu `rozdz2_zrodla.md`).

## Weryfikacja podpisu (rozdz. 1, 2)

### Hafemann, Sabourin, Oliveira 2017 — Offline Handwritten Signature Verification: Literature Review
- plik: hafemann2017review.pdf (arXiv v4, 8 stron)
- IPTA 2017, DOI 10.1109/IPTA.2017.8310112, strony w wersji IPTA do sprawdzenia
- cytowane w: 1, 2.1, 2.2, 2.3, 2.6, 3.4, 5.3
- abstrakt: dziedzina badana od dekad, nadal problem otwarty; uczenie głębokie uczy się cech z obrazów (Wstęp)
- rozdz. I (str. 1): cechy fizjologiczne i behawioralne (podpis, głos) (2.1)
- rozdz. I (str. 1): online = położenie pióra w czasie, czasem nacisk i nachylenie; offline = obraz po zakończeniu pisania (2.1)
- rozdz. I (str. 1): fałszerstwa losowe, proste, wykwalifikowane; wykwalifikowane „harder to detect” (Wstęp, 2.1, 3.4)
- rozdz. II (str. 2): writer-dependent i writer-independent, WI trenowany i testowany na innych osobach (2.1)
- rozdz. II.A (str. 2): duża zmienność podpisów jednej osoby, w praktyce tylko podpisy prawdziwe, mało próbek (2.1, 5.3)
- rozdz. III (str. 2): dużo badań na prywatnych zbiorach (2.2); fałszerstwa zbierane w osobnym procesie niż podpisy prawdziwe (2.6)
- rozdz. IV (str. 3): przygotowanie obrazów, m.in. przycięcie do podpisu albo ramka o stałym rozmiarze; prawdziwe podpisy różnią się grubością pióra, skalą, obrotem (2.3)
- rozdz. V i V.A (str. 3–4): rodzaje cech ręcznych, cechy globalne i lokalne (2.3)
- rozdz. V.B (str. 4): uczenie cech z pikseli (2.3)
- rozdz. VI (str. 5): WI uczy się porównywać podpis z wzorcem; klasyfikatory HMM, SVM, sieci (2.1, 2.3)
- rozdz. VI.E (str. 6): augmentacja w podpisach (Huang i Yan: obrót, skalowanie, pochylenie), w pracy niecytowane
- rozdz. VI.F (str. 6): FRR, FAR_skilled, AER (2.2); uwaga: definicja EER ma tam literówkę („FAR = FAR_skilled”), dlatego EER cytuję z Kalery
- tab. IV (str. 6): wyniki innych metod na CEDAR → tabela 2.1 w pracy

### Jain, Ross, Prabhakar 2004 — An Introduction to Biometric Recognition
- plik: jain2004.pdf
- IEEE Trans. on Circuits and Systems for Video Technology, vol. 14, nr 1, str. 4–20
- strony wg czasopisma (str. 1 w PDF = str. 4)
- cytowane w: 2.1, 2.2
- abstrakt (str. 4): definicja biometrii (cechy fizjologiczne i behawioralne) (2.1)
- rozdz. II (str. 4–5): tryb weryfikacji (1:1) i identyfikacji (1:N) (2.1)
- rozdz. II (str. 5–6): decyzja przez porównanie wyniku z progiem (2.2)
- rozdz. III (str. 6–7, rys. 2): FMR i FNMR = „false accept” i „false reject”, zależą od progu, kompromis (2.2)
- rozdz. III (str. 6–8): wymagania zależą od zastosowania (wysokie bezpieczeństwo → mały FMR) (2.2)
- rozdz. IV (str. 10): podpis akceptowany w sprawach urzędowych, prawnych, handlowych; cecha behawioralna, zmienia się w czasie, zależy od stanu fizycznego i emocjonalnego (2.1)
- nie ma definicji EER

### Kalera, Srihari, Xu 2004 — Offline Signature Verification and Identification Using Distance Statistics
- plik: kalera2004.pdf
- Int. Journal of Pattern Recognition and Artificial Intelligence, vol. 18, nr 7 (listopad 2004), str. 1339–1360, DOI 10.1142/S0218001404003630
- strony wg czasopisma (str. 1 w PDF = str. 1339)
- źródło zbioru CEDAR (u nich „Database A”)
- cytowane w: 2.1, 2.2, 2.3, 3.1, 3.2, 3.3
- str. 1339 (wstęp): obrazy offline bez informacji dynamicznej (2.1); nie piszą, że fałszerstwa wykwalifikowane są najtrudniejsze (tę tezę cytuję z Hafemanna)
- str. 1341 (rozdz. 2.1): 55 osób, 24 podpisy, ok. 20 fałszerzy, pole 2×2 cale, 300 dpi, 8-bit skala szarości, PNG (3.1, 3.2)
- str. 1342 (tab. 1): podsumowanie zbioru
- str. 1345–1348 (rozdz. 2.3–2.4): cechy GSC na obrazach zbinaryzowanych, wektor 1024 bitów, korelacja, klasyfikator Bayesa (2.3)
- str. 1349 (rozdz. 3.1.1): podział podpisów 16/8 (prawdziwych i fałszerstw), te same osoby w treningu i teście (2.3, 3.3)
- str. 1352 (rozdz. 4.1.1): definicje FAR i FRR (2.2)
- str. 1353: EER = punkt, w którym FAR = FRR; EER 21,9% (2.2, 2.3)
- str. 1357 (tab. 10): 78,1% dokładności weryfikacji
- uwaga: w tekście i tab. 10 FAR/FRR są zamienione względem tab. 6 (nie cytuję tych liczb)

## Sieci syjamskie i funkcja straty (rozdz. 2, 4)

### Bromley i in. 1993 — Signature Verification using a "Siamese" Time Delay Neural Network
- plik: bromley1993.pdf
- NIPS 6 (1993), str. 737–744
- cytowane w: 1, 2.5, 3.4, 4.2
- abstrakt (str. 737): dwie jednakowe podsieci połączone na wyjściu, odległość między wektorami cech (Wstęp, 2.5)
- rozdz. 2 (str. 738): podpisy z tabletu (online); fałszerstwa wykwalifikowane najtrudniejsze do wykrycia
- rozdz. 4 (str. 740): podsieci z identycznymi wagami, odległość = cosinus kąta (2.5, 4.2)
- rozdz. 4 (str. 741): pary 50% prawdziwy–prawdziwy, 40% z fałszerstwem, 10% z fałszerstwem losowym (2.5)
- przypis 1 (str. 741): fałszerstwa losowe to oryginały innych osób (3.4)
- rozdz. 6 (str. 743): przy progu wykrywającym 80% fałszerstw akceptowane 95,5% prawdziwych (2.5)

### Hadsell, Chopra, LeCun 2006 — Dimensionality Reduction by Learning an Invariant Mapping
- plik: hadsell2006.pdf (wersja przed publikacją, 8 stron)
- CVPR 2006, str. 1735–1742, DOI 10.1109/CVPR.2006.100
- strony poniżej wg PDF-u, w wersji CVPR mogą być inne
- cytowane w: 2.4, 2.5, 4.3
- str. 1: nauczone odwzorowanie działa dla nowych próbek (2.5)
- rozdz. 2.1 (str. 2–3): contrastive loss, pary podobne przyciągane, niepodobne odpychane do marginesu (2.5, 4.3)
- wzór (1) (str. 3): odległość euklidesowa; wzór (4) (str. 3): pełna funkcja straty z marginesem m
- Y=0 oznacza parę podobną (u mnie i w Li 2022 odwrotnie); ½ przed oboma składnikami, u mnie nie ma (to samo minimum)
- str. 3: bez składnika dla par niepodobnych rozwiązanie „zapadnięte” (2.5, 4.3)
- rozdz. 3.1 (str. 4–5): architektura syjamska ze wspólnymi parametrami; sieci splotowe uczą się cech niskiego i wysokiego poziomu (2.4)

### Li, Chen, Zhang 2022 — A Survey on Siamese Network: Methodologies, Applications, and Opportunities
- plik: li2022.pdf
- IEEE Trans. on Artificial Intelligence, vol. 3, nr 6, str. 994–1014, DOI 10.1109/TAI.2022.3207112
- strony wg czasopisma (str. 1 w PDF = str. 994)
- cytowane w: 2.5
- str. 994: sieć syjamską jako pierwszy zaproponował Bromley, do weryfikacji podpisu
- rozdz. II-A1 (str. 996): trzy części: wyznaczanie cech, porównanie, decyzja; gałęzie z tymi samymi wagami
- rozdz. II-A, II-A2 (str. 996–998): sieć pseudosyjamska (bez wspólnych wag)
- rozdz. II-A3 (str. 998): sieć trójkowa (triplet)
- str. 996, wzór (5): contrastive loss, tu Y=1 = para podobna
- rozdz. V (str. 1006): z N próbek N(N−1)/2 par
- rozdz. VI-B2 (str. 1009): wynik wrażliwy na margines, dobierany z doświadczenia

### Chopra, Hadsell, LeCun 2005 — Learning a Similarity Metric Discriminatively, with Application to Face Verification
- nie pobrane, w pracy niecytowane
- CVPR 2005, vol. 1, str. 539–546
- PDF: http://yann.lecun.com/exdb/publis/pdf/chopra-05.pdf
- SigNet cytuje contrastive loss właśnie z tej pracy (poz. [15])

### Koch, Zemel, Salakhutdinov 2015 — Siamese Neural Networks for One-shot Image Recognition
- nie pobrane, w pracy niecytowane
- ICML Deep Learning Workshop 2015
- PDF: https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf

## Sieci dla podpisów w postaci obrazów (rozdz. 2, 5)

### Dey i in. 2017 — SigNet: Convolutional Siamese Network for Writer Independent Offline Signature Verification
- plik: dey2017.pdf (arXiv v2)
- arXiv:1707.02131, 2017
- cytowane w: 1, 2.1, 2.4, 2.5, 3.1, 3.3, 4.1, 4.3, 5.3, 5.5
- rozdz. 1 (str. 1): online zwykle lepsze, ale wymaga sprzętu; czeki i dokumenty tylko jako obraz (2.1)
- rozdz. 1 (str. 2): WI bez ponownego trenowania po dodaniu osoby, przykład banku (Wstęp, 2.1, 3.3)
- rozdz. 2.1 (str. 2): skalowanie do 155×220 (bez zachowania proporcji), odwrócenie, dzielenie przez odchylenie; nic o usuwaniu tła (2.5, 4.1, 5.5)
- rozdz. 2.2 (str. 2): budowa CNN (splot, łączenie, ReLU), spadek gradientu, porcje danych (2.4)
- rozdz. 2.3, wzór (1) (str. 3): contrastive loss, margines m = 1, odległość euklidesowa (2.5, 4.3)
- tab. 1 (str. 4): 4 warstwy splotowe, 2 w pełni połączone (1024, 128) (2.5)
- tab. 2 (str. 4): RMSprop, lr 1e-4, 20 epok, batch 128 (2.5)
- rozdz. 3.1.1 (str. 4): opis CEDAR, każdy fałszerz podrabiał 3 osoby po 8 razy
- rozdz. 3.2, wzór (2) (str. 5): dokładność = najlepszy próg na zbiorze testowym (2.5, 5.5)
- rozdz. 3.3 i tab. 3 (str. 5): CEDAR 50 osób trening / 5 test, pary zrównoważone (2.5, 3.3, 5.5)
- tab. 4 (str. 6): CEDAR 100%, FAR 0, FRR 0 (2.5, 5.5); GPDS300 bez fałszerstw w treningu 76,83% → 65,36% (2.5, 5.3)
- rys. 3 (str. 6): model z CEDAR na innych zbiorach 54–64% (2.5)

### Hafemann, Sabourin, Oliveira 2017 — Learning Features for Offline Handwritten Signature Verification using Deep CNNs
- plik: hafemann2017features.pdf (arXiv v1, 35 stron)
- Pattern Recognition, vol. 70, str. 163–176, DOI 10.1016/j.patcog.2017.05.012
- strony poniżej wg arXiv, w czasopiśmie inne
- cytowane w: 2.1, 2.3, 2.4, 3.1, 4.1, 5.5
- rozdz. 1 (str. 2): na obrazie brak informacji o ruchu pióra; żaden sposób wyznaczania cech nie okazał się najlepszy (2.3)
- rozdz. 2.1 (str. 5–6): WD najczęstsze, WI zwykle gorsze, złożoność WD rośnie z liczbą osób (2.1)
- rozdz. 2.2 (str. 7): CNN – lokalne połączenia i wspólne wagi (2.4)
- rozdz. 3 (str. 8): uczenie cech niezależne od autora + klasyfikator zależny od autora; CNN wyznacza cechy lokalnie (2.3, 2.4)
- rozdz. 3.3 (str. 13): środek masy na dużym tle, Otsu (tło = 255, atrament w skali szarości), odwrócenie, zmiana rozmiaru (2.3, 4.1)
- tab. 3 (str. 16): CEDAR 55 osób, 24 + 24 (3.1)
- tab. 4 (str. 18): CEDAR – klasyfikator każdej osoby uczony na 12 jej podpisach, negatywy to podpisy innych osób (5.5)
- tab. 9 (str. 27): CEDAR EER 4,63% (SigNet-F, 12 podpisów wzorcowych) (2.3, 5.5)
- ich sieć też nazywa się „SigNet”, ale to inna sieć niż Dey i in.

## Zbiór danych (rozdz. 3)

### CEDAR Signature Dataset (Kaggle)
- https://www.kaggle.com/datasets/shreelakshmigp/cedardataset
- cytowane w: 3.1

## Przygotowanie obrazów (rozdz. 4)

### Otsu 1979 — A Threshold Selection Method from Gray-Level Histograms
- plik: otsu1979.pdf
- IEEE Trans. on Systems, Man, and Cybernetics, vol. SMC-9, nr 1, str. 62–66, DOI 10.1109/TSMC.1979.4310076
- w PDF-ie na str. 62 jest też koniec innego artykułu, Otsu zaczyna się w prawej kolumnie
- cytowane w: 4.1
- abstrakt (str. 62): automatyczny wybór progu tylko z histogramu, bez nadzoru
- rozdz. II (str. 63): piksele dzielone progiem k na dwie klasy
- wzór (14) (str. 63): wariancja międzyklasowa ω0·ω1·(μ1 − μ0)² – w tej postaci w pracy
- wzory (18)–(19) (str. 63): wybierany próg, przy którym wariancja międzyklasowa jest największa
- tekst w PDF-ie słabo rozpoznany (OCR), wzory sprawdzać na obrazie strony

## Sieci splotowe i trening (rozdz. 2, 4)

### Goodfellow, Bengio, Courville 2016 — Deep Learning
- bez PDF-a, strona: https://www.deeplearningbook.org/contents/convnets.html
- MIT Press, 2016
- cytowane w: 2.4
- wstęp rozdz. 9 (ok. str. 326): definicja sieci splotowej (dane w siatce, splot zamiast mnożenia macierzy)
- rozdz. 9.1: filtr i mapa cech
- rozdz. 9.2 (ok. str. 329): rzadkie połączenia (mniej parametrów), wspólne wagi, równoważność względem przesunięcia
- rozdz. 9.3 (ok. str. 335): warstwa = splot + aktywacja (np. ReLU) + łączenie; łączenie daje odporność na małe przesunięcia
- numery stron z nagłówków strony internetowej, niepewne; w pracy cytuję samą pozycję
- inne przydatne rozdziały (niecytowane): 7.4 augmentacja, 7.8 wczesne zatrzymanie, 7.12 dropout, 8.5.3 Adam, 8.7.1 BatchNorm

### Kingma, Ba 2015 — Adam: A Method for Stochastic Optimization
- plik: kingma2015.pdf (arXiv v9)
- ICLR 2015, arXiv:1412.6980, strony wg arXiv
- cytowane w: 4.3
- rozdz. 1 (str. 1): osobny, dopasowywany krok uczenia dla każdego parametru, z pierwszego i drugiego momentu gradientów
- algorytm 1 (str. 2): domyślnie α = 0,001 (u mnie lr 1e-3)

### Ioffe, Szegedy 2015 — Batch Normalization
- plik: ioffe2015.pdf (arXiv v3)
- ICML 2015, PMLR vol. 37, str. 448–456; strony poniżej wg arXiv
- cytowane w: 4.2
- algorytm 1 (str. 3): normalizacja średnią i wariancją z mini-batcha, potem γ i β
- rozdz. 3.1, algorytm 2 (str. 4): przy ocenie statystyki z całego treningu (dlatego `model.eval()`)
- abstrakt, rozdz. 3.4 (str. 1, 5): większy krok uczenia, działa jak regularyzacja

### Srivastava i in. 2014 — Dropout: A Simple Way to Prevent Neural Networks from Overfitting
- plik: srivastava2014.pdf
- JMLR vol. 15, str. 1929–1958; strony wg czasopisma (str. 1 w PDF = str. 1929)
- cytowane w: 4.2
- abstrakt (str. 1929): losowe wyłączanie neuronów w treningu przeciw przeuczeniu
- rys. 2 (str. 1931): przy teście wszystkie neurony włączone, wagi razy p
- u nich p = prawdopodobieństwo, że neuron zostaje; w PyTorch p = prawdopodobieństwo wyłączenia (moje 0,3 w PyTorch = p 0,7 u nich)

### Shorten, Khoshgoftaar 2019 — A survey on Image Data Augmentation for Deep Learning
- plik: shorten2019.pdf
- Journal of Big Data 6, 60, DOI 10.1186/s40537-019-0197-0; strony „Page N of 48”
- cytowane w: 2.4, 4.3, 5.2
- abstrakt (str. 1): definicja przeuczenia, augmentacja jako sposób na mało danych (2.4, 4.3)
- str. 7: „bezpieczeństwo” augmentacji = prawdopodobieństwo zachowania etykiety (5.2)
- str. 8: obrót – bezpieczne tylko małe kąty; przesunięcie – puste miejsce wypełniane stałą (4.3)
- nic o pogrubianiu/pocienianiu kresek

### LeCun, Bottou, Bengio, Haffner 1998 — Gradient-Based Learning Applied to Document Recognition
- nie pobrane, w pracy niecytowane
- Proceedings of the IEEE, vol. 86, nr 11, str. 2278–2324

## Wyniki i dyskusja (rozdz. 2, 5)

### Geirhos i in. 2020 — Shortcut Learning in Deep Neural Networks
- plik: geirhos2020.pdf (arXiv v5)
- Nature Machine Intelligence, vol. 2, nr 11, str. 665–673, DOI 10.1038/s42256-020-00257-z; strony wg arXiv
- cytowane w: 2.6, 5.3
- abstrakt: „shortcut” = reguła, która działa na typowym teście, ale nie w trudniejszych warunkach
- rozdz. 1 (str. 2): krowa rozpoznawana po trawie
- rozdz. 1, rys. 1 (str. 2–3): zapalenie płuc rozpoznawane po znaczniku szpitala
- rozdz. 4.1 (str. 7): obciążenie zbioru danych (dataset bias)
- rozdz. 4.2 (str. 8) i 6.3 (str. 14–15): sieć bierze dowolną wystarczającą cechę; wpływ budowy sieci, straty, optymalizacji
- rozdz. 6.1 (str. 11–12): ostrożna interpretacja, sprawdzanie prostych metod bez zamierzonych cech

## Nie pobrane (opcjonalne)
- Pal i in. 2016, zbiór BHSig260, tylko jeśli użyję drugiego zbioru
- Paszke i in. 2019, PyTorch, arXiv:1912.01703, tylko jeśli promotor każe cytować narzędzia

## Do znalezienia
- artykuł o tym, że złe dzielenie osób daje zawyżone wyniki na CEDAR – nie znaleziony; w pracy zamiast tego przykład Kalery (te same osoby w treningu i teście, 3.3) i SigNet (próg z testu, 5.5)
- czy ktoś w literaturze opisał różnicę tła między prawdziwymi podpisami a fałszerstwami w CEDAR – nie znalazłem
