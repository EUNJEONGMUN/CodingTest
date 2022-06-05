n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n)]

dp[0] = [rgb[0][0], rgb[0][1], rgb[0][2]]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + \
        rgb[i][0]  # i번째 집 -> 빨강. 이전은 초록or파랑
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + \
        rgb[i][1]  # i번째 집 -> 초록. 이전은 빨강or파랑
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + \
        rgb[i][2]  # i번째 집 -> 파랑. 이전은 빨강or초록
print(min(dp[n-1]))
