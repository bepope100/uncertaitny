import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return np.sin(x)

real_step = 20
imaginary_step = 20
resolution = 5
real = np.linspace(-resolution,resolution,real_step)
imaginary = np.linspace(-resolution,resolution,imaginary_step)
x,y = np.meshgrid(real,imaginary,indexing="ij")

complex_grid = x + (1j *y)
values = np.abs(f(complex_grid))

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111,projection="3d")
ax.plot_surface(x, y, values, cmap="viridis")
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_zlabel("|f(z)|")

plt.show()
