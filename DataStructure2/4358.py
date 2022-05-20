from collections import defaultdict
import sys
input = sys.stdin.readline
trees = defaultdict(int)
cnt = 0
while True:
    t = input().strip()
    if len(t) == 0:
        break
    trees[t] += 1
    cnt += 1

result = []
for key, value in trees.items():
    result.append([key, '{:.4f}'.format(value/cnt*100)])
result.sort()
for r in result:
    print(r[0]+" "+str(r[1]))
