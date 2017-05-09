def differentiate(coeff):
    index=0
    for x in coeff:
        coeff[index]=x*index
        index+=1
    coeff=coeff[1:]
    return coeff

coefficient=[1,2,3]
dcoeff=differentiate(coefficient)
