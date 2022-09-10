k, n = map(int, input().split())
numbers = list(range(1, k+1))
res = []


def permutation(arr):
    if len(arr) == n:
        res.append(arr[:])
        return
    for i in numbers:
        arr.append(i)
        permutation(arr)
        arr.pop()


permutation([])
for r in res:
    print(*r)
