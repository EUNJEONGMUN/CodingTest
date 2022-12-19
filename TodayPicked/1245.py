import sys
input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]  # 시계 방향으로
dy = [0, 1, 1, 1, 0, -1, -1, -1]  # ↑ ↗ → ↘ ↓ ↙ ← ↖


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def dfs(x, y):
    global flag
    visited[x][y] = True

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]

        if check_range(nx, ny):
            if area[x][y] < area[nx][ny]:  # 자신보다 높은 봉우리가 있다면 -> False
                flag = False
            if area[x][y] == area[nx][ny] and not visited[nx][ny]:  # 자신과 높이가 같다면 -> 같은 산봉우리가 될 수 있음
                dfs(nx, ny)


count = 0
for i in range(n):
    for j in range(m):
        if area[i][j] > 0 and not visited[i][j]:
            flag = True
            dfs(i, j)

            if flag:  # dfs를 거치고도 flag가 True면 산봉우리
                count += 1

print(count)
