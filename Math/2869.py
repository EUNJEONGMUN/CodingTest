a, b, tree = map(int, input().split())

if (tree-b) % (a-b) > 0:
    print((tree-b)//(a-b)+1)
else:
    print((tree-b)//(a-b))
