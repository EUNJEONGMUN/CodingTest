# 시간초과
#  s = input()
# p = input()


# def solution():
#     left_s, right_s, left_p, right_p = 0, 0, 0, 0

#     while right_s < len(s) and left_s < len(s):
#         if s[right_s] == p[right_p]:
#             right_s += 1
#             right_p += 1
#         else:
#             left_p = 0
#             left_s += 1
#             while left_s < len(s) and s[left_s] != p[left_p]:
#                 left_s += 1

#             right_s = left_s
#             right_p = left_p

#         if right_p == len(p):
#             return 1
#     return 0


# print(solution())
def make_table(pattern):
    table = [0]*len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


def kmp(parent, pattern):
    table = make_table(pattern)
    j = 0
    for i in range(len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j-1]
        if parent[i] == pattern[j]:
            if j == len(pattern)-1:
                return 1
            else:
                j += 1
    return 0


s = input()
p = input()

print(kmp(s, p))
