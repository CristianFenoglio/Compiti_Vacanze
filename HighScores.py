def top(aList):
    if len(aList)<3:
        raise Exception("list too short")
    tupl=[max(aList)]
    aList.remove(max(aList))
    while len(tupl)<3:
        tupl.append(max(aList))
        aList.remove(max(aList))
    return (tupl[0], tupl[1], tupl[2])

def es(aRankList):
    return [max(aRankList), aRankList[-1], top(aRankList)]