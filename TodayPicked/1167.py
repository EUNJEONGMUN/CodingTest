import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v = int(input())
tree = [[] for _ in range(v+1)]
visited = [-1]*(v+1)
for _ in range(v):
    numbers = list(map(int, input().split()))
    for j in range(1, len(numbers)-1, 2):
        tree[numbers[0]].append((numbers[j], numbers[j+1]))


def dfs(x, cost):
    for y, c in tree[x]:
        if visited[y] == -1:
            visited[y] = cost+c
            dfs(y, cost+c)


visited[1] = 0
dfs(1, 0)
start = visited.index(max(visited))  # 1번 노드에서 제일 먼 노드를 찾는다.
visited = [-1] * (v+1)
visited[start] = 0
dfs(start, 0)  # 1번 노드부터 가장 먼 노드에서 다시 제일 먼 노드를 찾는다.

print(max(visited))
