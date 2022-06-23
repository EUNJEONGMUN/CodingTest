from collections import deque
import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < R and y < C:
        return True
    return False


def create():  # 폭탄 생성
    temp = deque([])

    while q:  # 원래 있던 폭탄들
        x, y, cnt = q.popleft()
        if grid[x][y] == "O":  # 터지지 않았다면 시간 증가
            temp.append((x, y, cnt+1))

    for i in range(R):  # 폭탄이 없는 부분에 폭탄 생성
        for j in range(C):
            if grid[i][j] == ".":
                grid[i][j] = "O"
                temp.append((i, j, 1))
    return temp


def boom():  # 폭탄 폭발
    temp = deque([])
    while q:
        x, y, cnt = q.popleft()
        if cnt == 1:
            temp.append((x, y, cnt+1))
        else:
            grid[x][y] = "."
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if check_range(nx, ny) and grid[nx][ny] == "O":
                    grid[nx][ny] = "."
    return temp


q = deque([])
for i in range(R):
    for j in range(C):
        if grid[i][j] == "O":
            q.append((i, j, 1))

for n in range(1, N):
    if n % 2 == 1:
        q = create()
    else:
        q = boom()

for i in range(R):
    print("".join(grid[i]))
