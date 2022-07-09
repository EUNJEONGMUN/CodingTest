n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
# visited = [False]*n
res = []


def solution():
    if len(res) == m:
        print(*res)
        return

    last = 0
    for i in range(n):
        if last != numbers[i]:
            res.append(numbers[i])
            last = numbers[i]  # 마지막 숫자 체크
            solution()
            res.pop()


solution()
