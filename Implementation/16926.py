import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(x, y, height, width):
    q = deque([])

    for i in range(y, y+width):
        q.append(arr[x][i])
    for i in range(x+1, x+height):
        q.append(arr[i][y+width-1])
    for i in range(y+width-2, y-1, -1):
        q.append(arr[x+height-1][i])
    for i in range(x+height-2, x, -1):
        q.append(arr[i][y])

    q.rotate(-r)  # 양수를 넣으면 r 칸 오른쪽으로, 음수를 넣으면 r 칸 왼쪽으로

    for i in range(y, y+width):
        arr[x][i] = q.popleft()
    for i in range(x+1, x+height):
        arr[i][y+width-1] = q.popleft()
    for i in range(y+width-2, y-1, -1):
        arr[x+height-1][i] = q.popleft()
    for i in range(x+height-2, x, -1):
        arr[i][y] = q.popleft()


x, y = 0, 0
while True:
    if n == 0 or m == 0:
        break
    turn(x, y, n, m)
    x += 1
    y += 1
    n -= 2
    m -= 2

for i in arr:
    print(*i)
