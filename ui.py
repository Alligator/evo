import urwid
import generation
import utils

palette = [
        ('main', 'light gray', 'black'),
        ('title', 'white', 'black', 'bold'),
        ('key', 'light cyan', 'black', 'bold'),
        ('controls', 'light gray', 'black')
        ]

text_controls = [
        ('key', ' J'), ('controls', ' - Next Generation\n'),
        ('key', ' R'), ('controls', ' - Start Over\n'),
        '\n',
        ('key', ' M'), ('controls', ' - MIDI Output\n'),
        ('key', ' E'), ('controls', ' - DNA Export\n'),
        '\n',
        ('key', ' Q'), ('controls', ' - Quit')
        ]

midifocus = False
dnafocus = False
generation.init()
currentGen = utils.prettyPrint(generation.get(), generation.getScores())
prevGen = ""

def updateHeaders():
    current = generation.getAge()
    if current == 0:
        prev = 0
    else:
        prev = current-1
    leftheader.set_text([('title', 'Current Generation'), ('title', ' (' + str(current) + ')')])
    leftheader2.set_text([('title', 'Previous Generation'), ('title', ' (' + str(prev) + ')')])

content = [urwid.Text(currentGen)]
leftheader = urwid.Text('')
leftc = urwid.ListBox(content)
edit = urwid.Edit()
leftframe = urwid.Frame(leftc, header=leftheader, footer=edit)

content2 = [urwid.Text('The other stuff')]
leftheader2 = urwid.Text('')
leftc2 = urwid.ListBox(content2)
leftframe2 = urwid.Frame(leftc2, header=leftheader2)

controls = [urwid.Text(text_controls)]
rightc = urwid.ListBox(controls)
coloured = urwid.AttrMap(rightc, 'controls')

vlines = urwid.SolidFill(fill_char='|')
hlines = urwid.SolidFill(fill_char='-')

pile = urwid.Pile([ ('weight', 2, leftframe), ('fixed', 1, hlines), ('weight', 2, leftframe2) ])

body = urwid.Columns([ ('weight', 4, pile), ('fixed', 1, vlines), ('fixed', 21, coloured) ])

updateHeaders()

def update_on_cr(input):
    global midifocus
    global dnafocus
    if input in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    if input in ('j', 'J'):
        generation.step()
        update()
        pass
    if input in ('r', 'R'):
        restart()
    if input in ('m', 'M'):
        #midi
        midifocus = True
        edit.set_caption('Enter the piece ID: ')
        leftframe.set_focus('footer')
    if input in ('e', 'E'):
        #dna
        dnafocus = True
        edit.set_caption('Enter the piece ID: ')
        leftframe.set_focus('footer')
    if input == 'enter':
        if midifocus:
            piece = edit.get_edit_text()
            try:
                utils.convertToMIDI(generation.get()[int(piece)])
                edit.set_caption('Success')
            except Exception as e:
                edit.set_caption('Invalid ID: ' + str(e))
            edit.set_edit_text('')
            leftframe.set_focus('body')
        if dnafocus:
            piece = edit.get_edit_text
            #utils.convertToMIDI(generation.get()[int(piece)])
            edit.set_caption('Success')
            edit.set_edit_text('')
            leftframe.set_focus('body')

def update():
    movetolower()
    currentGen = utils.prettyPrint(generation.get(), generation.getScores())
    content.append(urwid.Text(currentGen))
    updateHeaders()

def restart():
    generation.init()
    del content[:]
    del content2[:]
    update()

def movetolower():
    try:
        del content2[:]
        content2.append(content[0])
        del content[:]
    except IndexError:
        pass

loop = urwid.MainLoop(body, palette, unhandled_input=update_on_cr)
loop.run()
