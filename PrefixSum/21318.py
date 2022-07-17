import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
table = [0]*n

for i in range(1, n):
    if arr[i-1] > arr[i]:
        table[i] = table[i-1]+1
    else:
        table[i] = table[i-1]

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(table[y-1]-table[x-1])
