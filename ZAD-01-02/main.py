def menu():
    print("---- Menu -----\n-- Opcje:\n -- 1. wyznaczenie wartości wielomianu w punkcie\n "
          "-- 2. dzielenie wielomianu przez dwumian"
          "\n-- Wybór:")
    choice = input()

    if choice == "1":
        polynomial = create_polynomial()
        polynomial_size = len(polynomial)
        polynomial_value(polynomial_size, polynomial)

    if choice == "2":
        dividing_polynomail()


def dividing_polynomail():
    polynomial = create_polynomial()
    polynomial_size = int(len(polynomial))
    new_polynomial = [None] * polynomial_size

    b_variable = float(input("Podaj zmienna b dla dwumianu (x-b)"))
    while not is_float(b_variable):
        print("Podaj poprawną wartość liczbową")
        b_variable = input()

    for i in reversed(range(polynomial_size)):
        print(polynomial[i])
        if i == (polynomial_size - 1):
            new_polynomial[i] = polynomial[i]
        else:
            new_polynomial[i] = (b_variable * new_polynomial[i+1])+polynomial[i]

    print("Wielomian W(x): ")
    for i in reversed(range(polynomial_size)):
        print(" " + str(polynomial[i]) + "*x^" + str(i))

    print("Po podzieleniu przez dwumian (x - " + str(b_variable) + ") równa się:")

    for i in reversed(range(polynomial_size)):
        if i > 0:
            print("" + str(new_polynomial[i]) + " * x^" + str(i-1))
        else:
            print("Reszta: "+str(new_polynomial[i]))


def create_polynomial():
    polynomial_size = input("Podaj stopień wielomianu (1-5)")
    while not polynomial_size.isdigit() or not (1 <= int(polynomial_size) <= 5):
        polynomial_size = input("Podaj poprawny stopień wielomianu (1-5)")

    polynomial_size = int(polynomial_size) + 1
    polynomial = [None] * polynomial_size
    for i in reversed(range(polynomial_size)):
        print("Podaj x^", i)
        polynomial[i] = input()
        while not is_float(polynomial[i]):
            print("Podaj poprawną wartość liczbową")
            polynomial[i] = input()

        polynomial[i] = float(polynomial[i])

    return polynomial


def polynomial_value(size, polynomial):
    if polynomial == None:
        polynomial = create_polynomial()

    point = input("Podaj punkt")
    while not is_float(point):
        point = input("Podaj poprawną wartość liczbową")
    point = float(point)

    value_in_point = 0
    score = 0

    for i in range(len(polynomial)):
        print("wartosc dla", i, polynomial[i])

    size = int(len(polynomial) - 1)
    for i in range(len(polynomial)):
        value_in_point = polynomial[size - i] * (point ** (size - i))
        score += value_in_point
        print(value_in_point)

    print("Wartość wielomianu W(x) w zdanym punkcie jest równa: ", score)


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


menu()
