# 가장 싼 전공책부터 찾았지만,
# 이렇게 될 경우 여러 권을 사게 된다면,
# 비싼 책 한 권 사는 것보다 돈이 많이 들 수 있다.
# from collections import Counter
# import sys

# input = sys.stdin.readline

# s = input().strip()
# n = int(input())
# books = []
# for _ in range(n):
#     price, title = input().split()
#     books.append([int(price), Counter(title)])
# books.sort()
# res = 0

# for price, title in books:
#     temp = ""
#     mark = False
#     for i in s:
#         if i in title and title[i] > 0:
#             title[i] -= 1
#             if not mark:
#                 mark = True
#             if title[i] == 0:
#                 del title[i]
#         else:
#             temp += i
#     s = temp
#     if mark:
#         res += price

# print(res)


# 시간초과.. 책을 먼저 골라야하나?
# from collections import defaultdict
# from collections import Counter
# import sys
# input = sys.stdin.readline

# s = input().strip()
# n = int(input())
# INF = int(1e9)

# books = []
# books_list = {}
# answer = INF

# for _ in range(n):
#     price, title = input().split()
#     books.append([Counter(title), title])
#     books_list[title] = int(price)


# def calcurate(book):
#     temp = 0
#     for name, quantity in book.items():
#         if quantity > 0:
#             temp += books_list[name]
#     return temp


# def solution(res, cnt):
#     global answer
#     if len(s) == cnt:
#         if sum(res.values()) == cnt:
#             answer = min(answer, calcurate(res))
#         return

#     for i in range(cnt, len(s)):
#         for title, name in books:
#             if s[i] in title and title[s[i]] > 0:
#                 print("s[", i, "]", s[i], name)
#                 res[name] += 1
#                 title[s[i]] -= 1
#                 solution(res, i+1)
#                 res[name] -= 1
#                 title[s[i]] += 1


# solution(defaultdict(int), 0)
# if answer == INF:
#     print(-1)
# else:
#     print(answer)

from itertools import combinations
from collections import Counter
import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())
INF = int(1e9)
answer = INF
books = [list(map(str, input().split())) for _ in range(n)]


def solution(s, choice):
    total = 0
    for price, name in choice:
        alpha = Counter(name)  # 알파벳 개수
        remain = ""
        is_used = False  # 사용 여부
        for i in s:  # s 돌면서 탐색
            if i in alpha and alpha[i] > 0:  # 알파벳이 남아있다면
                alpha[i] -= 1  # 감소
                is_used = True
            else:
                remain += i

        s = remain
        if is_used:  # 사용했다면
            total += int(price)  # 가격 추가

    if s != "":
        return INF
    return total


choices = []
for i in range(1, n+1):
    choices.extend(combinations(books, i))


for choice in choices:
    answer = min(answer, solution(s, choice))

if answer == INF:
    print(-1)
else:
    print(answer)
