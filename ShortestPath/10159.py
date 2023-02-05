# pypy3 메모리 초과, python 시간초과
# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# go = [set() for _ in range(n+1)]
# back = [set() for _ in range(n+1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     go[a].add(b)
#     back[b].add(a)


# def solution(graph, node):
#     can_go = set()
#     q = deque()
#     q.append(node)
#     can_go.add(node)

#     while q:
#         x = q.popleft()
#         for i in graph[x]:
#             can_go.add(i)
#             q.append(i)
#     return can_go


# for i in range(1, n+1):
#     go_cnt = solution(go, i)
#     back_cnt = solution(back, i)
#     answer = go_cnt.union(back_cnt)
#     print(n-len(answer))

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n+1):
    graph[i][i] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            if graph[i][j] == 1:
                continue
            if graph[i][k]+graph[k][j] < INF:
                graph[i][j] = 1

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] == 1 or graph[j][i] == 1:
            cnt += 1
    print(n-cnt)
