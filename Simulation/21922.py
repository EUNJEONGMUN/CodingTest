from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
U, R, D, L = 0, 1, 2, 3
case3 = [R, U, L, D]
case4 = [L, D, R, U]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def bfs(x, y):
    q = deque()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        q.append((nx, ny, i))

    while q:
        x, y, direction = q.popleft()

        if not check_range(x, y):
            continue

        visited[x][y] = True

        if arr[x][y] == 1:
            if direction == L or direction == R:
                continue
        elif arr[x][y] == 2:
            if direction == U or direction == D:
                continue
        elif arr[x][y] == 3:
            direction = case3[direction]
        elif arr[x][y] == 4:
            direction = case4[direction]
        elif arr[x][y] == 9:  # 에어컨을 만나면 멈춤
            continue
        q.append((x+dx[direction], y+dy[direction], direction))


for i in range(n):
    for j in range(m):
        if arr[i][j] == 9:
            visited[i][j] = True
            bfs(i, j)
answer = 0
for v in visited:
    answer += sum(v)
print(answer)
