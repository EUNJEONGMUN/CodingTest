import sys
input = sys.stdin.readline

n, k = map(int, input().split())
weight, value = [0], [0]

for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

# dp[i][j] -> i 개의 보석이 있고, 배낭의 무게 한도가 j일 때 최대 이익
dp = [[0]*(k+1) for _ in range(n+1)]
maximum = 0
for i in range(1, n+1):
    for j in range(1, k+1):
        if j-weight[i] >= 0:  # 현재 무게(j)에서 i번째 물건을 담을 수 있는가?
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
            # dp[i][j] = max(현재 물건을 담지 않을 때, 현재 물건을 담을 때)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
