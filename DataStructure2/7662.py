import heapq
import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    min_heapq = []
    max_heapq = []
    check = [False]*n

    for i in range(n):
        command = list(input().strip().split())

        if command[0] == "I":
            heapq.heappush(min_heapq, (int(command[1]), i))
            heapq.heappush(max_heapq, (-int(command[1]), i))

        elif command[0] == "D":
            if command[1] == "-1" and min_heapq:
                while min_heapq:
                    elem, idx = heapq.heappop(min_heapq)
                    if not check[idx]:
                        check[idx] = True
                        break
            else:
                while max_heapq:
                    elem, idx = heapq.heappop(max_heapq)
                    if not check[idx]:
                        check[idx] = True
                        break
    min_value = sys.maxsize
    max_value = -sys.maxsize

    while min_heapq:
        elem, idx = heapq.heappop(min_heapq)
        if not check[idx]:
            min_value = elem
            break
    while max_heapq:
        elem, idx = heapq.heappop(max_heapq)
        if not check[idx]:
            max_value = elem
            break

    if min_value == sys.maxsize and max_value == -sys.maxsize:
        print("EMPTY")
    else:
        print(-max_value, min_value)
