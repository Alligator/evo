import urwid

palette = [
        ('main', 'light gray', 'black'),
        ('title', 'white', 'black', 'bold'),
        ('key', 'light cyan', 'black', 'bold'),
        ('controls', 'light gray', 'black')
        ]

text_controls = [
        ('key', ' J'), ('controls', ' - Next Generation\n'),
        '\n',
        ('key', ' M'), ('controls', ' - MIDI Output\n'),
        ('key', ' E'), ('controls', ' - DNA Export\n'),
        '\n',
        ('key', ' Q'), ('controls', ' - Quit')
        ]

content = [urwid.Text('The content goes here')]
leftheader = urwid.Text(('title', 'Current Generation'))
leftc = urwid.ListBox(content)
leftframe = urwid.Frame(leftc, header=leftheader)

content2 = [urwid.Text('The other stuff')]
leftheader2 = urwid.Text(('title', 'Previous Generation'))
leftc2 = urwid.ListBox(content2)
leftframe2 = urwid.Frame(leftc2, header=leftheader2)

controls = [urwid.Text(text_controls)]
rightc = urwid.ListBox(controls)
coloured = urwid.AttrMap(rightc, 'controls')

vlines = urwid.SolidFill(fill_char='|')
hlines = urwid.SolidFill(fill_char='-')

pile = urwid.Pile([ ('weight', 2, leftframe), ('fixed', 1, hlines), ('weight', 2, leftframe2) ])

body = urwid.Columns([ ('weight', 4, pile), ('fixed', 1, vlines), ('fixed', 20, coloured) ])
#frame = urwid.Frame(urwid.AttrWrap(columns, 'body'))#, footer=footer)

def update_on_cr(input):
    if input in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    if input in ('j', 'J'):
        #content.append(urwid.Text('what up'))
        #raise urwid.ExitMainLoop()
        write('i know rite')

def clear():
    del content[:]

def write(msg):
    content.append(urwid.Text(msg))

loop = urwid.MainLoop(body, palette, unhandled_input=update_on_cr)
loop.run()
