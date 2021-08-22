TOTALOFCAHESSBORAD=64
def es(numberofchessboard):
    total=0
    for numb in range(TOTALOFCAHESSBORAD):
        total=total+2**numb
    return total, 2**(numberofchessboard-1)

