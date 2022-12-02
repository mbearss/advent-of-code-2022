# Advent of Code 2022 day 1


if __name__ == '__main__':
    snacks = [[]]
    with open('input.txt') as f:
        for line in f:
            if line == '\n':
                snacks.append([])
            else:
                snacks[-1].append(int(line))
    totals = list(map(sum, snacks))

    print('1:', max(totals))

    print('2:', sum(sorted(totals)[-3:]))
