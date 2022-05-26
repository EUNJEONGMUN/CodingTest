import math
n = int(input())


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def is_palindrome(x):
    temp = list(str(x))
    if temp == temp[::-1]:
        return True
    return False


while True:
    if is_palindrome(n) and is_prime(n):
        print(n)
        break
    else:
        n += 1
