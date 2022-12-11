# Advent of Code 2022 day 11
import math

monkey = []
inspect_count = []
modulo = 1


class Monkey:
    def __init__(self, index, items: list):
        self.index = index          # tracker for inspection count
        self.items = items
        self.t1, self.t2 = -1, -1   # target monkey

    def opp(self, i) -> int:
        return i

    def test(self, i) -> bool:
        return False

    def step(self, reduction):
        for i, e in enumerate(self.items):
            inspect_count[self.index] += 1
            self.items[i] = e = (self.opp(e) // reduction) % modulo
            monkey[self.t1 if self.test(e) else self.t2].items.append(e)
        self.items.clear()


if __name__ == '__main__':
    with open('input.txt') as f:
        for line in f:
            items = f.readline().strip().replace(',', '').split()[2:]
            monkey.append(Monkey(len(monkey), [int(i) for i in items]))
            inspect_count.append(0)

            opp = f.readline().strip().split()[4:]
            if opp[0] == '+':
                monkey[-1].opp = lambda x, y=opp[1]: x + (x if y == 'old' else int(y))
            elif opp[0] == '*':
                monkey[-1].opp = lambda x, y=opp[1]: x * (x if y == 'old' else int(y))

            test = f.readline().strip().split()[3]
            modulo *= int(test)
            monkey[-1].test = lambda x, y=int(test): x % y == 0

            monkey[-1].t1 = int(f.readline().strip().split()[-1])
            monkey[-1].t2 = int(f.readline().strip().split()[-1])

            f.readline()

    # save items
    org_items = []
    for m in monkey:
        org_items.append(tuple(m.items))

    for _ in range(20):
        for m in monkey:
            m.step(reduction=3)

    print('1:', math.prod(sorted(inspect_count)[-2:]))

    # restore original items
    for i, m in enumerate(monkey):
        m.items = [i for i in org_items[i]]
    inspect_count = [0] * len(monkey)

    for _ in range(10_000):
        for m in monkey:
            m.step(reduction=1)

    print('2:', math.prod(sorted(inspect_count)[-2:]))
