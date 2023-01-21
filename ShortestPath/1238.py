import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    dist = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, node = heapq.heappop(q)

        if (dist[node] < cost):
            continue

        for next_node, next_cost in graph[node]:
            if dist[node]+next_cost < dist[next_node]:
                dist[next_node] = dist[node]+next_cost
                heapq.heappush(q, (dist[node]+next_cost, next_node))
    print(start, dist)
    return dist[:]


# X번에서 다른 번호
distance = dijkstra(x)

# 다른 번호에서 X번
for i in range(1, n+1):
    if i == x:
        continue

    back_distance = dijkstra(i)
    distance[i] += back_distance[x]

print(max(distance[1:]))
