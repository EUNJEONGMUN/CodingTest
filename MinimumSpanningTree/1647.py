import sys
input = sys.stdin.readline


def find_parent(parent, x):  # 부모 찾기
    if parent[x] != x:  # 자신이 부모가 아니라면
        parent[x] = find_parent(parent, parent[x])  # 다시 부모 찾기
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)  # a의 부모 찾기
    b = find_parent(parent, b)  # b의 부모 찾기

    if a < b:  # 연결해주기
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n+1)]  # 부모 테이블 초기화

edges = [list(map(int, input().split())) for _ in range(m)]
edges = sorted(edges, key=lambda x: x[2])  # 비용 적은 순으로 정렬
result = []
for a, b, cost in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        # 만약 부모가 같다면 -> 사이클 발생
        # 부모가 같지 않다면 -> 사이클 발생하지 않음
        union_parent(parent, a, b)
        result.append(cost)

print(sum(result[:-1]))
