tc = int(input())


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        c = a % b
        return gcd(b, c)


for _ in range(tc):
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1, len(arr)-1):
        for j in range(i+1, len(arr)):
            result += gcd(arr[i], arr[j])
    print(result)
