# 최고의 33위치

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n-2):
    for j in range(n-2):
        res = max(res, sum(arr[i][j:j+3]) +
                  sum(arr[i+1][j:j+3])+sum(arr[i+2][j:j+3]))
print(res)
