n = int(input())

row = [0] * n
answer = 0


def check(x, y):
    # x 행 y열에 놓아도 괜찮은가?
    for i in range(x):
        if row[i] == y or abs(i-x) == abs(row[i]-y):
            return False
    return True


def bt(x):
    global answer

    if x == n:
        answer += 1
        return

    for y in range(n):
        if check(x, y):
            print(x, y)
            row[x] = y
            bt(x+1)


bt(0)
print(answer)
