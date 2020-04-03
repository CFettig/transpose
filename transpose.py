all_chords = dict({'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
          'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11})

def get_key(search_num, minor):
    for chord, num in all_chords.items():
        if num == search_num:
            if minor:
                res = chord + 'm'
            else:
                res = chord
            return res

def transpose_up(chords):
    res = []
    for chord in chords:
        minor = ('m' in chord) or ('M' in chord)
        if minor:
            chord = chord[:-1]
            chord = (all_chords[chord] + 1)%12
        else:
            chord = (all_chords[chord] + 1)%12
        res.append(get_key(chord, minor))
    return res

def transpose_down(chords):
    res = []
    for chord in chords:
        minor = ('m' in chord) or ('M' in chord)
        if minor:
            chord = chord[:-1]
            chord = (all_chords[chord] - 1)%12
        else:
            chord = (all_chords[chord] - 1)%12
        res.append(get_key(chord, minor))
    return res

def display(chords, i):
    i = str(i)
    print(i + ' ' + ' '.join([str(elem) for elem in chords]))
        
def get_transposin(og_chords):
    i = 0
    c = input("u for up, d for down:")
    while (c != 'x'):
        if c == 'u':
            i = (i + 1) % 8
            og_chords = transpose_up(og_chords)
            display(og_chords, i)
        elif c == 'd':
            i = (i - 1) % 8
            og_chords = transpose_down(og_chords)
            display(og_chords, i)
        else:
            print("\nNope")
        c = input()

def check_chords(chords):
    res = True
    for chord in chords:
        if not (chord in all_chords):
            res = False
    return res

if __name__ == "__main__":
    usr_in = input("Enter chords: ")
    usr_in = usr_in.upper()
    chords = usr_in.split()

    if (check_chords(chords)):
        get_transposin(chords)
    else:
        print("I can't do those chords")

    