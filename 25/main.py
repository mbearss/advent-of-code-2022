# Advent of Code 2022 day 25

chars = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}


def snaf_to_dec(x):
    s = 0
    m = 1
    for c in reversed(x):
        s += chars[c] * m
        m *= 5
    return s


def dec_to_snaf(x):
    if x == 0:
        return ''
    a, b = divmod(x + 2, 5)
    return dec_to_snaf(a) + '=-012'[b]


if __name__ == '__main__':
    total = 0
    with open('input.txt') as f:
        for line in f:
            total += snaf_to_dec(line.strip())

    print('1:', dec_to_snaf(total))