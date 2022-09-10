import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0


def get_sum(k):
    return k*k+(k+1)*(k+1)


def calculate(x, y, k):
    coin = 0
    for i in range(n):
        for j in range(n):
            if abs(i-x)+abs(j-y) <= k and arr[i][j] == 1:
                coin += 1
    return coin


for i in range(n):
    for j in range(n):
        for k in range(2*n-1):
            num = calculate(i, j, k)

            if num*m >= get_sum(k):
                res = max(res, num)
print(res)
