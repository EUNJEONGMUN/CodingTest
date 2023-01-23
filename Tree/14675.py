import sys
input = sys.stdin.readline

n = int(input())
graph = [set() for _ in range(n+1)]
reverse_graph = [set() for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].add(b)
    reverse_graph[b].add(a)


def delete_node(k):
    if len(graph[k]) + len(reverse_graph[k]) > 1:
        return True
    return False


q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        # 정점 지우기
        answer = delete_node(k)
    else:
        answer = True

    if answer:
        print("yes")
    else:
        print("no")
