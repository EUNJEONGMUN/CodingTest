import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
table = [[0]*(m+1) for _ in range(n+1)]
# 열별로 더하기
for i in range(1, n+1):
    for j in range(1, m+1):
        table[i][j] = table[i-1][j]+arr[i-1][j-1]

# 헹별로 더하기
for j in range(1, m+1):
    for i in range(1, n+1):
        table[i][j] += table[i][j-1]


def calculate(a, b, x, y):
    return table[x][y]-table[a-1][y]-table[x][b-1]+table[a-1][b-1]


max_value = -INF

for a in range(1, n+1):
    for b in range(1, m+1):
        for x in range(a, n+1):
            for y in range(b, m+1):
                temp = calculate(a, b, x, y)
                if temp > max_value:
                    max_value = temp
print(max_value)

#  다른 분 코드
# N, M = map(int, input().split())
# arr = [[int(x) for x in input().split()] for _ in range(N)]
# srr = [[0 for _ in range(M)] for _ in range(N)]
# for i in range(M):
#     srr[0][i] = arr[0][i]
# for i in range(1, N):
#     for j in range(M):
#         srr[i][j] = srr[i - 1][j] + arr[i][j]
# answer = max(max(arr[i]) for i in range(N))
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         temp = 0
#         for k in range(M):
#             val = srr[j][k] - srr[i][k]
#             print(">>>", j, k, i, k)
#             temp += val
#             answer = max(answer, temp)
#             if temp < 0:
#                 temp = 0
# print(answer)

# 다른 분 코드
# n, m = map(int, input().split())
# d = [[0] * (m + 1)]
# for _ in range(n):
#     d.append([0] + list(map(int, input().split())))
# ans = -int(4e9)
# for i in range(1, n + 1):
#     p = [0] * (m + 1)  # p 리스트에는 arr 리스트의 행 방향 누적합을 저장
#     for j in range(i, n + 1):
#         t = [0] * (m + 1)  # t 리스트에는 p 리스트의 열 방향 누적합을 저장
#         #  t 리스트에 누적합을 저장할 때, 이전 누적값이 음수라면 버리고 p 리스트 값만 저장한다.
#         for k in range(1, m + 1):
#             p[k] += d[j][k]
#             t[k] = max(t[k-1] + p[k], p[k])
#             ans = max(ans, t[k])
# print(ans)
