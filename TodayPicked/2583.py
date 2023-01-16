from collections import deque
import sys
input = sys.stdin.readline
m, n, k = map(int, input().split())
array = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if (x >= 0 and y >= 0 and x < n and y < m):
        return True
    return False


def fill_block(a, b, c, d):
    for i in range(a, c):
        for j in range(b, d):
            array[i][j] = 1


for _ in range(k):
    a, b, c, d = map(int, input().split())
    fill_block(a, b, c, d)


def bfs(x, y):
    q = deque()
    area = 1
    q.append((x, y))
    array[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (check_range(nx, ny) and array[nx][ny] == 0):
                q.append((nx, ny))
                array[nx][ny] = 1
                area += 1
    return area


blank_area_count = 0
answer = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            blank_area_count += 1
            answer.append(bfs(i, j))

print(blank_area_count)
print(*sorted(answer))
