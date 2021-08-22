## [1, 2, 3, 3, 4, 4, 4] -> [(1, 1), (2, 1), (3, 2), (4, 3)]

list1 = [1, 2, 3, 3, 4, 4, 4]
list2 = list(set([(i, list1.count(i)) for i in list1]))
list2.sort()
print(list2)


