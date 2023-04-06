import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


max_cnt = 1

log = set()


def dfs(x, y, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if check_range(nx, ny) and matrix[nx][ny] not in log:
            log.add(matrix[nx][ny])
            dfs(nx, ny, cnt+1)
            log.remove(matrix[nx][ny])


log.add(matrix[0][0])
dfs(0, 0, 1)
print(max_cnt)
