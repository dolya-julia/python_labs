import math
def com_symbol(s):
    k = 0
    for c in s:
        if s.count(c) >= k:
            k = s.count(c)
            symb = c
    st = ' '.join(l)
    return k - st.count(symb)
def sq_deviation(s):
    k = 0
    for c in s:
        if s.count(c) >= k:
            k = s.count(c)
            symb = c
    st = ' '.join(l)
    k_t = st.count(symb)
    sr = (k + k_t) / 2
    return math.sqrt(((k - sr) ** 2 + (k_t - sr) ** 2) / 2)
def vow_cons(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    k_vc = 0
    k_cv = 0
    for i in range(0, len(s) - 1):
        if s[i] in vowels and s[i+1] in consonants:
            k_vc += 1
        if s[i] in consonants and s[i+1] in vowels:
            k_cv += 1
    return k_vc - k_cv
n = int(input())
l = [str(input()) for i in range(n)]
l.sort(key = vow_cons)
print(l)