import sys
input = sys.stdin.readline

tc = int(input())


def turn_right(n, count, table):

    for _ in range(count):
        temp = []

        for i in range(n):
            temp.append(table[i][i])

        for i in range(n):
            prev = table[i][n//2]
            table[i][n//2] = temp[i]
            temp[i] = prev

        for i in range(n):
            prev = table[i][n-i-1]
            table[i][n-i-1] = temp[i]
            temp[i] = prev

        for i in range(n):
            prev = table[n//2][n-i-1]
            table[n//2][n-i-1] = temp[i]
            temp[i] = prev

        for i in range(n):
            table[n-i-1][n-i-1] = temp[i]


def turn_left(n, count, table):

    for _ in range(count):
        temp = []

        for i in range(n):
            temp.append(table[i][i])

        for i in range(n):
            prev = table[n//2][i]
            table[n//2][i] = temp[i]
            temp[i] = prev

        for i in range(n):
            prev = table[n-i-1][i]
            table[n-i-1][i] = temp[i]
            temp[i] = prev

        for i in range(n):
            prev = table[n-i-1][n//2]
            table[n-i-1][n//2] = temp[i]
            temp[i] = prev

        for i in range(n):
            table[n-i-1][n-i-1] = temp[i]


for _ in range(tc):
    n, d = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]

    if d < 0:
        turn_left(n, -d//45, table)
    else:
        turn_right(n, d//45, table)

    for i in table:
        print(*i)
