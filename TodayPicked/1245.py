import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, -1, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(x, y):
    count = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        flag = True
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if check_range(nx, ny) and area[x][y] <= area[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                flag = False
        if flag:
            count += 1

    return count


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


print(bfs(0, 0))
