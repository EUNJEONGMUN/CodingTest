import sys
input = sys.stdin.readline

n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
dp = [[[INF]*3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    dp[0][j] = [space[0][j]]*3

for i in range(1, n):
    for j in range(m):
        # 수직으로 내려오는 경우
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2])+space[i][j]

        # 왼쪽에서 내려오는 경우
        if j != 0:
            dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1])+space[i][j]

        # 오른쪽에서 내려오는 경우
        if j != m-1:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2])+space[i][j]

print(min([min(dp[n-1][j]) for j in range(m)]))
