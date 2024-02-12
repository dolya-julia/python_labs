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
n = int(input())
l = [str(input()) for i in range(n)]
l.sort(key = com_symbol)
print(l)