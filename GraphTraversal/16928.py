from collections import defaultdict, deque
n, m = map(int, input().split())

ladder = defaultdict(int)
snake = defaultdict(int)
visited = [False]*(101)

for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

q = deque()


def play_dice(x, count):
    global q
    for i in range(1, 7):
        if x+i == 100:
            print(count+1)
            return False

        # 사다리와 뱀이 있는 경우는 무조건 가야하므로 방문 확인을 하지 않음.
        if x+i in ladder:
            visited[ladder[x+i]] = True
            q.append((ladder[x+i], count+1))
        elif x+i in snake:
            visited[snake[x+i]] = True
            q.append((snake[x+i], count+1))
        elif not visited[x+i]:
            visited[x+i] = True
            q.append((x+i, count+1))
    return True


def solution():
    visited[1] = True
    answer = play_dice(1, 0)

    while q:
        if answer:
            x, count = q.popleft()
            answer = play_dice(x, count)
        else:
            break


solution()
