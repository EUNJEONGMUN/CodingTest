# import sys
# from collections import defaultdict
# input = sys.stdin.readline


# n, m, k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# table = [[5]*n for _ in range(n)]
# trees = defaultdict(list)
# for _ in range(m):
#     x, y, age = map(int, input().split())
#     trees[(x-1, y-1)].append(age)

# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# # k년이 지난 후 살아남은 나무 구하기


# def check_range(x, y):
#     if x >= 0 and y >= 0 and x < n and y < n:
#         return True
#     return False


# def spring_and_summer():
#     die = []

#     for key, value in trees.items():
#         ages = sorted(value)
#         finish = []
#         for age in ages:
#             if table[key[0]][key[1]] >= age:
#                 table[key[0]][key[1]] -= age
#                 finish.append(age+1)
#             else:
#                 die.append((key[0], key[1], age))
#                 break

#         if len(finish) != 0:
#             trees[key] = finish[:]

#     # summer
#     for x, y, age in die:
#         table[x][y] += age//2


# def autumn():
#     for key, value in trees.items():
#         for v in value:
#             if v % 5 == 0:
#                 for i in range(8):
#                     print(key)
#                     nx = key[0]+dx[i]
#                     ny = key[1]+dy[i]

#                     if check_range(nx, ny):
#                         trees[(nx, ny)].append(1)


# def winter():
#     for i in range(n):
#         for j in range(n):
#             table[i][j] += arr[i][j]


# def calculate():
#     res = 0
#     for key, value in trees.items():
#         res += len(value)
#     return res


# for _ in range(k):
#     spring_and_summer()
#     autumn()
#     winter()

# print(calculate())


import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
nutrients = [[5]*n for _ in range(n)]  # 양분 저장
trees = [[[] for _ in range(n)] for _ in range(n)]  # 나무들 저장

for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# k년이 지난 후 살아남은 나무 구하기


def check_range(x, y):  # 범위 확인
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


def spring_and_summer():
    # spring
    die = []  # 죽은 나무 리스트
    for i in range(n):
        for j in range(n):
            finish = []  # 산 나무들
            tree_sort = sorted(trees[i][j])  # 나이 어린 순으로 정렬
            for age in tree_sort:
                if nutrients[i][j] >= age:  # 나이만큼 양분을 먹을 수 있다면
                    nutrients[i][j] -= age  # 양분 먹고
                    finish.append(age+1)  # 저장
                else:
                    # 나이만큼 양분을 먹을 수 없다면, die 리스트에 저장
                    die.append((i, j, age))
            trees[i][j] = finish[:]  # 산 나무들 저장

    # summer
    for x, y, age in die:
        nutrients[x][y] += age//2  # 죽은 나무들의 양분 더하기


def autumn():
    for i in range(n):
        for j in range(n):
            for age in trees[i][j]:
                if age % 5 == 0:  # 5로 나누어 떨어질 경우, 주변 8곳에 나이1인 나무 추가
                    for a in range(8):
                        nx = i+dx[a]
                        ny = j+dy[a]

                        if check_range(nx, ny):
                            trees[nx][ny].append(1)


def winter():
    # 양분 추가
    for i in range(n):
        for j in range(n):
            nutrients[i][j] += arr[i][j]


def calculate():  # 마지막 결과 계산
    res = 0
    for i in range(n):
        for j in range(n):
            res += len(trees[i][j])
    return res


for _ in range(k):
    # 봄, 여름, 가을, 겨울 k번 반복
    spring_and_summer()  # 봄, 여름
    autumn()  # 가을
    winter()  # 겨울

print(calculate())
