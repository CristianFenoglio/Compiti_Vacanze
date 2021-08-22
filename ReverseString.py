def reverse_string(string):
    rev_string = ""
    cont = len(string) - 1

    while cont >= 0:
        rev_string += string[cont]
        cont = cont - 1

    return rev_string

def main():
    string = input("Insert a word >>>")

    print(f"{reverse_string(string)}")

if __name__ == "__main__":
    main()