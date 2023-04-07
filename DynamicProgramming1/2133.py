n = int(input())


def solution(n):
    if n % 2 == 1:
        return 0

    dp = [0]*(n//2+1)
    dp[0] = 1
    dp[1] = 3
    for i in range(2, n//2+1):
        dp[i] = (dp[i-1]*3)
        for j in range(i-2, -1, -1):
            dp[i] += dp[j]*2
    return dp[-1]


print(solution(n))
