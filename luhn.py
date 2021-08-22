def luhn(number):
    sumNumbers = 0

    numberSost = str(number).split()        #number sostitutivo trasformato da stringa a lista per eliminare gli spazi

    number = ""
        
    for i in numberSost:        #metto nella stringa i numeri della lista senza spazi
        number += i

    for n in range(0, len(str(number)), 2):

        if ((int(str(number)[n]) * 2) > 9):
            sumNumbers += (int(str(number)[n]) * 2) - 9
        
        else:
            sumNumbers += int(str(number)[n]) * 2

    for n in range(1, len(str(number)), 2):
        
        sumNumbers += int(str(number)[n])

    
    return sumNumbers % 10 == 0


print(luhn("4539 1488 0343 6467"))