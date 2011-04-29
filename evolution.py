# Evolution
from generation import Generation
import individual
import random
import sys
from individual import Individual

class Evolution:
    # Crossover masks
    SINGLE_POINT = '00000000000000001111111111111111'
    MULTI_POINT =  '00000000001111111111100000000000'
    UNIFORM =      '01010101010101010101010101010101'
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
        return winner[-2][1]

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
        self.currentGeneration = Generation(size)

if __name__ == '__main__':
    size = 50
    mutationRate = 0.85
    e = Evolution(size)
    f = open('results.txt', 'w')
    for n in range(0, 20000):
        #print e.currentGeneration.formatGeneration()
        f.write(str(sum([i.fitness for i in e.currentGeneration.population])/len(e.currentGeneration.population)))
        f.write('\n')
        sys.stdout.write('\r' + str(n))
        sys.stdout.flush()
        #if raw_input() == 'q':
        #    sys.exit(0)
        newpop = []
        for i in range(0, size):
            a = e.select(20, 0.5)
            b = e.select(20, 0.5)
            new = e.crossover(a.dna, b.dna, e.UNIFORM)
            if random.random() > mutationRate:
                notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
                for i in range (0, len(new)):
                    if random.random > mutationRate:
                        note = random.choice(notes)
                        note += str(random.randint(3, 5))
                        new[i] = note

            newpop.append(individual.Individual(new))
            #print a.dna, b.dna, newpop[-1].dna
        e.currentGeneration.setPopulation(newpop)
    f.close()

