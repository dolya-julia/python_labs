def global_max(l, d):
    if l[d] == max(l):
        return "yes"
    else:
        return "no"
def local_min(l, d):
    if d == 0 or d == len(l) - 1:
        return "no"
    else:
        if l[d] < l[d-1] and l[d] < l[d+1]:
            return "yes"
        else:
            return "no"
def move_array(l):
    return l[1:]+l[:1]

n = int(input())
l = [int(input()) for i in range(n)]
# d = int(input())
print(move_array(l))

