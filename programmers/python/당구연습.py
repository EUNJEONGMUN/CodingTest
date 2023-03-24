import math


def solution(m, n, startX, startY, balls):

    def calculate(x, y, ballsX, ballsY):
        return (x-ballsX)**2+(y-ballsY)**2

    answer = []

    for ballX, ballY in balls:
        min_value = int(10e9)
        # UP
        if not (startX == ballX and startY < ballY):
            min_value = min(min_value, calculate(
                startX, 2*n-startY, ballX, ballY))
        # DOWN
        if not (startX == ballX and startY > ballY):
            min_value = min(min_value, calculate(
                startX, -startY, ballX, ballY))
        # LEFT
        if not (startY == ballY and startX > ballX):
            min_value = min(
                min_value, calculate(-startX, startY, ballX, ballY))
        # RIGHT
        if not (startY == ballY and startX < ballX):
            min_value = min(min_value, calculate(
                2*m-startX, startY, ballX, ballY))

        answer.append(min_value)
    return answer


print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))
