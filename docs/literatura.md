# Literatura

## Weryfikacja podpisu (rozdz. 1, 2)

### Hafemann, Sabourin, Oliveira 2017 — Offline Handwritten Signature Verification: Literature Review
- przeczytany abstrakt i rozdz. II
- IPTA 2017, DOI 10.1109/IPTA.2017.8310112, strony do sprawdzenia
- PDF: https://arxiv.org/pdf/1507.07909
- abstrakt, 1. zdanie: dziedzina badana od dekad, nadal problem otwarty, cytowane we Wstępie
- abstrakt, 4. zdanie: uczenie głębokie uczy się cech z obrazów podpisów, cytowane we Wstępie
- rozdz. I: rodzaje fałszerstw (losowe, proste, wykwalifikowane), cytowane w 3.4
- rozdz. II: writer-dependent i writer-independent, cytowane w 3.3
- rozdz. II.A: duża zmienność podpisów jednej osoby, mało próbek na osobę
- rozdz. VI-F: definicje FRR, FAR, EER
- tabela IV: wyniki innych metod na CEDAR, do porównania w rozdz. 5
- numeracja rozdziałów wg wersji z arXiv, w wersji IPTA może być inna
- czytać jako pierwsze, dobry start do rozdz. 2

### Jain, Ross, Prabhakar 2004 — An Introduction to Biometric Recognition
- nieprzeczytane
- IEEE Trans. on Circuits and Systems for Video Technology, vol. 14, nr 1, str. 4–20
- PDF: https://cse.msu.edu/~rossarun/pubs/RossBioIntro_CSVT2004.pdf
- rozdz. II: weryfikacja (1:1) i identyfikacja (1:N)
- podpis jako biometria behawioralna
- używa nazw FMR/FNMR zamiast FAR/FRR i nie ma EER, te definicje brać z Hafemanna

## Sieci syjamskie i funkcja straty (rozdz. 2, 4)

### Bromley i in. 1993 — Signature Verification using a "Siamese" Time Delay Neural Network
- przeczytane
- NIPS 6 (1993), str. 737–744
- PDF: https://proceedings.neurips.cc/paper_files/paper/1993/file/288cc0ff022877bd3df94bc9360b9c5d-Paper.pdf
- abstrakt: definicja sieci syjamskiej, cytowane we Wstępie
- rozdz. 4: współdzielone wagi, proporcje par 50/40/10
- przypis 1 (str. 741): fałszerstwa losowe to oryginały innych osób, do rozdz. 3.4
- rozdz. 2: fałszerstwa wykwalifikowane są najtrudniejsze
- podpisy z tabletu (online), nie obrazy

### Hadsell, Chopra, LeCun 2006 — Dimensionality Reduction by Learning an Invariant Mapping
- nieprzeczytane
- CVPR 2006, str. 1735–1742, DOI 10.1109/CVPR.2006.100
- PDF: http://lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf
- rozdz. 2: definicja contrastive loss z marginesem m, numer wzoru do sprawdzenia
- oryginalne źródło funkcji straty, której używam, do rozdz. 2 i 4
- Y=0 oznacza parę podobną (w surveyu Li 2022 jest odwrotnie)

### Chopra, Hadsell, LeCun 2005 — Learning a Similarity Metric Discriminatively, with Application to Face Verification
- nieprzeczytane
- CVPR 2005, strony do sprawdzenia
- PDF: http://yann.lecun.com/exdb/publis/pdf/chopra-05.pdf
- wcześniejsza wersja pomysłu contrastive loss
- sieć syjamska z CNN do weryfikacji twarzy, podobny problem jak z podpisami

### Koch, Zemel, Salakhutdinov 2015 — Siamese Neural Networks for One-shot Image Recognition
- nieprzeczytane
- ICML Deep Learning Workshop 2015, dokładny opis sprawdzić w Google Scholar („Cytuj”)
- PDF: https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf
- abstrakt: sieć działa też dla zupełnie nowych klas
- rozdz. 3.2: strata cross-entropy zamiast contrastive
- zbiór Omniglot (znaki pisma), nie podpisy

