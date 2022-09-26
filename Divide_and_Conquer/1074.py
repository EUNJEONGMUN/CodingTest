n, r, c = map(int, input().split())

# r행 c열이 어디에 속하나 살펴보자


def solution(n, r, c):

    if n == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        else:
            return 3

    half = 2**(n-1)
    if r < half:
        if c >= half:  # 1사분면
            return (half**2)+solution(n-1, r, c-half)
        else:  # 2사분면
            return solution(n-1, r, c)
    else:
        if c >= half:  # 4사분면
            return (half**2)*3+solution(n-1, r-half, c-half)
        else:  # 3사분면
            return (half**2)*2+solution(n-1, r-half, c)


print(solution(n, r, c))
