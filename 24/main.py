# Advent of Code 2022 day 24

dirs = ['^', '>', 'v', '<']
move = [(-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)]

def add_tuple(x, y):
    if len(x) == 2:
        return x[0] + y[0], x[1] + y[1]
    return tuple(map(sum, zip(x, y)))

def simulate(blizzard):
    bp = []
    for b in blizzard:
        p, m = b[0], move[b[1]]
        np = add_tuple(p, m)
        if np[0] == 0:
            np = (extents[0] - 2, np[1])
        elif np[0] == extents[0] - 1:
            np = (1, np[1])
        elif np[1] == 0:
            np = (np[0], extents[1] - 2)
        elif np[1] == extents[1] - 1:
            np = (np[0], 1)
        bp.append((np, b[1]))
    return bp

if __name__ == '__main__':
    blizzard = []
    with open('input.txt') as f:
        for h, line in enumerate(f):
            for i, l in enumerate(line):
                if h == 0 and l == '.':
                    source = (h, i)
                for j, d in enumerate(dirs):
                    if d == l:
                        blizzard.append(((h, i), j))

    target = (h, line.index('.'))
    extents = [h + 1, i + 1]

    possible = set([source])
    s = 0
    phase = 0
    while True:
        blizzard = simulate(blizzard)
        bpos = set([b[0] for b in blizzard])
        np = []
        for p in possible:
            for m in move:
                pm = add_tuple(p, m)
                if pm == source or pm == target:
                    np.append(pm)
                if 0 < pm[0] < (extents[0] - 1) and 0 < pm[1] < (extents[1] - 1):
                    if pm not in bpos:
                        np.append(pm)
        possible = set(np)
        s += 1
        if phase == 0 and target in possible:
            part1 = s
            possible = set([target])
            phase += 1
        elif phase == 1 and source in possible:
            possible = set([source])
            phase += 1
        elif phase == 2 and target in possible:
            break

    print('1:', part1)
    print('2:', s)
