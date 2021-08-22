from abc import abstractproperty


def series(series, number):
    lst_result = []

    for i in range(len(str(number))):
        if i + series > len(str(number)):
            break

        ris = ""
        for k in range(i, i + series):      #k prende le lettere da i a i + serie (es da 0 a 3)
            
            ris += str(number)[k]

        lst_result.append(ris)

    return lst_result


print(series(4,49142))