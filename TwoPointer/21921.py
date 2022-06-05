import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

max_value = sum(arr[:x])  # 최댓값
value = sum(arr[:x])  # 매번 갱신될 value
left, right = 0, x
cnt = 1

while right < n:
    value = value - arr[left] + arr[right]  # left 빼고, right는 추가
    left += 1
    right += 1

    if value == max_value:
        cnt += 1

    elif value > max_value:
        max_value = value
        cnt = 1

if max_value == 0:
    print("SAD")
else:
    print(max_value)
    print(cnt)
