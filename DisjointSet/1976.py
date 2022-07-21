import sys
inupt = sys.stdin.readline


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


n = int(input())
m = int(input())

# 여행을 가기만 하면 되니까 -> 같은 부모이면 가능!

table = [list(map(int, input().split())) for _ in range(n)]
trip = list(map(int, input().split()))
parent = [i for i in range(n)]

for i in range(n):
    for j in range(i, n):
        if table[i][j] == 1:
            union_parent(parent, i, j)

# 이 코드가 없으면 왜 오류가 날까?
# find_parent 함수에서 부모 노드로 다 바꾸어주는 게 아닌가??
res = []
for i in trip:
    res.append(find_parent(parent, i-1))

if len(set(parent)) == 1:
    print("YES")
else:
    print("NO")


# 틀림
# import sys
# inupt = sys.stdin.readline


# def find_parent(parent, x):  # 부모 찾기
#     if parent[x] != x:  # 자신이 부모가 아니라면
#         parent[x] = find_parent(parent, parent[x])  # 다시 부모 찾기
#     return parent[x]


# def union_parent(parent, a, b):
#     a = find_parent(parent, a)  # a의 부모 찾기
#     b = find_parent(parent, b)  # b의 부모 찾기

#     if a < b:  # 연결해주기
#         parent[b] = a
#     else:
#         parent[a] = b


# n = int(input())
# m = int(input())

# # 여행을 가기만 하면 되니까 -> 같은 부모이면 가능!

# table = [list(map(int, input().split())) for _ in range(n)]
# trip = list(map(int, input().split()))
# parent = [i for i in range(n)]

# for i in range(n):
#     for j in range(i, n):
#         if table[i][j] == 1:
#             union_parent(parent, i, j)

# base = parent[trip[0]-1]
# for i in range(1, len(trip)):
#     if parent[trip[i]-1] != base:
#         print("NO")
#         break
# else:
#     print("YES")
