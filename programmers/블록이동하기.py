from collections import deque


def get_next_pos(pos, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    next_pos = []  # 이동 가능한 모든 경우의 수
    pos = list(pos)

    pos1x, pos1y, pos2x, pos2y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    for i in range(4):  # 상하좌우 이동하는 경우
        pos1nx, pos1ny, pos2nx, pos2ny = pos1x + \
            dx[i], pos1y+dy[i], pos2x+dx[i], pos2y+dy[i]

        if board[pos1nx][pos1ny] == 0 and board[pos2nx][pos2ny] == 0:  # 이동할 수 있다면
            next_pos.append({(pos1nx, pos1ny), (pos2nx, pos2ny)})

    # 회전 가능한 경우
    if pos1x == pos2x:
        # 로봇이 가로로 놓여있는 경우
        for i in [-1, 1]:
            if board[pos1x+i][pos1y] == 0 and board[pos2x+i][pos2y] == 0:
                next_pos.append({(pos1x, pos1y), (pos1x+i, pos1y)})
                next_pos.append({(pos2x, pos2y), (pos2x+i, pos2y)})
    else:
        # 로봇이 세로로 놓여있는 경우
        for i in [-1, 1]:
            if board[pos1x][pos1y+i] == 0 and board[pos2x][pos2y+i] == 0:
                next_pos.append({(pos1x, pos1y), (pos1x, pos1y+i)})
                next_pos.append({(pos2x, pos2y), (pos2x, pos2y+i)})
    return next_pos


def solution(board):
    N = len(board)
    new_board = [[1]*(N+2) for _ in range(N+2)]

    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]

    q = deque([])

    visited = []
    start = {(1, 1), (1, 2)}
    q.append((start, 0))
    visited.append(start)

    while q:
        pos, cost = q.popleft()

        # 끝까지 도달했다면
        if (N, N) in pos:
            return cost

        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
      0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
