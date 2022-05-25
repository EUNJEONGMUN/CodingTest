from collections import deque


def bfs(graph, visited):

    parent = list(range(n+1))  # 부모 노드

    q = deque([1])
    visited[1] = True

    while q:
        node = q.popleft()

        for i in graph[node]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                parent[i] = node
    return parent


n = int(input())
graph = [[] for _ in range(n+1)]  # 그래프의 정보
visited = [False]*(n+1)  # 방문 여부


for _ in range(n-1):
    a, b = map(int, input().split())
    # 양방향 그래프
    graph[a].append(b)
    graph[b].append(a)


result = bfs(graph, visited)

for i in range(2, n+1):
    print(result[i])
