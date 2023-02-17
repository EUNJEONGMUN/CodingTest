# 당연히.. 시간초과
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())

# matrix = [[INF] * (n+1) for _ in range(n+1)]

# for i in range(1, n+1):
#     matrix[i][i] = 0

# for _ in range(n-1):
#     a, b, c = map(int, input().split())
#     matrix[a][b] = c
#     matrix[b][a] = c

# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == j:
#                 continue
#             matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

# for _ in range(m):
#     a, b = map(int, input().split())
#     print(matrix[a][b])

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def solution(start, end):
    visited = [False]*(n+1)
    q = deque()
    q.append((start, 0))
    visited[start] = True
    while q:
        node, dist = q.popleft()

        if node == end:
            return dist

        for next_node, d in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, dist+d))


for _ in range(m):
    a, b = map(int, input().split())
    print(solution(a, b))
