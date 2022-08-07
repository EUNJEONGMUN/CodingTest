import sys
input = sys.stdin.readline

n = int(input())
rocks = [list(map(int, input().split())) for _ in range(n-1)]
k = int(input())
INF = int(1e9)
dp = [INF]*n

# dp 테이블 초기화
dp[0] = 0
if n > 1:
    dp[1] = rocks[0][0]
if n > 2:
    dp[2] = min(dp[1]+rocks[1][0], dp[0]+rocks[0][1])

# 작은 점프와 큰 점프 중 작은 값들로 dp 테이블 채우기
for i in range(3, n):
    dp[i] = min(dp[i-1]+rocks[i-1][0], dp[i-2]+rocks[i-2][1])
res = dp[-1]


def solution(table, start):
    for i in range(start+1, n):
        table[i] = min(table[i-1]+rocks[i-1][0], table[i-2]+rocks[i-2][1])
    return table[-1]


# 매우 큰 점프를 한 번씩 해보면서 최솟값으로 갱신
for i in range(3, n):
    val = solution(dp[:i]+[dp[i-3]+k]+dp[i+1:], i)
    res = min(res, val)

print(res)
