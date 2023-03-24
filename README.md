# Python wczytywanie pliku csv
Metody wczytywania pliku csv be użycia oraz użyciem pandas.  
Spis treści: 
* [Opis programu](#opis-programu)
* [Teoria](#teoria)
* [Technologie](#technologie)
* [Kod programu 1](#kod-programu-1)
* [Wynik 1](#wynik-1)
* [Zastosowanie Pandas](#zastosowanie-pandas)
* [Kod programu 2](#kod-programu-2)
* [Wynik 2](#wynik-2)
* [FFT](#FFT)
* [Kod programu 3](#kod-programu-3)
* [Wynik 3](#wynik-3)
* [Program z dodanym szumem gaussowskim](#program-z-dodanym-szumem-gaussowskim)
* [Kod programu 4](#kod-programu-4)
* [Wynik 4](#wynik-4)
## Opis programu
Program wczytuje plik z danymi data.csv. Znajdują się w nim pomiary z akcelerometru w osiach x, y, z wykonywane z częstotliwością 6666[Hz]. 
Program dodaje na początek przedrostek czasu oraz na koniec kolumnę z przyspieszeniem wypadkowym oraz 
zapisuje całość jako nowy plik csv nie używając pandas. Program odczytuje pierwszy wiersz, który określa nazwy tych danych ax,ay,az.

Drugi program wykonuje to samo przy pomocy biblioteki pandas.

Program trzeci oblicza FFT dla wszystkich osi, a wyniki przedstawione na wykresie z moliwością zapisu je do pliku. A także wynacenie częstotliwości wiodącej przy pomocy biblioeki pandas.

W program czwarty dodano sygnał szumu oraz jego odfiltrowanie stosując pasmowo przepustowy filtr Butterwortha.

## Teoria
Przyspieszenie wypadkowe akcelerometru to przyspieszenie, z jakim zmienia się prędkość akcelerometru w trzech osiach, x, y i z. 
Jest to miara siły, z jaką akcelerometr przyspiesza lub zwalnia w trzech wymiarach.

Przyspieszenie wypadkowe akcelerometru można obliczyć ze wzoru:

a = sqrt(ax^2 + ay^2 + az^2)

gdzie:

* a - przyspieszenie wypadkowe,
* ax - przyspieszenie wzdłuż osi x,
* ay - przyspieszenie wzdłuż osi y,
* az - przyspieszenie wzdłuż osi z,
* sqrt - funkcja pierwiastka kwadratowego.

FFT (Fast Fourier Transform) to algorytm wykorzystywany do obliczenia szybkiej transformaty Fouriera, 
czyli przekształcenia sygnału z dziedziny czasu na dziedzinę częstotliwości.

Link do manuala numpy: https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html

Wzór na dyskretną transformatę Fouriera (DFT) wygląda następująco:

X[k] = suma(x[n]exp(-2pijn*k/N))

gdzie:

x[n] to próbki sygnału w dziedzinie czasu,
X[k] to wartości sygnału w dziedzinie częstotliwości,
j to jednostka urojona, zdefiniowana jako pierwiastek z -1,
N to liczba próbek sygnału.

FFT to szybki algorytm obliczania DFT, który znacznie przyspiesza proces przekształcania 
sygnału z dziedziny czasu na dziedzinę częstotliwości, szczególnie dla dużych ilości próbek.

## Technologie
W programie pierwszym wykorzystane są dwa moduły wbudowane w Pythona: csv i math.
Moduł csv umożliwia wczytanie i zapisanie danych w formacie csv (ang. comma-separated values). 
Ten moduł udostępnia odczyt danych csv (csv.reader()) i zapis csv (csv.writer()), które pozwalają na łatwe operowanie na plikach csv.
Moduł math zawiera funkcje matematyczne, które są wykorzystane w programie do obliczenia przyspieszenia wypadkowego.

W programie drugim użyto metody pd.read_csv() do wczytania pliku csv do obiektu DataFrame. Następnie dodano kolumnę z czasem za pomocą metody df.insert(). Obliczono przyspieszenie wypadkowe przy użyciu funkcji lambda i metody df.apply(). Na koniec zapisano ramkę danych do pliku csv przy użyciu metody df.to_csv().

W programie trzecim została użyta biblioteka pandas do operacji na ramkach danych, 
biblioteka numpy do obliczeń numerycznych,biblioteka matplotlib do wyświetlania wykresów oraz biblioteka csv do wczytywania i zapisywania danych do plików CSV.

### Kod programu 1
```
import csv
import math

# Otwarcie pliku csv do odczytu
with open('data.csv', 'r') as file:
    # Utworzenie czytnika csv
    reader = csv.reader(file)

    # Odczytanie nagłówka z pierwszego wiersza
    header = next(reader)

    # Dodanie kolumny z czasem na początku nagłówka
    header.insert(0, 'time')

    # Utworzenie listy do przechowywania danych
    data = []

    # Przetworzenie każdego wiersza z pliku
    for row in reader:
        # Odczytanie pomiarów z osi x, y i z
        x, y, z = float(row[0]), float(row[1]), float(row[2])

        # Obliczenie przyspieszenia wypadkowego
        acceleration = math.sqrt(x**2 + y**2 + z**2)

        # Dodanie czasu na początek wiersza
        row.insert(0, str(len(data) / 6666.0))

        # Dodanie przyspieszenia wypadkowego na koniec wiersza
        row.append(str(acceleration))

        # Dodanie wiersza do listy danych
        data.append(row)

# Otwarcie pliku csv do zapisu
with open('nowy_data.csv', 'w', newline='') as file:
    # Utworzenie pisarza csv
    writer = csv.writer(file)

    # Zapisanie nagłówka
    writer.writerow(header)

    # Zapisanie danych
    writer.writerows(data)
```
## Wynik 1
![image](https://user-images.githubusercontent.com/76017554/227410566-21e8a221-3b0a-4f7b-93b5-1e8c0a4acab6.png)

## Zastosowanie Pandas
### Kod proggramu 2
```
import pandas as pd
import math

# Wczytanie danych z pliku csv
data = pd.read_csv('data.csv')

# Obliczenie przyspieszenia wypadkowego
acceleration = data.apply(lambda row: math.sqrt(row['ax']**2 + row['ay']**2 + row['az']**2), axis=1)

# Dodanie czasu na początek ramki danych
time = pd.Series([i / 6666.0 for i in range(len(data))])
data.insert(0, 'time', time)

# Dodanie kolumny z przyspieszeniem wypadkowym na koniec ramki danych
data['acceleration'] = acceleration

# Zapisanie danych do pliku csv
data.to_csv('nowy_data.csv', index=False)

```
## Wynik 2
![image](https://user-images.githubusercontent.com/76017554/227410260-cfa01776-309f-4b03-9464-0406a83145bb.png)

## FFT
W tymfragmencie kodu wykorzystuje się funkcję fft z biblioteki NumPy do obliczenia dyskretnej transformaty Fouriera (FFT) 
dla każdej osi pomiarów akcelerometru (ax, ay, az).

Funkcja np.fft.fft() zwraca wynik w postaci wektora liczb zespolonych. Aby uzyskać jedynie wyniki dla częstotliwości dodatnich, 
korzysta się z indeksowania i wybiera się tylko pierwszą połowę wektora (do punktu n//2), ponieważ reszta jest lustrzanym odbiciem.

Wektor częstotliwości f jest tworzony przez funkcję np.linspace(), która generuje równomiernie rozmieszczone wartości w podanym przedziale. W tym przypadku przedział zaczyna się od zera i kończy na połowie częstotliwości próbkowania (fs/2) z krokiem równym odstępowi między próbkami (1/n), dlatego ilość elementów wynosi n//2.


### Kod programu 3

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych z pliku csv
data = pd.read_csv('data.csv')

# Wyznaczenie częstotliwości próbkowania
fs = 6666.0

# Wyznaczenie liczby próbek
n = len(data)

# Tworzenie wektora częstotliwości
f = np.linspace(0, fs/2, n//2)

# Obliczanie FFT dla każdej osi
fft_x = np.fft.fft(data['ax'])[:n//2]
fft_y = np.fft.fft(data['ay'])[:n//2]
fft_z = np.fft.fft(data['az'])[:n//2]

# Obliczanie widma amplitudowego
fft_mag = np.sqrt(np.abs(fft_x)**2 + np.abs(fft_y)**2 + np.abs(fft_z)**2)

# Rysowanie wykresu widma amplitudowego
plt.plot(f, fft_mag)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.show()

# Zapisywanie wyników do pliku csv
fft_data = pd.DataFrame({'frequency': f, 'magnitude': fft_mag})
fft_data.to_csv('fft_data.csv', index=False)

# Znajdowanie częstotliwości wiodącej
freq_index = np.argmax(fft_mag)
leading_freq = f[freq_index]
print('Częstotliwość wiodąca: {:.2f} Hz'.format(leading_freq))
```
## Wynik 3
![image](https://user-images.githubusercontent.com/76017554/227413595-cdf7800b-e6c2-439a-a631-a0d477f57d76.png)

## Program z dodanym szumem gaussowskim

Dodano do programu szum gaussowski o amplitudzie równoważnej 1/10 maksymalnej wartości przyspieszenia wypadkowego. 
Następnie filtruje się szum i sygnał przy użyciu filtra pasmowo-przepustowego Butterwortha, którego częstotliwości graniczne wynoszą odpowiednio 5 Hz i 20 Hz. 
Na końcu obliczane jest widmo amplitudowe sygnału za pomocą transformaty Fouriera.
W kodzie został zastosowany jeden filtr typu pasmowo-przepustowego Butterwortha. Jest to filtr, który przepuszcza sygnały o częstotliwościach zawartych w określonym paśmie, a tłumi sygnały o częstotliwościach poza tym pasmem. 

### Kod Programu 4
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Wczytanie danych z pliku csv
data = pd.read_csv('data.csv')

# Obliczenie przyspieszenia wypadkowego
data['acceleration'] = np.sqrt(data['ax']**2 + data['ay']**2 + data['az']**2)

# Dodanie czasu na początek ramki danych
time = pd.Series([i / 6666.0 for i in range(len(data))])
data.insert(0, 'time', time)

# Przetwarzanie danych
serie = data['acceleration']
amp = np.max(serie) / 10.0
noise = np.random.normal(-amp, amp, len(serie))
serie = serie + noise
fs = 1 / (time.iloc[1] - time.iloc[0]) # fs to częstotliwość próbkowania
order = 4 #rząd filtru Butterwortha
flow = 5.0#dolna częstotliwość graniczna
fhigh = 20.0#górna częstotliwość graniczna
fnyquist = fs / 2 #częstotliwość Nyquista, czyli połowa częstotliwości próbkowania
low = flow / fnyquist # low i high określają częstotliwości graniczne dla filtru pasmowoprzepustowego Butterwortha
high = fhigh / fnyquist
b, a = butter(order, [low, high], btype='band')
serie = lfilter(b, a, serie)

# Obliczanie FFT
n = len(serie) #oblicza długość sygnału czasowego wejściowego.

#Generuje tablicę wartości częstotliwości odpowiadających wynikowi FFT, sięgającą od 0 Hz 
#do częstotliwości Nyquista (połowa częstotliwości próbkowania) z krokiem fs/(2*(n//2))
f = np.linspace(0, fs/2, n//2)

#Stosuje algorytm FFT na wejściowym sygnale czasowym i zwraca tylko pierwszą połowę 
#wyniku sprzężonego zespolonego. Dzieje się tak, ponieważ FFT rzeczywistego sygnału ma właściwość symetrii, 
#w której druga połowa wyniku jest sprzężeniem zespolonym pierwszej połowy. 
#Ponieważ potrzebujemy tylko informacji o składowych częstotliwości dodatnich, odrzucamy drugą połowę wyniku.
fft_serie = np.fft.fft(serie)[:n//2]

#oblicza amplitudę wyniku FFT
fft_mag = np.abs(fft_serie)

# Znajdowanie częstotliwości wiodącej, czyli największa amplituda
freq_index = np.argmax(fft_mag)
leading_freq = f[freq_index]
print('Częstotliwość wiodąca: {:.2f} Hz'.format(leading_freq))
#Funkcja np.argmax() zwraca indeks pierwszego wystąpienia maksymalnej wartości w tablicy fft_mag, 
# która zawiera wynik transformaty Fouriera.

#Indeks ten następnie jest używany do wyznaczenia częstotliwości, 
# dla której występuje maksymalna wartość, na podstawie wektora częstotliwości f.

#Ostatecznie, uzyskana wartość częstotliwości wiodącej jest wyświetlana na konsoli w jednostce Hz, 
# za pomocą metody format() i łańcucha formatującego '{:.2f} Hz'. 
# Wartość '{:.2f}' oznacza, że zostanie wyświetlona liczba zmiennoprzecinkowa z dwoma miejscami po przecinku.

# Wykres widma amplitudowego
plt.plot(f, fft_mag)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.show()

```

## Wynik 4

![image](https://user-images.githubusercontent.com/76017554/227420886-c4c322e9-0078-4a91-a1f9-877250888d38.png)



