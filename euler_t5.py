'''2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?

'''
def divisible(n):
    for i in range(1, 20):
        if n % i != 0:
            return False
    return True


def smallest():
    n = 2520
    while True:
        if divisible(n):
            return n
        n += 20


print(smallest())