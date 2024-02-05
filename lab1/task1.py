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

num = int(input())
print(simple_del(num))
