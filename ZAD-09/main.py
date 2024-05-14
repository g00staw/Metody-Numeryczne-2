from sympy import symbols, limit, diff, sympify, sin, cos, exp, E
import sys
from sympy import Symbol, S, diff, Interval
from sympy.calculus.util import continuous_domain


def simpson_method():
    x = Symbol('x')
    f = S('sin(x)*e**(-3*x)+x**3')

    a = -3
    b = 1

    n = 4     # ilosc przedzialow

    h = (b - a) / n

    xi_values = []
    for i in range(0, int(n + 1)):
        xi = a + i * h
        xi_values.append(xi)

    f_interval = Interval(a, b)

    f_p = diff(f, x)
    f_pp = diff(f_p, x)
    f_ppp = diff(f_pp, x)
    f_pppp = diff(f_ppp, x)

    if(check_continous(f, x, f_interval)):
        defect = deffect_func(a, b, h, f_pppp)
        print('Błąd wzoru wynosi', defect)

        score = simpson_algorythm(f, x, h, n, xi_values)
        score2 = score + defect

        print('Wynik: ', score2, '+ (', defect, ') =', score)

    else:
        score = simpson_algorythm(f, x, h, n, xi_values)
        print('Wynik: ', score)

def check_continous(f, x, interval):
    is_contionus = continuous_domain(f, x, interval)
    if(is_contionus == interval):
        return True
    else:
        return False

def deffect_func(a, b, h, f_pppp):
    return (((h**4) * (b - a))/180) * f_pppp.subs('x', b)

def calculate_derivative(f, x):
    try:
        f_prime = diff(f, x)
        return f_prime

    except:
        print("Nie można obliczyć pochodnej tej funkcji.")
        sys.exit()

def simpson_algorythm(f, x, h, n, xi_values):
        total = 0
        k = 0
        n = n / 2
        for i in range(0, int(n)):
            total = total + (
                        f.subs(x, xi_values[k]) + 4 * f.subs(x, xi_values[k + 1]) + f.subs(x, xi_values[k + 2]))
            k = k + 2
        return (h / 3) * total

simpson_method()