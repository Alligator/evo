# Evolution
import generation
import individual
import random
import sys
from individual import Individual

class Evolution:
    # Crossover masks
    SINGLE_POINT = '00000000000000001111111111111111'
    MULTI_POINT =  '00000000001111111111100000000000'
    age = 0

    # select()
    # Perform a tournament selection of the given size, and probability
    # Returns an individual.
    def select(self, size, p):
        members = []
        # Select the members of the tournament
        chosen = random.sample(self.currentGeneration.population, size)

        # Sort the members
        sort = sorted(chosen, key=lambda ind: ind.fitness, reverse=True)

        # Calculate each member's probabilities
        for i in range(0, len(chosen)):
            prob = p*((1-p)**(i))
            members.append((prob, sort[i]))

        # Now we select the winner!
        winner = sorted((random.random() * m[0], m[1]) for m in members)
        return winner[-1][1]

    # crossover()
    # Takes two dna sequences and crosses them over according to
    # the specified mask. Returns a dna sequence.
    def crossover(self, a, b, mask):
        dna = []
        for i in range(0, len(mask)):
            if mask[i] == '0':
                dna.append(a[i])
            else:
                dna.append(b[i])
        return dna

    def __init__(self, size):
        self.currentGeneration = generation.Generation(size)

if __name__ == '__main__':
    size = 20
    e = Evolution(size)
    while True:
        print e.currentGeneration.formatGeneration()
        if raw_input() == 'q':
            sys.exit(0)
        newpop = []
        for i in range(0, size):
            a = e.select(4, 0.5)
            b = e.select(4, 0.5)
            newpop.append(individual.Individual(e.crossover(a.dna, b.dna, e.SINGLE_POINT)))
            #print a.dna, b.dna, newpop[-1].dna
        print e.currentGeneration.formatGeneration(newpop)
        e.currentGeneration = False
        #e.currentGeneration = generation.Generation(len(newpop), newpop)

