import sys
inupt = sys.stdin.readline


def find_parent(x):  # 부모 찾기
    if parent[x] != x:  # 자신이 부모가 아니라면
        parent[x] = find_parent(parent[x])  # 다시 부모 찾기
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)  # a의 부모 찾기
    b = find_parent(b)  # b의 부모 찾기

    if a < b:  # 연결해주기
        parent[b] = a
        cnt[a] += cnt[b]
        cnt[b] = 0

    elif a > b:
        parent[a] = b
        cnt[b] += cnt[a]
        cnt[a] = 0

    # 서로 루트 노드가 같을 때는 pass


n = int(input())
parent = [i for i in range(1000001)]
cnt = [1 for i in range(1000001)]
query = [list(map(str, input().strip().split())) for _ in range(n)]
for temp in query:

    if temp[0] == "I":
        union_parent(int(temp[1]), int(temp[2]))
    else:
        p = find_parent(int(temp[1]))
        print(cnt[p])
