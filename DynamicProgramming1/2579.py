n = int(input())
arr = [0]+[int(input()) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n+2)]  # dp[i][j] -> i 번째 계단을 j 번 연속해서 올랐을 때 최댒값
dp[1][1] = arr[1]
for i in range(2, n+1):
    # i 번째 계단을 첫 번째로 오르려면, i-2번째에서 두칸건너 올라오면 됨
    dp[i][1] = max(dp[i-2][1], dp[i-2][2])+arr[i]
    # i 번째 계단을 두 번째로 오르려면, i-1번째에서 1칸 오른 상태였을 때 + 현재 상태 하면 됨. 2칸 오른 상태에서 값을 가져오면, 3칸 연속으로 오르는 것이기 때문에 안됨.
    dp[i][2] = dp[i-1][1]+arr[i]

print(max(dp[n][1], dp[n][2]))
