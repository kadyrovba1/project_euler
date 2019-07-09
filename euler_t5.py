'''2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?

'''
limit = 20

# Получить список уникальных делителей
divisors = [d for d in range(1 + limit // 2, limit)]
print(divisors)

n = limit * 2
while True:
    ok = True
    for d in divisors:
        if n % d != 0:
            ok = False
            break
    if ok:
        break
    else:
        n += limit
print(n)