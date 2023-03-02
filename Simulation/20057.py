import sys
import math
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

tornado = [
    [(-2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01),
     (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02), (0, -2, 0.05)],
    [(0, -2, 0.02), (1, -1, 0.1), (0, -1, 0.07), (-1, -1, 0.01),
     (1, 1, 0.1), (0, 1, 0.07), (-1, 1, 0.01), (0, 2, 0.02), (2, 0, 0.05)],
    [(-2, 0, 0.02), (-1, -1, 0.01), (-1, 0, 0.07), (-1, 1, 0.1),
     (1, -1, 0.01), (1, 0, 0.07), (1, 1, 0.1), (2, 0, 0.02), (0, 2, 0.05)],
    [(0, -2, 0.02), (1, -1, 0.01), (0, -1, 0.07), (-1, -1, 0.1),
     (1, 1, 0.01), (0, 1, 0.07), (-1, 1, 0.1), (0, 2, 0.02), (-2, 0, 0.05)]
]


def is_finish(x, y):
    if x == 0 and y == -1:
        return True
    return False


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


def decide_direction_and_move(x, y, direction):
    # (x, y)는 y의 좌표

    total_move = 0
    outer_move = 0
    for move_x, move_y, percent in tornado[direction]:
        nx, ny = x+move_x, y+move_y
        sand = math.floor(matrix[x][y]*percent)
        total_move += sand
        if check_range(nx, ny):
            matrix[nx][ny] += sand
        else:
            outer_move += sand

    # 알파 계산
    nx, ny = x+dx[direction], y+dy[direction]
    remain = matrix[x][y]-total_move
    if check_range(nx, ny):
        matrix[nx][ny] += remain
    else:
        outer_move += remain

    matrix[x][y] = 0
    return outer_move


x, y = n//2, n//2
dist = 1  # 같은 방향으로 움직이는 거리
direction = 0  # 방향
total_outer_move = 0  # 바깥으로 날아간 모래의 총합
while not is_finish(x, y):
    for _ in range(2):  # 같은 거리로 두 번씩 움직임
        for _ in range(dist):
            x, y = x+dx[direction], y+dy[direction]
            total_outer_move += decide_direction_and_move(x, y, direction)
        if is_finish(x, y):
            break
        direction = (direction+1) % 4
    dist += 1

print(total_outer_move)
