from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

arr = [(i, j) for j in range(1, n-1) for i in range(1, n-1)]
orders = list(combinations(arr, 3))

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]
res = 3001

for order in orders:
    print(order)
    visited = [[False]*n for _ in range(n)]
    temp = 0
    mark = False
    for k in range(3):
        x, y = order[k][0], order[k][1]
        for i in range(5):
            nx = x+dx[i]
            ny = y+dy[i]

            if not visited[nx][ny]:
                temp += grid[nx][ny]
                visited[nx][ny] = True
            else:
                mark = True
                break
        if mark:
            break
    else:
        res = min(res, temp)

print(res)
