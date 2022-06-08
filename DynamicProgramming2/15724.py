import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

sum_arr = [[0]*(m+1) for _ in range(n+1)]

# 행 별로 더해주기
for i in range(1, n+1):
    for j in range(1, m+1):
        sum_arr[i][j] = sum_arr[i][j-1]+arr[i-1][j-1]

# 열 별로 더해주기
for j in range(1, m+1):
    for i in range(1, n+1):
        sum_arr[i][j] += sum_arr[i-1][j]


def solution(x1, y1, x2, y2):
    return sum_arr[x2][y2]-sum_arr[x2][y1-1]-sum_arr[x1-1][y2]+sum_arr[x1-1][y1-1]


k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(solution(x1, y1, x2, y2))
