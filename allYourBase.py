def all_your_base(number, base):
    numberDecimal = 0
    counter = 0

    for c in str(number):
        numberDecimal += int(c) * base ** (len(str(number)) - counter - 1)      #** -> elevato

        counter += 1

    return numberDecimal


print(all_your_base(42, 10))