from collections import Counter


def solution(a):
    answer = -1
    for num, cnt in Counter(a).most_common():
        count = 0
        idx = 0
        while idx < len(a)-1:
            if (a[idx] != num and a[idx+1] != num) or (a[idx] == a[idx+1]):
                # 공통 요소가 없거나, 같은 요소라면 continue
                idx += 1
                continue
            count += 1
            idx += 2
        if answer < count:
            answer = count
        else:
            break
    return answer*2


print(solution([5, 2, 3, 3, 5, 3]))
print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
print(solution([0, 3, 3, 0, 0, 2, 2, 0, 0, 2]))
print(solution([0, 0, 3, 1, 2, 1, 3, 4, 0, 1, 4]))
print(solution([0, 3, 1, 6, 0, 2, 0, 7, 1, 3, 4, 0, 5, 1, 1]))
