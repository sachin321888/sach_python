
def logging(func):
    def wrap(*args):
        print("logging", args)
        result=func(*args)
        print("result is ",result)
        return result
    return wrap


def gtreater_first(func):
    def wrap(a,b):
        if a<b:
            a,b=b,a
        func(a,b)
    return wrap


@logging
@gtreater_first
def divide(a,b):
    return a/b




@gtreater_first
def sub(a,b):
    return a-b

#so what if there is variable number of arguments in addition or sub or div like def add(3,4,5,6 etc...)
@logging
def add(a,b,c,d):
    return a+b+c+d

print(divide(10,5))
print(sub(5,10))
print(add(1,3,4,5))


