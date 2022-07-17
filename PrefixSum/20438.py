# 틀렸습니다
# for문의 위치 때문에 틀림
# import sys
# input = sys.stdin.readline

# n, k, q, m = map(int, input().split())
# sleep = list(map(int, input().split()))
# qr_code = list(map(int, input().split()))
# students = [0]*(n+3)

# for s in sleep:
#     students[s] = -1

# for q in qr_code:
#     for i in range(q, n+3, q):
#         if students[i] == -1:
#             continue
#         else:
#             if students[i] == 0:
#                 students[i] = 1

# for i in range(3, n+3):
#     if students[i] == 1:
#         students[i] += students[i-1]
#     else:
#         students[i] = students[i-1]

# for _ in range(m):
#     s, e = map(int, input().split())
#     print((e-s+1) - (students[e]-students[s-1]))


import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = list(map(int, input().split()))
qr_code = list(map(int, input().split()))
students = [0]*(n+3)

for s in sleep:
    students[s] = -1

for q in qr_code:
    if students[q] == -1:
        continue
    for i in range(q, n+3, q):
        if students[i] == 0:
            students[i] = 1

for i in range(3, n+3):
    if students[i] == 1:
        students[i] += students[i-1]
    else:
        students[i] = students[i-1]

for _ in range(m):
    s, e = map(int, input().split())
    print((e-s+1) - (students[e]-students[s-1]))
