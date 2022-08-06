n, k = map(int, input().split())
dp = [100001]*100001
coins = [int(input()) for _ in range(n)]

dp[0] = 0

for coin in coins:
    for now in range(1, k+1):
        dp[now] = min(dp[now], dp[now-coin]+1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])
