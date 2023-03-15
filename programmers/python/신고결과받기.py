from collections import defaultdict
cnt_dict = defaultdict(int)
name_dict = defaultdict(set)


def solution(id_list, report, k):
    for r in report:
        p1, p2 = r.split()
        if p2 not in name_dict[p1]:
            cnt_dict[p2] += 1
        name_dict[p1].add(p2)
    res = []
    for id in id_list:
        cnt = 0
        for name in name_dict[id]:
            if cnt_dict[name] >= k:
                cnt += 1
        res.append(cnt)

    return res


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con",
      "ryan con", "ryan con", "ryan con"], 3))
