from sympy import Symbol, S, limit
import numpy as np
from sympy.printing.numpy import func


# zadanie 3

def bisection_method():
    x = Symbol('x')
    f = S('x**3+x-1')

    start = 0
    end = 1

    is_f_continuous = check_continuous(f, x, start, end)
    print(is_f_continuous)

    has_diffrent_signs = check_signs(f, x, start, end)
    print(has_diffrent_signs)

    if is_f_continuous and has_diffrent_signs == True:
        print("Funkcja spełnia założenia Bolzano-Cauchy’ego. Oto rozwiązanie zadania: ")
        bisection_method_algorithm(f, x, 0.01, start, end, 0)
    else:
        print("Funkcja nie spełnia założeń Bolzano-Cauchy’ego. Nie można rozwiązać zadania.")

def check_continuous(f, x, start, end):                          # Sprawdzenie ciągłości funkcji na przedziale [0,1]

    points = np.linspace(start, end, 100)

    is_continuous = True

    for c in points:                                            # Pętla po wszystkich punktach

        limit_left = limit(func, x, c, dir='-')                 # Obliczanie granic z obu stron
        limit_right = limit(func, x, c, dir='+')


        if limit_left != limit_right:                           # Sprawdzanie, czy granice są równe
            is_continuous = False
            break                                               # Jeśli funkcja nie jest ciągła w punkcie c, przerywamy pętlę

    return is_continuous


def check_signs(f, x, a, b):                                    # Sprawdzenie znaków na końcach przedziału
    value_at_a = f.subs(x, a)
    value_at_b = f.subs(x, b)

    a_multiply_b = value_at_a*value_at_b

    if a_multiply_b < 0:
        return True
    else:
        return False

def bisection_method_algorithm(f, x, E, a, b, iteration):

    z = (a+b)/2

    if abs(f.subs(x, z)) < E:
        print("Iteracje: ", iteration)
        print("Szukane miejsce zerowe to: ", z)
    else:
        if f.subs(x, z)*f.subs(x, a) < 0:
            b = z
        else:
            a = z

        if b-a < E:
            searched_x = (b+a)/2
            print("Iteracje: ", iteration)
            print("Szukany pierwiastek to: ", searched_x)
        else:
            iteration = iteration + 1
            bisection_method_algorithm(f, x, E, a, b, iteration)


bisection_method()
