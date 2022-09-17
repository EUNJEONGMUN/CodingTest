# from collections import defaultdict


# def solution(board, skill):
#     n, m = len(board), len(board[0])
#     power = defaultdict(int)

#     def attack(r1, c1, r2, c2, degree):
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 power[(i, j)] += degree

#     for t, r1, c1, r2, c2, degree in skill:
#         if t == 1:  # 적의 공격
#             attack(r1, c1, r2, c2, -degree)
#         else:
#             attack(r1, c1, r2, c2, degree)

#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if board[i][j]+power[(i, j)] > 0:
#                 cnt += 1
#     return cnt


def solution(board, skill):
    n, m = len(board), len(board[0])

    prefix = [[0]*(m+1) for _ in range(n+1)]

    def attack(r1, c1, r2, c2, degree):
        prefix[r1][c1] += degree
        prefix[r2+1][c1] += -degree
        prefix[r1][c2+1] += -degree
        prefix[r2+1][c2+1] += degree

    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:  # 적의 공격
            attack(r1, c1, r2, c2, -degree)
        else:  # 아군
            attack(r1, c1, r2, c2, degree)

    for i in range(1, n+1):
        for j in range(m+1):
            prefix[i][j] += prefix[i-1][j]

    for j in range(1, m+1):
        for i in range(n+1):
            prefix[i][j] += prefix[i][j-1]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]+prefix[i][j] > 0:
                cnt += 1
    return cnt


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [
      [1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [
      [1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
