n, m = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False


def bf(board, ax, ay, bx, by):
    # "나" -> ax, ay

    is_finished = True  # 이 턴에서 이동할 수 있는 곳이 없어 끝나는가?
    for i in range(4):
        nx = ax+dx[i]
        ny = ay+dy[i]
        if not check_range(nx, ny) or board[nx][ny] == 0:
            continue
        is_finished = False  # 이동가능하다!

    if is_finished:  # 이동 할 수 없다면
        return [False, 0]  # 지므로 False 반환

    if ax == bx and ay == by:  # 현재 두 유저가 같은 칸에 있다면, 내가 이김
        return [True, 1]  # 이기므로 True 반환

    board[ax][ay] = 0  # 이동 시작

    can_win = False  # 이길 수 있는지 확인
    min_turn = int(1e9)
    max_turn = 0

    for i in range(4):
        nx, ny = ax+dx[i], ay+dy[i]
        if not check_range(nx, ny) or board[nx][ny] == 0:
            continue
        result = bf(board, bx, by, nx, ny)
        if result[0] == False:  # 만약 상대방이 진다면
            can_win = True  # 내가 이김
            min_turn = min(min_turn, result[1])  # 내가 이겼을 경우는, 가장 최단 경우를 선택해야 함
        else:  # 만약 상대방이 이긴다면
            max_turn = max(max_turn, result[1])  # 즉, 내가 졌을 경우는 가장 오랫동안 이동해야 함.

    board[ax][ay] = 1  # 원상복귀
    if can_win:  # 내가 이길 수 있다면
        return [True, min_turn+1]  # 가장 적은 경우 +1
    else:  # 내가 진다면
        return [False, max_turn+1]  # 가장 많은 경우 +1


def solution(board, aloc, bloc):
    global n, m
    n = len(board)
    m = len(board[0])
    return bf(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
