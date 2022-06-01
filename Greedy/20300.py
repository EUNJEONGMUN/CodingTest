n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = arr[-1]
if n % 2 == 1:
    n -= 1  # 홀수라면 맨 끝 운동기구 하나 빼고
for i in range(n//2):
    if result < arr[n-i-1] + arr[i]:
        result = arr[n-i-1] + arr[i]

print(result)
