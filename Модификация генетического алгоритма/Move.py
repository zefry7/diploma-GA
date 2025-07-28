from Data import gas_fast_descent, speed, gas_descent, gas_way, gas_ascent, gas_fast_ascent, type_way

#получение количества топлива
def useGas(way, start_speed, end_speed):
    if way == -2:
        return gas_fast_descent[speed.index(start_speed)][speed.index(end_speed)]
    elif way == -1:
        return gas_descent[speed.index(start_speed)][speed.index(end_speed)]
    elif way == 0:
        return gas_way[speed.index(start_speed)][speed.index(end_speed)]
    elif way == 1:
        return gas_ascent[speed.index(start_speed)][speed.index(end_speed)]
    elif way == 2:
        return gas_fast_ascent[speed.index(start_speed)][speed.index(end_speed)]

#прохождение трассы
def Move(gen, way, type_weather, chance_sun):
    current_speed = 40
    result = [0, 0, []]

    if type_weather == 1:
        result = Sunny_weather(gen, way, current_speed)
    elif type_weather == 2:
        result = Cloudy_weather(gen, way, current_speed, chance_sun)
    elif type_weather == 3:
        result = Gloomy_weather(gen, way, current_speed)

    total_gas = result[0]
    time = result[1]
    avg_speed = result[2]

    total_gas += useGas(way[len(way) - 1], current_speed, 40) #получение количества топлива на последнем участке
    avg_speed.append((current_speed + 40) / 2) #средняя скорость на последнем участке

    for i in range(0, len(avg_speed)):
        time += 1/avg_speed[i]

    return [total_gas, round(time, 5)]


def Sunny_weather(gen, way, current_speed):
    flag_60 = False
    flag_stop = False
    total_gas = 0
    avg_speed = []
    time = 0

    for ind in range(0, len(way) - 1):
        ind_gen = 25 * speed.index(current_speed) + 5 * type_way.index(way[ind]) + type_way.index(way[ind + 1])  # вычисление индекса гена
        total_gas += useGas(way[ind], current_speed, current_speed + gen[ind_gen][3])  # получение количества топлива
        avg_speed.append((current_speed + current_speed + gen[ind_gen][3]) / 2)  # нахождения средней скорости (для времени)

        if current_speed == 60 and flag_60 == True:
            # print("Два участка подряд скорость по 60")
            flag_stop = True
            time += 0.15

        if current_speed == 60 and flag_stop == False:
            flag_60 = True
        else:
            flag_stop = False
            flag_60 = False

        current_speed += gen[ind_gen][3] #изменение скорости после прохождения текущего участка

    return [total_gas, time, avg_speed]

def Cloudy_weather(gen, way, current_speed, chance_sun):
    count_speed_60 = True
    total_gas = 0
    avg_speed = []
    time = 0

    for ind in range(0, len(way) - 1):
        ind_gen = 25 * speed.index(current_speed) + 5 * type_way.index(way[ind]) + type_way.index(way[ind + 1])  # вычисление индекса гена

        if chance_sun[ind]:
            count_speed_60 = True

        if current_speed + gen[ind_gen][3] == 60 and count_speed_60 == True:
            next_speed = 40
        elif current_speed + gen[ind_gen][3] == 60:
            count_speed_60 = False
            next_speed = 60
        else:
            next_speed = current_speed + gen[ind_gen][3]

        total_gas += useGas(way[ind], current_speed, next_speed)  # получение количества топлива
        avg_speed.append((current_speed + next_speed) / 2)  # нахождения средней скорости (для времени)

        current_speed = next_speed  # изменение скорости после прохождения текущего участка

    return [total_gas, time, avg_speed]

def Gloomy_weather(gen, way, current_speed):
    count_speed_60 = 2
    total_gas = 0
    avg_speed = []
    time = 0

    for ind in range(0, len(way) - 1):
        ind_gen = 25 * speed.index(current_speed) + 5 * type_way.index(way[ind]) + type_way.index(way[ind + 1])  # вычисление индекса гена

        if current_speed + gen[ind_gen][3] == 60 and count_speed_60 == 0:
            next_speed = 40
        elif current_speed + gen[ind_gen][3] == 60:
            count_speed_60 -= 1
            next_speed = 60
        else:
            next_speed = current_speed + gen[ind_gen][3]

        total_gas += useGas(way[ind], current_speed, next_speed)  # получение количества топлива
        avg_speed.append((current_speed + next_speed) / 2)  # нахождения средней скорости (для времени)


        current_speed = next_speed  # изменение скорости после прохождения текущего участка

    return [total_gas, time, avg_speed]