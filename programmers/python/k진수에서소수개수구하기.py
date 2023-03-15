import math


def convert_to_k(n, k):
    num = ""
    while n:
        num += str(n % k)
        n //= k
    return num[::-1]


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    prime = convert_to_k(n, k).split("0")
    cnt = 0
    for p in prime:
        if p and is_prime(int(p)):
            cnt += 1
    return cnt


print(solution(437674, 3))
print(solution(110011, 10))
print(solution(885733, 3))
