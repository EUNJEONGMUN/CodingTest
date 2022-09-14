# 넴모넴모

n, m = map(int, input().split())
res = 0
dx = [0, -1, -1]
dy = [-1, 0, -1]
arr = [[0]*m for _ in range(n)]


def change_xy(idx):  # idx를 x, y 좌표로 바꾸어주는 함수
    return idx//m, idx % m


def bf(now):
    global res
    if now == n*m:  # 현재 인덱스가 넘어갔을 때 종료
        res += 1
        return

    bf(now+1)  # 현재 인덱스에 넴모 설치 x
    i, j = change_xy(now)
    if arr[i+dx[0]][j+dy[0]] == 0 or arr[i+dx[1]][j+dy[1]] == 0 or arr[i+dx[2]][j+dy[2]] == 0:
        # 현재 인덱스에 놓을 수 있는 경우
        arr[i][j] = 1
        bf(now+1)
        arr[i][j] = 0


bf(0)
print(res)
