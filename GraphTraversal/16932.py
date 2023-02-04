from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

group = defaultdict(int)
group_num = 2


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 1
    arr[x][y] = group_num

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if check_range(nx, ny) and arr[nx][ny] == 1:
                q.append((nx, ny))
                count += 1
                arr[nx][ny] = group_num
    group[group_num] = count


def find_area(x, y):
    for value in area:
        if (x, y) in value:
            return value
    return set()


zero = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs(i, j)
            group_num += 1
        elif arr[i][j] == 0:
            zero.append((i, j))


answer = -1
for x, y in zero:
    temp = set()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if check_range(nx, ny) and arr[nx][ny] != 0:
            temp.add(arr[nx][ny])
    temp_sum = 0
    for t in temp:
        temp_sum += group[t]
    answer = max(answer, temp_sum+1)

print(answer)
