# 18352
from collections import deque
from sys import stdin
input = stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [-1]*(N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)


q = deque([X])
distance[X] = 0
while q:
    v = q.popleft()

    for i in graph[v]:
        if distance[i] == -1:
            q.append(i)
            distance[i] = distance[v]+1

for i in range(1, N+1):
    if distance[i] == K:
        print(i)

if K not in distance:
    print(-1)
