'''
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.

'''

def simple_sum(n):
    num_list = list(range(n))
    num_list[1] = 0 
    for i in num_list[2:]:
            for j in range(i + i, len(num_list), i):
                num_list[j] = 0
    return num_list

print(sum(simple_sum(2000000)))
