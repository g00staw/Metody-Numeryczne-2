import math
import sys

from sympy import Symbol, S, limit, diff, Interval
import numpy as np
from sympy.printing.numpy import func
from sympy.calculus.util import continuous_domain


# zadanie 4

def newton_method():
    x = Symbol('x')
    f = S('sin(x)-(x/2)')

    start = math.pi / 2
    end = math.pi

    f_prime = calculate_derivative(f, x)
    f_prime_prime = calculate_derivative(f_prime, x)

    f_interval = Interval(start, end)
    is_continous = None;

    if(check_continous(f, x, f_interval) and check_continous(f_prime, x, f_interval) and check_continous(f_prime_prime, x, f_interval)):
        print("f(x), f'(x) oraz f''(x) są ciągłe w zadanym przedziale.")
        is_continous = True

    diffrent_signs = check_signs(f, x, start, end)

    if(is_continous and diffrent_signs == True):
        print("Funkcja spełnia założenia Bolzano-Cauchy’ego. Oto rozwiązanie zadania: ")

        if(f.subs(x, start) * f_prime_prime.subs(x, start) > 0):
            x0 = start

        elif(f.subs(x, end) * f_prime_prime.subs(x, end) > 0):
            x0 = end

        newton_method_algorithm(f, x, 0.01, start, end, x0, 0)

    else:
        print("Czy ciagla?: ",is_continous)
        print("Czy rozne znaki?: ", diffrent_signs)

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

def check_signs(f, x, a, b):                                    # Sprawdzenie znaków na końcach przedziału
    value_at_a = f.subs(x, a)
    value_at_b = f.subs(x, b)

    print(value_at_a)
    print(value_at_b)

    a_multiply_b = value_at_a*value_at_b

    if a_multiply_b < 0:
        return True
    else:
        return False

def newton_method_algorithm(f, x, E, a, b, x0, i):

    f_prime = calculate_derivative(f, x)
    xn = x0 - (f.subs(x, x0)/f_prime.subs(x, x0))

    if(abs(f_prime.subs(x, a)) < abs(f_prime.subs(x, b))):
        m = abs(f_prime.subs(x, a))
    else:
        m = abs(f_prime.subs(x, b))

    if(abs(f.subs(x, xn)) / m < E):
        print("Iteracje: ", i)
        print("Szukane miejsce zerowe to: ", xn)
    else:
        i = i + 1
        newton_method_algorithm(f, x, E, a, b, xn, i)

# wywolanie
newton_method()