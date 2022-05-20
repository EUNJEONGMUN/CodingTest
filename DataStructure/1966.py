from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = deque(list(map(int, input().split())))
    idx = deque([i for i in range(n)])

    cnt = 0
    while p:
        priority = p.popleft()
        index = idx.popleft()

        if not p or priority >= max(p):
            cnt += 1
            if index == m:
                break
        else:
            p.append(priority)
            idx.append(index)
    print(cnt)
