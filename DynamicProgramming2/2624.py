import sys
input = sys.stdin.readline

t = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]

dp = [0]*(t+1)
dp[0] = 1
for coin, count in coins:
    for now in range(t, 0, -1):
        for i in range(1, count+1):
            if now-(coin*i) >= 0:
                dp[now] += dp[now - (coin * i)]

print(dp[t])
