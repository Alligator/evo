# individual.py
# Represents the individual compositions in a population
class Individual:
    def __init__(self, dna, fitness=0):
        self.dna = dna
        self.fitness = fitness

    # Getters
    def getDna():
        return self.dna
    def getFitness():
        return self.fitness

    # Setters
    def setDna(dna):
        self.dna = dna
    def setFitness(dna):
        self.fitness = fitness
