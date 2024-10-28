import numpy as np
import matplotlib.pyplot as plt

# Define the arrays
array1 = np.array([1, 2, 3, 4])
array2 = np.array([4, 3, 2, 1])

# Perform Fourier Transform on each array separately
fft_array1 = np.fft.fft(array1)
fft_array2 = np.fft.fft(array2)

# Add the two arrays
added_arrays = array1 + array2

# Perform Fourier Transform on the added array
fft_added_arrays = np.fft.fft(added_arrays)

# Add the Fourier Transforms of the individual arrays
fft_sum = fft_array1 + fft_array2

# Plot the results
fig, axs = plt.subplots(3, 1, figsize=(12, 18))

# Plot the original arrays
axs[0].stem(array1, linefmt='b-', markerfmt='bo', basefmt='r-', label='Array 1')
axs[0].stem(array2, linefmt='g-', markerfmt='go', basefmt='r-', label='Array 2', bottom=0.2)
axs[0].set_title('Original Arrays')
axs[0].legend()

# Plot the Fourier Transforms of the original arrays
axs[1].stem(np.abs(fft_array1), linefmt='b-', markerfmt='bo', basefmt='r-', label='FFT Array 1')
axs[1].stem(np.abs(fft_array2), linefmt='g-', markerfmt='go', basefmt='r-', label='FFT Array 2', bottom=0.2)
axs[1].set_title('Fourier Transforms of Original Arrays')
axs[1].legend()

# Plot the Fourier Transform of the summed array and the sum of the individual FFTs
axs[2].stem(np.abs(fft_added_arrays), linefmt='b-', markerfmt='bo', basefmt='r-', label='FFT Added Arrays')
axs[2].stem(np.abs(fft_sum), linefmt='g-', markerfmt='go', basefmt='r-', label='Sum of FFTs', bottom=0.2)
axs[2].set_title('FFT of Added Arrays vs Sum of FFTs')
axs[2].legend()

plt.tight_layout()
plt.show()
