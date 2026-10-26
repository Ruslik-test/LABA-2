from math import *

x = float(input('Введите значение аргумента x = '))

if x < 0:
    y = x + 2
elif x < 2:
    y = -sqrt(4 - x**2) # Нижняя полуокружность с центром (0,0)
elif x < 4:
    y = 2 + sqrt(4 - (x - 2)**2) # Верхняя полуокружность с центром (2,2)
else:
    y = 6 - x

print("X={0:.2f}  Y={1:.2f}".format(x, y))
