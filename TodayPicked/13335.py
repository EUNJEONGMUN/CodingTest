from collections import deque
import sys
input = sys.stdin.readline

NONE = 0

n, w, L = map(int, input().split())
cars = list(map(int, input().split()))

bridge = deque([0]*w, maxlen=w)
car_point = 0
time = 0
while car_point < n:
    bridge.popleft()
    if sum(bridge)+cars[car_point] <= L:
        bridge.append(cars[car_point])
        car_point += 1
    else:
        bridge.append(NONE)
    time += 1

while sum(bridge) != 0:
    bridge.append(NONE)
    time += 1

print(time)
