def easy_function(xi):
    return -xi ** 3 + 3 * xi ** 2 + 17 * xi - 0.25


def hard_function(xi):
    return 1 / (xi * xi - 1)


def simpson1_3_h(a, b, f):
    h = (b - a) / 2
    return (h / 3) * (f(a) + 4 * f((a + b) / 2) + f(b))


def simpson1_3_h_drugi_wzor(a, b, f):
    return ((b - a) / 6) * f(a) + (2 * (b - a)) / 3 * f((a + b) / 2) + ((b - a) / 6) * f(b)


the_simpsons = [simpson1_3_h, simpson1_3_h_drugi_wzor]


def simpson1_3(n, a, b, f, choose):
    h = (b - a) / n
    sim = the_simpsons[choose]
    res = 0
    a_s = a
    while a_s < b:
        res += sim(a_s, a_s + h, f)
        a_s += h
    return res


def simpson1_3_maby_fast(n, a, b, f):
    h = (b - a) / n
    sum_odd = 0
    a_start = a + h
    while a_start < b:
        sum_odd += f(a_start)
        a_start += 2 * h

    sum_eve = 0
    a_start = a + 2 * h
    while a_start < b:
        sum_eve += f(a_start)
        a_start += 2 * h
    return (b - a) / (3 * n) * (f(a) + 4 * sum_odd + 2 * sum_eve + f(b))


def trapezoidal_h(a, b, f):
    return (f(a) + f(b)) * (b - a) * 0.5


def trapezoidal(n, a, b, f):
    h = (b - a) / n
    a_s = a
    res = 0
    while a_s < b:
        res += trapezoidal_h(a_s, a_s + h, f)
        a_s += h
    return res


_1_div_sqrt_3 = 1 / 3 ** 0.5


def gauss_quadrature_h(a, b, f):
    b_minus_a_div_2 = 0.5 * (b - a)

    return b_minus_a_div_2 * f(b_minus_a_div_2 * (-_1_div_sqrt_3) + 0.5 * (b + a)) + b_minus_a_div_2 * \
           f(b_minus_a_div_2 * _1_div_sqrt_3 + (b + a) * 0.5)


def gauss_quadrature(n, a, b, f):
    h = (b - a) / n
    a_s = a
    res = 0
    while a_s < b:
        res += gauss_quadrature_h(a_s, a_s + h, f)
        a_s += h
    return res


_n = 20
_a = 3
_b = 20
print(simpson1_3(_n, _a, _b, easy_function, 0))
print(simpson1_3(_n, _a, _b, easy_function, 1))

print(simpson1_3_maby_fast(_n, _a, _b, easy_function))

print(trapezoidal(_n, _a, _b, easy_function))
print(gauss_quadrature(_n, _a, _b, easy_function))

print(gauss_quadrature(_n, 0, 1, hard_function))
