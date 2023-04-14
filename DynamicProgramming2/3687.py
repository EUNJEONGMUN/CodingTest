import sys
input = sys.stdin.readline

n = int(input())

dp = [-1]*101
dp[2], dp[3], dp[4], dp[5], dp[6], dp[7], dp[8] = 1, 7, 4, 2, 6, 8, 10

for num in range(9, 101):
    for i in range(2, 8):
        if i == 6:
            if dp[num] == -1:
                dp[num] = dp[num-i]*10
            else:
                dp[num] = min(dp[num], dp[num-i]*10)
        else:
            if dp[num] == -1:
                dp[num] = dp[num-i]*10+dp[i]
            else:
                dp[num] = min(dp[num], dp[num-i]*10+dp[i])

for _ in range(n):
    k = int(input())
    if k % 2 == 0:
        max_value = "1"*(k//2)
    else:
        max_value = "7"+"1"*((k-3)//2)
    print(dp[k], max_value)
