# tc = int(input())


# def postorder(inorder):
#     global visited
#     global preorder

#     if len(inorder) == 0:  # 비어있으면 리턴
#         return
#     if len(inorder) == 1:  # 하나라면 방문처리하고 출력후 리턴
#         visited[inorder[0]] = True
#         print(inorder[0], end=" ")
#         return

#     root = -1
#     for i in preorder:  # preorder의 원소 가 inorder의 어디에 위치해 있는지 찾기
#         if visited[i] == False and i in inorder:
#             root = i
#             visited[i] = True
#             break

#     idx = inorder.index(root)  # 루트 노드의 인덱스 : idx

#     postorder(inorder[:idx])  # 왼쪽 서브 노드
#     postorder(inorder[idx+1:])  # 오른쪽 서브 노드
#     print(inorder[idx], end=" ")  # 루트노드
#     return


# for _ in range(tc):
#     n = int(input())
#     preorder = list(map(int, input().split()))
#     inorder = list(map(int, input().split()))
#     visited = [False]*(n+1)
#     postorder(inorder)
#     print()


tc = int(input())


def postorder(preorder, inorder):

    if len(preorder) == 1:
        # preorder의 길이가 1이라면 하나 남은 노드 출력
        print(preorder[0], end=" ")
        return
    elif len(preorder) == 0:
        # preorder의 길이가 0이라면 그냥 리턴
        return

    root_node = preorder[0]  # 루트 노드
    root_idx = inorder.index(root_node)  # inorder 리스트에서 루트 노드위 위치 찾기

    left_sub = inorder[:root_idx]  # 왼쪽서브 트리
    right_sub = inorder[root_idx+1:]  # 오르쪽서브 트리

    # preorder을 자르는 기준은
    # 루트 노드를 제외하기 때문에 1부터 시작하고
    # 서브 노드의 길이와 같을 것이다.
    postorder(preorder[1:1+len(left_sub)], left_sub)
    postorder(preorder[1+len(left_sub):], right_sub)
    print(root_node, end=" ")


for _ in range(tc):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder(preorder, inorder)
    print()
