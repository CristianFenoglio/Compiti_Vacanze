def es(lstofFactor, limit):
    sum=0
    for i in range(0, limit):
        for j in lstofFactor:
            if i%j==0:
                sum+=i
                break
    return sum