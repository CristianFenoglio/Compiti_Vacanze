def es(x):
    try:
        alf=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        x=str(x)
        letters=list(x)
        for l in letters:
            l.lower()  
        while not len(letters)==0:
            if letters[0] in alf:
                alf.remove(letters[0])
            letters.remove(letters[0])
        return len(alf)==0
    except ValueError:
        raise Exception("something goes wrong")