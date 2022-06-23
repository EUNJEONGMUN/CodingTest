import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

table = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dh = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]


def check_range(h, x, y):
    if h >= 0 and x >= 0 and y >= 0 and h < H and x < N and y < M:
        return True
    return False


def bfs(arr):
    q = deque(arr)
    res = 0

    while q:
        h, x, y, cnt = q.popleft()
        res = max(res, cnt)
        for i in range(6):
            nh = h+dh[i]
            nx = x+dx[i]
            ny = y+dy[i]
            if check_range(nh, nx, ny) and table[nh][nx][ny] == 0:
                table[nh][nx][ny] = cnt+1
                q.append((nh, nx, ny, cnt+1))
    return res-1


tomato = []

for h in range(H):
    for i in range(N):
        for j in range(M):
            if table[h][i][j] == 1:
                tomato.append((h, i, j, 1))


res = bfs(tomato)
mark = False
for h in range(H):
    for i in range(N):
        if 0 in table[h][i]:
            mark = True
            break
    if mark:
        break

if mark:
    print(-1)
else:
    print(res)
