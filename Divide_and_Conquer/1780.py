import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

cnt_minus = 0
cnt_zero = 0
cnt_one = 0


def solution(x, y, n):
    global cnt_minus
    global cnt_zero
    global cnt_one

    total = set()
    for i in range(x, x+n):
        total.update(arr[i][y:y+n])
    if len(total) == 1:
        if "0" in total:
            cnt_zero += 1
            return
        elif "1" in total:
            cnt_one += 1
            return
        elif "-1" in total:
            cnt_minus += 1
            return

    solution(x, y, n//3)
    solution(x, y+(n//3), n//3)
    solution(x, y+(n//3)*2, n//3)
    solution(x+(n//3), y, n//3)
    solution(x+(n//3), y+(n//3), n//3)
    solution(x+(n//3), y+(n//3)*2, n//3)
    solution(x+(n//3)*2, y, n//3)
    solution(x+(n//3)*2, y+(n//3), n//3)
    solution(x+(n//3)*2, y+(n//3)*2, n//3)


solution(0, 0, n)
print(cnt_minus)
print(cnt_zero)
print(cnt_one)
