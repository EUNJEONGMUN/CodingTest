import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(m)]
graph.sort()
answer = [1]*(n+1)

for a, b in graph:
    if answer[b] < answer[a]+1:
        answer[b] = answer[a]+1

print(*answer[1:])
