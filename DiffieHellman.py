from random import *

def primenumbers(limit, start=2):
    listofunmarkednumber=list(range(start, limit))
    for i in listofunmarkednumber:
        remouver=i*2
        while remouver< limit:
            if remouver in listofunmarkednumber:
                listofunmarkednumber.remove(remouver)
            remouver+=i
    return listofunmarkednumber

def es():
    pn=primenumbers(50)
    p=pn[randint(0, len(pn)-1)]
    g=p
    while  p>=g:
        g=pn[randint(0, len(pn)-1)]
    a=1
    b=1
    while a<=1 or a>p:

        a=int(input('chiave alice'))
    while b<=1 or b>p:
        b=int(input('chiave bob'))
    
    A = g**a % p
    B = g**b % p

    return B**a % p == A**b % p