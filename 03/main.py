# Advent of Code 2022 day 3

def get_priority(l):
    return ord(l) - (96 if l.islower() else 38)


def one(path):
    sum = 0
    with open(path) as f:
        for line in f:
            # break sack into two sets
            x = set(line[:len(line) // 2])
            y = set(line[len(line) // 2:])
            p = x.intersection(y).pop()
            sum += get_priority(p)
    print(sum)


def two(path):
    rs = []
    with open(path) as f:
        for line in f:
            rs.append(set(line.strip()))

    sum = 0
    # iterate three sacks at a time
    for x, y, z in zip(*[iter(rs)] * 3):
        p = x.intersection(y, z).pop()
        sum += get_priority(p)
    print(sum)


if __name__ == '__main__':
    path = 'input.txt'
    one(path)
    two(path)
