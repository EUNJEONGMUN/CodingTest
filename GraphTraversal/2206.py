import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]
distance = [[[INF, INF] for _ in range(m)] for _ in range(n)]

NOT_BROKEN = 0
BROKEN = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def bfs(x, y):
    q = deque()
    q.append((1, x, y, NOT_BROKEN))
    distance[x][y] = [1, 1]

    while q:
        dist, x, y, now_broken = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if check_range(nx, ny):
                if matrix[nx][ny] == 1 and now_broken == NOT_BROKEN:
                    if distance[nx][ny][BROKEN] > dist+1:
                        distance[nx][ny][BROKEN] = dist+1
                        q.append((dist+1, nx, ny, True))
                elif matrix[nx][ny] == 0:
                    if distance[nx][ny][now_broken] > dist+1:
                        distance[nx][ny][now_broken] = dist+1
                        q.append((dist+1, nx, ny, now_broken))


bfs(0, 0)
answer = min(distance[-1][-1])
if answer == INF:
    print(-1)
else:
    print(answer)
