# 행성 터널

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
graph = [[i]+list(map(int, input().split())) for i in range(n)]
parent = [i for i in range(n)]
distance = []
res = 0

for i in [1, 2, 3]:
    graph.sort(key=lambda x: x[i])

    for k in range(n-1):
        dist = abs(graph[k][i]-graph[k+1][i])
        distance.append((graph[k][0], graph[k+1][0], dist))
distance.sort(key=lambda x: x[2])


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for a, b, cost in distance:
    if find(a) != find(b):
        union(a, b)
        res += cost
print(res)
