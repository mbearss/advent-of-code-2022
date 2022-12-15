# Advent of Code 2022 day 15
import re

from z3 import z3


def int_parse(x):
    return int(re.sub('[^\-0-9]', '', x))


def z3_abs(x):
    return z3.If(x >= 0, x, -x)


if __name__ == '__main__':
    test_row = 2_000_000
    beacon_in_row = set()
    cover = []

    # Microsoft Z3 solver
    z = z3.Solver()
    x, y = z3.Int("x"), z3.Int("y")
    # Add constraints
    z.add(0 <= x);
    z.add(x <= 4000000)
    z.add(0 <= y);
    z.add(y <= 4000000)

    with open('input.txt') as f:
        for line in f:
            sx, sy = map(int_parse, [s.split('=')[1] for s in line.strip().split(' ')[2:4]])
            bx, by = map(int_parse, [s.split('=')[1] for s in line.strip().split(' ')[8:10]])
            d = abs(sx - bx) + abs(sy - by) - abs(sy - test_row)
            if d >= 0:
                cover.append((sx - d, sx + d))
            if by == test_row:
                beacon_in_row.add(bx)

            # part 2
            m = abs(sx - bx) + abs(sy - by)
            z.add(z3_abs(sx - x) + z3_abs(sy - y) > m)

    c = set.union(*[set(range(a, b + 1)) for a, b in cover])
    print('1:', len(c - beacon_in_row))

    assert z.check() == z3.sat
    model = z.model()
    print('2:', model[x].as_long() * 4000000 + model[y].as_long())
