import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
waters = sorted(list(map(int, input().split())))
q = deque([])
visited = dict()
res = 0
house = 0

for water in waters:
    visited[water] = 1
    q.append((water, 0))

while q and house < k:
    x, cnt = q.popleft()

    for i in [-1, 1]:
        nx = x+i
        if nx not in visited:
            visited[nx] = 1
            res += cnt+1
            house += 1
            q.append((nx, cnt+1))
        if house == k:
            break

print(res)

"""
배열로 만들어서 풀었더니 메모리 초과가 발생했다.
dict로 만들어 풀었더니 훨씬 간편하고 쉽게 풀렸다.

"""
