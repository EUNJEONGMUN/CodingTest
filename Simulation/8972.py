r, c = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(r)]
moves = list(map(int, list(input().strip())))
INF = int(1e9)
dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

my_x, my_y = 0, 0
robots = set()

for i in range(r):
    for j in range(c):
        if matrix[i][j] == "I":
            my_x, my_y = i, j
        elif matrix[i][j] == "R":
            robots.add((i, j))


def check_range(x, y):
    if x >= 0 and y >= 0 and x < r and y < c:
        return True
    return False


def shortest_distance_point(robots):
    global my_x, my_y
    duplecated = set()
    answer = set()

    for x, y in robots:
        dist = INF
        ans = [0, 0]
        for i in range(1, 10):
            nx, ny = x+dx[i], y+dy[i]
            if check_range(nx, ny) and (abs(nx-my_x)+abs(ny-my_y) < dist):
                dist = abs(nx-my_x)+abs(ny-my_y)
                ans[0], ans[1] = nx, ny
        if tuple(ans) in answer:
            duplecated.add(tuple(ans))
        else:
            answer.add(tuple(ans))

    return answer, duplecated


def start_game():
    global robots, my_x, my_y
    count = 0
    for move in moves:
        count += 1
        my_x += dx[move]
        my_y += dy[move]

        if (my_x, my_y) in robots:
            print("kraj", count)
            return False

        robots, duplecated = shortest_distance_point(robots)

        if (my_x, my_y) in robots:
            print("kraj", count)
            return False

        robots = robots.difference(duplecated)
    return True


if start_game():
    for i in range(r):
        for j in range(c):
            if i == my_x and j == my_y:
                print("I", end="")
            else:
                if (i, j) in robots:
                    print("R", end="")
                else:
                    print(".", end="")
        print()
