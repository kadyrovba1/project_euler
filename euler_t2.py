def fib(num):
    if type(num) != int:
        return 'Input must be Integer'
    elif num < 0:
        return 'Number must be positive'
    x = 1
    y = 1
    z = 0
    result = 0
    while z < num:
        z = (x + y)
        if z % 2 == 0:
            result += z
        x, y = y, z
    return result


print(fib(4000000))