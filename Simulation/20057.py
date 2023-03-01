import sys
import math
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

tornado = [
    [(-2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01),
     (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02)],
    [(0, -2, 0.02), (1, -1, 0.1), (0, -1, 0.07), (-1, -1, 0.01),
     (1, 1, 0.1), (0, 1, 0.07), (-1, 1, 0.01), (0, 2, 0.02)],
    [(-2, 0, 0.02), (-1, -1, 0.01), (-1, 0, 0.07), (-1, 1, 0.1),
     (1, -1, 0.01), (1, 0, 0.07), (1, 1, 0.1), (2, 0, 0.02)],
    [(0, -2, 0.02), (1, -1, 0.01), (0, -1, 0.07), (-1, -1, 0.1),
     (1, 1, 0.01), (0, 1, 0.07), (-1, 1, 0.1), (0, 2, 0.02)]
]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


def decide_direction_and_move(x, y, direction):
    # (x, y)는 y의 좌표

    total_move = 0
    for move_x, move_y, percent in tornado[direction]:
        nx, ny = x+move_x, y+move_y
        move_amount = math.floor(matrix[x][y]*percent)
        print("x", x, "y", y, "percent", percent, "moveAmount", move_amount)
        if check_range(nx, ny):
            total_move += move_amount
            print("nx", nx, "ny", ny,
                  "matrix[nx][ny]", matrix[nx][ny], "moveAmount", move_amount)
            matrix[nx][ny] += move_amount

    nx, ny = x+(dx[direction]*2), y+(dy[direction]*2)
    move_amount = math.floor(matrix[x][y]*0.05)
    if check_range(nx, ny):
        print("nx", nx, "ny", ny,
              "matrix[nx][ny]", matrix[nx][ny], "moveAmount", move_amount)
        total_move += move_amount
        matrix[nx][ny] += move_amount

    nx, ny = x+dx[direction], y+dy[direction]
    if check_range(nx, ny):
        matrix[nx][ny] += matrix[x][y]-total_move
    matrix[x][y] = 0


x, y = n//2, n//2
dist = 1
count = 1
direction = 0
while not (x == 0 and y == -1):
    for _ in range(dist):
        x, y = x+dx[direction], y+dy[direction]
        print("====>", x, y, direction)
        decide_direction_and_move(x, y, direction)
        for m in matrix:
            print(*m)

    direction = (direction+1) % 4
    if count == 2:
        dist += 1
        count = 1
    else:
        count += 1
