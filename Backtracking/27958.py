import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
initial = list(list(map(int, input().split())) for _ in range(n))
shoot = list(map(int, input().split()))

present = [i[:] for i in initial]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


answer = 0


def solution(point, cnt):
    global answer
    if cnt == k:
        answer = max(answer, point)
        return

    for x in range(n):
        if sum(present[x]) == 0:
            continue
        for y in range(n):
            if present[x][y] != 0:
                initial_power = initial[x][y]
                present_power = present[x][y]
                if present[x][y] >= 10:
                    initial[x][y] = 0
                    present[x][y] = 0
                    solution(point+initial_power, cnt+1)
                    initial[x][y] = initial_power
                    present[x][y] = present_power
                else:
                    if present[x][y] > shoot[cnt]:
                        present[x][y] -= shoot[cnt]
                        solution(point, cnt+1)
                        present[x][y] += shoot[cnt]
                    else:
                        div = initial_power//4
                        initial[x][y] = 0
                        present[x][y] = 0
                        save_position = []
                        if div > 0:
                            for s in range(4):
                                nx, ny = x+dx[s], y+dy[s]
                                if check_range(nx, ny) and present[nx][ny] == 0:
                                    present[nx][ny] = div
                                    initial[nx][ny] = div
                                    save_position.append((nx, ny))
                        solution(point+initial_power, cnt+1)
                        present[x][y] = present_power
                        initial[x][y] = initial_power
                        for a, b in save_position:
                            present[a][b] = 0
                            initial[a][b] = 0
                break


solution(0, 0)
print(answer)
