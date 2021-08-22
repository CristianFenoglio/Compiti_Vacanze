def es(numb, numberofstep=0):
    if numb==1:
        return numberofstep
    if numb%2==0:
        return es(numb/2, numberofstep+1)
    else:
        return es(3*numb+1, numberofstep+1)
