# Advent of Code 2022 day 18
import numpy as np


def part1(g, cube):
    s = 0
    for c in cube:
        if g[c[0] - 1, c[1], c[2]]:
            s += 1
        if g[c[0] + 1, c[1], c[2]]:
            s += 1
        if g[c[0], c[1] - 1, c[2]]:
            s += 1
        if g[c[0], c[1] + 1, c[2]]:
            s += 1
        if g[c[0], c[1], c[2] - 1]:
            s += 1
        if g[c[0], c[1], c[2] + 1]:
            s += 1
    return len(cube) * 6 - s

def part2(g, cube):
    ext = [(0, 0, 0)]
    seen = set()
    edge = 0
    while ext:
        e = ext.pop()
        if e in seen:
            continue

        sides = [(e[0] - 1, e[1], e[2]),
                 (e[0] + 1, e[1], e[2]),
                 (e[0], e[1] - 1, e[2]),
                 (e[0], e[1] + 1, e[2]),
                 (e[0], e[1], e[2] - 1),
                 (e[0], e[1], e[2] + 1)]
        for s in sides:
            if all([-1 <= x < size for x in s]):
                if g[s] == 0:
                    ext.append(s)
                if g[s] == 1:
                    edge += 1   # external edge
        seen.add(e)

    return edge


if __name__ == '__main__':
    size = 26
    g = np.zeros(shape=(size, size, size), dtype=int)
    cube = []
    with open('input.txt') as f:
        for line in f:
            x, y, z = map(int, line.strip().split(','))
            g[x, y, z] = 1
            cube.append((x, y, z))

    print('1:', part1(g, cube))

    print('2:', part2(g, cube))
