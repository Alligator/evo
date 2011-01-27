import random
from midiutil.MidiFile import MIDIFile

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
mapping = {'C' : 60, 'D' : 62, 'E' : 64, 'F' : 65, 'G' : 67, 'A' : 69, 'B' : 71}

def generateNote():
    # C4 = middle C
    global notes
    random.seed()
    rand = random.randint(0,6)
    note = notes[rand]
    return note

def generatePitch():
    random.seed()
    return str(random.randint(3,5))

def generatePiece():
    piece = []
    for i in range(0,16):
        fullNote = generateNote()# + generatePitch()
        piece.append(fullNote)

    return piece

def convertToMIDI(piece):
    mfile = MIDIFile(1)
    track = 0
    time = 0
    tempo = 120

    mfile.addTrackName(track, time, "test")
    mfile.addTempo(track, time, tempo)

    channel = 0
    volume = 100

    # Actual magic happens here
    i = 0
    while i < len(piece)-1:
        # Get the corresponding pitch for the note
        pitch = mapping[piece[i]]

        # If we're dealing with a continued note
        if piece[i] == piece[i+1]:
            n = i
            duration = 0
            
            # Keep increasing the duration by 2 for
            # every consecutive matching note
            while piece[n] == piece[n+1]:
                print n
                duration += 2
                if n+1 == len(piece):
                    break
                # Single note duration is 2
                n += 1
            mfile.addNote(track, channel, pitch, i*2, duration, volume)
            i = n

        # If we're dealing with a single note, add it
        else:
            mfile.addNote(track, channel, pitch, i*2, 2, volume)

            # If we're on the penultimate note,
            # add the last note too
            if i == len(piece) - 1:
                pitch = mapping[piece[i+1]]
                mfile.addNote(track, channel, pitch, i*2, 2, volume)
        i += 1

    bfile = open("output.mid", "wb")
    mfile.writeFile(bfile)
    bfile.close()

    print piece
