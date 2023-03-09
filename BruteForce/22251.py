N, K, P, X = map(int, input().split())

numbers = [
    [1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
]

answer = 0


def get_different_count(a, b):
    cnt = 0
    for i in range(7):
        if numbers[a][i] != numbers[b][i]:
            cnt += 1
    return cnt


def solution(num, depth, remain_p):
    global answer
    if depth == len(num):
        temp = int("".join(list(map(str, num))))
        if temp <= N and temp >= 1 and temp != X:
            answer += 1
        return

    origin = num[depth]

    for i in range(10):
        diff_count = get_different_count(origin, i)
        if remain_p-diff_count >= 0:
            num[depth] = i
            solution(num, depth+1, remain_p-diff_count)
            num[depth] = origin


num = [0]*K
x = X
idx = K-1
while x > 0:
    num[idx] = x % 10
    x //= 10
    idx -= 1

solution(num, 0, P)
print(answer)
