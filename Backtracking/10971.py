import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
res = int(1e9)


def bt(arr):
    if len(arr) == n:  # arr에 n개의 도시가 다 들어왔다면
        if table[arr[-1]][arr[0]] != 0:  # arr의 맨 마지막 도시에서 arr의 처음 도시로 돌아갈 수 있을 때
            solution(arr[:]+[arr[0]])  # cost 계산하기
        return
    for i in range(n):  # i부터 n까지 탐색
        if i not in arr and (not arr or table[arr[-1]][i] != 0):
            # i를 이전에 방문하지 않았고,
            # arr이 비어있거나, arr의 마지막 도시에서 i도시로 이동할 수 있다면
            arr.append(i)  # 경로에 추가
            bt(arr)  # 탐색
            arr.pop()  # 경로에서 제거


def solution(order):
    global res
    cost = 0
    for i in range(n):
        # cost 계산
        cost += table[order[i]][order[i+1]]
    res = min(res, cost)  # 갱신


bt([])
print(res)

# orders 리스트를 만드니까 메모리 초과
# 경우의 수가 만족되면 바로 계산했음.
