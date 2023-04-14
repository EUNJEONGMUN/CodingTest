from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
balls = [[i]+list(map(int, input().split())) for i in range(n)]
balls.sort(key=lambda x: x[2])
color_count = defaultdict(int)
total_size = 0
answer = [0]*n

j = 0
for i in range(len(balls)):
    idx, color, size = balls[i]

    while balls[j][2] < size:
        total_size += balls[j][2]
        color_count[balls[j][1]] += balls[j][2]
        j += 1

    answer[idx] = total_size-color_count[color]

for a in answer:
    print(a)
