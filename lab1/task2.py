import random
def mix_words(s):
    l = s.split()
    random.shuffle(l)
    s = " ".join(l)
    return s
str = input()
print(mix_words(str))