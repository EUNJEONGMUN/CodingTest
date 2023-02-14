import heapq
import sys
input = sys.stdin.readline

n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

INF = int(1e9)
COST, TOTAL_COST = 0, 1
cost = [[INF, 0] for _ in range(n+1)]


def can_go(total_cost, next_cost):
    if total_cost+next_cost <= c:
        return True
    return False


def solution(start, goal):
    q = []
    cost[start][COST] = 0
    heapq.heappush(q, (0, 0, start))

    while q:
        min_cost, total_cost, node = heapq.heappop(q)

        if min_cost > cost[node][COST] and total_cost > cost[node][TOTAL_COST]:
            continue

        for next_node, next_cost in graph[node]:
            if can_go(total_cost, next_cost):
                if cost[next_node][COST] > max(min_cost, next_cost):
                    cost[next_node][COST] = max(min_cost, next_cost)
                    cost[next_node][TOTAL_COST] = total_cost+next_cost
                    heapq.heappush(
                        q, [cost[next_node][COST], cost[next_node][TOTAL_COST], next_node])
    return cost[goal][COST]


answer = solution(a, b)
print(-1 if answer == INF else answer)
