import numpy as np
import matplotlib.pyplot as plt

frequency = 200
duration = 0.5
sample_rate = 8000

t = np.linspace(0, duration, int(sample_rate * duration))

waveform = np.sin(2 * np.pi * frequency * t)

plt.plot(t, waveform)
plt.title('200 Hz Sine Wave')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
