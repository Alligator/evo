import generation
import utils
import sys

menu = """1 - Start a new generation
2 - Exit"""

gMenu = """1 - Step
2 - Score only
3 - Discard"""

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
            pass
        elif cmd == '3':
            return
        else:
            pass

def newGeneration():
    generation.init()
    utils.prettyPrint(generation)
    genMenu()

def step():
    generation.step()

if __name__ == "__main__":
    main()