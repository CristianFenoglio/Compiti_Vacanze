def es(number, start=2):
    for div in range(int(start+1), int(number+1)):
        if int(number) % div ==0 and not div==1:
            break
    if number/div ==1:
        return div
    return div, es (number/div, div-1)
