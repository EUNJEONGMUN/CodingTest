# from collections import deque
# import sys
# input = sys.stdin.readline

# dy = [-2, -1, 0, 1, 2]
# n, t = map(int, input().split())
# matrix = [[] for _ in range(200001)]

# for _ in range(n):
#     x, y = map(int, input().split())
#     matrix[y].append(x)


# def bfs():
#     queue = deque()
#     queue.append([(0, 0), 0])
#     while queue:
#         point, cnt = queue.popleft()
#         x, y = point
#         if y == t:
#             return cnt
#         for i in dy:
#             ny = y+dy[i]
#             if ny >= 0 and ny <= t:
#                 for nx in matrix[ny]:
#                     if nx >= 0 and nx <= n and abs(n-x) <= 2:
#                         queue.append((nx, ny), cnt+1)
#     return -1


# print(bfs())

from collections import deque
import sys
input = sys.stdin.readline

n, t = map(int, input().split())
hole = set()

for _ in range(n):
    x, y = map(int, input().split())
    hole.add((x, y))


def bfs(x, y):
    answer = sys.maxsize
    queue = deque()
    queue.append(((x, y), 0))
    while queue:
        point, cnt = queue.popleft()
        x, y = point
        if y == t:
            answer = min(answer, cnt)
            continue
        for i in range(-2, 3):
            for j in range(-2, 3):
                if (x+i, y+j) in hole:
                    queue.append(((x+i, y+j), cnt+1))
                    hole.remove((x+i, y+j))

    return -1 if answer == sys.maxsize else answer


print(bfs(0, 0))
