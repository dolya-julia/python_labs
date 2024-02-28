import random
n = 10
l = [str(random.randint(-10, 10)) for i in range(n)]
f = open("task2.txt", 'w')
f.writelines(f"{item}\n" for item in l)
f.close()
f = open("task2.txt", 'r')
ln = list(map(str.strip, f.readlines()))
counts = 0
for i in range(len(ln)):
    for j in range(i + 1, len(ln)):
        if int(ln[i]) == -1 * int(ln[j]):
            counts += 1
print(counts)
