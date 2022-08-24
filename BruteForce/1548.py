import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 1
for x in range(n-1):
    y = x+1
    for z in range(n-1, x, -1):
        if arr[x]+arr[y] > arr[z]:
            if z-x+1 > res:
                res = z-x+1
print(res)
