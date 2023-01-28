import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    grade = [list(map(int, input().split())) for _ in range(n)]
    grade.sort()
    count = 1
    upper_grade = grade[0][1]

    for i in range(1, n):
        if grade[i][1] < upper_grade:
            count += 1
            upper_grade = grade[i][1]
    print(count)
