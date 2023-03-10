from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
matrix = list(list(input().strip()) for _ in range(n))
INF = int(1e9)
dist = [[INF]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def solution():
    q = deque()
    dist[0][0] = 0
    q.append((0, (0, 0)))

    while q:
        cnt, position = q.popleft()

        if cnt > dist[position[0]][position[1]]:
            continue

        for i in range(4):
            nx, ny = position[0]+dx[i], position[1]+dy[i]
            if check_range(nx, ny):
                if matrix[nx][ny] == "1" and dist[nx][ny] > cnt+1:
                    dist[nx][ny] = cnt+1
                    q.append((cnt+1, (nx, ny)))
                elif matrix[nx][ny] == "0" and dist[nx][ny] > cnt:
                    dist[nx][ny] = cnt
                    q.append((cnt, (nx, ny)))


solution()
print(dist[-1][-1])
