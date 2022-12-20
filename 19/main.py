# Advent of Code 2022 day 19
import numpy as np
import re


def key(x):
    return tuple(x[0] + x[1]) + tuple(x[1])


def prune(x):
    return sorted({key(x): x for x in x}.values(), key=key)[-1000:]


def run(blueprint, d):
    next = [(np.array([0, 0, 0, 0]), np.array([0, 0, 0, 1]))]
    for d in range(d, 0, -1):
        next_p = list()
        for res, ro in next:
            for c, r in blueprint:
                if all(c <= res):
                    next_p.append((res + ro - c, ro + r))
        next = prune(next_p)
    return max(h[0] for h, _ in next)


if __name__ == '__main__':
    part1, part2 = 0, 1
    with open('input.txt') as f:
        for i, line in enumerate(f):
            c = np.array(list(map(int, re.findall(r'\d+', line)))[1:])
            bp = (np.array([0, 0, 0, c[0]]), np.array([0, 0, 0, 1])), \
                 (np.array([0, 0, 0, c[1]]), np.array([0, 0, 1, 0])), \
                 (np.array([0, 0, c[3], c[2]]), np.array([0, 1, 0, 0])), \
                 (np.array([0, c[5], 0, c[4]]), np.array([1, 0, 0, 0])), \
                 (np.array([0, 0, 0, 0]), np.array([0, 0, 0, 0]))

            part1 += run(bp, 24) * (i + 1)
            if i < 3:
                part2 *= run(bp, 32)

    print('1:', part1)
    print('2:', part2)
