def solution(n, m, board):
    board = [list(b) for b in board]
    delete = set()
    cnt = 0
    while True:

        for i in range(1, n):  # 4개짜리 찾기
            for j in range(1, m):
                if board[i][j] == " ":
                    continue
                if board[i][j] == board[i-1][j] == board[i-1][j-1] == board[i][j-1]:
                    delete.update([(i, j), (i-1, j), (i-1, j-1), (i, j-1)])
        if not delete:
            break
        cnt += len(delete)
        for x, y in list(delete):  # 삭제
            board[x][y] = " "

        for i in range(n-2, -1, -1):  # 내리기
            for j in range(m):
                if board[i][j] == " " or board[i+1][j] != " ":
                    continue
                idx = i
                while True:
                    if idx == n-1 or board[idx+1][j] != " ":
                        board[idx][j] = board[i][j]
                        board[i][j] = " "
                        break
                    idx += 1

        delete = set()
    return cnt


print(solution(6, 6, ["TTTANT", "RRFACC",
      "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
