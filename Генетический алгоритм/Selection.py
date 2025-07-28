from numpy.random import randint

from Data import countPopulation, countGen
from Mutation import mutation

#процесс скрещивания
def Selection(populationList, rating):
    list1 = rating[0:int(len(rating)/2):]
    list2 = rating[int(len(rating)/2):int(len(rating)):]
    listChoiceIndex = choiceIndexGen()

    for index in range(len(list2)):
        newPerson = [0] * countGen
        for numberGena in range(0, countGen):
            if numberGena in listChoiceIndex:
                newPerson[numberGena] = list.copy(populationList[list1[index][0] - 1][numberGena])
            else:
                newPerson[numberGena] = list.copy(populationList[list2[index][0] - 1][numberGena])
        populationList[list2[index][0] - 1] = mutation(newPerson)


def choiceIndexGen():
    listAllIndex = []
    listChoiceIndex = []

    for v in range(countGen):
        listAllIndex.append(v)

    for v in range(int(countGen/2) + 1):
        index = randint(0, len(listAllIndex))
        listChoiceIndex.append(listAllIndex[index])
        listAllIndex.pop(index)

    return listChoiceIndex

