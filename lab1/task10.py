my_list = list(map(str, input().split(".")))
my_list.sort(key=lambda x: len(x.split()))
print(my_list)
