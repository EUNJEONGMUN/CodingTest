import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
relationships = [list(map(int, input().split())) for _ in range(m)]
relationship = [set() for _ in range(n+1)]

for a, b in relationships:
    relationship[a].add(b)
    relationship[b].add(a)


def has_friends(node):
    if len(relationship[node]) < 2:
        return False
    return True


def is_friend(x, y):
    if y in relationship[x]:
        return True
    return False


def calculate_friend_count(a, b, c):
    return (len(relationship[a])-2)+(len(relationship[b])-2)+(len(relationship[c])-2)


friends = set()
for i in range(1, n+1):
    if not has_friends(i):
        continue
    for a, b in list(combinations(relationship[i], 2)):
        if is_friend(a, b):
            friends.add(tuple(sorted([i, a, b])))

min_value = int(1e9)
if not friends:
    print(-1)
else:
    for a, b, c in friends:
        min_value = min(min_value, calculate_friend_count(a, b, c))
    print(min_value)