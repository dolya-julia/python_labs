my_set1 = {}
my_set2 = {}
my_set1 = set(input().split())
my_set2 = set(input().split())
my_set3 = my_set1.intersection(my_set2)
print(sorted(my_set3))
