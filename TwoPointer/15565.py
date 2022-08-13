import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left, right, start, end = 0, 0, 0, 0
cnt = 0

while right < n:
    if arr[right] == 1:  # right가 가리키는 게 라이언이라면
        cnt += 1  # cnt 증가
        if cnt == k:  # 라이언이 k개를 만족시켰다면
            while arr[left] != 1:  # 왼쪽에서 어피치 제거하기
                left += 1
            if end-start > right-left or end == 0:  # 길이 갱신
                start, end = left, right
            left += 1  # 길이 갱신 했으므로 왼쪽 포인터 증가
            # 라이언 감소 (위의 while 문에서 왼쪽어피치를 제거 했으므로 left에 해당 하는 것은 라이언일 것임)
            cnt -= 1
        right += 1
    else:
        right += 1

if end == 0:  # end가 0이라면 아직 갱신된 적이 없는 것이므로
    print(-1)
else:
    print(end-start+1)
