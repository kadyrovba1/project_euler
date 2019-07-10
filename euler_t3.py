
'''
Задача 3
5, 7, 13, 29 - это простые множители числа 13195.
Найти наибольший простой множитель числа 600851475143.
'''

#n = 13195
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def largest_prime(n):
    if type(n) != int:
        return 'Input must be Integer'
    elif n < 0:
        return 'Number must be positive'
    factors = list()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            if is_prime(i):
                factors.append(i)
    return max(factors)


print(largest_prime(600851475143))