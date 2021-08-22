from math import *
listofprobAllergies=['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
def es(score):
    listofAllergies=[]
    while score > 0:
        powerof2=1
        while powerof2*2 <= score:
            powerof2=powerof2*2
        score-=powerof2
        if sqrt(powerof2)<= len(listofprobAllergies):
            if powerof2==1:
                listofAllergies.append(listofprobAllergies[0])
            else:
                listofAllergies.append(listofprobAllergies[int(sqrt(powerof2))])
    return listofAllergies