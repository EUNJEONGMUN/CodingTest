import sys
input = sys.stdin.readline

n = int(input())
count = 0
building = [0]

for _ in range(n):
    x, y = map(int, input().split())
    if (building[-1] < y):
        count += 1
        building.append(y)
    else:
        while building[-1] > y:
            building.pop()
        if (building[-1] < y):
            count += 1
            building.append(y)
print(count)
