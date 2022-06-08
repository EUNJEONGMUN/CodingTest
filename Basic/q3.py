def solution(n):
    for i in range(1, n):
        if i*i == n:
            return 1
    return 0


print(solution(9))
print(solution(756580036))
