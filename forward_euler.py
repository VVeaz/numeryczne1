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
xZ = []

xminZ = xmin
xZ.append(xminZ)
iZ = 1
dxZ = dx

mn = 1.01
while xminZ < xmax:
    xZ.append(xZ[iZ-1] + dxZ)
    dxZ *= mn
    xminZ = xZ[iZ]
    iZ += 1

sol = x * 0.
sol[0] = y0
print(type(x))
print(xZ)

xZnumpy = array(xZ)
solZ = xZnumpy * 0.
solZ[0] = y0

dxZ = dx
for i in range(1, size(solZ)):
    solZ[i] = solZ[i - 1] + dxZ * solZ[i - 1]
    dxZ *= mn

for i in range(1, npoints):
    sol[i] = sol[i - 1] + dx * sol[i - 1]

sol_exact = exp(x)

plt.figure()
plt.plot(x, sol, 'k')
plt.plot(x, sol_exact, '--k')
plt.plot(xZnumpy, solZ, 'r')
plt.title("forward euler")
plt.show()
