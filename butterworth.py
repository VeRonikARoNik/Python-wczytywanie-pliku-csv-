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
