import sys
from itertools import combinations
imput = sys.stdin.readline
n, m, d = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
arr = [b[:] for b in table]


def calculate_dist(a, b, x, y):
    return abs(a-x)+abs(b-y)


def calculate_enemy():
    res = 0
    for i in arr:
        res += sum(i)
    return res


def solution(x, y, z):
    cnt = 0
    one = []
    two = []
    three = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                one_dist = calculate_dist(i, j, n, x)
                two_dist = calculate_dist(i, j, n, y)
                three_dist = calculate_dist(i, j, n, z)
                if one_dist <= d:
                    one.append((one_dist, i, j))
                if two_dist <= d:
                    two.append((two_dist, i, j))
                if three_dist <= d:
                    three.append((three_dist, i, j))
    if one:
        one.sort(key=lambda x: (x[0], x[2]))
        if arr[one[0][1]][one[0][2]] == 1:
            cnt += 1
            arr[one[0][1]][one[0][2]] = 0
    if two:
        two.sort(key=lambda x: (x[0], x[2]))
        if arr[two[0][1]][two[0][2]] == 1:
            cnt += 1
            arr[two[0][1]][two[0][2]] = 0
    if three:
        three.sort(key=lambda x: (x[0], x[2]))
        if arr[three[0][1]][three[0][2]] == 1:
            cnt += 1
            arr[three[0][1]][three[0][2]] = 0
    return cnt


def move():
    arr[n-1] = [0]*m
    for i in range(n-2, -1, -1):
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] = 0
                arr[i+1][j] = 1


archer = list(combinations(range(m), 3))
res = 0
for x, y, z in archer:
    cnt_sum = 0
    while calculate_enemy() != 0:
        cnt_sum += solution(x, y, z)
        move()

    res = max(res, cnt_sum)
    arr = [b[:] for b in table]
print(res)
