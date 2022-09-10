n = int(input())
res = 0


def backtracking(arr):
    global res
    if len(arr) == n:
        res += 1
        return

    for i in [1, 2, 3, 4]:
        if len(arr)+i <= n:
            backtracking(arr+([i]*i))


backtracking([])
print(res)
