# 14501

N = int(input())

data = []
dp = [0]*(N+1)
max_value = 0

for i in range(1, N+1):
    data.append(tuple(map(int, input().split())))

for i in range(N-1, -1, -1):  # 시작하는 날짜
    time = data[i][0] + i

    if time <= N:
        dp[i] = max(data[i][1] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
