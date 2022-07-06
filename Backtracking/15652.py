# 중복 조합 직접 구현

n, m = map(int, input().split())
cnt = m
numbers = list(range(1, n+1))


def combination(pre, now, m):
    if m == 0:
        return pre

    for i in range(len(now)):
        pre.append(now[i])
        temp = combination(pre, now[i:], m-1)
        if temp and len(temp) == cnt:
            print(*temp)
        pre.pop()


combination([], numbers, m)
