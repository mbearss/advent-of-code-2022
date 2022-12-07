# Advent of Code 2022 day 7
import uuid

from anytree import Node, PostOrderIter


if __name__ == '__main__':
    root = Node("root", type='dir', id=uuid.uuid4())
    current = root
    mode = 'command'
    with open('input.txt') as f:
        for line in f:
            token = line.split()
            if token[0] == '$':
                mode = 'command'
            if mode == 'list':
                if token[0] == 'dir':
                    Node(token[1], type='dir', parent=current, id=uuid.uuid4())
                else:
                    Node(token[1], type='file', size=int(token[0]), parent=current, id=uuid.uuid4())

            if mode == 'command':
                if token[1] == 'cd':
                    if token[2] == '/':
                        current = root
                    elif token[2] == '..' and current.parent is not None:
                        current = current.parent
                    else:
                        for c in current.children:
                            if c.name == token[2]:
                                current = c
                                break
                elif token[1] == 'ls':
                    mode = 'list'

    size = {}
    for n in PostOrderIter(root):
        if n.type == 'file':
            size[n.id] = n.size
        else:
            dir_size = 0
            for c in n.children:
                dir_size += size[c.id]
            size[n.id] = dir_size

    size1 = 0
    for n in root.descendants:
        if n.type == 'dir':
            if size[n.id] <= 100_000:
                size1 += size[n.id]

    print('1:', size1)
    print('2:', min(s for s in size.values() if s >= size[root.id] - 40_000_000))

