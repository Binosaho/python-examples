"""
read file - > test.txt
hello world
this is my first python program
python is fun
hello world
hello world

[(hello, 3), (python, 2), ...]
"""
import re

words = []
with open("test.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        l2 = l.strip("\n")
        l3 = l2.split(" ")
        words.extend(l3)
#print(words)
count_list = [(i, words.count(i)) for i in words]
#print(list(set(count_list)))

###############################################

print(set(map(lambda w: (w, words.count(w)), words)))

###############################################
from collections import Counter
print(Counter(words))
