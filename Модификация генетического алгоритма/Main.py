from random import randint

from Data import way, way_mountain, way_plain, way_mix, countStep, countPopulation, lengthWay
from FactGen import FactGen
from Move import Move
from Population import Population
from Rating import Rating
from Selection import Selection
from Сhart import createChartThree, createChartWayThree, createChartWithWeather, createTableBestGenotype


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

def setChanceSun():
    chance_sun = []
    check = False

    for i in range(lengthWay):
        chance = randint(1, 5)

        if chance == 1 and check == False:
            chance_sun.append(True)
            check = True
        else:
            check = False
            chance_sun.append(False)

    return chance_sun

#весь алгоритм
def Algorithm(current_way, name):
    populationListForTypeWeather = Population(countPopulation) #формирование начального поколения
    totalGoodGen = []
    totalAvgGoodGen = []
    totalFactGen = []
    totalAvgBestThreeWay = []
    chance_sun = setChanceSun()


    for type_weather in range(1, 4):
        goodGen = []  # для записи лучших результатов
        avgGoodGen = []  # для записи среднего значения для 10 лучших результатов
        avgBestThreeWay = []  # для записи лучшего среднего значения среди по всем трассам в поколение(последний график)


        for x in range(len(way)):
            goodGen.append([])
            avgGoodGen.append([])

        populationList = populationListForTypeWeather.copy()

        for n in range(0, countStep):
            result_distance = []

            for i in range(0, len(current_way)):
                current_step = []
                searchGoodGen = 1000

                for index in range(len(populationList)):
                    [g, t] = Move(populationList[index], current_way[i], type_weather, chance_sun)
                    current_step.append([g, t, g + t * 100, index + 1])
                    searchGoodGen = min(searchGoodGen, g + t * 100)

                goodGen[i].append(searchGoodGen) #запись лучшего гена
                result_distance.append(current_step) #запись результатов каждой особи поколения

            avgBestThreeWay.append(setAvgBestWay(current_way, result_distance))
            rating = Rating(result_distance, current_way, avgGoodGen) #определение рейтинга

            if n != countStep - 1: #в последней итерации оставнока просиходит раньше
                Selection(populationList, rating) #селекция
            else:
                createTableBestGenotype(populationList[rating[0][0]], name + " " + str(type_weather))

        totalFactGen.append(FactGen(current_way, type_weather, chance_sun)) #фактическая особь(для графиков)
        totalGoodGen.append(goodGen.copy())
        totalAvgGoodGen.append(avgGoodGen.copy())
        totalAvgBestThreeWay.append(avgBestThreeWay.copy())

    createChartWithWeather(name, totalGoodGen, totalAvgGoodGen, totalFactGen, totalAvgBestThreeWay) #формирование графиков с результатами алгоритма

Algorithm(way_plain, "Равнинные трассы")
Algorithm(way_mountain, "Горные трассы")
Algorithm(way_mix,  "Смешанные трассы")
Algorithm(way,  "Все трассы")

