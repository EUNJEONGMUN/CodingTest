import sys
input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
sum_total = 0
for i in people:
    sum_total += sum(i)


def div(x, y, d1, d2):
    arr = [[0]*n for _ in range(n)]

    # 1번 선거구
    for i in range(d1+1):
        arr[x+i][y-i] = 5

    # 2번 선거구
    for i in range(d2+1):
        arr[x+i][y+i] = 5

    # 3번 선거구
    for i in range(d2+1):
        arr[x+d1+i][y-d1+i] = 5

    # 4번 선거구
    for i in range(d1+1):
        arr[x+d2+i][y+d2-i] = 5

    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0

    # 1번 구역 계산
    r, c = 0, 0
    while r < x+d1:
        if arr[r][c] == 5 or c > y:
            r += 1
            c = 0
        else:
            sum1 += people[r][c]
            c += 1
    # 2번 구역 계산
    r, c = 0, n-1
    while r <= x+d2:
        if arr[r][c] == 5 or c == y:
            r += 1
            c = n-1
        else:
            sum2 += people[r][c]
            c -= 1
    # 3번 구역 계산
    r, c = x+d1, 0
    while r < n:
        if arr[r][c] == 5 or c >= y-d1+d2:
            r += 1
            c = 0
        else:
            sum3 += people[r][c]
            c += 1

    # 4번 구역 계산
    r, c = x+d2+1, n-1
    while r < n:
        if arr[r][c] == 5 or c < y-d1+d2:
            r += 1
            c = n-1
        else:
            sum4 += people[r][c]
            c -= 1
    sum5 = sum_total-(sum1+sum2+sum3+sum4)

    return max(sum1, sum2, sum3, sum4, sum5)-min(sum1, sum2, sum3, sum4, sum5)


answer = sum_total
for x in range(n-2):
    for y in range(1, n-1):
        for d1 in range(1, n-x-1):
            for d2 in range(1, n-x-1):
                if x+d1+d2 < n and y-d1 >= 0 and y+d2 < n:
                    # (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N) 를 만족시키게 하기
                    answer = min(answer, div(x, y, d1, d2))
                    # print("x, y:", x, y, " d1, d2:", d1, d2, "answer:", answer)
print(answer)
