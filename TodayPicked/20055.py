from collections import deque
n, k = map(int, input().split())

belt = deque(map(int, input().split()))
robot = deque([False]*(2*n))
step = 1

while True:

    # 1. 벨트 이동
    belt.rotate(1)
    robot.rotate(1)
    robot[n-1] = False

    # 2. 로봇 이동
    for i in range(n-2, 0, -1):
        if robot[i] == True and belt[i+1] > 0 and robot[i+1] == False:
            belt[i+1] -= 1
            robot[i] = False
            robot[i+1] = True

    robot[n-1] = False

    # 3. 로봇 올리기
    if robot[0] == False and belt[0] > 0:
        belt[0] -= 1
        robot[0] = True

    if belt.count(0) >= k:
        print(step)
        break
    step += 1
