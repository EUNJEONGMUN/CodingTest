import heapq
import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
q = []
for num in nums:
    if num == 0:
        if q:
            answer = heapq.heappop(q)
            print(answer[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(num), num))
