from Move import Move
from Population import generationGene

#для получения результата особи с постоянной скоростью(зелёная функция)
def FactGen(way):
    factGen = generationGene()
    factRes = []
    for w in way:
        [g, t] = Move(factGen, w)
        factRes.append(g + t * 100)

    return factRes