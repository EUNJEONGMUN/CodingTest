import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0]*n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] > dp[i]:
            dp[i] = dp[j]  # 앞쪽까지의 값들 중에서 가장 큰 값으로 바꿈
    dp[i] += 1  # 1증가

print(max(dp))
