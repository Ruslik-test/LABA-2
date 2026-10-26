# -*- coding: cp1251 -*-
from math import *

# 1. Ввод данных
x = float(input('Введите значение x = '))

# 2. Ветвление по интервалам
if x <= 0:
    y = -x / 2
elif x > 0 and x <= 2:
    y = 2 - sqrt(4 - x**2)
elif x > 2 and x <= 4:
    y = sqrt(4 - (x - 2)**2)
else:
    y = -x / 2 + 2

# 3. Вывод результата
print("X = {0:.2f}  Y = {1:.2f}".format(x, y))