# import sys
# from collections import deque
# from itertools import combinations

# input = sys.stdin.readline

# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def check_range(x, y):
#     if x >= 0 and y >= 0 and x < n and y < m:
#         return True
#     return False


# def copy():
#     temp = [[0]*m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             temp[i][j] = grid[i][j]
#     return temp


# def bfs(i, j, arr):
#     visited = [[False]*m for _ in range(n)]
#     q = deque([(i, j)])

#     visited[i][j] = True

#     while q:
#         x, y = q.popleft()

#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]

#             if check_range(nx, ny) and arr[nx][ny] == 0 and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 q.append((nx, ny))

#     return visited


# def solution(i, j, k):
#     arr = copy()
#     for a, b in [i, j, k]:
#         arr[a][b] = 1

#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 2:
#                 visited = bfs(i, j, arr)

#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 0 and not visited[i][j]:
#                 cnt += 1
#     return cnt


# wall = []
# for i in range(n):
#     for j in range(m):
#         if grid[i][j] == 0:
#             wall.append((i, j))

# choices = combinations(wall, 3)

# res = 0
# for choice in choices:
#     temp = solution(choice[0], choice[1], choice[2])
#     res = max(res, temp)

# print(res)

# 14502 version1 -> deepcopy 사용 -> python3->5336ms, pypy3 ->1108ms
# import sys
# from itertools import combinations
# import copy
# input = sys.stdin.readline

# N, M = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# wall = []

# for i in range(N):
#     for j in range(M):
#         if grid[i][j] == 0:
#             wall.append((i, j))

# choices = combinations(wall, 3)


# def check(x, y):
#     if x >= 0 and x < N and y >= 0 and y < M:
#         return True
#     return False


# def dfs(temp, visited, x, y):
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if check(nx, ny) and temp[nx][ny] == 0:
#             temp[nx][ny] = 2
#             visited[nx][ny] = True
#             dfs(temp, visited, nx, ny)


# result = 0
# for choice in choices:
#     temp = copy.deepcopy(grid)
#     visited = [[False]*M for _ in range(N)]
#     for a, b in choice:  # 벽채우기
#         temp[a][b] = 1

#     for i in range(N):
#         for j in range(M):
#             if temp[i][j] == 2 and visited[i][j] == False:
#                 visited[i][j] = True
#                 dfs(temp, visited, i, j)
#     count = 0
#     for i in temp:
#         for j in i:
#             if j == 0:
#                 count += 1
#     result = max(count, result)

# print(result)


# version2 -> copy 사용 안함
# import sys
# from itertools import combinations
# import copy
# input = sys.stdin.readline

# N, M = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# wall = []

# for i in range(N):
#     for j in range(M):
#         if grid[i][j] == 0:
#             wall.append((i, j))

# choices = combinations(wall, 3)


# def copy():
#     temp = [[0]*M for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             temp[i][j] = grid[i][j]
#     return temp


# def check(x, y):
#     if x >= 0 and x < N and y >= 0 and y < M:
#         return True
#     else:
#         return False


# def dfs(temp, visited, x, y):
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if check(nx, ny) and temp[nx][ny] == 0:
#             temp[nx][ny] = 2
#             visited[nx][ny] = True
#             dfs(temp, visited, nx, ny)


# result = 0
# for choice in choices:
#     temp = copy()
#     visited = [[False]*M for _ in range(N)]
#     for a, b in choice:  # 벽채우기
#         temp[a][b] = 1

#     for i in range(N):
#         for j in range(M):
#             if temp[i][j] == 2 and visited[i][j] == False:
#                 visited[i][j] = True
#                 dfs(temp, visited, i, j)
#     count = 0
#     for i in temp:
#         for j in i:
#             if j == 0:
#                 count += 1
#     result = max(count, result)

# print(result)


# 14502 version3 -> 다른 분 코드 참고하여 리스트 컴프리헨션 추가, copy 수정
import sys
from itertools import combinations
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

wall = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == 0]


def check(x, y):
    if x >= 0 and x < N and y >= 0 and y < M:
        return True
    else:
        return False


def dfs(temp, visited, x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if check(nx, ny) and temp[nx][ny] == 0:
            temp[nx][ny] = 2
            visited[nx][ny] = True
            dfs(temp, visited, nx, ny)


result = 0
for choice in combinations(wall, 3):
    temp = [g[:] for g in grid]
    visited = [[False]*M for _ in range(N)]
    for a, b in choice:  # 벽채우기
        temp[a][b] = 1

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2 and visited[i][j] == False:
                visited[i][j] = True
                dfs(temp, visited, i, j)
    count = 0
    for i in temp:
        for j in i:
            if j == 0:
                count += 1
    result = max(count, result)

print(result)
