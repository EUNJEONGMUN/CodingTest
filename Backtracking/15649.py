# 순열 직접 구현
n, m = map(int, input().split())
cnt = m
numbers = list(range(1, n+1))

res = []


def permutation(pre, now, m):
    if len(now) < m or m == 0:
        return pre

    for i in range(len(now)):
        pre.append(now[i])
        temp = permutation(pre, now[:i]+now[i+1:], m-1)
        if temp and len(temp) == cnt:
            # res.append(temp[:])
            print(*temp)
        pre.pop()


permutation([], numbers, m)
# print(res)
