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


def nod(a):
    l = list()
    for i in range(3, a + 1):
        if i % 2 != 0 and a % i == 0:
            for j in range(2, i - 1):
                if i % j == 0:
                    l.append(i)
                    break
    d1 = max(l)
    pr = 1
    while a > 0:
        k = a % 10
        a = a // 10
        pr *= k
    d2 = pr
    while d1 != 0 and d2 != 0:
        if d1 > d2:
            d1 %= d2
        else:
            d2 %= d1
    return (d1 + d2)
# Функция 1 Найти максимальный простой делитель числа.
# Функция 2 Найти произведение цифр числа, не делящихся на 5
# Функция 3 Найти НОД максимального нечетного непростого делителя
# числа и произведения цифр данного числа.

num = int(input())
print(simple_del(num))
print(multiply_numbers(num))
print(nod(num))