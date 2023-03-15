n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0

for student in students:
    temp = student - b
    answer += 1

    if temp <= 0:
        continue

    if temp % c > 0:
        answer += (temp//c)+1
    else:
        answer += temp//c
print(answer)
