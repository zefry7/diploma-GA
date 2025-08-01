countStep = 500
countPopulation = 50
countGen = 75
lengthWay = 30
type_way = [-2, -1, 0, 1, 2]
speed = [20, 40, 60]
change_speed = [-20, 0, 20]

#трассы всех типов
way = [
    [0, 0, 1, 0, 0, -2, 0, 0, 2, 0, -1, 0, 1, 0, -1, 0, 0, 1, 0, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0],
    # [0, -2, 0, 0, 0, 1, 0, 0, 1, 0, -1, 1, 0, 0, 0, 0, -1, 0, 0, 1, 0, -1, 0, 1, 0, -1, 1, 0, 0, 0],
    # [-1, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1, 0, 2, 0, 0, -1, 0, 1, 0, 0, -2, 0, 0, 1, 0, -1, 0, 0, 2, 0],
    [1, 0, 1, 2, 0, 2, 0, -2, 0, -2, -1, 0, -1, 0, 0, 0, 1, -2, 0, 1, 2, 0, 0, 1, 0, 2, 0, -2, -2, 0],
    # [0, 1, 0, -2, -1, -2, 0, 1, 0, 2, 2, 0, 1, 0, -2, 0, 2, 0, 0, -2, -1, 0, 2, -1, 1, 0, -1, 0, 1, 2],
    # [1, 0, 2, 0, 1, 2, 1, -1, -2, 0, -1, -1, 0, -2, 0, 1, -1, 0, 0, 0, 0, -2, 0, 2, 2, -1, 0, 0, 1, 2],
    [0, 1, 0, 0, -2, 2, 0, 0, 1, 0, -1, 2, -2, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, -1, 0, -1, 2, -1],
    # [2, 0, 1, 0, 0, 1, 0, -1, 0, 0, 1, 0, -1, -1, 0, 0, 0, 1, 1, -1, 0, -1, 0, 1, 0, 1, 0, 0, -1, 0],
    # [0, 0, -2, -1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, -1, 1, 0, -1, 2, 0]
]

#ровнинные трассы
way_plain = [
    [0, 0, 1, 0, 0, -2, 0, 0, 2, 0, -1, 0, 1, 0, -1, 0, 0, 1, 0, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0],
    [0, -2, 0, 0, 0, 1, 0, 0, 1, 0, -1, 1, 0, 0, 0, 0, -1, 0, 0, 1, 0, -1, 0, 1, 0, -1, 1, 0, 0, 0],
    [-1, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1, 0, 2, 0, 0, -1, 0, 1, 0, 0, -2, 0, 0, 1, 0, -1, 0, 0, 2, 0]
]

#горные трассы
way_mountain = [
    [1, 0, 1, 2, 0, 2, 0, -2, 0, -2, -1, 0, -1, 0, 0, 0, 1, -2, 0, 1, 2, 0, 0, 1, 0, 2, 0, -2, -2, 0],
    [0, 1, 0, -2, -1, -2, 0, 1, 0, 2, 2, 0, 1, 0, -2, 0, 2, 0, 0, -2, -1, 0, 2, -1, 1, 0, -1, 0, 1, 2],
    [1, 0, 2, 0, 1, 2, 1, -1, -2, 0, -1, -1, 0, -2, 0, 1, -1, 0, 0, 0, 0, -2, 0, 2, 2, -1, 0, 0, 1, 2]
]

#смешанные трассы
way_mix = [
    [0, 1, 0, 0, -2, 2, 0, 0, 1, 0, -1, 2, -2, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, -1, 0, -1, 2, -1],
    [2, 0, 1, 0, 0, 1, 0, -1, 0, 0, 1, 0, -1, -1, 0, 0, 0, 1, 1, -1, 0, -1, 0, 1, 0, 1, 0, 0, -1, 0],
    [0, 0, -2, -1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, -1, 1, 0, -1, 2, 0]
]

finish_way = [
    [0, 1, 0, 0, -1, 0, 2, 0, 0, -2, 0, 0, 1, 0, -1, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0],
    [-2, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, -1, -1, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0],
    [2, 1, 0, 0, 2, 1, 0, -1, 0, -2, 1, 0, 0, -2, -2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 2, 1, 0, -1, 0, 2, 2, 0, -2, -2, 0, -1, -1, 0, -1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [-1, 0, 2, 2, 1, 0, -1, 0, 2, -1, -2, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 0, 1],
    [-1, 0, 0, 0, -1, 0, 0, 2, 0, 2, 0, 0, -2, 0, 0, 1, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 2, 0, 1, 0],
    [0, 0, 1, 0, -1, 2, 1, -1, 0, 1, 0, 1, -2, -1, -1, 0, 0, 1, 0, 1, -1, 0, 0, 0, 1, 0, 1, -2, 0, 1],
    [2, 0, 0, 1, 1, 0, -2, -1, 0, -1, 0, 0, 1, 0, -1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, -1, 0, 1, 1]
]

finish_way_plain = [
    [0, 1, 0, 0, -1, 0, 2, 0, 0, -2, 0, 0, 1, 0, -1, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0],
    [-2, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, -1, -1, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0]
]

finish_way_mountain = [
    [2, 1, 0, 0, 2, 1, 0, -1, 0, -2, 1, 0, 0, -2, -2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 2, 1, 0, -1, 0, 2, 2, 0, -2, -2, 0, -1, -1, 0, -1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [-1, 0, 2, 2, 1, 0, -1, 0, 2, -1, -2, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 0, 1]
]

finish_way_mix = [
    [-1, 0, 0, 0, -1, 0, 0, 2, 0, 2, 0, 0, -2, 0, 0, 1, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 2, 0, 1, 0],
    [0, 0, 1, 0, -1, 2, 1, -1, 0, 1, 0, 1, -2, -1, -1, 0, 0, 1, 0, 1, -1, 0, 0, 0, 1, 0, 1, -2, 0, 1],
    [2, 0, 0, 1, 1, 0, -2, -1, 0, -1, 0, 0, 1, 0, -1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, -1, 0, 1, 1]
]

#топливо - резкий спуск
gas_fast_descent = [
    [0, 1, 2],
    [0, 0, 1],
    [0, 0, 0]
]

#топливо - спуск
gas_descent = [
    [1, 3, 5],
    [0, 1, 3],
    [0, 0, 2]
]

#топливо - ровная
gas_way = [
    [5, 7, 12],
    [2, 6, 10],
    [1, 4, 8]
]

#топливо - подъём
gas_ascent = [
    [10, 14, 25],
    [8, 12, 20],
    [6, 10, 16]
]

#топливо - резкий подъём
gas_fast_ascent = [
    [15, 21, 37],
    [12, 18, 30],
    [8, 15, 24]
]

#ограничения для мутации
change_speed = [-20, 0, 20]
change_speed_20 = [0, 20]
change_speed_60 = [-20, 0]