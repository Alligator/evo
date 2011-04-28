# individual.py
# Represents the individual compositions in a population
import random

class Individual:
    def __init__(self, dna=[], fitness=0):
        # If dna is empty, generate a random dna
        if not dna:
            self.dna = self.generateDna()
        else:
            self.dna = dna

        self.fitness = fitness

    # generateDna()
    # Generate a random DNA sequence
    def generateDna(self):
        dna = []
        notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        for i in range(0, 32):
            random.seed()
            note = random.choice(notes)
            octave = random.randint(3, 5)
            dna.append(note + str(octave))
        return dna

