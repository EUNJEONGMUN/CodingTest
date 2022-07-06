# 조합 직접 구현
n, m = map(int, input().split())
cnt = m
numbers = list(map(int, input().split()))
numbers.sort()


def combination(pre, now, m):
    if len(now) < m or m == 0:
        return pre

    for i in range(len(now)):
        pre.append(now[i])
        temp = combination(pre, now[i+1:], m-1)
        if temp and len(temp) == cnt:
            print(*temp)
        pre.pop()


combination([], numbers, m)
