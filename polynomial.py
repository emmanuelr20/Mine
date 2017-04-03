print("solve the polynomil of 7x^4+9.3x^3+5x^2")
ask=1
while ask !=0:
    answer=0
    value=input("enter value for x: ")
    if value.isdigit():
        value=int(value)
        coeff=(0,0,0,5,9.3,7)
        answer=0
        pow=0
        for x in coeff:
            answer+=x*(value**pow)
            pow+=1
        print(answer)
    else: print("invalid value for x")
    ask=input("press (0) to exit or anykey to continue: ")
