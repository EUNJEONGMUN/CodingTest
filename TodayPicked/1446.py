import sys
input = sys.stdin.readline

n, d = map(int, input().split())
short_path = [list(map(int, input().split())) for _ in range(n)]

history = set()
history.add(0)
history.add(d)

answer = 0
for a, b, c in short_path:
    history.add(a)
    history.add(b)
history = sorted(list(history))
dp = [i for i in history]
for a, b, c in short_path:
    idx_a, idx_b = history.index(a), history.index(b)
    if dp[idx_b] > dp[idx_a]+c:
        dp[idx_b] = dp[idx_a]+c
        for i in range(idx_b+1, len(dp)):
            dp[i] = min(dp[i], dp[i-1]+(history[i]-history[i-1]))
    print(dp)
print(dp[history.index(d)])
