import sys
input = sys.stdin.readline

n = int(input())
start = [input().strip() for _ in range(n)]
end = [input().strip() for _ in range(n)]

start_point = 0
end_point = 0

passing = set()

while start_point < n and end_point < n:
    if start[start_point] == end[end_point]:
        start_point += 1
        end_point += 1
    else:
        if start[start_point] in passing:  # start[start_point]가 이미 추월한 차일 때
            start_point += 1
        else:
            passing.add(end[end_point])
            end_point += 1

print(len(passing))
