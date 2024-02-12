n = int(input())
l = [ str(input()) for i in range(n) ]
l.sort(key=len)
print(l)