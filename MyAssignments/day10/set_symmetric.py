# [1, 2, 3] [3, 4, 5] -> [1, 2, 4, 5]  using set symmetric function
## for set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 ^ set2)

## for list
list1 = [1, 2, 3]
list2 = [3, 4, 5]
print(set(list1) ^ set(list2))
