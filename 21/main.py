# Advent of Code 2022 day 21
from anytree import Node, RenderTree


def parse(root):
    if root.is_leaf:
        return root.value
    else:
        c = [parse(c) for c in root.children]
    if root.opp == '+':
        return c[0] + c[1]
    elif root.opp == '-':
        return c[0] - c[1]
    elif root.opp == '*':
        return c[0] * c[1]
    elif root.opp == '/':
        return c[0] // c[1]


def rparse(root, need):
    if root.is_leaf:
        return need
    if nodes['humn'] in root.children[0].descendants or nodes['humn'] == root.children[0]:
        root, other = root.children[0], parse(root.children[1])
        if root.parent.opp == '/':
            need *= other
        elif root.parent.opp == '-':
            need += other
        elif root.parent.opp == '+':
            need -= other
        elif root.parent.opp == '*':
            need //= other
        return rparse(root, need)
    else:
        root, other = root.children[1], parse(root.children[0])
        if root.parent.opp == '/':
            need = other / need
        elif root.parent.opp == '-':
            need = other - need
        elif root.parent.opp == '+':
            need -= other
        elif root.parent.opp == '*':
            need //= other
        return rparse(root, need)


if __name__ == '__main__':
    data = []
    with open('input.txt') as f:
        for line in f:
            token = line.strip().split(' ')
            if len(token) == 2:
                data.append((token[0][:-1], int(token[1])))
            else:
                data.append((token[0][:-1], token[1], token[3], token[2]))

    nodes = {}
    for d in data:
        if len(d) == 2:
            nodes[d[0]] = Node(d[0], value=d[1])

    while 'root' not in nodes:
        for d in data:
            if len(d) > 2 and d[0] not in nodes:
                if d[1] in nodes and d[2] in nodes:
                    nodes[d[0]] = Node(d[0], opp=d[3], children=[nodes[d[1]], nodes[d[2]]])

    root = nodes['root']
    print('1:', parse(root))

    # we need our subtree to equal this
    if nodes['humn'] in root.children[0].descendants:
        need = parse(root.children[1])
        x = rparse(root.children[0], need)
    else:
        need = parse(root.children[0])
        x = rparse(root.children[1], need)

    print('2:', x)
