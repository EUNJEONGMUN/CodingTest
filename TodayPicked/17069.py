# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# cnt = 0


# def move(a, b, direction):
#     global cnt
#     x, y = b[0], b[1]
#     if x == n-1 and y == n-1:
#         cnt += 1
#         return
#     elif x == n-1 and direction == "V":
#         return
#     elif y == n-1 and direction == "H":
#         return

#     if direction == "H":  # 가로 방향일 때
#         if arr[x][y+1] == 0:
#             move(b, [x, y+1], "H")
#         if x != n-1:
#             if arr[x+1][y+1] == 0 and arr[x+1][y] == 0 and arr[x][y+1] == 0:
#                 move(b, [x+1, y+1], "D")
#     elif direction == "V":
#         if arr[x][y+1] == 0:
#             move(b, [x+1, y], "V")
#         if y != n-1:
#             if arr[x+1][y+1] == 0 and arr[x+1][y] == 0 and arr[x][y+1] == 0:
#                 move(b, [x+1, y+1], "D")
#     else:
#         if arr[x][y+1] == 0:
#             move(b, [x, y+1], "H")
#         if x != n-1:
#             if arr[x][y+1] == 0:
#                 move(b, [x+1, y], "V")
#             if arr[x+1][y+1] == 0 and arr[x+1][y] == 0 and arr[x][y+1] == 0:
#                 move(b, [x+1, y+1], "D")


# move([0, 0], [0, 1], "H")
# print(cnt)


import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
# 0가로, 1세로, 2대각선

for i in range(n):
    for j in range(n):
        # 처음 놓여있는 칸이거나, 장애물이 있는 칸이면 pass
        if (i == 0 and j == 0) or (i == 0 and j == 1) or arr[i][j] == 1:
            continue
        if i == 0 and arr[i][j-1] == 0:  # 맨 첫째 행이면 왼쪽에서만 올 수 있음.
            dp[i][j][0] = dp[i][j-1][0]
        elif j == 0 and arr[i-1][j] == 0:  # 맨 첫째 열이면 위에서만 올 수 있음
            dp[i][j][1] = dp[i-1][j][1]
        else:
            if arr[i][j-1] == 0:  # 왼쪽에서 올 수 있는 경우
                dp[i][j][0] = dp[i][j-1][0]+dp[i][j-1][2]
            if arr[i-1][j] == 0:  # 위에서 올 수 있는 경우
                dp[i][j][1] = dp[i-1][j][1]+dp[i-1][j][2]
            if arr[i][j-1] == 0 and arr[i-1][j] == 0 and arr[i-1][j-1] == 0:  # 대각선에서 올 수 있는 경우
                dp[i][j][2] = sum(dp[i-1][j-1])

print(sum(dp[-1][-1]))
