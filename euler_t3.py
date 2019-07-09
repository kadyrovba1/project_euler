
'''
Задача 3
5, 7, 13, 29 - это простые множители числа 13195.
Найти наибольший простой множитель числа 600851475143.
'''

#n = 13195
import math
def issimple(a):
    r=math.ceil(math.sqrt(a))
    lst=[]
    for i in range(3,r):
        if a%i==0:
            if issimple(i)==[]:
                lst.append(i)
    return lst
r=issimple(600851475143)
print(max(r))