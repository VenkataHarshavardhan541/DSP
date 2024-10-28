import numpy as np
import matplotlib.pyplot as plt
x = np.array([9,5,7,3])

plt.figure(figsize=(12, 8))

def plot_dft(x, title, subplot_index):
    dft = np.fft.fft(x)
    freqs = np.fft.fftfreq(len(x))
    
    plt.subplot(2, 2, subplot_index)
    plt.stem(freqs, np.abs(dft))
    plt.title(title)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.grid(True)
plot_dft(x, "DFT of Original Sample", 1)

for i in range(1, 4):
    x = np.concatenate((x, np.zeros(5 * i)))
    plot_dft(x, f"DFT after Adding {i*5} Zeros", i+1)
plt.tight_layout()
plt.show()