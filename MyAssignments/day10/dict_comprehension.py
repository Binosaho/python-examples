# Write an example to demonstrate dictionaly comprehension
list1 = ['a', 'b', 'c', 'd']
dict = {list1.index(i) : i for i in list1}
print(dict)