def com_symbol(s):
    k = 0
    for c in s:
        if s.count(c) >= k:
            k = s.count(c)
            symb = c
    st = ' '.join(l)
    return k - st.count(symb)
n = int(input())
l = [str(input()) for i in range(n)]
l.sort(key = com_symbol)
print(l)