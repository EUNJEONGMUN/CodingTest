from collections import deque

INF = int(1e9)
tc = int(input())
for _ in range(tc):
    n = int(input())  # 편의점 개수
    store = [list(map(int, input().split())) for _ in range(n+2)]
    visited = [False]*(n+2)  # 방문노드

    # 시작 노드 초기화
    q = deque([0])
    visited[0] = True

    def calculate(x, y):  # 거리 계산 함수
        return abs(store[x][0]-store[y][0])+abs(store[x][1]-store[y][1])

    while q:
        now = q.popleft()

        for i in range(n+2):
            if not visited[i]:
                if calculate(now, i) <= 1000:
                    # 거리가 1000이하일 때만 방문할 수 있음
                    visited[i] = True
                    q.append(i)

    if visited[-1]:
        print("happy")
    else:
        print("sad")
