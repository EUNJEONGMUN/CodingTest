from collections import deque


def solution(game_board, table):
    N, M = len(game_board), len(game_board[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def check_range(x, y):
        if x >= 0 and y >= 0 and x < N and y < M:
            return True
        return False

    def bfs(arr, x, y, flag):
        # flag가 아닌 곳을 탐색하여 flag로 바꾸어줌
        q = deque()
        arr[x][y] = flag
        blank = set()
        blank.add((x, y))
        q.append((x, y))

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if check_range(nx, ny) and arr[nx][ny] != flag:
                    arr[nx][ny] = flag
                    blank.add((nx, ny))
                    q.append((nx, ny))
        return sorted(list(blank))

    def get_blanks(arr, flag):
        # 블럭을 모아 반환
        blanks = []
        for i in range(N):
            for j in range(M):
                if arr[i][j] != flag:
                    blanks.append(bfs(arr, i, j, flag))

        return blanks

    game_board_blank = get_blanks([g[:] for g in game_board], 1)
    answer = 0
    check_index_game_board = []  # 채운 곳의 인덱스 저장
    for _ in range(4):
        table_blank = get_blanks([t[:] for t in table], 0)
        check_index_table = []  # 채운 블록 인덱스 저장
        for i, g in enumerate(game_board_blank):
            if i in check_index_game_board:
                continue
            for j, t in enumerate(table_blank):
                if j in check_index_table:
                    continue
                if len(g) != len(t):
                    continue
                diff_x, diff_y = g[0][0]-t[0][0], g[0][1]-t[0][1]
                temp = list((s[0]+diff_x, s[1]+diff_y) for s in t)
                if g == temp:
                    answer += len(temp)
                    check_index_game_board.append(i)
                    check_index_table.append(j)
                    for a, b in t:
                        table[a][b] = 0
                    break

        table = list(map(list, zip(*table[::-1])))

    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [
      [1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]],
      [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
print(solution([[1, 1, 0, 0, 1, 1], [0, 0, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1]], [
      [1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1]]))
