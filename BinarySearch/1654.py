import sys
input = sys.stdin.readline
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in arr:
        cnt += i//mid

    if n <= cnt:  # 개수가 많다면 길이늘리기
        start = mid+1
        answer = mid
    else:  # 개수가 적다면 길이 줄이기
        end = mid-1

print(end)
