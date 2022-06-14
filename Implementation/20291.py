from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
docs = defaultdict(int)

for _ in range(n):
    name, extension = input().strip().split(".")
    docs[extension] += 1

res = sorted(list(docs.items()))
for key, value in res:
    print(key, value)
