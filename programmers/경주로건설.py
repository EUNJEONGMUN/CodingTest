import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
INF = int(1e9)


def solution(board):
    def check_range(x, y):
        if x >= 0 and y >= 0 and x < len(board) and y < len(board):
            return True
        return False

    distance = [[[100]*4 for _ in range(len(board))]
                for _ in range(len(board))]
    q = []

    heapq.heappush(q, (0, 0, 0, -1))
    distance[0][0] = [0, 0, 0, 0]
    while q:
        cost, x, y, direction = heapq.heappop(q)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if check_range(nx, ny) and board[nx][ny] == 0:
                if i == direction or direction == -1:  # 전과 방향이 같을 때, 혹은 처음일 때
                    if distance[nx][ny][i] >= cost+1:
                        heapq.heappush(q, (cost+1, nx, ny, i))
                        distance[nx][ny][i] = cost+1
                else:
                    if dx[i]*dx[direction]+dy[i]*dy[direction] == 0:  # 반대 방향이 아니라면
                        if distance[nx][ny][i] >= cost+6:
                            heapq.heappush(q, (cost+6, nx, ny, i))
                            distance[nx][ny][i] = cost+6

    return min(distance[-1][-1])*100


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [
      0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [
      1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [
      1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))  # 4500
