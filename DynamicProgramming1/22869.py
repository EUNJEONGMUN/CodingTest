import sys
input = sys.stdin.readline

n, k = map(int, input().split())
rocks = [0]+list(map(int, input().split()))
INF = int(1e9)
dp = [False]*(n+1)
dp[1] = True

for j in range(2, n+1):  # i에서 j까지 올 수 있는지 확인
    for i in range(1, j):  # i 순회
        if dp[i]:  # i까지 도달할 수 있다면
            temp = (j-i)*(1+abs(rocks[i]-rocks[j]))
            if temp <= k:
                dp[j] = True

if dp[-1]:
    print("YES")
else:
    print("NO")
