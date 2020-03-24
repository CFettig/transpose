import curses

all_chords = dict({'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
          'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11})

screen = curses.initscr()

def get_key(search_num):
    for chord, num in all_chords.items():
        if num == search_num:
            return chord

def transpose_up(chords):
    res = []
    for chord in chords:
        chord = (all_chords[chord] + 1)%12
        res.append(get_key(chord))
    return res

def transpose_down(chords):
    res = []
    for chord in chords:
        chord = (all_chords[chord] + 1)%12
        res.append(get_key(chord))
    return res

def get_og_chords():
    usr_in = []
    c = screen.getch()
    while (c != ord('x')):
        usr_in.append(c)
        c = screen.getch()
    return usr_in

def get_transposin(og_chords):
    screen.addstr("up arrow to transpose up, down arrow to transpose down\n")
    screen.refresh()
    c = screen.getkey()
    while (c != ord('x')):
        if c == curses.KEY_UP:
            transpose_up(og_chords)
            c = curses.getkey()
        elif c == curses.KEY_DOWN:
            transpose_down(og_chords)
            c = curses.getkey()
        else:
            screen.addstr("\nNope\n")
            screen.refresh()
            c = screen.getkey()

# curses.noecho()
screen.addstr("Give me some chords! Enter X when done: ")
screen.refresh()
og_chords = get_og_chords()
get_transposin(og_chords)
# chrods = ' '.join([str(chr(elem)) for elem in get_og_chords()])
# screen.addstr('\n' + chrods)
screen.refresh()
screen.getch()
curses.endwin()
# usr_in.append(screen.getch())

# curses.endwin()

    # usr_in = input("Enter chords: ")
    # usr_in = usr_in.upper()
    # chords = usr_in.split()

    # transpose_up(chords)

    # display(chords)

