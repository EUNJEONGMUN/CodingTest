n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
res = []


def solution(now, base):
    if len(res) == m:
        print(*res)
        return

    last = 0
    for i in range(len(now)):
        if last != now[i]:
            res.append(now[i])
            last = now[i]  # 마지막 숫자 체크
            solution(now[i:], base+i)
            res.pop()


solution(numbers[:], 0)
