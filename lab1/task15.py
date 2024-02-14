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
n = int(input())
l = [int(input()) for i in range(n)]
# ind = int(input())
print(even_odd_index(l))

