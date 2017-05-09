def isReal(num):
    """checks if num is a valid number either float or int"""
    try:
        float(num)
        return True
    except: return False
    
def getCoeff():
    """get the coefficient of a polynomial and return it as a list"""
    coeff=[]
    num_of_element = input("enter number of coefficient ")
    for x in range(int(num_of_element)):
        valid=False
        while valid == False:
            value = input("enter coefficient for x^{}: ".format(x))
            if isReal(value):
                coeff.append(float(value))
                valid=True
            else: print("invalid input, try again!!")
    print(coeff)
    return coeff
            
def polynomial(coeff):
    """ takes a list or tuple of coeff or get a list of coeff and solves the polynomial"""
    datatypes=[list,tuple]
    if type(coeff) not in datatypes:
        coeff=getCoeff()
        print(coeff)
    ask = None
    while ask != '0':
        valueX = input("enter value for x: ")
        if isReal(valueX):
                valueX = float(valueX)
                answer = 0
                for x in range(len(coeff)):
                    answer += coeff[x] * (valueX ** x)
                ask='0'
        else:
            print("invalid value for x")
            ask = input("press (0) to exit or anykey to continue: ")
    print(answer)
    return answer

polynomial(12)
