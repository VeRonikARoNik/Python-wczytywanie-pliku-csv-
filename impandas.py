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
