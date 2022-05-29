import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []  # 전위 순회

while True:
    s = input().strip()
    if s:
        preorder.append(int(s))
    else:
        break

inorder = sorted(preorder)  # 중위 순회 -> 정렬 순


def find(arr):
    global preorder
    if len(arr) == 0:  # arr에 아무 것도 없다면 리턴
        return

    root = preorder.pop(0)  # root - root는 전위 순회 리스트의 0번 인덱스
    index = arr.index(root)  # 루트를 기준으로 왼쪽 오른쪽 나누기
    left = arr[:index]
    right = arr[index+1:]

    find(left)
    find(right)
    print(root)


find(inorder)
