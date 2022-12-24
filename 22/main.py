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
        return str(self.yloc) + ', ' + str(self.xloc)

def wrap(pos, dir):
    x, y = pos.real, pos.imag
    match dir, x // side_length, y // side_length:
        case 1j, 0, _:
            return complex((side_length * 3 - 1) - x, (side_length * 2 - 1)), -1j
        case 1j, 1, _:
            return complex((side_length - 1), x + side_length), -1
        case 1j, 2, _:
            return complex((side_length * 3 - 1) - x, (side_length * 3 - 1)), -1j
        case 1j, 3, _:
            return complex((side_length * 3 - 1), x - (side_length * 2)), -1
        case -1j, 0, _:
            return complex((side_length * 3 - 1) - x, 0), 1j
        case -1j, 1, _:
            return complex((side_length * 2), x - side_length), 1
        case -1j, 2, _:
            return complex((side_length * 3 - 1) - x, side_length), 1j
        case -1j, 3, _:
            return complex(0, x - (side_length * 2)), 1
        case 1, _, 0:
            return complex(0, y + (side_length * 2)), 1
        case 1, _, 1:
            return complex((side_length * 2) + y, (side_length - 1)), -1j
        case 1, _, 2:
            return complex(-side_length + y, (side_length * 2 - 1)), -1j
        case -1, _, 0:
            return complex(side_length + y, side_length), 1j
        case -1, _, 1:
            return complex((side_length * 2) + y, 0), 1j
        case -1, _, 2:
            return complex((side_length * 4 - 1), y - (side_length * 2)), -1


if __name__ == '__main__':
    grid = []
    with open('input.txt') as f:
        y = 0
        g = []
        max_length = 0
        for line in f:
            if line.strip() == '':
                break
            grid.append(line)
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

    # gave up on the linked list interpretation because the cube was melting my brain
    # had some help from reddit with complex numbers
    side_length = 50

    pos, dir = grid[0].index('.') * 1j, 1j
    grid = {(x + y * 1j): c for x, l in enumerate(grid)
            for y, c in enumerate(l) if c in '.#'}

    for i in re.split(r'(\d+[RL])', instructions):
        if i == '':
            continue
        f, t = int(re.findall(r'\d+', i)[0]), i[-1]
        for _ in range(int(f)):
            p, d = pos + dir, dir
            if p not in grid: p, d = wrap(p, d)
            if grid[p] == '.':
                pos, dir = p, d

        if t == 'L':
            dir *= +1j
        elif t == 'R':
            dir *= -1j

    print('2:', int(1000 * (pos.real + 1) + 4 * (pos.imag + 1) + [1j, 1, -1j, -1].index(dir)))