def change(amount):
    money = [1, 5, 10, 25, 100]
    change = []

    while (amount != 0):
        if amount >= min(money):

            if (amount - max(money)) >= 0:
                change.append(max(money))
                amount -= max(money)

            else:
                money.remove(max(money))

        else:
            return "Not changeble"

    return change


print(change(37))