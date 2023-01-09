from collections import deque

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
log = set()
q = deque()
q.append([numbers[:], 0])
answer = -1
while q:
    temp, cnt = q.popleft()
    if temp == sorted(temp):
        answer = cnt
        break
    for i in range(n-k+1):
        reverse_temp = temp[i:i+k]
        reverse_temp.reverse()
        new_sort = temp[:i]+reverse_temp+temp[i+k:]
        if tuple(new_sort) not in log:
            log.add(tuple(new_sort))
            q.append([new_sort, cnt+1])

print(answer)
