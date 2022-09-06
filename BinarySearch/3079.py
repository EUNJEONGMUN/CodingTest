import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

start = 0
end = answer = max(arr)*m+1

while start <= end:
    mid = (start+end)//2

    people = 0

    for i in arr:
        people += mid//i
    # print(mid, "=", start, end, "people:", people)
    if people >= m:
        end = mid-1
        answer = min(mid, answer)
    else:
        start = mid+1
print(answer)
