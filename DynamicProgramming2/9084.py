import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    coins = [0] + list(map(int, input().split()))
    m = int(input())

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if j < coins[i]:
                dp[i][j] = dp[i-1][j]
            elif j == coins[i]:
                dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j]
    print(dp[-1][-1])
