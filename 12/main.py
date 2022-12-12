# Advent of Code 2022 day 12
import numpy as np


def step(g, r):
    for iy, ix in np.ndindex(g.shape):
        if ix > 0 and g[iy, ix] <= g[iy, ix - 1] + 1:
            r[iy, ix] = min(r[iy, ix], r[iy, ix - 1] + 1)
        if ix < mx and g[iy, ix] <= g[iy, ix + 1] + 1:
            r[iy, ix] = min(r[iy, ix], r[iy, ix + 1] + 1)
        if iy > 0 and g[iy, ix] <= g[iy - 1, ix] + 1:
            r[iy, ix] = min(r[iy, ix], r[iy - 1, ix] + 1)
        if iy < my and g[iy, ix] <= g[iy + 1, ix] + 1:
            r[iy, ix] = min(r[iy, ix], r[iy + 1, ix] + 1)


if __name__ == '__main__':
    g = []
    sx, sy, ex, ey = 0, 0, 0, 0     # start/end index
    with open('input.txt') as f:
        for line in f:
            if 'S' in line:
                sx, sy = line.index('S'), len(g)
            if 'E' in line:
                ex, ey = line.index('E'), len(g)
            g.append([ord(l) - 97 for l in line.strip().replace('S', 'a').replace('E', 'z')])

    g = np.array(g)
    r = np.full(shape=g.shape, fill_value=10_000)
    r[sy, sx] = 0
    mx, my = g.shape[1] - 1, g.shape[0] - 1  # highest index
    # run until the exit is reachable
    while r[ey, ex] == 10_000:
        step(g, r)

    print('1:', r[ey, ex])

    r = np.full(shape=g.shape, fill_value=10_000)
    r[g == 0] = 0
    t1 = np.sum(r)
    # run until the paths stop changing
    while True:
        step(g, r)
        t2 = np.sum(r)
        if t2 == t1:
            break
        t1 = t2

    print('2:', r[ey, ex])