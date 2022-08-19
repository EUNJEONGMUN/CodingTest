# 행복한 수열의 개수

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0


def calculate():
    cnt = 0
    for i in range(n):
        temp = 1
        flag = False
        for j in range(1, n):
            if arr[i][j-1] == arr[i][j]:
                temp += 1
                if temp >= m:
                    flag = True
            else:
                temp = 1
        cnt += flag
    return cnt


if m == 1:
    print(n*2)
else:
    res += calculate()
    arr = list(map(list, zip(*arr)))  # 행과 열 바꾸기
    res += calculate()

    print(res)
