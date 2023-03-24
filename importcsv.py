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
