n = int(input())
dp = [0]*(n+1)  # dp 테이블

for i in range(2, n+1):

    dp[i] = dp[i-1]+1  # 1을 뺄 때

    if i % 2 == 0:  # 2로 나누어 떨어질 때
        dp[i] = min(dp[i], dp[i//2]+1)

    if i % 3 == 0:  # 3으로 나누어 떨어질 때
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])
