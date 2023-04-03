import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
while True:
    if matrix[r][c] == 0:
        answer += 1
        matrix[r][c] = 2
    for _ in range(4):
        d = (d-1) % 4
        nx, ny = r+dx[d], c+dy[d]
        if matrix[nx][ny] == 0:
            r, c = nx, ny
            break
    else:
        # 빈 칸이 없는 경우
        nx, ny = r+(dx[d]*(-1)), c+(dy[d]*(-1))
        if matrix[nx][ny] == 1:
            break
        r, c = nx, ny

print(answer)
