import sys
input = sys.stdin.readline

m, n, l, k = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(k)]

max_count = 0
for i in range(k):
    for j in range(k):
        x, y = stars[i][0], stars[j][1]
        count = 0
        for star in range(k):
            a, b = stars[star]

            if 0 <= a-x <= l and 0 <= b-y <= l:
                count += 1
        max_count = max(max_count, count)

print(k-max_count)
