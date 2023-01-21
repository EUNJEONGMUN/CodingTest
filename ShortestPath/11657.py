import sys
input = sys.stdin.readline
INF = int(1e13)
n, m = map(int, input().split())
distance = [INF]*(n+1)

edges = [list(map(int, input().split())) for _ in range(m)]


def bellman_ford():
    distance[1] = 0

    for i in range(n):

        for start, end, cost in edges:
            if distance[start] != INF and distance[end] > distance[start]+cost:
                distance[end] = distance[start]+cost
                if i == n-1:
                    return True
    return False


infinite = bellman_ford()
if infinite:
    print(-1)
else:
    for d in distance[2:]:
        if d == INF:
            print(-1)
        else:
            print(d)
