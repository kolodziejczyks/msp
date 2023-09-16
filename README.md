# Bot automatyzujący MSP
Plan jest taki, aby stworzyć bota do automatyzacji nudnych tasków na MSP. Jest wiele naprawdę nieciekawych czynności, których nigdy nie chce mi się robić, więc wolę napisać bota niż czekać milion lat, aż ta durna aplikacja się załaduje. 

Sęk w tym, aby móc odpalić to headlessly na serwerze i móc zapomnieć o tym i niech to sobie działa w tle i zarabia mi fejma.

Pierwszy etap to będzie po prostu logowanie się i wylogowywanie się automatycznie.

### OCR
- Za pomocą OCR chcę znajdować lokalizację różnych przycisków, aby móc bez durnego wpisywania koordynatów klikać elementy i wykonywać zautomatyzowane akcje.
- Dla zwiększenia wydajności chciałbym puszczać pewnego rodzaju smoke test, zapisywać koordynaty wszystkich przycisków potrzebnych do wykonywania akcji oraz później odnosić się do tych wartości i pomijać cały OCR. 

### Automatyzacja wielu kont
Chcę stworzyć system, który pozwoli na wrzucenie listy kont i sam zajmie się jedną z kilku akcji typu: oglądanie filmów, dawanie autografów itp. W przypadku posiadania jakiegoś sensownego setu kont można by np. obejść problem dawania autografów co godzinę - gdy masz 30 kont z 20 lvl-em jesteś w stanie bez problemu wrzucać komuś taki jeden autograf z interwałem 2-minutowym. Daje to sensowny wynik, oczywiście nadal mniej niż oglądanie filmów, lecz będzie to dużo mniej problematyczne do automatyzacji.

### Trenowanie kont na sobie
Bardzo przydatną funkcjonalnością byłoby levelowanie kont na sobie - podawałoby się im dane i system mógłby w kilku / kilkunastu kontenerach uruchamiać wiele instancji skryptów na raz, aby levelować jedno konto do pewnego pułapu, następnie powtarzać to dla każdego kolejnego w danym zestawie. Skutkuje to większą wydajnością danego setu.
