from collections import deque
import sys
input = sys.stdin.readline

INVALID = "invalid"
VALID = "valid"

win_idx = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 가로
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 세로
    [0, 4, 8], [2, 4, 6]  # 대각선
]


def is_full(board):
    blank_count = board.count(".")
    if blank_count == 0:
        return True
    return False


def get_win_count(board, shape):
    visited = [False]*len(board)
    q = deque()
    count = 0

    for i in range(len(board)):
        if board[i] == shape and not visited[i]:
            q.append(i)
            visited[i] = True
            flag = False

            while q:
                node = q.popleft()

                for idx in win_idx:
                    if node in idx and (shape == board[idx[0]] == board[idx[1]] == board[idx[2]]):
                        flag = True
                        for j in range(3):
                            if not visited[idx[j]]:
                                visited[idx[j]] = True
                                q.append(idx[j])
            if flag:
                count += 1
    return count


def solution(board):
    x_count = board.count("X")
    o_count = board.count("O")

    x_win_count = get_win_count(board, "X")
    o_win_count = get_win_count(board, "O")

    if (x_count < o_count):
        # O는 X보다 많을 수 없다.
        return INVALID
    if (x_win_count == 0 and o_win_count == 0 and is_full(board)):
        # X와 O가 무승부일 경우는 모든 칸이 다 찼을 때이다.
        return VALID
    if (x_count == o_count) and (x_win_count == 0 and o_win_count == 1):
        # X와 O의 개수가 같을 때는 O가 이겨야 한다.
        return VALID
    if (x_count-1 == o_count) and (x_win_count == 1 and o_win_count == 0):
        # X가 O보다 많을 때는 X가 이겨야 한다.
        return VALID

    return INVALID


while True:
    board = input().strip()
    if board == "end":
        break
    print(solution(board))
