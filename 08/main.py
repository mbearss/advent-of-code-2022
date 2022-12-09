# Advent of Code 2022 day 8
import numpy as np


if __name__ == '__main__':
    with open('input.txt') as f:
        g = []
        for line in f:
            g.append([int(x) for x in line.strip()])
    g = np.array(g)
    v = np.zeros(g.shape)
    # set edge trees
    v[0, :], v[-1, :] = 1, 1
    v[:, 0], v[:, -1] = 1, 1

    for r in range(1, g.shape[0]):
        mh = g[r, 0]
        for c in range(1, g.shape[1]):
            v[r, c] += g[r, c] > mh
            mh = max(mh, g[r, c])

        mh = g[r, -1]
        for c in range(g.shape[1] - 1, 0, -1):
            v[r, c] += g[r, c] > mh
            mh = max(mh, g[r, c])

    for c in range(1, g.shape[1]):
        mh = g[0, c]
        for r in range(1, g.shape[0]):
            v[r, c] += g[r, c] > mh
            mh = max(mh, g[r, c])

        mh = g[-1, c]
        for r in range(g.shape[0] - 1, 0, -1):
            v[r, c] += g[r, c] > mh
            mh = max(mh, g[r, c])

    print('1:', int(np.sum(np.clip(v, 0, 1))))

    score = np.ones(g.shape)
    for _ in range(4):
        for r in range(g.shape[0]):
            for c in range(g.shape[1]):
                lower = [t < g[r, c] for t in g[r, c + 1:]]
                score[r, c] *= next((i + 1 for i, t in enumerate(lower) if ~t), len(lower))
        g, score = np.rot90(g), np.rot90(score)

    print('2:', int(np.max(score)))