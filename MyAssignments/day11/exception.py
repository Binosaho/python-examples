# write a function to check division by zero exception

def devzero_func(n1,n2):
    try:
       print(n1 / n2)
    except:
        print(ZeroDivisionError, "can not devide by zero")
    else:
        print("thats fine")

devzero_func(10,4)
