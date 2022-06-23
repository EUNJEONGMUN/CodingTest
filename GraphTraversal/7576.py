import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def bfs(arr):
    q = deque(arr)
    res = 0

    while q:
        x, y, cnt = q.popleft()
        res = max(res, cnt)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if check_range(nx, ny) and table[nx][ny] == 0:
                table[nx][ny] = cnt+1
                q.append((nx, ny, cnt+1))
    return res-1


tomato = []

for i in range(n):
    for j in range(m):
        if table[i][j] == 1:
            tomato.append((i, j, 1))


res = bfs(tomato)
# mark = False  # 익지 않은 토마토가 있다면 True로 바뀜
# for i in range(n):
#     for j in range(m):
#         if table[i][j] == 0:
#             mark = True
#     if mark:
#         break
# if mark:
#     print(-1)
# else:
#     print(res)

for i in range(n):
    if 0 in table[i]:
        print(-1)
        break
else:
    print(res)
