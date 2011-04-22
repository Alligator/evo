# generation.py
# Represents a single generation of individuals
import random
import utils
from individual import Individual

class Generation:
    # All possible notes (NOT all possible pitches)
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # createGeneration()
    # Create a new generation filled with random data
    def createGeneration(self):
        pass

    # createIndividual
    # Creates a new individual filled with random data
    def createIndividual(self):
        individual = []
        for i in range(0, 16):
            random.seed()
            note = random.choice(self.notes)
            octave = random.randint(3, 5)
            individual.append(note + str(octave))
        return individual

    def __init__(self, individuals=[]):
        if not individuals: #if individuals is empty
            self.createGeneration()
        else:
            self.individuals = individuals
##generate a single note
#def generateNote():
#    # C4 = middle C
#    global notes
#    random.seed()
#    rand = random.randint(0,6)
#    note = notes[rand]
#    return note
#
##generate single pitch
#def generatePitch():
#    random.seed()
#    return str(random.randint(3,5))
#
##generate a 16 note long random piece of music
#def generatePiece():
#    piece = []
#    for i in range(0,16):
#        fullNote = generateNote() + generatePitch()
#        piece.append(fullNote)
#
#    return piece
#
##generate a population of 8 pieces
#def init():
#    clear()
#    for i in range(0, 16):
#        gen.append(generatePiece())
#        genScore.append(0)
#    scoreGen()
#
#def step():
#    global genAge
#    genAge += 1
#    selection()
#
#def scoreGen():
#    for i in range(0,len(gen)):
#        piece = gen[i]
#        genScore[i] = score(piece)
#
#def score(piece):
#    score = 0
#    mj = 0
#    pt = 0
#    for i in range(0, len(piece) - 1):
#        current = piece[i][:-1]
#        next = piece[i+1][:-1]
#
#        #print "C:", current, " N:", next
#
#        if current and next in major:
#            mj += 1
#        if current and next in pent:
#            pt += 1
#
#    #print mj, ":", pt
#    score = abs(mj - pt)
#    return score
#
##returns the relative distance between two notes
#def getDistance(n1, n2):
#    i1 = notes.index(n1)
#    i2 = notes.index(n2)
#    if i1 < i2:
#        return i2 - i1
#    elif i1 == i2:
#        return 0
#    else:
#        de = (len(notes) - 1) - i1
#        ds = i2 + 1
#        return de + ds
#
#def get():
#    return gen
#
#def getScores():
#    return genScore
#
#def getAge():
#    return genAge
#
##clear the generation
