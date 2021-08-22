def es(n, d):
    int(len(d)/2)
    l=list(d.items()) 
    if l[int(len(l)/2)][0]<n:
        start= int(len(l)/2)
        end = len(l)
    else:
        start=0
        end=int(len(l)/2)
    for i in range(start, end):
        if n==l[i][0]:
            return l[i][1]
    return None

