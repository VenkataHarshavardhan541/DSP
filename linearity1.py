import numpy as np
x1 = np.array([1, 2, 3, 4])
x2 = np.array([4, 3, 2, 1])
ft1 = np.fft.fft(x1)
ft2 = np.fft.fft(x2)
sumoftwoarrays = x1 + x2
ftsumoftwoarrays = np.fft.fft(sumoftwoarrays)
ft_sum = ft1 + ft2
print("FT of first array:", ft1)
print("FT of second array:", ft2)
print("FT of added arrays:", ftsumoftwoarrays)
print("Sum of FTs:", ft_sum)

areequal = np.allclose(ft_sum, ftsumoftwoarrays)
print("Are the summed FTs equal to the FT of the summed arrays?", areequal)