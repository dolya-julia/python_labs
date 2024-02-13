def global_max(l, d):
    if l[d] == max(l):
        return "yes"
    else:
        return "no"
n = int(input())
l = [int(input()) for i in range(n)]
d = int(input())
print(global_max(l, d))
