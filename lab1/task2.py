import random
import array
def mix_words(s):
    l = s.split()
    random.shuffle(l)
    s = " ".join(l)
    return s
def count_even_words(s):
    k = 0
    lst = s.split()
    for l in lst:
        if len(l) % 2 == 0:
            k += 1
    return k
def russian_flag(mas):
    mas.sort()
    s = " ".join(mas)
    s_w = s.find('белый')
    s_b = s.find('синий')
    s_r = s.find('красный')
    str = s[s_w:s_r] + s[s_b:] + " " + s[s_r:s_b]
    mas = str.split()
    return mas
str = input()
mas = [i for i in input().split()]
print(mix_words(str))
print(count_even_words(str))
print(russian_flag(mas))
