tc = int(input())


def postorder(inorder):
    global visited
    global preorder

    if len(inorder) == 0:  # 비어있으면 리턴
        return
    if len(inorder) == 1:  # 하나라면 방문처리하고 출력후 리턴
        visited[inorder[0]] = True
        print(inorder[0], end=" ")
        return

    root = -1
    for i in preorder:  # preorder의 원소 가 inorder의 어디에 위치해 있는지 찾기
        if visited[i] == False and i in inorder:
            root = i
            visited[i] = True
            break

    idx = inorder.index(root)  # 루트 노드의 인덱스 : idx

    postorder(inorder[:idx])  # 왼쪽 서브 노드
    postorder(inorder[idx+1:])  # 오른쪽 서브 노드
    print(inorder[idx], end=" ")  # 루트노드
    return


for _ in range(tc):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    visited = [False]*(n+1)
    postorder(inorder)
    print()
