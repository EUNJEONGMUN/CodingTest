# import sys
# from collections import defaultdict
# from bisect import bisect_right

# input = sys.stdin.readline

# n, k = map(int, input().split())
# name_length = defaultdict(list)

# for i in range(n):
#     name = input()
#     name_length[len(name)].append(i)


# def count_best_friends(students, idx):
#     return bisect_right(students, idx+k)


# answer = 0
# for students in name_length.values():
#     for i, student in enumerate(students):
#         answer += count_best_friends(students[i+1:], student)

# print(answer)

import sys

input = sys.stdin.readline
NAME_LENGTH_MAX = 20

n, k = map(int, input().split())
name_length = [0]*(NAME_LENGTH_MAX+1)
students = [0]*n

answer = 0
for i in range(n):
    students[i] = len(input().rstrip())
    if i > k:  # k 보다 크기가 커지면 앞에 있는 학생들 하나씩 제거함
        # 슬라이딩 박스 안에서 맨 앞에 있는 학생의 이름 길이에 해당하는 수 하나 감소
        name_length[students[i-k-1]] -= 1
    # 슬라이딩 박스 안에 있는 같은 길이의 이름을 가진 학생들의 수를 더함
    answer += name_length[students[i]]
    name_length[students[i]] += 1

print(answer)
