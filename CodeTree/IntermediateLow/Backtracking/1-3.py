from itertools import permutations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
boom = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            boom.append((i, j))


orders = []


def bt(array):
    if len(array) == len(boom):
        orders.append(array[:])
        return
    for i in [1, 2, 3]:
        array.append(i)
        bt(array)
        array.pop()


bt([])

boom1_x = [1, 2, -1, -2]
boom1_y = [0, 0, 0, 0]
boom2_x = [1, -1, 0, 0]
boom2_y = [0, 0, 1, -1]
boom3_x = [1, 1, -1, -1]
boom3_y = [1, -1, 1, -1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


def boom_1(x, y):
    res = []
    for i in range(4):
        nx = x+boom1_x[i]
        ny = y+boom1_y[i]
        if check_range(nx, ny) and arr[nx][ny] == 0:
            res.append((nx, ny))
    return res


def boom_2(x, y):
    res = []
    for i in range(4):
        nx = x+boom2_x[i]
        ny = y+boom2_y[i]
        if check_range(nx, ny) and arr[nx][ny] == 0:
            res.append((nx, ny))
    return res


def boom_3(x, y):
    res = []
    for i in range(4):
        nx = x+boom3_x[i]
        ny = y+boom3_y[i]
        if check_range(nx, ny) and arr[nx][ny] == 0:
            res.append((nx, ny))
    return res


for order in orders:
    result = set()
    for o, b in zip(order, boom):
        if o == 1:
            result.update(boom_1(b[0], b[1]))
        elif o == 2:
            result.update(boom_2(b[0], b[1]))
        elif o == 3:
            result.update(boom_3(b[0], b[1]))
    answer = max(answer, len(result))
print(answer+len(boom))
