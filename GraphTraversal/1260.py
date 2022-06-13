import sys
from collections import deque
input = sys.stdin.readline


def dfs(start):
    visited[start] = False
    print(start, end=" ")
    for i in graph[start]:
        if visited[i]:
            dfs(i)


def bfs(start):
    visited[start] = True
    print(start, end=" ")
    q = deque([start])

    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                print(i, end=" ")
                q.append(i)


n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [True]*(n+1)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):  # 노드 번호가 작은 순서대로 방문해야 하므로 정렬
    graph[i].sort()

dfs(start)
print()
bfs(start)
