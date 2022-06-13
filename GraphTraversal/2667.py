import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


def bfs(a, b):
    cnt = 1
    q = deque([(a, b)])
    graph[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if check(nx, ny) and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1

    return cnt


res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            res.append(bfs(i, j))
res.sort()
print(len(res))
for i in res:
    print(i)
