def es(x):
    
    trasm={'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    x=str(x)
    letters=list(x)
    toret=""
    while not len(letters)==0:
        try:
            toret+=trasm[letters[0]]
        except ValueError:
            raise Exception("wrong input")
        letters.remove(letters[0])
    return toret
    
