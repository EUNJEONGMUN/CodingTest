def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    x, y = -1, 0
    number = 1

    def check_range(x, y):
        if x >= 0 and y >= 0 and x < n and y < n and x >= y:
            return True
        return False
    direction = 0
    while number <= (n*n+n)//2:

        nx, ny = x+dx[direction], y+dy[direction]
        if check_range(nx, ny) and answer[nx][ny] == 0:
            answer[nx][ny] = number
            x, y = nx, ny
            number += 1
        else:
            direction = (direction+1) % 3

    ans = []
    for a in answer:
        ans.extend(a)
    return ans


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
