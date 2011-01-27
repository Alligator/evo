import random
import utils

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
gen = []
genScore = []
genAge = 0;

#generate a single note
def generateNote():
    # C4 = middle C
    global notes
    random.seed()
    rand = random.randint(0,6)
    note = notes[rand]
    return note

#generate single pitch
def generatePitch():
    random.seed()
    return str(random.randint(3,5))

#generate a 16 note long random piece of music
def generatePiece():
    piece = []
    for i in range(0,16):
        fullNote = generateNote() + generatePitch()
        piece.append(fullNote)

    return piece

#generate a population of 8 pieces
def init():
    clear()
    for i in range(0, 8):
        gen.append(generatePiece())
        genScore.append(0)

def step():


def get():
    return gen

def getScores():
    return genScore

def getAge():
    return genAge

#clear the generation
def clear():
    del gen[:]
    del genScore[:]
