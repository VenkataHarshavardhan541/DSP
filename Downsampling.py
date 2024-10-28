import numpy as np
from matplotlib import pyplot as plt
'''x=[1,2,3,4,5]
y=[]
l=2
s=0
for i in x:
	s=i*l
	y.append(s)
print(y)
plt.plot(y)
plt.show()
plt.plot(x)
plt.show()'''
signal=[1,2,3,4,5]
l=2
dsignal=signal[::l]
print(signal)
print(dsignal)
plt.plot(signal,label='Original Signal')
plt.plot(dsignal,label='Downsampled signal')
plt.legend()
plt.show()
