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
