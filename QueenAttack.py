def es(listoflist):
    cont=0
    blackpos=None
    whitepos=None
    for i in listoflist:
        if 'w' in i:
            
            whitepos=(i.index('w'), cont)
        if 'b' in i:
            blackpos=(i.index('b'), cont)
        cont+=1

    try:
        return(whitepos[1]==blackpos[1] or whitepos[0]==blackpos[0] or (abs(whitepos[0]-blackpos[0])==abs(whitepos[1]-blackpos[1])))
    except ValueError:
        raise Exception("there isn't a piece on the board")
