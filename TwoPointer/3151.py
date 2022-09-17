# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()

# res = 0


# def solution(left, right):
#     global res
#     val = arr[left]+arr[right]
#     if val > 0:
#         start = left+1
#         while start < right:
#             if val+arr[start] == 0:
#                 res += 1
#             start += 1
#             if arr[start] > 0 or val+arr[start] > 0:
#                 break

#     elif val < 0:
#         start = right-1
#         while start > left:
#             if val+arr[start] == 0:
#                 res += 1
#             start -= 1
#             if arr[start] < 0 or val+arr[start] < 0:
#                 break

#     else:
#         start = left+1
#         while start < right:
#             if val+arr[start] == 0:
#                 res += 1
#             start += 1


# left, right = 0, n-1
# while left < right:
#     if arr[left]*arr[right] <= 0:
#         solution(left, right)
#     for i in range(left+1, right-1):
#         if arr[i]*arr[right] > 0:
#             break
#         solution(i, right)
#     for i in range(right-1, left+1, -1):
#         if arr[left]*arr[i] > 0:
#             break
#         solution(left, i)
#     left += 1
#     right -= 1

# print(res)

import sys
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0

for i in range(len(arr)-2):
    left, right = i+1, n-1
    while left < right:
        num = arr[i]+arr[left]+arr[right]
        if num > 0:
            right -= 1
        else:
            if num == 0:
                if arr[left] == arr[right]:
                    res += right-left
                else:
                    idx = bisect_left(arr, arr[right])
                    res += right-idx+1
            left += 1

print(res)
# for문을 돌면서 i가 하나씩 증가하면서 보기 때문에 i가 꼭 들어갈 경우의 수만 세야 한다!!
