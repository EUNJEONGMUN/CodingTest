# 시간 초과 & 메모리 초과
# n = int(input())
# arr = [False]
# while len(arr) < n:
#     temp = arr[:]
#     for i in temp:
#         arr.append(not i)

#         if len(arr) == n:
#             break

# print(int(arr[n-1]))

n = int(input())
k = 1
while k < n:
    k *= 2
answer = []


def solution(k, idx):
    if k == 1:
        return
    if idx < (k//2):  # 왼쪽에 속하면 reverse 안함
        answer.append(False)
        solution(k//2, idx)
    else:
        answer.append(True)  # 오른쪽에 속하면 reverse
        solution(k//2, idx-(k//2))


solution(k, n-1)

if sum(answer) % 2 == 0:  # reverse True 개수가 짝수개라면, 그대로 0 출력
    print(0)
else:  # reverse True 개수가 홀수개라면, 1 출력
    print(1)
