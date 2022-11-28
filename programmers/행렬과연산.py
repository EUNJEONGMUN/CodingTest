# from collections import deque
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# N, M = 0, 0


# def solution(rc, operations):
#     global N, M
#     N, M = len(rc), len(rc[0])
#     for operation in operations:
#         if operation == "Rotate":
#             rc = rotate(rc)
#         elif operation == "ShiftRow":
#             rc = shift_row(rc)
#     return rc


# def shift_row(table):
#     q = deque(table)
#     q.rotate(1)
#     return list(q)


# def rotate(table):
#     x, y = 0, 0
#     q = deque()
#     for i in range(4):
#         while True:
#             nx, ny = x+dx[i], y+dy[i]
#             if (not check_range(nx, ny)):
#                 break
#             q.append(table[nx][ny])
#             x, y = nx, ny
#     q.rotate(1)
#     x, y = 0, 0
#     for i in range(4):
#         while True:
#             nx, ny = x+dx[i], y+dy[i]
#             if (not check_range(nx, ny)):
#                 break
#             table[nx][ny] = q.popleft()
#             x, y = nx, ny
#     return table


# def check_range(x, y):
#     if (x >= 0 and y >= 0 and x < N and y < M):
#         return True
#     return False


# print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))


from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = 0, 0


def solution(rc, operations):
    global N, M
    N, M = len(rc), len(rc[0])
    rows = deque(deque(rc[i][1:-1]) for i in range(N))
    left = deque(rc[i][0] for i in range(N))
    right = deque(rc[i][-1] for i in range(N))

    for operation in operations:
        if operation == "ShiftRow":
            rows.rotate(1)
            left.rotate(1)
            right.rotate(1)
        else:
            rows[0].appendleft(left.popleft())
            right.appendleft(rows[0].pop())
            rows[-1].append(right.pop())
            left.append(rows[-1].popleft())

    answer = [[] for _ in range(N)]
    for i in range(N):
        answer[i].append(left.popleft())
        answer[i].extend(rows[i])
        answer[i].append(right.popleft())
    return answer


# print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
# print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]],
#       ["Rotate", "ShiftRow", "ShiftRow"]))
# print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
#       ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
print(solution([[1, 2], [5, 6], [9, 10]],
      ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
