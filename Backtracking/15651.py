#  중복 순열 직접 구현
n, m = map(int, input().split())
cnt = m
numbers = list(range(1, n+1))

res = []


def permutation(pre, m):
    if m == 0:
        return pre
    for i in range(len(numbers)):
        pre.append(numbers[i])
        temp = permutation(pre, m-1)
        if temp and len(temp) == cnt:
            print(*temp)
        pre.pop()


permutation([], m)
# print(res)
