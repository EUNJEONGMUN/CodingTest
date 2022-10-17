import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c*2))
    graph[b-1].append((a-1, c*2))


wolf = [[INF]*n for _ in range(2)]
fox = [INF]*n


def move_fox():

    q = [(0, 0)]
    fox[0] = 0

    while q:
        dist, node = heapq.heappop(q)

        if dist > fox[node]:
            continue

        for next_node, cost in graph[node]:
            temp = dist+cost
            if temp < fox[next_node]:
                fox[next_node] = temp
                heapq.heappush(q, (temp, next_node))


FAST = 0
SLOW = 1


def move_wolf():
    q = [(0, 0, SLOW)]
    wolf[SLOW][0] = 0

    while q:
        dist, node, speed = heapq.heappop(q)

        if speed == SLOW:
            # 이제 빠르게 갈 차례
            if dist > wolf[SLOW][node]:
                continue
            for next_node, cost in graph[node]:
                temp = dist+cost//2
                if temp < wolf[FAST][next_node]:
                    wolf[FAST][next_node] = temp
                    heapq.heappush(q, (temp, next_node, FAST))
        else:
            # 이제 느리게 갈 차례
            if dist > wolf[FAST][node]:
                continue
            for next_node, cost in graph[node]:
                temp = dist+cost*2
                if temp < wolf[SLOW][next_node]:
                    wolf[SLOW][next_node] = temp
                    heapq.heappush(q, (temp, next_node, SLOW))


move_fox()
move_wolf()
cnt = 0
for i in range(n):
    if fox[i] < min(wolf[SLOW][i], wolf[FAST][i]):
        cnt += 1
print(cnt)
