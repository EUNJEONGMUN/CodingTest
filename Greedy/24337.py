n, a, b = map(int, input().split())


def solution(n, a, b):
    answer = []
    for i in range(1, a):
        answer.append(i)
    answer.append(max(a, b))
    for i in range(b-1, 0, -1):
        answer.append(i)

    if len(answer) > n:
        print(-1)
    else:
        print(answer[0], end=" ")
        for _ in range(n-len(answer)):
            print(1, end=" ")
        print(*answer[1:])


solution(n, a, b)
