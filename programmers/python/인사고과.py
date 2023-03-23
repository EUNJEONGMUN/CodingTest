def solution(scores):
    if (len(scores) == 1):
        return 1
    wanho = scores[0]
    scores = sorted(scores, key=lambda x: (-x[0], x[1]))
    rank = 1
    min_value = 0
    for score in scores:
        if (wanho[0] < score[0] and wanho[1] < score[1]):
            return -1

        if (min_value <= score[1]):
            if sum(wanho) < sum(score):
                rank += 1
            min_value = score[1]
    return rank


print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))
print(solution([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]))  # 1
print(solution([[3, 1], [1, 4], [2, 3], [2, 3], [1, 5], [1, 0], [1, 0]]))  # 5
print(solution([[2, 2], [2, 2], [2, 3], [3, 2]]))
print(solution([[5, 5], [11, 2], [10, 1]]))
print(solution([[1, 1], [2, 1], [3, 1], [1, 4], [3, 3], [4, 4]]))
