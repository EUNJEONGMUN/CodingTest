# 풀이 1 52ms
# import sys
# from bisect import bisect_left

# n = int(input())
# students = [int(input()) for _ in range(n)]

# value = [students[0]]

# for i in range(1, n):
#     if students[i] > value[-1]:
#         value.append(students[i])
#     else:
#         idx = bisect_left(value, students[i])
#         value[idx] = students[i]

# print(n-len(value))


import sys

n = int(input())
students = [int(input()) for _ in range(n)]

dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if students[i] > students[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
