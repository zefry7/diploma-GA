from Data import way, way_mountain, way_plain, way_mix, countStep, countPopulation
from FactGen import FactGen
from Move import Move
from Population import Population
from Rating import Rating
from Selection import Selection
from Сhart import createChartThree, createChartWayThree, createTableBestGenotype


#нахождение лучшего среднего (для последняго графика)
def setAvgBestWay(current_way, result_distance):
    mass = []
    for i in range(countPopulation):
        sum_res = 0
        for j in range(len(current_way)):
            for k in range(len(result_distance[j])):
                if result_distance[j][k][3] == i + 1:
                    sum_res += result_distance[j][k][2]
        mass.append(sum_res/len(current_way))
    return min(mass)

#весь алгоритм
def Algorithm(current_way, name):
    goodGen = [] #для записи лучших результатов
    avgGoodGen = [] #для записи среднего значения для 10 лучших результатов
    avgBestThreeWay = [] #для записи лучшего среднего значения среди по всем трассам в поколение(последний график)

    for x in range(len(way)):
        goodGen.append([])
        avgGoodGen.append([])

    populationList = Population(countPopulation) #формирование начального поколения

    for n in range(0, countStep):
        result_distance = []

        for i in range(0, len(current_way)):
            current_step = []
            searchGoodGen = 1000

            for index in range(len(populationList)):
                [g, t] = Move(populationList[index], current_way[i])
                current_step.append([g, t, g + t * 100, index + 1])
                searchGoodGen = min(searchGoodGen, g + t * 100)

            goodGen[i].append(searchGoodGen) #запись лучшего гена
            result_distance.append(current_step) #запись результатов каждой особи поколения

        avgBestThreeWay.append(setAvgBestWay(current_way, result_distance))
        rating = Rating(result_distance, current_way, avgGoodGen) #определение рейтинга

        if n != countStep - 1: #в последней итерации оставнока просиходит раньше
            Selection(populationList, rating) #селекция
        # else:
        #     print(rating)
        #     print(populationList[rating[0][0]])
        #     createTableBestGenotype(populationList[rating[0][0]], name)

    factGen = FactGen(current_way) #фактическая особь(для графиков)
    createChartThree(name, goodGen, avgGoodGen, factGen, avgBestThreeWay) #формирование графиков с результатами алгоритма


Algorithm(way_plain, "Равнинные трассы")
Algorithm(way_mountain, "Горные трассы")
Algorithm(way_mix,  "Смешанные трассы")
Algorithm(way,  "Все трассы")
