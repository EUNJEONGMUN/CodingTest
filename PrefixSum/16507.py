import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
prefix_sum = [[0]*(c+1) for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        prefix_sum[i][j] = prefix_sum[i][j-1]+matrix[i-1][j-1]

for j in range(1, c+1):
    for i in range(2, r+1):
        prefix_sum[i][j] += prefix_sum[i-1][j]

for _ in range(q):
    a, b, c, d = map(int, input().split())
    total = prefix_sum[c][d]-prefix_sum[c][b-1] - \
        prefix_sum[a-1][d]+prefix_sum[a-1][b-1]
    count = (c-a+1)*(d-b+1)
    print(total//count)
