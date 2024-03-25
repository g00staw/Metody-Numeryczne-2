import math
import sys
from sympy import Symbol, S, limit, diff, Interval, lambdify
import numpy as np
from sympy.printing.numpy import func
from sympy.calculus.util import continuous_domain


def secant_method():
    x = Symbol('x')
    f = S('x**3+x**2-3*x-3')

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



    else:
        print("Czy ciagla?: ",is_continous)
        print("Czy rozne znaki?: ", diffrent_signs)

def check_continous(f, x, interval):
    is_contionus = continuous_domain(f, x, interval)
    if(is_contionus == interval):
        return True
    else:
        return False


#def find_roots(f,x):
#    x_initial_guesses = np.linspace(-10, 10, 1000)  # początkowe zgadnięcia
#    roots = []
#
#    # Przekształć 'f' w funkcję, którą można wywołać
#    f_callable = lambdify(x, f)
#
#    x_initial_guesses = np.linspace(-10, 10, 1000)  # początkowe zgadnięcia
#    roots = []
#
#    for x_guess in x_initial_guesses:
#        root = fsolve(f_callable, x_guess)
#        if len(roots) == 0 or np.min(np.abs(roots - root)) > 1e-5:  # jeżeli znaleziony pierwiastek jest nowy
#            roots.append(root)
#
#    if len(roots) == 1:
#        print("Funkcja ma dokładnie jeden pierwiastek pojedynczy.")
#    else:
#        print("Funkcja nie ma dokładnie jednego pierwiastka pojedynczego.")

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

secant_method()