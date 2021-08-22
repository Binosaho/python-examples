class Fibonacci:

    def __init__(self,num=0):
        self.num = num

    def __iter__(self):
        self.n = 0
        self.sumvalue = 0
        self.firstnum = 0
        self.secondnum = 1
        return self

    def __next__(self):
        if self.n < self.num:
            firstnum = self.firstnum
            self.sumvalue = self.firstnum + self.secondnum
            self.firstnum = self.secondnum
            self.secondnum = self.sumvalue
            self.n += 1
            return firstnum
        else:
            raise StopIteration


fib = Fibonacci(7)
i = iter(fib)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
#print(next(i))


###################################

## Fibonacci for a given num
def fib(num):
    print("Fib series of", num)
    sum = 0
    fnum = 0
    snum = 1
    for i in range(num):
        print(fnum , end=" ")
        sum = fnum + snum
        fnum = snum
        snum = sum


#fib(7)
