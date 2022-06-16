import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0


def check_range(i, j):
    if i >= 0 and j >= 0 and i < N and j < N:
        return True
    return False


def check_diff(a, b, c, d):  # 인구 차이 계산
    diff = abs(arr[a][b]-arr[c][d])
    if L <= diff <= R:
        return True
    return False


def bfs(i, j):
    q = deque([[i, j]])
    visited[i][j] = True
    res = []
    res.append([i, j])  # 인구 이동 할 좌표 list
    cnt = arr[i][j]  # 인구 합

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if check_range(nx, ny) and not visited[nx][ny] and check_diff(x, y, nx, ny):
                res.append([nx, ny])
                q.append([nx, ny])
                visited[nx][ny] = True
                cnt += arr[nx][ny]

    avg = cnt//len(res)

    if len(res) > 1:
        for a, b in res:
            arr[a][b] = avg
        return True
    else:
        return False


while True:

    visited = [[False]*N for _ in range(N)]
    mark = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and bfs(i, j):
                mark = True

    if mark:  # 인구 이동이 일어났다면
        answer += 1
    else:  # 인구 이동이 일어나지 않는다면
        break

print(answer)
