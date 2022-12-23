# Advent of Code 2022 day 22
import re
from dataclasses import dataclass


@dataclass()
class Node:
    up: 'Node'
    down: 'Node'
    left: 'Node'
    right: 'Node'
    xloc: int
    yloc: int
    type: int

    def __str__(self):
        return str(self.xloc + 1) + ', ' + str(self.yloc + 1)


if __name__ == '__main__':
    with open('input.txt') as f:
        y = 0
        g = []
        max_length = 0
        for line in f:
            if line.strip() == '':
                break
            max_length = max(max_length, len(line[:-1]))
            g.append([])
            x = 0
            for l in line[:-1]:
                if l == '.':
                    g[-1].append(Node(None, None, None, None, x, y, 1))
                elif l == '#':
                    g[-1].append(Node(None, None, None, None, x, y, 0))
                else:
                    g[-1].append(Node(None, None, None, None, x, y, -1))
                x += 1
            y += 1

        instructions = f.readline()

    # fix missing columns
    for r in g:
        while len(r) < max_length:
            r.append(Node(None, None, None, None, x, y, -1))


    # build the grid links
    for y in range(len(g)):
        for x, n in enumerate(g[y]):
            cx = x
            while g[y][cx - 1].type == -1:    # while empty space
                cx -= 1
            if g[y][cx - 1].type == 1:
                n.left = g[y][cx - 1]

            cx = x
            while g[y][(cx + 1) % len(g[y])].type == -1:    # while empty space
                cx += 1
            if g[y][(cx + 1) % len(g[y])].type == 1:
                n.right = g[y][(cx + 1) % len(g[y])]

            cy = y
            while g[cy - 1][x].type == -1:  # while empty space
                cy -= 1
            if g[cy - 1][x].type == 1:
                n.up = g[cy - 1][x]

            cy = y
            while g[(cy + 1) % len(g)][x].type == -1:  # while empty space
                cy += 1
            if g[(cy + 1) % len(g)][x].type == 1:
                n.down = g[(cy + 1) % len(g)][x]

    current = g[0][0]
    while current.type == -1:
        current = current.right

    dir = ['r', 'd', 'l', 'u']
    di = 0
    for i in re.split(r'(\d+[RL])', instructions):
        if i == '':
            continue
        f, t = int(re.findall(r'\d+',i)[0]), i[-1]
        if dir[di] == 'r':
            for _ in range(f):
                if current.right is not None and current.right.type == 1:
                    current = current.right
                else:
                    break
        if dir[di] == 'l':
            for _ in range(f):
                if current.left is not None and current.left.type == 1:
                    current = current.left
                else:
                    break
        if dir[di] == 'u':
            for _ in range(f):
                if current.up is not None and current.up.type == 1:
                    current = current.up
                else:
                    break
        if dir[di] == 'd':
            for _ in range(f):
                if current.down is not None and current.down.type == 1:
                    current = current.down
                else:
                    break
        di = (di + (1 if t == 'R' else -1 if t == 'L' else 0)) % 4

    print('1:', 1000 * (current.yloc + 1) + 4 * (current.xloc + 1) + di)