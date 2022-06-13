# import sys
# from collections import defaultdict
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


# def dfs(start):
#     visited[start] = True
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(i)

# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[b].append(a)

# result = defaultdict(list)
# max_count = 0

# for i in range(1, n+1):
#     visited = [False]*(n+1)
#     dfs(i)
#     result[sum(visited)].append(i)
# print(*sorted(result[max(result)]))


import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = [False]*(n+1)

    visited[start] = True
    q = deque([start])

    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return sum(visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


result = defaultdict(list)  # cnt가 key, 각 노드들이 value의 값으로 들어감.

for i in range(1, n+1):
    cnt = bfs(i)
    result[cnt].append(i)
print(*sorted(result[max(result)]))  # cnt가 가장 많은 노드들 정렬하여 출력
