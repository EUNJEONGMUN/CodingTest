def turn(arr):
    return list(map(list, zip(*arr[::-1])))  # 시계방향 90도


def solution(key, lock):
    n, m = len(key), len(key[0])

    # 칸 끼리 더해서 모두 1이 되면!! -> 성공
    # 하나라도 0이나 2이상이 있다면 -> 실패

    for _ in range(3):

        for key_x in range(n):
            for key_y in range(m):
                mark = True
                for i in range(n):
                    for j in range(n):
                        if key_x+i < n and key_y+j < m:
                            print(i, j, key_x+i, key_y+j)
                #             if lock[i][j]+key[key_x+i][key_y+j] != 1:
                #                 mark = False
                #                 break
                #         else:
                #             if lock[i][j] != 1:
                #                 mark = False

                #     if not mark:
                #         break
                # if mark:
                #     return True

        key = turn(key)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


for key_x in range(n):
    for key_y in range(n):
        for lock_x in range(n):
            for lock_y in range(m):
                if key_y
