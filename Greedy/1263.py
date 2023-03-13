import sys
input = sys.stdin.readline

n = int(input())
works = [tuple(map(int, input().split())) for _ in range(n)]
works.sort(key=lambda x: (-x[1], x[0]))


def solution(now):
    for duration, deadline in works:
        if deadline < now:
            now = deadline
        if 0 <= now - duration <= deadline:
            now -= duration
        else:
            return -1
    return now


solution(works[0][1])
