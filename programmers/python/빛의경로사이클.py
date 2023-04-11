def solution(grid):
    N, M = len(grid), len(grid[0])
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    matrix = [[[0]*4 for _ in range(M)] for _ in range(N)]

    def cycle(x, y, direction):
        count = 0
        while matrix[x][y][direction] != 1:
            matrix[x][y][direction] = 1
            count += 1
            if grid[x][y] == "L":
                direction = (direction-1) % 4
            elif grid[x][y] == "R":
                direction = (direction+1) % 4

            x, y = (x+dx[direction]) % N, (y+dy[direction]) % M
        return count

    answer = []
    for x in range(N):
        for y in range(M):
            for i in range(4):
                if matrix[x][y][i] == 0:
                    ans = cycle(x, y, i)
                    if ans:
                        answer.append(ans)

    return sorted(answer)


print(solution(["SL", "LR"]))  # 16
print(solution(["S", "S"]))  # 1 1 1 1 2 2
print(solution([["R", "R"]]))  # 4 4
print(solution(["RLS", "SLR"]))  # 12 12
print(solution([["SS", "SS"]]))  # 1 1 1 1 2 2
