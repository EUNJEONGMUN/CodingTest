INF = int(1e9)


def solution(n, s, a, b, fares):
    table = [[INF]*(n+1) for _ in range(n+1)]
    for x, y, cost in fares:
        table[x][y] = cost
        table[y][x] = cost
    for k in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                if x == y:
                    table[x][y] = 0
                else:
                    table[x][y] = min(table[x][y], table[x][k]+table[k][y])
    res = table[s][a]+table[s][b]
    for i in range(1, n+1):
        if i == s:
            continue
        res = min(res, table[s][i]+table[i][a]+table[i][b])
    return res


# print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
#       5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4],
#       [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [
      6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
