# generation.py
# Represents a single generation of individuals
import random
import utils
from math import sqrt
from individual import Individual

class Generation:
    # All possible notes (NOT all possible pitches)
    population = []
    scales = [
        # Major
        ['C','D','E','F','G','A','B'],
        # Chromatic
        ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'],
        # Pentatonic
        ['C', 'D', 'E', 'G', 'A'],
        # Hexatonic
        ['C','D','E','F#','G#','A#']
        ]

    # createGeneration()
    # Create a ne"w generation filled with random data
    def createGeneration(self, size):
        for i in range(0, size):
            self.population.append(Individual())

    # formatGeneration()
    # Returns a formatted printable string showing
    # the generation and it's scores.
    def formatGeneration(self, pop=[]):
        if not pop:
            pop = self.population
        width = len(pop[0].dna)*4
        fmtstring = '{0: <'+str(width)+'}{1}'
        out = fmtstring.format('DNA', '| Fitness') + "\n"
        out += ('{0:-^'+str(width)+'}').format('') + '+--------\n'
        i = 0
        for ind in pop:
            i += 1
            for note in ind.dna:
                out += note
                if len(note) == 2:
                    out += '  '
                else:
                    out += ' '
            out += '| {0:2.3f}'.format(ind.fitness) + "\n"
        return out
 
    # evaluateFitness()
    # Evaluate the fitness of the population
    def evaluateFitness(self):
        # For each individual
        for ind in self.population:
            #print ind.dna
            scores = []
            # For each scale to be checked
            for scale in self.scales:
                currentScore = 0
                # For the notes in each individua
                for i in range(0, len(ind.dna)-1):
                    current = ind.dna[i][:-1]
                    next = ind.dna[i+1][:-1]
                    # If the current note pair both belong to the same scale
                    if current and next in scale:
                        # Increase the score
                        currentScore += 1
                scores.append(currentScore)
            # Standard deviation in one line. Eeep.
            ind.fitness = sqrt(sum([(i - float(sum(scores))/len(scores))**2 for i in scores])/len(scores))
 
    def setPopulation(self, population):
        self.population = population
        self.evaluateFitness()

    # Constructor
    # The population can be given as a list of individuals, or
    # generated.
    def __init__(self, size, population=[]):
        if not population: #if individuals is empty
            self.createGeneration(size)
        else:
            self.population = population
        self.evaluateFitness()
