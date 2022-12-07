# Advent of Code 2022 day 6


if __name__ == '__main__':
    with open('input.txt') as f:
        # allow multiple cases
        for line in f:
            size = [4, 14]
            for k, s in enumerate(size):
                for i in range(len(line)):
                    if len(set(line[i:i+s])) == s:
                        print(str(k) + ':', i + s)
                        break

