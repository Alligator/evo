from midiutil.MidiFile import MIDIFile

mapping = { 'C' : 60,
            'C#': 61,
            'D' : 62,
            'D#': 63,
            'E' : 64,
            'F' : 65,
            'F#': 66,
            'G' : 67,
            'G#': 68,
            'A' : 69,
            'A#': 70,
            'B' : 71}

def convertToMIDI(piece):
    mfile = MIDIFile(1)
    track = 0
    time = 0
    tempo = 160

    mfile.addTrackName(track, time, "test")
    mfile.addTempo(track, time, tempo)

    channel = 0
    volume = 100

    # Actual magic happens here
    i = 0
    while i < len(piece)-1:
        # Get the corresponding pitch for the note
        pitch = mapping[piece[i][0]]
        diff = int(piece[i][-1]) - 4
        pitch += diff * 12

        # If we're dealing with a continued note
        if piece[i] == piece[i+1]:
            n = i
            duration = 0
            
            # Keep increasing the duration by 2 for
            # every consecutive matching note
            while piece[n] == piece[n+1]:
                #print n
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

def prettyPrint(generation, scores):
    out = ''
    for i in range(0, len(generation)):
        genstr = ''
        for j in range(0, len(generation[i])):
            genstr += generation[i][j][0]
            genstr += generation[i][j][1:].rjust(2) + '  '
            #if len(generation[i][j]) == 2:
            #    genstr += "  "
            #else:
            #    genstr += " "
        out += str(i).rjust(2) + ' | ' + genstr[:-1] + '| ' + str(scores[i]) + '\n'
    return out

def export(piece, filename):
    output = ""
    f = open(filename + ".dna", 'w')
    for i in range(0, len(piece)):
        output += piece[i] + ":"
    f.write(output[:-1])
    f.close()
