import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0


def check_same(x, y, k):
    res = 0
    for i in range(k):
        res += sum(grid[x+i][y:y+k])

    if res == 0 or res == k*k:  # 전체 합이 0또는 k*k 라면
        return True
    return False


def solution(x, y, k):
    global white
    global blue
    if k == 1 or check_same(x, y, k):
        if grid[x][y] == 0:
            white += 1
        else:
            blue += 1
        return
    else:
        solution(x, y, k//2)
        solution(x, y+(k//2), k//2)
        solution(x+(k//2), y, k//2)
        solution(x+(k//2), y+(k//2), k//2)


solution(0, 0, n)

print(white)
print(blue)
