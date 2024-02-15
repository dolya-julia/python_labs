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
    st = s[s_w:s_r] + s[s_b:] + " " + s[s_r:s_b]
    mas = st.split()
    return mas

print("Какую задачу вы хотите решить?")
print("Задача 3(перемешать слова в строке), задача 8(количество слов с четным количеством символов), задача 16(российский флаг)")
n = int(input())
if n == 3:
    print("Введите строку")
    st = input()
    print(mix_words(st))
elif n == 8:
    print("Введите строку")
    st = input()
    print(count_even_words(st))
elif n == 16:
    print('Введите массив, состоящий из элементов "белый", "синий", и "красный"')
    mas = [i for i in input().split()]
    print(russian_flag(mas))
else:
    print("Задача не выбрана")


