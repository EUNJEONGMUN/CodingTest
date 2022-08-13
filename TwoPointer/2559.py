n, k = map(int, input().split())
arr = list(map(int, input().split()))
INF = int(1e9)

arr_sum = [0]*(n+1)
for i in range(1, n+1):
    arr_sum[i] = arr_sum[i-1]+arr[i-1]
res = -INF

for i in range(k, n+1):
    res = max(res, arr_sum[i]-arr_sum[i-k])
print(res)
