def es(n):
    try:
        n=int(n)
        toret=""
        if n % 3==0:
            toret+='Pling'
        if n%5==0:
            toret+='Plang'
        if n%7==0:
            toret+='Plong'
        if toret=="":
            toret=str(n)
        return toret
    except ValueError:
        raise Exception("input Nan")
    
