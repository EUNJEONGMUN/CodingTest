import heapq
INF = int(1e9)


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    gates = set(gates)
    summits = set(summits)
    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))

    distance = [INF]*(n+1)

    def dijkstra():
        q = []
        for gate in gates:
            heapq.heappush(q, (0, gate))
            distance[gate] = 0

        while q:
            dist, now = heapq.heappop(q)
            # 정상이거나, 이미 방문한 노드라면 pass
            if now in summits or distance[now] < dist:
                continue
            for node, cost in graph[now]:
                if node in gates:
                    continue
                max_val = max(dist, cost)
                if distance[node] > max_val:
                    distance[node] = max_val
                    heapq.heappush(q, (max_val, node))

    dijkstra()
    res = [0, INF]
    for summit in summits:
        if res[1] > distance[summit]:
            res[0] = summit
            res[1] = distance[summit]
    return res


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [
      3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [
      2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [
      4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4],
      [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
