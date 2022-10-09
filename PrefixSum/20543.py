import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
original = [[0]*(n+1) for _ in range(n+1)]
# 누적합을 원래대로
# 열 복귀

for j in range(n):
    original[0][j] = arr[0][j]
    for i in range(1, n):
        original[i][j] = arr[i][j]-arr[i-1][j]
    original[n][j] = 0-arr[n-1][j]

# 행 복귀
for i in range(n+1):
    pre = original[i][0]
    for j in range(1, n+1):
        temp = original[i][j]-pre
        pre = original[i][j]
        original[i][j] = temp

res = [[0]*(n) for _ in range(n)]
for i in range(n+1):
    for j in range(n+1):
        if original[i][j] < 0:
            cnt = -original[i][j]
            res[i+(m//2)][j+(m//2)] = cnt
            original[i][j] += cnt
            original[i+m][j] -= cnt
            original[i][j+m] -= cnt
            original[i+m][j+m] += cnt

for i in res:
    print(*i)
