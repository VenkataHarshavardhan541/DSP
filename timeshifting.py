import numpy as np
from matplotlib import pyplot as plt


#Time Shifting
x1_n = [1,2,3,0,0,0]
N1 = len(x1_n)
omega = np.linspace(-np.pi, np.pi, 1000)
x_w = np.array([np.sum(x1_n * np.exp(-1j * k * np.arange(N1))) for k in omega])
x_shift = np.roll(x1_n, 3)
X_theoretical = x_w * np.exp(-1j * omega * 3)
x_shift_w = np.array([np.sum(x_shift * np.exp(-1j * k * np.arange(N1))) for k in omega])
if (x_shift_w.all() == X_theoretical.all()):
	print("Time shifting test pass")
else:
	print("Error")