from math import pi

"""
Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""

try:
    d = int(input("Число:  "))
except ValueError:
    print('Ошибка. Введите число')
else:
    s = pi * (d / 2) ** 2
    c = pi * d
    print(f'{s:.2f} Длина окружности: {c: .42f} ')
finally:
    print('')


