from collections import deque


def solution(n, edges):
    tree = [[] for _ in range(n+1)]
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    def bfs(node):
        distance = [-1]*(n+1)
        distance[node] = 0
        q = deque()
        q.append(node)

        while q:
            node = q.popleft()

            for next_node in tree[node]:
                if distance[next_node] == -1:
                    distance[next_node] = distance[node]+1
                    q.append(next_node)
        return distance[:]
    dist = bfs(1)
    node = dist.index(max(dist))
    dist2 = sorted(bfs(node))
    if dist.count(max(dist)) > 1:
        return dist2[-1]
    else:
        return dist2[-2]


print(solution(3, [[1, 2], [2, 3]]))
print(solution(4, [[1, 2], [2, 3], [2, 4]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(5, [[1, 5], [2, 5], [3, 5], [4, 5]]))
print(solution(11, [[1, 2], [2, 3], [3, 4], [4, 5], [
      5, 6], [6, 7], [7, 8], [8, 9], [6, 10], [10, 11]]))
