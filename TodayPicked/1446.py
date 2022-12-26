# import sys
# input = sys.stdin.readline

# n, d = map(int, input().split())
# short_path = [list(map(int, input().split())) for _ in range(n)]

# history = set()
# history.add(0)
# history.add(d)

# answer = 0
# for a, b, c in short_path:
#     history.add(a)
#     history.add(b)
# history = sorted(list(history))
# dp = [i for i in history]
# print(dp)
# for a, b, c in short_path:
#     idx_a, idx_b = history.index(a), history.index(b)
#     if dp[idx_b] > dp[idx_a]+c:
#         dp[idx_b] = dp[idx_a]+c
#         for i in range(idx_b+1, len(dp)):
#             dp[i] = min(dp[i], dp[i-1]+(history[i]-history[i-1]))
#     print(dp, a, b, c)
# print(dp[history.index(d)])


N, D = map(int, input().split())
short_path = [list(map(int, input().split())) for _ in range(N)]
distance = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    for a, b, c in short_path:
        if i == a and b <= D and distance[i]+c < distance[b]:
            distance[b] = distance[i]+c
print(distance[D])
