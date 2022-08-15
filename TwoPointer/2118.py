# 시간초과

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [int(input()) for _ in range(n)]*2

# res = 0

# for left in range(n-1):
#     temp_left = arr[left]
#     temp_right = sum(arr[left+1:left+n])
#     max_val = min(temp_left, temp_right)
#     if res < max_val:
#         res = max_val
#     for right in range(left+1, n-1):
#         temp_left += arr[right]
#         temp_right -= arr[right]
#         max_val = min(temp_left, temp_right)
#         if res < max_val:
#             res = max_val

# print(res)

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]*2
arr_sum = [0]*(n*2)
for i in range(1, n*2):  # 누적합 구하기
    arr_sum[i] = arr_sum[i-1]+arr[i-1]

res = 0
for left in range(n-1):
    for right in range(left+1, n):
        # 시계 방향 vs 반시계방향
        res = max(res, min(arr_sum[right]-arr_sum[left],
                  arr_sum[left+n]-arr_sum[right]))

print(res)
