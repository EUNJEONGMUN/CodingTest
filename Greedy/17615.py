import sys
input = sys.stdin.readline

n = int(input())
balls = list(input().strip())
red = 0
blue = 0
red_reverse = 0
blue_reverse = 0


def count_balls(idx):
    end = idx
    while end < n and balls[idx] == balls[end]:
        end += 1
    return end


def count_balls_reverse(idx):
    end = idx
    while end >= 0 and balls[idx] == balls[end]:
        end -= 1
    return end


start = 0
while True:
    end_idx = count_balls(start)

    if end_idx == n:
        break
    if balls[start] == 'R':
        red += end_idx-start
    else:
        blue += end_idx-start
    start = end_idx

start = n-1
while True:
    end_idx = count_balls_reverse(start)

    if end_idx == -1:
        break
    if balls[start] == 'R':
        red_reverse += start-end_idx
    else:
        blue_reverse += start-end_idx
    start = end_idx

print(min(red, blue, red_reverse, blue_reverse))
