import sys
input = sys.stdin.readline
n = int(input())
student = {}  # Key->학생 번호, value->좋아하는 학생리스트
order = []  # 자리 배치 순서
for _ in range(n**2):
    temp = list(map(int, input().split()))
    order.append(temp[0])
    student[temp[0]] = temp[1:]

grid = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):  # 범위 확인
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


def find(num):  # 자리 찾기
    # [인접 좋아하는 학생 수, 인접 빈 공간 수, 앉을 수 있는 자리 좌표x, 앉을 수 있는 자리 좌표y] 가 담길 것임.
    like = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:  # 해당 자리가 비어있지 않다면 pass
                continue
            blank_cnt = 0  # 인접 빈 공간 cnt
            like_cnt = 0  # 인접 종아하는 학생 cnt
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if check_range(nx, ny):
                    if grid[nx][ny] == 0:  # 비어있다면
                        blank_cnt += 1  # black_cnt 증가
                    elif grid[nx][ny] in student[num]:  # 좋아하는 학생리스트 안에 있다면
                        like_cnt += 1  # like_cnt 증가
            like.append([like_cnt, blank_cnt, i, j])  # like 리스트에 append
    # 좋아하는 학생 수, 빈 공간 수로 정렬, 같다면 행과 열이 작은 순으로 정렬
    like.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    return like[0][2], like[0][3]  # like 리스트의 맨 첫 번 째 요소의 x,y 값 리턴


def cal_satisfaction(x, y):  # 점수 계산
    like_cnt = 0
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if check_range(nx, ny) and grid[nx][ny] in student[grid[x][y]]:
            like_cnt += 1
    if like_cnt:
        return 10**(like_cnt-1)
    else:
        return 0


for num in order:
    x, y = find(num)
    grid[x][y] = num

res = 0
for i in range(n):
    for j in range(n):
        res += cal_satisfaction(i, j)
print(res)
