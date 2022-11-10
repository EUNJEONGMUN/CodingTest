from itertools import permutations
from collections import deque

res = 0
card_cnt = 0
table = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check_range(x, y):
    if x >= 0 and y >= 0 and x < 4 and y < 4:
        return True
    return False


def bf(x, y, now_cards, cnt, delete):
    global res
    if len(delete) == card_cnt:
        res = max(res, cnt)
        return

    if len(now_cards) == 2:
        # 현재 뒤집어진 카드가 두 장이라면
        if table[now_cards[0][0]][now_cards[0][1]] == table[now_cards[1][0]][now_cards[1][1]]:
            # 두 장의 카드가 같다면 삭제
            delete.append(now_cards)
            now_cards = []
        else:
            # 두 장의 카드가 다르다면 원상복귀
            now_cards = []
        bf(x, y, now_cards, cnt, delete)

    else:
        # 현재 뒤집어진 카드가 두 장 이하라면

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if check_range(nx, ny):
                # 카드가 있다면 엔터 -> 뒤집음
                if table[nx][ny] != 0 and (x, y) not in delete and (x, y) not in now_cards:
                    now_cards.append((x, y))
                    bf(nx, ny, now_cards, cnt+2, delete)
                else:
                    bf(nx, ny, now_cards, cnt+1, delete)

        new_x, new_y = x, y
        for i in range(4):
            nx = new_x+dx[i]
            ny = new_y+dy[i]
            new_cnt = cnt+1
            while check_range(nx, ny):
                if table[nx][ny] != 0 and (nx, ny) not in delete:
                    now_cards.append((x, y))
                    bf(nx, ny, now_cards, new_cnt+1, delete)

                new_x += dx[i]
                new_y += dy[i]
                new_cnt += 1


def solution(board, r, c):
    global card_cnt
    global table
    table = [b[:] for b in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                continue
            card_cnt += 1

    bf(r, c, [], 0, [])
    return res


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
