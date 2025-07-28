from Move import Move
from Population import generationGene

#для получения результата особи с постоянной скоростью(зелёная функция)
def FactGen(way, type_weather, chance_sun):
    factGen = generationGene()
    factRes = []
    for w in way:
        [g, t] = Move(factGen, w, type_weather, chance_sun)
        factRes.append(g + t * 100)

    return factRes