import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
left, right, cnt = 0, 0, 0

temp = arr[0]
while left < n:
    if temp == m:  # m과 같으면
        cnt += 1  # cnt 증가
        temp -= arr[left]  # 왼쪽 하나 줄여서 다시 탐색
        left += 1

    elif temp < m:  # temp가 m보다 작다면 더 늘려야 함.
        right += 1  # right 1 증가
        if right == n:
            break
        temp += arr[right]
    else:  # temp가 m보다 크다면, 줄어야 함.
        temp -= arr[left]  # left 감소
        left += 1

print(cnt)
