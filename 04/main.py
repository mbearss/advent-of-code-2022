# Advent of Code 2022 day 4


if __name__ == '__main__':
    subset, overlap = 0, 0
    with open('input.txt') as f:
        for line in f:
            s1, s2 = [e.split('-') for e in line.strip().split(',')]
            s1, s2 = [int(v) for v in s1], [int(v) for v in s2]

            if s1[0] >= s2[0] and s1[1] <= s2[1]:
                subset += 1
            elif s2[0] >= s1[0] and s2[1] <= s1[1]:
                subset += 1
            if s2[0] <= s1[0] <= s2[1] or s2[0] <= s1[1] <= s2[1]:
                overlap += 1
            elif s1[0] <= s2[0] <= s1[1] or s1[0] <= s2[1] <= s1[1]:
                overlap += 1
                
    print('1:', subset)
    print('2:', overlap)