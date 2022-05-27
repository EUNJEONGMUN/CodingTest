def preorder(graph, node):  # 전위 순회 MLR
    if node != ".":
        print(node, end="")
        preorder(graph, graph[node][0])
        preorder(graph, graph[node][1])


def inorder(graph, node):  # 중위 순회 LMR
    if node != ".":
        inorder(graph, graph[node][0])
        print(node, end="")
        inorder(graph, graph[node][1])


def postorder(graph, node):  # 후위 순회 LRM
    if node != ".":
        postorder(graph, graph[node][0])
        postorder(graph, graph[node][1])
        print(node, end="")


n = int(input())

graph = {}

for _ in range(n):
    a, b, c = map(str, input().split())
    graph[a] = [b, c]

preorder(graph, "A")
print()
inorder(graph, "A")
print()
postorder(graph, "A")
