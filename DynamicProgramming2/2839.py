INF = int(1e9)
n = int(input())
dp = [INF]*(n+1)
dp[0] = 0
for i in range(1, n+1):
    if i-3 >= 0:
        dp[i] = min(dp[i], dp[i-3]+1)
    if i-5 >= 0:
        dp[i] = min(dp[i], dp[i-5]+1)

print(-1 if dp[-1] == INF else dp[-1])
