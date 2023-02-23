import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know_truth = set(input().split()[1:])
parties = [set(input().split()[1:]) for _ in range(m)]

for _ in range(m):
    for party in parties:
        if party & know_truth:
            know_truth.update(party)

count = 0
for party in parties:
    if know_truth & party:
        continue
    count += 1
print(count)
