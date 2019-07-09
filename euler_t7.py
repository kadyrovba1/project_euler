'''Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?'''
def issimple(n):
    r=math.ceil(math.sqrt(n))
    for i in range(2,n):
        if n%i==0:
            return False
    return True

import math
def issimple(n):
    r=math.ceil(math.sqrt(n))
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=5
s=[2,3]
while True:
    if issimple(n) is True:
        s.append(n)
    if len(s)==10001:
        break
    n+=2

print(s[-1])
    