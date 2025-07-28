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
def Move(gen, way):
    current_speed = 40
    total_gas = 0
    avg_speed = []

    for ind in range(0, len(way) - 1):
        ind_gen = 25 * speed.index(current_speed) + 5 * type_way.index(way[ind]) + type_way.index(way[ind + 1]) #вычисление индекса гена
        total_gas += useGas(way[ind], current_speed, current_speed + gen[ind_gen][3]) #получение количества топлива
        avg_speed.append((current_speed + current_speed + gen[ind_gen][3])/2) #нахождения средней скорости (для времени)
        current_speed += gen[ind_gen][3] #изменение скорости после прохождения текущего участка

    total_gas += useGas(way[len(way) - 1], current_speed, 40) #получение количества топлива на последнем участке
    avg_speed.append((current_speed + 40) / 2) #средняя скорость на последнем участке

    time = 0
    for i in range(0, len(avg_speed)):
        time += 1/avg_speed[i]

    return [total_gas, round(time, 5)]

