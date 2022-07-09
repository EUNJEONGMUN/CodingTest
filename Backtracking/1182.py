from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
orders = []
res = 0
for i in range(1, n+1):
    orders.extend(list(combinations(arr, i)))

for order in orders:
    if sum(order) == s:
        res += 1
print(res)
