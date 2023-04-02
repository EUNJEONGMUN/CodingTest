from collections import deque


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    maps = [list(m) for m in maps]
    answer = []

    def check_range(x, y):
        if x >= 0 and y >= 0 and x < len(maps) and y < len(maps[0]):
            return True
        return False

    def bfs(x, y):
        q = deque()
        total = int(maps[x][y])
        q.append((x, y))
        maps[x][y] = "X"

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if check_range(nx, ny) and maps[nx][ny] != "X":
                    total += int(maps[nx][ny])
                    maps[nx][ny] = "X"
                    q.append((nx, ny))
        return total

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X":
                answer.append(bfs(i, j))
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
