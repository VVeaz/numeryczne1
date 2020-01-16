from sympy import *
import matplotlib.pyplot as plt
import scipy as sp
from tkinter import *

x, y = symbols('x y')

shift = 1


def example_function(xi):
    return -xi ** 3 + 3 * xi ** 2 + 17 * xi - 0.25


nx = 500

range_left = -4.
range_right = 6.

iks = sp.linspace(range_left, range_right, nx)
q = sp.linspace(0, 0, nx)
os_x = sp.linspace(0, 0, nx)

for i in range(len(iks)):
    q[i] = example_function(iks[i])


def derivative(f, xi):
    return diff(f(Symbol('x'))).subs('x', xi)


def bisection(f, xL, xU, epsilon, iterations):
    xM = (xL + xU) / 2
    if f(xM) == 0:
        return xM
    if xM * xU < 0:
        xL = xM
    else:
        xU = xM
    xM_old = xM
    xM = (xL + xU) / 2

    i = 0
    while abs(xM_old - xM) / xM > epsilon and i < iterations:
        if xM * xU < 0:
            xL = xM
        else:
            xU = xM
        xM_old = xM
        xM = (xL + xU) / 2
        i += 1
    return xM


__next = 0

window = Tk()


def next_step_on_click(event):
    global __next, window
    __next = 1


button_next_step = Button(window, text="dalej", font=("Comic Sans MS", 16, "bold"), background="red")
button_next_step.bind("<Button-1>", next_step_on_click)
button_next_step.pack(fill=X)


def newton_raphson(f, xi, epsilon, iterations):
    global __next, window
    start_x = xi
    xi_old = xi
    xi = xi - (f(xi) / derivative(f, xi))
    i = 0
    q_tmp_last = sp.linspace(0, 0, nx)
    while i < iterations and abs(f(xi_old)) > epsilon:  # abs(xi_old - xi) / xi > epsilon:
        plt.clf()

        xlimL = max(float(start_x - shift), range_left)
        xlimP = min(float(start_x + shift), range_right)

        xlim = max(abs(start_x - xlimL), abs(start_x - xlimP))
        xlimL = start_x - xlim
        xlimP = start_x + xlim

        plt.xlim(xlimL, xlimP)

        plt.plot(iks, q)
        plt.plot(iks, os_x, color='black')
        plt.title("start x0 " + "= " + str(start_x) + " found " + str(xi))

        xi_old = xi
        a = derivative(f, xi)
        b = example_function(xi) - a * xi

        xi = xi - f(xi) / a
        iks_tmp = sp.linspace(int(xlimL), int(xlimP), nx)
        q_tmp = sp.linspace(0, 0, nx)

        for j in range(len(iks_tmp)):
            q_tmp[j] = a * iks_tmp[j] + b
        plt.ylim(max(q_tmp), min(q_tmp))
        plt.plot(iks_tmp, q_tmp)
        plt.plot(iks_tmp, q_tmp_last)
        q_tmp_last = q_tmp
        while __next == 0:
            plt.pause(1)
        __next = 0
        i += 1
    print("Found " + str(xi) + " f(found)= " + str(f(xi)))
    return xi


def secant(f, xi, xi_m1, epsilon, iterations):
    global __next, window
    start_x = xi
    start_x_m1 = xi_m1
    xi_old = xi
    xi = xi - ((f(xi) * (xi - xi_m1)) / (f(xi) - f(xi_m1)))
    xi_m1 = xi_old
    i = 0
    q_tmp_last = sp.linspace(0, 0, nx)
    while i < iterations and abs(f(xi_old)) > epsilon:  # abs(xi_old - xi) / xi > epsilon:

        plt.clf()

        xlimL = max(float(start_x - shift), range_left)
        xlimP = min(float(start_x + shift), range_right)

        xlim = max(abs(start_x - xlimL), abs(start_x - xlimP))
        xlimL = start_x - xlim
        xlimP = start_x + xlim
        plt.xlim(xlimL, xlimP)

        plt.plot(iks, q)
        plt.plot(iks, os_x, color='black')
        plt.title("start x0 " + "= " + str(start_x) + "start x_-1 " + "= " + str(start_x_m1) + " found " + str(xi))

        xi_old = xi
        a = (f(xi) - f(xi_m1)) / (xi - xi_m1)
        b = example_function(xi) - a * xi

        xi = xi - ((f(xi) * (xi - xi_m1)) / (f(xi) - f(xi_m1)))
        xi_m1 = xi_old

        iks_tmp = sp.linspace(int(xi - 2), int(xi + 2), nx)
        q_tmp = sp.linspace(0, 0, nx)

        for j in range(len(iks_tmp)):
            q_tmp[j] = a * iks_tmp[j] + b

        plt.ylim(max(q_tmp), min(q_tmp))
        plt.plot(iks_tmp, q_tmp)
        plt.plot(iks_tmp, q_tmp_last)
        q_tmp_last = q_tmp
        while __next == 0:
            plt.pause(1)
        __next = 0
        i += 1
    print("found " + str(xi) + " f(found)= " + str(f(xi)))
    return xi


print("BISECTION ", bisection(example_function, 5.5, 6.3, 0.001, 50))
print(newton_raphson(example_function, 6.3, 0.001, 50))
print(newton_raphson(example_function, 5.5, 0.001, 50))

print(bisection(example_function, -3.5, -2.3, 0.0001, 50))
print(newton_raphson(example_function, -2.3, 0.0001, 50))
print(newton_raphson(example_function, -3.5, 0.0001, 50))

print(secant(example_function, 7.3, 6.2, 0.001, 50))
