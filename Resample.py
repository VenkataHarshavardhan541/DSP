import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample

# Parameters
frequency = 200  # Frequency in Hz
duration = 0.5   # Duration in seconds
original_sample_rate = 8000  # Original sample rate in Hz
new_sample_rate = 1000  # New sample rate in Hz

# Time array for original sample rate
t_original = np.linspace(0, duration, int(original_sample_rate * duration))

# Original sine wave
waveform_original = np.sin(2 * np.pi * frequency * t_original)

# Resample the waveform
num_samples_new = int(new_sample_rate * duration)
waveform_resampled = resample(waveform_original, num_samples_new)

# Time array for new sample rate
t_new = np.linspace(0, duration, num_samples_new, endpoint=False)

# Plotting original and resampled waveforms
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t_original, waveform_original)
plt.title('Original 200 Hz Sine Wave (8 kHz Sample Rate)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t_new, waveform_resampled)
plt.title('Resampled 200 Hz Sine Wave (1 kHz Sample Rate)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
