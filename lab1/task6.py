def count_char(s):
    s = s.lower()
    k = 0
    for i in range(len(s)):
        if (s[i] >= 'а' and s[i] <= 'я') or s[i] == 'ё':
            k += 1
    return k

s = input()
print(count_char(s))