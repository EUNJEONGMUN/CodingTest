# 21610 마법사 상어와 비바라기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]


# def change(x):  # 좌표 바꾸기
#     if x < 0:
#         x = -x
#         return n-(x % n)
#     else:
#         div = x % n
#         return div if div != 0 else n


def move_cloud(direction, move):
    for i in range(len(cloud)):
        nx = (cloud[i][0] + dx[direction]*move) % n
        ny = (cloud[i][1] + dy[direction]*move) % n
        cloud[i] = [nx, ny]
        print("nx", nx, "ny", ny)
        grid[ny][ny] += 1
    print()


def water_double():
    for i in range(len(cloud)):
        x = cloud[i][0]
        y = cloud[i][1]
        count = 0
        for j in range(2, 9, 2):  # 대각선 방향으로 움직임
            nx = x + dx[j]
            ny = y + dy[j]

            if nx >= 0 and ny >= 0 and nx < n and ny < n and grid[nx][ny] > 0:
                count += 1
        grid[x][y] += count


def make_cloud():
    new_cloud = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and [i, j] not in cloud:
                new_cloud.append([i, j])
                grid[i][j] -= 2

    return new_cloud


for i in range(len(move)):
    # 1단계 : 구름 이동, 2단계 : 비내림
    move_cloud(move[i][0], move[i][1])

    # 3단계 : 구름이 사라짐

    # 4단계 : 물복사 버그 마법
    water_double()

    # 5단계 : 구름 생성
    cloud = make_cloud()

result = 0
for i in range(n):
    for j in range(n):
        result += grid[i][j]

print(result)
