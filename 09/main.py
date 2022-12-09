# Advent of Code 2022 day 9
import numpy as np

if __name__ == '__main__':
    direction = {'L': [-1, 0], 'D': [0, 1], 'R': [1, 0], 'U': [0, -1]}
    num_knots = 10
    one = set()
    two = set()
    with open('input.txt') as f:
        k = np.zeros((num_knots, 2))
        # track the tail locations
        one.add(tuple(k[1]))
        two.add(tuple(k[num_knots - 1]))
        for line in f:
            d, l = line.strip().split(' ')
            for _ in range(int(l)):
                k[0] += direction[d]                    # move head
                for i in range(1, num_knots):           # move tail
                    diff = k[i-1] - k[i]
                    if np.max(np.abs(diff) // 2) >= 1:  # do we move
                        k[i] += np.clip(diff, -1, 1)
                        one.add(tuple(k[1]))
                        two.add(tuple(k[num_knots - 1]))

    print('1:', len(one))
    print('2:', len(two))


