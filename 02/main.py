# Advent of Code 2022 day 2

# lookup tables
l1 = {(1, 2): 0, (2, 3): 0, (3, 1): 0, (1, 3): 6, (2, 1): 6, (3, 2): 6}
l2 = {(1, 1): 3, (1, 2): 1, (1, 3): 2, (3, 1): 2, (3, 2): 3, (3, 3): 1}


def one(g):
    return g[0] + (3 if g[0] == g[1] else l1[me, opp])


def two(g):
    return (g[0] - 1) * 3 + (g[1] if g[0] == 2 else l2[me, opp])


if __name__ == '__main__':
    s1, s2 = 0, 0
    with open('input.txt') as f:
        for line in f:
            me, opp = ord(line[2]) - 87, ord(line[0]) - 64
            s1 += one((me, opp))
            s2 += two((me, opp))

    print('1:', s1)
    print('2:', s2)
