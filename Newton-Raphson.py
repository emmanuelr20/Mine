def isReal(num):
    """checks if num is a valid number either float or int"""
    try:
        float(num)
        return True
    except: return False
    
def getCoeff():
    """get the coefficient of a polynomial and return it as a list"""
    coeff=[]
    valid=False
    while valid == False:
        num_of_element = input("enter number of coefficient ")
        if num_of_element.isdigit():
            num_of_element=int(num_of_element)
            valid=True
        else: print("invalid input, try again!!")
    for x in range(num_of_element):
        valid=False
        while valid == False:
            value = input("enter coefficient for x^{}: ".format(x))
            if isReal(value):
                coeff.append(float(value))
                valid=True
            else: print("invalid input, try again!!")
    return coeff

def polynomial(coeff,x):
    """solve polynomial taking coefficient [list,tuple] and float value of x """
    fx = 0
    pow = 0
    for i in coeff:
        fx += i * (x ** pow)
        pow += 1
    return fx

def differentiate(coeff):
    """differentiate a function by taking it coefficient"""
    index=0
    for x in coeff:
        coeff[index] = x*index
        index += 1
    coeff = coeff[1:]
    return coeff

def Newton():
    """solves newton rapshon """
    epsilon=0.0001
    ask=1
    while ask != '0':
        x = input("Enter intial guess for x: ")
        if isReal(x):
            x=float(x)
            coeff = getCoeff()
            dcoeff = differentiate(coeff[:])
            fx = 100000
            counter=0
            while abs(fx) > epsilon:
                counter += 1
                fx = polynomial(coeff,x)
                dfx =polynomial(dcoeff,x)
                if dfx == 0:
                    print (" x = ", x)
                    print("the function has no real root")
                    break
                x -= fx / dfx
            ask='0'
            print("\nf(x)= {}\n".format(coeff),"f'(x) = {}\n".format(dcoeff), "root of f(x) is x = {}\n".format(x))
        else: 
            print("x is not a digit try again")
            ask = input("press (0) to exit or anykey to continue: ")
    return x,counter

print(Newton())
