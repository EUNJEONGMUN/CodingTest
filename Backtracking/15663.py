n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False]*n
res = []


def solution():
    if len(res) == m:
        print(*res)
        return

    last = 0
    for i in range(n):
        if not visited[i] and last != numbers[i]:
            visited[i] = True
            res.append(numbers[i])
            last = numbers[i]  # 마지막 숫자 체크
            solution()
            visited[i] = False
            res.pop()


solution()
