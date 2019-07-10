'''Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.'''

def sum_of_multiples(num):
    if num < 1:
        return 'Number must be positive'
    elif type(num) != int:
        return 'Input must be Integer'
    num_sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            num_sum += i
    return num_sum


print(sum_of_multiples(1000))