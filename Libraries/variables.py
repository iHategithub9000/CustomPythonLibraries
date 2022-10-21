intlimit = 2147483647
negativeintlimit = -2147483648
pi = 3.141592653589793
def rand(a,b):
    import random
    return random.randint(a,b)

def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "No."
    else:
        return a / b
def exp(a,b):
    return a ** b

def printtype(var):
    print(str(type(var)).replace("<class '", "").replace(">","").replace("'",""))
def killuser():
    for i in range(intlimit):
        if not i == 0:
            print("GET READY FOR MATH "+i)
