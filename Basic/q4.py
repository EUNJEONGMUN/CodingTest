def solution(n):
    res = 1
    while res*2 <= n:
        res = res*2
    return res


print(solution(5))
print(solution(97615282))
print(solution(1024))
