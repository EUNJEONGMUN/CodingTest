import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
tower = [(i, h) for i, h in enumerate(tower, start=1)]

answer = [0]*(n+1)
save = []
while tower:
    idx, high = tower.pop()
    while save:
        if save[-1][1] < high:
            s = save.pop()
            answer[s[0]] = idx
        else:
            break
    if tower:
        if tower[-1][1] > high:
            answer[idx] = tower[-1][0]
        else:
            save.append((idx, high))

print(*answer[1:])
