import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(n)]

# 입력 받은 리스트의 위, 아래, 좌, 우에 테두리를 씌워줄 역할을 할 큰 리스트를 만듦.
grid = [[0]*(m+2) for _ in range(n+2)]
for i in range(1, n+1):
    for j in range(1, m+1):
        grid[i][j] = temp[i-1][j-1]
visited = [[False]*(m+2) for _ in range(n+2)]

# 짝수행 -> 오른쪽 위, 오른쪽 아래, 윈쪽 위, 왼쪽 아래, 왼쪽, 오른쪽
dx_even = [-1, 1, -1, 1, 0, 0]
dy_even = [0, 0, -1, -1, -1, 1]

# 홀수행 -> 왼쪽 위, 왼쪽 아래, 오른쪽 위, 오른쪽 아래, 왼쪽, 오른쪽
dx_odd = [-1, 1, -1, 1, 0, 0]
dy_odd = [0, 0, 1, 1, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n+2 and y < m+2:
        return True
    return False


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(6):  # 6방향 탐색
            if x % 2 == 0:
                nx = x+dx_even[i]
                ny = y+dy_even[i]
            else:
                nx = x+dx_odd[i]
                ny = y+dy_odd[i]

            if check_range(nx, ny):
                if grid[nx][ny] == 1:  # 만약 벽과 만난다면
                    cnt += 1  # 카운트 증가
                elif grid[nx][ny] == 0 and not visited[nx][ny]:  # 벽이 아니고 아직 방문하지 않았다면 deque에 삽입
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return cnt


print(bfs(0, 0))
