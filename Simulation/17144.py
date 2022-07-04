import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())  # RxC 격자판, T초가 지난 후 미세먼지 양
grid = [list(map(int, input().split())) for _ in range(R)]
robot1, robot2 = 0, 0

# 공기청정기 위치 찾기
for i in range(R-1):
    if grid[i][0] == -1:
        robot1 = i
        robot2 = i+1
        break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 범위 확인
def check_range(x, y):
    if x >= 0 and y >= 0 and x < R and y < C:
        return True
    return False

# 미세먼지 확산


def spread_pm25(second):

    pm25 = [[0]*C for _ in range(R)]

    for x in range(R):
        for y in range(C):

            # grid가 5이상일 때 -> -1이면 로봇이고, 5이하이면 확산 수치 0
            if grid[x][y] >= 5:
                count = 0
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]

                    if check_range(nx, ny) and grid[nx][ny] != -1:
                        # 범위 안에 들고, 공기 청정기가 아닐 때
                        pm25[nx][ny] += grid[x][y]//5
                        count += 1

                # grid 갱신
                grid[x][y] = grid[x][y]-(grid[x][y]//5)*count

    for x in range(R):
        for y in range(C):
            grid[x][y] += pm25[x][y]  # 확산 된 값을 더해줌

# 공기청정기 작동


def spread_robot(second):

    # 위에 있는 공기청정기
    # 위->아래
    for i in range(robot1-2, -1, -1):
        grid[i+1][0] = grid[i][0]
    grid[robot1][0] = -1

    # 오른쪽 -> 왼쪽
    for i in range(1, C):
        grid[0][i-1] = grid[0][i]

    # 아래 -> 위
    for i in range(1, robot1+1):
        grid[i-1][-1] = grid[i][-1]

    # 왼쪽 -> 오른쪽
    for i in range(C-2, 0, -1):
        grid[robot1][i+1] = grid[robot1][i]
    grid[robot1][1] = 0

    # 아래에 있는 공기청정기

    # 아래 -> 위
    for i in range(robot2+2, R):
        grid[i-1][0] = grid[i][0]

    # 오른쪽 -> 왼쪽
    for i in range(1, C):
        grid[-1][i-1] = grid[-1][i]

    # 위 -> 아래
    for i in range(R-2, robot2-1, -1):
        grid[i+1][-1] = grid[i][-1]

    # 왼쪽 -> 위
    for i in range(C-2, 0, -1):
        grid[robot2][i+1] = grid[robot2][i]
    grid[robot2][1] = 0


for i in range(1, T+1):
    spread_pm25(i)  # 미세먼지 확산
    spread_robot(i)  # 공기청정기 작동

result = 0
for i in range(R):
    for j in range(C):
        result += grid[i][j]

print(result+2)  # 공기청정기가 -1이기 때문에 +2를 해줌
