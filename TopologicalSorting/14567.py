import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

answer = [1]*(n+1)

for i in range(1, n+1):
    for j in graph[i]:
        answer[j] = max(answer[j], answer[i]+1)

print(*answer[1:])
