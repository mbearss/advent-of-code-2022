# Advent of Code 2022 day 10
import numpy as np


if __name__ == '__main__':
    q = [1, 0]      # instruction queue
    with open('input.txt') as f:
        for line in f:
            token = line.strip().split(' ')
            j = token[0]
            if j == 'noop':
                q.append(0)
            elif j == 'addx':
                op = int(token[1])
                q.extend((op, 0))       # takes two steps to execute
    q = np.array(q)
    x = np.add.accumulate(q, 0)

    print('1:', sum([(i + 1) * x[i] for i in range(19, 220, 40)]))

    print('2:')
    for i in range(0, 240, 40):
        for j in range(0, 40):
            # I found it easier to read with space instead of .
            print('#' if (x[i + j] - 1) <= j <= (x[i + j] + 1) else ' ', end='')
        print()



