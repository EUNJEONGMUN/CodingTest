import sys
input = sys.stdin.readline


def calculate(room_idx, money):
    if room_info[room_idx][0] == "E":
        return money
    elif room_info[room_idx][0] == "L":
        if money >= room_info[room_idx][1]:
            return money
        else:
            return room_info[room_idx][1]
    elif room_info[room_idx][0] == "T":
        return money-room_info[room_idx][1]


def dfs(node, money):
    global flag
    if node == n:
        flag = True
        return
    for next_room in graph[node]:
        if not visited[next_room] and calculate(next_room, money) >= 0:
            visited[next_room] = True
            dfs(next_room, calculate(next_room, money))
            if flag:
                break
            visited[next_room] = False


while True:
    n = int(input())
    if n == 0:
        break

    room_info = [tuple()]
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    for i in range(1, n+1):
        command = list(input().strip().split())
        room_info.append((command[0], int(command[1])))
        for next_room in command[2:-1]:
            graph[i].append(int(next_room))

    flag = False
    dfs(1, 0)

    if flag:
        print("Yes")
    else:
        print("No")
