import math
def simple_del(a):
    i = 2
    l = list()
    while i < math.ceil(math.sqrt(a)):
        if a % i == 0:
            l.append(i)
            while a % i == 0:
                a = a // i
        i = i + 1
    if a != 1:
        l.append(a)
    return max(l)
def multiply_numbers(a):
    pr = 1
    while a > 0:
        k = a % 10
        a = a // 10
        if (k % 5 != 0):
            pr *= k
    return pr
num = int(input())
print(simple_del(num))
print(multiply_numbers(num))
