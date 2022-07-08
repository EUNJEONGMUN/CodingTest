import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def solution(x, y, k):

    if k == 2:
        answer = [grid[x][y], grid[x][y+1], grid[x+1][y], grid[x+1][y+1]]
        answer.sort()
        return answer[-2]

    part1 = solution(x, y, k//2)
    part2 = solution(x, y+(k//2), k//2)
    part3 = solution(x+(k//2), y, k//2)
    part4 = solution(x+(k//2), y+(k//2), k//2)

    answer = [part1, part2, part3, part4]
    answer.sort()
    return answer[-2]


print(solution(0, 0, n))
