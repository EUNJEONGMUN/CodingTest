a, b = map(int, input().split())

cnt = 0

while b != a and b > 0:
    if b % 10 == 1:  # 일의 자리가 1이면
        b //= 10  # 10으로 나눈 몫을 취함
        cnt += 1
    elif b % 2 == 0:  # 2로 나누어 떨어진다면
        b //= 2  # 2로 나눈 몫을 취함
        cnt += 1
    else:
        break

if a == b:
    print(cnt+1)
else:
    print(-1)
