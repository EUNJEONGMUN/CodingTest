# from collections import defaultdict


# def remove(x):  # x 노드의 자식들 삭제
#     if x in tree:
#         for i in tree[x]:
#             remove(i)
#         del(tree[x])


# n = int(input())
# graph = list(map(int, input().split()))
# tree = defaultdict(list)  # key: 부모, value:자식
# for i in range(n):
#     tree[graph[i]].append(i)

# delete = int(input())
# remove(delete)
# cnt = 0

# tree[graph[delete]].remove(delete)

# for key, value in tree.items():
#     if key == -1:
#         continue
#     for i in value:
#         if i not in tree and i != delete:
#             cnt += 1

# print(cnt)


n = int(input())
arr = list(map(int, input().split()))
delete = int(input())
tree = [[] for _ in range(n)]
start = 0
for i in range(len(arr)):
    if arr[i] == -1:
        start = i
    else:
        tree[arr[i]].append(i)  # 부모노드 -> 자식노드

cnt = 0


def dfs(v):
    global cnt
    if v == delete:  # 노드가 삭제될 노드이면 return
        return
    if len(tree[v]) == 0:  # 자식노드가 없다면
        cnt += 1  # cnt+=1
    elif len(tree[v]) == 1 and delete in tree[v]:  # 자식 노드가 1개이지만, 삭제 된 노드이면 cnt+=1
        cnt += 1

    else:
        for i in tree[v]:  # 삭제 되지 않은 노드 dfs 탐색
            if i != delete:
                dfs(i)


dfs(start)
print(cnt)
