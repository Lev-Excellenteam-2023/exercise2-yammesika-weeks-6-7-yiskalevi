#Yiska Levi

def type_check(correnct_type):
    def decorating(fn):
        def inner(num):
            if not isinstance(num, correnct_type):
                raise TypeError("the parameter the function receives is of the not correct type")
            return fn(num)
        return inner
    return decorating



@type_check(int)
def times2(num):
    return num*2
try:
    print(times2(2))
except TypeError:
    print("the parameter the function receives is of the not correct type")
