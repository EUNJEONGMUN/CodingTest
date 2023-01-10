# 메모리 초과
# from collections import deque

# n = int(input())
# now = list(map(bool, list(map(int, list(input())))))
# wish = list(map(bool, list(map(int, list(input())))))
# log = set()

# queue = deque()
# log.add(tuple(wish))
# queue.append([wish[:], 0])
# answer = -1
# while queue:
#     temp, cnt = queue.popleft()

#     if (temp == now):
#         if answer == -1:
#             answer = cnt
#         else:
#             answer = min(answer, cnt)
#     for i in range(len(temp)):
#         new_temp = temp[:]
#         if i == 0:
#             new_temp[0] = not temp[0]
#             new_temp[1] = not temp[1]
#         elif i == len(temp)-1:
#             new_temp[-1] = not temp[-1]
#             new_temp[-2] = not temp[-2]
#         else:
#             new_temp[i-1] = not temp[i-1]
#             new_temp[i] = not temp[i]
#             new_temp[i+1] = not temp[i+1]

#         if (tuple(new_temp) not in log):
#             log.add(tuple(new_temp))
#             queue.append([new_temp, cnt+1])
# print(answer)

n = int(input())
now = list(map(bool, list(map(int, list(input())))))
wish = list(map(bool, list(map(int, list(input())))))
INF = int(1e9)
answer = -1


def change(bulb: list):
    count = 0
    for i in range(1, n):
        if (bulb[i-1] != wish[i-1]):
            count += 1
            bulb[i-1] = not bulb[i-1]
            bulb[i] = not bulb[i]
            if (i != n-1):
                bulb[i+1] = not bulb[i+1]
    return count if bulb == wish else INF


answer = change(now[:])
now[0] = not now[0]
now[1] = not now[1]
answer = min(answer, change(now[:])+1)
print(-1 if answer == INF else answer)
