import math

n = int(input())
nums = set(list(map(int, input().split())))


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


arr = []
for num in nums:
    if is_prime(num):
        arr.append(num)

if arr:
    temp = arr[0]
    for i in range(1, len(arr)):
        temp *= arr[i]
    print(temp)
else:
    print(-1)
