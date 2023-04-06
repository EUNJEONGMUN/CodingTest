# from collections import deque


# def solution(n, m, x, y, queries):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]

#     def move(positions, query):
#         direction, dist = query
#         q = []
#         for now_x, now_y in positions:
#             nx, ny = now_x+(dx[direction]*dist), now_y+(dy[direction]*dist)
#             if direction == 0:
#                 if now_y == 0:
#                     for i in range(min(m-1, ny)+1):
#                         q.append((nx, i))
#                 else:
#                     if ny < m:
#                         q.append((nx, ny))
#             elif direction == 1:
#                 if now_y == m-1:
#                     for i in range(max(0, ny), m):
#                         q.append((nx, i))
#                 else:
#                     if ny >= 0:
#                         q.append((nx, ny))
#             elif direction == 2:
#                 if now_x == 0:
#                     for i in range(min(n-1, nx)+1):
#                         q.append((i, ny))
#                 else:
#                     if nx < n:
#                         q.append((nx, ny))
#             elif direction == 3:
#                 if now_x == n-1:
#                     for i in range(max(0, nx), n):
#                         q.append((i, ny))
#                 else:
#                     if nx >= 0:
#                         q.append((nx, ny))
#         return q

#     log = [(x, y)]
#     for query in queries[::-1]:
#         log = move(log, query)
#         print(log)

#     return len(log)

def solution(n, m, x, y, queries):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def move(start, end, distance, K):
        if start == 0 and distance > 0:
            ns = 0
        else:
            ns = start+distance

        if end == K-1 and distance < 0:
            ne = K-1
        else:
            ne = end+distance

        if (ns >= K or ne < 0):
            return (-1, -1)
        elif (ns < 0):
            return (0, ne)
        elif (ne >= K):
            return (ns, K-1)
        else:
            return (ns, ne)

    start_x, start_y, end_x, end_y = x, y, x, y

    for direction, dist in queries[::-1]:
        if direction == 0 or direction == 1:
            start_y, end_y = move(start_y, end_y, (dy[direction]*dist), m)
        else:
            start_x, end_x = move(start_x, end_x, (dx[direction]*dist), n)
        if start_x == -1 or start_y == -1:
            return 0
    return (end_x-start_x+1)*(end_y-start_y+1)


def solution2(n, m, x, y, queries):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    start_x, start_y, end_x, end_y = x, y, x, y
    for direction, dist in queries[::-1]:
        if direction == 0:
            if start_y != 0:
                start_y += (dy[direction]*dist)
            end_y = min(m-1, end_y+dy[direction]*dist)
        elif direction == 1:
            if end_y != m-1:
                end_y += (dy[direction]*dist)
            start_y = max(0, start_y+dy[direction]*dist)
        elif direction == 2:
            if start_x != 0:
                start_x += (dx[direction]*dist)
            end_x = min(n-1, end_x+dx[direction]*dist)
        elif direction == 3:
            if end_x != n-1:
                end_x += (dx[direction]*dist)
            start_x = max(0, start_x+dx[direction]*dist)

        if start_x > end_x or start_y > end_y:
            return 0
    return (end_x-start_x+1)*(end_y-start_y+1)


# print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
print(solution2(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))
