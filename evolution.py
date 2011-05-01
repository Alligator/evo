# Evolution
from generation import Generation
import individual
import random
import sys
from individual import Individual

class Evolution:
    # Crossover masks
    masks = { 'single' : '00000000000000001111111111111111',
              'multi'  : '00000000001111111111100000000000',
              'uniform1':'01010101010101010101010101010101',
              'uniform2':'00110011001100110011001100110011',
              'uniform3':'11110000111100001111000011110000'
            }
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
        flip = random.choice(['1', '0'])
        for i in range(0, len(mask)):
            if mask[i] == flip:
                dna.append(a[i])
            else:
                dna.append(b[i])
        return dna

    def __init__(self, size):
        self.currentGeneration = Generation(size)

if __name__ == '__main__':

    # size mr g ts tp ct
    size = int(sys.argv[1])
    mutationRate = float(sys.argv[2])
    generations = int(sys.argv[3])
    tournamentSize = int(sys.argv[4])
    tournamentProb = float(sys.argv[5])
    crossoverType = sys.argv[6]
    filename = 's{0}_mr{1:2.2f}_g{2}_ts{3}_tp{4:2.2f}_c{5}.txt'.format(size, mutationRate, generations, tournamentSize, 
                                                            tournamentProb, crossoverType)
    e = Evolution(size)
    f = open(filename, 'w')
    f.write('size: {0} mutation: {1} generations: {2} tsize: {3} tprob: {4} crossover: {5}\n'.format(
        size, mutationRate, generations, tournamentSize, tournamentProb, crossoverType))
    for n in range(0, generations):
        #print e.currentGeneration.formatGeneration()
        avg = sum([i.fitness for i in e.currentGeneration.population])/len(e.currentGeneration.population)
        best = sorted([i.fitness for i in e.currentGeneration.population])[-1]
        sys.stdout.write('\r' + str(n))
        if n % (generations/1000) == 0:
            f.write(str(n) + "," + str(avg) + "," + str(best) + '\n')
            sys.stdout.write('\t' + str(avg) + '\t' + str(best))
        sys.stdout.flush()
        #if raw_input() == 'q':
        #    sys.exit(0)
        newpop = []
        for i in range(0, size):
            a = e.select(tournamentSize, tournamentProb)
            b = e.select(tournamentSize, tournamentProb)
            #new = e.crossover(a.dna, b.dna, random.choice([e.UNIFORM, e.SINGLE_POINT, e.MULTI_POINT]))
            new = e.crossover(a.dna, b.dna, e.masks[crossoverType])
            if random.random() < mutationRate:
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

