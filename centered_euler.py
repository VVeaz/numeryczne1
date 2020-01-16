import matplotlib.pyplot as plt
import scipy as sp
from numpy import *

y0 = 1.  # c tilda
xmin = 0.
xmax = 10.
npoints = 1500

dx = (xmax - xmin) / float(npoints)
print(dx)
x = sp.linspace(xmin, xmax, npoints)
sol = x * 0.
sol[0] = y0
sol[1] = sol[0] + dx * sol[0]  # centered euler

for i in range(2, npoints):
    sol[i] = 2 * dx * sol[i - 1] + sol[i - 2]
    print(sol[i])

sol_exact = exp(x)

plt.figure()
plt.plot(x, sol, 'k')
plt.plot(x, sol_exact, '--k')
plt.title("centered euler")
plt.show()
