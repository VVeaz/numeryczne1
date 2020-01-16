import matplotlib.pyplot as plt
import scipy as sp
from numpy import *

y0 = 1.  # c tilda
xmin = 0.
xmax = 10.
npoints = 150

dx = (xmax - xmin) / float(npoints)
print(dx)
x = sp.linspace(xmin, xmax, npoints)
sol = x * 0.
sol[0] = y0

for i in range(1, npoints):
    sol[i] = sol[i - 1] / (1 - dx)
    # print(sol[i])

sol_exact = exp(x)

plt.figure()
plt.plot(x, sol, 'k')
plt.plot(x, sol_exact, '--k')
plt.title("backward euler")
plt.show()
