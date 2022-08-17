import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def check_ragne(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def bfs(x, y):
    q = deque([(x, y, 0)])
    visited[x][y] = 0

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if check_ragne(nx, ny) and visited[nx][ny] == -1:
                visited[nx][ny] = cnt+1
                q.append((nx, ny, cnt+1))


start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start_x, start_y = i, j
        elif arr[i][j] == 0:  # 가지 못하는 곳 체크
            visited[i][j] = 0
bfs(start_x, start_y)
for i in visited:
    print(*i)


"""
for 문을 돌면서 2(시작점)를 찾을 때 arr[i][j]가 0인 부분도 찾아서 visited를 0으로 바꾸어 주어야 한다.
그 이유는 
input
2 2
2 0
0 0

output
0 0
0 0

위와 같은 예시가 들어왔을 때, 일반적인 bfs로 풀게 되면, 
0 0 
0 -1
이 나오게 된다. 

갈 수 없는 부분의 arr[i][j]=0 의 부분을 -1로 출력 하기 때문에 먼저 arr[i][j]=0인 부분을 확인해야 한다.
"""
