'''
Задача 9
Пифагорова тройка - это набор и тех натуральных чисел, a < b < c, для которых:
    a ^ 2 + b ^ 2 = c ^ 2
Существует одна пифагорова тройка для которой a + b + c = 1000.
Найти произведение abc.
'''

import math

def triplet():
    for i in range(4, 1000):
        for j in range(5, 1000):
            c = pow(i,2) + pow(j,2)
            if math.sqrt(c) - int(math.sqrt(c)) == 0:
                return str(i) + ' ' + str(j) + ' ' + str(int(math.sqrt(c)))