
n1 = 1
n2 = 2
s = 0
while n2 <= 4000000:
    if n2 % 2 == 0:
        s += n2
    temp = n1 + n2
    n1 = n2
    n2 = temp
print(s)