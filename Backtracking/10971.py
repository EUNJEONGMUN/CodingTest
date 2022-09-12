import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
res = int(1e9)


def bt(arr):
    if len(arr) == n:
        if table[arr[-1]][arr[0]] != 0:
            solution(arr[:]+[arr[0]])
        return
    for i in range(n):
        if i not in arr and (not arr or table[arr[-1]][i] != 0):
            arr.append(i)
            bt(arr)
            arr.pop()


def solution(order):
    global res
    cost = 0
    for i in range(n):
        if table[order[i]][order[i+1]] == 0:
            break
        cost += table[order[i]][order[i+1]]
    else:
        res = min(res, cost)


bt([])
print(res)

# orders 리스트를 만드니까 메모리 초과
# 경우의 수가 만족되면 바로 계산했음.
