from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

INF = int(10e9)


def check_range(z, x, y):
    if x >= 0 and y >= 0 and z >= 0 and x < R and y < C and z < L:
        return True
    return False


def find_start():
    for z in range(L):
        for x in range(R):
            for y in range(C):
                if building[z][x][y] == 'S':
                    return (z, x, y)


def bfs(start):
    q = deque()
    distance[start[0]][start[1]][start[2]] = 0
    q.append((0, start))

    while q:
        dist, p = q.popleft()
        z, x, y = p
        for i in range(6):
            nz, nx, ny = z+dz[i], x+dx[i], y+dy[i]
            if check_range(nz, nx, ny):
                if building[nz][nx][ny] == '.' and distance[nz][nx][ny] == INF:
                    distance[nz][nx][ny] = dist+1
                    q.append((dist+1, (nz, nx, ny)))
                elif building[nz][nx][ny] == 'E':
                    return dist+1
    return -1


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    building = []
    distance = [[[INF]*C for _ in range(R)] for _ in range(L)]

    for _ in range(L):
        floor = list(list(input().strip()) for _ in range(R))
        building.append(floor)
        input()

    start = find_start()
    ans = bfs(start)

    if ans == -1:
        print("Trapped!")
    else:
        print("Escaped in {} minute(s).".format(ans))
