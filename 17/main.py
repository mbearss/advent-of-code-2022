# Advent of Code 2022 day 17
import operator

import numpy as np

chars = {-1: '-', 0: '.', 1: '#', 2: '@'}
rock = [[(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
        [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (0, 1), (1, 0), (1, 1)]]
r_start = [0, 2, 2, 3, 1]

def run(num_rocks):
    r_idx, w = 0, 0
    g = np.zeros(shape=(1_000_000, 7))
    g[-1] = -1
    highest = g.shape[0]
    r_loc = np.array((highest - 5 - r_start[r_idx % 5], 2))
    block_height = []

    while r_idx < num_rocks:
        if wind[w % len(wind)] == '>':
            for r in rock[r_idx % 5]:
                y, x = r_loc + r
                if (r_loc + r)[1] >= g.shape[1] - 1 or g[y, x + 1] != 0:
                    break
            else:
                r_loc[1] += 1
        elif wind[w % len(wind)] == '<':
            for r in rock[r_idx % 5]:
                y, x = r_loc + r
                if (r_loc + r)[1] <= 0 or g[y, x - 1] != 0:
                    break
            else:
                r_loc[1] -= 1
        adv = False
        for r in rock[r_idx % 5]:
            y, x = r_loc + r
            if g[y + 1, x] != 0:
                adv = True
                break
        if adv:
            for r in rock[r_idx % 5]:
                y, x = r_loc + r
                g[y, x] = 1
                highest = min(highest, y)
            r_idx += 1
            r_loc = np.array((highest - 4 - r_start[r_idx % 5], 2))
            block_height.append(g.shape[0] - highest - 1)

        else:
            r_loc[0] += 1
        w += 1
    return g.shape[0] - highest - 1, block_height



if __name__ == '__main__':
    with open('input.txt') as f:
        wind = f.read().strip()

    height, block_height = run(2022)
    print('1:', height)

    # run a large batch and look for a cycle
    height, block_height = run(200_000)
    # compute interval distance between blocks
    x = list(map(operator.sub, block_height[1:], block_height[:-1]))
    for cl in range(2, 2000):
        success = True
        for i in range(10_000, 20_000):
            if x[i] != x[i + cl]:
                success = False
        if success:
            break

    # multiply the hight of a cycle by the number of cycles
    # assuming the cycles are established by block 10_000
    total = block_height[10_000 - 1]
    ch = sum(x[10_000:10_000 + cl])
    total += ch * ((1_000_000_000_000 - 10_000) // cl)
    # blocks after the last full cycle
    total += sum(x[10_000: 10_000 + (1_000_000_000_000 - 10_000) % cl])
    print('2:', total)



