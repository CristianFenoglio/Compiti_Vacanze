val={
'Black': 0,
'Brown': 1,
'Red': 2,
'Orange': 3,
'Yellow': 4,
'Green': 5,
'Blue': 6,
'Violet': 7,
'Grey': 8,
'White': 9
}

def es(x):
    toret=0
    cont=1
    for color in x:
        try: 
            toret+=val[color]*(10**(len(x)-cont))
            cont+=1
        except ValueError:
            raise Exception("wrong input")
    
    return toret
