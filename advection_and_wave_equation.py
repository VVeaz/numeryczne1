import scipy as sp
import matplotlib.pyplot as plt
from math import exp

from tkinter import *

# wybory schematu, kształtu i warunków granicznych
scheme_choose = -1
shape_choose = -1
boundary_choose = -1


# aplikacja okienkowa
def rysuj_on_click(event):
    window.quit()
    window.destroy()


def ftcs_on_click(event):
    global scheme_choose
    scheme_choose = 0


def godunov_on_click(event):
    global scheme_choose
    scheme_choose = 1


def lf_on_click(event):
    global scheme_choose
    scheme_choose = 2


def lw_on_click(event):
    global scheme_choose
    scheme_choose = 3


def rownanie_falowe_on_click(event):
    global scheme_choose
    scheme_choose = 4


def square_on_click(event):
    global shape_choose
    shape_choose = 0


def e_do_minus_x_kwadrat_on_click(event):
    global shape_choose
    shape_choose = 1


def chudy_on_click(event):
    global shape_choose
    shape_choose = 2


def periodic_on_click(event):
    global boundary_choose
    boundary_choose = 0


def open_on_click(event):
    global boundary_choose
    boundary_choose = 1


window = Tk()

label = Label(window, text="Co narysować?", font=("Arial Black", 24, "bold"), foreground="yellow", background="blue")
label.pack(expand=YES, fill=BOTH)

button_ftcs = Button(window, text="FTCS", font=("Comic Sans MS", 16, "bold"), background="red")
button_ftcs.bind("<Button-1>", ftcs_on_click)
button_ftcs.pack(fill=X)

button_godunov = Button(window, text="Godunov", font=("Comic Sans MS", 16, "bold"), background="red")
button_godunov.bind("<Button-1>", godunov_on_click)
button_godunov.pack(fill=X)

button_lf = Button(window, text="Lax–Friedrichs", font=("Comic Sans MS", 16, "bold"), background="red")
button_lf.bind("<Button-1>", lf_on_click)
button_lf.pack(fill=X)

button_lw = Button(window, text="Lax–Wendroff", font=("Comic Sans MS", 16, "bold"), background="red")
button_lw.bind("<Button-1>", lw_on_click)
button_lw.pack(fill=X)

button_rownanie_falowe = Button(window, text="Równanie falowe", font=("Comic Sans MS", 16, "bold"), background="red")
button_rownanie_falowe.bind("<Button-1>", rownanie_falowe_on_click)
button_rownanie_falowe.pack(fill=X)

button_kwadrat = Button(window, text="Kształt prostokąta", font=("Comic Sans MS", 16, "bold"), background="cyan")
button_kwadrat.bind("<Button-1>", square_on_click)
button_kwadrat.pack(fill=X)

button_gauss = Button(window, text="Zbliżony do rozkładu normalnego", font=("Comic Sans MS", 16, "bold"),
                      background="cyan")
button_gauss.bind("<Button-1>", e_do_minus_x_kwadrat_on_click)
button_gauss.pack(fill=X)

button_slim = Button(window, text="Szczupły", font=("Comic Sans MS", 16, "bold"), background="cyan")
button_slim.bind("<Button-1>", chudy_on_click)
button_slim.pack(fill=X)

button_periodic = Button(window, text="Warunki periodyczne", font=("Comic Sans MS", 16, "bold"), background="yellow")
button_periodic.bind("<Button-1>", periodic_on_click)
button_periodic.pack(fill=X)

button_open = Button(window, text="Warunki otwarte", font=("Comic Sans MS", 16, "bold"), background="yellow")
button_open.bind("<Button-1>", open_on_click)
button_open.pack(fill=X)

button_rysuj = Button(window, text="RYSUJ", font=("Comic Sans MS", 16, "bold"), background="#2aff1f")
button_rysuj.bind("<Button-1>", rysuj_on_click)
button_rysuj.pack(fill=X)

window.mainloop()

# warunki początkowe
nx = 5000  # number of points
nx_ghost = 2  # ghost cells

v = 1  # velocity
CFL = 0.95  # CFL number
CFL2 = CFL * CFL
nx = nx + nx_ghost

# generate space
x = sp.linspace(-2., 2., nx)
q = sp.linspace(0, 0, nx)

qnm1 = sp.linspace(0, 0, nx)
qn = sp.linspace(0, 0, nx)

dx = (max(x) - min(x)) / nx
dt = CFL * dx.min() / abs(v)


# schematy numeryczne
def ftcs():
    for i in range(nx_ghost, len(x) - nx_ghost):
        q[i] = q[i] + CFL * (q[i - 1] - q[i + 1]) / 2


def godunov():
    for i in range(nx_ghost, len(x) - nx_ghost):
        q[i] = q[i] + CFL * (q[i - 1] - q[i])


def godunov():
    for i in range(nx_ghost, len(x) - nx_ghost):
        q[i] = q[i] + CFL * (q[i - 1] - q[i])


def lax_friedrichs():
    q[1:-1] = ((q[2:] + q[:-2]) + CFL * (q[:-2] - q[2:])) * 0.5


def lax_wendroff():
    q[1:-1] = ((CFL2 + CFL) * q[:-2] - 2 * q[1:-1] * (CFL2 - 1) + (CFL2 - CFL) * q[2:]) * 0.5


def wave_equation():
    global qn, qnm1
    q[0] = qn[1]
    q[nx - 1] = qn[nx - 2]
    for i in range(0, len(qn)):
        qnm1[i] = qn[i]
        qn[i] = q[i]
    for i in range(nx_ghost, len(x) - nx_ghost):
        q[i] = (2 - 2 * CFL2) * qn[i] + CFL2 * (qn[i - 1] + qn[i + 1]) - qnm1[i]


# kształty
def square():
    for i in range(0, len(x)):
        q[i] = 1
        qn[i] = 1
        if abs(x[i]) <= 0.5:
            q[i] = 2
            qn[i] = 2


def almost_gauss():
    for i in range(0, len(x)):
        q[i] = exp(-(x[i] * x[i]))
        qn[i] = exp(-(x[i] * x[i]))


def slim():
    for i in range(0, len(x)):
        q[i] = (exp(-(x[i] * x[i]))) ** 4
        qn[i] = q[i]


# warunki brzegowe
def boundary_conditions_periodic():
    q[0] = q[-4]
    q[1] = q[-3]
    q[-2] = q[2]
    q[-1] = q[3]


def boundary_conditions_open():
    q[1] = q[0]
    q[0] = q[-1]
    q[-2] = q[-1]
    q[-1] = q[0]


# ustalenie wyborów schematu, kształtu i granic
schemes = [ftcs, godunov, lax_friedrichs, lax_wendroff, wave_equation]
scheme = schemes[scheme_choose]

shapes = [square, almost_gauss, slim]
shapes[shape_choose]()

boundaries = [boundary_conditions_periodic, boundary_conditions_open]
boundary = boundaries[boundary_choose]

# symulacja
t = 0.0
plt.ion()
for k in range(0, 10000):
    plt.clf()
    plt.subplot(1, 1, 1)
    plt.plot(x, q, '-k')
    plt.plot(x * 0 + x[0], sp.linspace(-3, 3, len(x)), '-')
    #plt.plot(x * 0 + x[-1], sp.linspace(-3, 3, len(x)), '-')
    plt.title('time = ' + str(t) + " " + scheme.__name__)
    plt.ylabel('q(x)')
    plt.ylabel('x')
    plt.ylim(0, 3)
    plt.pause(0.001)
    scheme()  # wybrany schemat
    boundary()
    t = t + dt
