def solution(scores):
    if (len(scores) == 1):
        return 1
    wanho = scores[0]
    scores = sorted(scores, key=lambda x: (-x[0], x[1]))
    rank = 1
    min_value = 0
    for score in scores:
        if (wanho[0] < score[0] and wanho[1] < score[1]):
            # 완호가 인센티브를 받을 수 없는 경우
            return -1

        if (min_value <= score[1]):
            # score[0]이 내림차순 정렬되어 있기 때문에
            # score[1]가 min_value보다 같거나 커야 인센티브를 받을 수 있다.
            # 왜냐하면 score[1]이 min_value보다 작다는 것은, 이미 score[0]이 위에 있던 값들보다 작은 값인데, score[1]마저 작은 값이기 때문이다.
            if sum(wanho) < sum(score):
                # 인센티브를 받을 수 있지만 완호의 점수보다 크다면 rank를 하나 증가시킨다.
                rank += 1
            min_value = score[1]
    return rank


print(solution([[1, 5], [1, 6], [3, 2], [3, 2], [2, 1], [1, 6]]))
print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))
print(solution([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]))  # 1
print(solution([[3, 1], [1, 4], [2, 3], [2, 3], [1, 5], [1, 0], [1, 0]]))  # 5
print(solution([[2, 2], [2, 2], [2, 3], [3, 2]]))
print(solution([[5, 5], [11, 2], [10, 1]]))
print(solution([[1, 1], [2, 1], [3, 1], [1, 4], [3, 3], [4, 4]]))
