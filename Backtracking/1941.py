board = [list(input()) for _ in range(5)]
answer = set()
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < 5 and y < 5:
        return True
    return False


def dfs(dasom, doyeon, log):
    global answer
    if dasom+doyeon == 7:
        answer.add(tuple(sorted(log)))
        return
    neighbor = []
    for x, y in log:
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if check_range(nx, ny) and (nx, ny) not in log:
                neighbor.append((nx, ny))
    for nx, ny in neighbor:
        if board[nx][ny] == "S":
            dfs(dasom+1, doyeon, log+[(nx, ny)])
        else:
            if doyeon < 3:
                dfs(dasom, doyeon+1, log+[(nx, ny)])


for i in range(5):
    for j in range(5):
        if board[i][j] == "S":
            dfs(1, 0, [(i, j)])
        else:
            dfs(0, 1, [(i, j)])

print(len(answer))
