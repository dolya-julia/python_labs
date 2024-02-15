import math
n = int(input())
l = [str(input()) for i in range(n)]
st = ' '.join(l)
def com_symbol(s):
    k = 0
    for c in s:
        if s.count(c) >= k:
            k = s.count(c)
            symb = c
    global st
    k_t = st.count(symb)
    return k - k_t
def sq_deviation(s):
    k = 0
    for c in s:
        if s.count(c) >= k:
            k = s.count(c)
            symb = c
    global st
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
def com_symbol_st(s):
    global st
    k = 0
    symb = ''
    for c in st:
        if st.count(c) >= k and c != ' ':
            k = st.count(c)
            symb = c
    k_t = s.count(symb)
    sr = (k + k_t) / 2
    return math.sqrt(((k - sr) ** 2 + (k_t - sr) ** 2) / 2)



print("Какую задачу вы хотите решить?")
print("Задача 3(В порядке увеличения разницы наиболее часто"
      "встречаемого символа в строке и частотой его появления в алфавите.), "
      "задача 5(увеличения квадратичного отклонения самого встречаемого в строке символа от его стречаемости в текстах),"
      " задача 7(увеличения разницы между количеством сочетаний гласная-согласная и согласная-гласная в строке.),"
      " задача 12(самого распространенного символа в наборе строк от частоты его встречаемости в данной строке.)")
nm = int(input())
if nm == 3:
    l.sort(key=com_symbol)
    print(l)
elif nm == 5:
    l.sort(key=sq_deviation)
    print(l)
elif nm == 7:
    l.sort(key=vow_cons)
    print(l)
elif nm == 12:
    l.sort(key=com_symbol_st)
    print(l)
else:
    print("Задача не выбрана")