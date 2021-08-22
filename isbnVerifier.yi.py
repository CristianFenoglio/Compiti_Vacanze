def isbn_verifier(isbn):
    numMax = 10
    sumIsbn = 0

    if "-" in isbn:     #se trattini presenti in isbn
        isbnSost = str(isbn).split("-")        #number sostitutivo trasformato da stringa a lista per eliminare gli spazi

        isbnString = ""
        
        for i in isbnSost:        #metto nella stringa i numeri della lista senza spazi
            isbnString += i

    else:
        isbnString = isbn

    
    for n in range(0, len(isbnString), 1):
        sumIsbn += n * numMax

        numMax -= 1

    
    return sumIsbn % 11 == 0


print(f"- {isbn_verifier('3-598-21508-8')}")
print(isbn_verifier("3-598-21508-8"))