# dfs 풀이 -> 시간초과

# import sys
# input = sys.stdin.readline

# n = int(input())
# table = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0]*n for _ in range(n)]


# def check_range(x, y):
#     if x >= 0 and y >= 0 and x < n and y < n:
#         return True
#     return False


# def solution(x, y):
#     if x == n-1 and y == n-1:
#         return

#     if check_range(x, y+table[x][y]):
#         dp[x][y+table[x][y]] += 1
#         solution(x, y+table[x][y])

#     if check_range(x+table[x][y], y):
#         dp[x+table[x][y]][y] += 1
#         solution(x+table[x][y], y)


# solution(0, 0)
# print(dp[-1][-1])


import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1  # 초기화
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[-1][-1])
            break
        now = table[i][j]
        if j+table[i][j] < n:  # 오른쪽
            dp[i][j+now] += dp[i][j]
        if i+table[i][j] < n:  # 아래
            dp[i+now][j] += dp[i][j]
