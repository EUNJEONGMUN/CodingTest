n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False]*n
res = []


def solution(now, base):
    if len(res) == m:
        print(*res)
        return

    last = 0
    for i in range(len(now)):
        if not visited[i+base] and last != now[i]:
            visited[i+base] = True
            res.append(now[i])
            last = now[i]  # 마지막 숫자 체크
            solution(now[i+1:], base+i+1)
            visited[i+base] = False
            res.pop()


solution(numbers[:], 0)
