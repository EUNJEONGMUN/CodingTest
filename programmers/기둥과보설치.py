def check_range(n, x, y):
    if x >= 0 and y >= 0 and x <= n and y <= n:
        return True
    return False


def solution(n, build_frame):
    table = [[[False]*2 for i in range(n+1)] for j in range(n+1)]
    for y, x, a, b in build_frame:
        if a == 0:
            if b == 0:
                # 기둥 삭제
                mark = True
                # 바로 위가 보일때
                if table[x][y+1][1]:
                    if check_range(n, x+1, y-1) and table[x+1][y-1][1] and (table[x+1][y-1][0] or (check_range(n, x+1, y-2) and table[x+1][y-2][1])):
                        mark = True
                    else:
                        mark = False
                    if mark and check_range(n, x+1, y+1) and table[x+1][y+1][1] and (table[x+1][y+1][0] or (check_range(n, x+1, y+2) and table[x+1][y+2][1])):
                        mark = True
                    else:
                        mark = False

                if table[x][y+1][0]:
                    # 바로 위가 기둥일 때
                    mark = False
                if mark:
                    table[x][y][0] = False
                    table[x+1][y][0] = False
            else:
                # 기둥 설치
                if x == 0 or table[x][y][0] or table[x][y][1]:
                    table[x][y][0] = True
                    table[x+1][y][0] = True
        else:
            if b == 0:
                # 보 삭제
                # 왼쪽에 보가 있을 때
                mark = False
                if y == 0 or not table[x][y-1][1] or (table[x][y-1][1] and (table[x][y][0] or table[x][y-1][0])):
                    mark = True
                else:
                    mark = False
                # 오론쪽에 보가 있을 때
                if mark and not table[x][y+1][1] or (table[x][y+1][1] and table[x][y][0] or table[x][y+1][0]):
                    mark = True
                else:
                    mark = False

                if mark:
                    table[x][y][1] = False
                    table[x][y+1][1] = False

            else:
                # 보 설치
                if table[x][y][0] or table[x][y+1][0] or (table[x][y][1] and table[x][y+1][1]):
                    table[x][y][1] = True
                    table[x][y+1][1] = True

    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if j == n and i == n:
                continue
            elif i == n:
                if table[i][j][1] and table[i][j+1][1]:
                    answer.append([j, i, 1])
            elif j == n:
                if table[i][j][0] and table[i+1][j][0]:
                    answer.append([j, i, 0])
            else:
                if table[i][j][0] and table[i+1][j][0]:
                    answer.append([j, i, 0])
                elif table[i][j][1] and table[i][j+1][1]:
                    answer.append([j, i, 1])
    answer.sort()

    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
      2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
