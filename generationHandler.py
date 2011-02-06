import generation
import utils
import sys

menu = """1 - Start a new generation
2 - Exit"""

gMenu = """1 - Step
2 - MIDI Output
3 - Export DNA
4 - Discard"""
def main():
    while True:
        print "\n", menu
        cmd = raw_input("> ")
        if cmd == '1':
            newGeneration()
        elif cmd == '2':
            sys.exit(0)
        else:
            print "oops"

def genMenu():
    while True:
        print "\n", gMenu
        cmd = raw_input("> ")
        if cmd == '1':
            pass
        elif cmd == '2':
            midi()
        elif cmd == '3':
            export()
        elif cmd == '4':
            return
        else:
            pass

def midi():
    piece = raw_input("Enter piece ID > ")
    utils.convertToMIDI(generation.get()[int(piece)])

def export():
    piece = raw_input("Enter piece ID > ")
    filename = raw_input("Enter a filename > ")
    utils.export(generation.get()[int(piece)], filename)
    print "File written"

def newGeneration():
    generation.init()
    print utils.prettyPrint(generation.get(), generation.getScores())
    genMenu()

def step():
    generation.step()

if __name__ == "__main__":
    main()
