import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0], -(x[1]-x[0])))
table = [0]*367

for start, end in arr:
    for i in range(start, end+1):
        table[i] += 1

res = 0
left = 1
for right in range(1, 367):
    if table[left] == 0:
        left = right
    else:
        if table[right] == 0:
            res += max(table[left:right])*(right-left)
            left = right
print(res)
