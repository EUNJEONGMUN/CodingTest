n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end, left, right = -1, -1, 0, 0
cnt = 0
while right < n:
    cnt += arr[right]

    if cnt < m:  # 합이 m보다 작다면
        right += 1  # 오른쪽 하나 늘리기
    else:
        while cnt > m:  # cnt가 m보다 크다면
            if cnt - arr[left] < m:  # 그리고 왼쪽을 줄였을 때도 m보다 크다면
                break
            cnt -= arr[left]  # 왼쪽줄이기
            left += 1

        if (end-start) > (right-left) or end == -1:  # 정답 최소 길이로 갱신
            start, end = left, right
            cnt -= arr[left]
            left += 1
        right += 1
if end == -1:
    print(0)
else:
    print(end-start+1)
