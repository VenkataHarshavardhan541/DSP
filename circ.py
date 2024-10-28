import numpy as np

x1 = [1, 2, 3, 4]
x2 = [-1, 0, 5, 3]
N = len(x1)

def cyclic_convolution(x1, x2):
    z = []
    x2_r = x2[::-1]  # Reverse x2
    for n in range(N):
        y = np.roll(x2_r, n)
        z.append(np.dot(x1, y))
        print(y)
        return z

Y = cyclic_convolution(x1, x2)
print("Cyclic Convolution Result:", Y)
