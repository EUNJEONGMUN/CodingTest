import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
A, B, C = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    distance = [INF]*(n+1)

    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, cost in graph[node]:
            if dist+cost < distance[next_node]:
                distance[next_node] = dist+cost
                heapq.heappush(q, (dist+cost, next_node))
    return distance


answer = [INF]*(n+1)

for i in [A, B, C]:
    dist = dijkstra(i)
    for i in range(n+1):
        answer[i] = min(dist[i], answer[i])
print(answer.index(max(answer[1:])))
