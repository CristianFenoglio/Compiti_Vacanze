def es(word):
    try:
        word=str(word)
        letters=list(word)

        while not len(letters)==0:
            temp=letters[0]
            letters.remove(letters[0])
            if temp in letters and not (temp==" " or temp=="-"):
                return False
        return True
    except ValueError:
        raise Exception("wrong input")