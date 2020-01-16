import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import random

nx = 50
nx_lin = 1000
x_lin = sp.linspace(0., 101., nx_lin)
x = sp.linspace(1., 100., nx)
y_lin = sp.linspace(0, 0, nx_lin)
y = sp.linspace(0, 0, nx)
SumX = 0
SumXk = 0
SumY = 0
SumXY = 0

for i in range(0, len(x)):
    y[i] = np.sin(x[i]) / random.randint(i + 5 / 5, i + 6 / 2)
    SumX += x[i]
    SumXk += (x[i] * x[i])
    SumY += y[i]
    SumXY += (x[i] * y[i])

a = (nx * SumXY - SumX * SumY) / (nx * SumXk - (SumX * SumX))
b = 1.0 / nx * (SumY - a * SumX)

for i in range(0, len(x_lin)):
    y_lin[i] = x_lin[i] * a + b
plt.plot(x, y, '.k')
plt.plot(x_lin, y_lin, '-')
plt.plot()
plt.pause(10)
