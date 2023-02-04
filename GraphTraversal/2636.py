from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    count = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if check_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                if matrix[nx][ny] == 0:
                    q.append((nx, ny))
                elif matrix[nx][ny] == 1:
                    count += 1
                    matrix[nx][ny] = 0
    return count


answer = 0
time = 0
while True:
    visited = [[False]*(m) for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        print(time)
        print(answer)
        break
    else:
        time += 1
        answer = cnt
