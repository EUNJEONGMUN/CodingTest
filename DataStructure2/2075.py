# import heapq
# import sys

# input = sys.stdin.readline
# n = int(input())
# q = []
# for _ in range(n):
#     line = list(map(int, input().split()))
#     for l in line:
#         heapq.heappush(q, -l)

# result = 0
# for i in range(n):
#     result = heapq.heappop(q)
# print(-result)

import heapq
import sys

input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    line = list(map(int, input().split()))
    if not q:  # 큐에 아무 것도 없다면 추가
        for l in line:
            heapq.heappush(q, l)
    else:  # 큐에 있다면
        for i in line:
            if q[0] < i:  # 큐에서 가장 작은 원소와, i와 비교하여 i가 더 크다면 가장 작은 원소를 빼고 삽입.
                heapq.heappop(q)
                heapq.heappush(q, i)

print(q[0])
