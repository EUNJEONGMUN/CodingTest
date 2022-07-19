# 시간초과
# 1 ≤ N ≤ 200,000 이기 때문에
# 부분 집합의 경우의 수가 200억 정도
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# arr = [0]+list(map(int, input().split()))
# res = 0
# for i in range(1, n+1):
#     arr[i] += arr[i-1]

# for num in range(1, n+1):
#     start, end = 1, num

#     while end < len(arr):
#         if arr[end]-arr[start-1] == k:
#             res += 1
#         start += 1
#         end += 1

# print(res)

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# res = 0

# for i in range(1, n+1):
#     arr[i] += arr[i-1]

# for num in range(1, n+1):
#     start, end = 1, num

#     while end < len(arr):
#         if arr[end]-arr[start-1] == k:
#             res += 1
#         start += 1
#         end += 1

# print(res)

import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans, pSum, cnt = 0, 0, defaultdict(int)
cnt[0] = 1
for i in range(n):
    pSum += arr[i]
    if pSum - k in cnt:
        ans += cnt[pSum - k]
    cnt[pSum] += 1
print(ans)
