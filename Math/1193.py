n = int(input())


def get_depth(num):
    max_value = 1
    depth = 1
    while True:
        if num <= max_value:
            return depth, max_value
        depth += 1
        max_value += depth


def get_rc(num):
    depth, max_value = get_depth(num)
    if depth % 2 == 0:
        col = 1
        row = depth
        while max_value != num:
            max_value -= 1
            col += 1
            row -= 1
    else:
        col = depth
        row = 1
        while max_value != num:
            max_value -= 1
            col -= 1
            row += 1
    return row, col


row, col = get_rc(n)
print(str(row)+"/"+str(col))
