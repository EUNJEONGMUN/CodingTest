from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
north_area = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        count = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # visited를 확인해주는 이유는 해당 횟수에 count를 빼서 0이 된 경우도 있으므로.
            if check_range(nx, ny) and not visited[nx][ny]:
                if north_area[nx][ny] == 0:
                    count += 1
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))

        if north_area[x][y] - count < 0:
            north_area[x][y] = 0
        else:
            north_area[x][y] -= count


try_count = 0
while True:
    group_count = 0
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if north_area[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                group_count += 1

    if group_count > 1:
        print(try_count)
        break
    if group_count == 0:
        print(0)
        break
    try_count += 1
