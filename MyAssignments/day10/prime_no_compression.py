# Find out the list of prime number between 1 to 100 using list comprehension

def isPrimeno(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count == 2

p = [i for i in range(1,101) if(isPrimeno(i))]
print(p)


## OR
"""
The all() function is an inbuilt function in Python which returns true if all the elements of a given iterable( List, Dictionary, Tuple, set, etc) are True else it returns False. It also returns False if the iterable object is empty
"""
l = [x for x in range(1, 101) if all(x % y != 0 for y in range(2, x))]
print(l)





