import numpy as np
import matplotlib.pyplot as plt

L = 10
x_n = np.cos(0.2 * np.pi * np.arange(L))

phi = np.pi
omega = np.arange(-phi, phi, 0.001 * phi)

X_omega = np.array([np.sum(x_n * np.exp(-1j * w * np.arange(L))) for w in omega])

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(omega, np.abs(X_omega))
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('|X(ω)|')

plt.subplot(2, 1, 2)
plt.plot(omega, np.angle(X_omega))
plt.title('Phase Spectrum')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('∠X(ω)')

plt.tight_layout()
plt.show()
