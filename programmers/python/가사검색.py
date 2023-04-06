# def find_pre(query):
#     start = 0
#     end = len(query)-1

#     while start < end:
#         mid = (start+end)//2

#         if query[mid] == '?':
#             start = mid+1
#         else:
#             end = mid
#     return end


# def find_suff(query):
#     start = 0
#     end = len(query)-1

#     while start < end:
#         mid = (start+end)//2

#         if query[mid] == '?':
#             end = mid
#         else:
#             start = mid+1
#     return end


# def solution(words, queries):

#     answer = []
#     for query in queries:
#         mark = ''
#         if query[0] == '?' and query[-1] == '?':
#             mark = "all"
#         elif query[0] == '?':
#             mark = "pre"
#             idx = find_pre(query)
#         else:
#             mark = "suff"
#             idx = find_suff(query)

#         cnt = 0
#         for word in words:
#             if len(query) != len(word):
#                 continue

#             if mark == "all":
#                 cnt += 1
#             elif mark == "pre":
#                 if word[idx:] == query[idx:]:
#                     cnt += 1
#             else:
#                 if word[:idx] == query[:idx]:
#                     cnt += 1
#         answer.append(cnt)

#     return answer

from collections import defaultdict
from bisect import bisect_left, bisect_right


def count(find_list, left, right):
    right_idx = bisect_right(find_list, right)
    left_idx = bisect_left(find_list, left)
    return right_idx-left_idx


def solution(words, queries):
    answer = []
    words_dict = defaultdict(list)
    words_dict_reverse = defaultdict(list)

    for word in words:
        words_dict[len(word)].append(word)
        words_dict_reverse[len(word)].append(str(word[::-1]))

    for key, value in words_dict.items():
        value.sort()

    for key, value in words_dict_reverse.items():
        value.sort()

    for query in queries:
        if query[0] != "?":
            cnt = count(words_dict[len(query)], query.replace(
                "?", "a"), query.replace("?", "z"))

        else:
            cnt = count(words_dict_reverse[len(
                query)], query[::-1].replace("?", "a"), query[::-1].replace("?", "z"))
        answer.append(cnt)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], [
      "fro??", "????o", "fr???", "fro???", "pro?"]))