### Li, Chen, Zhang 2022 — A Survey on Siamese Network: Methodologies, Applications, and Opportunities
- przeczytany abstrakt i wstęp
- IEEE Trans. on Artificial Intelligence, vol. 3, nr 6, str. 994–1014, DOI 10.1109/TAI.2022.3207112
- PDF mam lokalnie
- str. 994: sieć syjamską jako pierwszy zaproponował Bromley
- str. 996, rys. 2: schemat sieci syjamskiej
- str. 996, wzór (5): contrastive loss, tutaj Y=1 oznacza parę podobną
- przydatny do szukania innych źródeł w bibliografii

## Sieci dla podpisów w postaci obrazów (rozdz. 2, 5)

### Dey i in. 2017 — SigNet: Convolutional Siamese Network for Writer Independent Offline Signature Verification
- przeczytany abstrakt i wstęp
- arXiv:1707.02131, 2017
- PDF: https://arxiv.org/pdf/1707.02131
- rozdz. 1: czym jest writer-independent i dlaczego nie trzeba przetrenowywać modelu, cytowane we Wstępie
- rozdz. 3.3 i tab. 3: CEDAR podzielony 50 osób trening / 5 test (u mnie 35/10/10)
- wyniki na CEDAR do porównania w rozdz. 5
- najbardziej podobna praca do mojej (sieć syjamska, CNN, contrastive loss, CEDAR)
- cytowane w 3.1 (CEDAR często używany) i 3.3 (writer-independent, podział 50/5)
- rozdz. 2.1: obrazy skalowane do 155×220, odwrócone kolory

### Hafemann, Sabourin, Oliveira 2017 — Learning Features for Offline Handwritten Signature Verification using Deep CNNs
- nieprzeczytane
- Pattern Recognition, vol. 70, str. 163–176, DOI 10.1016/j.patcog.2017.05.012
- PDF: https://arxiv.org/pdf/1705.05787
- abstrakt: na obrazie podpisu nie ma informacji o ruchu pióra
- używa CEDAR (55 osób, po 24 oryginały i 24 fałszerstwa)
- inne podejście niż sieć syjamska (uczenie cech przez CNN), do rozdz. 2
- tabela 3: CEDAR wśród używanych zbiorów, cytowane w rozdz. 3.1
- rozdz. 3.3: przygotowanie obrazów (środek masy, OTSU, odwrócenie kolorów)

## Zbiór danych (rozdz. 3)

### Kalera, Srihari, Xu 2004 — Offline Signature Verification and Identification Using Distance Statistics
- Int. Journal of Pattern Recognition and Artificial Intelligence
- mam PDF, do przeczytania rozdz. 1–2 (ok. 3 strony)
- vol. 18, nr 7 (listopad 2004), str. 1339–1360, DOI 10.1142/S0218001404003630
- źródło zbioru CEDAR
- str. 1339 (wstęp): obrazy offline bez informacji o ruchu, fałszerstwa wykwalifikowane trudne, cytowane we Wstępie
- str. 1341 (rozdz. 2.1): opis zbioru, cytowane w 3.1 i 3.2 (8-bit skala szarości)
- str. 1342 (tab. 1): podsumowanie zbioru
- str. 1349 (rozdz. 3.1.1): podział podpisów 16/8, te same osoby w treningu i teście, cytowane w 3.3
- metoda: cechy GSC na obrazach zbinaryzowanych, 78% dokładności weryfikacji (abstrakt)

## Podstawy uczenia głębokiego (rozdz. 2, 4)

### Goodfellow, Bengio, Courville 2016 — Deep Learning
- nieprzeczytane
- MIT Press, 2016
- online za darmo: https://www.deeplearningbook.org
- rozdz. 9: sieci konwolucyjne
- rozdz. 8: optymalizacja
- podręcznikowe definicje do rozdz. 2 i 4

### LeCun, Bottou, Bengio, Haffner 1998 — Gradient-Based Learning Applied to Document Recognition
- nieprzeczytane
- Proceedings of the IEEE, vol. 86, nr 11, str. 2278–2324
- klasyczne źródło CNN (LeNet), tylko gdyby był potrzebny cytat historyczny

## Do dodania później
- optymalizator, np. Adam (Kingma, Ba 2015, arXiv:1412.6980), jeśli go użyję
- PyTorch, jeśli promotor każe cytować narzędzia

## Do znalezienia
- coś o BHSig260, jeśli użyję go jako drugiego zbioru
- artykuł o tym, że złe dzielenie osób daje zawyżone wyniki na CEDAR, do rozdz. 5
- czy ktoś w literaturze opisał różnicę tła między prawdziwymi podpisami a fałszerstwami w CEDAR