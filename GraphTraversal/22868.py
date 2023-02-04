from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
graph = [sorted(i) for i in graph]
S, E = map(int, input().split())

go = []
back = []


def solution(start, end, visited):
    q = deque()
    q.append((0, start, []))
    visited.add(start)

    while q:
        dist, x, trace = q.popleft()
        if x == end:
            return trace
        for i in graph[x]:
            if i not in visited:
                visited.add(i)
                q.append((dist+1, i, trace+[i]))


go = solution(S, E, set())
back = solution(E, S, set(go))
print(len(go)+len(back))
