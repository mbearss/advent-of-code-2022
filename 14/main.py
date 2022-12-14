# Advent of Code 2022 day 14
import numpy as np


def sand() -> bool:
    if g[0, 500] != 0:
        return False        # source blocked
    s = [0, 500]
    while s[0] < 999 and 0 <= s[1] < 999:
        if g[s[0] + 1, s[1]] == 0:
            s[0] += 1
        elif g[s[0] + 1, s[1] - 1] == 0:
            s[0] += 1
            s[1] -= 1
        elif g[s[0] + 1, s[1] + 1] == 0:
            s[0] += 1
            s[1] += 1
        else:
            g[s[0], s[1]] = 1
            return True     # placed
    return False            # abyss

if __name__ == '__main__':
    g = np.zeros(shape=(1000, 1000))
    floor_y = 0
    with open('input.txt') as f:
        for line in f:
            r = line.strip().split('->')
            i = 0
            while i < len(r) - 1:
                x1, y1 = map(int, r[i].split(','))
                x2, y2 = map(int, r[i+1].split(','))
                # make sure they are in order
                if x2 < x1:
                    x1, x2 = x2, x1
                if y2 < y1:
                    y1, y2 = y2, y1
                floor_y = max(floor_y, y1, y2)
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        g[y, x] = 2
                i += 1

    c = 0
    while sand():
        c += 1
    print('1:', c)

    # reset sand
    g[g == 1] = 0

    g[floor_y + 2, :] = 2

    c = 0
    while sand():
        c += 1
    print('2:', c)
