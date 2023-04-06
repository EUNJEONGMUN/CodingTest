import heapq
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(n, x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


tc = 0
while True:
    tc += 1
    n = int(input())
    MAX = n*n*10
    if n == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(n)]
    rupee = [[MAX]*n for _ in range(n)]
    q = []

    rupee[0][0] = matrix[0][0]
    heapq.heappush(q, (matrix[0][0], 0, 0))

    while q:
        r, x, y = heapq.heappop(q)
        if r > rupee[x][y]:
            continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if check_range(n, nx, ny) and rupee[nx][ny] > r+matrix[nx][ny]:
                rupee[nx][ny] = r+matrix[nx][ny]
                heapq.heappush(q, (rupee[nx][ny], nx, ny))
    print("Problem %d: %d" % (tc, rupee[-1][-1]))
