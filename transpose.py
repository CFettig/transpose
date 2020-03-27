all_chords = dict({'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
          'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11})

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
        chord = (all_chords[chord] - 1)%12
        res.append(get_key(chord))
    return res

def display(chords):
    print(' '.join([str(elem) for elem in chords]))
        
def get_transposin(og_chords):
    # res = [0, og_chords]
    c = input("u for up, d for down:")
    while (c != 'x'):
        if c == 'u':
            # print(c == 'u')
            # print("\n")
            og_chords = transpose_up(og_chords)
            display(og_chords)
        elif c == 'd':
            # print("\n")
            og_chords = transpose_down(og_chords)
            display(og_chords)
            # print(og_chords)
        else:
            print("\nNope")
        c = input()

if __name__ == "__main__":
    usr_in = input("Enter chords: ")
    usr_in = usr_in.upper()
    chords = usr_in.split()

    get_transposin(chords)