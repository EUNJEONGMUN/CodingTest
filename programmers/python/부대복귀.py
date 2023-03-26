import heapq
INF = int(1e9)


def solution(n, roads, sources, destination):

    graph = [[] for _ in range(n+1)]
    distance = [INF]*(n+1)

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    q = []
    distance[destination] = 0
    heapq.heappush(q, (0, destination))

    while q:
        dist, node = heapq.heappop(q)

        if dist > distance[node]:
            continue

        for next_node in graph[node]:
            if distance[next_node] > dist+1:
                distance[next_node] = dist+1
                heapq.heappush(q, (dist+1, next_node))
    answer = []
    for source in sources:
        if distance[source] == INF:
            answer.append(-1)
        else:
            answer.append(distance[source])
    return answer
