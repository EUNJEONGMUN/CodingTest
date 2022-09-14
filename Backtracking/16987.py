import sys
input = sys.stdin.readline

n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
res = 0
S, W = 0, 1  # S:내구성, W:무게


def bf(now):
    global res
    if now == n:  # 마지막 계란일 경우
        cnt = 0
        for i in range(n):  # 깨진 계란의 개수를 세어 res에 반영
            if eggs[i][S] <= 0:
                cnt += 1
        res = max(res, cnt)
        return

    # 단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.

    # 자신이 깨져있다면 다음 계란으로
    if eggs[now][S] <= 0:
        bf(now+1)
        return

    # 자신을 제외한 모든 계란이 깨졌다면
    for i in range(n):
        if n == now:
            continue
        if eggs[i][S] > 0:
            break
    else:
        res = max(res, n-1)
        return

    for next_egg in range(n):
        # 깰 개란이 현재 계란이거나, 깨진 계란이라면 pass
        if next_egg == now or eggs[next_egg][W] <= 0:
            continue
        # 계란 깨기
        eggs[now][S] -= eggs[next_egg][W]
        eggs[next_egg][S] -= eggs[now][W]
        bf(next_egg)  # 다음 계란 탐색
        # 계란 원상 복구
        eggs[now][S] += eggs[next_egg][W]
        eggs[next_egg][S] += eggs[now][W]


bf(0)
print(res)

"""
N이 8이하이기 때문에 O(N^2)이어도 2천만을 넘지 않는다.
"""
