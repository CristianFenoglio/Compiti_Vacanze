def es(x):
    try:
        x=str(x)
        words=x.split(" ")
        for word in words:
            word=word.lower()
        toret={}
        while not len(words)==0:
            toret[words[0]]=1
            temp=words[0]
            words.remove(words[0])
            while temp in words:
                toret[temp]= toret[temp]+1
                words.remove(temp)
        return toret
    except ValueError:
        raise Exception("something goes wrong")
