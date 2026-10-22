from math import *

def f(x):
    if x < -9 or x > 9:
        return None
    elif x < -6:
        return -sqrt(9 - (x + 6)**2)
    elif x < 0:
        return 0.5*x + 3
    elif x < 3:
        return sqrt(9 - x**2)
    else:
        return 0.5*(x - 3)

x = float(input('Введите значение x='))
y = f(x)
if y is None:
    print("x вне области определения")
else:
    print("X={0:.2f} Y={1:.2f}".format(x, y))
