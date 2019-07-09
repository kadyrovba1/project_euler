''' Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.'''

def is_polindrom(num):
    raw=str(num)
    r_num=int(raw[::-1])
    if num==r_num:
        return True
    else:
        return False

pol=[]
for i in range(100,1000):
    for j in range(100,1000):
        if is_polindrom(i*j)==True:
            pol.append(i*j)
print(max(pol))