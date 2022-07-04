import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

grid = [[0]*101 for _ in range(101)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def solution(x, y, d, g):
    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)-1, -1, -1):
            temp.append((move[i]+1) % 4)
        move.extend(temp)

    grid[x][y] = 1
    for i in move:
        x += dx[i]
        y += dy[i]
        if grid[x][y] != 1:
            grid[x][y] = 1


def count():
    cnt = 0
    for i in range(100):
        for j in range(100):
            if grid[i][j] == 1 and grid[i+1][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j+1] == 1:
                cnt += 1
    return cnt


for y, x, d, g in arr:
    solution(x, y, d, g)
print(count())
