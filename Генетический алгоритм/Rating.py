from Data import countPopulation


def Rating(result_distance, way, avgGoodGen):
    res = ""
    rating = []

    #формирование списка особей
    for i in range(countPopulation):
        rating.append([i + 1, 0])

    #сортировка списка особей по результату
    for i in range(0, len(result_distance)):
        result_distance[i].sort(key=lambda el: el[2])

    #получение среднего результата 10 лучших особей
    for k in range(len(way)):
        avg = 0
        for i in range(10):
            avg += result_distance[k][i][2]
        avgGoodGen[k].append(round(avg/10, 3))

    #начисление баллов
    for k in range(0, countPopulation):
        a = ""
        for col in range(0, len(result_distance)):
            a += str(result_distance[col][k]) + " "
            rating[result_distance[col][k][3] - 1] = [result_distance[col][k][3], (countPopulation - k) + rating[result_distance[col][k][3] - 1][1]]
        res += a + "\n"

    #сортировка по баллам особей
    rating.sort(key=lambda a: a[1], reverse=True)

    return rating