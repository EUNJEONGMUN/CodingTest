# n = int(input())
# arr = [0]+list(map(int, input().split()))
# for i in range(1, n+1):
#     arr[i] += arr[i-1]

# res = 0
# table = {}


# def calculate(a, b):
#     if a > b:
#         return 0
#     return table[(a, b)]


# for i in range(1, n+1):
#     for j in range(i, n+1):
#         table[(i, j)] = arr[j]-arr[i-1]

# # 벌통이 오른쪽 끝에 있을 때
# for i in range(1, n-1):
#     for j in range(i+1, n):
#         temp = calculate(i+1, j-1)+calculate(j+1, n)*2
#         if res < temp:
#             res = temp
# # 벌통이 가운데에 있을 때
# for i in range(2, n):
#     res = max(res, calculate(2, i)+calculate(i, n-1))

# # 벌통이 왼쪽에 있을 때
# for i in range(2, n):
#     for j in range(i+1, n+1):
#         temp = calculate(1, i-1)*2+calculate(i+1, j-1)
#         if res < temp:
#             res = temp

# print(res)


n = int(input())
arr = [0]+list(map(int, input().split()))
for i in range(1, n+1):
    arr[i] += arr[i-1]

res = 0


def calculate(a, b):
    if b < a:
        return 0
    return arr[b]-arr[a-1]


# 벌통이 오른쪽 끝에 있을 때, 맨 왼쪽 벌은 가장 왼쪽에 있는 게 최대선택
for i in range(2, n):
    temp = calculate(2, i-1)+(calculate(i+1, n)*2)
    if res < temp:
        res = temp
# 벌통이 가운데에 있을 때, 두 벌은 양쪽 끝에 있는 게 최대 선택
for i in range(2, n):
    res = max(res, calculate(2, i)+calculate(i, n-1))

# 벌통이 왼쪽에 있을 때, 맨 오른쪽 벌은 가장 오른쪽에 있는 게 최대 선택
for i in range(2, n):
    temp = calculate(1, i-1)*2+calculate(i+1, n-1)
    if res < temp:
        res = temp

print(res)
