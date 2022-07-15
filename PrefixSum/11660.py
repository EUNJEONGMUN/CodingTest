import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

table = [[0]*(n+1)]
for a in arr:
    table.append([0]+a[:])

# 열별로 더하기
for i in range(1, n+1):
    for j in range(1, n+1):
        table[i][j] += table[i-1][j]
# 헹별로 더하기
for j in range(1, n+1):
    for i in range(1, n+1):
        table[i][j] += table[i][j-1]

for _ in range(m):
    a, b, x, y = map(int, input().split())
    print(table[x][y]-table[x][b-1]-table[a-1][y]+table[a-1][b-1])
