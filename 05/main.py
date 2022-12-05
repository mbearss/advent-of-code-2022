# Advent of Code 2022 day 5


def one(path):
    rows = []
    with open(path) as f:
        # find out how many stacks there are before parsing
        for line in f:
            if line[1] == '1':
                n = int(line[-2])
                break
            else:
                rows.append(line[:-1])

        # build the stacks
        stacks = [[] for _ in range(n)]
        for r in rows:
            for i, s in enumerate(stacks):
                index = 1 + i * 4
                if len(r) > index and r[index] != ' ':
                    s.insert(0, r[index])

        f.readline()
        # move the crates
        for line in f:
            i, cf, ct = [int(line.split(' ')[i]) for i in [1, 3, 5]]
            for _ in range(i):
                stacks[ct - 1].extend(stacks[cf - 1].pop())

    print('1:', end='')
    for s in stacks:
        print(s[-1], end='')

def two(path):
    rows = []
    with open(path) as f:
        # find out how many stacks there are before parsing
        for line in f:
            if line[1] == '1':
                n = int(line[-2])
                break
            else:
                rows.append(line[:-1])

        # build the stacks
        stacks = [[] for _ in range(n)]
        for r in rows:
            for i, s in enumerate(stacks):
                index = 1 + i * 4
                if len(r) > index and r[index] != ' ':
                    s.insert(0, r[index])

        f.readline()
        # move the crates
        for line in f:
            i, cf, ct = [int(line.split(' ')[i]) for i in [1, 3, 5]]
            t = stacks[cf - 1][-i:]
            del stacks[cf - 1][-i:]
            stacks[ct - 1].extend(t)

    print('\n2:', end='')
    for s in stacks:
        print(s[-1], end='')

if __name__ == '__main__':
    filepath = 'input.txt'
    one(filepath)
    two(filepath)