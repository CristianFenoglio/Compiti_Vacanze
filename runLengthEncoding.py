def run_length_encoding(string):
    contLetter = 1
    prec = ""
    finalString = ""

    string += " "

    for letter in string:
        if prec == letter:
            contLetter += 1
        
        elif contLetter != 1:
            finalString += str(contLetter) + prec
            contLetter = 1

        else:
            finalString += prec
        
        prec = letter

    return finalString


def main():
    string = input("Insert a string >>>")
    print(run_length_encoding(string))

if __name__ == "__main__":
    main()