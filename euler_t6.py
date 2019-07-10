'''
Задача 6
Сумма квадратов первых десяти натуральных чисел равна
    1^2 + 2^2 + ... + 10^2 = 385
Квадрат суммы ервых десяти натуральных чисел равен
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
Разница между этими числами равна
    3025 - 385 = 2640
Найти разницу между квадратом суммы и суммой квадратов для первой
тысячи натуральных чисел.
'''

'''
Квадрат суммы можно разложить:
(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2ac + 2cb
следовательно:
(a + b + c)^2 - (a^2 + b^2 + c^2) = 2ab + 2ac + 2cb = 2 * (ab + ac + cb)
'''

def sum_diff(n):
    if n < 0:
        return 'Number must be positive'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        sum1 = 0
        sum2 = 0
        for i in range(1, n+1):
            sum1 += i*i
            sum2 += i
        return sum2*sum2-sum1