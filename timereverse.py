import numpy as np
from matplotlib import pyplot as plt
x=np.array([4,6,8,13])
revx=x[::-1]
print(revx)
ftx=np.fft.fft(x)
print("fourier transform of x",ftx)
ftrev=np.fft.fft(revx)
print("fourier transform of time reversed signal",ftrev)

plt.subplot(2,2,1)
plt.plot(ftx)
plt.subplot(2,2,4)
plt.plot(ftrev)
plt.show()
