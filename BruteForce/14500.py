import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def tetromino1():
    res = -1
    # ㅁㅁㅁㅁ
    for i in range(n):
        for j in range(m-3):
            res = max(res, sum(arr[i][j:j+4]))
    # ㅁ
    # ㅁ
    # ㅁ
    # ㅁ
    for i in range(n-3):
        for j in range(m):
            res = max(res, arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j])
    return res

# ㅁㅁㅁ
# ㅁㅁㅁ


def tetromino2():
    res = -1
    for i in range(n-1):
        for j in range(m-2):
            total = sum(arr[i][j:j+3]+arr[i+1][j:j+3])
            delete = min(arr[i][j]+arr[i+1][j], arr[i][j]+arr[i+1][j+2], arr[i+1][j]+arr[i][j+2], arr[i][j+2]+arr[i+1][j+2], arr[i][j]+arr[i][j+1], arr[i][j+1]+arr[i][j+2],
                         arr[i+1][j]+arr[i+1][j+1], arr[i+1][j+1]+arr[i+1][j+2], arr[i][j]+arr[i][j+2], arr[i+1][j]+arr[i+1][j+2])

            res = max(res, total-delete)
    return res

# ㅁㅁ
# ㅁㅁ
# ㅁㅁ


def tetromino3():
    res = -1
    for i in range(n-2):
        for j in range(m-1):
            total = sum(arr[i][j:j+2]+arr[i+1][j:j+2]+arr[i+2][j:j+2])
            # delete = min(arr[i][j]+arr[i][j+1], arr[i][j]+arr[i+2][j+1], arr[i][j+1]+arr[i+2][j], arr[i+2][j]+arr[i+2][j+1], arr[i][j]+arr[i+1][j], arr[i+1][j]+arr[i+2][j],
            #              arr[i][j+1]+arr[i+1][j+1], arr[i+1][j+1]+arr[i+2][j+1], arr[i][j]+arr[i+2][j], arr[i][j+1]+arr[i+2][j+1])
            delete = min(arr[i][j]+arr[i+2][j+1], arr[i][j+1]+arr[i+2][j], arr[i][j]+arr[i+1][j], arr[i+1][j]+arr[i+2][j],
                         arr[i][j+1]+arr[i+1][j+1], arr[i+1][j+1]+arr[i+2][j+1], arr[i][j]+arr[i+2][j], arr[i][j+1]+arr[i+2][j+1])
            res = max(res, total-delete)
    return res


print(max(tetromino1(), tetromino2(), tetromino3()))
