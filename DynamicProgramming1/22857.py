# 투 포인터
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# left, right = 0, 0
# result = 0
# delete = 0
# while right < n:
#     if arr[right] % 2 == 0:
#         right += 1
#     else:
#         if delete < k:  # 아직 지울 기회가 남았다면 지우기
#             delete += 1
#             right += 1

#         else:  # 지울 기회가 남지 않았다면
#             result = max(result, right-left-delete)  # 지금까지의 결과 중 최대값을 저장
#             while True:  # 왼쪽에서 홀수가 나올때까지 while문
#                 if arr[left] % 2 == 1:
#                     delete -= 1
#                     left += 1
#                     break
#                 left += 1
# print(max(result, right-left-delete))

# DP
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0]+list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(k+2)]
for j in range(1, n+1):
    for i in range(1, k+2):
        if arr[j] % 2 == 0:  # 짝수일 때
            dp[i][j] = dp[i][j-1]+1
        else:
            dp[i][j] = dp[i-1][j-1]

print(max([max(i) for i in dp]))
