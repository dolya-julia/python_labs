import re
def count_char(s):
    s = s.lower()
    k = 0
    for i in range(len(s)):
        if (s[i] >= 'а' and s[i] <= 'я') or s[i] == 'ё':
            k += 1
    return k
def lower_char(s):
    st = ''
    for i in range(len(s)):
        st += " "
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            st += s[i]
    return st
def min_digit(s):
    l = re.findall(r'\d+', s)
    l = [int(i) for i in l]
    return min(l)
s = input()
print(count_char(s))
print(lower_char(s))
print(min_digit(s))