import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

matrix = [[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    matrix[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

answer = INF
for k in range(1, v+1):
    answer = min(answer, matrix[k][k])

if answer == INF:
    print(-1)
else:
    print(answer)
