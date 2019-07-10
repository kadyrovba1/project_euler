'''
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.

'''
def sum_primes(n):
    if type(n) != int:
        return 'Input must be Integer'
    elif n < 0:
        return 'Number must be positive'
    result, cell = 0, [True] * n
    for p in range(2, n):
        if cell[p]:
            result += p
            for i in range(p*p, n, p):
                cell[i] = False
    return result


print(sum_primes(2000000))
