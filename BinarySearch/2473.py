from bisect import bisect_right
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()


res = sys.maxsize

for i in range(n-2):
    start, end = i + 1, n - 1  # i 값 이후
    while start < end:
        value = arr[i] + arr[start] + arr[end]
        if abs(value) < res:
            res = abs(value)
            result = [arr[i], arr[start], arr[end]]
        if value < 0:
            start += 1
        elif value > 0:
            end -= 1
        else:
            break

print(result[0], result[1], result[2])
