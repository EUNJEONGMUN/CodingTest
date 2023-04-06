import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    coins = dict()
    total = 0
    for _ in range(n):
        coin, cnt = map(int, input().split())
        coins[coin] = cnt
        total += (coin*cnt)

    if total % 2 != 0:
        print(0)
        continue
    total //= 2

    dp = [False]*(total+1)
    dp[0] = 1

    for coin, cnt in coins.items():
        for now in range(total, coin-1, -1):
            if dp[now-coin]:
                for j in range(cnt):
                    if now + coin*j > total:
                        break
                    dp[now+coin*j] = True

        if dp[total]:
            print(1)
            break
    else:
        print(0)
