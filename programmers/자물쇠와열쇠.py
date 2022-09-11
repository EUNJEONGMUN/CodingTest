def check_range(x, y, n):
    if n <= x < n*2 and n <= y < n*2:
        return True
    return False


def is_possible(blank, key, x, y, n):
    cnt = 0
    for i in range(len(key)):
        for j in range(len(key)):
            if check_range(x+i, y+j, n) and key[i][j] == 1:  # 열쇠가 돌기일 때
                if (x+i-n, y+j-n) in blank:  # 자물쇠가 홈이라면
                    cnt += 1  # cnt 증가
                else:  # 그렇지 않다면 바로 false 반환
                    return False
    if cnt == len(blank):
        return True
    else:
        return False


def solution(key, lock):

    n, m = len(lock), len(key)
    blank = []  # 열쇠가 필요한 부분 넣기
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                blank.append((i, j))

    for _ in range(4):
        for x in range(n*3):
            for y in range(n*3):
                if is_possible(blank, key, x, y, n):
                    return True
        key = list(map(list, zip(*key[::-1])))  # 90도 회전하기
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

print(solution([[0, 0], [0, 0]], [[1, 0, 0], [1, 0, 0], [1, 1, 1]]))
print(solution([[1, 0], [0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
