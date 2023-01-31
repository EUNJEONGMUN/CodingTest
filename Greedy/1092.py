# from collections import deque

# n = int(input())
# cranes = sorted(list(map(int, input().split())), reverse=True)
# m = int(input())
# boxes = deque(sorted(list(map(int, input().split())), reverse=True))


# def solution():
#     count = 0
#     while boxes:
#         count += 1
#         for i in range(n):
#             if boxes:
#                 if boxes[0] > cranes[i]:
#                     if i == 0:
#                         return -1
#                     break
#                 boxes.popleft()
#     return count


# print(solution())

"""
반례
3
10 6 5
11
6 8 9 6 8 6 9 6 8 6 9
// 6

1
1
1
1
// 1
"""

from bisect import bisect_right

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int, input().split())))


def solution():
    answer = 0
    while True:
        update = False
        answer += 1
        for i in range(n):
            idx = bisect_right(boxes, cranes[i])
            if idx == 0:
                if len(boxes) == 0:
                    return answer if update else answer-1
                continue
            boxes.pop(idx-1)
            update = True

        if not update:
            return -1


print(solution())
