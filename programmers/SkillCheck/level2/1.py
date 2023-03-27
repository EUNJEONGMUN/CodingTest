from collections import defaultdict


# def solution(info, queries):
#     answer = []
#     database = defaultdict(set)
#     grade = []
#     for idx, elem in enumerate(info):
#         split_info = elem.split()
#         for e in split_info[:-1]:
#             database[e].add(idx)
#         grade.append(int(split_info[-1]))

#     for query in queries:
#         ans = 0
#         split_query = query.split()
#         pick = set(list(range(len(info))))
#         for q in split_query[:-1]:
#             if q == '-' or q == 'and':
#                 continue
#             pick = pick.intersection(database[q])
#         for people in pick:
#             if grade[people] >= int(split_query[-1]):
#                 ans += 1
#         answer.append(ans)
#     return answer

def solution(info, queries):
    answer = []
    database = dict()
    for language in ["cpp", "java", "python"]:
        for part in ["backend", "frontend"]:
            for level in ["junior", "senior"]:
                for food in ["chicken", "prizza"]:
                    database[(language, part, level, food)] = set()
    database = defaultdict(set)
    grade = []
    for idx, elem in enumerate(info):
        split_info = elem.split()
        database[tuple(split_info[:-1])].add(idx)
        grade.append(int(split_info[-1]))

    for query in queries:
        ans = 0
        split_query = query.split()
        pick = set()
        con = set()
        for q in split_query[:-1]:
            if q == '-' or q == "and":
                continue
            con.add(q)
        for key, value in database.items():
            if not con.difference(set(key)):
                pick.update(value)

        for people in pick:
            if grade[people] >= int(split_query[-1]):
                ans += 1
        answer.append(ans)
    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
