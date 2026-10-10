# Zasady formatowania pracy

Dwa źródła zasad:
- szablon wydziałowy WEII (`docs/weiiszablon_oryginal.tex`, `praca/weiiszablon.sty`)
- uwagi od promotora (`literatura_pdf/Uwagi.docx`), ogólne, pisane pod Worda

Promotor sam pisze, że trzeba uwzględnić wymagania wydziału, więc przy różnicach zostaję przy szablonie WEII.

## Różnice między promotorem a szablonem WEII
- marginesy: promotor góra/dół 2,5 cm, boki 2 cm; WEII lustrzane 2 cm + 1,5 cm na oprawę → zostaje WEII
- wcięcie akapitu: promotor ok. 8 mm; WEII 1,25 cm → zostaje WEII
- podpisy rysunków i tabel: promotor kursywa 10 pkt; WEII prosto 9 pkt → zostaje WEII, zapytać promotora
- odwołania do rysunków w tekście: promotor kursywą; WEII zwykłą czcionką → zostaje WEII
- numer przy Wprowadzeniu i Podsumowaniu: promotor „zwykle nie”; WEII numerowane → zostaje WEII, zapytać promotora
- format literatury: promotor tytuł kursywą w cudzysłowie i „s.”; WEII tytuł zwykłą czcionką i „str.” → zostaje WEII

## Zasady promotora, które stosuję (zgodne z WEII)
- Times 12 pkt, interlinia 1,5, rozdziały od prawej strony
- podpis rysunku pod rysunkiem, podpis tabeli nad tabelą
- przed rysunkiem, tabelą i wzorem akapit, który się do nich odwołuje
- odwołania przez `\ref`, nigdy wpisane na sztywno; do wzorów w nawiasie: `(\ref{...})`
- skrót przy pierwszym użyciu z rozwinięciem: SKRÓT (ang. *rozwinięcie* -- tłumaczenie), do tego wykaz skrótów na początku pracy
- nie robić numerowanych podrozdziałów z 1–2 akapitów, zamiast tego `\subsubsection*{}` (pogrubiony tytuł bez numeru i bez spisu treści)
- nie robić pojedynczego podrozdziału na danym poziomie (np. samo 4.1 bez 4.2)
- nazwy własne (pliki, zmienne, funkcje) w `\texttt{}`
- jednoliterowe spójniki z tyldą (`w~`, `i~`, `z~`, `a~`, `o~`, `u~`)
- polskie cudzysłowy ,,…'', przecinek w liczbach dziesiętnych
- w wypunktowaniu: punkty z przecinkiem zaczynam małą literą, ostatni kończę kropką
- bez kropki na końcu tytułów
- przecinek przed całym „w którym”, „dla których” itd., nie w środku

## Znalezione błędy
- październik 2026: tekst był w Latin Modern zamiast Times, bo szablon ładuje `lmodern` po `mathptmx`; poprawione w `weiiszablon.tex` (zmiana `\rmdefault` i czcionek matematycznych), `weiiszablon.sty` bez zmian

## Do zrobienia przed oddaniem każdej wersji
- wydrukować, przeczytać na papierze
- dać komuś do sprawdzenia pod kątem językowym
- czcionka Times New Roman na rysunkach `cedar_przyklad.png` i `tlo_histogram.png` (notebook 01), podpisy osi na `tlo_histogram` po zmniejszeniu mają ok. 7,7 pkt, a minimum to 8
- rozdz. 4 ma na razie tylko podrozdział 4.1, dojdą 4.2 (sieć) i 4.3 (trening)

## Pytania do promotora
- czy Wprowadzenie i Podsumowanie mają mieć numer (szablon WEII numeruje)
- czy podpisy rysunków i tabel kursywą, czy jak w szablonie WEII