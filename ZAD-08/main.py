from sympy import symbols, lambdify

x = symbols('x')
f = 6*x**2 + 1

f_lambdified = lambdify(x, f)               # Przekształcam wyrażenie sympy na funkcję, którą można wywołać

a = 0                                       # Definiuję granice całkowania
b = 1

n = 1000                                    # Definiuję liczbę prostokątów
dx = (b - a) / n                            # Obliczam szerokość każdego prostokąta

x_values = [a + i*dx for i in range(n)]                             # Obliczam wartości x, w których zostanie oceniona funkcja
area = sum(f_lambdified(x_value) * dx for x_value in x_values)      # Obliczam powierzchnię każdego prostokąta i sumuję je

print(f"Wynik numerycznego całkowania funkcji od {a} do {b} wynosi {area}.")