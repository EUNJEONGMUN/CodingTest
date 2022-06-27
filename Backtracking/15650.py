# 조합 직접 구현

from itertools import combinations

n, m = map(int, input().split())
cnt = m
numbers = list(range(1, n+1))

# res = []


def combination(pre, now, m):
    if len(now) < m or m == 0:
        return pre

    for i in range(len(now)):
        pre.append(now[i])
        temp = combination(pre, now[i+1:], m-1)
        if temp and len(temp) == cnt:
            # res.append(temp[:])
            print(*temp)
        pre.pop()


combination([], numbers, m)
