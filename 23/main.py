# Advent of Code 2022 day 23
import numpy as np
from scipy import ndimage

filter = [[[1, 1, 1], [1, 0, 1], [1, 1, 1]],
          [[1, 1, 1], [0, 0, 0], [0, 0, 0]], \
          [[0, 0, 0], [0, 0, 0], [1, 1, 1]], \
          [[1, 0, 0], [1, 0, 0], [1, 0, 0]], \
          [[0, 0, 1], [0, 0, 1], [0, 0, 1]]]

# emptry rows and columsn that extend beyond the input
# may need to adjust this based on input
extends = 55


def run(directions):
    d = []
    for dir in directions:
        if dir == 'n':
            d.append(ndimage.generic_filter(g, np.sum, footprint=filter[1], mode='constant'))
        if dir == 's':
            d.append(ndimage.generic_filter(g, np.sum, footprint=filter[2], mode='constant'))
        if dir == 'w':
            d.append(ndimage.generic_filter(g, np.sum, footprint=filter[3], mode='constant'))
        if dir == 'e':
            d.append(ndimage.generic_filter(g, np.sum, footprint=filter[4], mode='constant'))
        # only choose first
        for j in range(len(d) - 2, -1, -1):
            d[-1][d[j] == 0] = 1

    # remove complete
    done = ndimage.generic_filter(g, np.sum, footprint=filter[0], mode='constant') == 0
    c = done & (g == 1)
    g[c] = 0

    dx = []
    for i, dir in enumerate(directions):
        if dir == 'n':
            dx.append(np.roll((d[i] == 0) & g, shift=-1, axis=0))
        if dir == 's':
            dx.append(np.roll((d[i] == 0) & g, shift=1, axis=0))
        if dir == 'w':
            dx.append(np.roll((d[i] == 0) & g, shift=-1, axis=1))
        if dir == 'e':
            dx.append(np.roll((d[i] == 0) & g, shift=1, axis=1))

    move = dx[0] + dx[1] + dx[2] + dx[3]

    # these will not move
    n_move = (g==1)
    for i in range(1, 5):
        n_move &= ndimage.generic_filter(g, np.sum, footprint=filter[i], mode='constant') > 0

    # fix bad moves
    for iy in range(len(move)):
        for ix in range(len(move[0])):
            if move[iy, ix] > 1:
                #print('fix:', iy, ix)
                move[iy, ix] = 0
                if g[iy - 1, ix] & (d[directions.index('s')][iy - 1, ix] == 0):
                    move[iy - 1, ix] = 1
                if g[iy + 1, ix] & (d[directions.index('n')][iy + 1, ix] == 0):
                    move[iy + 1, ix] = 1
                if g[iy, ix - 1] & (d[directions.index('e')][iy, ix - 1] == 0):
                    move[iy, ix - 1] = 1
                if g[iy, ix + 1] & (d[directions.index('w')][iy, ix + 1] == 0):
                    move[iy, ix + 1] = 1

    move[c] = 1
    return move + n_move


if __name__ == '__main__':
    g = []
    with open('input.txt') as f:
        for line in f:
            g.append([0 if l == '.' else 1 for l in line.strip()])
    g = np.array(g)

    # extend the boundary
    g = np.insert(g, 0, np.zeros(shape=(extends, g.shape[0])), axis=1)
    g = np.insert(g, g.shape[1], np.zeros(shape=(extends, g.shape[0])), axis=1)
    g = np.insert(g, 0, np.zeros(shape=(extends, g.shape[1])), axis=0)
    g = np.insert(g, g.shape[0], np.zeros(shape=(extends, g.shape[1])), axis=0)

    dirs = ['n', 's', 'w', 'e']
    for _ in range(10):
        g = run(dirs)
        dirs = dirs[1:] + dirs[:1]

    min_x, min_y, max_x, max_y = 0, 0, len(g[0]) - 1, len(g) - 1
    while np.sum(g, axis=0)[min_x] == 0:
        min_x += 1
    while np.sum(g, axis=0)[max_x] == 0:
        max_x -= 1
    while np.sum(g[min_y]) == 0:
        min_y += 1
    while np.sum(g[max_y]) == 0:
        max_y -= 1

    print('1:', np.sum(np.logical_not(g[min_y:max_y + 1, min_x: max_x + 1])))

    gp = np.array(g)
    for i in range(100_000):
        g = run(dirs)
        dirs = dirs[1:] + dirs[:1]
        if np.all(gp == g):
            break
        gp = np.array(g)

    print('2:', i+11)
