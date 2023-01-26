# Helikopterowy-Komiwojazer

Interfejs można podzielić na pięć podstawowych składowych:
• Menu główne
• Wybór trybu
• Interfejs obsługujący rozwiązanie permutacyjne
• Interfejs obsługujący metodę podziału i ograniczeń
• Interfejs obsługujący algorytm genetyczny
W pierwszej kolejności użytkownik przekierowywany jest do menu głównego, skąd może 
przejść do kolejnego okna, przeczytać informacje dotyczące aplikacji lub z niej wyjść.

Po wciśnięciu przycisku „START” użytkownik trafia do menu, z którego może wrócić do 
poprzedniego okna lub wybrać jeden z trzech algorytmów rozwiązujących problem komiwojażera. 
Wśród nich znajdują się:
• poglądowe rozwiązanie permutacyjne,
• metoda podziału i ograniczeń,
• algorytm genetyczny.

Każdy z podprogramów rozwiązujących TSP posiada dedykowany interfejs 
wykorzystujący implementacje bibliotek matplotlib oraz turtle, pozwalających na wprowadzanie 
danych przy użyciu myszy komputerowej. Wyjątek stanowi tutaj podprogram algorytmu 
genetycznego, do którego użytkownik musi najpierw podać liczbę pokoleń do rozpatrzenia, za 
pomocą terminala. Ze względu na wysoką złożoność czasową oraz konieczność sprawdzenia 
każdego rozwiązania, niezalecane jest korzystanie z rozwiązania permutacyjnego dla więcej niż 
11 wprowadzonych miast. Wciśnięcie przycisku „Q” (spacji dla metody podziału i ograniczeń) po 
naniesieniu na mapę punktów, rozpoczyna pracę algorytmu. Dla metody podziału i ograniczeń, 
zaimplementowano dodatkowe funkcjonalności. Po naciśnięciu przycisku „C” algorytm stara się
nie przecinać trasy. Po wciśnięciu przycisku „V” program pokazuje trasy pośrednie, a po 
naciśnięciu klawisza „F”, pokazywana jest tylko pierwsza wygenerowana trasa.
Następnie w terminalu prezentowany jest wynik obliczeń w postaci długości najkrótszej 
ścieżki oraz czasu pracy. Dla metody podziału i ograniczeń wynik zaprezentowany jest w oknie 
wygenerowanym przez moduł turtle.
W celu powrócenia do okna wyboru trybu i wybrania nowego algorytmu, użytkownik musi 
najpierw zamknąć okno, w którym zakończone zostały obliczenia.
