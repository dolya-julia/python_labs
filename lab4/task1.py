file1 = open('27-168b.txt')
st = file1.readline()
st.rstrip()
n, k = map(int, st.split())
l = []
for i in range(n):
    temp = int(file1.readline())
    l.append(temp)
mx1 = 0
mx2 = 0
mx = 0
for i in range(2*k, n):
    mx1 = max(mx1, l[i - 2*k])
    mx2 = max(mx2, mx1 * l[i - k])
    mx = max(mx, mx2 * l[i])
print(mx % (10 ** 6 + 1))