import sys
input = sys.stdin.readline
N, M = map(int, input().split())  # N: 파티장의 크기, M: 서비스를 요청한 손님의 수

graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k]+graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
