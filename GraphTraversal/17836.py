import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
distance = [[INF]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def bfs():
    q = deque([(0, 0)])
    distance[0][0] = 0

    while q:
        x, y = q.popleft()

        if arr[x][y] == 2:  # '그람'을 먹을 경우 바로 공주님 까지의 거리 계산 가능
            distance[-1][-1] = min(distance[-1][-1],
                                   distance[x][y]+(n-1-x)+(m-1-y))

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if check_range(nx, ny) and arr[nx][ny] != 1:
                if distance[nx][ny] > distance[x][y]+1:  # 거리가 더 짧을 경우 갱신
                    distance[nx][ny] = distance[x][y]+1
                    q.append((nx, ny))


bfs()

if distance[-1][-1] > t:
    print("Fail")
else:
    print(distance[-1][-1])
