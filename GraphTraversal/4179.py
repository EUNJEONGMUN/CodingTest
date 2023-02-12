from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
jihun_x, jihun_y = 0, 0
q = deque()
FIRE = -1
VISITED = "v"
NOT_VISITED = "."
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if matrix[i][j] == "J":
            jihun_x, jihun_y = i, j
        elif matrix[i][j] == "F":
            q.append((FIRE, i, j))

q.appendleft((1, jihun_x, jihun_y))  # 지훈이가 먼저 움직여야 하므로 deque의 맨 앞에 넣어준다.
matrix[jihun_x][jihun_y] = VISITED


def check_range(x, y):
    if x >= 0 and y >= 0 and x < r and y < c:
        return True
    return False


def is_finish(x, y):
    if x == 0 or y == 0 or x == r-1 or y == c-1:
        return True
    return False


def bfs():
    while q:
        time, x, y = q.popleft()

        if time == FIRE:  # 불
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if check_range(nx, ny) and (matrix[nx][ny] == VISITED or matrix[nx][ny] == NOT_VISITED):
                    matrix[nx][ny] = "F"
                    q.append((-1, nx, ny))

        else:
            if is_finish(x, y) and matrix[x][y] != "F":
                return time
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if check_range(nx, ny) and matrix[nx][ny] == NOT_VISITED:
                    matrix[nx][ny] = VISITED
                    q.append((time+1, nx, ny))
    return "IMPOSSIBLE"


print(bfs())
