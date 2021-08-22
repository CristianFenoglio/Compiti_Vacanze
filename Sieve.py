def es(limit, start=2):
    listofunmarkednumber=list(range(start, limit))
    for i in listofunmarkednumber:
        remouver=i*2
        while remouver< limit:
            if remouver in listofunmarkednumber:
                listofunmarkednumber.remove(remouver)
            remouver+=i
    return listofunmarkednumber