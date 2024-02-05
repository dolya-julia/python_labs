import random
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
str = input()
print(mix_words(str))
print(count_even_words(str))