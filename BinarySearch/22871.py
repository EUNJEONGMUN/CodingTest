import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
rocks = [0]+list(map(int, input().split()))
INF = int(1e9)
dp = [INF]*(n+1)
dp[0], dp[1] = 0, 0

for j in range(2, n+1):
    for i in range(1, n):
        if i >= j:
            continue
        power = (j-i)*(1+abs(rocks[i]-rocks[j]))
        dp[j] = min(dp[j], max(power, dp[i]))

print(dp[-1])
