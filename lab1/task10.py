n = int(input())
l = [ str(input()) for i in range(n) ]
l.sort(key=lambda x: len(x.split()))
print(l)
