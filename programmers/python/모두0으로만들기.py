import sys
sys.setrecursionlimit(100000)


def solution(values, edges):
    graph = [[] for _ in range(len(values))]
    visited = [False]*len(values)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    count = []

    def dfs(node):
        visited[node] = True
        for next_node in graph[node]:
            if not visited[next_node]:
                values[node] += dfs(next_node)
        diff = values[node]
        values[node] = 0
        count.append(abs(diff))
        return diff

    ans = dfs(0)
    if ans == 0:
        return (sum(count))
    else:
        return -1


print(solution([0, 1, 0], [[0, 1], [1, 2]]))  # -1
print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))  # 9
print(solution([-2, 8, -5, -5, -3, 0, 5, 2], [[0, 1],
      [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7]]))  # 17
