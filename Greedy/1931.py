n = int(input())
meet = [tuple(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간순 정렬, 끝나는 시간이 같다면 빨리 시작하는 순.
cnt = 1
time = meet[0][1]
for i in range(1, n):
    start, end = meet[i]
    if time <= start:
        cnt += 1
        time = end
print(cnt)
