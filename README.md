# Python-wczytywanie-pliku-csv-
Metody wczytywania pliku csv.  
Spis treści: 
* [Opis programu](#opis-programu)
* [Teoria](#teoria)
* [Technologie](#technologie)
* [Kod programu](#kod-programu)
* [Wynik](#wynik)
* [Zastosowanie Pandas](#zastosowanie-pandas)

## Opis programu
Program wczytuje plik z danymi data.csv. Znajdują się w nim pomiary z akcelerometru w osiach x, y, z wykonywane z częstotliwością 6666[Hz]. 
Program dodaje na początek przedrostek czasu oraz na koniec kolumnę z przyspieszeniem wypadkowym oraz 
zapisuje całość jako nowy plik csv nie używając pandas. Program odczytuje pierwszy wiersz, który określa nazwy tych danych ax,ay,az.

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

## Technologie
W tym programie wykorzystane są dwa moduły wbudowane w Pythona: csv i math.

Moduł csv umożliwia wczytanie i zapisanie danych w formacie csv (ang. comma-separated values). 
Ten moduł udostępnia odczyt danych csv (csv.reader()) i zapis csv (csv.writer()), które pozwalają na łatwe operowanie na plikach csv.

Moduł math zawiera funkcje matematyczne, które są wykorzystane w programie do obliczenia przyspieszenia wypadkowego.

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
## Wynik
![image](https://user-images.githubusercontent.com/76017554/227410566-21e8a221-3b0a-4f7b-93b5-1e8c0a4acab6.png)

## Zastosowanie Pandas

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
## Reultat 
![image](https://user-images.githubusercontent.com/76017554/227410260-cfa01776-309f-4b03-9464-0406a83145bb.png)

