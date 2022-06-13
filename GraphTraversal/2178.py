import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]
dist = [[INF]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(x, y):
    if x >= 0 and y >= 0 and x < n and y < m and graph[x][y] == 1:
        return True
    return False


def bfs(a, b):
    dist[a][b] = 1
    q = deque([(a, b)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if check(nx, ny) and dist[x][y]+1 < dist[nx][ny]:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))


bfs(0, 0)
print(dist[-1][-1])
