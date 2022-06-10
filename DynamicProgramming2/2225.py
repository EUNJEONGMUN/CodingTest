import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0]*(N+1) for _ in range(K+1)]


for k in range(1, K+1):
    for n in range(1, N+1):
        if n == 1:
            dp[k][n] = k
        else:
            dp[k][n] = dp[k-1][n]+dp[k][n-1]

print(dp[-1][-1])
