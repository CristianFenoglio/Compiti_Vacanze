import random
lstofName=[]
def es():
    name= None
    while name==None or name in lstofName:
        name=chr(random.randint(65, 91))+chr(random.randint(65, 91))+str(random.randint(100, 1000))
    lstofName.append(name)
    return name