def giveprimenumber(limit, start=2):
    listofunmarkednumber=list(range(start, limit))
    for i in listofunmarkednumber:
        remouver=i*2
        while remouver< limit:
            if remouver in listofunmarkednumber:
                listofunmarkednumber.remove(remouver)
            remouver+=i
    return listofunmarkednumber

def es(number):
    primenumbers=giveprimenumber(number+1)
    if not number in primenumbers:
        return f'{number} is not a prime'
    return f'{len(primenumbers)}th'