import sys
import sympy
from sympy import *
from sympy.calculus.util import continuous_domain


def trapezoidal_method():
    x = Symbol('x')
    f = sqrt(1+x)

    a = 0
    b = 1

    f_interval = Interval(0, 1)
    if(check_continous(f, x, f_interval) == True):
        print("Funkcja jest ciągła.")
        trapezoidal_method_algorithm(f, x, 3, 1/3, a, b)


def check_continous(f, x, interval):
    is_contionus = continuous_domain(f, x, interval)
    if(is_contionus == interval):
        return True
    else:
        return False
def calculate_derivative(f, x):
    try:
        f_prime = diff(f, x)
        return f_prime

    except:
        print("Nie można obliczyć pochodnej tej funkcji.")
        sys.exit()

def trapezoidal_method_algorithm(f, x, n, h, a, b):
    f_prime = calculate_derivative(f, x)
    f_prime_prime = calculate_derivative(f_prime, x)

    f_interval = Interval(0, 1)

    sumE = 0

    i = 1
    for i in range(n - 1):
        xi = a + i * h
        sumE = sumE + f.subs(x, xi)

    if(check_continous(f_prime, x, f_interval) and check_continous(f_prime_prime, x, f_interval)):
        print("f'(x) oraz f''(x) są ciągłe w zadanym przedziale.")

        if(a > b):
            E = a
        else:
            E = b

        Rf = (-1/12) * (b-a) * h * h * f_prime_prime.subs(x, E)
        score = (1/2) * h * (f.subs(x, a) + f.subs(x, b) + 2 * sumE) + Rf

    else:
        score = (1/2) * h *(f.subs(x, a) + f.subs(x, b) + 2 * sumE)
    print("Wynik: ")
    print(score)

trapezoidal_method()