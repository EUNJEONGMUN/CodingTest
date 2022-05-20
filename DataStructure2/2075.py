import heapq
import sys

input = sys.stdin.readline
n = int(input())
# grid = [list(map(int,input().split())) for _ in range(n)]
q = []
for _ in range(n):
    line = list(map(int, input().split()))
    for l in line:
        heapq.heappush(q, -l)

result = 0
for i in range(n):
    result = heapq.heappop(q)
print(-result)
