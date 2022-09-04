import sys
from collections import Counter
input = sys.stdin.readline


r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]


def calculate():
    new = []
    max_len = 0
    for row in arr:
        count = list(Counter(row).items())
        count.sort(key=lambda x: (x[1], x[0]))  # 정렬
        temp = []
        for x, y in count:
            if x == 0:  # 0은 세지 않음
                continue
            temp.extend([x, y])
        new.append(temp[:])
        max_len = max(max_len, len(temp))

    # 남은 공간 0으로
    for i in range(len(new)):
        if len(new[i]) < max_len:
            new[i].extend([0]*(max_len-len(new[i])))
        arr[i] = new[i][:]


time = 0
while time <= 100:
    if len(arr) >= r and len(arr[0]) >= c and arr[r-1][c-1] == k:
        # 찾으면 break
        print(time)
        break
    if len(arr) >= len(arr[0]):
        # R연산
        calculate()
    else:
        # C연산
        arr = list(map(list, zip(*arr)))  # 행과 열 바꾸기
        calculate()
        arr = list(map(list, zip(*arr)))  # 행과 열 바꾸기
    time += 1

else:
    print(-1)
