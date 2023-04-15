N = int(input())


def create_prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


prime_list = create_prime_list(N+1)
answer = 0

left, right = 0, 0
if len(prime_list) == 0:
    print(0)
else:
    total = prime_list[0]
    while left <= right:
        if total == N:
            answer += 1
        if total < N:
            right += 1
            if right >= len(prime_list):
                break
            total += prime_list[right]
        else:
            total -= prime_list[left]
            left += 1

    print(answer)
