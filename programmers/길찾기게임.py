import sys
sys.setrecursionlimit(10**6)

X, Y, IDX = 0, 1, 2


def solution(nodeinfo):
    nodeinfo = [nodeinfo[i]+[i+1] for i in range(len(nodeinfo))]
    sortedY = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    pre_order = []
    post_order = []
    pre(sortedY, pre_order)
    post(sortedY, post_order)
    return [pre_order, post_order]


def pre(sortedY, answer):
    global X, Y, IDX
    root = sortedY[0]

    left = []
    right = []

    for i in range(1, len(sortedY)):
        if sortedY[i][X] < root[X]:
            left.append(sortedY[i])
        else:
            right.append(sortedY[i])

    answer.append(root[IDX])

    if (len(left)) > 0:
        pre(left, answer)
    if (len(right)) > 0:
        pre(right, answer)
    return


def post(sortedY, answer):
    global X, Y, IDX
    root = sortedY[0]

    left = []
    right = []

    for i in range(1, len(sortedY)):
        if sortedY[i][X] < root[X]:
            left.append(sortedY[i])
        else:
            right.append(sortedY[i])

    if (len(left)) > 0:
        post(left, answer)
    if (len(right)) > 0:
        post(right, answer)
    answer.append(root[IDX])
    return


print(solution([[5, 3], [11, 5], [13, 3], [3, 5],
      [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
