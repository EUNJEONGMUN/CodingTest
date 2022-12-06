import sys
input = sys.stdin.readline
INF = int(1e9)

c, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

dp = [INF]*(c+100)
dp[0] = 0

for cost, customer in arr:
    for i in range(customer, c+100):
        dp[i] = min(dp[i], dp[i-customer]+cost)


print(min(dp[c:]))
