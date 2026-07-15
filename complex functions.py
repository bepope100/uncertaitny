import matplotlib.pyplot as plt
import numpy as np
import math

def f(x,t):
    return np.sin(t*x)

real_step = 20
imaginary_step = 20
resolution = 5
real = np.linspace(-resolution,resolution,real_step)
imaginary = np.linspace(-resolution,resolution,imaginary_step)
x,y = np.meshgrid(real,imaginary,indexing="ij")
running = True
t=0

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111,projection="3d")
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_zlabel("|f(z)|")
complex_grid = x + (1j *y)
try :
    while running:
        t+=0.001

        
        values = f(complex_grid,t)
        imag = np.imag(values)
        real = np.real(values)

        

        ax.plot_surface(x, y, real,facecolors = plt.cm.jet(imag))
        plt.show()
except KeyboardInterrupt:
    pass



