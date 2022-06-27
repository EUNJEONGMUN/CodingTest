# 풀이1 -> combinations
from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

orders = combinations(list(range(m)), 3)

res = 0

for a, b, c in orders:
    temp = 0
    for people in arr:
        temp += max(people[a], people[b], people[c])

    if res < temp:
        res = temp
print(res)

# 풀이2 for문
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# res = 0


# for a in range(m-2):
#     for b in range(a+1, m-1):
#         for c in range(b+1, m):
#             temp = 0
#             for people in arr:
#                 temp += max(people[a], people[b], people[c])
#             if res < temp:
#                 res = temp
# print(res)
