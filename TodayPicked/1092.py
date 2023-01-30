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
//6
"""

from collections import deque, Counter

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
a = Counter(list(map(int, input().split())))
boxes = deque(sorted(a.items(), reverse=True))


def solution():
    count = 0
    while boxes:
        count += 1
        box_index = 0
        for i in range(n):
            if box_index < len(boxes):
                while box_index < len(boxes):
                    if boxes[box_index][0] > cranes[i]:
                        if i == 0:
                            return -1
                        else:
                            box_index += 1
                    else:
                        box, cnt = boxes.popleft()
                        cnt -= 1
                        if cnt > 0:
                            boxes.appendleft((box, cnt))
                        break
            else:
                break
    return count


print(solution())
