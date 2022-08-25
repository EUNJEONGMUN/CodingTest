import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
res = -1


def check(n):
    return math.sqrt(n) - int(math.sqrt(n)) == 0


# 시작점
for a in range(n):
    for b in range(m):

        # 증가폭
        for i in range(-n, n):
            for j in range(-m, m):
                if i == 0 and j == 0:
                    continue
                nx = a
                ny = b
                num = ""

                while 0 <= nx < n and 0 <= ny < m:
                    num += arr[nx][ny]
                    nx += i
                    ny += j
                    if check(int(num)):
                        res = max(res, int(num))
print(res)
