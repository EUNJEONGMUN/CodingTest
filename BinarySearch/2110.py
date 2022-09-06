import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
start = 1
end = arr[n-1]-arr[0]
res = 0
while start <= end:
    mid = (start+end)//2

    cnt = 1
    last = arr[0]
    for a in arr[1:]:
        if a-last >= mid:
            cnt += 1
            last = a
            if cnt == c:  # 개수가 같다면, break
                break

    if cnt >= c:
        if cnt == c:
            res = max(res, mid)
        start = mid+1
    else:
        end = mid-1

print(res)
