
def issecondinfirst(listA, listB):
    for i in range(len(listA)-len(listB)+1):
        if listA[i] == listB[0]:
            istrue=True
            for a in range (len(listB)):
                if not listA[a+i]==listB[a]:
                    istrue=False
                    break
            if istrue:
                return True
    return False


def es(listA, listB):
    if listA==listB:
        return 'A and B are equal'
    else:
        if len(listB)< len(listA):
            if issecondinfirst(listA, listB):
                return 'A is a superlist of B'
        else:
            if issecondinfirst(listB, listA):
                return 'A is a sublist of B'
    return 'A is not a superlist of, sublist of or equal to B'