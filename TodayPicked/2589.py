import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def bfs(x, y):
    q = deque()
    q.append((x, y))
    distance = [[-1]*m for _ in range(n)]
    distance[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if check_range(nx, ny) and area[nx][ny] == "L":
                if distance[nx][ny] == -1 or distance[x][y]+1 < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y]+1
                    q.append((nx, ny))
    return max([max(row) for row in distance])


result = 0
for i in range(n):
    for j in range(m):
        if area[i][j] == "L":
            result = max(result, bfs(i, j))

print(result)
