from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(a, b):
    if a >= 0 and b >= 0 and a < n and b < m:
        return True
    return False


def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]

    ways = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if check_range(nx, ny) and board[x][y] > board[nx][ny]:
            ways += dfs(nx, ny)

    visited[x][y] = ways
    return visited[x][y]


print(dfs(0, 0))
