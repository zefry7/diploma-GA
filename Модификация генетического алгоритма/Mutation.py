from random import randint
from Data import change_speed_20, change_speed_60, change_speed


#процесс мутации
def mutation(gen):
    mutation_active = randint(0, 3)
    if mutation_active == 1:
        for ind in range(0, 15):
            index_gen = randint(0, 4)
            if gen[ind * 5 + index_gen][0] == 20:
                index_change_speed = randint(0, 1)
                gen[ind * 5 + index_gen][3] = change_speed_20[index_change_speed]
            elif gen[ind * 5 + index_gen][0] == 60:
                index_change_speed = randint(0, 1)
                gen[ind * 5 + index_gen][3] = change_speed_60[index_change_speed]
            else:
                index_change_speed = randint(0, 2)
                gen[ind * 5 + index_gen][3] = change_speed[index_change_speed]
    return (
        list.copy(gen))