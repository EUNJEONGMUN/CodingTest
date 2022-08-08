# 정렬로 풀기 -> 시간초과

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# works = []

# for i in enumerate(arr, 1):
#     start, work = i
#     end, cost = start+work[0]-1, work[1]
#     if end <= n:
#         works.append([start, end, cost])

# works.sort(key=lambda x: (-x[2], x[1], -x[0]))

# dp = [False]*(n+1)

# res = 0
# for start, end, cost in works:
#     if sum(dp[start:end+1]) == 0:
#         res += cost
#         dp[start:end+1] = [True]*(end-start+1)

# print(res)
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)

max_value = 0
for i in range(n):
    max_value = max(dp[i], max_value)
    if i+arr[i][0] > n:
        continue
    dp[i+arr[i][0]] = max(dp[i+arr[i][0]],  max_value + arr[i][1])
print(max(dp))
