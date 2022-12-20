# Advent of Code 2022 day 20

class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)


def init(vals):
    for a, b in zip(vals, vals[1:]):
        a.next = b
        b.prev = a

    vals[0].prev = vals[-1]
    vals[-1].next = vals[0]
    return vals


def run(vals):
    for o in vals:
        o.prev.next = o.next
        o.next.prev = o.prev
        a, b = o.prev, o.next
        m = o.value % (len(vals) - 1)
        for _ in range(m):
            a = a.next
            b = b.next
        a.next = o
        o.prev = a
        b.prev = o
        o.next = b
    return vals


def ans(vals):
    o = vals[0]
    nums = 0
    while o.value != 0:
        o = o.next
    for _ in range(3):
        for _ in range(1000):
            o = o.next
        nums += o.value
    return nums


if __name__ == '__main__':
    part1, part2 = [], []
    with open('input.txt') as f:
        for line in f:
            part1.append(Node(int(line.strip())))
            part2.append(Node(int(line.strip()) * 811589153))

    part1 = init(part1)
    part2 = init(part2)

    part1 = run(part1)
    print('1:', ans(part1))

    for _ in range(10):
        part2 = run(part2)
        o = part2[0]

    print('2:', ans(part2))
