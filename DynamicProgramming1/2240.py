t, w = map(int, input().split())

jadu = list(int(input()) for _ in range(t))
dp = [[0]*(w+1) for _ in range(t)]

if jadu[0] == 1:
    dp[0][0] = 1
else:
    dp[0][1] = 1

for i in range(1, t):
    if jadu[i] == 1:
        dp[i][0] = dp[i-1][0]+1
    else:
        dp[i][0] = dp[i-1][0]

for i in range(1, t):
    for j in range(1, w+1):
        if j % 2 == jadu[i] % 2:  # 해당 칸에서 자두를 얻을 수 없을 경우
            dp[i][j] = dp[i-1][j]
        else:
            # 해당 칸에서 자두를 얻을 수 있는 경우
            # 움직여서 자두 얻기 vs 안움직여서 자두 얻기
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+1

print(max(dp[-1]))
