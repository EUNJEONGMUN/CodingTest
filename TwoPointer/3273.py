import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

left, right, cnt = 0, n-1, 0

while left < right:
    if arr[left]+arr[right] == x:
        cnt += 1
        left += 1
        right -= 1
    elif arr[left]+arr[right] > x:
        right -= 1
    else:
        left += 1

print(cnt)
