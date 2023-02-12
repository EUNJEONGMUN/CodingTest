import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
link = [[] for _ in range(n+1)]
bridges = dict()
INF = int(1e9)

for _ in range(m):
    x, y, z = map(int, input().split())
    if (x, y) not in bridges:
        bridges[(x, y)] = z
        bridges[(y, x)] = z
        link[x].append(y)
        link[y].append(x)
    else:
        if bridges[(x, y)] < z:
            bridges[(x, y)] = z
            bridges[(y, x)] = z

A, B = map(int, input().split())
weights = [0]*(n+1)

q = []
heapq.heappush(q, (-INF, A))
weights[A] = INF

while q:
    weight, node = heapq.heappop(q)
    weight *= -1
    if weights[node] > weight or node == B:
        continue

    for next_node in link[node]:
        min_value = min(weight, bridges[(node, next_node)])
        if min_value > weights[next_node]:
            weights[next_node] = min_value
            heapq.heappush(q, (-min_value, next_node))
print(weights[B])
