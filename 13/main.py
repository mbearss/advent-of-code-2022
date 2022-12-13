# Advent of Code 2022 day 13
from functools import cmp_to_key


def compare_packet(x, y) -> int:
    if type(x) is list and type(y) is int:
        y = [y]
    elif type(y) is list and type(x) is int:
        x = [x]

    if type(x) is list  and len(x) > 0 and type(y) is list and len(y) > 0:
        for z in map(compare_packet, x, y):
            if z:
                return z
        return compare_packet(len(x), len(y))

    return -1 if x < y else 1 if x > y else 0


if __name__ == '__main__':
    packets = []
    with open('input.txt') as f:
        for line in f:
            if line != '\n':
                packets.append(eval(line.strip(), {'__builtins__': None}))

    correct = []
    for i in range(0, len(packets), 2):
        if compare_packet(packets[i + 1], packets[i]) == 1:
            correct.append((i + 2) // 2)  # account for 2 indexing

    print('1:', sum(correct))

    # append the divider packets
    packets.append([[2]])
    packets.append([[6]])

    x = sorted(packets, key=cmp_to_key(compare_packet))
    print('2:', (x.index([[2]]) + 1) * (x.index([[6]]) + 1))
