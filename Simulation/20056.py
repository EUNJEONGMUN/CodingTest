import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())  # n: 격자크기, m:파이어볼 개수, k: 이동횟수
balls = [list(map(int, input().split())) for _ in range(m)]


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def change(x):  # 좌표 바꾸기
    if x < 0:
        x = -x
        return n-(x % n)
    else:
        div = x % n
        return div if div != 0 else n


def move():  # 이동
    for i in range(len(balls)):
        x, y, s, d = balls[i][0], balls[i][1], balls[i][3], balls[i][4]
        nx, ny = change(x+(dx[d]*s)), change(y+(dy[d]*s))
        balls[i][0], balls[i][1] = nx, ny


def separate():  # 분리
    temp = defaultdict(list)
    while balls:
        x, y, m, s, d = balls.pop()
        temp[(x, y)].append([m, s, d])

    for key, value in temp.items():
        if len(value) < 2:  # 1개 이하일 때는 분리되지 않음
            balls.append([key[0], key[1], value[0][0],
                         value[0][1], value[0][2]])
        else:
            sum_m, sum_s, odd, even = 0, 0, 0, 0
            for v in value:
                sum_m += v[0]
                sum_s += v[1]
                if v[2] % 2 == 0:
                    even += 1
                else:
                    odd += 1

            if sum_m//5 == 0:  # 질량이 0인 파이어볼은 없어진다.
                continue

            if odd == 0 or even == 0:  # 방향이 짝수 혹은 홀수
                for i in [0, 2, 4, 6]:
                    balls.append(
                        [key[0], key[1], sum_m//5, sum_s//(odd+even), i])
            else:
                for i in [1, 3, 5, 7]:
                    balls.append(
                        [key[0], key[1], sum_m//5, sum_s//(odd+even), i])


for _ in range(k):
    move()
    separate()

res = 0
for ball in balls:
    res += ball[2]
print(res)
