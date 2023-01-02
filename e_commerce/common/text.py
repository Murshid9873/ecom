def div_dec(funct):

    def wrapper(a,b) :
        if b > a :
            a,b = b,a

        return funct(a,b)
    return wrapper

@div_dec
def divide(a,b):
    res = a/b
    print(res)

divide(2,20)