# 풀이1
# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# INF = int(10e9)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# matrix = [list(map(int, input().split())) for _ in range(n)]
# lands = []


# def check_range(x, y):
#     if x >= 0 and y >= 0 and x < n and y < n:
#         return True
#     return False


# def find_land(idx, x, y):
#     land = []
#     q = deque()
#     visited[x][y] = True
#     matrix[x][y] = idx
#     q.append((x, y))

#     while q:
#         x, y = q.popleft()
#         flag = False
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if check_range(nx, ny) and not visited[nx][ny]:
#                 if matrix[nx][ny] == 1:
#                     q.append((nx, ny))
#                     visited[nx][ny] = True
#                     matrix[nx][ny] = idx
#                 else:
#                     flag = True
#         if flag:
#             land.append((x, y))
#     return land


# def find_shortest(index):
#     distance = [[INF]*n for _ in range(n)]
#     answer = INF
#     q = deque(lands[index])
#     for x, y in lands[index]:
#         distance[x][y] = 0
#     now_index = matrix[x][y]

#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if check_range(nx, ny):
#                 if matrix[nx][ny] == 0:
#                     if distance[x][y]+1 < distance[nx][ny]:
#                         distance[nx][ny] = distance[x][y]+1
#                         q.append((nx, ny))
#                 elif matrix[nx][ny] != now_index:
#                     answer = min(answer, distance[x][y])
#     return answer


# visited = [[False]*n for _ in range(n)]
# idx = 2
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] == 1 and not visited[i][j]:
#             lands.append(find_land(idx, i, j))
#             idx += 1

# ans = INF
# for i in range(len(lands)):
#     ans = min(ans, find_shortest(i))

# print(ans)


# 풀이2
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
INF = int(10e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

matrix = [list(map(int, input().split())) for _ in range(n)]
lands = []


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


def find_land(x, y):
    land = []
    q = deque()
    visited[x][y] = True
    q.append((x, y))

    while q:
        x, y = q.popleft()
        flag = False
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if check_range(nx, ny) and not visited[nx][ny]:
                if matrix[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                else:
                    flag = True
        if flag:
            land.append((x, y))
    return land


def find_shortest(x, y):
    ans = INF
    for a, b in lands[x]:
        for c, d in lands[y]:
            ans = min(ans, (abs(a-c)+abs(b-d)-1))
    return ans


visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            lands.append(find_land(i, j))

ans = INF
for i in range(len(lands)):
    for j in range(i+1, len(lands)):
        ans = min(find_shortest(i, j), ans)

print(ans)
