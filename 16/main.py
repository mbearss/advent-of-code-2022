# Advent of Code 2022 day 16
import networkx as nx

flow = {}
start = 'AA'


def all_orders(sp, c, left, done, time):
    for l in left:
        if sp[c][l] + 1 < time:
            yield from all_orders(sp, l, left - {l},
                                  done + [l], time - (sp[c][l] + 1))
    yield done


def run(path, start, left, t):
    f = 0
    c = start
    for l in left:
        t -= path[c][l] + 1
        f += t * flow[l]
        c = l
    return f


if __name__ == '__main__':
    g = nx.Graph()
    with open('input.txt') as f:
        for line in f:
            token = line.strip().replace(',', '').split()
            flow[token[1]] = int(token[4].replace(';', '').split('=')[1])
            for p in token[9:]:
                g.add_edge(token[1], p)

    sp = nx.floyd_warshall(g)
    # only look at nodes with positive flow rates
    valves = {n for n in sp if flow[n] > 0}

    part1 = max(run(sp, start, order, 30) for order in
                     all_orders(sp, start, valves, [], 30))
    print("1:", int(part1))

    part2 = [(run(sp, start, order, 26), set(order))
                 for order in all_orders(sp, start, valves, [], 26)]
    part2.sort(key=lambda x: -x[0])

    max_f = 0
    for i, (f1, p1) in enumerate(part2):
        if f1 * 2 < max_f:
            break
        for f2, p2 in part2[i + 1:]:
            if not p1 & p2:
                score = f1 + f2
                if score > max_f:
                    max_f = score
    print("2:", int(max_f))
