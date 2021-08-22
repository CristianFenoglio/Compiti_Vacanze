def bob(string):

    if string.endswith("?"):

        if string.isupper():
            return "Calm down, I know what I'm doing!"

        else:
            return "Sure."

    elif string.isupper():
        return "Whoa, chill out!"

    elif string == "":
        return "Fine. Be that way!"

    else:
        
        return "Whatever."

def main():
    question = input("> ")

    print(bob(question))
    
if __name__ == "__main__":
    main()