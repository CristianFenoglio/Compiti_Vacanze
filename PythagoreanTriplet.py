def isATriplet(a, b, c):
    return (a**2 + b**2==c**2)and(a<b and b<c)

def es(n):
    try:
        n=int(n)
        lstres=[]
        for c in range(n):
            for b in range(c):
                for a in range(b):
                    if isATriplet(a, b, c) and n==a+b+c:
                        lstres.append((a,b,c))
        return lstres
    except ValueError:
        raise Exception("input Nan")
