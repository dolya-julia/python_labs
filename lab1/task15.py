def global_max(l, ind):
    if l[ind] == max(l):
        return "yes"
    else:
        return "no"
def local_min(l, ind):
    if ind == 0 or ind == len(l) - 1:
        return "no"
    else:
        if l[ind] < l[ind-1] and l[ind] < l[ind+1]:
            return "yes"
        else:
            return "no"
def move_array(l):
    return l[1:]+l[:1]
def even_odd_index(l):
    return l[::2] + l[1::2]
def create_list(l):
    unique_list = []
    n_repeat_list = []
    for elem in l:
        if elem not in unique_list:
            unique_list.append(elem)
            n_repeat_list.append(l.count(elem))
    return [unique_list, n_repeat_list]
n = int(input())
l = [int(input()) for i in range(n)]
print("Какую задачу вы хотите решить?")
print("Задача 3, задача 15, задача 27, задача 39, задача 51")
nm = int(input())
if nm == 3:
    print("Введите индекс")
    ind = int(input())
    print(global_max(l, ind))
elif nm == 15:
    print("Введите индекс")
    ind = int(input())
    print(local_min(l, ind))
elif nm == 27:
    print(move_array(l))
elif nm == 39:
    print(even_odd_index(l))
elif nm == 51:
    print(create_list(l))
else:
    print("Задача не выбрана")
