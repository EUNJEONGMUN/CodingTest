# n, m, k = map(int, input().split())
# UP = 0
# LEFT = 1
# table = [[[0, 0] for _ in range(m)] for _ in range(n)]


# def convert_xy(num):
#     return num//m, num % m


# if k == 0:
#     for i in range(n):
#         for j in range(m):
#             if i == 0 and j == 0:
#                 continue
#             if i == 0:
#                 table[i][j] = [0, 1]
#             elif j == 0:
#                 table[i][j] = [1, 0]
#             else:
#                 table[i][j][UP] = sum(table[i-1][j])
#                 table[i][j][LEFT] = sum(table[i][j-1])
# else:
#     x, y = convert_xy(k-1)

#     for i in range(x+1):
#         for j in range(y+1):
#             if i == 0 and j == 0:
#                 continue
#             if i == 0:
#                 table[i][j] = [0, 1]
#             elif j == 0:
#                 table[i][j] = [1, 0]
#             else:
#                 table[i][j][UP] = sum(table[i-1][j])
#                 table[i][j][LEFT] = sum(table[i][j-1])
#     for i in range(x, n):
#         for j in range(y, m):
#             if i == x and j == y:
#                 continue
#             if i == x:
#                 table[i][j] = [0, sum(table[x][y])]
#             elif j == y:
#                 table[i][j] = [sum(table[x][y]), 0]
#             else:
#                 table[i][j][UP] = sum(table[i-1][j])
#                 table[i][j][LEFT] = sum(table[i][j-1])

# print(sum(table[-1][-1]))

n, m, k = map(int, input().split())

table = [[1]*m for _ in range(n)]


def convert_xy(num):
    return num//m, num % m


if k == 0:
    for i in range(1, n):
        for j in range(1, m):
            table[i][j] = table[i-1][j]+table[i][j-1]
else:
    x, y = convert_xy(k-1)

    for i in range(1, x+1):
        for j in range(1, y+1):
            table[i][j] = table[i-1][j]+table[i][j-1]

    for i in range(x, n):
        for j in range(y, m):
            if i == x or j == y:
                table[i][j] = table[x][y]
            else:
                table[i][j] = table[i-1][j]+table[i][j-1]
print(table[-1][-1])
