def es(root, string):
    toret=''
    for c in string:
        if ord(c)<=122 and ord(c)>=97:
            toret+=chr((int((ord(c)-97+root))%26+97))
        else:
            toret+=c
    return toret
