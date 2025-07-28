from Data import speed, type_way

#Создание начальной особи
def generationGene():
    gen = []

    for i in speed:
        for j in type_way:
            for k in type_way:
                gen.append([i, j, k, 0])

    return gen

#Создание начального поколения
def Population(countPopulation):
    populationList = []

    for i in range(0, countPopulation):
        populationList.append(generationGene())

    return populationList
