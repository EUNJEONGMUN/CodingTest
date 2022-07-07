import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, list(input().strip()))) for _ in range(n)]


def check_same(x, y, k):
    res = 0
    for i in range(k):
        res += sum(grid[x+i][y:y+k])

    if res == 0 or res == k*k:  # 전체 합이 0또는 k*k 라면
        return True
    return False


def solution(x, y, k):
    if k == 1 or check_same(x, y, k):
        answer.append(grid[x][y])
        return
    else:
        answer.append("(")
        solution(x, y, k//2)
        solution(x, y+(k//2), k//2)
        solution(x+(k//2), y, k//2)
        solution(x+(k//2), y+(k//2), k//2)
        answer.append(")")


answer = []
solution(0, 0, n)

print("".join(list(map(str, answer))))
