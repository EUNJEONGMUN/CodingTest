def solution(n):
    res = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


for n in [15, 34567, 27639]:
    print(solution(n))
