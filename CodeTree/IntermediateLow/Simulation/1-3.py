import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def calculate1():  # ㄱ 모양 계산
    """
    ㄱ 모양을 회전하면 나올 수 있는 총 모양은 ㄱ, ㄴ, 「 , 」이다.
    이 모양들을 합치면 ㅁ 모양이 될 것이다.
    이 모양들 중에서 가장 큰 값은 
    4칸의 합 + 4개의 칸 중에서 가장 작은 값 일 것이다. 
    """
    res = 0
    for i in range(n-1):
        for j in range(m-1):
            res = max(res, arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1]
                      [j+1]-min(arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]))
    return res


def calculate2():
    res = 0

    # 행 계산
    for i in range(n):
        for j in range(m-2):
            res = max(res, arr[i][j]+arr[i][j+1]+arr[i][j+2])

    # 열 계산
    for i in range(n-2):
        for j in range(m):
            res = max(res, arr[i][j]+arr[i+1][j]+arr[i+2][j])
    return res


print(max(calculate1(), calculate2()))
