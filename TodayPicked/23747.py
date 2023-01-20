from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 1, 0, 0]  # U D L R
dy = [0, 0, -1, 1]


def check_ragne(x, y):
    if x >= 0 and y >= 0 and x < r and y < c:
        return True
    return False


def bfs(x, y):
    this_area = matrix[x][y]
    q = deque()
    matrix[x][y] = "."
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if check_ragne(nx, ny) and matrix[nx][ny] == this_area:
                matrix[nx][ny] = "."
                q.append((nx, ny))


now_x, now_y = map(int, input().split())
now_x -= 1
now_y -= 1
move = list(input().rstrip())

for m in move:
    if m == "W" and matrix[now_x][now_y] != ".":
        bfs(now_x, now_y)
    elif m == "U":
        now_x, now_y = now_x+dx[0], now_y+dy[0]
    elif m == "D":
        now_x, now_y = now_x+dx[1], now_y+dy[1]
    elif m == "L":
        now_x, now_y = now_x+dx[2], now_y+dy[2]
    elif m == "R":
        now_x, now_y = now_x+dx[3], now_y+dy[3]

for i in range(4):
    nx, ny = now_x+dx[i], now_y+dy[i]
    if check_ragne(nx, ny):
        matrix[nx][ny] = "."
matrix[now_x][now_y] = "."

for mat in matrix:
    for m in mat:
        if m == ".":
            print(".", end="")
        else:
            print("#", end="")
    print()
