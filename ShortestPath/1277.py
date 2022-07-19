import heapq
import math
import sys
input = sys.stdin.readline
INF = int(1e9)
n, w = map(int, input().split())
m = float(input())
nodes = [()]+[tuple(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n+1)]


def calculate(a, b):  # 거리 계산
    x1, y1 = nodes[a]
    x2, y2 = nodes[b]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


for _ in range(w):  # 이미 연결 된 노드끼리는 cost 0
    a, b = map(int, input().split())
    graph[a].append([b, 0])
    graph[b].append([a, 0])

# 모든 노드 사이의 거리 구하기
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cost = calculate(i, j)
        if cost <= m:
            graph[i].append([j, cost])
            graph[j].append([i, cost])


def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[-1]


print(math.trunc(dijkstra(1)*1000))
