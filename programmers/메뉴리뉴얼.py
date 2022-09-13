# from collections import defaultdict
# from itertools import combinations


# def solution(orders, course):
#     combi = defaultdict(int)
#     for order in orders:
#         o = sorted(order)
#         for i in range(2, len(order)+1):
#             for elem in list(combinations(o, i)):
#                 combi[elem] += 1
#     res = []
#     combi = sorted(combi.items(), key=lambda x: (len(x[0]), -x[1]))

#     max_dict = defaultdict(int)
#     for key, value in combi:
#         if value < 2:
#             continue
#         if len(key) in course:
#             if len(key) not in max_dict:
#                 max_dict[len(key)] = value
#                 res.append("".join(key))
#             else:
#                 if value >= max_dict[len(key)]:
#                     res.append("".join(key))

#     return sorted(res)

from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    combi = defaultdict(int)

    for order in orders:
        o = sorted(order)
        for size in course:
            for elem in list(combinations(o, size)):
                combi[elem] += 1
    res = []
    combi = sorted(combi.items(), key=lambda x: (len(x[0]), -x[1]))

    max_dict = defaultdict(int)
    for key, value in combi:
        if value < 2:
            continue
        if len(key) in course:
            if len(key) not in max_dict:
                max_dict[len(key)] = value
                res.append("".join(key))
            else:
                if value >= max_dict[len(key)]:
                    res.append("".join(key))

    return sorted(res)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
